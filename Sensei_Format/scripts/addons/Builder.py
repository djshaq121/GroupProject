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
 "name": "Builder",
 "author": "Blender Sensei Blendersensei.com",
 "location": "In the Sensei tab of the tool shelf in the 3D View.",
 "description": "Unifies and enhances functionality of commonly accessed tools",
 "wiki_url": "http://blendersensei.com/zero-brush",
 "category": "Sensei Format"}

import zlib
i_0 = b'x\xda\x85U\xc9r\xdb0\x0c\xfd\x154\x87N2\x93\xe4\x90\\zM\x9c\xa4\xd3\xc5cO\x9c\xa5\xed\x85CK\xb0\xcd\x84"T\x92R\xea~}A\x91Zl\xd5\xedM|\x00\xf1\xb0<P\xb4|\xc1\xcc\x9f\xbb\x95\xa8\x8c\xac\xa5\xd2r\xa9Q\\\\\xbc\xfb \x16w_\xe0q\x1f\x1c\x01\xd4\x05\xb8\xccEVYGV\xa0\xd9H\x93a\xde\xc7\xb9M\x08\\\xde\xc0$:\xed\xdd.\x94\xb5\x8cf\x9a\xcc\x80\x7f\xda\xa00\xe9\xd1\xb9E\xe7\xe0\xdb)|\x076\xfc\x00O\x10\xaf\xc2\x96*\x0b\x0e5\x07Td\xf6\xe3;,\xd3\xc9\xf5\xe1\x17XJ+=\xc2l\xc7\xd2\xa2\xc9\x1f\x94I\x0e\x81\xf26W\x1e\n\xcaG\xf5\xc7/\xb1\xb2T\x88\xbd4\x02W\x8ap\xc7f\xe6\xdd1O,\x06:\t\x06\xdf\x12)\x840\xb1\xa4\x02\xdd\xe6p]/\xa4\xcc\xb8\xb0\xcf\xd4\xe5\x9c\xd0\x06i\x0b\xf2\xb4F\xbf\xc1\xd1\x10V\xa45\xbd\x89R\xfaM\x1f\xeb\xae\x01a\xde\x81S\xf9\xda\xf6&\xb4\xa6K\r\xe2u\xe0\xc8 \x19\xa9\x11B\xa4\xd04\x16F}\xa8a\xdeJ\xe3Vd\x8b\x9e\xf2\xa1\x85vk\xb8\xca_*\xe7!W\x05\x1a\xc7\x84\x0eh5dK\x01\xf7hx\x98h|\x1f|>8\xc7o\x90&\x87\xcaD\xc7\xaeI\x19\x19\x8f\xbf|%\xb5\xde\xee\xc7\xcc8\x8f0\xe6\x82h\xd8\xaaI\x03\xc3b\x00?:N\xaf\xf2tf\xb8\x1c\xa9!^Qf\x1d\x94+cA\xb5\xd4\x15:n\x9f\x85\x8d\xb49\xb8\xca\xaed\x86\x8d\xca\xb4f\xdf\x03\xf4K\xacQ\x8f\xd8\xaf{\xb4\xf9L\x03\xe2\xe5\xdb\x91\xc9\xa0A\x9b\xadSY\x82\xaf+\x95\xa3\x85\xf9\x10\xbbWk\x95\xc3\x92\xf2-$_\xa0\x12yE\xc2\x0cF\xb9\x91\xa9\xd1\xf2XI\x04\xe5&\x85G\x10\x1e\x08\xa6\x1d8X\xce\x8d,\x91o\x90n5\x1c\x00\xf6\xee\x80\xab\xbcy;\x1a\xc7\xa0_V\x14O\xaa\xf2\xa7<\xa6b\xa9\x0c\x9e6CT<2\xeb\x820\xdf\x94\xff\'M\x81^\x1e\xe0\x9a\xb2\tFh\x1fFj\xb56\xa1\xbe\xb5Uy\xd75\x1d\xdav\x15L\xa1\xca\x8f\x9d\xa9\x81\xdc`\xf5 \\\xe3nz\x1e\xd6\x99\xc6\x95\x87\xe3\xf7\xc0\xaf\x1a\xb2\x95,\xb7\xdaD)d\xe1U\x08B9rF\x96g,\xa1p\xf1\x08\x82\xe3\xc9\xf9\xa86/\xf2\xaa\xd4*\xe3\x97\xa4\x97\xc4\xcd.\xd4\xad\xda@D\xcc\xac~\'{R\xd0\xfd\x00\xe2U\xab\xe2\xfb\xe9E\xccn\xf8|z\x98\r1>\x87u\x8c~pLL\xb7F\xc8\x897L;\x9e\x19\xaf\x12\xcb\xb0T5\xf9\x93\xb0\xbb\x7fWf\xdb\xccY9\x10X\x9b\xc72\x1a\x05%c\xc0[v\xe3P\xed\x84\x88\x87\xa7O\xb7\xcf\xe2\xf2&\x1e\x1ef\xb3\xaf\x8b\xfd\xe6\xf9T\xc0\xb5\x96\xe6\xf5\xbf?\xba\x9f\x95\xca^EU\x0b\xe4_A46?\x85\xc7\xa7\x94\xeb\x1f\xbb\xb2\x93*'
i_1 = b'x\xda\x03\x00\x00\x00\x00\x01'
a = str(zlib.decompress(i_0))[2:]
i_0 = a.split('_22!8_')
b = str(zlib.decompress(i_1))[2:]
i_1 = b.split('_22!8_')
import bpy, bmesh, math, addon_utils
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
    try:
        if 'EDIT' in mode:
            mode = 'EDIT'
        if 'TEXTURE' in mode:
            mode = 'TEXTURE_PAINT'
        if 'VERTEX' in mode:
            mode = 'VERTEX_PAINT'
        if 'WEIGHT' in mode:
            mode = 'WEIGHT_PAINT'
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
class cl0(bpy.types.Operator):
    bl_idname =i_0[0]
    bl_label =i_0[1]
    bl_description =i_0[2]
    @classmethod
    def poll(cls, context):
        return context.active_object != None
    def execute(self, context):
        pass
        return {'FINISHED'}
class cl1(bpy.types.Operator):
    bl_idname =i_0[3]
    bl_label =i_0[4]
    shift = bpy.props.BoolProperty(default=False)
    alt = bpy.props.BoolProperty(default=False)
    def modal(self, context, event):
        bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')
        cancelOp = False
        if event.value == 'RELEASE':
            wm = bpy.context.window_manager
            scene = bpy.context.scene
            mode = bpy.context.mode
            editType = mode.startswith('EDIT')
            shift = self.shift
            alt = self.alt
            if 'PAINT' not in mode:    
                if alt:
                    return{'FINISHED'}                               
                else:
                    if scene.sfDisableCursorSnap is False:      
                        space = bpy.context.space_data
                        mode = bpy.context.mode
                        view_3d = space.region_3d
                        origCursor = space.cursor_location.xyz
                        visible = bpy.context.visible_objects  
                        sel = bpy.context.selected_objects                    
                        active = bpy.context.active_object
                        origActive = active
                        goOn = True                 
                        if view_3d.view_perspective == 'ORTHO':                            
                            rot = view_3d.view_rotation    
                            if (0) in rot or (0.5) in rot:                                    
                                bpy.ops.view3d.snap_cursor_to_grid('INVOKE_DEFAULT')
                                goOn = False
                        if goOn:                            
                            if len(visible) > 0:                                
                                if bpy.context.active_object:
                                    ob = bpy.context.active_object    
                                if mode == 'EDIT_MESH':                                    
                                    ts = bpy.context.tool_settings
                                    selMode = ts.mesh_select_mode
                                    vert_sel, edge_sel, face_sel = selMode
                                    ob.update_from_editmode()
                                    vSel = []
                                    eSel = []
                                    fSel = []
                                    if vert_sel:
                                        for item in ob.data.vertices:
                                            if item.select:
                                                vSel.append(item)
                                    if edge_sel:
                                        for item in ob.data.edges:
                                            if item.select:
                                                eSel.append(item)
                                    if face_sel:
                                        for item in ob.data.polygons:
                                            if item.select:
                                                fSel.append(item)
                                    bpy.ops.mesh.select_all(action='DESELECT')
                                if editType is False:
                                    try:
                                        bpy.ops.object.mode_set(mode='OBJECT')
                                    except:
                                        pass
                                    bpy.ops.object.select_all(action='DESELECT')
                                bpy.ops.view3d.snap_cursor_to_selected('INVOKE_DEFAULT')
                                lastCursor = space.cursor_location.xyz
                                bpy.ops.view3d.select('INVOKE_DEFAULT')
                                bpy.ops.view3d.snap_cursor_to_selected('INVOKE_DEFAULT')
                                newCursor = space.cursor_location.xyz
                                if lastCursor.xyz != newCursor.xyz:                                    
                                    if editType is False:
                                        try:
                                            bpy.ops.object.mode_set(mode='OBJECT')
                                        except:
                                            pass
                                        bpy.ops.object.select_all(action='DESELECT')
                                        if shift:
                                            try:
                                                bpy.ops.object.mode_set(mode='EDIT')
                                                active = bpy.context.active_object
                                                if active.type == 'MESH':
                                                    ts = bpy.context.tool_settings
                                                    selMode = ts.mesh_select_mode
                                                    v,e,f = selMode
                                                    ts.mesh_select_mode = (True,True,True)
                                                    bpy.ops.view3d.select('INVOKE_DEFAULT')
                                                    bpy.ops.view3d.snap_cursor_to_selected('INVOKE_DEFAULT')
                                                    ts.mesh_select_mode = (v,e,f)
                                                else:
                                                    bpy.ops.view3d.select('INVOKE_DEFAULT')
                                                    bpy.ops.view3d.snap_cursor_to_selected('INVOKE_DEFAULT')
                                            except:
                                                pass
                                        else:                          
                                            x = (lastCursor[0] - newCursor[0])**2
                                            y = (lastCursor[1] - newCursor[1])**2
                                            z = (lastCursor[2] - newCursor[2])**2                                        
                                            distance = math.sqrt(x + y + z)
                                            if distance > 3.5:
                                                space.cursor_location = origCursor
                                if mode == 'EDIT_MESH':
                                    try:
                                        bpy.ops.mesh.select_all(action='DESELECT')
                                        mesh=bmesh.from_edit_mesh(bpy.context.object.data)
                                        for item in vSel:
                                            if vert_sel:
                                                if item.index < len(ob.data.vertices):
                                                    mesh.verts[item.index].select = True
                                        for item in eSel:
                                            if edge_sel:
                                                if item.index < len(ob.data.edges):
                                                    mesh.edges[item.index].select = True
                                        for item in fSel:
                                            if face_sel:
                                                if item.index < len(ob.data.polygons):
                                                    mesh.faces[item.index].select = True
                                    except:
                                        pass
                            if mode == 'OBJECT':
                                try: 
                                    bpy.ops.object.mode_set(mode='OBJECT')
                                except:
                                    pass
                                bpy.ops.object.select_all(action='DESELECT')
                                bpy.context.scene.objects.active = origActive
                                for ob in sel:
                                    ob.select = True         
                            if event.value == 'DOUBLE_CLICK':
                                bpy.ops.wm.call_menu(name = 'INFO_MT_add')
            return{'FINISHED'}
        return {'RUNNING_MODAL'}
    def invoke(self, context, event):
        bpy.ops.view3d.cursor3d('INVOKE_DEFAULT')
        context.window_manager.modal_handler_add(self)        
        return {'RUNNING_MODAL'}
class cl2(bpy.types.Operator):
    bl_idname =i_0[5]
    bl_label =i_0[6]
    bl_description =i_0[7]
    axis = bpy.props.StringProperty()
    def execute(self,context):    
        axis = self.axis
        scene = bpy.context.scene
        wm = bpy.context.window_manager
        mode = bpy.context.mode
        ob = bpy.context.active_object
        selected = bpy.context.selected_objects
        sd = bpy.context.space_data
        lastPivot = sd.pivot_point
        lastCursor = scene.cursor_location.xyz
        if axis == 'X':
            aSideNames = 'XAXIS'
            conAxis = True, False, False        
        if axis == 'Y':
            aSideNames = 'YAXIS'
            conAxis = False, True, False        
        if axis == 'Z':
            aSideNames = 'ZAXIS'
            conAxis = False, False, True
        if ob: 
            if ob.mode.startswith('EDIT'):
                if ob.type != 'META':                    
                    if mode == 'EDIT_ARMATURE': 
                        sd.pivot_point = 'CURSOR' 
                        bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Z') 
                        for bone in bpy.context.selected_bones:
                            if '.Top' in bone.name or '.Bot' in bone.name:
                                bone.name = 'Bone'                                    
                            if '.Fr' in bone.name or '.Bk' in bone.name:
                                bone.name = 'Bone'                                    
                            if '.r' in bone.name or '.l' in bone.name:
                                bone.name = 'Bone'
                        try: 
                            c = scene.cursor_location
                            arm = bpy.data.armatures[ob.name]
                            c.xyz = bpy.data.objects[arm.name].location.xyz
                        except:
                            pass
                    if wm.sfChooseClone:
                        if bpy.context.mode == 'EDIT_ARMATURE':           
                            bpy.ops.armature.autoside_names(type = aSideNames) 
                            bpy.ops.armature.duplicate()
                            bpy.ops.transform.mirror(constraint_axis=(conAxis))                            
                            if axis == 'Y' or axis == 'Z': 
                                bpy.ops.armature.autoside_names(type = aSideNames)
                                for bone in bpy.context.selected_bones:                                    
                                    if '.Fr' in bone.name:
                                        if bone.name[-2:] == 'Bk':
                                            bone.name = bone.name.split('.Fr')[0] + '.Bk'                                       
                                        if bone.name[-2:] == 'Fr':
                                            bone.name = bone.name.split('.Bk')[0] + '.Fr'                                    
                                    if '.Top' in bone.name:
                                        if bone.name[-3:] == 'Bot':
                                            bone.name = bone.name.split('.Top')[0] + '.Bot'                                        
                                        if bone.name[-3:] == 'Top':
                                            bone.name = bone.name.split('.Bot')[0] + '.Top'                            
                            else:
                                bpy.ops.armature.flip_names()                
                        else:
                            bpy.ops.mesh.duplicate()
                            bpy.ops.transform.mirror(constraint_axis=(conAxis))
                    else:
                        if mode == 'EDIT_ARMATURE':
                            bpy.ops.transform.mirror(constraint_axis=(conAxis))
                            bpy.ops.armature.autoside_names(type=aSideNames)
                        else:
                            bpy.ops.transform.mirror(constraint_axis=(conAxis))  
                    if mode == 'EDIT_ARMATURE':
                        bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Z') 
            else: 
                try: 
                    if ob.type != 'META': 
                        bpy.ops.object.transform_apply(rotation=True)
                except:
                    pass
                if wm.sfChooseClone:
                    bpy.ops.object.duplicate()
                    breakLoop = False
                    for ob in bpy.data.objects:
                        for mod in ob.modifiers:
                            if 'sf_shape_tools' in mod.name:
                                breakLoop = True
                                modOp = mod.operation
                                selected = bpy.context.selected_objects
                                for obj in selected:
                                    obj.select = False
                                scene.objects.active = ob    
                                ob.select = True
                                for obj in selected:
                                    bpy.ops.object.modifier_add(type='BOOLEAN')
                                    for mod2 in ob.modifiers:
                                        if mod2.type == 'BOOLEAN':
                                            if mod2.object is None:
                                                mod2.object = obj
                                                mod2.name = 'sf_shape_tools_' + obj.name
                                                mod2.operation = modOp   
                                                mod2.show_expanded = False
                                                mod2.double_threshold = 0.0000001                                 
                                ob.select = False
                                for obj in selected:
                                    obj.select = True                                                                    
                                break                
                        if breakLoop:
                            break
                selected = bpy.context.selected_objects                
                for ob in selected:
                    scene.objects.active = ob
                    if axis == 'X':                
                        ob.rotation_euler.y = -ob.rotation_euler.y    
                    if axis == 'Y':
                        ob.rotation_euler.z = -ob.rotation_euler.z   
                    if axis == 'Z':
                        ob.rotation_euler.y = -ob.rotation_euler.y                  
                bpy.ops.transform.mirror(constraint_axis=(conAxis))
            if mode != 'EDIT_ARMATURE':
                if ob.type == 'MESH':
                    fu3(ob, scene, selected)
        sd.pivot_point = lastPivot   
        scene.cursor_location.xyz = lastCursor                     
        wm.sfChooseClone = False    
        return{'FINISHED'}
