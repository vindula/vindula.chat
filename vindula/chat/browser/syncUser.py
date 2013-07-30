# coding: utf-8
from five import grok
from zope.interface import Interface

from vindula.chat.interfaces import IXMPPUsers
from zope.app.component.hooks import getSite
from zope.component import getUtility
import logging

import urllib
logger = logging.getLogger('vindula.chat')

from vindula.myvindula.models.instance_funcdetail import ModelsInstanceFuncdetails

class SyncUser(grok.View):
    grok.context(Interface)
    grok.require('zope2.View')
    grok.name('sync-user-openfire')

    def render(self):
        return 'usuarios sinconizados'

    def update(self):
        xmpp_users = getUtility(IXMPPUsers)
        host = getSite().portal_url() + '/http-user'
        key = xmpp_users.getSettings().get('key_http_user')

        users = ModelsInstanceFuncdetails().get_allFuncDetails()

        for item in users:
            user = item.get('username')
            name = item.get('name') or item.get('username')
    
            url = '%s/plugins/userService/userservice?type=update&secret=%s&username=%s&name=%s' %(host,key,user, name)
            try:   
                page = urllib.urlopen(url)
                result = page.read()
            except:
               continue
        
            if 'error' in result or page.getcode() != 200:
                logger.info("%s - Error - %s - %s"% (user, result, page.getcode()))
            else:
                logger.info("%s - OK -"% (user))
