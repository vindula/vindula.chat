# coding: utf-8

from zope.app.component.hooks import getSite
from vindula.chat import MessageFactory as _

#Imports regarding the connection of the database 'strom'
from storm.locals import *
from storm.locals import Store

#dependencias Myvindula
from vindula.myvindula.user import BaseStore, BaseFunc
from vindula.myvindula.validation import valida_form

class ModelsUserOpenFire(Storm, BaseStore):    
    __storm_table__ = 'vin_chat_user_openfire'
    
    id = Int(primary=True)
    username = Unicode()
    password = Unicode()
    jid = Pickle()
    date_creation = DateTime()
    
    def set_UserOpenFire(self, **kwargs):
        # adicionando...
        user = ModelsUserOpenFire(**kwargs)
        self.store.add(user)
        self.store.flush()        
    
    
    def get_UserOpenFire_by_username(self,username):
        data = self.store.find(ModelsUserOpenFire, ModelsUserOpenFire.username == username).one()
        
        if data:
            return data
        else:
            return None
        
    def remove_UserOpenFire_by_username(self,username):
        result = self.get_UserOpenFire_by_username(username)
        if result:
            self.store.remove(result)
            self.store.flush()


        
