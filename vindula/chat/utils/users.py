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
    
    if 'error' in result or page.getcode() != 200:
        logger.info("%s - Error - %s - %s"% (user, result, page.getcode()))
        return False
    else:
        logger.info("%s - OK -"% (user))
        return True
    

def deletePrincipal(principal_jid):
    """Delete a jabber account as well as remove its associated nodes.
    """
    principal_id = principal_jid.user

    xmpp_users = getUtility(IXMPPUsers)       
    host = getSite().portal_url() + '/http-user'
    key = xmpp_users.getSettings().get('key_http_user')

    url = '%s/plugins/userService/userservice?type=delete&secret=%s&username=%s'%(host,key,principal_id)
    page = urllib.urlopen(url)
    result = page.read()

    if 'error' in result or page.getcode() != 200:
        logger.info("%s - Error - %s - %s"% (user, result, page.getcode()))
        return False
    else:
        logger.info("%s - OK Delete -"% (principal_id))
        return True
    
    