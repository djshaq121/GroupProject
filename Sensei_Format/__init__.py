#===============================================================
#  Copyright (C)2012-2016 Blender Sensei (Seth Fentress: Licensor)
#  For more information visit Blendersensei.com
#
#  ####BEGIN LICENSE BLOCK #####
#  By using this software (from this point on referred to as "The
#  Software", you (the Licensee) agree to the terms of its license. 
#  The conditions of this license are as follows:
#
#  • You may not redistribute, share or sell this software.
#  • The content you create with this software may be used
#    for personal or commercial use. 
#  • The Software is provided under an AS-IS basis. Licensor shall 
#    never, and without any limit, be liable for any damage, cost, 
#    expense or any other payment incurred by Licensee as a result 
#    of Software’s actions, failure, bugs and/or any other interaction 
#    between The Software and Licensee’s end-equipment, computers, 
#    other software or any 3rd party, end-equipment or services.
#  ####END LICENSE BLOCK #####
#
#===============================================================


bl_info = {
 "name": "Sensei Format",
 "author": "Blender Sensei",
 "version": (5, 4, 4),
 "description": "Enhanced Blender Interface. Visit Blendersensei.com",
 "wiki_url": "https://blendersensei.com",
 "category": "Sensei Format"}

import bpy, os, shutil, addon_utils, datetime
import threading, urllib.request, re
from bpy_extras.io_utils import ImportHelper
from bpy.app.handlers import persistent


#Resolution finder
def resFinder():
    wm = bpy.context.window_manager
    
    #Check for largest of open windows
    windows = []
    for window in wm.windows:
        windows.append(window.width)    
    width = max(windows)

    startup = ''
    if width <= 1280:
        startup = '1280x1024.blend'
    if width <= 1366:
        if width > 1280:
            startup = '1366x768.blend'
    if width <= 1440:
        if width > 1366:
            startup = '1440x900.blend'
    if width <= 1600:
        if width > 1440:
            startup = '1600x900.blend'
    if width <= 1680:
        if width > 1600:
            startup = '1680x1050.blend'
    if width > 1680:
        startup = '1920x1080.blend'

    #Default to 1920x1080 if failure
    if width > 1920:
        startup = '1920x1080.blend'
    if width < 100:
        startup = '1920x1080.blend'
    if len(startup) < 1:
        startup = '1920x1080.blend'
    
    print('')
    print('Using ', startup, 'for startup file')    
    return startup


def userprefRefresh():
    #Refresh opengl
    system = bpy.context.user_preferences.system
    system.solid_lights[0].use = False
    system.solid_lights[0].use = True   
    return
    
