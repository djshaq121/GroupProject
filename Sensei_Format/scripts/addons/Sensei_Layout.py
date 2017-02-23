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
 "name": "Sensei Layout",
 "author": "Blender Sensei",
 "location": "All over.",
 "description": "Layout tweaks from your friendly neighborhood Blender Sensei.",
 "wiki_url": "http://blendersensei.com",
 "category": "Sensei Format"}

import zlib
i_0 = b'x\xda}T\xc1n\xdb0\x0c\xfd\x15\xee\xd6\x02C\x0f\xcde\xd74qQ/n\xdd\xc5F\xb6\x9d\x04\xc5\xa6\x13\xb5\xb2dHr\xd3\x00\xfb\xf8Q\x8eb\'\x86\xd1\x8b-\xf2\xf1\x89\xa4\x1e\xa5G!\x91\xdd\xdf\x7f\xfb\xc1\x96\xe9k\x94=EQ\xce\xa2e\x9c\xa7\xeb\xb1\xf79gX\n\xa7\r\xabQ\xb5\xf6\x04\x9f\xbey\xf4\xe7\x9a\xd59\xbe \xe8\xed\x1b\x16\xee\xceV\x8c7\x8d<2\xb7\xc7\x1aY\xa1%\x05w\x01\xd9\xe3\n\xe6\x1e\x82\x0c%\x85\n\xad`1\xc0k\xb4\xe8@\x1b\xe8\xe8@t\x8b\xd0\xd1-\x19F\xb7\xbb\xbdn\x1d-\x85\xb7\xfd\xde\xe3\xb4\x966\xb0\xcc`e\xd0\xee/rv~H\xc4\xd6ps\x84\xf5%\x1e\x0c\xb4pb\x83\x0cQ\x1f\x02\x0f\xe3\x04R\xa8w\xdf\x1c\xaar\xd8=!\xa7o\xabw\xd2\xe1\xbe@\x12?\xac\xe7\xeb\xbf\xf0\x0f\xb2\xf9&\x82\xfc)\xce\xe01N"r$\xf1\xcb\nnlw\x04XBEb\xc1\x16\xa5>\xdc\x128\x7f%\xf6r\x12\xfe\x0e\\Z\r\xa2n\xb4\xa1B=`o\xc7%ny\xf1\xce\x9cf\xb3rh\xc0W\xf9@~\xc85\xcc\x96\xb0\xe9\x81M\x1c\xfdf\xb3e\x907M\x93\xec\xb4\x9c+Qs/\xcf\xe5\xee\xb5.\xc3\x89G\x9f\x8e\x9a\xa5\xdar\xad\xa5\x1dW\xf0\x8e\xc7\xcapR\xc7\r\xa8\xaf`\x15\xfc\x97\xacy\xf9\xd6Z\x07\xfc\x9c\x0f\xce\xe4\x80/hi8\xa4\x8d\x07\x83\xcf\xcf\x9d\xcfSt\x18\xd3\x01\xf3\xee\xeb\x00)>\x90\x86\xa1\xd0\xa6\xbc@O\x92} \x8d\x81G\xe0\xb9G\xae\x93\xd1\x9f,w\x1e\xce\xa1?\xca\xdb\'\x1d\xcf\x07?\xd2\x84R2k\xf9\x0e/\xefF\xac*mB\x8f|\x1b\xc6X\xed,\xec4\xfd\x80\xbcB\xf9\xa1\x06[\xa0\n\xcc\xb4u\r\x05N6\xaf;l\xa2\xf9D\xec\xf6\xceo9I\x93\x01\x9d \xfej\x05M\xc8\xda\x0bk\xe8~:\x1f6b\x9b\x0ed\xf6\x0c\x0ed/\xe0\x95\xf6om\xddLH\xff\xb3w\xfb\x158\xdd\xf5\xac\xf0\xd3\xf5\xca\xc3\r\xbd\x00{.+\xb0$\x90*AT\xa04\xd4\xda\xe00\x1da\xecsQ#\xddI\x9cn\xd6\x05\xf4Z\xadC}\'h_&H\x91\xa0\r\x99\x10\xf7\xe6B\xfa\x83\xa0\xd2\n\xdd\x1cO\xaf\x8d\'\x80\xf2\xc5\x85\x8a\x0b)\x9a\xad\xe6&\xdc\xf8E\xfa\x92\xa5I\xf4\xd5\xe3x\x0e\xe9\x8c\xff4\xa8\xf2\xb3'
i_1 = b'x\xda\x03\x00\x00\x00\x00\x01'
a = str(zlib.decompress(i_0))[2:]
i_0 = a.split('_22!8_')
b = str(zlib.decompress(i_1))[2:]
i_1 = b.split('_22!8_')
import bpy, math, os, shutil, addon_utils,colorsys
from bpy.types import Panel, Header, Menu
from bpy.app import handlers
from bpy.app.translations import pgettext_iface as iface_
def fu0():
    d = bpy.data
    item = [d.images,d.textures,d.node_groups,d.materials,d.speakers,d.texts,
            d.groups,d.lamps,d.lattices,d.armatures,d.metaballs,d.movieclips,
            d.worlds,d.particles,d.scenes,d.sounds,d.meshes,d.objects]
    for i in item:
        for ob in i:
            if ob.users < 1:                
                if 'RigidBody' not in ob.name:
                    try:
                        i.remove(ob, do_unlink = True)
                    except:
                        try:
                            i.remove(ob)
                        except:
                            pass
def fu1(mode):
    if 'EDIT' in mode:
        mode = 'EDIT'
    if 'TEXTURE' in mode:
        mode = 'TEXTURE_PAINT'
    if 'VERTEX' in mode:
        mode = 'VERTEX_PAINT'
    if 'WEIGHT' in mode:
        mode = 'WEIGHT_PAINT'    
    try:
        bpy.ops.object.mode_set(mode= mode)
    except:
        pass
    return
def fu2(target):
    override = 0
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == target:
                override = {'window': window, 'screen': screen, 'area': area}
                break                   
    return override
class INFO_MT_file(Menu):
    bl_label =i_0[0]
    def draw(self, context):
        layout = self.layout      
        layout.menu("menu.sf_options_menu", icon = 'MONKEY')
        layout.separator() 
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.read_homefile", text="New", icon='NEW').load_ui = True
        layout.operator("wm.open_mainfile", text="Open...", icon='FILE_FOLDER')
        layout.menu("INFO_MT_file_open_recent", icon='OPEN_RECENT')
        layout.operator("wm.revert_mainfile", icon='FILE_REFRESH')
        layout.operator("wm.recover_last_session", icon='RECOVER_LAST')
        layout.operator("wm.recover_auto_save", text="Recover Auto Save...", icon='RECOVER_AUTO')
        layout.separator()
        layout.operator_context = 'EXEC_AREA' if context.blend_data.is_saved else 'INVOKE_AREA'
        layout.operator("wm.save_mainfile", text="Save", icon='FILE_TICK')
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save As...", icon='SAVE_AS')
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_as_mainfile", text="Save Copy...", icon='SAVE_COPY').copy = True
        layout.separator()
        layout.operator("screen.userpref_show", text="User Preferences...", icon='PREFERENCES')
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.save_homefile", icon='SAVE_PREFS')
        layout.operator("wm.read_factory_settings", icon='LOAD_FACTORY')
        layout.separator()
        layout.operator_context = 'INVOKE_AREA'
        layout.operator("wm.link", text="Link", icon='LINK_BLEND')
        layout.operator("wm.append", text="Append", icon='APPEND_BLEND')
        layout.menu("INFO_MT_file_previews")
        layout.separator()
        layout.menu("INFO_MT_file_import", icon='IMPORT')
        layout.menu("INFO_MT_file_export", icon='EXPORT')
        layout.separator()
        layout.menu("INFO_MT_file_external_data", icon='EXTERNAL_DATA')
        layout.separator()
        layout.operator_context = 'EXEC_AREA'
        if bpy.data.is_dirty and context.user_preferences.view.use_quit_dialog:
            layout.operator_context = 'INVOKE_SCREEN'  
        layout.operator("wm.quit_blender", text="Quit", icon='QUIT')
class DOPESHEET_HT_header(Header):
    bl_space_type =i_0[1]
    def draw(self, context):      
        scene = bpy.context.scene
        screen = bpy.context.screen  
        st = context.space_data
        toolsettings = context.tool_settings
        area = bpy.context.area    
        hideAnim = False
        layout = self.layout
        row = layout.row(align=True)
        if area.y < 10:                
            sub = row.row(align=True)
            sub.scale_x = 0.675
            sub.prop_search(scene.keying_sets_all, "active", scene, "keying_sets_all", text="")
            sub = row.row(align=True)
            sub.scale_x = 0.33
            sub.operator('action.interpolation_type', text ='')
            row.scale_x = 1
            row.prop(toolsettings, "use_keyframe_insert_auto", text="", toggle=True)
            row = layout.row(align=True)
            row.operator("screen.frame_jump", text="", icon='REW').end = False
            row.operator("anim.sf_keyframe_jump", text="", icon='PREV_KEYFRAME').func = 'reverse'
            if not screen.is_animation_playing:
                if scene.sync_mode == 'AUDIO_SYNC' and context.user_preferences.system.audio_device == 'JACK':
                    sub = row.row(align=True)
                    sub.scale_x = 2.25
                    sub.operator("screen.animation_play", text="", icon='PLAY')
                else:
                    sub = row.row(align=True)
                    sub.scale_x = 2.25
                    sub.operator("screen.animation_play", text="", icon='PLAY')
            else:
                sub = row.row(align=True)
                sub.scale_x =2.25
                sub.operator("screen.animation_play", text="", icon='PAUSE')
            row.operator("anim.sf_keyframe_jump", text="", icon='NEXT_KEYFRAME').func = 'forward'
            row.operator("anim.sf_keyframe_jump", text="", icon='FF').func = 'last'
            row.separator()
            sub = row.row(align=True)
            sub.scale_x = 0.65
            if not scene.use_preview_range:
                sub.prop(scene, "frame_start", text="Start")
                sub = row.row(align=True)
                sub.scale_x = 1
                sub.prop(bpy.context.scene, 'use_preview_range',text='')
                sub = row.row(align=True)
                sub.scale_x = 0.75
                sub.prop(scene, "frame_end", text="End")
            else:
                sub.prop(scene, "frame_preview_start", text="Start")
                sub = row.row(align=True)
                sub.scale_x = 1
                sub.prop(bpy.context.scene, 'use_preview_range',text='')
                sub = row.row(align=True)
                sub.scale_x = 0.8
                sub.prop(scene, "frame_preview_end", text="End")
            row.separator()
            rd = context.scene.render
            sub = row.row(align=True)
            sub.scale_x = 0.725
            sub.prop(rd, "fps")
            sub = row.row(align=True)
            sub.scale_x = 0.48
            sub.operator("wm.call_menu", icon="BLANK1", text="").name = "menu.sf_timeline_options"
            sub = row.row(align=True)
            sub.scale_x = 0.725
            sub.prop(scene, "frame_current", text="FR")
            sub.separator()
            row = layout.row(True)
            row.scale_x = 0.8
            row.operator('object.sf_insert_key',text='',icon='SPACE2')
            row.operator('object.sf_keyframe_tools', text = 'Reverse').tool = 'REVERSE'            
            row.operator('object.sf_keyframe_tools', text = 'Mirror').tool = 'MIRROR'
            DOPESHEET_MT_editor_menus.draw_collapsible(context, layout)
            layout.prop(st, "mode", text="")
            row = layout.row(align=True)
            if st.mode in {'ACTION', 'SHAPEKEY'}:                
                row.operator("action.layer_prev", text="", icon='TRIA_DOWN')
                row.operator("action.layer_next", text="", icon='TRIA_UP')
                layout.template_ID(st, "action", new="action.new", unlink="action.unlink")
                row = layout.row(align=True)
                row.operator("action.push_down", text="", icon='NLA_PUSHDOWN')
                row.operator("action.stash", text="", icon='FREEZE')
            if st.mode == 'DOPESHEET':
                row.prop(st.dopesheet, "show_only_selected", text="")
            elif st.mode == 'ACTION':
                row = layout.row(True)
                row.prop(st.dopesheet, "show_only_selected", text="")
            elif st.mode == 'GPENCIL':
                row.prop(st.dopesheet, "show_only_selected", text="")
            row.prop(toolsettings, "use_proportional_action",
            text="", icon_only=True)            
            if toolsettings.use_proportional_action:
                row.prop(toolsettings, "proportional_edit_falloff",
                         text="", icon_only=True)
        else:      
            row.template_header() 
            DOPESHEET_MT_editor_menus.draw_collapsible(context, layout)
            layout.prop(st, "mode", text="")
            if st.mode in {'ACTION', 'SHAPEKEY'}:
                row = layout.row(align=True)
                row.operator("action.layer_prev", text="", icon='TRIA_DOWN')
                row.operator("action.layer_next", text="", icon='TRIA_UP')
                layout.template_ID(st, "action", new="action.new", unlink="action.unlink")
                row = layout.row(align=True)
                row.operator("action.push_down", text="Push Down", icon='NLA_PUSHDOWN')
                row.operator("action.stash", text="Stash", icon='FREEZE')
            layout.prop(st.dopesheet, "show_summary", text="Summary")
            if st.mode == 'DOPESHEET':
                fu4(layout, context)
            elif st.mode == 'ACTION':
                fu4(layout, context, genericFiltersOnly=True)
            elif st.mode == 'GPENCIL':
                row = layout.row(align=True)
                row.prop(st.dopesheet, "show_gpencil_3d_only", text="Active Only")
                if st.dopesheet.show_gpencil_3d_only:
                    row = layout.row(align=True)
                    row.prop(st.dopesheet, "show_only_selected", text="")
                    row.prop(st.dopesheet, "show_hidden", text="")
                row = layout.row(align=True)
                row.prop(st.dopesheet, "use_filter_text", text="")
                if st.dopesheet.use_filter_text:
                    row.prop(st.dopesheet, "filter_text", text="")
            row = layout.row(align=True)
            row.prop(toolsettings, "use_proportional_action",
                     text="", icon_only=True)
            if toolsettings.use_proportional_action:
                row.prop(toolsettings, "proportional_edit_falloff",
                         text="", icon_only=True)
            if st.mode != 'GPENCIL':
                layout.prop(st, "auto_snap", text="")
            row = layout.row(align=True)
            row.operator("action.copy", text="", icon='COPYDOWN')
            row.operator("action.paste", text="", icon='PASTEDOWN')
            if st.mode not in ('GPENCIL', 'MASK'):
                row.operator("action.paste", text="", icon='PASTEFLIPDOWN').flipped = True
