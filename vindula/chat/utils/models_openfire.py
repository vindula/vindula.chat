# coding: utf-8

from zope.app.component.hooks import getSite
from vindula.chat import MessageFactory as _

#Imports regarding the connection of the database 'strom'
from storm.locals import *
from storm.locals import Store
from zope.component import getUtility
from storm.zope.interfaces import IZStorm

#---Interação no banco de dados do Openfire------
class OpenFireStore(object):
   
    def __init__(self, *args, **kwargs):
        self.store = getUtility(IZStorm).get('openfire')
        
        #Lazy initialization of the object
        for attribute, value in kwargs.items():
            if not hasattr(self, attribute):
                raise TypeError('unexpected argument %s' % attribute)
            else:
                setattr(self, attribute, value)        
  
        # divide o dicionario 'convertidos'
        for key in kwargs:
            setattr(self,key,kwargs[key])

    
class ModelsGroupOpenFire(Storm, OpenFireStore):    
    __storm_table__ = 'ofGroup'    
    
    groupName = Unicode(primary=True)
    description = Unicode()
    administrator = Bool()

    def set_GroupOpenFire(self, **kwargs):
        # adicionando...
        group = ModelsGroupOpenFire(**kwargs)
        self.store.add(group)
        self.store.flush()      

    def get_GroupOpenFire_by_name(self,name):
        data = self.store.find(ModelsGroupOpenFire, ModelsGroupOpenFire.groupName == name).one()
        
        if data:
            return data
        else:
            return None
