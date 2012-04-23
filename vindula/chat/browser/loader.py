# -*- coding: utf-8 -*-
import logging
import json

from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getUtility, queryUtility

from jarn.xmpp.twisted.client import randomResource
from jarn.xmpp.twisted.httpb import BOSHClient

from vindula.chat.interfaces import IAdminClient, IXMPPUsers

logger = logging.getLogger('vindula.chat')


class XMPPLoader(BrowserView):
    """
    """

    @property
    def available(self):
        self._available = True
        client = queryUtility(IAdminClient)
        if client is None:
            self._available = False
            return

        pm = getToolByName(self.context, 'portal_membership')
        self.user_id = pm.getAuthenticatedMember().getId()
        if self.user_id is None:
            self._available = False
            return
        
        self.xmpp_users = getUtility(IXMPPUsers)
        self.jid = self.xmpp_users.getUserJID(self.user_id)
        self.jpassword = self.xmpp_users.getUserPassword(self.user_id)
        self.jid.resource = randomResource()
        if self.jpassword is None:
            self._available = False
            return

        try:
            self.pubsub_jid = self.xmpp_users.getSettings().get('conference_jid')
        except KeyError:
            self._available = False

        return self._available

    @property
    def bosh(self):
        return getToolByName(self.context, 'portal_url')() + '/http-bind'

    def prebind(self):
        b_client = BOSHClient(self.jid, self.jpassword, self.bosh)
        if b_client.startSession():
            return b_client.rid, b_client.sid
        return ('', '')

    def __call__(self):
        bosh_credentials = {}
        if self.available: 
            rid, sid = self.prebind()
            if rid and sid:
                logger.info('Pre-binded %s' % self.jid.full())
                bosh_credentials = {
                    'BOSH_SERVICE': self.bosh,
                    'rid': int(rid),
                    'sid': sid,
                    'jid': self.jid.full(),
                    'pubsub_jid': self.pubsub_jid}
            else:
                logger.warning('Unable to pre-bind %s' % self.jid)
        else:
            logger.warning('Not avaliable %s in server XMPP' % self.jid)
        
        response = self.request.response
        response.setHeader('content-type', 'application/json')
        response.setHeader('Cache-Control', 'max-age=0, must-revalidate, private')
        response.setBody(json.dumps(bosh_credentials))
        return response