class DOPESHEET_MT_editor_menus(Menu):
    bl_idname =i_0[2]
    bl_label =i_0[3]
    def draw(self, context):
        self.fu3(self.layout, context)
    @staticmethod
    def fu3(layout, context):
        st = context.space_data
        layout.menu("DOPESHEET_MT_view")
        layout.menu("DOPESHEET_MT_select")
        layout.menu("DOPESHEET_MT_marker")
        if st.mode == 'DOPESHEET' or (st.mode == 'ACTION' and st.action is not None):
            layout.menu("DOPESHEET_MT_channel")
        elif st.mode == 'GPENCIL':
            layout.menu("DOPESHEET_MT_gpencil_channel")
        if st.mode != 'GPENCIL':
            layout.menu("DOPESHEET_MT_key")
        else:
            layout.menu("DOPESHEET_MT_gpencil_frame")
def fu4(layout, context, genericFiltersOnly=False):
    dopesheet = context.space_data.dopesheet
    is_nla = context.area.type == 'NLA_EDITOR'
    row = layout.row(align=True)
    row.prop(dopesheet, "show_only_selected", text="")    
    row.prop(dopesheet, "show_hidden", text="")
    if is_nla:
        row.prop(dopesheet, "show_missing_nla", text="")
    else:  
        row.prop(dopesheet, "show_only_errors", text="")
    if not genericFiltersOnly:
        if bpy.data.groups:
            row = layout.row(align=True)
            row.prop(dopesheet, "show_only_group_objects", text="")
            if dopesheet.show_only_group_objects:
                row.prop(dopesheet, "filter_group", text="")
    if not is_nla:
        row = layout.row(align=True)
        row.prop(dopesheet, "show_only_matching_fcurves", text="")
        if dopesheet.show_only_matching_fcurves:
            row.prop(dopesheet, "filter_fcurve_name", text="")
    else:
        row = layout.row(align=True)
        row.prop(dopesheet, "use_filter_text", text="")
        if dopesheet.use_filter_text:
            row.prop(dopesheet, "filter_text", text="")
    if not genericFiltersOnly:
        row = layout.row(align=True)
        row.prop(dopesheet, "show_datablock_filters", text="Filters")
        if dopesheet.show_datablock_filters:
            row.prop(dopesheet, "show_scenes", text="")
            row.prop(dopesheet, "show_worlds", text="")
            row.prop(dopesheet, "show_nodes", text="")
            row.prop(dopesheet, "show_transforms", text="")
            if bpy.data.meshes:
                row.prop(dopesheet, "show_meshes", text="")
            if bpy.data.shape_keys:
                row.prop(dopesheet, "show_shapekeys", text="")
            if bpy.data.meshes:
                row.prop(dopesheet, "show_modifiers", text="")
            if bpy.data.materials:
                row.prop(dopesheet, "show_materials", text="")
            if bpy.data.lamps:
                row.prop(dopesheet, "show_lamps", text="")
            if bpy.data.textures:
                row.prop(dopesheet, "show_textures", text="")
            if bpy.data.cameras:
                row.prop(dopesheet, "show_cameras", text="")
            if bpy.data.curves:
                row.prop(dopesheet, "show_curves", text="")
            if bpy.data.metaballs:
                row.prop(dopesheet, "show_metaballs", text="")
            if bpy.data.lattices:
                row.prop(dopesheet, "show_lattices", text="")
            if bpy.data.armatures:
                row.prop(dopesheet, "show_armatures", text="")
            if bpy.data.particles:
                row.prop(dopesheet, "show_particles", text="")
            if bpy.data.speakers:
                row.prop(dopesheet, "show_speakers", text="")
            if bpy.data.linestyles:
                row.prop(dopesheet, "show_linestyles", text="")
            if bpy.data.grease_pencil:
                row.prop(dopesheet, "show_gpencil", text="")
class TEXT_HT_header(Header):
    bl_space_type =i_0[4]
    def draw(self, context):
        layout = self.layout
        st = context.space_data
        text = st.text
        row = layout.row(align=True)        
        if bpy.context.screen.name != 'Hacker':
            row.template_header()
        row = layout.row(align=True)
        row.operator("screen.screen_full_area", text = "",
        icon = "FULLSCREEN_ENTER")
        sub = row.row(align=True)
        sub.scale_x = 0.8
        sub.operator("text.find")
        sub = row.row(align=True)
        sub.scale_x = 1
        sub.prop(st, "find_text", text="")
        TEXT_MT_editor_menus.draw_collapsible(context, layout)
        if text and text.is_modified:
            sub = row.row(align=True)
            sub.alert = True
            sub.operator("text.resolve_conflict", text="", icon='HELP')
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.template_ID(st, "text", new="text.new", unlink="text.unlink", open="text.open")
        if bpy.context.screen.name != 'Hacker':
            row = layout.row(align=True)
            row.prop(st, "show_line_numbers", text="")
            row.prop(st, "show_word_wrap", text="")
            row.prop(st, "show_syntax_highlight", text="")
        if text:
            osl = text.name.endswith(".osl") or text.name.endswith(".oso")
            if osl:
                row = layout.row()
                row.separator()
                row.operator("node.shader_script_update")
            else:
                row = layout.row()
                row.operator("text.run_script")
                if bpy.context.screen.name != 'Hacker':
                    row = layout.row()
                    row.active = text.name.endswith(".py")
                    row.prop(text, "use_module")
            if bpy.context.screen.name != 'Hacker':
                row = layout.row()
                if text.filepath:
                    if text.is_dirty:
                        row.label(text=iface_("File: *%r (unsaved)") %
                                  text.filepath, translate=False)
                    else:
                        row.label(text=iface_("File: %r") %
                                  text.filepath, translate=False)
                else:
                    row.label(text="Text: External"
                              if text.library
                              else "Text: Internal")
class TEXT_MT_editor_menus(Menu):
    bl_idname =i_0[5]
    bl_label =i_0[6]
    def draw(self, context):
        self.fu3(self.layout, context)
    @staticmethod
    def fu3(layout, context):
        text = context.space_data.text
        layout.menu("TEXT_MT_view")
        layout.menu("TEXT_MT_text")
        if text:
            layout.menu("TEXT_MT_edit")
            layout.menu("TEXT_MT_format")
        layout.menu("TEXT_MT_templates")        
def sfCustomization(self, context):
    scene = bpy.context.scene
    layout = self.layout
    layout.prop(scene, "sfCustomization",icon="COLLAPSEMENU",text="Customize Theme")
    if scene.sfCustomization:
        row = layout.row()
        row.label("3D VIEW")
        row = layout.row(align=True)
        row.label("Selection:")
        theme = bpy.context.user_preferences.themes[0]
        view_3d = theme.view_3d
        user_interface = theme.user_interface
        properties = theme.properties
        if bpy.context.mode in 'EDIT_MESH':
            row.prop(view_3d, "edge_select", text="")
        else:
            row.prop(view_3d, "object_active", text="")
        row = layout.row()
        row.label("Background:")
        sub = row.row(align=True)
        sub.prop(view_3d.space.gradients, "show_grad", text='', icon="ARROW_LEFTRIGHT")
        if view_3d.space.gradients.show_grad:
            sub = sub.row(True)
            sub.scale_x = 0.45
            sub.prop(view_3d.space.gradients, "gradient", text="")
            sub = sub.row(True)
            sub.scale_x = 1.25
            sub.prop(view_3d.space.gradients, "high_gradient", text="")
        else:
            sub.scale_x = 1
            sub.prop(view_3d.space.gradients, "high_gradient", text="")
        row = layout.row()
        row.prop(view_3d.space, "text_hi", text="View Text")
        row = layout.row()
        row.prop(view_3d, "grid")
        row = layout.row(align=True)
        row.label("X Y Z:")
        row.separator()
        sub = row.row(align=True)
        sub.scale_x = 0.36
        sub.prop(user_interface, "axis_x", text="")
        sub.prop(user_interface, "axis_y", text="")
        sub.prop(user_interface, "axis_z", text="")
        row = layout.row()
        row = layout.row()
        row = layout.row()
        row.label("GENERAL")
        row = layout.row()
        row.prop(view_3d.space, "header", text="Headers")
        row = layout.row()
        row.prop(view_3d.space, "button", text="Shelves")
        row = layout.row()
        row.prop(properties.space, "back", text="Skin")
        row = layout.row()
        row = layout.row(align=True)
        row.operator("object.sf_apply_theme_color",
        text="Reset",icon ='FILE_REFRESH').action = 'Reset'
        row.operator("object.sf_apply_theme_color", text="Apply All").action = 'Apply'
        row = layout.row()
        sub = row.row()
        sub.scale_y = 1.4
        sub.operator("wm.save_userpref",text="Save Changes",icon="FILE_TICK")
class cl0(bpy.types.Operator):
    bl_idname =i_0[7]
    bl_label =i_0[8]
    bl_description =i_0[9]
    action = bpy.props.StringProperty(default = 'Apply')
    def execute(self,context):
        action = self.action
        theme = bpy.context.user_preferences.themes[0]
        view_3d = theme.view_3d
        timeline = theme.timeline
        graph_editor = theme.graph_editor
        dopesheet_editor = theme.dopesheet_editor
        nla_editor = theme.nla_editor
        image_editor = theme.image_editor
        sequence_editor = theme.sequence_editor
        text_editor = theme.text_editor
        node_editor = theme.node_editor
        logic_editor = theme.logic_editor
        properties = theme.properties
        outliner = theme.outliner
        user_preferences = theme.user_preferences
        info = theme.info
        file_browser = theme.file_browser
        console = theme.console
        clip_editor = theme.clip_editor
        themeAreas = [view_3d, timeline, graph_editor, dopesheet_editor, nla_editor,
        image_editor, sequence_editor, text_editor, node_editor, logic_editor,
        properties, outliner, user_preferences, info, file_browser, console,
        clip_editor]
        if action == 'Apply': 
            if bpy.context.mode in 'EDIT_MESH':
                newColor = view_3d.edge_select
            else:
                newColor = view_3d.object_active
            view_3d.clipping_border_3d = newColor[0], newColor[1], newColor[2], 0
            view_3d.object_active = newColor
            view_3d.object_selected = newColor
            view_3d.edge_select = newColor
            view_3d.vertex_select = newColor
            view_3d.face_dot = newColor
            view_3d.transform = newColor
            view_3d.nurb_sel_uline = newColor
            view_3d.nurb_sel_vline = newColor
            view_3d.lastsel_point = newColor
            view_3d.extra_face_area = newColor
            view_3d.editmesh_active = newColor[0], newColor[1], newColor[2], 0.5
            view_3d.face_select = newColor[0], newColor[1], newColor[2], 0.05
            newShelves = view_3d.space.button
            newSkins = properties.space.back
            newHeaders = view_3d.space.header
            for themeArea in themeAreas:
                try: 
                    themeArea.space.header =  newHeaders
                except:
                    pass
                try: 
                    themeArea.space.tab_active[0] = newShelves[0]
                    themeArea.space.tab_active[1] = newShelves[1]
                    themeArea.space.tab_active[2] = newShelves[2]
                    themeArea.space.tab_inactive[0] = (newShelves[0] - 0.120)
                    themeArea.space.tab_inactive[1] = (newShelves[1] - 0.120)
                    themeArea.space.tab_inactive[2] = (newShelves[2] - 0.120)
                    themeArea.space.button = newShelves
                except:
                    pass
                try:
                    if themeArea.bl_rna.name not in ["Theme File Browser", "Theme Outliner",
                    "Theme Dope Sheet", "Theme Console","Theme Timeline", "Theme Text Editor",
                    "Theme Info", "Theme Image Editor", "Theme NLA Editor",
                    "Theme Clip Editor", "Theme Graph Editor", "Theme Node Editor"]:
                        themeArea.space.back = newSkins
                except:
                    pass
        else:
            try: 
                user_path = bpy.utils.resource_path('USER')
                theme_path = os.path.join(user_path, "scripts\\presets\\interface_theme\\sensei.xml")
                bpy.ops.script.execute_preset(filepath=theme_path, menu_idname="USERPREF_MT_interface_theme_presets")
            except:
                self.report({'INFO'}, "Had trouble resetting the theme")
        return {'FINISHED'}
class cl1(bpy.types.Operator):
    bl_idname =i_0[10]
    bl_label =i_0[11]
    bl_description =i_0[12]
    @classmethod
    def poll(cls, context):
        proceed = False
        wm = bpy.context.window_manager  
        if wm.sfDisplayAssets:
            if len(bpy.context.screen.areas) > 4:
                area = bpy.context.area
                params = area.spaces[0].params  
                if params.display_type != 'THUMBNAIL':
                    if params.display_type != 'FILE_IMGDISPLAY':
                        proceed = True        
        return proceed
    def execute(self,context):  
        wm = bpy.context.window_manager
        bpy.ops.file.select('INVOKE_DEFAULT')        
        wm.sfDisplayAssets = False
        wm.sfDisplayAssets = True
        return{'FINISHED'}
def fu5(self,context):
    wm = bpy.context.window_manager    
    screen = bpy.context.window.screen
    if self.sfDisplayAssets:
        openDir = ''
        for area in screen.areas:
            if area.type == 'FILE_BROWSER':
                params = area.spaces[0].params
                openDir = params.directory
                params.use_filter_blender = False
                params.use_filter_backup = False
                params.use_filter_image = False
                params.use_filter_movie = False
                params.use_filter_script = False
                params.use_filter_font = False
                params.use_filter_sound = False
                params.use_filter_text = False                
                break        
        for area in screen.areas:
            if area.type == 'DOPESHEET_EDITOR':
                if area.y == 0:
                    area.type = 'FILE_BROWSER'
                    break 
        for area in screen.areas:
            if area.type == 'FILE_BROWSER':
                if area.y == 0:
                    try:
                        params = area.spaces[0].params                                        
                        params.directory = openDir
                        try:
                            params.display_type = 'THUMBNAIL'                            
                        except:
                            params.display_type = 'FILE_IMGDISPLAY'
                    except:
                        bpy.ops.wm.redraw_timer(type='DRAW_WIN', iterations=0)
                        params = area.spaces[0].params                                        
                        params.directory = openDir
                        try:
                            params.display_type = 'THUMBNAIL'                            
                        except:
                            params.display_type = 'FILE_IMGDISPLAY'
                        bpy.ops.file.select('INVOKE_DEFAULT')                           
                    break
    else:
        for window in wm.windows:
            screen = window.screen
            for area in screen.areas:
                if area.type == 'FILE_BROWSER':
                    if area.y == 0:
                        area.type = 'DOPESHEET_EDITOR'
                    else:
                        params = area.spaces[0].params
                        params.use_filter_blender = True
                        params.use_filter_image = True
                        params.use_filter_movie = True
                        params.use_filter_script = True
                        params.use_filter_font = True
                        params.use_filter_sound = True
                        params.use_filter_text = True    
def fu6(self,context):    
    if bpy.context.screen.name != 'Shader':
        scene = bpy.context.scene
        wm = bpy.context.window_manager    
        layout = self.layout
        row = layout.row(align=True)
        row.separator()
        row.prop(wm, 'sfDisplayAssets', text='', icon="TRIA_UP")
        if wm.sfDisplayAssets:
            row.operator('object.sf_link_append', text = '', icon = 'TRIA_DOWN').option = 'save'
            row.operator('object.sf_link_append', text = 'link', icon = 'LINK_BLEND').option = 'link'
            row.operator('object.sf_link_append', text = 'append', icon = 'APPEND_BLEND').option = 'append' 
            row.separator()         
