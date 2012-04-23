# -*- coding: utf-8 -*-
import logging

from plone.app.registry.browser.controlpanel import RegistryEditForm, ControlPanelFormWrapper
from plone.registry.interfaces import IRegistry
from twisted.words.protocols.jabber.jid import JID
from zope.component import getUtility
from zope.interface import implements
from plone.z3cform import layout

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
        registry = getUtility(IRegistry)
        vars = {'enable_chat':registry.records.get('vindula.chat.interfaces.IVindulaChatConnector.enable_chat').value,
                'xmpp_domain':registry.records.get('vindula.chat.interfaces.IVindulaChatConnector.xmpp_domain').value,
                'admin_jid':registry.records.get('vindula.chat.interfaces.IVindulaChatConnector.admin_jid').value,
                'admin_pwd':registry.records.get('vindula.chat.interfaces.IVindulaChatConnector.admin_pwd').value,
                
                'conference_jid':registry.records.get('vindula.chat.interfaces.IVindulaChatConnector.conference_jid').value,
                'pubsub_jid':registry.records.get('vindula.chat.interfaces.IVindulaChatConnector.pubsub_jid').value,
                
                'key_http_user':registry.records.get('vindula.chat.interfaces.IVindulaChatConnector.key_http_user').value,
                }
        
        return vars
    


class VindulaChatControlPanel(RegistryEditForm):
    schema = IVindulaChatConnector

VindulaChatControlPanelView = layout.wrap_form(VindulaChatControlPanel, ControlPanelFormWrapper)
VindulaChatControlPanelView.label = u"Vindula: Chat settings"