#Sensei Format Menu Options
class sfMenuOptions(bpy.types.Operator):
    bl_idname = "object.sf_menu_options"
    bl_label = "Sensei Format Menu Options"
    bl_description = "Requires Blender restart"
    
    option = bpy.props.StringProperty()
    
    def execute(self, context):
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        
        user_path = bpy.utils.resource_path('USER')
        scripts_path = os.path.join(user_path, "scripts")
        config_path = os.path.join(user_path, "config")
        addons_path = os.path.join(scripts_path, "addons")
        sf_path = os.path.join(addons_path, "Sensei_Format")
        sf_scripts = os.path.join(sf_path, "scripts")
        sf_presets = os.path.join(sf_scripts, "presets")
        sf_interface_theme = os.path.join(sf_presets, "interface_theme")      
        sf_addons = os.path.join(sf_scripts, "addons")
        sf_defaults = os.path.join(sf_path, "defaults")
        
        installSwitch1 = os.path.join(sf_path,"installSwitch1.txt")
        installSwitch2 = os.path.join(sf_path,"installSwitch2.txt")
        sf_activated = os.path.join(sf_path, "senseiActivated.txt")
        option = self.option
        
        startup_path = os.path.join(config_path, "startup.blend")    
        startup_backup = os.path.join(config_path,"startup_backup.blend")
        startup_sf_backup = os.path.join(config_path,"startup_sf_backup.blend")
        
        userpref_path = os.path.join(config_path, "userpref.blend")
        userpref_backup = os.path.join(config_path, "userpref_backup.blend")
        userpref_sf_backup = os.path.join(config_path, "userpref_sf_backup.blend")
        
        
        
        if option == 'reload_defaults':
            try:
                newStartup = resFinder()            
            except:
                newStartup = '1920x1080.blend'                
            new_startup_path = os.path.join(sf_defaults, newStartup)
            
            if os.path.exists(startup_path):
                os.remove(startup_path)                
            shutil.copyfile(new_startup_path, startup_path)
            
            #Activate load ui if needed
            userpref = bpy.context.user_preferences
            paths = userpref.filepaths
            uiState = paths.use_load_ui
            
            paths.use_load_ui = True
            bpy.ops.wm.save_userpref()
            
            bpy.ops.wm.open_mainfile(filepath = startup_path)
            bpy.ops.wm.save_homefile()
            
            if uiState is False:
                paths.use_load_ui = False
                bpy.ops.wm.save_userpref()
                
            bpy.ops.wm.quit_blender()
            
        
        if option == 'activate':
            print('BACKING UP USER FILES...')
            #Rename user's files for safe keeping
            if os.path.exists(startup_path):
                if os.path.exists(startup_backup):
                    os.remove(startup_backup)
                os.rename(startup_path, startup_backup)        
            if os.path.exists(userpref_path):
                if os.path.exists(userpref_backup):
                    os.remove(userpref_backup)
                os.rename(userpref_path, userpref_backup)
            
            #If previous SF settings found then use them
            if os.path.exists(userpref_sf_backup):
                if os.path.exists(userpref_path):
                    os.remove(userpref_path)
                os.rename(userpref_sf_backup, userpref_path)
            else:
                #Install SF Theme
                theme_path = os.path.join(sf_interface_theme, "sensei.xml")
                bpy.ops.wm.theme_install(overwrite=True, filepath=theme_path)
                
            #Setup startup file
            startup = ''
            if os.path.exists(startup_sf_backup):                    
                os.rename(startup_sf_backup, startup_path)
            else:
                #Check screen to find right size for startup
                startup = resFinder()
                new_startup = os.path.join(sf_defaults, startup)
                if os.path.exists(startup_path):
                    os.remove(startup_path)
                shutil.copyfile(new_startup, startup_path)

            #Now open startup file
            bpy.ops.wm.read_homefile()
            
            
            #Enable addons
            #This will activate all user's custom addons
            #(as well as additional Sensei Format addons)
            addons = os.listdir(addons_path)
            for addon in addons:  
                if 'pycache' in addon:
                    addons.remove(addon)
                else:
                    if '.py' in addon:
                        addon = addon.replace('.py', '')                        
                    addon_utils.enable(addon, default_set = True)
                  
                       
            if os.path.exists(installSwitch2) is False:
                bpy.context.user_preferences.view.use_quit_dialog = False
                addon_utils.enable("Sensei_Format", default_set = True)
                                
                try: #Disable SF master addons calls
                    bpy.ops.wm.addon_disable(module="Screencast_Keys")
                    bpy.ops.wm.addon_disable(module="Sensei_Format_Distributor")
                    
                    #ZB over ZB Lite
                    zb_path = os.path.join(addons_path, "Zero_Brush.py")
                    if os.path.exists(zb_path) is False:
                        bpy.ops.wm.addon_disable(module="Zero_Brush")
                    else:
                        bpy.ops.wm.addon_disable(module="Zero_Brush_Lite")
                except:
                    pass
                                
                #Save userpref
                bpy.ops.wm.save_userpref()
                
                #Create Install Switch
                if os.path.exists(installSwitch2) is False:
                    iSwitch2 = open(installSwitch2, "w")          
                    iSwitch2.close()
                    
            
            if os.path.exists(sf_activated) is False:
                sa = open(sf_activated, "w")
                sa.close()
                
            #Quit Blender    
            print('==================SENSEI FORMAT ACTIVATED')
            bpy.ops.wm.quit_blender()     
            
   
        
        #Deactivate and Full Uninstall
        if 'deactivate' in option:            
            try:
                bpy.types.INFO_HT_header.remove(newBlendAvailable)
            except:
                pass
            
            if 'uninstall' in option:
                if os.path.exists(installSwitch1):
                    os.remove(installSwitch1)
                if os.path.exists(installSwitch2):
                    os.remove(installSwitch2)
        
            #Disable addons
            addons = ['add_mesh_walls','matlib','Builder.py','Mesh_Bsurfaces.py',
            'Sensei_Keys.py','Sensei_Layout.py','Zero_Brush_Lite.py']
            
            for addon in addons: 
                if 'uninstall' in option:
                    #Remove addons
                    addonToX = os.path.join(addons_path, addon)
                    if os.path.exists(addonToX):
                        if '.py' in addonToX:
                            os.remove(addonToX)
                        else:
                            shutil.rmtree(addonToX)
                        
                #Disable live addons        
                addon = addon.replace('.py','')
                addon_utils.disable(addon, default_set = True)
                
            if 'uninstall' not in option:    
                #Save Sensei startup
                if os.path.exists(startup_path):
                    if os.path.exists(startup_sf_backup):
                        os.remove(startup_sf_backup)
                    os.rename(startup_path, startup_sf_backup)

                #Save Sensei userpref
                if os.path.exists(userpref_path):
                    if os.path.exists(userpref_sf_backup):
                        os.remove(userpref_sf_backup)
                    os.rename(userpref_path, userpref_sf_backup)
            
            #Return previous settings
            startup_default = ''
            if os.path.exists(sf_activated):
                os.remove(sf_activated)
                if os.path.exists(startup_backup):
                    if os.path.exists(startup_path):
                        os.remove(startup_path)
                    os.rename(startup_backup, startup_path)
                else:
                    #User had no original so use defaults            
                    startup_default = os.path.join(sf_defaults, "startup.blend")
                    if os.path.exists(startup_path):
                        os.remove(startup_path)
                    shutil.copyfile(startup_default, startup_path)

                if os.path.exists(userpref_backup):
                    if os.path.exists(userpref_path):
                        os.remove(userpref_path)
                    os.rename(userpref_backup, userpref_path)
                else:
                    userpref_default = os.path.join(sf_defaults, "userpref.blend")
                    if os.path.exists(userpref_path):
                        os.remove(userpref_path)
                    shutil.copyfile(userpref_default, userpref_path)
            
                #Reload user's settings 
                bpy.ops.wm.open_mainfile(filepath=startup_path, load_ui=True)
            
            #If had to load startup default, then activate Sensei addon
            if 'uninstall' not in option:
                if len(startup_default) > 0:
                    addon_utils.enable("Sensei_Format", default_set = True)
                    bpy.ops.wm.save_userpref()
                else:
                    #Reload userpref
                    bpy.ops.wm.read_homefile()

            else:
                addon_utils.disable("Sensei_Format", default_set = True)
                bpy.ops.wm.save_userpref()
                
            #Quit Blender    
            bpy.ops.wm.quit_blender()
            print('==================SENSEI FORMAT DEACTIVATED')
        
        
        if option == 'update_blender':
            
            #=======Copy settings folder            
            parDir = os.path.dirname(user_path)
            
            #Get new folder name
            new_path = str(scene.sfLatestBlender)
            new_path = new_path[:1] + '.' + new_path[1:]
            
            #If new folder settings already exist rename            
            
            #Copy settings folder
            new_path = os.path.join(parDir, new_path)
            if os.path.exists(new_path) is False:            
                shutil.copytree(user_path, new_path)
            
            else:
                renamed_path = new_path + '_previous_settings'
                os.rename(new_path, renamed_path)
                shutil.copytree(user_path, new_path)
            
            #Launch download page
            bpy.ops.wm.url_open(url="http://blender.org/download")
        
        
        
        if option == 'update_sensei':
  
            sf_update_zip = os.path.join(addons_path, "Sensei_Format.zip")
            sf_download = "https://blendersensei.com/download/sensei-format/"

            #Get new Sensei Format files
            if os.path.exists(sf_update_zip):
                os.remove(sf_update_zip)    
            urllib.request.urlretrieve (sf_download, sf_update_zip)

            #Unzip, replace and delete zip
            if os.path.exists(sf_path):
                shutil.rmtree(sf_path)
            
            #Account for browser auto-unzipping    
            if os.path.exists(sf_update_zip):        
                shutil.unpack_archive(sf_update_zip, addons_path, 'zip')
                os.remove(sf_update_zip)


                                    
            #UPDATE ADDONS
            addons = os.listdir(sf_addons)

            #Replace or update addons
            for addon in addons:
                if 'pycache' in addon:
                    addons.remove(addon)
                else:
                    sfAddon = os.path.join(sf_addons, addon)
                    sfAddonNewPath = os.path.join(addons_path, addon)
                    if '.py' in addon:
                        if os.path.exists(sfAddonNewPath):
                            os.remove(sfAddonNewPath)
                        shutil.copyfile(sfAddon,sfAddonNewPath)
                    else:
                        if os.path.exists(sfAddonNewPath):
                            shutil.rmtree(sfAddonNewPath)
                        shutil.copytree(sfAddon,sfAddonNewPath)

            
            #Create install switches
            iSwitch = open(installSwitch1, "w")
            iSwitch.close()
            iSwitch2 = open(installSwitch2, "w")
            iSwitch2.close()
            
            if os.path.exists(sf_activated) is False:
                sa = open(sf_activated, "w")
                sa.close()
                    
            #Activate new theme
            theme_path = os.path.join(sf_interface_theme, "sensei.xml")
            bpy.ops.wm.theme_install(overwrite=True, filepath=theme_path)

            updateLog = "https://blendersensei.com/sensei-format-update-log/"
            bpy.ops.wm.url_open(url=updateLog)
            
            
            #Quit Blender to be restarted
            bpy.ops.wm.quit_blender()
                
        if option == 'cancel':
            bpy.ops.wm.read_homefile()
        return{'FINISHED'}
        