class cl2(bpy.types.Operator):    
    bl_idname =i_0[13]
    bl_label =i_0[14]
    bl_description =i_0[15]
    option = bpy.props.StringProperty()
    def execute(self,context):
        scene = bpy.context.scene
        option = self.option
        message = ''
        screen = bpy.context.window.screen
        mode = bpy.context.mode
        matStart = len(bpy.data.materials)
        ob = bpy.context.active_object
        if ob:
            bpy.ops.object.mode_set(mode='OBJECT')
        for area in screen.areas:
            if area.type == 'FILE_BROWSER':
                if area.y == 0:
                    totalOb = []
                    for ob in bpy.data.objects:
                        totalOb.append(ob)
                    params = area.spaces[0].params
                    dir_path = params.directory
                    file_name = params.filename
                    importers = ['.blend', '.obj', '.3ds', '.fbx', '.dae', '.bvh', '.ply',
                                 '.x3d', '.wrl', '.svg']
                    zipTypes = ['bztar', 'bzip2', 'gztar', 'gzip', 'tar', 'zip']
                    if option == 'save':
                        blendFile = bpy.data.filepath                        
                        if len(blendFile) < 3:
                            fName = 'Untitled.blend'
                            ob = bpy.context.active_object 
                            if ob:
                                fName = ob.name
                                fName = fName + '.blend'
                            file_path = os.path.join(dir_path, fName)
                            bpy.ops.wm.save_mainfile(filepath = file_path)
                        else:
                            bpy.ops.wm.save_mainfile()                        
                        override = fu2('FILE_BROWSER')
                        bpy.ops.file.refresh(override)
                        message = 'Saved current file to ' + dir_path
                    if option in ['append', 'link']:                                                       
                        if len(file_name) > 2:
                            if '.' in file_name:
                                file_ext = file_name.split('.')[1].lower()
                                file_path = os.path.join(dir_path,file_name)
                                if '.' + file_ext in importers or file_ext in zipTypes:     
                                    print(file_ext, 'found in importers')
                                    if os.path.exists(file_path):
                                        newGroups = []
                                        newObjects = []
                                        li = False
                                        if file_ext in zipTypes:
                                            message = 'Imported file was unzipped'
                                            orig_path = file_path
                                            fName = file_name.split('.')[0]
                                            new_dir = os.path.join(dir_path, fName)
                                            os.makedirs(new_dir)  
                                            shutil.unpack_archive(file_path, new_dir, file_ext)
                                            digDeeper = True
                                            nothing = True
                                            children = os.listdir(new_dir)                                        
                                            for child in children:
                                                if '.' in child:
                                                    for fType in importers:                                                
                                                        if fType in child.lower():
                                                            file_name = child
                                                            file_ext = fType.lower()
                                                            file_path = os.path.join(new_dir, child)
                                                            digDeeper = False
                                                            nothing = False                                                 
                                                            if fType == '.fbx':
                                                                break                                            
                                            if digDeeper:
                                                for child in children:                                                
                                                    if '.' not in child:
                                                        child = os.path.join(new_dir, child)
                                                        if os.path.exists(child):
                                                            grandChildren = os.listdir(child)
                                                            for grandChild in grandChildren:
                                                                if nothing:
                                                                    new_dir = os.path.join(new_dir, child)
                                                                    if '.' in grandChild:
                                                                        for fType in importers:
                                                                            if fType in grandChild.lower():
                                                                                file_name = grandChild
                                                                                file_ext = fType.lower()
                                                                                file_path = os.path.join(new_dir, grandChild)                                                                            
                                                                                if fType == '.fbx':
                                                                                    nothing = False
                                                                                    break
                                                                    else:
                                                                        new_dir = os.path.join(new_dir, grandChild)
                                                                        if os.path.exists(new_dir):
                                                                            ggChildren = os.listdir(new_dir)
                                                                            for ggChild in ggChildren:
                                                                                for fType in importers:
                                                                                    if fType in ggChild.lower():
                                                                                        file_name = ggChild
                                                                                        file_ext = fType.lower()
                                                                                        file_path = os.path.join(new_dir, ggChild)
                                                                                        if os.path.exists(file_path):
                                                                                            nothing = False
                                                                                        if fType == '.fbx':
                                                                                            nothing = False
                                                                                            break 
                                            if nothing:
                                                override = fu2('FILE_BROWSER')
                                                bpy.ops.file.refresh(override)
                                                message = 'File was unzipped but file type is not yet supported'
                                            else:
                                                message = 'Imported file was unzipped and successfully loaded'
                                                if os.path.exists(orig_path):
                                                    os.remove(orig_path)         
                                        if '.obj' in file_name.lower():
                                            bpy.ops.import_scene.obj(filepath=file_path, use_image_search = True)
                                        if '.3ds' in file_name.lower():
                                            bpy.ops.import_scene.autodesk_3ds(filepath=file_path, use_image_search = True)
                                        if '.fbx' in file_name.lower():
                                            bpy.ops.import_scene.fbx(filepath=file_path, use_image_search = True)
                                        if '.dae' in file_name.lower():
                                            bpy.ops.wm.collada_import(filepath=file_path)
                                        if '.bvh' in file_name.lower():                                                                                
                                            bpy.ops.import_anim.bvh(filepath=file_path, use_fps_scale = True, global_scale = .1)
                                            scene.frame_current = 0
                                            scene.sfASnap = False
                                            bpy.ops.object.origin_set()
                                            bpy.ops.view3d.snap_selected_to_cursor()
                                        if '.ply' in file_name.lower():
                                            bpy.ops.import_mesh.ply(filepath=file_path)
                                        if '.x3d' in file_name.lower(): 
                                            bpy.ops.import_scene.x3d(filepath=file_path)
                                        if '.wrl' in file_name.lower(): 
                                            bpy.ops.import_scene.x3d(filepath=file_path)
                                        if '.svg' in file_name.lower():
                                            bpy.ops.object.select_all(action='DESELECT')
                                            curveSel = []
                                            for ob in bpy.data.objects:
                                                if ob.type == 'CURVE':
                                                    curveSel.append(ob)
                                            bpy.ops.import_curve.svg(filepath=file_path)
                                            for ob in bpy.data.objects:
                                                if ob.type == 'CURVE':
                                                    if ob not in curveSel:
                                                        ob.select = True
                                                        scene.objects.active = ob
                                            bpy.ops.object.join()
                                            ob = bpy.context.active_object
                                            ob.scale = [20,20,20]
                                            bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')                                        
                                            ob.rotation_euler[0] = 1.5708
                                            ob.name = file_name.split('.')[0]
                                        if option == 'append':
                                            li = False
                                        if option == 'link':
                                            li = True
                                        if '.blend' in file_name.lower():
                                            with bpy.data.libraries.load(file_path, link = li) as (data_from, data_to):         
                                                data_to.groups = data_from.groups                                
                                                newGroups = data_from.groups
                                            groupsToRemove = []
                                            if len(newGroups) > 0:
                                                for gr in newGroups:
                                                    if gr.objects:
                                                        removeGroup = False
                                                        if option == 'append':   
                                                            for ob in gr.objects:
                                                                if 'RigidBodyWorld' in gr.name:    
                                                                    bpy.context.space_data.show_relationship_lines = True                                                        
                                                                    if 'RigidBodyWorld' in bpy.data.groups:
                                                                        if gr.name != 'RigidBodyWorld':
                                                                            gr.objects.unlink(ob)
                                                                            bpy.data.groups['RigidBodyWorld'].objects.link(ob)
                                                                            if gr not in groupsToRemove:
                                                                                groupsToRemove.append(gr)
                                                                        else:
                                                                            scene.rigidbody_world.group = gr
                                                                if 'RigidBodyConstraints' in gr.name:                                                            
                                                                    if 'RigidBodyConstraints' in bpy.data.groups:
                                                                        if gr.name != 'RigidBodyConstraints':
                                                                            gr.objects.unlink(ob)
                                                                            bpy.data.groups['RigidBodyConstraints'].objects.link(ob)
                                                                            if gr not in groupsToRemove:
                                                                                groupsToRemove.append(gr)
                                                                        else:
                                                                            scene.rigidbody_world.constraints = gr                                         
                                                                try:
                                                                    scene.objects.link(ob)
                                                                except:
                                                                    pass                                               
                                                        if option == 'link':
                                                            bpy.ops.object.group_instance_add(group=gr.name)
                                                            text1 = 'LINKED GROUPED OBJECTS FROM FILE: these can be transformed'
                                                            text2 = ' and animated (unlike linked objects not found in groups)'
                                                        if option == 'append':
                                                            text1 = 'APPENDED GROUPS FROM FILE'
                                                            text2 = ''
                                                        message = text1 + text2
                                            with bpy.data.libraries.load(file_path, link = li) as (data_from, data_to):
                                                newObjects = data_from.objects
                                                obsToLoad = []
                                                for obName in newObjects:
                                                    addOb = True
                                                    for group in bpy.data.groups:
                                                        for ob in group.objects:
                                                            if obName == ob.name:
                                                                addOb = False
                                                    if addOb:
                                                        if 'zbCyclesLight' not in obName:
                                                            obsToLoad.append(obName)
                                                data_to.objects = obsToLoad                            
                                                newObjects = obsToLoad
                                                if obsToLoad:
                                                    if message == '':
                                                        if option == 'link':
                                                            text1 = 'LINKED OBJECTS FROM FILE: linked objects (not belonging to any group) can'
                                                            text2 = 'not be transformed or animated'
                                                        if option == 'append':
                                                            text1 = 'APPENDED OBJECTS FROM FILE'
                                                            text2 = ''
                                                        message = text1 + text2    
                                            if len(newObjects) > 0:
                                                for ob in bpy.data.objects:
                                                    if ob.users == 0:
                                                        if ob.type not in ['LAMP', 'CAMERA']:
                                                            loadIt = True
                                                            if ob.name == 'Character':
                                                                if ob.active_material:
                                                                    if ob.active_material.name == 'Basic':
                                                                        if len(ob.data.polygons) == 6:
                                                                            loadIt = False
                                                            if loadIt:
                                                                try:
                                                                    scene.objects.link(ob)
                                                                except:
                                                                    pass
                                            bpy.ops.object.select_all(action='DESELECT')
                                            try: 
                                                bpy.ops.object.parent_no_inverse_set()
                                            except:
                                                pass                                        
                                            if groupsToRemove:
                                                for gr in groupsToRemove:
                                                    if gr in newGroups:
                                                        newGroups.remove(gr)
                                                        gr.user_clear()
                                        if len(bpy.data.objects) > len(totalOb):
                                            for ob in bpy.data.objects:
                                                if ob not in totalOb:
                                                    ob.select = True
                                            sel = bpy.context.selected_objects                                            
                                            reposition = True
                                            for ob in sel:
                                                if hasattr(ob, 'animation_data'):
                                                    if hasattr(ob.animation_data, 'action'):
                                                        action = ob.animation_data.action
                                                        if hasattr(action, 'fcurves'):
                                                            for fc in action.fcurves:
                                                                if hasattr(fc,'data_path'):
                                                                    if 'location' in fc.data_path:                       
                                                                        reposition = False
                                                                        break
                                            if reposition:    
                                                bpy.ops.view3d.snap_selected_to_cursor()
                                                if message == '':
                                                    message = 'Successfully loaded items from file'     
                                            else:
                                                if message == '':
                                                    message = 'Location animation data found, so not moving objects to cursor location.'
                                            fu0()
                                            aType = bpy.context.area.type
                                            bpy.context.area.type = 'DOPESHEET_EDITOR'
                                            bpy.ops.anim.channels_collapse()    
                                            bpy.context.area.type = aType
                                            bpy.ops.view3d.view_selected(use_all_regions=False)
                                            override = fu2('FILE_BROWSER')
                                            bpy.ops.file.refresh(override)      
                                else:
                                    message = 'The type of file you selected is not currently supported.'
                        else:
                            message = 'You must select a file from the library before linking or appending it'
                    if message:
                        self.report({'INFO'}, message)
        if mode != 'cancel':
            fu1(mode)
        if len(bpy.data.materials) > matStart:            
            for area in bpy.context.screen.areas:
                if area.type == 'VIEW_3D':
                    area.spaces[0].viewport_shade = 'MATERIAL'
        return{'FINISHED'}
def fu7(self,context):
    ob = bpy.context.active_object
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    last = bpy.context.active_object
    try: 
        cam = scene.camera
        scene.objects.active = cam
        cam.hide = False
    except:
        pass
    if len(self.sfCTarget) > 0:
        buildTrackTo = True
        if cam.constraints:
            if 'Track To' in cam.constraints: 
                cam.constraints['Track To'].target = bpy.data.objects[self.sfCTarget]
                buildTrackTo = False
        if buildTrackTo:
            bpy.ops.object.constraint_add(type='TRACK_TO')
            for con in cam.constraints:
                if con.type == 'TRACK_TO':
                    con.show_expanded = False
                    con.track_axis = 'TRACK_NEGATIVE_Z'
                    con.up_axis = 'UP_Y'
                    con.target = bpy.data.objects[self.sfCTarget]
        scene.objects.active = last
    else:
        try:
            cam.constraints['Track To'].target = None
        except:
            pass
def sfUnifiedFocus(self,context):
    scene = bpy.context.scene
    screen = bpy.context.screen
    uf = self.sfUnifiedFocus
    for area in screen.areas:
        if area.type == 'VIEW_3D':
            if area.spaces[0].lock_camera:
                view = area.spaces[0]
                view.fx_settings.use_dof = True
    try: 
        camOb = scene.camera
        cam = camOb.data
        cCam = camOb.data.cycles
        camOb.data.gpu_dof.fstop = uf
        try: 
            nodes = bpy.context.scene.node_tree.nodes
            dNode = nodes['sf_dNode']
            dNode.f_stop = uf
        except:
            pass
        uf = 1 - (uf/10) - .5
        cCam.aperture_size = uf
    except:
        pass
def sfUnifiedAmbient(self,context):
    screen = bpy.context.screen
    ao = self.sfUnifiedAmbient
    if bpy.context.screen.name == 'Shader': 
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                view = area.spaces[0]
                fx  = view.fx_settings
                fx.ssao.factor = (ao * 3)
    else:        
        view = context.space_data
    view.fx_settings.use_ssao = True
    fx  = view.fx_settings
    fx.ssao.factor = (ao * 3)
    if fx.ssao.samples < 5:
        fx.ssao.samples = 20
    world = bpy.context.scene.world
    world.light_settings.ao_factor = ao
    return
