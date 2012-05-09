# -*- coding: utf-8 -*-
from five import grok

from vindula.chat.interfaces import IXMPPUsers 
from zope.app.component.hooks import getSite
from zope.component import getUtility
from Products.CMFCore.interfaces import ISiteRoot
from zope.interface import Interface
import urllib2, logging

from vindula.myvindula.user import BaseFunc, ModelsFuncDetails
from vindula.chat.utils.setup import setupXMPPEnvironment

logger = logging.getLogger('vindula.chat')
    
# View congif chat
class ChatConfigView(grok.View):
    grok.context(Interface) 
    grok.name('vindula-chat-config') 
    grok.require('zope2.View')
    
    def enableChat(self):
        xmpp_users = getUtility(IXMPPUsers)
        settings = xmpp_users.getSettings()
        altenticado = getSite().portal_membership.isAnonymousUser()
        
        if settings.get('enable_chat',False) and altenticado == 0:
            return True 
        else:
            return False

    def render(self):
        return 'vindula-chat-config'
    
# Setup Inicial do Chat    
class SetupXMPPForm(grok.View):
    grok.context(ISiteRoot) 
    grok.name('setup-xmpp') 
    grok.require('cmf.ManagePortal')

    def update(self):
        """ Receive itself from request and do some actions """
        form = self.request.form
        submitted = form.get('form.submitted', False)
        if submitted:
            self.log = setupXMPPEnvironment(self.context)               
    
    
    
class ChatUserFoto(grok.View):
    grok.context(Interface) 
    grok.name('portraits-user') 
    grok.require('zope2.View')
    
    def render(self):
        return self.url_image
    
    def update(self):
        form = self.request.form
        user = form.get('user','')
        
        try:user_id = unicode(user, 'utf-8')    
        except:user_id = user 

        dados_user =  ModelsFuncDetails().get_FuncDetails(user_id)
        if dados_user:
            photo = dados_user.photograph
    
            if photo is not None and not ' ' in photo:
                 local = photo.split('/')
                 try:
                     ctx= getSite()[local[0]][local[1]][local[2]]
                     obj = ctx.restrictedTraverse('@@images').scale('photograph', height=150, width=120)
                 
                     self.url_image = obj.index_html()
                 except:
                     self.url_image =  ''
       
            else:
                self.url_image = ''
        else:
            self.url_image = ''     

class ChatChangePasswd(grok.View):
    grok.context(ISiteRoot) 
    grok.name('change-chatpasswd') 
    grok.require('zope2.View')
    
    def update(self):
        pass
     
    
    