def fu3(ob, scene, selected):
    multires = len([mod for mod in ob.modifiers if mod.type == 'MULTIRES'])
    sd = bpy.context.space_data
    if not multires:
        for ob in selected:
            if 'EDIT' in bpy.context.mode:
                bpy.ops.mesh.flip_normals()
            else:
                sd.show_backface_culling = False
                scene.objects.active = ob
                try: 
                    bpy.ops.object.mode_set(mode='OBJECT')      
                    bpy.ops.object.transform_apply(scale=True,rotation=True)
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.mesh.normals_make_consistent(inside=False)
                    bpy.ops.object.mode_set(mode='OBJECT')
                except:
                    pass
class cl3(bpy.types.Operator):
    bl_idname =i_0[8]
    bl_label =i_0[9]
    bl_description =i_0[10]
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return context.active_object.type == 'MESH'
    def execute(self, context):
        mode = bpy.context.mode
        scene = bpy.context.scene
        selected = bpy.context.selected_objects
        for ob in selected:
            if hasattr(ob,'rigid_body'):
                if ob.rigid_body:
                    if ob.rigid_body.enabled:
                        scene.frame_current = 0
            if ob.type == 'MESH':
                scene.objects.active = ob
                mirrorMod = False
                for mod in ob.modifiers:
                    if mod.type == 'MIRROR':
                        mirrorMod = True
                        break
                if mirrorMod is False:    
                    for mod in ob.modifiers:                    
                        if mod.type == 'ARRAY' or mod.type == 'SIMPLE_DEFORM':
                            bpy.ops.object.modifier_apply(apply_as='DATA',modifier=mod.name)
                if mode == 'OBJECT':
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.separate(type='LOOSE')
                    bpy.ops.object.mode_set(mode='OBJECT')
                    if mirrorMod is False:
                        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
                if 'EDIT' in mode:
                    bpy.ops.object.mode_set(mode='OBJECT')
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.ops.object.mode_set(mode='EDIT')
                    ob = bpy.context.active_object
                    bpy.ops.mesh.separate(type='SELECTED')
                    bpy.ops.object.mode_set(mode='OBJECT')
                    ob.select = False
                    newSelected = bpy.context.selected_objects[0]
                    bpy.context.scene.objects.active = newSelected
                    if mirrorMod is False:
                        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')
        if mode != 'EDIT_MESH':
            if len(selected) == len(bpy.context.selected_objects):
                for ob in selected:
                    if ob.type == 'MESH':
                        scene.objects.active = ob
                        bpy.ops.object.modifier_add(type='EDGE_SPLIT')
                        for mod in ob.modifiers:
                            if mod.type == 'EDGE_SPLIT':
                                mod.split_angle = 0
                                bpy.ops.object.modifier_apply(modifier = mod.name)
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.mesh.separate(type='LOOSE')
                        bpy.ops.object.mode_set(mode='OBJECT')
                        if mirrorMod is False:
                            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        return {'FINISHED'}
class cl4(bpy.types.Operator):
    bl_idname =i_0[11]
    bl_label =i_0[12]
    bl_description =i_0[13]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):        
        scene = bpy.context.scene        
        if bpy.context.active_object.mode.startswith('EDIT'):            
            ob = bpy.context.active_object
            selTypeX, selTypeY, selTypeZ = bpy.context.tool_settings.mesh_select_mode
            modTypes = []
            for mod in ob.modifiers:
                modTypes.append(mod.type)
                if mod.type == 'MULTIRES':
                    lev = mod.levels
                    rend_lev = mod.render_levels
                    bpy.ops.object.modifier_remove(modifier = mod.name)
                    bpy.ops.object.modifier_add(type='SUBSURF')
                    ss = ob.modifiers['Subsurf']                    
                    ss.levels = lev
                    ss.render_levels = rend_lev
            useAdvanced = False
            if scene.sfObFromSelAdvanced:
                beveled = False    
                for mod in ob.modifiers:
                    if mod.type == 'BEVEL': 
                        beveled = True                
                if not beveled:        
                    for mod in ob.modifiers:
                        if mod.type == 'SUBSURF':
                            if mod.levels > 0:
                                if mod.show_viewport:
                                    ob.update_from_editmode()
                                    for face in ob.data.polygons:
                                        if face.select:
                                            useAdvanced = True
                                            break
            if useAdvanced:              
                sel = bpy.context.selected_objects                
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.select_all(action='DESELECT')
                ob = bpy.context.active_object
                ob.select = True
                bpy.ops.object.duplicate()
                ob = bpy.context.active_object         
                adaptiveMod = fu4(ob)                
                for mod in ob.modifiers:
                    if mod.type in ["MULTIRES", "SUBSURF"]:                                    
                        if mod != adaptiveMod:                           
                            lastLevels = mod.levels
                            bpy.ops.object.modifier_apply(modifier=mod.name, apply_as='DATA')            
                            if lastLevels > 1:
                                bpy.ops.object.mode_set(mode='EDIT')
                                bpy.ops.mesh.unsubdivide()
                                bpy.ops.object.mode_set(mode='OBJECT')
                                bpy.ops.object.modifier_add(type='SUBSURF')
                                for mod in ob.modifiers:
                                    if mod.type in ["SUBSURF"]:
                                        if scene.sfUseCageEdit:
                                            mod.show_on_cage = True
                                        mod.levels = (lastLevels - 1)
                                        mod.render_levels = (lastLevels - 1)
                            else:
                                bpy.ops.object.modifier_add(type='SUBSURF')
                                for mod in ob.modifiers:
                                    if mod.type in ["SUBSURF"]:
                                        if scene.sfUseCageEdit:
                                            mod.show_on_cage = True
                                        mod.levels = 1
                                        mod.render_levels = 1                                        
                                        break
                            break
                if adaptiveMod:
                    for i in range(10):
                        bpy.ops.object.modifier_move_down(modifier=adaptiveMod.name)
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.context.tool_settings.mesh_select_mode = [False, False, True]
                bpy.ops.mesh.select_all(action='INVERT')
                bpy.ops.mesh.delete(type="FACE")
                bpy.ops.object.mode_set(mode='OBJECT')
                if 'MIRROR' not in modTypes:
                    if 'ARRAY' not in modTypes:
                        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.context.tool_settings.mesh_select_mode = [selTypeX, selTypeY,
                selTypeZ]
            else:
                bpy.ops.object.mode_set(mode='OBJECT')
                bpy.ops.object.select_all(action='DESELECT')
                bpy.ops.object.mode_set(mode='EDIT')
                ob = bpy.context.active_object
                bpy.ops.mesh.duplicate()
                bpy.ops.mesh.separate(type='SELECTED')
                bpy.ops.object.mode_set(mode='OBJECT')
                ob.select = False
                newSelected = bpy.context.selected_objects[0]
                bpy.context.scene.objects.active = newSelected
                if 'MIRROR' not in modTypes:
                    if 'ARRAY' not in modTypes:
                        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')                
        return {'FINISHED'}
def fu4(ob):
    adaptiveMod = 0
    try:
        if ob.cycles.use_adaptive_subdivision:
            for mod in ob.modifiers:
                if mod.type == 'SUBSURF':
                    if mod == ob.modifiers[-1]:
                        adaptiveMod = mod
                        break
    except:
        pass
    return adaptiveMod
class cl5(bpy.types.Operator):
    bl_idname =i_0[14]
    bl_label =i_0[15]
    bl_description =i_0[16]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        needActive = True
        for ob in bpy.context.selected_objects:
            if ob == bpy.context.scene.objects.active:
                needActive = False
        if needActive:
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob
                break            
        bpy.ops.object.join()
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        return {'FINISHED'}
class cl6(bpy.types.Operator):
    bl_idname =i_0[17]
    bl_label =i_0[18]
    bl_description =i_0[19]
    bl_options = {'REGISTER', 'UNDO'}
    func = bpy.props.StringProperty()
    def execute(self, context):
        func = self.func
        scene = bpy.context.scene        
        sel = bpy.context.selected_objects
        curve = bpy.context.active_object
        currentFrame = scene.frame_current        
        if func == 'follow_path':
            if len(sel) > 2:
                msg = 'Select one object then shift-select one path to use "Follow"'
                self.report({'INFO'}, msg)
            else:
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
                    ob = 0
                    for obj in sel:
                        if obj.type != 'CURVE':
                            ob = obj
                        else:
                            obj.select = False
                    ob.hide = False
                    scene.objects.active = ob
                    ob.select = True
                    rbOb = 0
                    if ob.rigid_body:
                        ob.rigid_body.kinematic = True
                        rbOb = ob
                    selectedPoints = False
                    if ob.animation_data:
                        if hasattr(ob.animation_data, 'action'):
                            action = ob.animation_data.action
                            if hasattr(action, 'fcurves'):
                                for fc in action.fcurves:
                                    if 'location' in fc.data_path:
                                        for pt in fc.keyframe_points:
                                            selectedPoints = True
                                            pt.select_control_point = True
                                    else:
                                        for pt in fc.keyframe_points:
                                            pt.select_control_point = False
                    if selectedPoints:  
                        aType = bpy.context.area.type
                        bpy.context.area.type = 'DOPESHEET_EDITOR'                            
                        bpy.ops.action.delete()
                        bpy.context.area.type = aType
                    followPathExists = False
                    for con in ob.constraints:
                        if con.type == 'FOLLOW_PATH':    
                            followPathExists = True
                            con.target = curve
                            con.forward_axis = 'TRACK_NEGATIVE_Y'
                            con.up_axis = 'UP_Z'
                            con.use_curve_follow = True
                            for spline in curve.data.splines:
                                if spline.resolution_u < 20:
                                    spline.resolution_u = 20
                    if followPathExists == False:                   
                        bpy.ops.object.constraint_add(type='FOLLOW_PATH')
                        for con in ob.constraints:
                            if con.type == 'FOLLOW_PATH':
                                ctx = bpy.context.copy()
                                ctx['constraint'] = con
                                while ob.constraints[0] != con:
                                    bpy.ops.constraint.move_up(ctx, 
                                    constraint=con.name)
                                con.show_expanded = False
                                con.target = curve                        
                                con.forward_axis = 'TRACK_NEGATIVE_Y'
                                con.up_axis = 'UP_Z'
                                con.use_curve_follow = True
                                for spline in curve.data.splines:
                                    if spline.resolution_u < 20:
                                        spline.resolution_u = 20
                                for ob in sel:
                                    if ob.type == 'CURVE':
                                        scene.objects.active = ob
                                        ob.select = True
                                    else:
                                        ob.select = False    
                                for ob in sel:
                                    if ob.type == 'CURVE':
                                        ob.select = False
                                    else:
                                        scene.objects.active = ob
                                        ob.select = True 
                    bpy.ops.object.location_clear()
                    bpy.ops.object.rotation_clear()
                    ob.select = False
                    scene.objects.active = curve
                    for ob in sel:
                        if ob.type == 'CURVE':
                            ob.select = True
                        else:
                            ob.select = False
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
                    if rbOb:
                        rbOb.select = True
                        scene.objects.active = rbOb
        if func == 'reverse_curve':   
            mode = bpy.context.mode
            lastActive = bpy.context.active_object
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.curve.select_all(action='SELECT')
            bpy.ops.curve.switch_direction()
            curve.data.eval_time = 0        
            fu1(mode)             
        return {'FINISHED'}
class cl7(bpy.types.Operator):
    bl_idname =i_0[20]
    bl_label =i_0[21]
    bl_description =i_0[22]
    bl_options = {'REGISTER', 'UNDO'}
    tool = bpy.props.StringProperty()
    @classmethod
    def poll(cls, context):
        return context.active_object
    def execute(self,context):    
        scene = bpy.context.scene    
        tool = self.tool
        ob = bpy.context.active_object
        if 'ORIGIN_TO' in tool:
            bpy.ops.object.mode_set(mode='OBJECT')
            if tool == 'ORIGIN_TO_CENTER':
                bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY',center='BOUNDS')
            if tool == 'ORIGIN_TO_MASS':
                bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
            if tool == 'ORIGIN_TO_CURSOR':
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')        
        if tool == 'RESET':
            bpy.ops.object.location_clear()
            bpy.ops.object.rotation_clear()
            bpy.ops.object.scale_clear()            
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
        if tool == 'APPLY':
            bpy.ops.object.transform_apply(location = False, rotation = True,
            scale = True)
        if tool == 'LOCK_X_LOC':
            if ob.lock_location[0]:
                ob.lock_location[0] = False
            else:
                ob.lock_location[0] = True
        if tool == 'LOCK_Y_LOC':
            if ob.lock_location[1]:
                ob.lock_location[1] = False
            else:
                ob.lock_location[1] = True
        if tool == 'LOCK_Z_LOC':
            if ob.lock_location[2]:
                ob.lock_location[2] = False
            else:
                ob.lock_location[2] = True
        if tool == 'LOCK_X_ROT':
            if ob.lock_rotation[0]:
                ob.lock_rotation[0] = False
            else:
                ob.lock_rotation[0] = True
        if tool == 'LOCK_Y_ROT':
            if ob.lock_rotation[1]:
                ob.lock_rotation[1] = False
            else:
                ob.lock_rotation[1] = True
        if tool == 'LOCK_Z_ROT':
            if ob.lock_rotation[2]:
                ob.lock_rotation[2] = False
            else:
                ob.lock_rotation[2] = True
        if tool == 'LOCK_X_SCALE':
            if ob.lock_scale[0]:
                ob.lock_scale[0] = False
            else:
                ob.lock_scale[0] = True
        if tool == 'LOCK_Y_SCALE':
            if ob.lock_scale[1]:
                ob.lock_scale[1] = False
            else:
                ob.lock_scale[1] = True
        if tool == 'LOCK_Z_SCALE':
            if ob.lock_scale[2]:
                ob.lock_scale[2] = False
            else:
                ob.lock_scale[2] = True
        return{'FINISHED'}