def fu8(self,context):
    wm = bpy.context.window_manager
    re = bpy.context.scene.render.engine
    scene = bpy.context.scene
    uf = scene.sfUnifiedFocus
    last = bpy.context.active_object
    try:
        cam = scene.camera
        scene.objects.active = cam
    except:
        pass
    if last == cam:
        print("Make sure the object you're focusing on isn't a camera")
        try: 
            nodes = bpy.context.scene.node_tree.nodes
            nodes['sf_rNode'].mute = False
            nodes['sf_dNode'].mute = False
            nodes['sf_cNode'].mute = False
        except:
            pass
    else:
        if len(self.sfCFocus) > 0:
            for screen in bpy.data.screens:
                for area in screen.areas:
                    if area.type == 'VIEW_3D':
                        try:
                            area.spaces[0].fx_settings.use_dof = True
                        except:
                            pass
            cam.data.dof_object = bpy.data.objects[scene.sfCFocus]
            cam.hide = False
            aType = bpy.context.area.type
            bpy.context.area.type = 'NODE_EDITOR'
            bpy.context.space_data.tree_type = 'CompositorNodeTree'
            if re == 'CYCLES':
                nodes = bpy.context.scene.node_tree.nodes
                try:
                    nodes['sf_dNode'].mute = True
                    mNode = nodes['sf_mNode']
                    mNode.inputs[1].enabled = True
                except:
                    cam.data.cycles.aperture_size = 0.075
                    cam.data.cycles.aperture_blades = 15
                    cam.data.cycles.aperture_rotation = 0.523599
            else:
                scene.use_nodes = True
                try:
                    nodes = scene.node_tree.nodes
                    nodes['sf_rNode'].mute = False
                    nodes['sf_dNode'].mute = False
                    nodes['sf_cNode'].mute = False
                    dNode = nodes['sf_dNode']
                    mNode = nodes['sf_mNode']
                    mNode.inputs[1].enabled = False
                    links = bpy.context.scene.node_tree.links
                    links.new(dNode.outputs['Image'], mNode.inputs['Image'])
                    mNode.inputs[2].enabled = True
                except:
                    nodes = scene.node_tree.nodes
                    links = scene.node_tree.links
                    rNode = 0
                    for node in nodes:
                        if node.type == 'R_LAYERS':
                            rNode = node
                            break
                    if rNode == 0:
                        rNode = nodes.new(type="CompositorNodeRLayers")
                        rNode.name = 'sf_rNode'
                    dNode = 0
                    for node in nodes:
                        if node.type == 'DEFOCUS':
                            dNode = node
                            break
                    if dNode == 0:
                        dNode = nodes.new(type="CompositorNodeDefocus")
                        dNode.name = 'sf_dNode'
                    mNode = 0
                    for node in nodes:
                        if node.name == 'sf_mNode':
                            mNode = node
                            break
                    if mNode == 0:
                        mNode = nodes.new(type="CompositorNodeMixRGB")
                        mNode.name = 'sf_mNode'
                    cNode = 0
                    for node in nodes:
                        if node.type == 'COMPOSITE':
                            cNode = node
                            break
                    if cNode == 0:
                        cNode = nodes.new(type="CompositorNodeComposite")
                        cNode.name = 'sf_cNode'
                    vNode = 0
                    for node in nodes:
                        if node.type == 'VIEWER':
                            vNode = node
                            break
                    if vNode == 0:
                        vNode = nodes.new(type='CompositorNodeViewer')
                        vNode.location = (800,-140)
                        links.new(mNode.outputs['Image'], vNode.inputs['Image'])
                    dNode.use_zbuffer = True
                    dNode.use_preview = False
                    dNode.use_gamma_correction = True
                    dNode.f_stop = uf
                    dNode.blur_max = 4.5
                    dNode.threshold = 1.5
                    cNode.use_alpha = True
                    rNode.location = (-400,0)
                    dNode.location = (400,0)
                    mNode.location = (600,0)
                    cNode.location = (800,0)
                    links.new(rNode.outputs['Image'], dNode.inputs['Image'])
                    links.new(rNode.outputs['Z'], dNode.inputs['Z'])
                    links.new(dNode.outputs['Image'], mNode.inputs[2])
                    links.new(mNode.outputs['Image'], cNode.inputs['Image'])                  
                    bgNode = 0
                    for node in nodes:
                        if node.name == 'Background':
                            bgNode = node
                            break
                    if bgNode:
                        aoNode = 0
                        for node in nodes:
                            if node.name == 'sf_aoNode':
                                aoNode = node
                                break
                        if aoNode:                            
                            links.new(aoNode.outputs['Image'],dNode.inputs['Image'])
                    cam.data.cycles.aperture_size = 0.075
                    cam.data.cycles.aperture_blades = 3
                    cam.data.cycles.aperture_rotation = 0.523599
            for camera in bpy.data.cameras:
                camera.gpu_dof.use_high_quality = False
                camera.gpu_dof.fstop = uf
            bpy.context.space_data.tree_type = 'ShaderNodeTree'
            bpy.context.area.type = aType
            bpy.context.scene.objects.active = last
        else:                
            cam.data.dof_object = None
            cam.data.cycles.aperture_size = 0
            for screen in bpy.data.screens:
                for area in screen.areas:
                    if area.type == 'VIEW_3D':
                        try:
                            area.spaces[0].fx_settings.use_dof = False
                        except:
                            bpy.context.space_data.fx_settings.use_dof = False
        bpy.context.scene.objects.active = last
    return
def fu9(self,context):
    render = context.scene.render
    renderX = render.resolution_x
    renderY = render.resolution_y
    bpy.context.scene.render.resolution_percentage = 100
    if self.sfRenderType == '1920':
        render.resolution_x = 1920
        render.resolution_y = 1080
    if self.sfRenderType == '1280':
        render.resolution_x = 1280
        render.resolution_y = 720
    if self.sfRenderType == '4k':
        render.resolution_x = 4096
        render.resolution_y = 2160
    if self.sfRenderType == '300dpi':
        render.resolution_x = int(renderX * 4.166666666666667)
        render.resolution_y = int(renderY * 4.166666666666667)
def fu10(self,context):
    layout = self.layout
    wm = context.window_manager
    scene = bpy.context.scene
    row = layout.row()
    row.operator("node.view_all", text="", icon='VIEWZOOM')
    if bpy.context.space_data.tree_type == 'CompositorNodeTree':
        row.operator('object.sf_cam_options', text='Save Image',
        icon='SCENE').func = 'save_node_preview_image'
        row.operator("object.sf_back_to_3dview", text='GO BACK',
        icon='FILE_TICK')
    if bpy.context.screen.name == "Shader":
        layout = self.layout
        context = bpy.context
        wm = context.window_manager
        scene = context.scene
        rd = scene.render
        row = layout.row(align=True)
        row.operator("wm.call_menu", icon="COLLAPSEMENU", text="").name = "menu.sf_render_settings_menu"
        row.operator("object.sf_cam_options", text="", icon='RENDER_STILL').func = "render"
        sub = row.row(align=True)
        sub.scale_x = 0.67
        sub.prop(rd, "resolution_percentage", text="")
        row.separator()
        row.separator()
        try:
            if bpy.context.scene.cycles.preview_pause:
                zbRendIcon = "MATERIAL"
            else:
                zbRendIcon = "SMOOTH"
            row.operator("object.zb_render_prev", icon =zbRendIcon, text="")
        except:
            print('Activate Zero Brush addon to use this feature')
        sub = row.row(align=True)
        sub.scale_x = 0.75
        sub.operator("wm.call_menu", text='Lights').name = "menu.sf_lighting_options_menu"
        sub.operator("wm.call_menu",text='Camera').name = "menu.sf_camera_options_menu"
        row.separator()
class cl3(bpy.types.Operator):
    bl_idname =i_0[16]
    bl_label =i_0[17]
    def execute(self,context):
        s = bpy.context.screen.name
        aType = bpy.context.area.type
        try:
            if s == 'Shader':
                bpy.context.area.type = 'NODE_EDITOR'
            else:
                bpy.context.area.type = 'VIEW_3D'
        except:
            pass
        return {'FINISHED'}
def fu11(self,context):
    layout = self.layout
    row = layout.row()
    try:
        showSave = False
        for img in bpy.data.images:
            if 'Render' in img.name:
                showSave = True
                break
        if showSave:
            row.operator('image.save_as', text='Save Image',
            icon='SCENE')
    except:
        pass
    row.operator("object.sf_back_to_3dview", text='GO BACK',
    icon='FILE_TICK')
def sfDisplay(self,context):
    if self.sfDisplayAllNames:
        for ob in bpy.data.objects:
            ob.show_name = True
            try:
                ob.data.show_names = True
            except:
                pass
    else:
        for ob in bpy.data.objects:
            ob.show_name = False
            try:
                ob.data.show_names = False
            except:
                pass
def sfHideBevel(self,context):
    mode = bpy.context.mode
    bpy.ops.object.mode_set(mode='OBJECT')
    if self.sfHideBevel:
        activeOb = bpy.context.active_object
        selected = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')
        for ob in bpy.data.objects:
            try:
                for mod in ob.modifiers:
                    if mod.type == 'BEVEL':
                        if ob.hide == False:
                            bpy.context.scene.objects.active = ob
                            bpy.context.active_object.select = True
                        mod.show_viewport = False
                        bpy.ops.object.shade_flat()
            except:
                pass
        bpy.ops.object.select_all(action='DESELECT')
        for ob in selected:
            ob.select = True
        bpy.context.scene.objects.active = activeOb
    else:
        activeOb = bpy.context.active_object
        selected = bpy.context.selected_objects
        bpy.ops.object.select_all(action='DESELECT')
        for ob in bpy.data.objects:
            try:
                for mod in ob.modifiers:
                    if mod.type == 'BEVEL':
                        if ob.hide == False:
                            bpy.context.scene.objects.active = ob
                            bpy.context.active_object.select = True
                        mod.show_viewport = True
                        bpy.ops.object.shade_smooth()
            except:
                pass
        bpy.ops.object.select_all(action='DESELECT')
        for ob in selected:
            ob.select = True
        bpy.context.scene.objects.active = activeOb
    fu1(mode)
def sfUseCageEdit(self,context):
    if self.sfUseCageEdit:
        for ob in bpy.data.objects:
            for mod in ob.modifiers:
                    mod.show_on_cage = True
    else:
        for ob in bpy.data.objects:
            for mod in ob.modifiers:
                    mod.show_on_cage = False
def fu12(self,context):
    ob = bpy.context.active_object
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    col = self.layout.column()
    try:
        col.prop(scene, 'sfDisplayAllNames', text='All Names')
        col.prop(scene, 'sfHideBevel', text='Hide Bevel')
        col.prop(scene, 'sfUseCageEdit', text='Cage Edit')
        col.prop(ob, 'show_x_ray')         
    except:
        pass
class VIEW3D_PT_tools_cl4(Panel):
    bl_space_type =i_0[18]
    bl_region_type =i_0[19]
    bl_category =i_0[20]
    bl_context =i_0[21]
    bl_label =i_0[22]
    def draw(self, context):
        scene = bpy.context.scene
        layout = self.layout
        col = layout.column(align=True)
        col.label('Keyframes:', icon='SPACE3')
        sub = col.row(True)
        col.operator('object.sf_keyframe_tools',
        text = 'Fill').tool = 'FILL'
        sub = col.row(align=True)
        sub.operator('object.sf_keyframe_tools',
        text = 'Chain Select').tool = 'CHAIN_SELECT'
        sub = sub.row(True)
        sub.scale_x = .45
        sub.prop(scene,'sfFrameChainSelect', text = '')
        sub = col.row(True)
        sub.scale_y = 1.25
        sub.operator('object.sf_keyframe_tools',
        text = 'Invert Selection').tool = 'INVERT'
        sub = sub.row(True)
        sub.scale_x = .45
        sub.scale_y = 1.25
        sub.operator('object.sf_keyframe_tools',
        text = 'Delete').tool = 'DELETE'
        col = layout.column(align=True)
        col.label('Adjust Interpolation', icon = 'SPACE3')
        sub = col.row(align=True)
        sub.operator('object.sf_keyframe_tools',
        text = 'Clean').tool = 'CLEAN'
        sub.operator('object.sf_keyframe_tools',
        text = 'Smooth').tool = 'SMOOTH'                 
        col = layout.column()        
        col = layout.column(align=True)
        col.label('Delete Object Keyframes:', icon = 'SPACE3')
        sub = col.row(align=True)
        sub.operator('object.sf_keyframe_tools',
        text = 'Location').tool = 'DELETE_LOC'
        sub = sub.row(True)
        sub.scale_x = 0.95
        sub.operator('object.sf_keyframe_tools',
        text = 'Rotation').tool = 'DELETE_ROT'
        sub = sub.row(True)
        sub.scale_x = 0.75
        sub.operator('object.sf_keyframe_tools',
        text = 'Scale').tool = 'DELETE_SCALE'
        col = layout.column()   
        col = layout.column()   
        col.label('Distribute Keyframes:', icon = 'SPACE3')
        col.operator('object.make_links_data',
        text = 'Distribute keyframes').type = 'ANIMATION'
