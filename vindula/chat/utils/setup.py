# -*- coding: utf-8 -*-
import logging

from twisted.internet import defer
from twisted.words.protocols.jabber.jid import JID

from zope.component import getUtility
from Products.CMFCore.utils import getToolByName

from vindula.chat.interfaces import IAdminClient, IXMPPPasswordStorage, IXMPPUsers

#from vindula.chat.utils.pubsub import getAllChildNodes
from vindula.chat.utils.users import setupPrincipal
#from vindula.chat.subscribers.startup import populatePubSubStorage
from vindula.chat.utils.models import ModelsUserOpenFire
import pickle

logger = logging.getLogger('vindula.chat')

def setupXMPPEnvironment(context):
    xmpp_users = getUtility(IXMPPUsers)
    pass_storage = getUtility(IXMPPPasswordStorage)
    mt = getToolByName(context, 'portal_membership')
    
    member_ids = mt.listMemberIds()
    pass_storage.clear()
    
    for member_id in member_ids:
        D = {}
        member_jid = xmpp_users.getUserJID(member_id)
        member_password = pass_storage.set(member_id)
        
        try:D['username'] = unicode(member_id,'utf-8')
        except:D['username'] = member_id
        
        D['jid'] =  pickle.dumps(member_jid)
        
        try:D['password'] = unicode(member_password,'utf-8')
        except:D['password'] = member_password
            
        #if ModelsUserOpenFire().get_UserOpenFire_by_username(D['username']):
        #    ModelsUserOpenFire().remove_UserOpenFire_by_username(D['username'])
        
        if setupPrincipal(member_jid, member_password, D['username']):
            ModelsUserOpenFire().set_UserOpenFire(**D)
       

    return True