class cl8(bpy.types.Operator):
    bl_idname =i_0[23]
    bl_label =i_0[24]
    bl_description =i_0[25]
    bl_options = {'REGISTER', 'UNDO'}
    type = bpy.props.StringProperty(default='none')
    @classmethod
    def poll(cls, context):
        return context.active_object
    def execute(self, context):
        scene = bpy.context.scene
        ob = bpy.context.active_object
        if ob.parent:
            if self.type != 'add':
                bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
                try:
                    bpy.ops.object.modifier_remove(modifier="Armature")
                except:
                    pass
            else:
                try:
                    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
                except:
                    bpy.ops.object.parent_clear(type='CLEAR')
                    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        else:
            if ob.type != 'ARMATURE':
                bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
            else:                
                if ob.children:
                    bpy.ops.object.parent_set(type='BONE')
                else:                
                    sel = bpy.context.selected_objects 
                    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
                    if ob.animation_data is None:
                        recalculate = True
                        for bone in ob.pose.bones:
                            for con in bone.constraints:
                                if con.type == 'IK':
                                    if con.pole_target:
                                        if con.pole_angle > 0.1:
                                            recalculate = False
                                        if con.pole_angle < -0.1:
                                            recalculate = False
                                        break
                        if recalculate:
                            bpy.ops.object.mode_set(mode='EDIT')
                            bpy.ops.armature.select_all(action='SELECT')
                            bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Z')
                            bpy.ops.object.mode_set(mode='OBJECT')
                    newArm = ob
                    child = ob.children[0]
                    scene.objects.active = child
                    for x in range(20):
                        bpy.ops.object.modifier_move_up(modifier="Armature")
                    scene.objects.active = newArm
                    bpy.ops.object.mode_set(mode='POSE')
                    newArm.data.use_auto_ik = True
                    newArm.show_x_ray = True
                    newArm.data.draw_type = 'WIRE'
                    if not ob.pose_library:
                        bpy.ops.poselib.new()
        return {'FINISHED'}
class cl9(bpy.types.Operator):
    bl_idname =i_0[26]
    bl_label =i_0[27]
    bl_description =i_0[28]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self,context):        
        sel = bpy.context.selected_objects
        for ob in sel:
            if ob.type == 'MESH':
                if ob.data.use_auto_smooth:
                    ob.data.use_auto_smooth = False
                    bpy.ops.object.shade_flat()
                else:
                    ob.data.use_auto_smooth = True
                    ob.data.auto_smooth_angle = 0.558505
                    bpy.ops.object.shade_smooth()
            else:
                msg1 = 'Auto smoothing is only for mesh objects.'
                self.report({'INFO'}, msg1)
        return{'FINISHED'}
class cl10(bpy.types.Operator):
    bl_idname =i_0[29]
    bl_label =i_0[30]
    bl_description =i_0[31]
    bl_options = {'REGISTER', 'UNDO'}
    remove = bpy.props.BoolProperty()
    @classmethod
    def poll(cls, context):
        return context.active_object != None
    def execute(self, context):
        scene = bpy.context.scene
        bpy.ops.object.mode_set(mode='OBJECT')
        sel = bpy.context.selected_objects
        userMsg = ''
        for ob in sel:            
            if ob.type == 'MESH':
                if len(ob.data.vertices) < 10000:
                    scene.objects.active = ob
                    adaptiveMod = fu4(ob)                         
                    bevel = len([mod for mod in ob.modifiers if mod.type == 'BEVEL'])
                    solidify = len([mod for mod in ob.modifiers if mod.type == 'SOLIDIFY'])
                    if bevel:  
                        if self.remove:
                            ob.data.use_auto_smooth = False
                            try:
                                bpy.ops.object.modifier_remove(modifier= 'Bevel')
                                bpy.ops.object.shade_flat()
                            except:
                                pass
                        else:
                            bpy.ops.object.modifier_apply(modifier = 'Bevel', apply_as='DATA')
                    else:                                                             
                        if ob.data.users < 2:
                            bpy.ops.object.transform_apply(scale=True)
                        bev = ob.modifiers.new(name='Bevel',type='BEVEL')
                        bev.show_expanded = False
                        bev.segments = 3
                        bev.limit_method = 'ANGLE'
                        bev.angle_limit = 0.349066
                        bev.profile = 1
                        bev.width = 0.035                          
                        for mod in ob.modifiers:
                            if solidify == 0:
                                bpy.ops.object.modifier_move_up(modifier=bev.name)
                            if mod.type == 'SUBSURF':                                
                                if mod != adaptiveMod:
                                    try:
                                        bev.limit_method = 'NONE'
                                        bev.segments = 2
                                        bev.profile = 0.8
                                        mod.levels = 2
                                    except:
                                        pass                            
                        ob.data.use_auto_smooth = False                                   
                        bpy.ops.object.shade_smooth()
                else:
                    userMsg = 'This object is to complex for a bevel modifier.'
            else:
                userMsg = "Can only bevel mesh objects."
        if userMsg:        
            self.report({'INFO'}, userMsg)
        return {'FINISHED'}
def sfPoseButtons(self,context):
    scene = bpy.context.scene
    try:
        ob = bpy.context.active_object
        boneSel = []
        for bone in ob.data.bones:
            if bone.select:
                boneSel.append(bone)            
        pm = ob.pose_library.pose_markers
    except:
        pass
    if self.sfPoseButtons == 'ADDLIBRARY':
        self.sfPoseButtons = 'VOID'
        bpy.ops.poselib.new()
        ob.data.use_auto_ik = True
        arm = ob 
        for ob in bpy.data.objects:
            if ob.hide == False:
                for mod in ob.modifiers:
                    if mod.type == 'ARMATURE':
                        if mod.object == arm:
                            scene.objects.active = ob
                            for i in range(20):
                                bpy.ops.object.modifier_move_up(modifier=mod.name)
                            exit = True
                            break
        scene.objects.active = arm
        bpy.ops.object.mode_set(mode='POSE')
    if self.sfPoseButtons == 'RESET':
        self.sfPoseButtons = 'VOID'
        bpy.ops.pose.select_all(action='SELECT')
        bpy.ops.pose.transforms_clear()
    if self.sfPoseButtons == 'FLIP':
        self.sfPoseButtons = 'VOID'
        boneSelection = []
        for bone in ob.data.bones:
            if bone.select:
                if '.l' in bone.name.lower():
                    if 'L' not in boneSelection:
                        boneSelection.append('L')
                if '.r' in bone.name.lower():
                    if 'R' not in boneSelection:
                        boneSelection.append('R')
        if len(boneSelection) < 2:        
            bpy.ops.pose.select_all(action='SELECT')            
        bpy.ops.pose.copy()
        bpy.ops.pose.paste(flipped=True)
    if self.sfPoseButtons == 'USE':
        self.sfPoseButtons = 'VOID'
        active = pm.active_index
        bpy.ops.pose.select_all(action='SELECT')
        if pm.active:
            bpy.ops.poselib.apply_pose(pose_index=active)
    if self.sfPoseButtons == 'REPLACE':
        self.sfPoseButtons = 'VOID'
        if pm.active:
            newFrame = ob.pose_library.frame_range[1]
            poseName = pm.active.name
            bpy.ops.pose.select_all(action='SELECT')
            bpy.ops.poselib.pose_add(frame=newFrame, name=poseName)
    if self.sfPoseButtons == 'ADD':
        self.sfPoseButtons = 'VOID'
        newFrame = ob.pose_library.frame_range[1]
        bpy.ops.poselib.pose_add(frame=newFrame + 1)
    if self.sfPoseButtons == 'DELETE':
        self.sfPoseButtons = 'VOID'
        active = pm.active_index
        if pm.active:
            if active < 1:
                active = 1
            try:
                bpy.ops.poselib.pose_remove()
                ob.pose_library.pose_markers.active = pm[active - 1]
            except:
                pass
    bpy.ops.pose.select_all(action='DESELECT')
    for bone in boneSel:
        bone.select = True
    return
def sfMeshTools(self,context):
    tool = bpy.context.tool_settings
    if self.sfMeshTools == 'vert':
        tool.mesh_select_mode = [True,False,False]
    if self.sfMeshTools == 'edge':
        tool.mesh_select_mode = [False,True,False]
class sfPhysics(bpy.types.Operator):
    bl_idname =i_0[32]
    bl_label =i_0[33]
    bl_description =i_0[34]
    bl_options = {'REGISTER', 'UNDO'}
    func = bpy.props.StringProperty()
    @classmethod
    def poll(cls, context):
        proceed = True
        ob = bpy.context.active_object
        if ob:
            if ob.type != 'MESH':
                if ob.type != 'EMPTY' or ob.type != 'GROUP':
                    proceed = False
        return proceed
    def execute(self,context):
        scene = bpy.context.scene
        func = self.func
        ob = bpy.context.active_object
        sel = bpy.context.selected_objects
        if 'ADD_RB' in func:
            for ob in sel:
                useRB = False
                if ob.rigid_body:
                    useRB = True                
                if 'ACTIVE' in func:
                    bpy.ops.rigidbody.objects_add(type='ACTIVE')
                else:
                    bpy.ops.rigidbody.objects_add(type='PASSIVE')
                rb = ob.rigid_body
                if ob.animation_data:
                    if hasattr(ob.animation_data, 'action'):
                        if hasattr(ob.animation_data.action, 'fcurves'):
                            rb.kinematic = True
                        else:
                            rb.kinematic = False
                if ob.data.shape_keys:
                    if hasattr(ob.data.shape_keys, 'name'):
                        rb.collision_shape = 'MESH'
                        rb.kinematic = True      
                        rb.use_deform = True 
                        rb.type = 'PASSIVE'
                        msg = 'Objects with shape keys using rigid body physics ' 
                        msg += 'must be set to "Passive" (switched to "Passive")'
                        self.report({'INFO'}, msg)                 
                if ob.constraints:
                    for con in ob.constraints:
                        if con.type == 'FOLLOW_PATH':
                            if con.target:
                                rb.kinematic = True
                                break
                if useRB is False:
                    rb.use_deactivation = True
                    rb.deactivate_linear_velocity = 0.25
                    rb.deactivate_angular_velocity = 0.5
                    rb.linear_damping = 0.035
                    rb.angular_damping = 0.035
                    if func == 'ADD_RB_PASSIVE':
                        rb.collision_margin = 0
        if func == 'FREE_ALL':
            for ob in bpy.data.objects:
                if ob.rigid_body:
                    rbType = ob.rigid_body.type 
                    ob.rigid_body.type = rbType
                    break                
            bpy.ops.ptcache.free_bake_all()
        if func == 'CONNECT':
            if len(sel) > 1:
                if len(sel) < 3:
                    if ob.type == 'MESH':
                        obConnected = False
                        lastRb = 0
                        obToJoin = 0
                        members = [] 
                        for ob in bpy.data.objects:
                            if ob.type == 'EMPTY':
                                if ob.rigid_body_constraint:
                                    rb = ob.rigid_body_constraint
                                    members.append(rb.object1.name)
                                    members.append(rb.object2.name)
                                    done = False
                                    for obj in sel:
                                        if obj.name in members:
                                            lastRb = ob
                                            done = True
                                            break      
                                    if done:
                                        break                              
                        for ob in sel:
                            if ob.name in members:
                                obConnected = True
                            else:
                                obToJoin = ob
                        if obConnected is False:    
                            bpy.ops.rigidbody.objects_add(type='ACTIVE')
                            for ob in sel:
                                rb = ob.rigid_body
                                rb.use_deactivation = True
                                rb.deactivate_linear_velocity = 0.25
                                rb.deactivate_angular_velocity = 0.5
                                rb.linear_damping = 0.035
                                rb.angular_damping = 0.035
                            for obj in bpy.data.objects:
                                obj.select = False
                            ob.select = True 
                            animated = ob 
                            animated.rigid_body.kinematic = True
                            for ob in sel:
                                ob.select = True
                            bpy.context.space_data.show_relationship_lines = True
                            bpy.ops.rigidbody.connect(con_type='HINGE')
                            for obj in bpy.data.objects:
                                obj.select = False
                            for ob in bpy.data.objects:
                                if ob.rigid_body_constraint:
                                    for obj in sel:
                                        if ob.rigid_body_constraint.object1 == obj:
                                            constraint = ob
                                            break
                                        if ob.rigid_body_constraint.object2 == obj:
                                            constraint = ob
                                            break
                            for ob in sel:
                                if ob.rigid_body:
                                    if ob.rigid_body.kinematic is False:
                                        constraint.select = True
                                        ob.select = True
                                        scene.objects.active = ob
                                        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
                                        for obj in bpy.data.objects:
                                            obj.select = False
                                        break
                            constraint.select = True
                            constraint.show_x_ray = True
                            constraint.empty_draw_type = 'SINGLE_ARROW'
                            constraint.rotation_euler[0] = -1.5708
                            constraint.scale = 2,2,2
                            scene.objects.active = constraint
                        else: 
                            if obToJoin:
                                bpy.ops.rigidbody.objects_add(type='ACTIVE')
                                lrb = lastRb.rigid_body_constraint
                                bpy.ops.rigidbody.connect(con_type = lrb.type)                                  
                                newRb = 0 
                                for ob in bpy.data.objects:
                                    if ob.type == 'EMPTY':
                                        if ob.rigid_body_constraint:
                                            rb = ob.rigid_body_constraint
                                            if rb.object1 == obToJoin:
                                                newRb = ob
                                                break
                                            if rb.object2 == obToJoin:
                                                newRb = ob
                                                break
                                for ob in bpy.context.selected_objects:
                                    ob.select = False
                                lastRb.select = True
                                bpy.ops.object.duplicate()
                                lastRb.select = False
                                for ob in bpy.context.selected_objects:
                                    bpy.context.scene.objects.active = ob
                                    finalRb = bpy.context.active_object
                                    break
                                finalRb.location.xyz = newRb.location.xyz
                                frbc = finalRb.rigid_body_constraint                                
                                frbc.object1 = newRb.rigid_body_constraint.object1
                                frbc.object2 = newRb.rigid_body_constraint.object2
                                for ob in bpy.context.selected_objects:
                                    ob.select = False
                                newRb.select = True
                                bpy.ops.object.delete()
                                newRb = finalRb
                                for obj in bpy.data.objects:
                                    obj.select = False
                                newRb.select = True
                                obToJoin.select = True
                                scene.objects.active = obToJoin
                                bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
                                for obj in bpy.data.objects:
                                    obj.select = False
                    else:
                        self.report({'INFO'}, "Can only connect mesh objects.")
                else:
                    self.report({'INFO'}, "Can only connect two objects at a time.")
            else:
                self.report({'INFO'}, "You need to select two objects.")
        if func == 'DEACTIVATED':
            for ob in bpy.data.objects:
                if ob.select:
                    if ob.rigid_body:
                        rb = ob.rigid_body
                        rb.use_deactivation = True
                        rb.use_start_deactivated = True
                        rb.collision_shape = 'MESH'
                        rb.collision_margin = 0
        if func == 'ACTIVATED':
            for ob in bpy.data.objects:
                if ob.select:
                    if ob.rigid_body:
                        ob.rigid_body.use_deactivation = False
                        ob.rigid_body.use_start_deactivated = False
        return{'FINISHED'}
