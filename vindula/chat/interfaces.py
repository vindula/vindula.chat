# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope.component.interfaces import IObjectEvent, implements
from zope.viewlet.interfaces import IViewletManager
from zope import schema


class IVindulaChatConnector(Interface):
    """
    Vindula Chat Connector interface
    """
    enable_chat = schema.Bool(title=u"Ativar função de chat",default=True)
    xmpp_domain = schema.TextLine(title=u"Endereço do dominio da intranet",default=u"vindula.com")
    admin_jid = schema.TextLine(title=u"Login do administrador do servidor XMPP ",default=u'admin@vindula.com')
    admin_pwd = schema.TextLine(title=u"Senha do login do administrador",default=u"temp123")
    
    conference_jid = schema.TextLine(title=u"Endereço do compartilhamento do servidor XMPP",default=u"plone.vindula.com")
    pubsub_jid = schema.TextLine(title=u"Chave de conexão de compartilhamento do servidor XMPP",default=u"secret")
        
    key_http_user = schema.TextLine(title=u"Chave de HttP com o plugin 'User Service' do servidor XMPP",default=u"NYIqhNdx")

class IXMPPUsers(Interface):
    """ Marker interface for the XMPP tool.
    """

class IXMPPPasswordStorage(Interface):
    """ Marker interface for the xmmp user passwords
    """

class IPubSubable(Interface):
    """Interface for objects that can be uniquely linked to pubsub nodes.
    """

class IPubSubStorage(Interface):
    """Marker interface for the PubSub storage
    """

class IAdminClient(Interface):
    """Marker interface for the PubSub twisted client.
    """

class IAdminClientConnected(IObjectEvent):
    """Admin client has connected.
    """

class AdminClientConnected(object):
    implements(IAdminClientConnected)

    def __init__(self, obj):
        self.object = obj


class IAdminClientDisconnected(IObjectEvent):
    """Admin client has connected.
    """

class AdminClientDisconnected(object):
    implements(IAdminClientConnected)

    def __init__(self, obj):
        self.object = obj


class IXMPPLoaderVM(IViewletManager):
    """Viewlet manager for the loader viewlet.
    """