class cl4(bpy.types.Operator):
    bl_idname =i_0[23]
    bl_label =i_0[24]
    bl_description =i_0[25]
    tool = bpy.props.StringProperty()
    def execute(self,context):
        scene = bpy.context.scene
        tool = self.tool
        points, all_points, gKeys = fu13()
        indicatorLoc = bpy.context.scene.frame_current
        lastArea = 0        
        if bpy.context.area.type != 'DOPESHEET_EDITOR':
            lastArea = bpy.context.area.type
            bpy.context.area.type = 'DOPESHEET_EDITOR'
        dsMode = bpy.context.space_data.mode
        if gKeys:
            bpy.context.space_data.mode = 'GPENCIL'
        else:
            bpy.context.space_data.mode = 'DOPESHEET'
        if tool == 'REVERSE':
            if len(points) > 1: 
                keyFrames = []
                for p in points:                        
                    pFrame = 0
                    if gKeys:
                        pFrame = p.frame_number
                    else:
                        pFrame = int(p.co[0])     
                    keyFrames.append(pFrame)
                keyFrames = sorted(keyFrames)
                selLength = max(keyFrames) - min(keyFrames)  
                if len(keyFrames) < 200: 
                    if selLength % 2 != 0:
                        selLength += 1
                        for point in points:
                            if gKeys:
                                if point.frame_number == max(keyFrames):
                                    point.frame_number = max(keyFrames) + 1
                            else:
                                if point.co[0] == max(keyFrames):
                                    point.co[0] = max(keyFrames) + 1
                centerSel = (selLength / 2) + min(keyFrames)  
                bpy.context.scene.frame_current = centerSel
                bpy.ops.transform.transform(mode='TIME_SCALE', value=(-1.0, 0, 0, 0))
                scene.frame_current = indicatorLoc            
                if not gKeys:
                    interpol = points[0].interpolation
                    if interpol:
                        bpy.ops.action.interpolation_type(type=interpol)
        if tool == 'MIRROR':
            if len(points) > 1: 
                keyFrames = []
                for p in points:                        
                    pFrame = 0
                    if gKeys:
                        pFrame = p.frame_number
                    else:
                        pFrame = int(p.co[0])
                    keyFrames.append(pFrame)                
                keyFrames = sorted(keyFrames)
                bpy.ops.action.duplicate()
                bpy.context.scene.frame_current = max(keyFrames)
                bpy.ops.transform.transform(mode='TIME_SCALE', value=(-1.0, 0, 0, 0))
                try:  
                    bpy.ops.action.clean(channels=False)
                except:
                    pass
                scene.frame_current = indicatorLoc                            
                if not gKeys:
                    interpol = points[0].interpolation
                    if interpol:
                        bpy.ops.action.interpolation_type(type=interpol)
        if tool == 'CHAIN_SELECT':
            if len(all_points) > 1:
                val = scene.sfFrameChainSelect 
                keyFrames = []
                for point in points: 
                    if gKeys:
                        point.select = True
                        keyFrames.append(point.frame_number)
                    else:
                        if point.co[0] not in keyFrames:
                            point.select_control_point = True                            
                            keyFrames.append(point.co[0])
                keyFrames = sorted(keyFrames)
                bpy.ops.action.select_all_toggle(invert=False)            
                count = val + 1
                for key in keyFrames:
                    if count > val:
                        count = 0
                        for point in points:                            
                            if gKeys:
                                if point.frame_number == key:
                                    point.select = True
                            else:
                                if int(point.co[0]) == int(key):
                                    point.select_control_point = True                   
                    count += 1
        if 'DELETE_' in tool:            
            keyFrames = []
            for point in points: 
                if gKeys:
                    point.select = True
                    keyFrames.append(point.frame_number)
                else:
                    if point.co[0] not in keyFrames:
                        point.select_control_point = True                            
                        keyFrames.append(point.co[0])
            keyFrames = sorted(keyFrames)
            bpy.ops.action.select_all_toggle(invert=False)  
            propToDelete = ''
            if tool == 'DELETE_LOC':
                propToDelete = 'location'
            if tool == 'DELETE_ROT':
                propToDelete = 'rotation'
            if tool == 'DELETE_SCALE':
                propToDelete = 'scale'    
            selectedPoints = False    
            for ob in bpy.context.selected_objects:
                if hasattr(ob.animation_data, 'action'):
                    action = ob.animation_data.action
                    if hasattr(action, 'fcurves'):   
                        for fc in action.fcurves:
                            if propToDelete in fc.data_path:
                                for pt in fc.keyframe_points:
                                    selectedPoints = True
                                    pt.select_control_point = True
                            else:
                                for pt in fc.keyframe_points:
                                    pt.select_control_point = False
            if selectedPoints:                              
                bpy.ops.action.delete()
            for ob in bpy.context.selected_objects:
                if hasattr(ob.animation_data, 'action'):
                    if ob.animation_data.action:                    
                        for fc in ob.animation_data.action.fcurves:
                            for pt in fc.keyframe_points:
                                pt.select_control_point = True          
        if tool == 'FILL':
            bpy.ops.action.sample()
            points, all_points, gKeys = fu13()             
            for point in points:
                point.type = 'KEYFRAME'
        if tool == 'SMOOTH':
            bpy.context.area.type = 'GRAPH_EDITOR'
            try:
                bpy.ops.graph.smooth()
            except:
                msg = 'This type of keyframe can not be smoothed'
                self.report({'INFO'}, msg)            
        if tool == 'CLEAN':
            for point in points:
                point.interpolation = 'BEZIER'        
        if tool == 'INVERT':                
            bpy.ops.action.select_all_toggle(invert=True)        
        if tool == 'DELETE':                
            bpy.ops.action.delete()  
        bpy.context.space_data.mode = dsMode
        if lastArea:
            bpy.context.area.type = lastArea
            for area in bpy.context.screen.areas:
                if area.type == 'DOPESHEET_EDITOR':
                    area.tag_redraw()    
        return{'FINISHED'}
def fu13():
    scene = bpy.context.scene
    gKeys = False 
    for area in bpy.context.screen.areas:
        if area.type == 'DOPESHEET_EDITOR':
            if area.spaces[0].mode == 'GPENCIL':
                gKeys = True
                break
    points = []
    all_points = []
    if gKeys:
        try:
            for layer in scene.grease_pencil.layers:
                for frame in layer.frames:
                    all_points.append(frame)
                    if frame.select:
                        points.append(frame)
        except:
            pass
        for ob in bpy.data.objects:
            try:
                for layer in ob.grease_pencil.layers:
                    for frame in layer.frames:
                        all_points.append(frame)
                        if frame.select:
                            points.append(frame)
            except:
                pass
    else: 
        objects = 0
        for area in bpy.context.screen.areas:
            if area.type == 'DOPESHEET_EDITOR':
                if area.spaces[0].dopesheet.show_only_selected:
                    objects = bpy.context.selected_objects
                    break        
        if objects == 0:
            objects = bpy.data.objects
        for ob in objects:
            if hasattr(ob.data, 'animation_data'):
                if hasattr(ob.data.animation_data, "keys"):
                    try:
                        for fcurve in ob.data.animation_data.action.fcurves:
                            if fcurve.lock or (fcurve.hide and context.space_data.type == "GRAPH_EDITOR"):
                                continue
                            for keyframe_point in fcurve.keyframe_points:
                                all_points.append(keyframe_point)
                                if keyframe_point.select_control_point:
                                    points.append(keyframe_point)
                    except:
                        pass
            if hasattr(ob.animation_data, "keys"):
                try:
                    for fcurve in ob.animation_data.action.fcurves:
                        if fcurve.lock or (fcurve.hide and context.space_data.type == "GRAPH_EDITOR"):
                            continue
                        for keyframe_point in fcurve.keyframe_points:
                            all_points.append(keyframe_point)
                            if keyframe_point.select_control_point:
                                points.append(keyframe_point)
                except:
                    pass
            if hasattr(ob.data, "shape_keys"):
                try:
                    if hasattr(ob.data.shape_keys.animation_data, "keys"):                        
                        for fcurve in ob.data.shape_keys.animation_data.action.fcurves:
                            try:
                                for keyframe_point in fcurve.keyframe_points:
                                    all_points.append(keyframe_point)
                                    if keyframe_point.select_control_point:
                                        points.append(keyframe_point)
                            except:
                                pass                       
                except:
                    pass
    return points, all_points, gKeys
def fu14(self,execute):
    if bpy.context.area.spaces[0].lock_camera:
        if bpy.context.screen.name in {'Hacker-nonnormal',
        'Blender-nonnormal', 'Blender', 'Hacker'}:
            layout = self.layout
            context = bpy.context
            wm = context.window_manager
            scene = context.scene
            rd = scene.render
            row = layout.row(align=True)
            row.operator("wm.call_menu", icon="COLLAPSEMENU", text="").name = "menu.sf_render_settings_menu"
            row.operator("object.sf_cam_options", text="", icon='RENDER_STILL').func = "render"
            sub = row.row(align=True)
            sub.scale_x = 0.67
            sub.prop(rd, "resolution_percentage", text="")
            row.separator()
            row.separator()
            try:
                if bpy.context.space_data.viewport_shade != 'MATERIAL':
                    zbRendIcon = "SMOOTH"
                else:
                    zbRendIcon = "MATERIAL"
                row.operator("object.zb_render_prev", icon =zbRendIcon, text="")
            except:
                print('Activate Zero Brush addon to use this feature')
            sub = row.row(align=True)
            sub.scale_x = 0.75
            sub.operator("wm.call_menu", text='Lights').name = "menu.sf_lighting_options_menu"
            sub.operator("wm.call_menu",text='Camera').name = "menu.sf_camera_options_menu"
            fu20(self,context)
            row = layout.row()
            row = layout.row()
            row = layout.row()
            row = layout.row()
def fu15(self,context):
    uf = self.fu15
    return
class cl5(bpy.types.Menu):
    bl_label =i_0[26]
    bl_idname =i_0[27]
    def draw(self, context):
        re = bpy.context.scene.render.engine
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        world = bpy.context.scene.world
        layout = self.layout
        mode = bpy.context.mode
        if len(bpy.data.cameras) > 1:
            layout.prop(scene, "camera", text = '')
            layout.separator()
        layout.operator('object.sf_cam_options',
        text='Track Selected', icon='CAMERA_DATA').func = 'track'
        camExists = False
        try:
            camOb = scene.camera
            cam = camOb.data
            cCam = camOb.data.cycles
            camExists = True
        except:
            pass
        if camExists:
            if camOb.constraints:
                if 'Track To' in camOb.constraints:
                    track = camOb.constraints['Track To']
                    if track.target:
                        layout.operator('object.sf_cam_options',
                        text='Stop Tracking').func = 'untrack'
                        layout.prop(camOb.constraints['Track To'], "influence",
                        text ="       Influence")
                        if len(bpy.data.curves) < 1:
                            layout.separator()        
            if len(bpy.data.curves) > 0:
                if 'PAINT' not in mode and 'SCULPT' not in mode:  
                    layout.separator() 
                    showFollow = True
                    for con in camOb.constraints:
                        if con.type == 'FOLLOW_PATH': 
                            showFollow = False
                            break
                    if showFollow:    
                        layout.operator('object.sf_cam_options',
                        text='Follow Path', icon='ANIM_DATA').func = 'follow_path'
                    else:
                        layout.operator('object.sf_cam_options',
                        text='Stop Follow', icon='ANIM_DATA').func = 'stop_follow_path'
                    for con in camOb.constraints:
                        if con.type == 'FOLLOW_PATH': 
                            txt = "Track Path"                            
                            if con.use_curve_follow:
                                txt = "Stop Track"
                            layout.operator('object.sf_cam_options',
                            text= txt).func = 'track_path'
                            layout.operator('object.sf_cam_options',
                            text='Reverse Path').func = 'reverse_path'
                            layout.operator('object.sf_cam_options',
                            text='Reset Path').func = 'reset_path'
                            break
                    layout.separator()    
            layout.operator('object.sf_cam_options',
            text='Focus Selected', icon='CURSOR').func = 'dof'
            if camOb.data.dof_object:
                layout.operator('object.sf_cam_options',
                text='Stop Focusing').func = 'remove_dof'
                layout.prop(scene, 'sfUnifiedFocus', text='       Focus')
                layout.separator()   
            layout.prop(cam, 'lens', text='       Lens Size')
            if bpy.context.screen.name != 'Shader':   
                layout.separator()     
                layout.menu('menu.sf_live_record_menu',
                text = 'Record Live', icon = 'REC')
class cl6(bpy.types.Menu):
    bl_idname =i_0[28]
    bl_label =i_0[29]
    def draw(self, context):
        layout = self.layout
        layout.operator('object.sf_cam_options',
        text = 'Record Basic').func = 'record_basic'
        layout.operator('object.sf_cam_options',
        text = 'Record Walking').func = 'record_walkmode'
        layout.operator('object.sf_cam_options', 
        text = 'Record Fly Mode').func = 'record_flymode'  
