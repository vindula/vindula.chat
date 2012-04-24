# -*- coding: utf-8 -*-
import logging

from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.events import IPrincipalCreatedEvent, IPrincipalDeletedEvent
from zope.component import adapter, getUtility

from vindula.chat.interfaces import IAdminClient, IPubSubStorage, IXMPPPasswordStorage, IXMPPUsers
from vindula.chat.utils.users import setupPrincipal, deletePrincipal

from vindula.chat.utils.models import ModelsUserOpenFire
import pickle

logger = logging.getLogger('vindula.chat')


@adapter(IPrincipalCreatedEvent)
def onUserCreation(event):
    """Create a jabber account for new user.
    """

    client = getUtility(IAdminClient)
    xmpp_users = getUtility(IXMPPUsers)
    storage = getUtility(IPubSubStorage)
    principal = event.principal
    mtool = getToolByName(principal, 'portal_membership')

    principal_id = principal.getUserId()
    principal_jid = xmpp_users.getUserJID(principal_id)
    
    pass_storage = getUtility(IXMPPPasswordStorage)
    principal_pass = pass_storage.set(principal_id)

    D = {}
    try:D['username'] = unicode(principal_id,'utf-8')
    except:D['username'] = principal_id
    
    D['jid'] =  pickle.dumps(principal_jid)
    
    try:D['password'] = unicode(principal_pass,'utf-8')
    except:D['password'] = principal_pass

    if setupPrincipal(principal_jid, principal_pass, D['username']):
        ModelsUserOpenFire().set_UserOpenFire(**D)
        logger.info("Usuario criado altomaticamente")

        return True
    else:
        logger.info("Erro ao criar o usuario")
        return False


@adapter(IPrincipalDeletedEvent)
def onUserDeletion(event):
    """Delete jabber account when a user is removed.
    """
    client = getUtility(IAdminClient)
    xmpp_users = getUtility(IXMPPUsers)
    storage = getUtility(IPubSubStorage)

    principal_id = event.principal
    principal_jid = xmpp_users.getUserJID(principal_id)

    try:username = unicode(principal_id,'utf-8')
    except:username = principal_id

    if deletePrincipal(principal_jid):
        ModelsUserOpenFire().remove_UserOpenFire_by_username(username)
        logger.info("Usuario removido altomaticamente")

        return True
    else:
        logger.info("Erro ao excluir o usuario")
        return False