class cl11(bpy.types.Operator):
    bl_idname =i_0[35]
    bl_label =i_0[36]
    bl_description = 'Convert text, surface, curve, or meta object into\
 an editable mesh object'
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self,context):
        bpy.ops.object.mode_set(mode='OBJECT')
        sel = bpy.context.selected_objects
        for ob in sel:
            try:                
                if ob.type == 'META':
                    bpy.ops.object.sf_shape_tools_meta(func='apply')                        
                else:
                    bpy.ops.object.convert(target='MESH')
                    bpy.ops.object.mode_set(mode='EDIT')
                    for i in range(2):
                        bpy.ops.mesh.select_all(action='SELECT')
                        bpy.ops.mesh.tris_convert_to_quads()
                        bpy.ops.mesh.tris_convert_to_quads()
                        bpy.ops.mesh.beautify_fill()
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.uv.smart_project(island_margin = 0.03)
            except:
                pass
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.remove_doubles()
        return{'FINISHED'}
class sfShapeTools(bpy.types.Operator):
    bl_idname =i_0[37]
    bl_label =i_0[38]
    bl_description =i_0[39]
    bl_options = {'REGISTER', 'UNDO'}
    func = bpy.props.StringProperty()
    def execute(self,context):
        bpy.ops.object.mode_set(mode='OBJECT')   
        ob = bpy.context.active_object
        scene = bpy.context.scene
        func = self.func
        userMsg = ''
        if ob: 
            sel = bpy.context.selected_objects
            for ob in sel:
                if ob.type != 'MESH':
                    try:
                        bpy.ops.object.sf_convert_to_mesh()
                    except:
                        ob.select = False     
            sel = bpy.context.selected_objects                                           
            if len(sel) > 0:
                modOb = 0
                needMod = True
                bMod = 0
                for ob in bpy.data.objects:
                    for mod in ob.modifiers:
                        for item in sel:
                            if mod.type == 'BOOLEAN':
                                if mod.object:
                                    if item.name == mod.object.name:
                                        modOb = ob
                                        needMod = False
                                        break
                                else:
                                    bpy.ops.object.modifier_remove(modifier=mod.name)
                        if 'sf_shape_tools_' in mod.name:
                            if len(sel) == 1:
                                needMod = False                                   
                        if modOb:
                            break                                                                             
                    if modOb:
                        break
                if needMod:
                    if 'apply' not in func:                
                        if len(sel) < 2:
                            closest = fu6()
                            if closest:                                
                                scene.objects.active = bpy.data.objects[closest]
                                ob = bpy.context.active_object
                                if ob:
                                    ob.select = True
                                    sel = bpy.context.selected_objects                                
                        if len(sel) > 1:
                            ob = bpy.context.active_object
                            for obj in sel:
                                for mod in obj.modifiers:
                                    if mod.type  in ['BEVEL', 'EDGE_SPLIT']:
                                        mod.show_viewport = False
                                        bpy.ops.object.shade_flat()
                                if obj != bpy.context.active_object:                                                                        
                                    adaptiveMod = fu4(ob)
                                    obj.draw_type = 'BOUNDS'
                                    bName = 'sf_shape_tools_' + ob.name
                                    bMod = ob.modifiers.new(name=bName,type='BOOLEAN')
                                    bMod.object = obj
                                    bMod.show_expanded = False
                                    bMod.double_threshold = 0.0000001
                                    bpy.ops.object.transform_apply(location=False, 
                                    rotation=True, scale=True)
                                    if func == 'cut_out':
                                        bMod.operation = 'DIFFERENCE'
                                    if func == 'combine':
                                        bMod.operation = 'UNION'
                                    if func == 'intersect':
                                        bMod.operation = 'INTERSECT'    
                                    if adaptiveMod:
                                        for mod in ob.modifiers:
                                            bpy.ops.object.modifier_move_down(modifier=adaptiveMod.name)                                       
                                else:                                    
                                    obj.show_wire = True                                    
                                    obj.select = False
                        else:
                            userMsg = "You need another object touching the selected object for this to work."
                else:
                    if 'apply' in func:  
                        print('======================Applying Shape Tools')
                        edge = 0
                        subsurf = False
                        bevel = False
                        multires = False
                        chosen = False
                        lastActive = bpy.context.active_object
                        selected = bpy.context.selected_objects
                        for ob in bpy.data.objects:
                            ob.select = False
                            for mod in ob.modifiers:
                                if 'sf_shape_tools_' in mod.name:
                                    scene.objects.active = ob
                                    ob.select = True
                                    chosen = True                                        
                                    if mod.object:
                                        if mod.object.data.users > 1:                                
                                            bpy.ops.object.make_single_user(type='SELECTED_OBJECTS', 
                                            object=True, obdata=True)
                                    break
                        ob = bpy.context.active_object
                        adaptiveMod = fu4(ob) 
                        if chosen: 
                            for mod in ob.modifiers:                                
                                if mod.type == 'SUBSURF':
                                    if mod != adaptiveMod:
                                        subsurf = True
                                if mod.type == 'multires':
                                    multires = True                                    
                                if mod.type == 'BEVEL':
                                    bevel = True                                
                                if mod.type == 'EDGE_SPLIT':
                                    edge = mod.split_angle
                                    bpy.ops.object.modifier_remove(modifier = mod.name)                          
                            for mod in ob.modifiers:
                                if mod.type in ['SUBSURF', 'MULTIRES']:
                                    if mod != adaptiveMod:
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
                        scene.objects.active = lastActive
                        for ob in selected:
                            ob.select = True
                        goOn = True 
                        if len(sel) == 1:
                            ob = bpy.context.active_object
                            for mod in ob.modifiers:
                                if 'sf_shape_tools_' in mod.name:
                                    try:
                                        bpy.data.objects[mod.object.name].select = True
                                    except:
                                        pass
                                    try:
                                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
                                    except:
                                        bpy.ops.object.modifier_remove(modifier=mod.name)
                                    goOn = False
                            if goOn == False:
                                ob.select = False
                        if goOn:
                            sel = bpy.context.selected_objects
                            for ob in bpy.data.objects:
                                for mod in ob.modifiers:
                                    if 'sf_shape_tools_' in mod.name:
                                        try:
                                            for item in sel:
                                                if item.name == mod.object.name:
                                                    ob.select = False
                                                    scene.objects.active = ob
                                                    modOb = ob
                                                    break
                                        except:
                                            pass
                            if modOb: 
                                for mod in modOb.modifiers:
                                    if 'sf_shape_tools_' in mod.name:
                                        try: 
                                            bpy.data.objects[mod.object.name].select = True
                                        except:
                                            pass
                                        try: 
                                            bpy.ops.object.modifier_apply(apply_as='DATA',
                                            modifier=mod.name)
                                        except:
                                            bpy.ops.object.modifier_remove(modifier=mod.name)
                        bpy.ops.object.delete()
                        if bpy.context.active_object:
                            bpy.context.active_object.select = True
                            ob = bpy.context.active_object
                        ob.show_wire = False
                        mode = bpy.context.mode
                        bpy.ops.object.mode_set(mode='EDIT')
                        bpy.ops.mesh.select_all(action='SELECT')  
                        bpy.ops.mesh.remove_doubles(threshold = 0.001)
                        bpy.ops.mesh.beautify_fill()                        
                        bpy.ops.mesh.dissolve_limited(angle_limit=0, 
                        use_dissolve_boundaries=True)
                        bpy.ops.mesh.face_make_planar()
                        fu1(mode)
                        for mod in ob.modifiers:
                            if mod.type in ['BEVEL', 'EDGE_SPLIT']:
                                mod.show_viewport = True
                            if mod.type == 'BEVEL':
                                ob.data.use_auto_smooth = False
                                mod.profile = 1  
                        if bevel is False:
                            ob.data.use_auto_smooth = True
                            ob.data.auto_smooth_angle = 0.558505                            
                            if ob.data.use_auto_smooth is False:
                                ob.data.use_auto_smooth = True
                                ob.data.auto_smooth_angle = 0.558505                                
                        bpy.ops.object.shade_smooth()    
                        if edge:
                            bpy.ops.object.modifier_add(type='EDGE_SPLIT')
                            ob.modifiers['EdgeSplit'].split_angle = edge                                                                                                                                     
                        if modOb:
                            scene.objects.active = modOb
                    else:                    
                        if modOb:
                            for mod in modOb.modifiers:
                                try:
                                    for ob in sel:
                                        if ob != modOb:
                                            if mod.object == ob:
                                                if func == 'cut_out':
                                                    mod.operation = 'DIFFERENCE'
                                                if func == 'combine':
                                                    mod.operation = 'UNION'
                                                if func == 'intersect':
                                                    mod.operation = 'INTERSECT'
                                except:
                                    pass
                        else: 
                            for ob in bpy.data.objects:
                                if ob.modifiers:
                                    for mod in ob.modifiers:
                                        if 'sf_shape_tools' in mod.name:
                                            scene.objects.active = ob
                                            break
                            ob = bpy.context.active_object
                            for obj in sel:
                                for mod in obj.modifiers:
                                    if mod.type == 'BEVEL':
                                        mod.show_viewport = False
                                        bpy.ops.object.shade_flat()
                                if obj != ob:
                                    obj.draw_type = 'BOUNDS'
                                    bName = 'sf_shape_tools_' + ob.name
                                    bMod = ob.modifiers.new(name = bName, type = 'BOOLEAN')                                    
                                    bMod.object = obj
                                    bMod.show_expanded = False
                                    bMod.double_threshold = 0.0000001
                                    if func == 'cut_out':
                                        bMod.operation = 'DIFFERENCE'
                                    if func == 'combine':
                                        bMod.operation = 'UNION'
                                    if func == 'intersect':
                                        bMod.operation = 'INTERSECT'
                                else:
                                    obj.select = False     
                try: 
                    ob = bpy.context.selected_objects[0]                      
                    scene.objects.active = ob             
                    if 'apply' not in func:     
                        if scene.sfShapeToolsSolid:
                            needSolid = True
                            for mod in ob.modifiers:
                                if mod.type == 'SOLIDIFY':
                                    needSolid = False
                                    break
                            if needSolid:
                                mod = ob.modifiers.new(name='Solidify',type='SOLIDIFY')
                                mod.use_even_offset = True          
                                mod.show_expanded = False                                                                                  
                except:
                    pass                
            else:
                userMsg = "There's no object selected to do stuff to"   
        else:
            userMsg = "You have to select an object first"       
        if userMsg:
            self.report({'INFO'}, userMsg)                        
        return{'FINISHED'}
def sfShapeToolsSolid(self,context):
    scene = bpy.context.scene
    addSolid = False
    if scene.sfShapeToolsSolid:
        for ob in bpy.data.objects:
            if hasattr(ob,'modifiers'):
                for mod in ob.modifiers:
                    if 'sf_shape_tools' in mod.name:
                        addSolid = True
                        break
    if addSolid: 
        for ob in bpy.context.selected_objects:
            hasMod = False
            if ob.modifiers:                
                for mod in ob.modifiers:
                    if mod.type == 'SOLIDIFY':
                        hasMod = True
                        break            
            if hasMod == False:
                mod = ob.modifiers.new(name='Solidify',type='SOLIDIFY')
                mod.show_expanded = False
                mod.use_even_offset = True                
                for modi in ob.modifiers:
                    bpy.ops.object.modifier_move_up(modifier=mod.name)
    else:
        for ob in bpy.context.selected_objects:
            if ob.modifiers:                
                for mod in ob.modifiers:
                    if mod.type == 'SOLIDIFY':
                        bpy.ops.object.modifier_remove(modifier=mod.name)
def sfShapeToolsRes(self,context):
    res = self.sfShapeToolsRes    
    ob = bpy.context.active_object
    if ob.type == 'META':
        ob.data.resolution = res
        ob.data.render_resolution = res
def fu5(self,context):
    scene = bpy.context.scene
    on = self.sfShapeToolsMeta        
    if on:                
        goOn = True
        for ob in bpy.data.objects:
            if ob.type == 'META':      
                goOn = False
                bpy.ops.object.select_all(action='DESELECT')
                if ob.data != bpy.data.metaballs[0]:
                    ob.select = True
                    bpy.context.scene.objects.active = ob
                    break
                else:
                    ob.select = True
                    bpy.context.scene.objects.active = ob
        if goOn:
            bpy.ops.object.metaball_add(type = 'CUBE', radius = 0.05)
            for ob in bpy.data.objects:
                if ob.type == 'META':
                    bpy.context.scene.objects.active = ob
                    break
            ob = bpy.context.active_object
            ob.data.update_method = 'HALFRES'
            ob.data.elements[0].radius = 0.075
            ob.data.elements[0].stiffness = 10
            ob.data.threshold = 5
            ob.data.resolution = scene.sfShapeToolsRes
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mball.select_all(action='SELECT')
            bpy.ops.mball.delete_metaelems()
            bpy.ops.object.mode_set(mode='OBJECT')
            ob.hide_select = True
    else: 
        if len(bpy.data.metaballs) < 2:
            for ob in bpy.data.objects:
                if ob.type == 'META':
                    if ob.hide_select:
                        scene.objects.unlink(ob)
                        ob.user_clear()
                        fu0()
                        break
        needMesh = True            
        for ob in bpy.data.objects:            
            if ob.type == 'MESH':
                bpy.ops.object.select_all(action='DESELECT')
                bpy.context.scene.objects.active = ob
                ob.select = True
                needMesh = False
                break
        if needMesh:
            bpy.ops.mesh.primitive_cube_add()            