class cl7(bpy.types.Operator):
    bl_label =i_0[30]
    bl_idname =i_0[31]
    func = bpy.props.StringProperty()
    bpy.types.Scene.mistInit = bpy.props.BoolProperty(default=True)
    def execute(self,context):
        scene = bpy.context.scene
        wm = bpy.context.window_manager
        ren = scene.render.engine
        world = scene.world
        mode = bpy.context.mode
        func = self.func                
        userMsg = ''
        ob = bpy.context.active_object      
        if ob:            
            try:
                ob.hide = False
                ob.select = True
                bpy.ops.object.mode_set(mode='OBJECT')
            except:
                pass
        if func == 'save_node_preview_image':            
            bpy.context.area.type = 'IMAGE_EDITOR'    
            vNode = False  
            for img in bpy.data.images:
                if 'Viewer Node' in img.name:
                    vNode = True
                    bpy.context.area.spaces.active.image = img      
                    bpy.ops.image.save_as('INVOKE_DEFAULT')   
                    for map in wm.keyconfigs.addon.keymaps:   
                        ki = map.keymap_items        
                        for key in ki: 
                            if 'Image Editor Listener' in key.name:
                                key.active = True
                                break
                    break                           
            if vNode is False:
                userMsg = 'You need a viewer node present to save images from the Node Editor'
        if 'render' in func:  
            abortRender = False
            if scene.sfOptimizeRender:
                if wm.sfDisableORen:
                    abortRender = True
                    bpy.ops.object.sf_layout_message('INVOKE_DEFAULT',
                    message = 'RENDER_ERROR')
                else:
                    if ren == 'CYCLES':
                        bpy.app.handlers.render_complete.append(fu17)
                        bpy.app.handlers.render_cancel.append(fu18)
                        fu16()
                        wm.sfDisableORen = True                    
                    fu19(self,context)
            if abortRender is False:
                if mode == 'PAINT_TEXTURE':
                    bpy.ops.object.mode_set(mode='OBJECT')
                    mode = 'OBJECT'
                if scene.render.display_mode == 'NONE':
                    scene.render.display_mode = 'AREA'            
                if scene.use_nodes:
                    nodes = scene.node_tree.nodes                
                    needsComp = True
                    for node in nodes:
                        if node.type == 'COMPOSITE':
                            needsComp = False
                            break                
                    if needsComp:
                        nodes.new(type = 'CompositorNodeComposite')
                        userMsg = 'Connect an image node to the composite node in the Node Editor first!'                               
                if ren == 'CYCLES':
                    try:
                        lampOb = bpy.data.objects['-Shadows']             
                        lampOb.hide_render = True 
                    except:
                        pass
                if func == 'render_anim':                                    
                    bpy.ops.render.render('INVOKE_DEFAULT', animation=True)
                else: 
                    if scene.use_nodes is False:                            
                        if scene.auto_advance_render_slot:                                   
                            try: 
                                r = bpy.data.images['Render Result']
                                rSlot = r.render_slots.active_index
                                if rSlot < 7:
                                    rSlot += 1
                                else:
                                    rSlot = 0
                                r.render_slots.active_index = rSlot
                            except:
                                pass                           
                    if scene.sfUseCompositing:
                        scene.render.use_compositing = True   
                        scene.use_nodes = True
                        aType = bpy.context.area.type
                        bpy.context.area.type = 'NODE_EDITOR'
                        sd = bpy.context.space_data
                        sd.tree_type = 'CompositorNodeTree'
                        nodes = scene.node_tree.nodes
                        links = scene.node_tree.links 
                        if len(nodes) < 3:
                            nodes.clear()                                        
                            nodeComposite = nodes.new(type = 'CompositorNodeComposite')
                            nodeComposite.name = 'sf_cNode'                                                
                            nodeComposite.location = (800, 0)
                            nodeViewer = nodes.new(type = 'CompositorNodeViewer')                                    
                            nodeViewer.location = (800, -135)
                            nodeViewer.hide = True
                            nodeMix = 0
                            for node in nodes:
                                if node.name == 'sf_mNode':
                                    nodeMix = node
                                    break                                    
                            if nodeMix == 0:        
                                nodeMix = nodes.new(type = 'CompositorNodeMixRGB')
                                nodeMix.location = (610, 0)
                                nodeMix.name = 'sf_mNode'
                            nodeRL = nodes.new(type = 'CompositorNodeRLayers')
                            nodeRL.name = 'sf_rNode'
                            nodeRL.location = (-400, 0)
                            if len(scene.render.layers) < 2:                            
                                rl = scene.render.layers.active                            
                                if ren != 'CYCLES':
                                    rl.use_sky = False
                                bpy.ops.scene.render_layer_add()
                                rl = scene.render.layers.active
                                rl.use_solid = False
                                rl.use_halo = False
                                rl.use_ztransp = False
                                rl.use_edge_enhance = False
                                rl.use_strand = False                            
                                nodeAO = nodes.new(type = 'CompositorNodeAlphaOver')
                                nodeAO.name = 'sf_aoNode'
                                nodeAO.location = (610, -185)
                                nodeAO.hide = True
                                nodeRL2 = nodes.new(type = 'CompositorNodeRLayers')
                                nodeRL2.name = 'Background'
                                nodeRL2.label = 'Background'                            
                                nodeRL2.layer = rl.name
                                nodeRL2.location = (-400, -240)
                                links.new(nodeAO.outputs['Image'], nodeMix.inputs[2])
                                links.new(nodeRL2.outputs['Image'], nodeAO.inputs[1])
                                links.new(nodeRL.outputs['Image'], nodeAO.inputs[2])
                                if scene.sfRenderTransparent:
                                    if ren != 'CYCLES':
                                        links.new(nodeRL.outputs['Alpha'], nodeComposite.inputs['Alpha'])
                                        links.new(nodeRL.outputs['Alpha'], nodeViewer.inputs['Alpha'])
                            else:
                                links.new(nodeRL.outputs['Image'], nodeMix.inputs[2]) 
                            links.new(nodeMix.outputs['Image'], nodeComposite.inputs['Image'])
                            links.new(nodeMix.outputs['Image'], nodeViewer.inputs['Image'])                  
                        bpy.context.area.type = aType    
                    if scene.sfLastRE == 'CYCLES':
                        scene.render.engine = 'CYCLES'
                        for mat in bpy.data.materials:       
                            try:
                                nodes = mat.node_tree.nodes
                                for node in nodes:
                                    if node.type == 'OUTPUT_MATERIAL':
                                        mat.use_nodes = True
                            except:
                                pass
                    bpy.ops.render.render('INVOKE_DEFAULT')
                    if scene.sfUseCompositing:
                        scene.render.display_mode = 'NONE'
                        if 'NODE_EDITOR' not in bpy.context.screen.areas:                        
                            for area in bpy.context.screen.areas:
                                if area.type == 'IMAGE_EDITOR':
                                    area.type = 'NODE_EDITOR'
                                    sd = area.spaces[0]
                                    sd.tree_type = 'CompositorNodeTree'
                                    sd.show_backdrop = True                      
                                    break
        if func == 'ambient':
            ao = scene.sfUnifiedAmbient
            for world in bpy.data.worlds:
                w = world.light_settings
                w.use_ambient_occlusion = True
                w.ao_factor = ao
            for screen in bpy.data.screens:
                for area in screen.areas:
                    if area.type == 'VIEW_3D':
                        view = 0
                        if area.spaces:
                            if area.spaces[0].lock_camera:
                                view = area.spaces[0]
                        else:
                            if bpy.context.space_data.lock_camera:
                                view = bpy.context.space_data
                        if view:
                            view.fx_settings.use_ssao = True                            
                            fx  = view.fx_settings
                            fx.ssao.factor = (ao * 3)                            
                            if fx.ssao.samples < 5:
                                fx.ssao.samples = 20
        if func == 'ambient_off':
            for world in bpy.data.worlds:
                w = world.light_settings
                w.use_ambient_occlusion = False
            for screen in bpy.data.screens:
                for area in screen.areas:
                    if area.type == 'VIEW_3D':
                        view = 0
                        if area.spaces:
                            if area.spaces[0].lock_camera:
                                view = area.spaces[0]
                        else:
                            if bpy.context.space_data.lock_camera:
                                view = bpy.context.space_data
                        if view:
                            view.fx_settings.use_ssao = False
        if func == 'dof':
            if context.active_object != None:
                scene.sfCFocus = ob.name
                try:
                    node = bpy.context.scene.node_tree.nodes['sf_dNode']
                    node.mute = False
                except:
                    pass
            else:
                userMsg = "There is no selected object to focus"
        if func == 'remove_dof':
            scene.sfCFocus = ''
            try:
                node = bpy.context.scene.node_tree.nodes['sf_dNode']
                node.mute = True
            except:
                pass
        if func == 'track':
            if context.active_object != None:
                scene.sfCTarget = ob.name
            else:
                userMsg = "There is no selected object to track"
        if func == 'untrack':
            scene.sfCTarget = ''
        if func == 'track_path':
            lastActive = bpy.context.active_object
            cam = scene.camera
            scene.objects.active = cam
            for con in cam.constraints:
                if con.type == 'FOLLOW_PATH':
                    if con.use_curve_follow:
                        con.use_curve_follow = False
                    else:
                        bpy.ops.object.location_clear()
                        bpy.ops.object.rotation_clear()
                        bpy.ops.object.scale_clear()             
                        con.use_curve_follow = True
            scene.objects.active = lastActive
        if func == 'follow_path':
            sel = bpy.context.selected_objects
            curve = bpy.context.active_object
            currentFrame = scene.frame_current
            points = []
            for ob in bpy.data.objects:
                if hasattr(ob.animation_data, 'action'):
                    anim = ob.animation_data                    
                    if hasattr(anim.action, 'fcurves'):
                        for fcurve in anim.action.fcurves:
                            for key in fcurve.keyframe_points:
                                try:
                                    points.append(key.co[0])
                                except:
                                    pass
            if points:
                evalTime =  abs(max(points))    
                if evalTime < scene.render.fps * 4:
                    evalTime = scene.render.fps * 4                        
            else:
                evalTime = scene.render.fps * 4
            for ob in sel:
                ob.select = False
            if curve.type != 'CURVE':
                for ob in bpy.data.objects:
                    if ob.type == 'CURVE':
                        curve = ob
                        break
            if curve.type == 'CURVE':
                change = ['Nurbs', 'Bezier']
                for name in change:
                    if name in curve.name:
                        curve.name = 'Animation Path'
                bpy.ops.object.transform_apply(location = True, 
                rotation = True, scale = True)
                cam = bpy.context.scene.camera
                cam.hide = False
                scene.objects.active = cam
                cam.select = True
                bpy.ops.object.sf_parent(type="none")
                followPathExists = False
                for con in cam.constraints:
                    if con.type == 'FOLLOW_PATH':    
                        followPathExists = True
                        con.target = curve
                        con.forward_axis = 'TRACK_NEGATIVE_Z'
                        con.up_axis = 'UP_Y'
                        con.use_curve_follow = True
                        for spline in curve.data.splines:
                            if spline.resolution_u < 20:
                                spline.resolution_u = 20
                if followPathExists == False:                   
                    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
                    for con in cam.constraints:
                        if con.type == 'FOLLOW_PATH':
                            ctx = bpy.context.copy()
                            ctx['constraint'] = con
                            while cam.constraints[0] != con:
                                bpy.ops.constraint.move_up(ctx, 
                                constraint=con.name)
                            con.show_expanded = False
                            con.target = curve                        
                            con.forward_axis = 'TRACK_NEGATIVE_Z'
                            con.up_axis = 'UP_Y'
                            con.use_curve_follow = True
                            for spline in curve.data.splines:
                                if spline.resolution_u < 20:
                                    spline.resolution_u = 20
                            bpy.context.scene.objects.active = cam
                bpy.ops.object.location_clear()
                bpy.ops.object.rotation_clear()
                bpy.ops.object.scale_clear() 
                cam.select = False
                bpy.context.scene.objects.active = curve
                for ob in sel:
                    ob.select = True
                animateCurve = True
                if hasattr(curve.data.animation_data, 'action'): 
                    if hasattr(curve.data.animation_data.action, 'fcurves'): 
                        animateCurve = False
                if animateCurve:           
                    curve.data.path_duration = evalTime
                    curve.data.eval_time = 0
                    curve.data.keyframe_insert(data_path="eval_time", 
                    frame = 0)            
                    curve.data.eval_time = evalTime
                    curve.data.keyframe_insert(data_path="eval_time", 
                    frame= evalTime)
                    override = fu2('DOPESHEET_EDITOR')
                    if override:
                        bpy.ops.anim.channels_collapse(override)
                    else:
                        aType = bpy.context.area.type
                        bpy.context.area.type = 'DOPESHEET_EDITOR'
                        bpy.ops.anim.channels_collapse()
                        bpy.context.area.type = aType
                    scene.frame_current = currentFrame
                    curve.data.eval_time = 0             
            else:
                userMsg = "There are no curves to use as a camera path"
        if func == 'reverse_path':
            mode = bpy.context.mode
            lastActive = bpy.context.active_object
            curve = 0
            if scene.camera:
                if scene.camera.constraints:
                    for con in scene.camera.constraints:
                        if con.type == 'FOLLOW_PATH':
                            if con.target:
                                curve = con.target                                
                                con.forward_axis = 'TRACK_NEGATIVE_Z'        
            if curve:
                scene.objects.active = curve            
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.curve.select_all(action='SELECT')
                bpy.ops.curve.switch_direction()
                curve.data.eval_time = 0
            fu1(mode)
            scene.objects.active = lastActive    
        if func == 'reset_path':
            if scene.camera:
                sel = bpy.context.selected_objects
                bpy.ops.object.select_all(action='DESELECT')
                scene.camera.hide = False
                scene.camera.select = True
                bpy.ops.object.location_clear()
                bpy.ops.object.rotation_clear()
                bpy.ops.object.scale_clear() 
                if scene.camera.constraints:
                    for con in scene.camera.constraints:
                        if con.type == 'FOLLOW_PATH':
                            if con.target:
                                curve = con.target 
                                curve.data.eval_time = 0  
                bpy.ops.object.select_all(action='DESELECT')
                for ob in sel:
                    ob.select = True
        if func == 'stop_follow_path':
            lastActive = bpy.context.active_object
            sel = bpy.context.selected_objects
            bpy.ops.object.select_all(action='DESELECT')
            cam = scene.camera
            scene.objects.active = cam
            prevCursor = scene.cursor_location.xyz
            bpy.ops.view3d.snap_cursor_to_active()
            for con in cam.constraints:
                if con.type == 'FOLLOW_PATH':                    
                    cam.constraints.remove(con)
            cam.location.xyz = scene.cursor_location.xyz            
            scene.cursor_location = prevCursor.xyz            
            scene.objects.active = lastActive
        if func == 'mist':
            scene.render.layers.active = scene.render.layers[0]
            layer = scene.render.layers.active            
            aType = bpy.context.area.type
            nodes = scene.node_tree.nodes
            links = scene.node_tree.links            
            for world in bpy.data.worlds:
                layer.use_pass_mist = True
                mist = world.mist_settings
                mist.use_mist = True
            if scene.mistInit:
                for world in bpy.data.worlds:
                    mist = world.mist_settings
                    if mist.depth == 250:
                        mist.depth = 25
                        mist.intensity = 0
                        mist.start = 5
                    scene.mistInit = False
            if ren == 'CYCLES':
                bpy.context.area.type = 'NODE_EDITOR'
                bpy.context.space_data.tree_type = 'CompositorNodeTree'
                scene.use_nodes = True
                try:
                    rNode = nodes['sf_rNode']
                    rNode.mute = False
                    mNode = nodes['sf_mNode']
                    mNode.mute = False
                    cNode = nodes['sf_cNode']
                    cNode.mute = False
                    mNode.blend_type = 'MIX'
                    bgNode = nodes['Background']
                    links.new(rNode.outputs['Mist'], mNode.inputs['Fac'])
                    links.new(rNode.outputs['Image'], mNode.inputs[1])
                    links.new(bgNode.outputs['Image'], mNode.inputs[2])
                except:                    
                    rNode = 0
                    for node in nodes:
                        if node.type == 'R_LAYERS':
                            rNode = node
                            node.mute = False
                            break
                    if rNode == 0:
                        rNode = nodes.new(type="CompositorNodeRLayers")
                        rNode.name = 'sf_rNode'                        
                    mNode = 0
                    for node in nodes:
                        if node.name == 'sf_mNode':
                            mNode = node
                            node.mute = False                            
                            break
                    if mNode == 0:
                        mNode = nodes.new(type="CompositorNodeMixRGB")
                        mNode.name = 'sf_mNode'
                    mNode.inputs[0].default_value = 1  
                    cNode = 0
                    for node in nodes:
                        if node.type == 'COMPOSITE':
                            cNode = node
                            node.mute = False                            
                            break
                    if cNode == 0:
                        cNode = nodes.new(type="CompositorNodeComposite")
                        cNode.name = 'sf_cNode'
                    vNode = 0
                    for node in nodes:
                        if node.type == 'VIEWER':
                            vNode = node
                            break
                    if vNode == 0:
                        vNode = nodes.new(type='CompositorNodeViewer')
                        vNode.location = (800,-140)
                        links.new(mNode.outputs['Image'], vNode.inputs['Image'])
                    rNode.location = (-400,0)
                    mNode.location = (600,0)
                    cNode.location = (800,0)
                    links.new(rNode.outputs['Image'], mNode.inputs[1])
                    links.new(rNode.outputs['Mist'], mNode.inputs['Fac'])
                    links.new(mNode.outputs['Image'], cNode.inputs['Image'])
                    if 'Background' not in nodes:
                        if len(scene.render.layers) < 2:
                            bpy.ops.scene.render_layer_add()
                            bgLayer = scene.render.layers[1]
                            bgLayer.use_solid = False
                            bgLayer.use_strand = False
                            rNode2 = nodes.new(type = 'CompositorNodeRLayers')
                            rNode2.location = (-400,-250)
                            rNode2.layer = bgLayer.name
                            rNode2.name = 'Background'
                            rNode2.label = 'Background'                            
                            links.new(rNode2.outputs['Image'],mNode.inputs[2])
                try: 
                    nodes = bpy.context.scene.node_tree.nodes
                    world = bpy.context.scene.world
                    try: 
                        node = world.node_tree.nodes['Background']
                        color = node.inputs[0].default_value
                    except:
                        pass
                    nodes['sf_mNode'].inputs[2].default_value = color
                    nodes['sf_dNode'].mute = True
                except:
                    pass
            bpy.context.area.type = aType
            if bpy.context.screen.name == 'Shader':
                bpy.context.space_data.tree_type = 'ShaderNodeTree'
        if func == 'mist_off':
            scene.render.layers.active = scene.render.layers[0]
            nodes = scene.node_tree.nodes
            layer = scene.render.layers.active
            layer.use_pass_mist = False
            for world in bpy.data.worlds:
                world.mist_settings.use_mist = False
            try:
                mNode = nodes['sf_mNode']
                if ren == 'CYCLES':
                    mNode.inputs['Fac'].default_value = 0
                else:
                    mNode.inputs['Fac'].default_value = 1
            except:
                pass
        if 'record_' in func:            
            if scene.camera:
                bpy.ops.object.mode_set(mode='OBJECT')
                for ob in bpy.context.selected_objects:
                    ob.select = False
                cam = scene.camera
                cam.hide = False
                cam.select = True
                bpy.ops.anim.keyframe_insert()
                bpy.ops.screen.sf_frame_shut()
                if scene.camera.constraints:
                    bpy.ops.object.constraints_clear()
                userMsg = 'Camera constraints are removed to use Walk or Fly mode'
                inputs = context.user_preferences.inputs
                if func == 'record_walkmode':
                    inputs.navigation_mode = 'WALK'
                    bpy.ops.view3d.navigate('INVOKE_DEFAULT')
                if func == 'record_flymode':
                    inputs.navigation_mode = 'FLY'                        
                    bpy.ops.view3d.navigate('INVOKE_DEFAULT')
                userpref = context.user_preferences
                userpref.edit.use_keyframe_insert_available = False
                scene.tool_settings.use_keyframe_insert_auto = True
                bpy.ops.screen.animation_play()
        if 'record_' not in func:
            fu1(mode)  
        if userMsg:
            self.report({'INFO'}, userMsg)       
        func = ''
        return{'FINISHED'}