#UPDATE CHECK FUNCTIONS===========================
#Extract text from site url
def getSiteString(site_text):
    url = urllib.request.urlopen(site_text)
    urlBytes = url.read()
    #page must be converted from bytes
    site_text = urlBytes.decode("utf8")
    url.close()
    return site_text


#Use sub thread to speed up checking
def updateCheckSubThread():
    scene = bpy.context.scene
    latestBlendVersion = 0
    latestSenseiFormat = 0
    
    user_path = bpy.utils.resource_path('USER')
    scripts_path = os.path.join(user_path, "scripts")
    addons_path = os.path.join(scripts_path, "addons")
    sf_path = os.path.join(addons_path, "Sensei_Format")
    check_date = os.path.join(sf_path, "checkdate.txt")
        
    #try: #Check if Blender up to date
    if 1==1:
        site_text = getSiteString("https://blender.org/download")
        
        beginPos = ''
        i = 2
        while beginPos == '':
            text_search = "Blender " + str(i) + '.'
            beginPos = site_text.find(text_search)
            if i > 100:
                break
            
        latestBlendVersion = site_text[beginPos+8:beginPos+12]        
        #Do not auto-update unless official, stable release
        if 'rc'.lower() in latestBlendVersion.lower():
            latestBlendVersion = int(re.sub("[^0-9]", "", latestBlendVersion)) - 1            
        else:
            latestBlendVersion = int(re.sub("[^0-9]", "", latestBlendVersion))

        try: #Check if Sensei Format up to date
            site_text = getSiteString("http://versioninfo.blendersensei.com")
            text_search = "Sensei Format "
            beginPos = site_text.find(text_search)
            latestSenseiFormat = site_text[beginPos+14:beginPos+18]
            latestSenseiFormat = int(latestSenseiFormat.replace('.',''))           
        except:
            #Reset for next time incase failed to check            
            if os.path.exists(check_date):
                os.remove(check_date)
            print('==================Unable to check for update at Blendersensei.com')


        blendVersion = scene.statistics()[1:5]
        blendVersion = int(re.sub("[^0-9]", "", blendVersion))        
          
        sfVersion = ''
        for mod in addon_utils.modules():
            if mod.bl_info.get('name') == 'Sensei Format':
                sfVersion = str(mod.bl_info.get('version'))       
        sfVersion = int(re.sub("[^0-9]", "", sfVersion)) 
            
        
        if blendVersion < latestBlendVersion:
            scene.sfLatestBlender = latestBlendVersion
            
        if sfVersion < latestSenseiFormat:
            scene.sfLatestSenseiFormat = latestSenseiFormat
        
        if (scene.sfLatestBlender + scene.sfLatestSenseiFormat) > 0:
            if scene.sfLatestBlender > 0:
                print('Your version of Blender is ',blendVersion)
                print('Blender version ',latestBlendVersion, ' is now available.')                
                #Reset update check
                if os.path.exists(check_date):
                    os.remove(check_date) 
                    
                
            if scene.sfLatestSenseiFormat > 0:
                print('Your version of Sensei Format is ', sfVersion)
                print('Sensei Format version ', latestSenseiFormat,' is now available.')                
                #Reset update check
                if os.path.exists(check_date):
                    os.remove(check_date)               
                
                
            try: #Avoid drawing doubles
                bpy.types.INFO_HT_header.remove(updatesAvailable)
            except:
                pass  
            bpy.types.INFO_HT_header.append(updatesAvailable)
                    
            for screen in bpy.data.screens:
                for area in screen.areas:
                    if area.type == 'INFO':
                        area.tag_redraw()        
        else:    
            print('==================Sensei Format and Blender up to date!')
    else: #except:
        print('==================Unable to check for update at Blender.org')
            
        
                
def sfCheckForUpdates(self,context):    
    try:
        bpy.types.INFO_HT_header.remove(updatesAvailable)
    except:
        pass    
    #Remove check file
    user_path = bpy.utils.resource_path('USER')
    scripts_path = os.path.join(user_path, "scripts")
    modules_path = os.path.join(scripts_path, "modules")
    config_path = os.path.join(user_path, "config")
    addons_path = os.path.join(scripts_path, "addons")
    sf_path = os.path.join(addons_path, "Sensei_Format")
    check_date = os.path.join(sf_path, "checkdate.txt")    
    
    if os.path.exists(check_date):
        os.remove(check_date)    
    if self.sfCheckForUpdates:
        sfUpdateCheckMainFunciton(sf_path)



