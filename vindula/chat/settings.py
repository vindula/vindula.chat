# -*- coding: utf-8 -*-
import logging

from plone.app.registry.browser.controlpanel import RegistryEditForm, ControlPanelFormWrapper
from plone.registry.interfaces import IRegistry
from twisted.words.protocols.jabber.jid import JID
from zope.component import getUtility
from zope.interface import implements
from plone.z3cform import layout
from zope.app.component.hooks import getSite 

from vindula.chat.utils.models import ModelsUserOpenFire
from vindula.chat.interfaces import IXMPPPasswordStorage, IXMPPUsers, IVindulaChatConnector

logger = logging.getLogger('vindula.chat')


class XMPPUsers(object):

    implements(IXMPPUsers)

    def getUserJID(self, user_id):
        registry = self.getSettings()
        xmpp_domain = registry['xmpp_domain']
        return JID("%s@%s" % (user_id, xmpp_domain))

    def getUserPassword(self, user_id):
        #pass_storage = getUtility(IXMPPPasswordStorage)
        try:user = unicode(user_id,'utf-8')
        except:user = user_id
        
        pass_storage = ModelsUserOpenFire().get_UserOpenFire_by_username(user)
        if pass_storage:
            return pass_storage.password
        else:
            return None
    
    def getSettings(self):
        try:
            registry = getSite()['control-panel-objects']['vindula_chat_settings']
                
            vars = {'enable_chat':registry.enable_chat,
                    'xmpp_domain':registry.xmpp_domain,
                    'admin_jid':registry.admin_jid,
                    'admin_pwd':registry.admin_pwd,
                    
                    'conference_jid':registry.conference_jid,
                    'pubsub_jid':registry.pubsub_jid,
                    
                    'key_http_user':registry.key_http_user,
                    }
        except:        
            vars = {'enable_chat':False,
                    'xmpp_domain':'vindula.com' ,
                    'admin_jid':'admin@vindula.com',
                    'admin_pwd':'temp123',
                    'conference_jid':'secret',
                    'pubsub_jid':'plone.vindula.com',
                    'key_http_user':'NYIqhNdx'
                    }
        
        return vars