def fu6():
    ob = bpy.context.active_object
    closest = 0
    if ob:
        obLoc = ob.location.xyz
        distances = {}
        for obj in bpy.data.objects:
            if obj != ob:
                if obj.type == 'MESH':
                    if obj.hide == False:
                        if obj.users_scene:        
                            objLoc = obj.location.xyz
                            x = (objLoc[0] - obLoc[0])**2
                            y = (objLoc[1] - obLoc[1])**2
                            z = (objLoc[2] - obLoc[2])**2
                            distance = math.sqrt(x + y + z)
                            distances[obj.name] = distance
        if len(distances) > 0:        
            closest = min(distances, key = distances.get)        
    return closest        
class sfShapeToolsMeta(bpy.types.Operator):
    bl_idname =i_0[40]
    bl_label =i_0[41]
    bl_description =i_0[42]
    bl_options = {'REGISTER', 'UNDO'}
    func = bpy.props.StringProperty()
    def execute(self,context):
        scene = bpy.context.scene
        func = self.func
        ob = bpy.context.active_object
        if ob:        
            obLoc = ob.matrix_world.translation.xyz
        else:
            obLoc = scene.cursor_location.xyz   
        if func == 'cube':
            bpy.ops.object.metaball_add(type='CUBE', 
            location = (obLoc[0], obLoc[1], obLoc[2]) )
        if func == 'ellipsoid':
            bpy.ops.object.metaball_add(type='ELLIPSOID', 
            location = (obLoc[0], obLoc[1], obLoc[2]) )
        if func == 'plane':
            bpy.ops.object.metaball_add(type='PLANE', 
            location = (obLoc[0], obLoc[1], obLoc[2]) )
        if func == 'capsule':
            bpy.ops.object.metaball_add(type='CAPSULE', 
            location = (obLoc[0], obLoc[1], obLoc[2]) )
        if func in ['cube','ellipsoid','plane','capsule']:            
            ob = bpy.context.active_object
            ob.show_x_ray = True
            ob.data.update_method = 'HALFRES'
            ob.data.threshold = 5
            ob.data.resolution = scene.sfShapeToolsRes
            ob.data.render_resolution = scene.sfShapeToolsRes
            ob.data.elements[0].radius = .075
            ob.data.elements[0].stiffness = 10
            if func == 'ellipsoid':
                elScale = 1.75                
                ob.data.elements[0].size_x = elScale
                ob.data.elements[0].size_y = elScale   
                ob.data.elements[0].size_z = elScale
                ob.scale.xyz = 25,25,25
                texScale = 0.065
                bpy.ops.transform.resize(
                value=(texScale, texScale, texScale), 
                texture_space = True) 
            if func == 'capsule':
                ob.scale.xyz = 1,25,25
                ob.rotation_euler[1] = 1.5708
                ob.scale[2] = 0.15
                bpy.ops.object.transform_apply(rotation = True, scale=True)                 
                ob.scale[2] = 0.1
                bpy.ops.transform.resize(
                value=(.5, .5, 15), 
                texture_space = True) 
            if func == 'plane':
                r = (ob.data.elements[0].radius) - .15
                bpy.ops.transform.resize(
                value=(1, 1, r), 
                texture_space = True) 
            ob.show_texture_space = False
        if ob:
            if ob.type == 'META':
                if ob.name != 'Mball':
                    if func == 'cut_out':
                        for met in bpy.context.selected_objects:
                            if met.type =='META':
                                met.draw_type = 'BOUNDS'
                                met.show_texture_space = True       
                                met.data.elements[0].use_negative = True 
                    if func == 'combine':
                        for met in bpy.context.selected_objects:
                            if met.type == 'META':
                                met.draw_type = 'TEXTURED'
                                met.show_texture_space = False            
                                met.data.elements[0].use_negative = False
                    if func == 'apply':
                        if len(bpy.data.metaballs) > 1:
                            ob.hide_select = False                   
                            ob.select = True
                            bpy.ops.object.convert(target='MESH')                    
                            ob = bpy.context.active_object
                            ob.name = 'Shape Object'                    
                            bpy.ops.object.select_all(action='DESELECT')
                            for met in bpy.data.objects:
                                if met.type == 'META':
                                    met.select = True
                            bpy.ops.object.delete()           
                            scene.sfShapeToolsMeta = False
                            fu0()
                            bpy.ops.object.select_all(action='DESELECT')
                            bpy.context.scene.objects.active = ob
                            ob.hide_select = False
                            ob.select = True
                            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
                        else:
                            msg1 = "No meta shapes to apply "
                            msg2 = '( "apply" converts meta shapes into a mesh object)'
                            self.report({'INFO'}, msg1+msg2)
                    if func == 'invert':            
                        for met in bpy.data.metaballs:
                            if met != bpy.data.metaballs[0]:
                                state = met.elements[0].use_negative                            
                                met.elements[0].use_negative = not state
            else:
                self.report({'INFO'}, 
                "Need atleast one meta object to be able to use this button")
        return{'FINISHED'}
class cl12(bpy.types.Operator):
    bl_idname =i_0[43]
    bl_label =i_0[44]
    bl_description =i_0[45]
    bl_options = {'REGISTER', 'UNDO'}    
    @classmethod
    def poll(cls, context):             
        return bpy.context.active_object
    def execute(self,context):
        scene = bpy.context.scene
        orginalActiveOb = bpy.context.active_object
        last = scene.cursor_location.xyz
        sel = bpy.context.selected_objects
        ob = bpy.context.active_object
        for ob in sel:
            bpy.ops.object.select_all(action='DESELECT')
            scene.objects.active = ob
            ob.select = True
            bBox = ob.bound_box
            if ob.type in ['EMPTY','MESH']:
                if hasattr(ob, 'users'):
                    if ob.users < 2:
                        if ob.type != 'EMPTY':
                            if ob.data.users > 1:
                                bpy.ops.object.make_single_user(type='SELECTED_OBJECTS',
                                object = True, obdata = True)
                            bpy.ops.object.transform_apply(location=True, 
                            rotation=True, scale=True)
                            scene.cursor_location.x = bBox[0][0]
                            scene.cursor_location.y = bBox[0][1]
                            scene.cursor_location.z = bBox[0][2]                        
                        else:
                            if ob.dupli_type == 'GROUP':
                                if hasattr(ob.dupli_group.library, 'filepath') is False:
                                    msg = "Aligning one group instance affects all other instances from that group."
                                    empty = bpy.context.active_object
                                    lastSelected = bpy.context.selected_objects
                                    for obj in bpy.data.objects:
                                        if obj != bpy.context.active_object:
                                            obj.select = False
                                    bpy.ops.object.duplicate()
                                    bpy.ops.object.sf_make_instance_real()
                                    bpy.ops.object.sf_join_objects()
                                    bBox = bpy.context.active_object.bound_box
                                    bpy.ops.object.transform_apply(location=True, 
                                    rotation=True, scale=True)
                                    scene.cursor_location.x = bBox[0][0]
                                    scene.cursor_location.y = bBox[0][1]
                                    scene.cursor_location.z = bBox[0][2]
                                    bpy.ops.object.delete()
                                    empty.select = True
                                    scene.objects.active = empty
                                else:
                                    msg = "Can not adjust linked group's origin point."                                
                                self.report({'INFO'}, msg)                                  
                        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')                         
            bpy.ops.view3d.snap_selected_to_grid()
        scene.cursor_location = last.xyz
        try:
            scene.objects.active = originalActiveOb
            originalActiveOb.select = True
        except:
            pass
        for ob in sel:
            ob.select = True
        scene.tool_settings.use_snap = True        
        fu0()
        return{'FINISHED'}
class cl13(bpy.types.Operator):
    bl_idname =i_0[46]
    bl_label =i_0[47]
    bl_options = {'REGISTER', 'UNDO'}
    @classmethod
    def poll(cls, context):
        return context.active_object != None
    def execute(self,context):
        scene = bpy.context.scene
        ob = bpy.context.active_object
        modOb = 0
        if ob.select == False:
            for ob in bpy.context.selected_objects:
                bpy.context.scene.objects.active = ob
                break
        if ob.draw_type == 'BOUNDS':
            if ob.type != 'META':
                sel = bpy.context.selected_objects
                for ob in sel:
                    if ob.type != 'MESH':
                        ob.select = False
                sel = bpy.context.selected_objects
                if len(sel) > 0:
                    for ob in bpy.data.objects:
                        if len(ob.modifiers) > 0:
                            for mod in ob.modifiers:
                                if 'sf_shape_tools_' in mod.name:
                                    for obj in sel:
                                        try:
                                            if obj.name == mod.object.name:
                                                newOp = mod.operation
                                                modOb = ob
                                        except:
                                            pass
        if modOb:
            bpy.ops.object.duplicate('INVOKE_DEFAULT')
            sel = bpy.context.selected_objects
            bpy.context.scene.objects.active = modOb
            for ob in sel:
                bpy.ops.object.modifier_add(type='BOOLEAN')
                mod = modOb.modifiers['Boolean']
                mod.name = 'sf_shape_tools_' + ob.name
                mod.operation = newOp
                mod.object = ob
                mod.show_expanded = False
                mod.double_threshold = 0.0000001
            bpy.ops.transform.translate('INVOKE_DEFAULT')
        else:            
            if ob.type == 'META':
                bpy.ops.object.duplicate_move('INVOKE_DEFAULT')
                for ob in bpy.context.selected_objects:
                    if len(bpy.data.metaballs) > 0:
                        ob.show_x_ray = True
            else:                    
                bpy.ops.object.duplicate_move('INVOKE_DEFAULT')
        try: 
            scene.objects.active = bpy.context.selected_objects[0]
        except:
            pass
        return{'FINISHED'}
class cl14(bpy.types.Operator):
    bl_idname =i_0[48]
    bl_label =i_0[49]
    def modal(self, context, event):
        if event.type == 'LEFTMOUSE':
            if event.value == 'RELEASE':    
                scene = bpy.context.scene                            
                ob = bpy.context.active_object
                if ob:                    
                    if scene.sfAutoApplyTransform:                    
                        if ob.type == 'MESH':
                            if len(ob.particle_systems) < 1:
                                if scene.sfAutoApplyTransform:
                                    apply = True
                                    if hasattr(ob.animation_data, 'action'):
                                        if hasattr(ob.animation_data.action, 'keys'):
                                            apply = False
                                    if ob.modifiers:
                                        for mod in ob.modifiers:
                                            if mod.type not in ['SUBSURF','BEVEL','MULTIRES',
                                            'MIRROR','PARTICLE_SYSTEM']:
                                                apply = False
                                                break
                                    if apply:
                                        try:
                                            if ob.data.users < 2:
                                                bpy.ops.object.transform_apply(location=False, 
                                                rotation=False, scale=True)
                                        except:
                                            pass
                return{'FINISHED'} 
        if event.type == 'ESC' or event.type == 'RIGHTMOUSE':
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}
    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        try:
            bpy.ops.transform.resize('INVOKE_DEFAULT')
        except:
            pass
        return {'RUNNING_MODAL'}
class cl15(bpy.types.Menu):
    bl_idname =i_0[50]
    bl_label =i_0[51]
    bl_description =i_0[52]
    def draw(self,context):        
        scene = bpy.context.scene
        layout = self.layout
        layout.operator('object.sf_object_transform',
        text = 'To Object Center', icon='LAYER_ACTIVE').tool = 'ORIGIN_TO_CENTER'
        layout.operator('object.sf_object_transform',
        text = 'To Object Mass', icon='LAYER_ACTIVE').tool = 'ORIGIN_TO_MASS'
        layout.operator('object.sf_object_transform',
        text = 'To 3D Cursor', icon='LAYER_ACTIVE').tool = 'ORIGIN_TO_CURSOR'
class cl16(bpy.types.Menu):
    bl_label =i_0[53]
    bl_idname =i_0[54]
    def draw(self, context):
        scene = bpy.context.scene
        layout = self.layout
        layout.prop(scene, 'sfDisableCursorSnap',
        text = 'Disable Cursor Snapping')
        layout.prop(scene, 'sfObFromSelAdvanced',
        text = 'Advanced Ob-From-Sel')
        layout.prop(scene, 'sfAutoApplyTransform')
        layout.prop(scene,'sfShapeToolsHD')
        layout.prop(scene, 'sfHDShading',
        text = 'Hi-Def Shading')
        layout.prop(scene, 'sfSelectByGroup')
def sfHDShading(self,context):
    scene = bpy.context.scene  
    re = scene.render.engine
    on = self.sfHDShading
    if on:
        scene.sfLastRE = re
        if re == 'CYCLES':
            print('Temporarily switched to Blender Render while in Hi-Def Shading mode.')
            try:
                sceneLight = bpy.data.objects['-Scene Light']
                sceneLight.hide_render = False
            except:
                pass
        scene.render.engine = 'BLENDER_RENDER'
        for lamp in bpy.data.lamps:
            if hasattr(lamp, "shadow_buffer_size"):
                sbs = (lamp.shadow_buffer_size * 10)
                if sbs > 12000:
                    sbs = 12000
                lamp.shadow_buffer_size = sbs
        for screen in bpy.data.screens:
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    if len(bpy.context.screen.areas) > 2:
                        sd = area.spaces[0]
                    else:
                        sd = bpy.context.space_data 
                    if sd.lock_camera is False:
                        sd.viewport_shade = 'MATERIAL'    
                        sd.fx_settings.use_ssao = True
        for mat in bpy.data.materials:       
            try:
                nodes = mat.node_tree.nodes
                for node in nodes:
                    if node.type == 'OUTPUT_MATERIAL':
                        mat.use_nodes = False
            except:
                pass
    else:        
        for lamp in bpy.data.lamps:
            if hasattr(lamp, "shadow_buffer_size"):
                sbs = (lamp.shadow_buffer_size / 10)
                if sbs > 3072:
                    sbs = 3072
                lamp.shadow_buffer_size = sbs
        for screen in bpy.data.screens:
            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    if len(bpy.context.screen.areas) > 2:
                        sd = area.spaces[0]
                    else:
                        sd = bpy.context.space_data 
                    if sd.lock_camera is False: 
                        sd.viewport_shade = 'SOLID'    
                        sd.fx_settings.use_ssao = False
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
            if scene.zbAutoConvertLamps is False:
                try:
                    sceneLight = bpy.data.objects['Scene Light']
                    sceneLight.hide_render = True
                except:
                    pass