def sfUpdateCheckMainFunciton(sf_path):
    try:
        #Only check once a day
        check_date = os.path.join(sf_path, "checkdate.txt")
        today = str(datetime.date.today())                                        
        runCheck = True
   
        if os.path.exists(check_date):
            cd = open(check_date, 'r')            
            if cd.read() == today:
                runCheck = False
            else:
                cd = open(check_date, "w")
                cd.write(today)
                cd.close()  
        else:
            cd = open(check_date, "w")
            cd.write(today)
            cd.close()                  
   
        if runCheck:
            #Use sub thread to check for updates to prevent startup slowdown
            checkForUpdates = threading.Thread(target=updateCheckSubThread)
            checkForUpdates.start()        
        else:
            print('')
            print('==================Sensei Format and Blender up to date!')
            print('(already checked for updates today)')
            print('')
    except:
        pass

            
def updatesAvailable(self,context):
    scene = bpy.context.scene
    layout = self.layout
    
    #Define paths
    user_path = bpy.utils.resource_path('USER')
    scripts_path = os.path.join(user_path, "scripts")
    modules_path = os.path.join(scripts_path, "modules")
    config_path = os.path.join(user_path, "config")
    addons_path = os.path.join(scripts_path, "addons")
    sf_path = os.path.join(addons_path, "Sensei_Format")
    sf_activated = os.path.join(sf_path, "senseiActivated.txt")
    
    message = ''
    if scene.sfLatestBlender > 0:
        if scene.sfLatestSenseiFormat == 0:
            message = 'Blender version update available (see File menu)'    
    if scene.sfLatestSenseiFormat > 0:
        if scene.sfLatestBlender == 0:
            message = 'Sensei Format update available (see File menu)'    
    if scene.sfLatestSenseiFormat > 0:
        if scene.sfLatestBlender > 0:
            message = 'Blender & Sensei Format update available (see File menu)'    
    if message == 'SENSEI FORMAT UPDATE AVAILABLE!':
        if os.path.exists(sf_activated):      
            layout.label(message, icon = 'MONKEY')
    else:
        layout.label(message, icon = 'MONKEY')
    




@persistent
def sfStartupSettingsInit(scene):
    
    try: #Initialize various options
        scene = bpy.context.scene
        world = scene.world.light_settings

        for screen in bpy.data.screens:
            #Timeline options
            screen.use_follow = True
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    
                    #Turn on live ambient
                    if area.spaces[0].lock_camera:
                        fx = area.spaces[0].fx_settings                        
                        if world.use_ambient_occlusion:
                            fx.use_ssao = True                    
                        if len(scene.sfCFocus) > 0:
                            fx.use_dof = True                                          
    except:
        pass    
    
        
    #Turn on HD shading
    if hasattr(scene, 'sfHDShading'):
        if scene.sfHDShading:
            if scene.sfLastRE == 'CYCLES':
                scene.render.engine = 'CYCLES'             
                try:
                    for area in bpy.context.screen.areas:
                        if area.type == 'VIEW_3D':
                            if area.y != 0:
                                fx = area.spaces[0].fx_settings
                                fx.use_ssao = True
                                break
                except:
                    pass                
            else:
                scene.sfHDShading = False
                scene.sfHDShading = True                        

    
    try: #Switch to mat view if needed
        if bpy.context.active_object.active_material:                        
            screen = bpy.context.screen
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    area.spaces[0].viewport_shade = 'MATERIAL'
    except:
        pass
    
    try: #If not texture paint, disable "Display Only Render"
        mode = bpy.context.mode
        if mode != 'PAINT_TEXTURE':
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    if area.y != 0:
                        area.spaces.active.show_only_render = False
                        break
    except:
        pass
                
            


