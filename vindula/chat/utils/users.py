# -*- coding: utf-8 -*-

#from vindula.chat.utils.models_openfire import ModelsUserOpenFire, ModelsGroupUserOpenFire
from vindula.chat.interfaces import IXMPPUsers
from zope.app.component.hooks import getSite
from zope.component import getUtility
import logging

import urllib

logger = logging.getLogger('vindula.chat')
   
def setupPrincipal(principal_jid, principal_password, principal_id):
    """Create a jabber account for a new user as well
       as create and configure its associated nodes."""
       
    xmpp_users = getUtility(IXMPPUsers)       
    
    host = getSite().portal_url() + '/http-user'
    key = xmpp_users.getSettings().get('key_http_user')
    user = principal_id
    password = principal_password
    name = principal_id
    email = principal_jid.userhost()
    groups = 'vindula'
    
    url = '%s/plugins/userService/userservice?type=add&secret=%s&username=%s&password=%s&name=%s&email=%s&groups=%s' %(host,key,user, password,name, email, groups)
    page = urllib.urlopen(url)
    result = page.read()
    
    if 'error' in result:
        logger.info("%s - Error - %s "% (user, result))
        return False
    else:
        logger.info("%s - OK"% (user))
        return True
    

    
    
#    if not ModelsUserOpenFire().get_UserOpenFire_by_username(principal_id):
#        D['username'] = principal_id
#        D['encryptedPassword'] = unicode(x) 
#        D['name'] = principal_id
#        D['email'] = principal_jid.userhost()
#        D['creationDate'] = u'0'
#        D['modificationDate'] = u'0'
#    
#        ModelsUserOpenFire().set_UserOpenFire(**D)
#    
#    if not ModelsGroupUserOpenFire().get_GroupUserOpenFire_by_username(principal_id):
#        F = {}
#        F['groupName'] = u'vindula' 
#        F['username'] = principal_id
#        F['administrator'] = False
#        ModelsGroupUserOpenFire().set_GroupUserOpenFire(**F)


def deletePrincipal(client, principal_jid):
    """Delete a jabber account as well as remove its associated nodes.
    """
    principal_id = principal_jid.user

    def deleteUser(result):
        if result == False:
            return False
        d = client.admin.deleteUsers(principal_jid.userhost())
        return d

    d = client.deleteNode(principal_id)
    d.addCallback(deleteUser)
    return d