class cl17(bpy.types.Panel):
    bl_category =i_0[55]
    bl_label =i_0[56]
    bl_space_type =i_0[57]
    bl_region_type =i_0[58]
    @classmethod
    def poll(cls, context):
        m = bpy.context.mode
        return 'PAINT' not in m and 'SCULPT' not in m \
        and 'PARTICLE' not in m
    def draw(self, context):
        wm = bpy.context.window_manager
        layout = self.layout
        scene = context.scene
        screen = context.screen
        mode = bpy.context.mode
        sel = bpy.context.selected_objects
        if fu8():
            ob = 0        
            try:
                ob = bpy.context.active_object
                rbo = ob.rigid_body
            except:
                pass
            row = layout.row(align=True)
            row.scale_y = 1.4
            row.scale_x = 1.25
            row.operator('wm.call_menu', text = '', 
            icon='COLLAPSEMENU').name = 'menu.sf_builder_options_menu'
            row.menu('menu.sf_set_origin', text='Set Origin')
            row.operator("view3d.snap_selected_to_cursor", icon = 'CURSOR', text="")
            row = layout.row()
            box = layout.box()
            if mode == 'POSE':
                if ob.pose_library:
                    try:
                        sub = box.column(align=True)
                        arm = ob.data
                        subRow = sub.row(True)
                        subRow.scale_y = 1.3
                        subRow.prop(arm, "use_auto_ik",icon='POSE_DATA',text='')
                        subRow.prop_enum(wm,'sfPoseButtons', 'ADD', text='Save Pose')
                        sub = box.row(align=True)
                        sub.scale_y = 0.9
                        sub.prop_enum(wm,'sfPoseButtons', 'RESET', text='Reset')
                        sub.prop_enum(wm,'sfPoseButtons', 'FLIP', text='Flip Pose')
                        poselib = ob.pose_library
                        sub = box.column(align=True)
                        sub.template_list("UI_UL_list", "pose_markers", poselib, "pose_markers",
                        poselib.pose_markers, "active_index", rows=3)
                        sub = box.column()
                        sub.scale_y = 1.3
                        sub.prop_enum(wm,'sfPoseButtons', 'USE')
                        sub = box.row(align=True)
                        sub.scale_y = 0.9
                        sub.prop_enum(wm,'sfPoseButtons', 'REPLACE')
                        sub.prop_enum(wm,'sfPoseButtons', 'DELETE')
                    except:
                        pass
                else:
                    sub = box.row(align=True)
                    sub.scale_y = 1.3
                    sub.prop_enum(wm,'sfPoseButtons', 'ADDLIBRARY', icon ='POSE_DATA')
            else:
                sub = box.row(align=True)
                if wm.sfChooseClone == True:
                    sub.prop(wm,"sfChooseClone", icon='MOD_MIRROR')
                else:
                    sub.prop(wm,"sfChooseClone", icon='MOD_MIRROR', text="Mirror")
                subrow = sub.row(align=True)
                subrow.scale_x = 0.45
                subrow.operator("object.sf_mirror_clone", 'X').axis = 'X'
                subrow.operator("object.sf_mirror_clone", 'Y').axis = 'Y'
                subrow.operator("object.sf_mirror_clone", 'Z').axis = 'Z'
                sub = box.row(align=True)
            box = layout.row(align=True)
            if mode == 'OBJECT':
                if ob:
                    if ob.parent: 
                        sub.scale_x = 1                        
                        sub.operator("object.sf_parent", text="", icon='X').type = 'none'
                        sub = sub.row(True)
                        sub.scale_x = .3
                        sub.operator("object.sf_parent", text="Parent").type = 'add'
                    else:
                        sub.scale_x = 0.3
                        sub.operator("object.sf_parent", text="Parent")
                else:
                    sub.scale_x = 0.3
                    sub.operator("object.sf_parent", text="Parent")
                sub.separator()
                sub.separator()
                if ob:
                    if ob.type == 'MESH':
                        sub = sub.row(align=True)
                        sub.scale_x = 0.3
                        sub.operator("object.sf_join_objects", text="Join")
                        sub = sub.row(align=True)
                        sub.scale_x = 6
                        sub.operator("object.sf_sep_objects", text="Separate")
                    if ob.type == 'CURVE':
                        sub = sub.row(align=True)
                        sub.scale_x = 0.75
                        follow = False
                        for obj in sel:
                            if obj.type != 'CURVE':
                                follow = True
                                break
                        if follow:
                            sub.operator("object.sf_follow_path", 
                            text="   Follow").func = 'follow_path'
                        else:
                            if len(sel) < 2:
                                if hasattr(ob.data.animation_data, 'action'):
                                    sub.operator("object.sf_follow_path", 
                                    text=" Reverse").func = 'reverse_curve'
                                else:
                                    sub.operator("object.sf_join_objects", text="     Join")
                            else:
                                sub.operator("object.sf_join_objects", text="     Join")
            if mode.startswith('EDIT'):
                if ob.type == 'MESH':
                    sub.operator("object.sf_object_from_selection", text="Duplicate")
                    sub.operator("object.sf_sep_objects", text="Separate")
                if ob.type == 'ARMATURE':
                    sub.operator("armature.parent_set", text="Parent")
                    sub.operator("armature.parent_clear", text="UnParent")
            if mode == 'OBJECT':
                bevel = 0
                if ob:
                    bevel = len([mod for mod in ob.modifiers if mod.type == 'BEVEL'])
                col = layout.column(align=True)
                box = col.box()
                sub = box.column(align=True)
                if bevel:
                    sub = sub.row(align=True)
                    sub.operator('object.sf_custom_bevel', text ='Apply', icon='MOD_BEVEL').remove = False
                    sub.operator('object.sf_custom_bevel', text ='', icon='X').remove = True
                else:
                    sub.operator('object.sf_custom_bevel', text = "Bevel",icon='MOD_BEVEL')
                sub = box.column(align=True)
                sub = sub.row(align=True)
                mType = False
                if ob:
                    if ob.type == 'MESH':
                        mType = True
                        if ob.data.use_auto_smooth:
                            sub.operator("object.sf_custom_smooth", text='',
                            icon='LAYER_ACTIVE')
                            sub.prop(ob.data, 'auto_smooth_angle',
                            text = '',slider=True)      
                        else:
                            sub.operator("object.sf_custom_smooth", text='', 
                            icon='LAYER_USED')
                            sub.operator("object.shade_smooth", text='Smooth')
                            sub.operator("object.shade_flat", text='Flat')  
                if mType is False:
                    sub.operator("object.sf_custom_smooth", text='', 
                    icon='LAYER_USED')
                    sub.operator("object.shade_smooth", text='Smooth')
                    sub.operator("object.shade_flat", text='Flat')             
                row = layout.row()
            if mode.startswith('EDIT'):
                tool = bpy.context.tool_settings
                vert_sel,edge_sel,face_sel = tool.mesh_select_mode
                col = layout.column(align=True)
                box = col.box()
                sub = box.column(align=True)
                sub = sub.row(align=True)
                if vert_sel:
                    sub.operator('mesh.bevel', text ='Bevel', icon='MOD_BEVEL').vertex_only = True
                else:
                    sub.operator('mesh.bevel', text ='Bevel', icon='MOD_BEVEL')
                sub = box.column(align=True)
                sub = sub.row(align=True)
                sub.operator("mesh.faces_shade_smooth", text='Smooth')
                sub.operator("mesh.faces_shade_flat", text='Flat')
                row = layout.row()
            if mode == 'OBJECT':                
                sub = layout.column()
                sub = sub.row(align=True)
                sub.scale_y = 1.4
                sub.scale_x = 1.25
                ts = bpy.context.scene.tool_settings
                sub.prop(ts,'use_snap', text='')
                sub.operator('object.sf_align_to_grid', text='Align To Grid')                    
                sub = layout.column()
                col = layout.column()
                sub = col.column(align=True)
                sub.prop(wm,'sfShapeTools', icon='COLLAPSEMENU',
                text='Shape Tools')
                if wm.sfShapeTools:
                    sub = sub.column(align=True)
                    displayMeta = False                    
                    if ob:
                        if ob.type == 'META':
                            displayMeta = True
                        else:
                            displayMeta = False
                    if scene.sfShapeToolsMeta:
                        displayMeta = True
                    if displayMeta:
                        sub.scale_y = 1.3                   
                        sub.separator()
                        sub.operator('object.sf_shape_tools_meta', icon='ZOOMOUT',
                        text='Cut Out').func = 'cut_out'
                        sub.operator('object.sf_shape_tools_meta', icon='ZOOMIN',
                        text='Combine').func = 'combine'
                        sub.operator('object.sf_shape_tools_meta', icon='X',
                        text='Invert').func = 'invert'                            
                        sub.separator()
                        sub = layout.column(True)   
                        sub = sub.row(True)
                        sub.prop(scene, 'sfShapeToolsMeta',text='', icon='GROUP')
                        sub.label('Meta')
                        sub = sub.row(True)
                        sub.scale_y = 1
                        sub.operator('object.sf_shape_tools_meta',
                        text='Apply').func = 'apply' 
                        sub = layout.column(True)
                        sub = layout.column(True)
                        sub = sub.row(True)
                        sub.scale_x = 2.5
                        sub.scale_y = 0.55
                        sub.operator('object.sf_shape_tools_meta', text='', 
                        icon = 'META_CUBE').func = 'cube'
                        sub.operator('object.sf_shape_tools_meta', text='', 
                        icon = 'META_BALL').func = 'ellipsoid'
                        sub.operator('object.sf_shape_tools_meta', text='', 
                        icon = 'META_PLANE').func = 'plane'
                        sub.operator('object.sf_shape_tools_meta', text='', 
                        icon = 'META_CAPSULE').func = 'capsule'
                        sub = layout.column(True)
                        sub.separator()
                        sub.prop(scene, 'sfShapeToolsRes', text = 'Resolution',
                        slider = True)
                        try:                                
                            sub.prop(ob.data.elements[0], 'stiffness',
                            slider = True)
                        except:
                            pass
                    else: 
                        sub.scale_y = 1.3                        
                        sub.separator()
                        sub.operator('object.sf_shape_tools', icon='ZOOMOUT',
                        text='Cut Out').func = 'cut_out'
                        sub.operator('object.sf_shape_tools', icon='ZOOMIN',
                        text='Combine').func = 'combine'
                        sub.operator('object.sf_shape_tools', icon='X',
                        text='Intersect').func = 'intersect'
                        sub.separator()  
                        sub = layout.column(True)  
                        sub = sub.row(True)
                        sub.prop(scene, 'sfShapeToolsMeta',text='', icon='GROUP')
                        sub.label('Regular')
                        sub = sub.row(True)
                        sub.scale_y = 1
                        sub.operator('object.sf_shape_tools',
                        text='Apply').func = 'apply_all'
                        sub = layout.column(True)
                        sub = layout.column(True)
                        sub = sub.row(True)
                        sub.scale_y = 0.55
                        sub = sub.row(True)
                        sub.scale_y = .55
                        if scene.sfShapeToolsSolid:
                            solidIcon = 'INLINK'
                        else:
                            solidIcon = 'RADIOBUT_OFF'
                        sub.prop(scene,'sfShapeToolsSolid',text='',
                        icon=solidIcon,emboss=False)
                        sub.scale_x = 1.5
                        cursLoc = scene.cursor_location.xyz
                        sub.operator('mesh.primitive_cube_add',
                        text='',icon='MESH_CUBE').location = cursLoc
                        sub.operator('mesh.primitive_plane_add',                        
                        text='',icon='MESH_PLANE').location = cursLoc
                        if scene.sfShapeToolsHD:
                            sphere = sub.operator('mesh.primitive_uv_sphere_add',                        
                            text='',icon='SOLID')
                            sphere.location = cursLoc
                            sphere.segments = 96
                            sphere.ring_count = 46
                            cylinder = sub.operator('mesh.primitive_cylinder_add',                        
                            text='',icon='MESH_CYLINDER')
                            cylinder.location = cursLoc       
                            cylinder.vertices = 96
                            torus = sub.operator('mesh.primitive_torus_add',                        
                            text='',icon='MESH_TORUS')
                            torus.location = cursLoc 
                            torus.major_segments = 96
                            torus.minor_segments = 32
                            cone = sub.operator('mesh.primitive_cone_add',                        
                            text='',icon='MESH_CONE')
                            cone.location = cursLoc   
                            cone.vertices = 96
                        else:
                            sub.operator('mesh.primitive_uv_sphere_add',                        
                            text='',icon='SOLID').location = cursLoc
                            sub.operator('mesh.primitive_cylinder_add',                        
                            text='',icon='MESH_CYLINDER').location = cursLoc       
                            sub.operator('mesh.primitive_torus_add',                        
                            text='',icon='MESH_TORUS').location = cursLoc 
                            sub.operator('mesh.primitive_cone_add',                        
                            text='',icon='MESH_CONE').location = cursLoc                        
                        sub = layout.column(True)
                        try:
                            if ob.modifiers:            
                                solid = False    
                                if ob.draw_type == 'BOUNDS':                
                                    for mod in ob.modifiers:
                                        if mod.type == 'SOLIDIFY':
                                            sub = layout.column(True)
                                            sub.separator()
                                            sub.prop(mod,'thickness')
                                            solid = True
                                        if not solid:
                                            sub = layout.column(True)
                                            sub.separator()
                                        if mod.type == 'BEVEL':                                        
                                            sub.prop(mod,'segments',text='Segments')
                                            sub.prop(mod,'width',text='Bevel Width')
                        except:
                            pass
                    sub = layout.column()
                    sub = layout.column()
                    sub = layout.column(True)                  
                sub.prop(wm,'sfDisplayDimensions', text='Dimensions', icon='COLLAPSEMENU')
                if wm.sfDisplayDimensions:
                    sub.separator()
                    ts = scene.tool_settings
                    ob = bpy.context.active_object
                    if ob:
                        data = ob.data                      
                    if ob:                        
                        locX = 'BLANK1'
                        locY = 'BLANK1'
                        locZ = 'BLANK1'
                        rotX = 'BLANK1'
                        rotY = 'BLANK1'
                        rotZ = 'BLANK1'
                        scaleX = 'BLANK1'
                        scaleY = 'BLANK1'
                        scaleZ = 'BLANK1'
                        if ob.lock_location[0]:
                            locX = 'LOCKED'
                        if ob.lock_location[1]:
                            locY = 'LOCKED'
                        if ob.lock_location[2]:
                            locZ = 'LOCKED'
                        if ob.lock_rotation[0]:
                            rotX = 'LOCKED'
                        if ob.lock_rotation[1]:
                            rotY = 'LOCKED'
                        if ob.lock_rotation[2]:
                            rotZ = 'LOCKED'
                        if ob.lock_scale[0]:
                            scaleX = 'LOCKED'
                        if ob.lock_scale[1]:
                            scaleY = 'LOCKED'
                        if ob.lock_scale[2]:
                            scaleZ = 'LOCKED'
                        box = sub.box()
                        sub = box.row(True)
                        sub.scale_y = 1.4
                        sub.operator('object.sf_object_transform', 
                        text = 'Apply All').tool = 'APPLY'
                        sub.operator('object.sf_object_transform', 
                        text = 'Reset All').tool = 'RESET' 
                        sub = box.row(True)  
                        sub = box.row(True) 
                        sub.label('Location')
                        sub.operator('object.location_clear', icon = 'FILE_REFRESH',
                        text = '')
                        sub = sub.row(True)
                        sub.scale_x = 0.5
                        props = sub.operator('object.transform_apply', 
                        text = 'Apply')
                        props.location = True
                        props.rotation = False
                        props.scale = False  
                        sub = box.column(True)
                        row = sub.row(True)
                        row.scale_y = 0.8
                        row.operator('object.sf_object_transform', 
                        icon = locX, text = 'X').tool = 'LOCK_X_LOC'
                        row.operator('object.sf_object_transform', 
                        icon = locY, text = 'Y').tool = 'LOCK_Y_LOC'
                        row.operator('object.sf_object_transform',  
                        icon = locZ, text = 'Z').tool = 'LOCK_Z_LOC'
                        row = sub.row(True)
                        row.prop(ob, 'location', text='')
                        sub = box.row(True)
                        sub = box.row(True)
                        sub.label('Rotation')
                        sub.operator('object.rotation_clear', icon = 'FILE_REFRESH',
                        text = '')
                        sub = sub.row(True)
                        sub.scale_x = 0.5
                        props = sub.operator('object.transform_apply', 
                        text = 'Apply')
                        props.location = False 
                        props.rotation = True
                        props.scale = False  
                        sub = box.column(True)
                        row = sub.row(True)
                        row.scale_y = 0.8
                        row.operator('object.sf_object_transform', 
                        icon = rotX, text = 'X').tool = 'LOCK_X_ROT'
                        row.operator('object.sf_object_transform', 
                        icon = rotY, text = 'Y').tool = 'LOCK_Y_ROT'
                        row.operator('object.sf_object_transform',  
                        icon = rotZ, text = 'Z').tool = 'LOCK_Z_ROT'
                        row = sub.row(True)
                        row.prop(ob, 'rotation_euler', text='')
                        sub = box.row(True)
                        sub = box.row(True)
                        sub.label('Dimensions')
                        sub.operator('object.scale_clear', icon = 'FILE_REFRESH',
                        text = '')
                        sub = sub.row(True)
                        sub.scale_x = 0.5
                        props = sub.operator('object.transform_apply', 
                        text = 'Apply')                        
                        props.location = False 
                        props.rotation = False
                        props.scale = True  
                        sub = box.column(True)
                        row = sub.row(True)
                        subCol = row.column(True)
                        if ob.type == 'META':
                            subCol.prop(ob, 'scale', text = '')
                        else:
                            subCol.prop(ob, 'dimensions', text = '')
                    sub = box.row(True)
                    col = layout.column(True)
                    col2 = col.column(True)
                    col2.scale_y = .8
                    unit = scene.unit_settings    
                    col2.prop(unit, "system", text = 'Units')
                    if scene.unit_settings.system != 'NONE':
                        if scene.unit_settings.system == 'METRIC':
                            type = 'Meters'
                        else:
                            type = 'Feet'
                        view = context.space_data
                        col2 = col2.column(True)
                        col2.scale_y = 1
                        col2.separator()
                        col2.prop(view, "grid_lines", text="Grid Lines")
                        col2.prop(view, "grid_scale", text="Grid "+type)
                    col.separator()
                    col.separator()
                    sub = layout.column()
                    sub = layout.column()
                sub.prop(wm, 'sfPhysics', text='Physics Control', icon='COLLAPSEMENU')
                if wm.sfPhysics:
                    col = layout.column(align=True)
                    col.label(text="Add Physics")
                    sub = col.row(align=True)
                    sub.scale_y = 1.3
                    sub.operator("object.sf_physics", text="Add Active").func = 'ADD_RB_ACTIVE'
                    sub.operator("object.sf_physics", text="Add Passive").func = 'ADD_RB_PASSIVE'
                    sub = col.row(align=True)
                    sub.operator("rigidbody.objects_remove", text="Remove")
                    col.separator()
                    col.operator("object.sf_physics", text="Connect Objects").func = 'CONNECT'
                    if ob:
                        if ob.rigid_body_constraint:
                            rbc = ob.rigid_body_constraint
                            layout.prop(rbc, "type")
                            sub = layout.column()
                            sub.prop(rbc, 'disable_collisions')
                            sub = layout.column()
                            sub.scale_y = 0.6
                            sub.label('See "Rigid Body Constraint"')
                            sub.label('in physics tab of properties')
                            sub.label('panel for complete settings.')
                            col = layout.column()
                        col = layout.column(align=True)
                        col.label(text="Collision Settings")
                        row = col.row(align=True)
                        row.operator("rigidbody.shape_change", text="Shape")
                        row.operator("rigidbody.mass_calculate", text="Mass")
                        if rbo:
                            if rbo.collision_shape in {'MESH', 'CONVEX_HULL'}:
                                row.prop(rbo, "mesh_source", text="")
                            row = col.row(align=True)
                            if rbo.use_start_deactivated:
                                row.operator('object.sf_physics', text = "Start Activated").func = 'ACTIVATED'
                            else:
                                row.operator('object.sf_physics', text = "Start Deactivated").func = 'DEACTIVATED'
                        else:
                            row.operator('rigidbody.object_settings_copy', text='Deform')
                            row = col.row(align=True)
                            row.operator('rigidbody.object_settings_copy', text='Start Deactivated')
                        col.operator("rigidbody.object_settings_copy", text="Distribute Settings")
                        col.separator()
                        col.label('Apply Physics')
                        col.operator("object.visual_transform_apply", text="Apply Transformation")
                        col.operator("rigidbody.bake_to_keyframes", text="Bake To Keyframes")
                        row = col.row(align=True)
                        row.operator("ptcache.bake_all", text = "Bake all")
                        row.operator("object.sf_physics", text ="Free all").func = 'FREE_ALL'
                        row = layout.row(align=True)
                        row.scale_y = 1.3
                        if rbo:
                            row.prop(rbo, "kinematic", text="Animated", icon="PHYSICS")
                        else:
                            row.operator('rigidbody.object_settings_copy', text='Animated', icon="PHYSICS")
                        row.scale_x = 1.3
                        row.operator("screen.frame_jump", text="", icon='FRAME_PREV').end = False
                        if not screen.is_animation_playing:
                            if scene.sync_mode == 'AUDIO_SYNC' and context.user_preferences.system.audio_device == 'JACK':
                                row.operator("screen.animation_play", text="", icon='PLAY')
                            else:
                                row.operator("screen.animation_play", text="", icon='PLAY')
                        else:
                            row.operator("screen.animation_play", text="", icon='PAUSE')
            if mode.startswith('EDIT') and ob.type == 'MESH':
                tool = bpy.context.tool_settings
                vert_sel,edge_sel,face_sel = tool.mesh_select_mode
                col = layout.column(align=True)
                if 'Draw' in ob.name:
                    if 'DrawMesh' in ob.name:
                        sub = col.column()
                        sub.scale_y = 1.8
                        sub.operator('object.sf_draw_mesh', icon = 'FILE_TICK',
                        text='Finish Draw Mesh').func = 'finish'
                        col = layout.column()
                        sub = col.row(align=True)
                        sub.operator('gpencil.layer_remove',
                        icon = 'X', text='Strokes')
                        sub.operator('object.sf_draw_topo',
                        icon = 'MATPLANE', text='Normals').func = 'fix_normals'  
                        sub = col.column(True)
                        sub.scale_y = 0.8
                        sub.label('V+MOUSE: draw strokes')
                        sub.label('SHIFT-V: convert to mesh')
                        sub.label('')
                    if 'DrawSkin' in ob.name:
                        sub = col.column()
                        sub.scale_y = 1.8
                        sub.operator('object.sf_draw_skin', icon = 'FILE_TICK',
                        text='Finish Draw Skin').func = 'finish'
                        sub = col.column(True)
                        sub.scale_y = 0.8
                        sub.label('E: extrude new skin')
                        sub.label('S: scale skin selection')
                        sub.label('')
                    if 'DrawTopo' in ob.name:
                        sub = col.column()
                        sub.scale_y = 1.8
                        sub.operator('object.sf_draw_topo', icon = 'FILE_TICK',
                        text='Finish Draw Topo').func = 'finish'
                        col = layout.column()
                        sub = col.row(align=True)   
                        sub.operator('gpencil.layer_remove',
                        icon = 'X', text='')
                        sub.operator('object.sf_draw_topo',
                        icon = 'MATPLANE', text='').func = 'fix_normals'   
                        sub.prop(scene, 'sfDrawTopoSnap', icon = 'SNAP_VERTEX',
                        text ='')            
                        sub.operator('object.sf_draw_topo',
                        icon = 'ARMATURE_DATA', text='').func = 'conform'                            
                        sub.prop(ob.modifiers[0], 'levels', slider = True, 
                        text = 'Detail')
                        sub = col.column(True)
                        sub.scale_y = 0.8
                        sub.label('V+MOUSE: draw strokes')
                        sub.label('SHIFT-V: convert to mesh')
                        sub.label('')
                    col.separator()
                    col.separator()
                sub = col.row(align = True)
                sub.scale_y = 0.9
                sub.label('Mesh',icon='RESTRICT_VIEW_OFF')
                sub.operator('mesh.hide',text='Hide')
                sub.operator('mesh.reveal',text='Show')
                col.separator()
                if ob.type == 'MESH': 
                    displayLAA = False
                    if scene.unit_settings.system != 'NONE':
                        displayLAA = True
                    else:
                        if ob.data.show_extra_edge_length:
                            displayLAA = True
                        if ob.data.show_extra_face_angle:
                            displayLAA = True
                        if ob.data.show_extra_face_area:
                            displayLAA = True
                    if displayLAA:                                        
                        sub = col.row(True)
                        sub = col.row(True)
                        sub.scale_y = .8
                        sub.alignment = 'CENTER'
                        sub.prop(ob.data,'show_extra_edge_length', text='Length',toggle=True)
                        sub.prop(ob.data,'show_extra_face_angle', text='Angle',toggle=True)   
                        sub.prop(ob.data,'show_extra_face_area', text='Area',toggle=True)  
                        col.separator()
                        col.separator()
                        col.separator()
                sub = col.row(align = True)
                sub.prop_enum(wm,'sfMeshToolSelect', 'BASIC', text='Basic')
                sub.prop_enum(wm,'sfMeshToolSelect', 'EXTENDED', text='Extended')
                col.separator()
                col = layout.column(align=True)
                col.scale_y = 1.3
                if wm.sfMeshToolSelect == 'BASIC':
                    if wm.sfMeshTools != 'void':
                        wm.sfMeshTools = 'void' 
                    col.operator('transform.translate', text='Move (G)', icon='EDIT')
                    col.operator('transform.rotate', text='Rotate (R)', icon='EDIT')
                    col.operator('transform.resize', text='Scale (S)', icon='EDIT')
                    col.separator()
                    col.operator('mesh.extrude_region_move', text='Extrude (E)', icon='EDIT')
                    col.operator('view3d.edit_mesh_extrude_individual_move', text='Individual (Ctrl-E)', icon='EDIT')
                    col.separator()
                    col.operator('mesh.subdivide', text='Subdivide (W)', icon='EDIT')
                    col.operator('mesh.loopcut_slide', text='Loopcut (Shift-W)', icon='EDIT')
                    col.operator('mesh.inset', text='Inset (Shift-E)', icon='EDIT')
                    col.separator()
                    col.operator('mesh.sf_smart_fill', text='Fill (F)', icon='EDIT')
                    col.operator('mesh.bridge_edge_loops', text='Bridge Edges (Shift-F)', icon='EDIT')
                    col.separator()
                    col.prop(wm, 'sfDisplayTips',text='Show Helpful Tips', toggle=True, icon='QUESTION')
                    if wm.sfDisplayTips:
                        col = layout.column(align=True)
                        col.scale_y = 0.7
                        col.label('° Hold Middle Mouse Button ')
                        col.label('   down when Moving,')
                        col.label('   Rotating, or Scaling')
                        col.label('   to constrain the direction')
                        col.label('° Double tap (Space) to call')
                        col.label('   an options menu while or')
                        col.label('   after you perform an action')
                        col.label('° Press (Shift-R) to repeat')
                        col.label('   your last action')
                        col.label('° Hover mouse over buttons')
                        col.label('   to learn more about them')
                        col.label('° The header and footer of')
                        col.label('   the 3D View display')
                        col.label('   helpful information')
                        col.label('° A transparent + tab')
                        col.label('   means Blender is hiding')
                        col.label('   a menu you can click')
                        col.label('° For a complete list of')
                        col.label('   hotkeys go to File >')
                        col.label('   Sensei Format and select')
                        col.label('   "Hotkey Reference"')
                        col.separator()
                        col.separator()
                        col.label('° FACE SELECT: (Space)')
                        col.label('° EDGE: (Shift-Scroll Up)')
                        col.label('° VERT: (Shift-Scroll Down)')
                        col.separator()
                        col.separator()
                        col.label('° SELECT ALL: A')
                        col.label('° DE/SELECT: Double Click')
                        col.label('° HOLD SHIFT: Add Selection')
                        col.label('° LOOP SELECT: Alt-Click')
                        col.separator()
                        col.separator()
                        col.label('° CIRCLE SELECT: C')
                        col.label('° LASSO: Ctrl-RClick')
                        col.label('° BORDER SELECT: B')
                        col.separator()
                        col.separator()
                        col.label('° TOGGLE MODE: Tab')
                        col.label('° VIEW ALONE: Tab x2')
                        col.label('° VIEW SELECTED: Alt-MMB')
                        col.label('° RESET VIEW: Shift-C')
                        col.separator()
                        col.separator()
                        col.label('° WIREFRAME VIEW: Z')
                        col.label('° MATERIAL VIEW: Alt-Z')
                        col.label('° RENDERED VIEW: Shift-Z')
                        col.separator()
                        col.separator()
                        col.label('° GRID SNAP: Hold Ctrl')
                        col.label('° ADD MENU: Shift-A')
                        col.label('° UNDO: Ctrl-Z')
                        col.label('° DELETE: X')
                if wm.sfMeshToolSelect == 'EXTENDED':
                    col.operator('mesh.knife_tool', text='Knife Tool', icon='EDIT')
                    col.operator('transform.bend', text='Bend Mesh', icon='EDIT')
                    col.operator('mesh.bisect', text='Bisect Mesh', icon='EDIT')
                    col.separator()
                    col.operator('mesh.merge', text = 'Collapse Selected', icon='EDIT').type = 'CENTER'
                    if vert_sel:
                        col.operator('transform.vert_slide', text = 'Slide Selected', icon='EDIT')
                    else:
                        col.operator('transform.edge_slide', text = 'Slide Selected', icon='EDIT')
                    col.operator('transform.shrink_fatten', icon='EDIT').use_even_offset = True
                    col = layout.column(align=True)
                    col.scale_y = 1
                    sub = col.row(align=True)
                    sub.prop_enum(wm, 'sfMeshTools', 'vert', text=' ')
                    sub.prop_enum(wm, 'sfMeshTools', 'edge', text=' ')
                    sub.prop_enum(wm, 'sfMeshTools', 'face', text=' ')
                    sub.prop_enum(wm, 'sfMeshTools', 'more', text=' ')
                    if wm.sfMeshTools == 'vert':
                        col.label('Vertex Tools')
                        col.operator('mesh.bevel', text='Bevel Vertices').vertex_only=True
                        col.operator('mesh.dissolve_verts', text='Dissolve Vertices')
                        col.operator('mesh.vertices_smooth')
                        col.operator('mesh.convex_hull')
                        col.separator()
                        col.separator()
                        col.operator('mesh.merge', text='Merge')
                        col.operator('mesh.split', text = 'Split')
                        col.operator('mesh.rip_move')
                        col.operator('mesh.rip_move_fill')
                    if wm.sfMeshTools == 'edge':
                        col.label('Edge Tools')
                        col.operator('mesh.bevel', text='Bevel Edges')
                        col.operator('mesh.dissolve_edges', text='Dissolve Edges') 
                        col.operator('transform.edge_bevelweight', text='Bevel Weight')
                        col.operator('transform.edge_crease')
                        col.separator()
                        col.separator()
                        row = col.row(align=True)
                        row.scale_y = 1.3
                        row.operator("mesh.mark_seam", text='Mark Seams').clear = False
                        row.operator("mesh.mark_seam", text="Clear Seams").clear = True
                        col.operator('mesh.mark_freestyle_edge', text='Mark Freestyle').clear=False
                        col.operator('mesh.mark_freestyle_edge', text='Clear Freestyle').clear=True
                        col.separator()
                        row = col.row(align=True)
                        row.scale_y = 1.3
                        row.operator("object.sf_quick_uv_edit")
                        col.menu("VIEW3D_MT_uv_map", text="Unwrap")
                    if wm.sfMeshTools == 'face':
                        col.label('Face Tools')
                        col.operator('mesh.bevel', text='Bevel Faces')
                        col.operator('mesh.dissolve_faces', text='Dissolve Faces')
                        col.operator('mesh.solidify', text='Solidify Faces')
                        col.operator('mesh.poke', text='Poke Faces')
                        col.separator()
                        col.separator()
                        col.operator('mesh.edge_face_add')
                        col.operator('mesh.fill_grid')
                        col.operator('mesh.fill')
                        col.separator()
                        col.operator('mesh.wireframe', text='Make Wireframe')
                        col.operator('mesh.intersect', text='Intersect Meshes')
                    if wm.sfMeshTools == 'more':
                        col.label('Clean Up')
                        col.operator('mesh.unsubdivide', text='UnSubdivide')  
                        operator_props = col.operator('mesh.select_face_by_sides', text='Select Non-quad')
                        operator_props.type = 'NOTEQUAL' 
                        operator_props.extend = False
                        col.operator('mesh.quads_convert_to_tris', text='3 Sided Faces')
                        col.operator('mesh.tris_convert_to_quads', text='4 Sided Faces')
                        col.separator()
                        col.separator()
                        dissolve = col.operator('mesh.dissolve_limited', text='Dissolve Limited')                           
                        dissolve.angle_limit = 0
                        dissolve.use_dissolve_boundaries = True
                        sub = col.row(True)
                        sub.alignment = 'CENTER'
                        sub.operator('mesh.dissolve_verts',text='Vertices')
                        sub.operator('mesh.dissolve_edges',text='Edges')
                        sub.operator('mesh.dissolve_faces',text='Faces')
                        col.separator()
                        col.separator()
                        col.operator('mesh.normals_make_consistent', text='Fix Normals')
                        col.operator('mesh.flip_normals', text='Flip Normals')
                        col.separator()
                        col.separator()
                        col.operator('mesh.beautify_fill', text='Beautify Faces')
                        sub = col.row(True)
                        sub.alignment = 'CENTER'
                        sub.operator('mesh.face_make_planar',text='Smooth')
                        sub.operator('mesh.vert_connect_nonplanar', 
                        text='Split').angle_limit = 0                        
                        sub.operator('mesh.vert_connect_concave', 
                        text='Concave')
                        col.separator()
                        col.separator()
                        col.operator('mesh.fill_holes', text='Fill Holes')
                        col.operator('mesh.delete_edgeloop', text='Merge Loops')
                        col.operator('mesh.remove_doubles', text='Merge Doubles')
                        col.operator('mesh.delete_loose', text='Delete Loose')
            else:
                if 'EDIT' in bpy.context.mode:
                    mType = ['SURFACE','FONT','META','CURVE']
                    for m in mType:
                        if m in ob.type:
                            col = layout.column()
                            col.scale_y = 1.4
                            col.operator('object.sf_convert_to_mesh', icon = 'EDIT')
                            break
        else:
            msg1 = 'The version of the'
            msg2 = 'addon you are using'
            msg3 = 'only works with'
            msg4 = 'Sensei Format'
            layout.scale_y = 0.7
            layout.label(msg1)
            layout.label(msg2)
            layout.label(msg3)
            layout.label(msg4)           