def fu16():    
    scene = bpy.context.scene
    userPref = bpy.context.user_preferences
    system = userPref.system
    props = system.bl_rna.properties
    availableTypes = props['compute_device_type'].enum_items.keys()
    if system.compute_device_type == 'NONE' or scene.cycles.device == 'CPU':
        if len(availableTypes) > 1:
            deviceType = 'NONE'
            for deviceType in availableTypes:
                if 'CUDA' in deviceType:
                    system.compute_device_type = deviceType
                    break
                if deviceType != 'NONE':
                    system.compute_device_type = deviceType
                    break
            if deviceType != 'NONE':    
                availableDevices = props['compute_device'].enum_items.keys()                
                multi_device = []
                normal_device = []
                for device in availableDevices:        
                    if 'MULTI' in device:
                        multi_device.append(device)
                    else:
                        normal_device.append(device)                
                if multi_device:
                    multi = []
                    for d in multi_device:
                        if d.isdigit():
                            multi.append(int(d))        
                    if multi:
                        maxMulti = max(multi)            
                        for device in multi_device:
                            if str(maxMulti) in device:
                                system.compute_device = device
                                break
                    else:
                        system.compute_device = multi_device[0]                
                if normal_device:
                    normal = []
                    for d in normal_device:
                        if d.isdigit():
                            normal.append(int(d))          
                    if normal:    
                        maxNormal = max(normal)      
                        for device in normal_device:
                            if str(maxNormal) in device:
                                system.compute_device = device
                                break        
                    else:
                        system.compute_device = normal_device[0]    
                scene.cycles.device = 'GPU'
def fu17(scene):
    bpy.app.handlers.render_cancel.remove(fu18)
    bpy.app.handlers.render_complete.remove(fu17)     
    wm = bpy.context.window_manager    
    wm.sfDisableORen = False
def fu18(scene):
    bpy.app.handlers.render_cancel.remove(fu18)
    bpy.app.handlers.render_complete.remove(fu17)   
    wm = bpy.context.window_manager
    wm.sfDisableORen = False
def fu19(self,context):
    scene = bpy.context.scene
    ren = scene.render.engine
    paths = scene.cycles
    paths.transparent_max_bounces = 8
    paths.transparent_min_bounces = 0
    paths.max_bounces = 1
    paths.min_bounces = 1                    
    paths.diffuse_bounces = 1
    paths.glossy_bounces = 4
    paths.transmission_bounces = 8
    paths.volume_bounces = 0       
    paths.use_animated_seed = True           
    paths.debug_use_hair_bvh = True
    if scene.sfOptimizeRender:
        fu16()
    else:
        scene.cycles.device = 'CPU'
    if ren == 'CYCLES':    
        renDevice = scene.cycles.device
        if scene.cycles.device == 'CPU':
            scene.render.tile_x = 16
            scene.render.tile_y = 16
        else:
            scene.cycles.preview_start_resolution = 512
            scene.render.tile_x = 128
            scene.render.tile_y = 128                        
    else:
        scene.render.tile_x = 24
        scene.render.tile_y = 24 
class cl8(bpy.types.Operator):
    bl_idname =i_0[32]
    bl_label =i_0[33]
    bl_description =i_0[34]
    message = bpy.props.StringProperty()
    def execute(self, context):
        scene = bpy.context.scene
        message = self.message     
        scene = bpy.context.scene
        wm = bpy.context.window_manager
        if message == 'RENDER_ERROR':
            scene.sfOptimizeRender = False
            scene.cycles.device = 'CPU'
        return {'FINISHED'}
    def draw(self, context):
        message = self.message
        layout = self.layout
        sub = layout.column()
        sub.scale_y = 0.75
        if message == 'RENDER_ERROR':
            sub.label('It looks like there was an error the last time')
            sub.label('you rendered. This may be due to an issue with')
            sub.label('your graphics card. Sensei Format auto-enables')
            sub.label('GPU rendering if it is detected on your device.')
            sub.label('')
            sub.label('This option is called "Optimize Render" and it')
            sub.label('can be disabled in the render settings menu in')
            sub.label('the bottom right corner of the default workspace')
            sub.label('next to the render button.')
            sub.label('')
            sub.label('In this menu under "Output Options", uncheck the')
            sub.label('option "Optimize Render". To save these changes')
            sub.label('press "File" at the top left of the screen and')
            sub.label('select "Save Startup File". It is best to make')
            sub.label('changes like this directly after opening Blender')
            sub.label('so your startup file stays clean.')
            sub.label('')
            sub.label('Press "OK" below to disable this option now and')
            sub.label('return Blender to the default CPU render method')
            sub.label('to help avoid errors.')        
            sub.label('')
    def invoke(self, context, event):
        width = 300
        height = bpy.context.window.height/2
        return context.window_manager.invoke_props_dialog(self, width, height)
class cl9(bpy.types.Menu):
    bl_label =i_0[35]
    bl_idname =i_0[36]
    def draw(self,context):
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        layout = self.layout
        if bpy.context.scene.render.engine == 'CYCLES':
            layout.prop(scene.cycles, "samples", text="Render Quality")
            layout.prop(scene.cycles, "preview_samples", text="Preview Quality")
        else:
            layout.prop(scene.world.light_settings, "samples", text="Render Quality")
        layout.prop(scene, "frame_step", text="Frame Step")
        layout.prop(scene, 'sfOptimizeRender', text = 'Optimize Render')             
        layout.prop(scene,'auto_advance_render_slot')
        layout.prop(scene, "sfRenderTransparent", text='Use Transparent')
        layout.prop_menu_enum(wm,'sfRenderType', text="Resolution", icon='CHECKBOX_HLT')
class cl10(bpy.types.Menu):
    bl_label =i_0[37]
    bl_idname =i_0[38]
    def draw(self,context):
        layout = self.layout
        col = layout.column()
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        if bpy.context.scene.render.engine =='CYCLES':
            cscene = scene.cycles
            if scene.zbQuickLights == True:
                try:
                    try:
                        node = bpy.data.materials['zbCyclesLight'].node_tree.nodes['Emission']
                    except:
                        for mat in bpy.data.materials:
                            lightMat = 0
                            if 'lamp' in mat.name:
                                lightMat = mat
                                break
                            if 'light' in mat.name:
                                lightMat = mat
                                break
                            if lightMat:
                                for n in nodes:
                                    if 'Emission' in n.name:
                                        node = n
                                        break
                    col.prop(node.inputs['Strength'], "default_value", text="Scene Brightness")
                except:
                    pass
            else:
                col.prop(wm, "sfBrightness")
        if bpy.context.scene.render.engine =='BLENDER_RENDER':
            col.prop(wm, "sfBrightness")
            col.prop(wm, "sfShadowDarkness")
            col.prop(wm, "sfShadowBlur")
        col.separator()
        col.prop(scene.view_settings, "exposure")
        col.prop(scene.view_settings, "gamma")
        col.separator()
        world = scene.world
        if world:
            if world.mist_settings.use_mist:
                set = world.mist_settings
                col.prop(set, 'depth', text='Mist Depth')
                col.prop(set, 'start', text='Mist Range')
        if scene.render.engine == 'BLENDER_RENDER':
            if world:
                if world.light_settings.use_ambient_occlusion:    
                    col.prop(scene,"sfUnifiedAmbient", text="Ambient Value")
                    col.operator("object.sf_cam_options", icon='CHECKBOX_HLT', text="Ambient").func = 'ambient_off'
                else:
                    col.operator("object.sf_cam_options", icon='CHECKBOX_DEHLT', text="Ambient").func = 'ambient'
        if scene.render.engine =='CYCLES':
            col.prop(scene, "zbQuickLights", text="Quick Lights")
        if world:    
            if world.mist_settings.use_mist:
                col.operator('object.sf_cam_options',text='Use Mist',
                icon='CHECKBOX_HLT').func = 'mist_off'
            else:
                col.operator('object.sf_cam_options',text='Use Mist',
                icon='CHECKBOX_DEHLT').func = 'mist'
class cl11(bpy.types.Menu):
    bl_label =i_0[39]
    bl_idname =i_0[40]
    def draw(self, context):
        context = bpy.context
        world = bpy.context.scene.world
        wm = context.window_manager
        scene = context.scene
        layout = self.layout
        col = layout.column(align=True)
        col.operator("object.sf_cam_options", text="Render Animation", icon='RENDER_ANIMATION').func = "render_anim"
        col.operator("sound.mixdown",icon='SPEAKER',text='Render Sound')
        try: 
            bpy.data.images['Render Result']
            col.operator("render.play_rendered_anim",
            text="Play Animation", icon="PLAY")
        except:
            pass
        col.menu("menu.sf_output_options_menu",icon='RENDER_STILL')
        col.prop(scene, "zbGoCycles", text="Use Cycles")
        col.prop(scene, "zbFastMode", text="Fast Mode")
        col.prop(scene, 'sfUseCompositing', text = 'Composite')
def sfBrightness(self,context):
    scene = bpy.context.scene
    wm = bpy.context.window_manager
    ren = bpy.context.scene.render.engine
    try:
        if 'Hemi' in bpy.data.lamps:
            if '-Scene Light' in bpy.data.objects:
                lamp = bpy.data.objects['-Scene Light'].data
            else:
                lamp = bpy.data.lamps['Hemi']
            lamp.energy = self.sfBrightness
            if lamp.use_nodes:
                try:
                    emit = lamp.node_tree.nodes['Emission']
                    emit.inputs[1].default_value = self.sfBrightness
                except:
                    pass
    except:
        pass
    world = bpy.context.scene.world
    b = self.sfBrightness
    wHor = world.horizon_color
    horHSV = colorsys.rgb_to_hsv(wHor[0], wHor[1], wHor[2])        
    horHSV = (horHSV[0], horHSV[1], b)      
    horRGB = colorsys.hsv_to_rgb(horHSV[0], horHSV[1], horHSV[2])
    world.horizon_color = horRGB
    wTex = world.active_texture
    if wTex:
        world.light_settings.environment_energy = self.sfBrightness
    try: 
        world = scene.world
        for node in world.node_tree.nodes:
            if node.type == 'BACKGROUND':
                bgNode = node
                break
        bgNode.inputs['Strength'].default_value = self.sfBrightness
    except:
        pass
def sfShadowDarkness(self,context):
    for lamp in bpy.data.lamps:
        try:
            if lamp.shadow_method != 'NOSHADOW':
                lamp.energy = self.sfShadowDarkness
        except:
            pass
def sfShadowBlur(self,context):
    for lamp in bpy.data.lamps:
        try:
            if lamp.shadow_method != 'NOSHADOW':
                lamp.shadow_soft_size = self.sfShadowBlur
                var = int(self.sfShadowBlur)
                if var < 6:
                    lamp.shadow_ray_samples = 10
                else:
                    lamp.shadow_ray_samples = var + 4
        except:
            pass
class cl12(bpy.types.Operator):
    bl_idname =i_0[41]
    bl_label =i_0[42]
    bl_description =i_0[43]
    func = bpy.props.StringProperty('')
    def execute(self,context):
        currentFrame = bpy.context.scene.frame_current
        func = self.func
        points = []
        for ob in bpy.data.objects:
            if hasattr(ob.data, "animation_data"):
                if hasattr(ob.data.animation_data, "action"):
                    try:
                        for fcurve in ob.data.animation_data.action.fcurves:
                            if fcurve.lock or (fcurve.hide and context.space_data.type == "GRAPH_EDITOR"):
                                continue
                            for keyframe_point in fcurve.keyframe_points:
                                points.append(keyframe_point)
                    except:
                        pass
            if hasattr(ob.animation_data, "action"):
                try:
                    for fcurve in ob.animation_data.action.fcurves:
                        if fcurve.lock or (fcurve.hide and context.space_data.type == "GRAPH_EDITOR"):
                            continue
                        for keyframe_point in fcurve.keyframe_points:
                            points.append(keyframe_point)
                except:
                    pass
        if points:
            if func == 'forward':
                potential=[]
                for p in points:
                    if p.co[0] > currentFrame:
                        potential.append(p.co[0])
                if potential:
                    newFrame = min(potential)
                else:
                    sec = (bpy.context.scene.render.fps / 2)
                    remainder = currentFrame % sec
                    if remainder > 0:
                        newFrame = currentFrame + (sec - remainder)
                    else:
                        newFrame = currentFrame + sec
                bpy.ops.anim.change_frame(frame = newFrame)
            if func == 'reverse':
                potential = []
                for p in points:
                    if p.co[0] < currentFrame:
                        potential.append(p.co[0])
                if potential:
                    newFrame = max(potential) 
                else:
                    sec = (bpy.context.scene.render.fps / 2)
                    remainder = currentFrame % sec
                    if remainder > 0:
                        newFrame = currentFrame - (sec + remainder)
                    else:
                        newFrame = currentFrame - sec
                bpy.ops.anim.change_frame(frame = newFrame)
            if func == 'last':
                last = [0]
                for p in points:
                    last.append(p.co[0])
                last = max(last)
                bpy.ops.anim.change_frame(frame = last)
        else:
            if func == 'last':
                end = bpy.context.scene.frame_end
                bpy.ops.anim.change_frame(frame = end)
            elif func == 'forward':
                sec = (bpy.context.scene.render.fps / 2)
                newFrame = currentFrame + sec
                bpy.ops.anim.change_frame(frame = newFrame)
            elif func == 'reverse':
                sec = (bpy.context.scene.render.fps / 2)
                newFrame = currentFrame - sec
                bpy.ops.anim.change_frame(frame = newFrame)
            else:
                bpy.ops.anim.change_frame(frame = 0)
        func = '' 
        return{'FINISHED'}
