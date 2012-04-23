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
        
        # adiciona a data atual
        #self.date_creation = datetime.now()    



#class ModelsUserOpenFire(Storm, OpenFireStore):    
#    __storm_table__ = 'ofUser'
#
#    username = Unicode(primary=True)
#    plainPassword = Unicode()
#    encryptedPassword  = Unicode()
#    name = Unicode()
#    email = Unicode()
#    creationDate = Unicode()
#    modificationDate = Unicode()
#    
#    def set_UserOpenFire(self, **kwargs):
#        # adicionando...
#        user = ModelsUserOpenFire(**kwargs)
#        self.store.add(user)
#        self.store.flush()     
#    
#    def get_UserOpenFire_by_username(self,username):
#        data = self.store.find(ModelsUserOpenFire, ModelsUserOpenFire.username == username).one()
#        
#        if data:
#            return data
#        else:
#            return None
#
#    
#    
#class ModelsGroupUserOpenFire(Storm, OpenFireStore):    
#    __storm_table__ = 'ofGroupUser'    
#    
#    __storm_primary__ = "groupName", "username","administrator"
#    
#    groupName = Unicode()
#    username = Unicode()
#    administrator = Bool()
#    
#    def set_GroupUserOpenFire(self, **kwargs):
#        # adicionando...
#        groupUser = ModelsGroupUserOpenFire(**kwargs)
#        self.store.add(groupUser)
#        self.store.flush()          
#
#    def get_GroupUserOpenFire_by_username(self,username):
#        data = self.store.find(ModelsGroupUserOpenFire, ModelsGroupUserOpenFire.groupName == u'vindula',
#                                                        ModelsGroupUserOpenFire.username == username,
#                                                        ModelsGroupUserOpenFire.administrator == False).one()
#        
#        if data:
#            return data
#        else:
#            return None


    
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
        
        
        
#        key = 'This is a test key'
#        cipher = Blowfish(key)
#        cl = cipher.cipher(xl, cipher.ENCRYPT)
#        