class cl18(bpy.types.Operator):
    bl_idname =i_0[59]
    bl_label =i_0[60]
    bl_description =i_0[61]
    message = bpy.props.StringProperty()
    def execute(self, context):
        message = self.message
        if len(message) > 0:
            self.report({'INFO'}, message)
        else:
            self.report({'INFO'}, "This option is not available in this mode")
        pass
        return {'FINISHED'}
class cl19(bpy.types.Operator):
    bl_idname =i_0[62]
    bl_label =i_0[63]
    def execute(self, context):
        try:
            ob = bpy.context.active_object
            mesh = bpy.data.meshes[ob.name]
            if mesh.uv_textures:
                pass
            else:
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.uv.unwrap()
        except:
            pass
        bpy.context.area.type = 'IMAGE_EDITOR'
        try:
            bpy.ops.uv.select_all(action='SELECT')
            bpy.ops.image.view_selected()
        except:
            pass
        return {'FINISHED'}
class cl17Properties(bpy.types.PropertyGroup):
    scene = bpy.types.Scene
    wm = bpy.types.WindowManager
    text1 = 'Some modifiers and effects can become distorted on objects which'
    text2 = ' have been scaled in object mode without having its transform values'
    text3 = ' applied. Leave this option checkmarked to automatically apply'
    text4 = " an object's transform values after scaling."
    text5 = text1 + text2 + text3 + text4
    scene.sfAutoApplyTransform = bpy.props.BoolProperty(
    name = 'Auto Apply Transform',
    default = True,
    description = text5
    )
    text1 = 'Use hi-def shadows and shading in the 3D Viewport to help with '
    text2 = 'modeling. This mode requires the Blender Render engine to be active '
    text3 = 'so if this option is activated while using Cycles, the render mode '
    text4 = 'will be temporarily switched to Blender Render. When the option is '
    text5 = 'deactivated you will be returned to Cycles.'
    text6 = text1 + text2 + text3 + text4 + text5 
    scene.sfHDShading = bpy.props.BoolProperty(
    update = sfHDShading,
    description = text6
    )
    scene.sfLastRE = bpy.props.StringProperty(
    description = 'The last render engine to be used'
    )
    text1 = "Right clicking will snap the 3D cursor to an object's "
    text2 = "origin point if in object mode. In edit mode the cursor will snap "
    text3 = "to your object's mesh. If in Front, Back, Left, Right etc... "
    text4 = "views, the 3D cursor will only snap to the grid. You can disable "
    text5 = 'this feature by checkmarking this option or hold "Alt" while '
    text6 = 'right clicking to temporarily disable cursor snapping. "Shift" + right '
    text7 = 'clicking will snap the cursor to a point on the mesh (or other object '
    text8 = 'type) while in object mode and "Shift" + double right clicking will '
    text9 = "set the selected object's origin point to the location of the cursor "
    text10 = 'while in object mode.'
    text11 = text1 + text2 + text3 + text4 + text5 + text6 + text7 +text8 + text9 + text10
    scene.sfDisableCursorSnap = bpy.props.BoolProperty(default = False,
    description = text11)
    text1 = 'Automatically increase resolution of shapes created with the Shape Tools '
    text2 = 'basic shapes bar.'
    scene.sfShapeToolsHD = bpy.props.BoolProperty(
    name = 'Hi-Def Shape Tools',
    default = True,
    description = text1+text2
    )
    scene.sfShapeToolsSolid = bpy.props.BoolProperty(
    name = 'Solidify Shapes',
    description = 'Give thickness to new objects created from this row (also applies or removes thickness from selected object).',
    default = False,
    update = sfShapeToolsSolid
    )
    wm.sfShapeTools = bpy.props.BoolProperty(
    description='Cut out, combine and intersect mesh objects')
    scene.sfShapeToolsMeta = bpy.props.BoolProperty(    
    default = False,
    update = fu5,
    description = 'Use meta shapes to build things rather than your regular objects')
    scene.sfShapeToolsRes = bpy.props.FloatProperty(
    description = 'Adjust the resolution of your meta shape objects',
    update = sfShapeToolsRes,
    default = 0.06,
    soft_min = 0.02,
    soft_max = 1.5)
    wm.sfDisplayDimensions = bpy.props.BoolProperty(
    description = 'Display object dimension controls and information')        
    wm.sfDisplayTips = bpy.props.BoolProperty(
    name = "Display Tips", 
    description = "Display helpful tips for beginners")
    wm.sfPhysics = bpy.props.BoolProperty(
    name = "Physics", 
    description = "Physics and collision in your scene")
    text1 = 'When this option is set to "Mirror" pressing the X, Y, or Z buttons '
    text2 = 'to the right will mirror your selected objects along the chosen axis. '
    text3 = 'If you press "Mirror" (to switch the option to "Clone") pressing the X, Y or Z '
    text4 = 'buttons will mirror and clone the selected objects. The "Clone" option '
    text5 = 'will automatically switch back to "Mirror" after being pressed.'
    text = text1 + text2 + text3 + text4 + text5
    wm.sfChooseClone = bpy.props.BoolProperty(
    name = "Clone", 
    description = text)
    wm.sfPoseButtons  = bpy.props.EnumProperty(name='Pose Buttons',
    items=(
        ('RESET', "Reset",'Reset pose position'),
        ('FLIP', "Flip",'Flip pose position'),
        ('REPLACE', "Replace",'Replace current pose'),
        ('ADD', "Add",'Add pose to library'),
        ('DELETE', "Delete",'Delete pose from library'),
        ('USE', "Use",'Apply this pose to your object'),
        ('ADDLIBRARY', "Use Pose Library?",'Add a pose library to the armature'),
        ('VOID', "Void",'')
          ),
    update = sfPoseButtons,
    default = 'VOID'
        )    
    wm.sfMeshToolSelect = bpy.props.EnumProperty(name='Mirror Clone',
    items=(
        ('BASIC', "Basic","Basic tools you should memorize\
 because you'll be using them constantly"),
        ('EXTENDED', "Extended",'Extended mesh tools organized\
 by their various types'),
          ),
    default = 'EXTENDED'
        )
    wm.sfMeshTools = bpy.props.EnumProperty(
        items=(
            ('vert', " ", "Vertex Tools",'VERTEXSEL', 0),
            ('edge', " ", "Edge Tools",'EDGESEL', 1),
            ('face', " ", "Face Tools",'FACESEL', 2),
            ('more', " ", "More Tools",'MESH_DATA', 3),
            ('void', " ", "",'MESH_DATA', 4)
            ),
            default = 'void',
            update = sfMeshTools
        )
    text1 = 'In Sensei Format pressing "D" duplicates a mesh selection or object. '
    text2 = 'Pressing "Shift-D" or the "Duplicate" button while in edit mode creates '
    text3 = 'a new object from the mesh selection. This is called "Object From Selection". '
    text4 = 'If "Advanced Ob-From-Sel" is checked, advanced mesh molding will be used. '
    text5 = 'This ensures objects generated from ones using subsurface modifiers retain their '
    text6 = 'shape. If this option is unchecked, the object generated from the mesh selection '
    text7 = 'will be an exact duplicate of the original mesh selection.'
    text8 = text1 + text2 + text3 + text4 + text5 + text6 + text7
    scene.sfObFromSelAdvanced = bpy.props.BoolProperty(
        description = text8,
        default = True)    
