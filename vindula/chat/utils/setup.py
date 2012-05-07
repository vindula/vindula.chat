# -*- coding: utf-8 -*-
import logging

from twisted.internet import defer
from twisted.words.protocols.jabber.jid import JID

from zope.component import getUtility
from Products.CMFCore.utils import getToolByName

from vindula.chat.interfaces import IAdminClient, IXMPPPasswordStorage, IXMPPUsers
from vindula.chat.utils.users import setupPrincipal
from vindula.chat.utils.models import ModelsUserOpenFire
import pickle

logger = logging.getLogger('vindula.chat')

def setupXMPPEnvironment(context):
    xmpp_users = getUtility(IXMPPUsers)
    pass_storage = getUtility(IXMPPPasswordStorage)
    mt = getToolByName(context, 'portal_membership')
    
    member_ids = mt.listMemberIds()
    pass_storage.clear()
    
    log = []
    for member_id in member_ids:
        D = {}
        resposta = {}
        member_jid = xmpp_users.getUserJID(member_id)
        member_password = pass_storage.set(member_id)
        
        try:D['username'] = unicode(member_id,'utf-8')
        except:D['username'] = member_id
        
        D['jid'] =  pickle.dumps(member_jid)
        
        try:D['password'] = unicode(member_password,'utf-8')
        except:D['password'] = member_password
            
        resposta['user'] = member_jid

        if setupPrincipal(member_jid, member_password, D['username']):
            ModelsUserOpenFire().set_UserOpenFire(**D)
            
            resposta['log'] = "Usuario criado com sucesso"
        else:
            resposta['log'] = "Erro ao criar o usuario"
        
        log.append(resposta)

    return log