#Sensei Format Initialization
class sfInit(bpy.types.Operator):
    bl_idname = "object.sensei_format_init"
    bl_label = "Sensei Format Initialization"

    def execute(self, context):
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        
        user_path = bpy.utils.resource_path('USER')
        scripts_path = os.path.join(user_path, "scripts")
        modules_path = os.path.join(scripts_path, "modules")
        config_path = os.path.join(user_path, "config")
        addons_path = os.path.join(scripts_path, "addons")
        sf_path = os.path.join(addons_path, "Sensei_Format")
        sf_activated = os.path.join(sf_path, "senseiActivated.txt")
        sf_defaults = os.path.join(sf_path, "defaults")
        sf_scripts = os.path.join(sf_path, "scripts") 
        sf_modules = os.path.join(sf_scripts, "modules")
        sf_addons = os.path.join(sf_scripts, "addons")

        
        installSwitch1 = os.path.join(sf_path,"installSwitch1.txt")        
        if os.path.exists(installSwitch1):
            
            
            #=========================SENSEI FORMAT (startup maintenance)
            if os.path.exists(sf_activated):

                try:#Make sure core addons enabled
                    sf_keys = os.path.join(addons_path, 'Sensei_Keys.py')
                    sf_layout = os.path.join(addons_path, 'Sensei_Layout.py')                
                    sf_builder = os.path.join(addons_path, 'Builder.py')
                    sf_amw = os.path.join(addons_path, 'add_mesh_walls')
                    sf_meshbs = os.path.join(addons_path, 'Mesh_Bsurfaces.py')
                    sf_zbl = os.path.join(addons_path, 'Zero_Brush_Lite.py')
                    sf_zb = os.path.join(addons_path, 'Zero_Brush.py')
                    
                    addons = [sf_keys, sf_layout, sf_builder, sf_amw, 
                    sf_matutil, sf_meshbs, sf_zbl, sf_zb]
                    
                    needSaving = False
                    use_zb = False
                    for addon in addons:
                        if os.path.exists(addon):
                            addon = os.path.basename(addon)
                            
                            if 'Zero_Brush' not in addon:
                                if '.py' in addon:
                                    addon = addon.split('.')[0]                                
                                default, state = addon_utils.check(addon)
                                if state == False:
                                    print('activated the addon ', addon)
                                    addon_utils.enable(addon, default_set = True)
                                    needSaving = True
                            else:
                                if addon == 'Zero_Brush.py':
                                    use_zb = True     
                    
                    
                    if use_zb:                                                  
                        default, state = addon_utils.check('Zero_Brush')
                        if state is False:
                            addon_utils.enable('Zero_Brush', default_set = True)  
                            needSaving = True                            
                    else:
                        default, state = addon_utils.check('Zero_Brush_Lite')
                        if state is False:
                            addon_utils.enable('Zero_Brush_Lite', default_set = True)
                            needSaving = True       
                except:
                    pass         
                
                try: #Disable conflict keys
                    map =  ['Mesh', 'Mesh', 'Weight Paint']         
                    item = ['mesh.tris_convert_to_quads', 'transform.shrink_fatten', 'paint.weight_gradient']
                    key = ['J', 'S', 'LEFTMOUSE']

                    keyConfig = bpy.context.window_manager.keyconfigs.active
                    x = 0
                    for i in map: #Remove things
                        for this in keyConfig.keymaps[map[x]].keymap_items:
                            
                            if item[x] == this.idname:
                                if key[x] in this.type:                                             
                                    if this.active:
                                        this.active = False
                                    break
                        x += 1
                    
                    #Add keys which require activation
                    keys = wm.keyconfigs.active.keymaps['Knife Tool Modal Map'].keymap_items                    
                    if 'S' not in keys:
                        keys.new_modal('IGNORE_SNAP_ON', 'S', 'PRESS')                    
                        keys.new_modal('IGNORE_SNAP_OFF', 'S', 'RELEASE')      
                    
                    
                    #Adjust key settings
                    keys = wm.keyconfigs.active.keymaps['3D View'].keymap_items
                    for key in keys:
                        if key.type == 'SELECTMOUSE':
                            if key.shift:
                                if key.ctrl:
                                    if hasattr(key.properties, 'center'):
                                        key.properties.center = False
                                        break                                                                   
                except:
                    pass
                                  
                
                try: #Initialize various options
                    scene = bpy.context.scene
                    world = scene.world.light_settings

                    for screen in bpy.data.screens:
                        #Timeline options
                        screen.use_follow = True

                        for area in screen.areas:
                            if area.type == 'VIEW_3D':
                                
                                if area.spaces[0].lock_camera:
                                    fx = area.spaces[0].fx_settings
                                    
                                    if world.use_ambient_occlusion:
                                        fx.use_ssao = True                    
                                    if len(scene.cTarget) > 0:
                                        fx.use_dof = True                      
                except:
                    pass      
                sfStartupSettingsInit(scene)  
                                                                                             
            #Check for updates
            if scene.sfCheckForUpdates:
                sfUpdateCheckMainFunciton(sf_path)



        else:
            try: #=========================SENSEI FORMAT NEW INSTALL
                print('Installing Sensei Format')
                
                #Bypass install on master
                sf_distributor = os.path.join(addons_path, 'Sensei_Format_Distributor.py')
                if os.path.exists(sf_distributor) is False:
                    
                    #Check for Sensei Format in previous Blender
                    #versions, import instead of install if found
                    parDir = os.path.dirname(user_path)                
                    currentVersion = os.path.basename(user_path)
                    currentV = round(float(currentVersion),2)
                    
                    #Count backwards to check most recent SF install
                    usedPrevious = False
                    while currentV > 1:
                        currentV = round((currentV-.01),2)  
                        version = str(currentV)                        
                        if len(version) < 4:
                            version += '0'
                            
                        try: #Search for Sensei
                            searchPath = os.path.join(parDir, version)
                            if os.path.exists(searchPath):
                                searchPath_scripts = os.path.join(searchPath, "scripts")
                                searchPath_addons = os.path.join(searchPath_scripts, "addons")
                                sf_old_path = os.path.join(searchPath_addons, "Sensei_Format")
                                
                                if os.path.exists(sf_old_path):
                                    print('Importing Settings from ', version)                                    
                                    #Replace current settings with previous
                                    shutil.rmtree(user_path)
                                    shutil.copytree(searchPath, user_path)
                                    usedPrevious = True
                                    break
                        except:
                            pass
                        
                            
                    if usedPrevious:
                        bpy.ops.object.sf_message_system('INVOKE_DEFAULT', 
                            message = 'previous_sf_installed')                        
                    else:                        
                        #Save user pref for future de/activation
                        bpy.ops.wm.save_userpref()                        
                        
                        #Transfer Python modules
                        if os.path.exists(modules_path) is False:
                            os.makedirs(modules_path)
                            
                        modules = os.listdir(sf_modules)
                        for mod in modules:
                            sfMod = os.path.join(sf_modules, mod)
                            newMod = os.path.join(modules_path, mod)
                            
                            if os.path.exists(newMod):
                                os.remove(newMod)
                            shutil.copyfile(sfMod, newMod)
                        
                        #Get list of Sensei addons
                        addons = os.listdir(sf_addons)
                            
                                                    
                        #Replace or update addons
                        for addon in addons:
                            if 'pycache' in addon:
                                addons.remove(addon)
                            else:
                                sfAddon = os.path.join(sf_addons, addon)
                                sfAddonNewPath = os.path.join(addons_path, addon)
                                if '.py' in addon:
                                    if os.path.exists(sfAddonNewPath):
                                        os.remove(sfAddonNewPath)
                                    shutil.copyfile(sfAddon,sfAddonNewPath)
                                else:
                                    if os.path.exists(sfAddonNewPath):
                                        shutil.rmtree(sfAddonNewPath)
                                    shutil.copytree(sfAddon,sfAddonNewPath)
                            
                        #Create Install Switch
                        iSwitch = open(installSwitch1, "w")
                        iSwitch.close()
                        
                        #Display intro message to user
                        bpy.ops.object.sf_message_system('INVOKE_DEFAULT', 
                        message = 'sensei_installed')
                            
                    
            except: #IF INSTALL FAIL
                try:#Shut off Initialization
                    for map in wm.keyconfigs.addon.keymaps:               
                        ki = map.keymap_items              
                        for key in ki: 
                            if 'Sensei Format Initialization' in key.name:
                                key.active = False
                                break 
                    del addon_keymaps[:] 
                except:
                    pass
                                     
                bpy.ops.object.sf_message_system('INVOKE_DEFAULT', 
                message = 'unable_to_install')
                        
            
        #Shut off Initialization
        for map in wm.keyconfigs.addon.keymaps:               
            ki = map.keymap_items              
            for key in ki: 
                if 'Sensei Format Initialization' in key.name:
                    key.active = False
                    break 
        del addon_keymaps[:]
     
        return {'FINISHED'}

        
        
