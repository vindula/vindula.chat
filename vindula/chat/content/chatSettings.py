# coding=utf-8
from five import grok
from zope import schema
from plone.directives import form
from vindula.chat import MessageFactory as _


# Interface and schema
class IVindulaChatSettings(form.Schema):
    """ Vindula Chat Settings """
    
    enable_chat = schema.Bool(title=_(u"Ativar função de chat"),
                              description=_(u""),
                              default=False,
                              required=True,
                              )
    
    xmpp_domain = schema.TextLine(title=_(u"Endereço do dominio da intranet"),
                                  description=_(u""),
                                  default=_(u"vindula.com"),
                                  required=True,
                                  )
    xmpp_host = schema.TextLine(title=_(u"Endereço do servidor xmpp"),
                                  description=_(u""),
                                  default=_(u"127.0.0.1"),
                                  required=True,
                                  )
    
    
    admin_jid = schema.TextLine(title=_(u"Login do administrador do servidor XMPP "),
                                description=_(u""),
                                default=_(u'admin@vindula.com'),
                                required=True,)
    
    admin_pwd = schema.TextLine(title=_(u"Senha do login do administrador"),
                                description=_(u""),
                                default=_(u"temp123"),
                                required=True,)
    
    conference_jid = schema.TextLine(title=_(u"Endereço do compartilhamento do servidor XMPP"),
                                     description=_(u""),
                                     default=_(u"plone.vindula.com"),
                                     required=True,
                                     )
    
    pubsub_jid = schema.TextLine(title=_(u"Chave de conexão de compartilhamento do servidor XMPP"),
                                 description=_(u""),
                                 default=_(u"secret"),
                                 required=True,
                                 )
        
    key_http_user = schema.TextLine(title=_(u"Chave de HTTP com o plugin 'User Service' do servidor XMPP"),
                                    description=_(u""),
                                    default=_(u"NYIqhNdx"),
                                    required=True,)
    
    