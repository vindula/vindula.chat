# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from five import grok
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalFooter


grok.context(Interface) 

# Viewlet for portal logo top
class ChatViewlet(grok.Viewlet): 
    grok.name('vindula.chat.listUsers') 
    grok.require('zope2.View')
    grok.viewletmanager(IPortalFooter) 
