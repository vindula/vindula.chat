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


def create_obj_settings(context):
    
    portal = context.getSite()

    # Creating Control Panel Folder
    if 'control-panel-objects' in portal.objectIds():
        
        folder_control_panel = portal['control-panel-objects']
        type = 'vindula.chat.content.settings'
        id = 'vindula_chat_' + type.split('.')[3]
        if not id in folder_control_panel.objectIds():
            folder_control_panel.setConstrainTypesMode(0)
            portal.portal_types.get(type).global_allow = True        
            folder_control_panel.invokeFactory(type, id=id)
            print 'Create %s object.' % id          
            portal.portal_types.get(type).global_allow = False

    