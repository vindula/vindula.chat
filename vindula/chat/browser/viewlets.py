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
        chooser = getUtility(ICacheChooser)
        cache = chooser('vindula.chat.ijabconf')
        settings = xmpp_users.getSettings()
        
        try:
            ap = getSite()['control-panel-objects']['vindula_chat_settings']
            modified = str(ap.bobobase_modification_time())    
        except:
            modified = None
        
        #iJabConf = cache.get(modified, None)
        iJabConf = None
        if iJabConf is None:
            iJabConf = {}
            iJabConf['client_type'] = 'xmpp'
            iJabConf['app_type'] = 'bar'
            iJabConf['theme'] = 'standard'
            iJabConf['debug'] = False
            iJabConf['avatar_url'] = '%s/portraits-user?user={username}' %(self.context.portal_url())
            iJabConf['enable_roster_manage'] = True
            iJabConf['enable_talkto_stranger'] =  True
            iJabConf['expand_bar_default'] =  False 
            iJabConf['enable_login_dialog'] = False
            iJabConf['hide_online_group'] = False
            iJabConf['hide_poweredby'] = True
            
            iJabConf['disable_option_setting'] = True
            iJabConf['disable_msg_browser_prompt'] =  False
            iJabConf['disable_toolbox'] =  False 
            
            iJabConf['xmpp'] = {
                'domain': settings.get('xmpp_domain', '' ),
                'http_bind': self.context.portal_url() +'/http-bind/',
                'host': settings.get('xmpp_host',''),
                'port': 5222,
                'server_type': 'openfire',
                'auto_login': True,
                'none_roster': False,
                'get_roster_delay': True,
                'username_cookie_field': '__ijab_name',
                'token_cookie_field': '__ijab_password',
                'anonymous_prefix': '',
                'max_reconnect': 3,
                'enable_muc': True,
                'muc_servernode': '',
                'vcard_search_servernode': '',
                'gateways': []
                }
            
            iJabConf['tools'] = [
                                 {'href':"%s/change-chatpasswd" % self.context.portal_url(),
                                  'target':"_blank",
                                  'img':"%s/++resource++vindula.chat/img/changepasswd.png" % self.context.portal_url(),
                                  'text':"Alterar senha"
                                  }
                                 ]
            iJabConf['shortcuts'] = []
            iJabConf['ijabcometd'] = {}
            
            iJabConf = cjson.encode( iJabConf )
            
            # cache
            cache[modified] = iJabConf
        
        #Configuração Ejaber
        self.iJabConf = iJabConf
        
        #URL do portal        
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        self.site_url = portal_state.portal_url()
    
        #User Senha Logado
        altenticado = self.context.portal_membership.getAuthenticatedMember()
        self.user = altenticado.getUserName()
        self.password = xmpp_users.getUserPassword(self.user)