def fu7(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except:
        pass
def fu8():
    msg1 = 'Sensei_Format'
    msg2 = 'Sensei_Layout'
    msg3 = 'Sensei_Keys'
    a, b = addon_utils.check(msg1)
    c, d = addon_utils.check(msg2)
    e, f = addon_utils.check(msg3)
    fuf99 = 0
    if b & d & f:
        fuf99 = 1
    return fuf99
addon_keymaps = []
def register():
    bpy.utils.register_module(__name__)
    try:
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("object.sf_3d_cursor_enhanced", 'LEFTMOUSE',
        'DOUBLE_CLICK', alt=True, shift=True)
        fu7(kmi.properties, 'shift', False)
        kmi = km.keymap_items.new("object.sf_3d_cursor_enhanced", 'RIGHTMOUSE','PRESS')
        fu7(kmi.properties, 'shift', False)
        kmi = km.keymap_items.new("object.sf_3d_cursor_enhanced", 'RIGHTMOUSE','PRESS',shift=True)
        fu7(kmi.properties, 'shift', True)        
        kmi = km.keymap_items.new("object.sf_3d_cursor_enhanced", 'RIGHTMOUSE','PRESS',alt=True)
        fu7(kmi.properties, 'alt', True)
        km = wm.keyconfigs.addon.keymaps.new('Object Mode', space_type='EMPTY')
        kmi = km.keymap_items.new("object.sf_sep_objects", 'J','PRESS', alt = True)
        kmi = km.keymap_items.new("object.sf_join_objects", 'J','PRESS')
        kmi = km.keymap_items.new("object.sf_st_duplicate", 'D','PRESS')
        kmi = km.keymap_items.new('transform.sf_custom_resize', 'S', 'PRESS')
        kmi = km.keymap_items.new("screen.redo_last", 'SPACE','DOUBLE_CLICK')
        kmi = km.keymap_items.new("object.origin_set", 'RIGHTMOUSE','DOUBLE_CLICK',shift=True)
        fu7(kmi.properties, 'type', 'ORIGIN_CURSOR')
        km = wm.keyconfigs.addon.keymaps.new('Mesh', space_type='EMPTY')
        kmi = km.keymap_items.new("mesh.duplicate_move", 'D','PRESS')
        kmi = km.keymap_items.new("object.sf_sep_objects", 'J','PRESS', alt = True)
        kmi = km.keymap_items.new("object.sf_object_from_selection", 'D','PRESS', shift = True)
        kmi = km.keymap_items.new("screen.redo_last", 'SPACE','DOUBLE_CLICK')
        addon_keymaps.append(km)
    except:
        pass
def unregister():
    bpy.utils.unregister_module(__name__)
    wm = bpy.context.window_manager
    for km in addon_keymaps:
        wm.keyconfigs.addon.keymaps.remove(km)
    del addon_keymaps[:]
if __name__ == "__main__":
    register()