# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalFooter
from vindula.chat.interfaces import IXMPPUsers 
from zope.component import getUtility
from zope.app.component.hooks import getSite


# Viewlet for portal logo top
class ChatViewlet(grok.Viewlet):
    grok.context(Interface)
    grok.name('vindula.chat.listUsers') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter) 
    
    
    def enableChat(self):
        xmpp_users = getUtility(IXMPPUsers)
        settings = xmpp_users.getSettings()
        return settings.get('enable_chat',None)


# View congif chat
class ChatConfigView(grok.View):
    grok.context(Interface) 
    grok.name('vindula-chat-config') 
    grok.require('zope2.View')
    
    def enableChat(self):
        xmpp_users = getUtility(IXMPPUsers)
        settings = xmpp_users.getSettings()
        altenticado = getSite().portal_membership.isAnonymousUser()
        
        if settings.get('enable_chat',False) and altenticado == 0:
            return True 
        else:
            return False

    def render(self):
        return 'vindula-chat-config'
        