#Sensei Format options in Blender File menu
def sfFileMenu(self,context):
    scene = bpy.context.scene
    
    if hasattr(scene, 'sfShapeToolsMeta') is False:      
        layout = self.layout      
        layout.menu("menu.sf_options_menu", icon = 'MONKEY')
        layout.separator()   


#Sensei Format options menu
class sfOptionsMenu(bpy.types.Menu):
    bl_idname = "menu.sf_options_menu"
    bl_label = "Sensei Format"
    bl_description = "Sensei Format options"
    
    def draw(self,context):
        scene = bpy.context.scene
        
        user_path = bpy.utils.resource_path('USER')
        scripts_path = os.path.join(user_path, "scripts")
        addons_path = os.path.join(scripts_path, "addons")
        sf_path = os.path.join(addons_path, "Sensei_Format")
        sf_activated = os.path.join(sf_path, "senseiActivated.txt")
        
        layout = self.layout  
        
        layout.operator("wm.url_open", text="View Manual", icon='QUESTION').url = "https://blendersensei.com/sensei-format-user-manual/"
        layout.operator("wm.url_open", text="View Hotkeys", icon='QUESTION').url = "https://blendersensei.com/sensei-format-hotkeys/"
        layout.separator()
        layout.operator("wm.url_open", text="Training Videos", icon='QUESTION').url = "https://youtube.com/user/blendersensei"
        layout.operator("wm.url_open", text="Ask A Question", icon='QUESTION').url = "https://blendersensei.com/forums/"
        layout.separator()
 
 
        
        if scene.sfLatestBlender > 0:
            layout.operator("object.sf_message_system", text = 'Update Blender Now', icon='FILE_REFRESH').message = 'update_blender'
            
            try:            
                blend = str(scene.sfLatestBlender)
                s1 = blend[0]
                s2 = blend[1:3]
                blend = s1 + '-' + s2 + '/'
                featURL = 'http://blender.org/features/' + blend
                
                layout.operator("wm.url_open", text="Read About Update", icon='QUESTION').url = featURL
            except:
                pass
 
        if scene.sfLatestSenseiFormat > 0:
            if os.path.exists(sf_activated):
                layout.operator("object.sf_message_system", text = 'Update Sensei Now', icon='FILE_REFRESH').message = 'update_sensei'
                layout.operator("wm.url_open", text="Read About Update", icon='QUESTION').url = "https://blendersensei.com/sensei-format-update-log/"
                
                
                
        if os.path.exists(sf_activated):        
            layout.operator("object.sf_message_system", text = 'Deactivate Sensei', icon ='CHECKBOX_DEHLT').message = 'deactivate_sensei'
        else:
            layout.operator("object.sf_message_system", text = 'Activate Sensei', icon ='CHECKBOX_DEHLT').message = 'activate_sensei' 
            
        layout.prop(scene, "sfCheckForUpdates", text="Check For Updates")
        
        layout.separator()
        layout.operator("object.sf_message_system", text = 'Full Uninstall', icon='X').message = 'uninstall_sensei'
        
        #Sensei Format version info
        sfVersion = ''
        for mod in addon_utils.modules():
            if mod.bl_info.get('name') == 'Sensei Format':
                sfVersion = str(mod.bl_info.get('version'))
                sfVersion = sfVersion.strip('()')
                sfVersion = sfVersion.replace(',','')
                sfVersion = sfVersion[:2] + '.' + sfVersion[1:]
                                    
                break       
            
            
        layout.operator("object.sf_manual_update", 
        text = 'Manual Update', icon='LOOP_FORWARDS')
        
        layout.operator("object.sf_message_system", 
        text = 'Reset Layout', icon='LOOP_FORWARDS').message = 'reload_defaults'
        layout.operator("wm.url_open", text="Sensei  " + sfVersion, 
        icon='MESH_MONKEY').url = "https://blendersensei.com/sensei-format-update-log/"
        



#Manual update
class sfManualUpdate(bpy.types.Operator, ImportHelper):
    bl_idname = "object.sf_manual_update"
    bl_label = "Update Sensei Format"
    bl_description = "Select a Sensei Format zip file and manually update Sensei Format (file will close after updating)"

    def execute(self, context):
        userMsg = sfManualUpdate(context, self.filepath)
        
        if len(userMsg) > 0:
            self.report({'INFO'}, userMsg)
            
        return {'FINISHED'}


def sfManualUpdate(context, filepath):    
    scene = bpy.context.scene
    userMsg = ''
    
    if len(filepath) > 3:
        if filepath.endswith('Sensei_Format.zip'):
            user_path = bpy.utils.resource_path('USER')
            scripts_path = os.path.join(user_path, "scripts")
            config_path = os.path.join(user_path, "config")
            addons_path = os.path.join(scripts_path, "addons")
            sf_path = os.path.join(addons_path, "Sensei_Format")
            sf_scripts = os.path.join(sf_path, "scripts")
            sf_presets = os.path.join(sf_scripts, "presets")
            sf_interface_theme = os.path.join(sf_presets, "interface_theme")      
            sf_addons = os.path.join(sf_scripts, "addons")
            
            sf_activated = os.path.join(sf_path, "senseiActivated.txt")
            installSwitch1 = os.path.join(sf_path,"installSwitch1.txt")
            installSwitch2 = os.path.join(sf_path,"installSwitch2.txt")
            
            sf_update_zip = filepath

            #Unzip, replace and delete zip
            if os.path.exists(sf_path):
                shutil.rmtree(sf_path)
            
            if os.path.exists(sf_update_zip):        
                shutil.unpack_archive(sf_update_zip, addons_path, 'zip')

                                    
                #UPDATE ADDONS
                addons = os.listdir(sf_addons)

                #Replace or update addons
                for addon in addons:
                    if 'pycache' in addon:
                        addons.remove(addon)
                    else:
                        sfAddon = os.path.join(sf_addons, addon)
                        sfAddonNewPath = os.path.join(addons_path, addon)
                        if '.py' in addon:
                            if os.path.exists(sfAddonNewPath):
                                os.remove(sfAddonNewPath)
                            shutil.copyfile(sfAddon,sfAddonNewPath)
                        else:
                            if os.path.exists(sfAddonNewPath):
                                shutil.rmtree(sfAddonNewPath)
                            shutil.copytree(sfAddon,sfAddonNewPath)

                
                if os.path.exists(installSwitch1):
                    os.remove(installSwitch1)
                if os.path.exists(installSwitch2):
                    os.remove(installSwitch2)
                    
                #Create install switches
                iSwitch = open(installSwitch1, "w")
                iSwitch.close()
                iSwitch2 = open(installSwitch2, "w")
                iSwitch2.close()
                
                if os.path.exists(sf_activated) is False:
                    sa = open(sf_activated, "w")
                    sa.close()
                        
                #Activate new theme
                theme_path = os.path.join(sf_interface_theme, "sensei.xml")
                bpy.ops.wm.theme_install(overwrite=True, filepath=theme_path)
                
                #Quit Blender to be restarted
                bpy.ops.wm.quit_blender()
            

        else:
            userMsg = 'The selected file must be a "Sensei_Format.zip" file from blendersensei.com'
    else:
        userMsg = 'You did not select a file to update Sensei Format'
    
    return userMsg
            
    
    



 