def fu20(self,context):
    layout = self.layout
    screen = bpy.context.screen
    row = layout.row(align=True)
    row.scale_x = 1.2
    row.operator("screen.frame_jump", text="", icon='FRAME_PREV').end = False
    if not screen.is_animation_playing:
        row.operator("screen.animation_play", text="", icon='PLAY')
    else:
        row.operator("screen.animation_play", text="", icon='PAUSE')
class cl13(bpy.types.Menu):
    bl_label =i_0[44]
    bl_idname =i_0[45]
    def draw(self, context):        
        scene = bpy.context.scene
        layout = self.layout
        layout.prop(scene, 'sfAutoshutKeyframes', text = 'Auto-shut Keyframes')
        layout.prop(scene, 'sfAutoKeysetAdjust', text = 'Auto Keyset Adjust')
        layout.prop(scene, 'sfASnap', text = 'Disable Timeline Snap')
        layout.prop(scene, 'sfDisableKeySnap', text = 'Disable Keyframe Snap')
        layout.prop_menu_enum(scene, 'sfSnapSize', text='Snap Increment')    
        layout.menu("TIME_MT_playback", text = 'Playback options')
        layout.menu("TIME_MT_autokey", text = 'Record Options')
        layout.menu("DOPESHEET_MT_marker", text = 'Marker Options')        
def fu21():
    icons = bpy.types.UILayout.bl_rna.functions['prop'].parameters['icon'].\
        enum_items.keys()
    icons.remove("NONE")
    icons = [key for key in icons]
    return icons
class WM_OT_icon_info(bpy.types.Operator):
    bl_idname =i_0[46]
    bl_label =i_0[47]
    bl_description =i_0[48]
    icon = bpy.props.StringProperty()
    icon_scroll = bpy.props.IntProperty()
    def invoke(self, context, event):
        bpy.data.window_managers['WinMan'].clipboard = self.icon
        self.report({'INFO'}, "Icon ID: %s" % self.icon)
        return {'FINISHED'}
class CONSOLE_MT_editor_menus(Menu):
    bl_idname =i_0[49]
    bl_label =i_0[50]
    def draw(self, context):
        self.fu3(self.layout, context)
    @staticmethod
    def fu3(layout, context):
        layout.menu("CONSOLE_MT_console")
def sfAutocomplete(self, context):
    wm = bpy.context.window_manager
    keyMaps = wm.keyconfigs.addon.keymaps
    if self.sfAutocomplete:       
        bpy.ops.console.autocomplete()
        if 'Console' in keyMaps:
            for item in keyMaps['Console'].keymap_items:
                item.active = True
    else:
        if 'Console' in keyMaps:
            for item in keyMaps['Console'].keymap_items:
                item.active = False
class CONSOLE_HT_header(Header):
    bl_space_type =i_0[51]
    def draw(self, context):
        scene = bpy.context.scene
        userpref = context.user_preferences
        view = userpref.view
        layout = self.layout
        row = layout.row(align=True)
        if bpy.context.screen.name != 'Hacker':
            row.template_header()
        row.separator()
        row.operator("screen.screen_full_area", text = "",
        icon = "FULLSCREEN_ENTER")
        row.prop(scene, "sfAutocomplete", text="Autocomplete", toggle=True)
        row.separator()
        if bpy.context.screen.name != 'Hacker':
            CONSOLE_MT_editor_menus.draw_collapsible(context, row)
        row = layout.row(align=True)
        sub = row.row(align=True)
        sub.scale_x = 1.5
        try:
            sub.operator("wm.console_toggle", text="", icon ="CONSOLE")
            sub = row.row(align=True)
        except:
            pass
        sub.scale_x = 1
        sub.prop(view, "show_tooltips_python", text ="", icon='COLOR_GREEN')
        sub.prop(scene.icon_props, 'console',text='',icon='SOLID')
        props = scene.icon_props
        if props.console:
            sub = row.row(align=True)
            sub = row.row(align=True)
            sub.scale_x = 0.6
            sub.prop(props, "scroll",text='icons')
            sub = row.row(align=True)
            if len(self.icon_list) == 0:
                sub.label("No icons found")
            else:
                sub.separator()
                for icon in self.icon_list[props.scroll - 1:
                    props.scroll - 1 + self.amount]:
                    sub.operator("wm.icon_info", text="", icon=icon,
                    emboss=False).icon = icon
    def __init__(self):
        self.amount = 20
        self.icon_list = fu21()
def fu22(self,context):
    mode = bpy.context.mode
    layout = self.layout
    col = layout.column(align=True)
    col.separator()
    sub = col.column(align=True)
    sub.scale_y = 1.4
    if mode == 'OBJECT':
        sub.operator('object.mode_set', text='Edit What Text Says',
        icon = 'FONT_DATA').mode = 'EDIT'
    else:
        sub.operator('object.mode_set', text='Finished Editing Text Words',
        icon = 'FONT_DATA').mode = 'OBJECT'
def fu23(self,context):
    layout = self.layout
    layout.operator('marker.camera_bind')
def sfRenderTransparent(self,context):
    scene = bpy.context.scene
    ren = scene.render.engine
    nodes = scene.node_tree.nodes
    links = scene.node_tree.links
    scene.render.layers.active = scene.render.layers[0]
    if self.sfRenderTransparent:
        scene.render.image_settings.color_mode = 'RGBA'        
        scene.cycles.film_transparent = True
        scene.render.alpha_mode = 'TRANSPARENT'
        if scene.use_nodes:
            if ren != 'CYCLES':
                try:
                    rNode = nodes['sf_rNode']
                    cNode = nodes['sf_cNode']
                    vNode = nodes['Viewer']                    
                    links.new(rNode.outputs['Alpha'],cNode.inputs['Alpha'])
                    links.new(rNode.outputs['Alpha'],vNode.inputs['Alpha'])
                except:
                    pass            
    else:
        scene.cycles.film_transparent = False
        scene.render.alpha_mode = 'SKY'
        if scene.use_nodes:
            try:
                rNode = nodes['sf_rNode']   
                for i in range(2):                                
                    l = rNode.outputs['Alpha'].links[0]
                    links.remove(l)
            except:
                pass
class cl14(bpy.types.PropertyGroup):
    wm = bpy.types.WindowManager
    scene = bpy.types.Scene
    wm.sfDisableORen = bpy.props.BoolProperty(default=False)
    text1 = 'Automatically increase the render slot before each render so you can compare'
    text2 = ' your rendered images instead of rendering over them. This option is automatically'
    text3 = ' disabled when using the compositor or multiple render layers.'
    scene.auto_advance_render_slot = bpy.props.BoolProperty(
    name = 'Auto Advance Slot',
    default = True,
    description = text1+text2+text3
    )
    text1 = 'Optimize render performance and speed for Blender Render and Cycles. '
    text2 = 'Will auto-activate GPU rendering if available, adjust light path settings '
    text3 = 'for Cycles as well as adjust tile size to maximize render speed (at minimal '
    text4 = 'cost to stability) for the active render engine.'
    scene.sfOptimizeRender = bpy.props.BoolProperty(
    name = 'Optimize Render',
    default = False,
    update = fu19,
    description = text1+text2+text3+text4
    )
    scene.sfAutocomplete = bpy.props.BoolProperty(
    name = 'SFK Autocomplete',
    default = True,
    description = 'Enable/Disable autocomplete and reference for console (as you type)',
    update = sfAutocomplete    
    )
    scene.sfAutoshutKeyframes = bpy.props.BoolProperty(default = True,
    description = 'Automatically shut close additional keyframe info after keyframe insertion')
    scene.sfAutoKeysetAdjust = bpy.props.BoolProperty(default = True,
    description = 'Automatically adjust keying set to work best for different modes and object types')
    txt1 = 'Send the render output to the compositor "Node Editor" for effects. '
    txt2 = "(also builds required nodes to seperate foreground from background)."
    scene.sfUseCompositing = bpy.props.BoolProperty(default = False,
    description = txt1+txt2)
    scene.sfFrameChainSelect = bpy.props.IntProperty(
    default = 4,
    min = 1,
    description = 'Amount of space between frames to make selections'
    )
    txt1 = 'Expand library below to link or append objects and groups from a selected file ' 
    txt2 = 'into this scene (the link and append buttons will also import any selected '
    txt3 = 'file type which Blender is capable of importing)'
    wm.sfDisplayAssets = bpy.props.BoolProperty(
    update = fu5,
    description = txt1+txt2+txt3)    
    scene.sfCustomization = bpy.props.BoolProperty(
    description = "Customize selection, background and other theme colors"
    )
    scene.sfDisplayAllNames = bpy.props.BoolProperty(
    description = 'Display all names of everything in scene',
    update = sfDisplay
    )
    scene.sfUseCageEdit = bpy.props.BoolProperty(
    description= 'Turn on cage editing of objects when in edit mode',
    update = sfUseCageEdit,
    default = True
    )
    scene.sfHideBevel = bpy.props.BoolProperty(
    description= 'Hide bevel modifier effects of all objects',
    update = sfHideBevel
    )
    scene.sfRenderTransparent = bpy.props.BoolProperty(
    description = 'Render a transparent background instead of the sky\
 texture or color',
    update = sfRenderTransparent,
    )
    wm.sfBrightness = bpy.props.FloatProperty(name='Scene Brightness',
    default = 0.825, min = 0, update = sfBrightness,
    description='Control the brightness of the lamps and background')
    wm.sfShadowDarkness = bpy.props.FloatProperty(name='Shadow Darkness',
    default = 0.3, min = 0, update = sfShadowDarkness,
    description='Control the darkness of lamp shadows in Blender Render')
    wm.sfShadowBlur = bpy.props.FloatProperty(name='Shadow Blur',
    default = 0.65, min = 0, update = sfShadowBlur,
    description='Control the blur, soft size and samples, of all lamps \
 (Use Render Preview button see effects)')
    wm.sfRenderType = bpy.props.EnumProperty(
    items=(
            ('1920', "Render HD 1920-1080", "Render at full HD 1920-1080",
            'RADIOBUT_OFF', 0),
            ('1280', "Render HD 1280-720", "Render at HD (good for youtube)",
            'RADIOBUT_OFF', 1),
            ('4k', "Render 4k Film", "Render your image or animation at\
4k (4096 X 2160) film standard. (Extremely long render)",'RADIOBUT_OFF', 2),
            ('300dpi', "Render 300 DPI", "Converts current resolution size to\
 print quality 300 DPI (long render times)",'RADIOBUT_OFF', 3)
            ), default = '1920', update = fu9
          )
    scene.sfCFocus = bpy.props.StringProperty(
    update = fu8
    )
    scene.sfUnifiedFocus = bpy.props.FloatProperty(
    update = sfUnifiedFocus,
    default = 2,
    min = 0,
    name = "Focus",
    description = "Camera focus (smaller value more blurry, higher less blurry)"
    )
    scene.sfCTarget = bpy.props.StringProperty(
    name="Camera Follow",
    description = "Choose object for camera to follow",
    update = fu7
    )
    scene.sfUnifiedAmbient = bpy.props.FloatProperty(
    description = "Set scene ambience value",
    default = 1,
    min = 0,
    max = 2,
    update = sfUnifiedAmbient
    )
def fu24(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except:
        pass
addon_keymaps = []
def register():
    try:
        wm = bpy.context.window_manager
        global IconProps 
        icons_total = len(fu21())
        icons_per_row = 10
        class IconProps(bpy.types.PropertyGroup):
            console = bpy.props.BoolProperty(name='Show System Icons',
                description='Display the Icons in the console header',
                default=False)
            expand = bpy.props.BoolProperty(name="Expand",
                description="Expand, to display all icons at once",
                default=False)
            scroll = bpy.props.IntProperty(name="Scroll",
                description="Drag to scroll icons",
                default=1, min=1, max=max(1, icons_total - icons_per_row + 1))
        bpy.utils.register_module(__name__) 
        bpy.types.Scene.icon_props = bpy.props.PointerProperty(type=IconProps)
    except:
        pass
    try:
        km = wm.keyconfigs.addon.keymaps.new(name='Console', space_type='CONSOLE')        
        mapThisBitch = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
        'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z','PERIOD', 'QUOTE', 'LEFT_BRACKET', 'RIGHT_BRACKET',
        'ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','ZERO',
        'COMMA']
        for aKey in mapThisBitch:
            kmi = km.keymap_items.new("console.autocomplete", aKey,'RELEASE')
        kmi = km.keymap_items.new("console.autocomplete", 'NINE','RELEASE', shift=True)
        kmi = km.keymap_items.new("console.autocomplete", 'ZERO','RELEASE', shift=True)
        kmi = km.keymap_items.new("console.autocomplete", 'MINUS','RELEASE', shift=True)
        kmi = km.keymap_items.new("console.autocomplete", 'QUOTE','RELEASE', shift=True)
        km = wm.keyconfigs.addon.keymaps.new('Screen', space_type='EMPTY', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('object.sf_cam_options', 'F12', 'PRESS')
        fu24(kmi.properties, 'func', 'render')
        km = wm.keyconfigs.addon.keymaps.new('File Browser Main', space_type='FILE_BROWSER', region_type='WINDOW', modal=False)
        kmi = km.keymap_items.new('object.sf_assets_refresh', 'LEFTMOUSE', 'RELEASE')
        bpy.types.DOPESHEET_MT_marker.prepend(fu23)
        bpy.types.VIEW3D_HT_header.prepend(fu14)
        bpy.types.VIEW3D_PT_view3d_display.append(sfCustomization)
        bpy.types.VIEW3D_PT_view3d_display.append(fu12)        
        bpy.types.DATA_PT_font.append(fu22)
        bpy.types.IMAGE_HT_header.append(fu11)
        bpy.types.NODE_HT_header.append(fu10)
        bpy.types.VIEW3D_HT_header.append(fu6)
        bpy.types.GRAPH_HT_header.append(fu20)
        bpy.types.NLA_HT_header.append(fu20)
        bpy.types.CLIP_HT_header.append(fu20)
        bpy.types.SEQUENCER_HT_header.append(fu20)        
    except:
        pass
def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.DOPESHEET_MT_marker.remove(fu23)
    bpy.types.VIEW3D_HT_header.remove(fu14)
    bpy.types.DATA_PT_font.remove(fu22)
    bpy.types.VIEW3D_PT_view3d_display.remove(fu12)
    bpy.types.VIEW3D_PT_view3d_display.remove(sfCustomization)
    bpy.types.IMAGE_HT_header.remove(fu11)
    bpy.types.NODE_HT_header.remove(fu10)
    bpy.types.VIEW3D_HT_header.remove(fu6)
    bpy.types.GRAPH_HT_header.remove(fu20)
    bpy.types.NLA_HT_header.remove(fu20)
    bpy.types.CLIP_HT_header.remove(fu20)
    bpy.types.SEQUENCER_HT_header.remove(fu20)
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    del addon_keymaps[:]
if __name__ == "__main__":
    register()