# -*- coding: utf-8 -*-


from vindula.chat.utils.models_openfire import ModelsGroupOpenFire
        
def set_GroupXMPP_default(context):
    try:
        if not ModelsGroupOpenFire().get_GroupOpenFire_by_name(u'vindula'):
            D={}
            D['groupName'] = u'vindula'
            D['description'] = u'Grupo dos usuarios do vindula'
            D['administrator'] = False
            
            ModelsGroupOpenFire().set_GroupOpenFire(**D)
            
    
    except:
        print "Error" 