#Messages    
class sfMessageSystem(bpy.types.Operator):
    bl_idname = "object.sf_message_system"
    bl_label = ""
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = 'Activate or deactivate Sensei Format'
    
    message = bpy.props.StringProperty()
    width = bpy.props.IntProperty()
    
    def execute(self, context):
        message = self.message
        

        if 'sensei_installed' in message:
            bpy.ops.object.sf_menu_options(option = 'activate')
        
        if message == 'unable_to_install':
            bpy.ops.wm.quit_blender()
            
        if message == 'activate_sensei':
            bpy.ops.object.sf_menu_options(option = 'activate')
        
        if message == 'deactivate_sensei':
            bpy.ops.object.sf_menu_options(option = 'deactivate')
        
        if message == 'uninstall_sensei':
            bpy.ops.object.sf_menu_options(option = 'deactivate_uninstall')
        
        if message == 'update_blender':
            bpy.ops.object.sf_menu_options(option = 'update_blender')
        
        if message == 'previous_sf_installed':
            bpy.ops.wm.quit_blender()
        
        if message == 'update_sensei':
            bpy.ops.object.sf_menu_options(option = 'update_sensei')
        
        if message == 'reload_defaults':
            bpy.ops.object.sf_menu_options(option = 'reload_defaults')
            
        return {'FINISHED'}

    
    def draw(self, context):
        message = self.message
        layout = self.layout
        
        sub = layout.column()
        sub.scale_y = 0.75
        
        
        if message == 'reload_defaults':
            sub.separator()
            sub.label("This will reset the default Sensei Format startup file. Use this if you", icon='MONKEY')
            sub.label("changed and saved over something in Sensei Format that you need back or")
            sub.label("to have the newest version of Sensei Format's layout overwrite your old")
            sub.label("one. You may need to reactivate some addons after performing this action.")
            sub.label("Sensei Format needs to shut down Blender to reset the startup file.")
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label("RELOAD SENSEI FORMAT LAYOUT NOW?", icon = 'QUESTION')
            sub = sub.column()
        
        
        if message == 'unable_to_install':
            sub.label('UNABLE TO INSTALL SENSEI FORMAT', icon='MONKEY')
            sub.separator()
            sub.separator()
            sub.label('Something went wrong while trying to install Sensei Format') 
            sub.label("Here's a few things you may wish to try to get it working: ") 
            sub.separator()
            sub.separator()
            sub.label("• You don't need to manually move the Sensei Format addon")
            sub.label("  to your addons directory. In fact, this may be your problem")
            sub.label("  if you manually placed the addon in your addons folder, try")
            sub.label("  removing the addon folder from that location then download")
            sub.label("  the Sensei Format addon again, and this time just install it")
            sub.label("  from your desktop, downloads folder, or anywhere that's not")
            sub.label("  your Blender addons folder. Blender will import it for you.")
            sub.separator()
            sub.separator()
            sub.label("• The Sensei Format addon MUST REMAIN ZIPPED, when you go to")
            sub.label('  press "Install From File" in the Blender addons menu. Some')
            sub.label('  browsers (such as Safari) automatically unzip downloaded files')
            sub.label("  if this is the case, you'll need to disable this within the browser's")
            sub.label("  settings or simply re-zip the addon once downloaded.")
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label("• Blender must now be restarted. For more help visit the forums")
            sub.label("  section at blendersensei.com")
            sub = sub.column()
            
        if message == 'sensei_installed':
            sub.label('SENSEI FORMAT SUCCESSFULLY INSTALLED', icon='MONKEY')
            sub.separator()
            sub.separator()
            sub.label('You can activate or deactivate Sensei Format any time by selecting') 
            sub.label('"Sensei Format" in the File menu. If you are using additional addons') 
            sub.label('you will need to reactivate them in the user preferences once Sensei')
            sub.label('Format has been activated. This only needs to be done once. Any')
            sub.label('changes you make to your default Blender settings or Sensei Format')
            sub.label('settings will be stored seperately and fully restored when switching')
            sub.label('between default Blender and Sensei Format.')
            sub.label('')
            sub.label('Click "Sensei Format" in the File menu to view hotkeys, get started') 
            sub.label('with the Blender Crash Course tutorial series or download the manual.')
            sub.label('Blender will shut down after activating Sensei Format.')
            sub.label('')
            sub.label('ACTIVATE SENSEI FORMAT NOW?', icon='QUESTION')
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.operator('object.sf_menu_options', text='NO').option = 'cancel'
            sub = sub.column()
            
        if message == 'sensei_installed_sf_user':            
            sub.separator()
            sub.label('SENSEI FORMAT SUCCESSFULLY INSTALLED', icon='MONKEY')
            sub.separator()
            sub.separator()
            sub.label("Hi. Looks like you were using some previous version of Sensei Format.") 
            sub.label("If you decide not to activate Sensei Format by pressing OK bellow, you'll") 
            sub.label("need to restart Blender (or simply press NO bellow) to let the new Sensei")
            sub.label('Format finish tidying up the place. Or just activate now by pressing OK.')
            sub.separator()
            sub.separator()
            sub.label('You can activate or deactivate Sensei Format any time by selecting') 
            sub.label('"Sensei Format" in the File menu. You can also view hotkeys, get') 
            sub.label('started with the tutorial series or visit the forums for more help.')
            sub.separator()
            sub.separator()
            sub.label('Blender will shut down after activating or deactivating Sensei Format.')
            sub.label("Don't worry, all your current themes, workspaces, hotkeys, addons and")
            sub.label("settings are saved when switching between Sensei and regular Blender.")
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label('ACTIVATE SENSEI FORMAT NOW?', icon='QUESTION')
            sub.operator('object.sf_menu_options', text='NO').option = 'cancel'
            sub = sub.column()
            
            
        if message == 'activate_sensei':
            sub.separator()
            sub.label("Sensei Format needs to shut down Blender to activate. If you're working", icon='MONKEY')
            sub.label("on a file, then you should save it before switching to Sensei Format.")
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label("ACTIVATE SENSEI FORMAT NOW?", icon = 'QUESTION')
            sub = sub.column()
            
        if message == 'deactivate_sensei':
            sub.separator()
            sub.label("Sensei Format needs to shut down Blender to activate your old settings. If", icon='MONKEY')
            sub.label("you're working on a file, then you should save it before deactivating.")
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label("DEACTIVATE SENSEI FORMAT NOW?", icon = 'QUESTION')
            sub = sub.column()
            
        if message == 'uninstall_sensei':            
            sub.label('Sensei Format needs to shut down Blender to fully uninstall. All, settings,', icon='MONKEY')
            sub.label(' hotkeys and addons will be removed. You can re-install Sensei Format any')
            sub.label(' time. You can always download the latest version free at blendersensei.com')
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label('FULLY UNINSTALL SENSEI FORMAT?', icon='QUESTION')
            sub = sub.column()
            
        if message == 'update_blender':
            sub.label('There is a new version of Blender available. If you wish to install', icon='MONKEY')
            sub.label("it press OK and you will be taken to Blender's download page to select")
            sub.label("and download the latest version of Blender for your computer.")
            sub.separator()
            sub.separator()
            sub.label('Sensei Format will transfer all your settings for you. Just download')
            sub.label('and install Blender as you normally would, then when you open Blender')
            sub.label("back up, you'll have immediate access to Sensei Format, your addons,")
            sub.label("workspaces, themes and all your settings.")
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label("UPDATE BLENDER NOW?", icon='QUESTION') 
            sub = sub.column()
            
        if message == 'update_sensei':
            sub.label('An update to Sensei Format has been released. Updating will require', icon='MONKEY')
            sub.label("Blender to be shut down. If you're working on anything, you should save")
            sub.label('it first before updating.')
            sub.separator()
            sub.separator()
            sub.label('Please allow one to two minutes for the updates to download and install.')
            sub.label("When finished, Blender will shut itself down and you may open it again.")
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label('UPDATE SENSEI FORMAT NOW?', icon='QUESTION')
            sub = sub.column()
            
        if message == 'previous_sf_installed':            
            sub.label('Your settings from a previous version of Blender were', icon='MONKEY')
            sub.label("found and transferred to the new version you just installed. This was")
            sub.label("done so that your Blender settings from before you installed Sensei")
            sub.label("Format will remain available if ever you need to deactivate Sensei")
            sub.label('Format via File > Sensei Format > Deactivate Sensei.')
            sub.label('')
            sub.label('If you were trying to update to a new version of Sensei Format then')
            sub.label('after this message is closed, you will need to go to File > Sensei')
            sub.label('Format > and press "Manual Update", then select the newest zip file')
            sub.label('of Sensei Format you have to finish updating.')
            sub.label('')
            sub.label('You can avoid the hassle next time Blender or Sensei Format needs to')
            sub.label('update by check marking "Check For Updates" in the Sensei Format menu')
            sub.label('and then saving your startup file to keep your changes.')
            sub.label('')
            
            sub = sub.column()
            sub.scale_y = 1.09
            sub.label("SHUTDOWN BLENDER NOW", icon='QUESTION') 
            sub = sub.column()
            
    def invoke(self, context, event):
        width = self.width
        if width < 1:
            width = 410
        return context.window_manager.invoke_props_dialog(self,width)
        

        
        
