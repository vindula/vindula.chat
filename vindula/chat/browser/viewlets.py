# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalFooter
from vindula.chat.interfaces import IXMPPUsers 
from zope.app.component.hooks import getSite
from zope.component import getUtility, getMultiAdapter
from plone.memoize.interfaces import ICacheChooser
from Acquisition import aq_inner, aq_base

import urllib, cjson

# Viewlet for portal logo top
class ChatViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.name('vindula.chat.listUsers') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter) 
    ''' A viewlet show ijab bar. '''
    
    def settingsChat(self):
        xmpp_users = getUtility(IXMPPUsers)
        settings = xmpp_users.getSettings()
        return settings
    
       
    def enableChat(self):
        xmpp_users = getUtility(IXMPPUsers)
        settings = xmpp_users.getSettings()
        altenticado = getSite().portal_membership.isAnonymousUser()
        
        if settings.get('enable_chat',False) and altenticado == 0:
            return True 
        else:
            return False        
        
    
    def update(self):
        xmpp_users = getUtility(IXMPPUsers)
        #chooser = getUtility(ICacheChooser)
        #cache = chooser('vindula.chat.ijabconf')
        
        settings = xmpp_users.getSettings()

        #URL do portal        
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        
        self.site_url = portal_state.portal_url()
    
        #User Senha Logado
        altenticado = self.context.portal_membership.getAuthenticatedMember()
        
        fullname = altenticado.getProperty('fullname')
        if not fullname:
            fullname = altenticado.getUserName()
            
        self.nickname = fullname
        self.user = altenticado.getUserName()
        self.password = xmpp_users.getUserPassword(self.user)