#REGISTRATION==========================
class sfAddonProperties(bpy.types.PropertyGroup):
    wm = bpy.context.window_manager
    scene = bpy.types.Scene
    
    text1 = 'Check once a day for new versions of Blender and Sensei Format at'
    text2 = ' Blender startup. Only official, stable releases of Blender are checked'
    text3 = ' for. You will be notified in the header menu if an update is available.'
    message = text1 + text2 + text3
    
    scene.sfCheckForUpdates = bpy.props.BoolProperty(
    default = True,    
    description = message,
    update = sfCheckForUpdates
    )
    
    scene.sfLatestBlender = bpy.props.IntProperty(default = 0)
    scene.sfLatestSenseiFormat = bpy.props.IntProperty(default = 0)
    
        
addon_keymaps = []
def register():    
    bpy.utils.register_module(__name__)
    wm = bpy.context.window_manager
    
    try:
        #Create keymaps
        km = wm.keyconfigs.addon.keymaps.new(name='Screen', space_type='EMPTY')
        kmi = km.keymap_items.new("object.sensei_format_init", 'MOUSEMOVE', 'ANY')
        addon_keymaps.append(km)
        
        #Append Sensei menu to file menu
        bpy.types.INFO_MT_file.prepend(sfFileMenu)
    except:
        pass
        
def unregister():
    bpy.utils.unregister_module(__name__)
    wm = bpy.context.window_manager
    
    try:
        bpy.types.INFO_MT_file.remove(sfFileMenu)
        bpy.types.INFO_HT_header.remove(newBlendAvailable)
    except:
        pass
    try:
        bpy.app.handlers.load_post.remove(sfStartupSettingsInit)
    except:
        pass
    
    
    #Unregister keymaps
    for km in addon_keymaps:
        try:
            wm.keyconfigs.addon.keymaps.remove(km)
        except:
            pass
    del addon_keymaps[:]
       
if __name__ == "__main__":
    register()