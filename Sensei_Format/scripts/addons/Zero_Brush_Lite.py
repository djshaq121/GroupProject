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
 "name": "Zero Brush Lite",
 "author": "Blender Sensei Blendersensei.com",
 "version": (1, 8, 0),
 "location": "Properties shelf & Tool shelf of Sensei tab (SPACE: brush menu | Q: options)",
 "description": "Zero button texture painting by Blender Sensei",
 "wiki_url": "https://blendersensei.com/zero-brush",
 "category": "Sensei Format"}

import zlib
i_0 = b'x\xda}WKo\xdb8\x10\xfe+\xb3\xb9l\n\x04)\xd0^\x16{\x8b\x9d\xb4\r\xd6\xd9\x04q\xdc\x02{\x11hil\xb1\x91I\x95\xa4\xecj\xd1\x1f\xbf3|H\x94\xed\xec\xc5\x96f\xc8y\x7f3#\x87?]g\xf0\xfa\xdfu\xd1hQ\x15k\xd3\xd9\xba\xf8\xf0\xe1\xb7?\x8a\xd9\xf8\xb8 \x16\x08\x05r\'\xb6\x08\x97\xad\xda^\xc1\xf7\x16\xe9\xd7\xc9\xcd\xe6\n\xd0\x95\xd7\xd7\xef@X\x10\x90I\xd0\xeb\xefX:\x96\xdd\n\xe3d\xd9`Q\xa1\x13\xb2),6\xc4\t\xa7\x9e"\x0fn=\x0f\x96\x19/<\x83\xab\x11\\\xdf"\xe8\r$QP\xd6\xb2\xa9\x0c*\x082\xc1i\x90\xaa4(,\x9d3D\x8d\xcf\x97\xc3\r\xac\xa4\x83\x9d\xae\xf0\n\x82i\xf1\x85\x84Th\xde\x05\x95\x0f\xc2\xa1\x91\xa2\x81\xc7\xd6I\xadl\xa0\xeePu\xec\xc8.r\x0b\x1d\xb9\xcc8\xba\xa8[4\xc2s\xa1\x91\xafH\xe2wz/\xd5\x16\xd2e\xcb\xf6u{zo-l\x8c\xdeQ\xd8BD\xe8\xd2u\x90vc\xad\xdc*HB\xa7V\x88\xaa\x1a-\t\xc7+J\xd0\xa0\x80c\xc11\x0bB\xb1\x8a\xee&\xb7\xbd\xfe\x1d\xda\xfaz\x12\xe5Y\xff\x86\xba\x98\xadu\x7f\xa44\xde\x13M3\x08v\xb5 \x82A\xe8,{\xccF\x0cFyO\x99\xd2H\xeb\xae\x8fK$\x8bl\n\xdfIB\xa6\x8cg\x8e+z\xf5cd\x07%G\xbe\xdb\xa9B\xbb)D\xdb6}\xe1\xf0gt\xe6\xd3_p\xc3$x\t\x98\x08\xe4\xb9V{4.\x94\xbe\x85\xca\xe8\xb6e\xa1\x8aB\x9c\x9c\x1etn$U\xd9\xda\xe8\x83EC\xc5HG\x06\xc3\xa2zw\x0eoh3\xc4\xa5\x97\x809\xd8\xe8\x86j\x93\x0b?Z\xf0\x7f\xe8\x9bH\x9b\xe60\xc0r\xac\xd6\x7ff\xe0\xd5\x019\xc8F\x1d\xa7#\x9c/\xcf0)te\x08\xca4B/\x1a\x1e0A?\x11\x95V\xbe\xd2\x86X\x85\xa8\xe0i\x8b`(\x16\xeb\xce\xb9!\xbf3\xff\x12\x9e\x1f\x03^\x7f\xc1\xb2\xec\x9a\x96\x1f\x9e\x04\x89\xf2\xff\x11\xdd\xbf\x12b\xe9\xe9S\xd74\x96\xf0\x8f\xeaX\x8dEW\x08\x02\xda\x1e\x8bF\xf4hR%;\xb8\xf1\xd4\x94}X\x8c\xdc\xc8\x89\xb9\x83\xec^\xcbF\xb0X\xaaL\x8b\xe1u\x88\xef\x1d\xd3\x0c<%#\xbeP*\xc1\xd6r\xe3\x18\x9f\xfe\x06\xf8\x1bWp@\xb9\xad\xe9\x9fc\x86?\xa9\xd5VT9\xf6\xd5w\x88\xd3@\x91\xed.\xaf\xd1\x07=\xda\x9dQ&\xf6B\xd7\xfa\xae\xa8\x0f\'!\xa9\x08)\xeeH\xe4\xad\xa7M\x85F\xda\x990\x8c\xb2\x0c\xfa\xb2&L\x16\xa1^\x87h<{\x0e\xdc\x10Z\xef3N$3\x88I.\x1aEO\xbd\xef\xd4\x84\xb2X\xf2kQ\xbe\x86\xc2\x995\xbeU\x9f$U\xa4tF\xa9K"\xc0C\x1f\x92\x18i\xf3F\x92\x18WK\x12\x88\x1bM\x1e\xd05nR\xbd\xeeL\x80.i`Q4Z\x84b\xc5;Qy\xa2\xc2Cp7\xc1\x98\xfcY\xf6\xd6\xe1\xee\xa8Q\x06\x9a\xce\'G\xf8\xddK<|\xbc\xf5\xb0\xf7a;\x1d\x1fy\'|\xc5\xa2S\xf2G\x87\x83\xb6\x07\xa2\xc1*\xa3yB\x9cb\xf9\xd9<\x15\\\xeb\xdd~\x084\xbd\xc2\xea+\x89jsJ\x92\xe1\xc7\x91\xaf<\x02\x930o\xa5\xd7\x87\xbf5\xb8\xcf\x12\xcb4x"\x1a9\x99D\x9f\xd2\xf2m\x80aR\xeaF\x9bqz\xcd\xc7\xd7\x17\xce\x11\xcd8^\'\x0cn\xbb\x86\xcc\x99\x163\xa5\x0cJZH\xbc$\xd0\xea\xbc\x86u\xb7kG\x05\xb3\xe1-\x97\x1f\xe4\x1d\xa4\xab\xe9\xe5\x82o\\\x00n6\x1c\x92\xcb\xbd\xb4rMeq\xa8\xb98\x82\xef\\0\x92\x9a\xb1\x82yO\x81\xb2\xef\xce\xab\xb6-\x96l\xf7\xa8~9\xa1\xe4&\xa4\xb3\x8c\xcf\x8be-\x95Th\xed\x85\xcf\x07\xa9.k \xdcY\xefs\xf0\xf7P#E\x82\xdf\x0fB\x85\xed\x88\xda\x8a\xc2\xf3\xa68#\x94\xa5\x1d\x08Skbk^\x8e\x89\xde\xa0\x83$\x18R\x98U\xc0D,\r\xa9R \xb8:\xc8\x96\xcc\x14j\xef\xf2dv\x88\xa6\xadE\xc1\rlTx\xc34\xaa\xbdD\xf3\xfa\x8e\xfc\x1a--\xfb0as3\xbc\xd7\xfb\x94\xfcZk\xfb\x86\xc3\xdbF\x1fF\xc5\x9f\xf37\x9fqn\xb5\x80;\xe9\x1c\'\xd3\x17\xc05\xac\xa8\x19\xfb\x11\xaeMI\x19\x97\xb4>\xf4\xa7;J\xd78I\xb8\xf2\x0b\xd8\x08\xc30\x93\x04Eh:\xfc\x8eV\x90\xd0\xc2(\xdf\xc3\xf1\xc4\xe0\xb8Z\'\xf8\x8a\xe7\x91]\'-\xce3\x8a\xaaWb\'\xcb\xd8\xe5\xc2,\xbc\r4n\x9c\xb1Q\x8f\x04\xd8\xa2\xe2\xad\t\xc3\x14\x16!\xdcA\x18\\\x1a\xfc\xd1\xb1?T\xdbN\xb7\x04\xc0m\xcfaV\xd4\r\x95\xa4M\xa2:\xa9n\xdbeQ\x88\xa3\xc6\xa4\xd5=Z\xd5\xad+\xb9\x97\x15N\xb2\xb7\xe1\x95\x93\x8f\x86m\x9d\x82\xf2\xa6\xab\x83\xfcqX-\x08\x10\x13%\xcfXu\xe5D\xc3\xef6\xb9Ue\xe7\x8e\xdba5\x91\xc1\xfd\xef\xf6\x84\xc2[\xcc\x84<\nI\xd1,\xd6<\xee\xc75\xc6\x97\xc1L\xa4\x8a\x0c{d0\x87<\x1d?P\xb8\xc2:n#M\xef?\x08X\x13m\xb5;\xa1\x08\x88)}\x19\x90\xa8\xcc,\xa3\xa2\xb2Y#9"\\A\xa9\xdb\xfe*|\xf3\xf8\t=|\xf0\xc4\xbbaA\xcdb\x15\x0b;\x18\xe8\xd3\xea\x8c\xa6\xa1cwZ\xbbz\x1cq\x9e\n\xcb\x8czrEr\xa9[<\xbes\x9f\x93\xb3\xf2\t\x97\xde\\\xf3\xc2R\xe7\xbbqE\xbb-r\x7f\xa2\xde&Z\xb4\x7f\xc2\xf3\xdd\xe7\xd5\xe2\xe6\x19f\xcf\xab\xe5\x97\xf70_=\x7f\xbd{\x0f\x8b\xfb\xbf\xe9w~\xff<_\xdc\x1d\xab+\xe9:\x8d+\x1a\xca\xaaL\xc9\x9c{\x1a\xd9yJ\x8b\xe7<\x1c}\xb9\x80\xd1\xce\x7fq\x04\x84\x12\xa2\xcex\x14\xe4\xd8^%T\xd2S\x12\x1f]\xfcz\x7f\xf7\xad\xf8x\x1b;\xdf\xe3\xe3b\x99\xd6NeQ\xc6\xd8\xa1\xd1q%_\xd0\xf2sr\xf6,\x7f"xu\x9fr\xc4\x8b/\xef\xe9d\x1f\x01\xd9\x15\xfc\xc1\xc5\x95;d\xe9\x9e\xa8$&\xa7\x0e\xabl\xfc\xda\x0b+i\xb1\x93\xc6\xe8\xf1b\xfc\xe4\xfb\xe6\x99\xf0\x901\xc7\xaf\x03\x17\x939k\x84\x8a\xdd~\xa5\xc4\x9e 0\xb6\xc8\xff\x00~@\xcf\xb6'
i_1 = b'x\xda\x03\x00\x00\x00\x00\x01'
a = str(zlib.decompress(i_0))[2:]
i_0 = a.split('_22!8_')
b = str(zlib.decompress(i_1))[2:]
i_1 = b.split('_22!8_')
import bpy, os, addon_utils
from bpy.props import*
from bpy_extras.io_utils import ImportHelper
from bpy.types import Menu, Panel
from bl_ui.properties_paint_common import (
        UnifiedPaintPanel,
        brush_texture_settings,
        )
def fu0():
    d = bpy.data
    item = [d.images,d.textures,d.node_groups,
    d.materials,d.worlds,d.meshes,d.objects]
    for i in item:
        try:
            for ob in i:
                if ob.users < 1:                
                    try:
                        i.remove(ob, do_unlink = True)
                    except:
                        try:
                            i.remove(ob)
                        except:
                            pass
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
    if 'PARTICLE' in mode:
        mode = 'PARTICLE_EDIT'
    try:
        bpy.ops.object.mode_set(mode= mode)
    except:
        print('unable to return to previous mode')
    return
def fu2(fn):    
    newName = ''.join(x for x in fn if x not in
    ',<>:""[]{}()/\|!@$%^&*,.?')    
    newName = newName.replace("-", " ")
    newName = newName.replace("_", " ")
    if len(newName) > 20:
        newName = newName.replace(" ", "")
    newName = newName[:18]
    for i in newName:
        if newName[:1] == ' ':
            newName = newName[1:]
    if len(newName) < 1:
        newName = "myBrush"
    newName = "°" + newName.title()    
    return newName
def fu3(brush, tex, fn, filepath, brushes, mode):
    tool_settings = bpy.context.tool_settings
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    mode = bpy.context.mode
    if brushes == 1:
        newName = brush.name
    else:
        newName = fu2(fn)
        brush.name = newName
        brush.texture = tex
        brush.use_custom_icon = True
        brush.icon_filepath = filepath
    try: 
        brush.stroke_method = 'DOTS'
        brush.texture_slot.tex_paint_map_mode = 'TILED'
        brush.texture_overlay_alpha = 30
        brush.mask_overlay_alpha = 30
        tool_settings.image_paint.input_samples = 1
        tool_settings.sculpt.input_samples = 1
    except:
        pass
    if bpy.context.mode == 'SCULPT':
        bpy.ops.brush.curve_preset(shape='LINE')
        brush.texture.filter_eccentricity = 64
        bpy.ops.brush.curve_preset(shape='MAX')
def fu4(context, filepath):
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    settings = bpy.context.tool_settings
    mode = bpy.context.mode
    aType = bpy.context.area.type
    if aType == 'IMAGE_EDITOR':
        bpy.context.area.type = 'VIEW_3D'
        bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
    if os.path.isdir(filepath):
        return
    else:
        fn = bpy.path.display_name_from_filepath(filepath)
        imgExists = False
        for image in bpy.data.images:
            if image.name in filepath:
                img = image
                imgExists = True
                break
        if imgExists == False:
            img = bpy.data.images.load(filepath)
            img.use_fake_user =True
        tex = bpy.data.textures.new(name =fn, type='IMAGE')
        tex.image = img 
        if 'PAINT' in mode:
            if mode == 'PAINT_TEXTURE':
                bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
                bpy.ops.brush.add()
                brush = bpy.context.tool_settings.image_paint.brush
                bpy.data.brushes[brush.name].image_tool = 'DRAW'
            else:
                bpy.ops.object.mode_set(mode='VERTEX_PAINT')
                bpy.ops.brush.add()
                brush = bpy.context.tool_settings.vertex_paint.brush
                bpy.data.brushes[brush.name].vertex_tool = 'MIX'
            bpy.ops.brush.curve_preset(shape='SHARP')
            brush.color = (1, 1, 1)
            brush.strength = 1
        if 'SCULPT' in mode:
            bpy.ops.brush.add()
            brush = bpy.context.tool_settings.sculpt.brush
            bpy.data.brushes[brush.name].sculpt_tool = 'DRAW'
            bpy.ops.brush.curve_preset(shape='SHARP')
            brush.strength = 0.125
            brush.auto_smooth_factor = 0.15
        if scene.zbLoadImgSculpt:
            if 'SCULPT' in mode:
                brush.use_paint_image = True
                brush.use_paint_vertex = True
            else:
                brush.use_paint_sculpt = True
        brushes = 0 
        fu3(brush, tex, fn, filepath, brushes, mode)
    fu1(mode)
    if aType == 'IMAGE_EDITOR':
        bpy.context.area.type = aType
        bpy.ops.object.mode_set(mode='EDIT')
    return {'FINISHED'}
class cl0(bpy.types.Operator, ImportHelper):
    bl_idname =i_0[0]
    bl_label =i_0[1]
    bl_description =i_0[2]
    @classmethod
    def poll(cls, context):
        return context.active_object != None
    def execute(self, context):
        return fu4(context, self.filepath)
class zbParticleDetailSelect(bpy.types.Operator):
    bl_idname =i_0[3]
    bl_label =i_0[4]
    bl_description =i_0[5]
    detailSelect = bpy.props.StringProperty()
    def execute(self,context):
        scene = bpy.context.scene
        dSel = self.detailSelect        
        scene.zbParticleDetailSelect = dSel        
        return{'FINISHED'}
class cl1(bpy.types.Menu):
    bl_label =i_0[6]
    bl_idname =i_0[7]
    bl_description =i_0[8]
    def draw(self, context):
        layout = self.layout
        col = layout.column()
        ob = bpy.context.active_object
        if ob:
            mat = ob.active_material
            col.menu('menu.zb_add_material',icon='ZOOMIN')
            col.operator('object.zb_material_operations',
            text='Remove Materials',icon='ZOOMOUT').op = 'REMOVE_MATERIALS'
            col.operator('object.zb_material_operations',
            text='Remove UV Maps',icon='ZOOMOUT').op = 'REMOVE_UVMAPS'
            col.menu('menu.zb_select_by_material',icon='HAND')  
            if ob.active_material:
                col.separator()
                try:
                    col.operator("object.zb_make_unique", text="Make Unique",
                    icon='MATERIAL')
                except:
                    pass
            else:
                try:
                    if ob.data.uv_textures.active.data[0].image:
                        col.separator()
                        col.operator('object.sf_apply_tex',text='Convert UV To Material',
                        icon = 'MATERIAL')
                except:
                    pass  
        else:
            col.label('Material Operations (select object first)')
class cl2(bpy.types.Menu):
    bl_label =i_0[9]
    bl_idname =i_0[10]
    bl_description =i_0[11]
    def draw(self, context):
        layout = self.layout
        col = layout.column()        
        if len(bpy.data.materials) > 0:
            for mat in bpy.data.materials:
                col.operator('object.zb_material_operations',text=mat.name,
                icon='MATERIAL').op = mat.name + '__ZB__ADD_MATERIAL'
        else:
            col.label('No Materils Found In File',icon='MATERIAL')
class cl3(bpy.types.Menu):
    bl_label =i_0[12]
    bl_idname =i_0[13]
    bl_description =i_0[14]
    def draw(self, context):
        layout = self.layout
        col = layout.column()        
        if len(bpy.data.materials) > 0:
            for mat in bpy.data.materials:
                col.operator('object.zb_material_operations',text=mat.name,
                icon='MATERIAL').op = mat.name + '__ZB__SELECT_BY_MATERIAL'
        else:
            col.label('No Materils To Select From',icon='MATERIAL')   
class cl4(bpy.types.Operator):
    bl_idname =i_0[15]
    bl_label =i_0[16]
    bl_description =i_0[17]
    op = bpy.props.StringProperty()
    def execute(self,context):
        scene = bpy.context.scene
        mode = bpy.context.mode
        wm = bpy.context.window_manager
        ob = bpy.context.active_object
        selected = bpy.context.selected_objects
        op = self.op
        if 'ADD_MATERIAL' in op:
            mName = op.split('__ZB__ADD_MATERIAL')[0] 
            mat = bpy.data.materials[mName]
            if 'EDIT' in mode:
                if not ob.active_material:
                    bpy.ops.object.material_slot_add()
                if mName not in ob.data.materials:
                    ob.data.materials.append(mat)                
                i=0
                for m in ob.data.materials:
                    if ob.active_material == mat:
                        break
                    else:
                        ob.active_material_index = i
                        i+=1
                bpy.ops.object.material_slot_assign()
            else:             
                for ob in selected:                
                    ob.active_material = mat   
        if 'REMOVE_MATERIALS' in op:
            activeOb = bpy.context.active_object            
            for obj in selected:
                if hasattr(obj.data,'materials'):
                    scene.objects.active = obj                    
                    for m in obj.data.materials:
                        try:
                            bpy.ops.object.material_slot_remove()
                        except:
                            print('Could not remove material for',obj.name)
            scene.objects.active = ob
        if 'REMOVE_UVMAPS' in op:
            activeOb = bpy.context.active_object            
            for obj in selected:
                scene.objects.active = obj
                if hasattr(obj.data,'uv_textures'):
                    for uv in obj.data.uv_textures:
                        try:
                            bpy.ops.mesh.uv_texture_remove()
                        except:
                            print('Could not remove uv map for',obj.name)
            scene.objects.active = ob
        if 'SELECT_BY_MATERIAL' in op:
            mName = op.split('__ZB__SELECT_BY_MATERIAL')[0]
            for ob in bpy.data.objects:
                if hasattr(ob,'active_material'):
                    if hasattr(ob,'data'):
                        if hasattr(ob.data,'materials'):
                            if mName in ob.data.materials:
                                ob.select = True
                            else:
                                ob.select = False
                        else:
                            ob.select = False
                    else:
                        ob.select = False
                else:                        
                    ob.select = False
        return{'FINISHED'}
class cl5(bpy.types.Operator):
    bl_idname =i_0[18]
    bl_label =i_0[19]
    bl_description =i_0[20]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        scene = bpy.context.scene
        renEng = scene.render.engine
        scene = bpy.context.scene
        selected = bpy.context.selected_objects
        mode = bpy.context.mode
        for ob in selected:
            if ob.type == 'MESH':
                scene.objects.active = ob
                if ob.data.uv_textures:
                    img = ob.data.uv_textures.active.data[0].image                
                    bpy.ops.object.zb_paint_color()
                    mat = ob.active_material
                    mat.active_texture.image = img
                    imgNode = mat.node_tree.nodes['Image Texture zbColor']
                    imgNode.image = img
        fu1(mode)                    
        return {'FINISHED'}
def fu5(context, filepath):
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    aType = bpy.context.area.type
    settings = bpy.context.tool_settings
    mode = bpy.context.mode
    if aType == 'IMAGE_EDITOR':
        bpy.context.area.type = 'VIEW_3D'
        bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
    if os.path.isdir(filepath):
        directory = filepath
    else:
        li = filepath.split(os.sep)
        directory = filepath.rstrip(li[-1])
    files = os.listdir(directory)
    for f in files:
        imgExists = False
        for blendImage in bpy.data.images:
            if blendImage.name in f:
                imgExists = True
                img = blendImage
                fn = f[3:] 
                tex = bpy.data.textures.new(name =fn, type='IMAGE')
                tex.use_fake_user =True
                tex.image = img 
                break
        if imgExists == False:
            try:
                fn = f[3:]
                img = bpy.data.images.load(filepath = directory +os.sep + f)
                img.use_fake_user =True
                tex = bpy.data.textures.new(name =fn, type='IMAGE')
                tex.use_fake_user =True
                tex.image = img 
            except:
                pass
            if bpy.context.mode.startswith('PAINT'):
                if mode == 'PAINT_TEXTURE':
                    bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
                    bpy.ops.brush.add()
                    brush = bpy.context.tool_settings.image_paint.brush
                    bpy.data.brushes[brush.name].image_tool = 'DRAW'
                else:
                    bpy.ops.object.mode_set(mode='VERTEX_PAINT')
                    bpy.ops.brush.add()
                    brush = bpy.context.tool_settings.vertex_paint.brush
                    bpy.data.brushes[brush.name].vertex_tool = 'MIX'
                bpy.ops.brush.curve_preset(shape='SHARP')
                brush.color = (1, 1, 1)
            if bpy.context.mode.startswith('SCULPT') is True:
                bpy.ops.object.mode_set(mode='SCULPT')
                bpy.ops.brush.add()
                brush = bpy.context.tool_settings.sculpt.brush
                bpy.data.brushes[brush.name].sculpt_tool = 'DRAW'
                bpy.ops.brush.curve_preset(shape='SHARP')
                brush.strength = 0.125
                brush.auto_smooth_factor = 0.15
            fn = bpy.path.display_name_from_filepath(directory +os.sep + f)
            newName = fu2(fn)
            brush.name = newName
            brush.texture = tex
            brush.use_custom_icon = True
            brush.icon_filepath = directory +os.sep + f
            brushes = 1
            if scene.zbLoadImgSculpt:
                if 'SCULPT' in mode:
                    brush.use_paint_image = True
                    brush.use_paint_vertex = True
                else:
                    brush.use_paint_sculpt = True
            fu3(brush, tex, fn, filepath, brushes, mode)
    fu1(mode)
    if aType == 'IMAGE_EDITOR':
        bpy.context.area.type = aType
        bpy.ops.object.mode_set(mode='EDIT')
    return {'FINISHED'}
class cl0es(bpy.types.Operator, ImportHelper):
    bl_idname =i_0[21]
    bl_label =i_0[22]
    bl_description =i_0[23]
    @classmethod
    def poll(cls, context):
        return context.active_object != None
    def execute(self, context):
        return fu5(context, self.filepath)
class cl6(bpy.types.Menu):
    bl_label =i_0[24]
    bl_idname =i_0[25]
    def draw(self, context):
        mode = bpy.context.mode
        ts = bpy.context.tool_settings
        aType = bpy.context.area.type
        layout = self.layout
        flow = layout.column_flow(columns=3)
        if fu20():
            for brush in bpy.data.brushes:
                if mode == 'PAINT_TEXTURE' or aType == 'IMAGE_EDITOR':
                    if brush.use_paint_image:
                        row = flow.row(align=True)
                        row.operator('object.zb_brush_context', text= brush.name,
                        icon_value=layout.icon(brush)).brushName = brush.name
                if mode == 'SCULPT':
                    if brush.use_paint_sculpt:
                        row = flow.row(align=True)
                        row.operator('object.zb_brush_context', text= brush.name,
                        icon_value=layout.icon(brush)).brushName = brush.name
                if mode == 'PAINT_WEIGHT':
                    if brush.use_paint_weight:
                        row = flow.row(align=True)
                        row.operator('object.zb_brush_context', text= brush.name,
                        icon_value=layout.icon(brush)).brushName = brush.name
                if mode == 'PAINT_VERTEX':
                    if brush.use_paint_vertex:
                        row = flow.row(align=True)
                        row.operator('object.zb_brush_context', text= brush.name,
                        icon_value=layout.icon(brush)).brushName = brush.name
            if mode == 'PARTICLE':
                settings = ts.particle_edit
                brush = settings.brush
                tool = settings.tool
                tools = ['COMB','SMOOTH','ADD','LENGTH','PUFF','CUT']
                for tool in tools:
                    row = flow.row()
                    row.operator('object.zb_brush_context',
                    text=tool.title(), icon='PARTICLEMODE').brushName = tool
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
class cl7(bpy.types.Operator):
    bl_label =i_0[26]
    bl_idname =i_0[27]
    brushName = bpy.props.StringProperty()
    def execute(self,context):
        scene = bpy.context.scene
        wm = bpy.context.window_manager
        sd = bpy.context.space_data
        ts = bpy.context.tool_settings
        ups = ts.unified_paint_settings
        aType = bpy.context.area.type
        mode = bpy.context.mode
        if mode == 'PAINT_TEXTURE' or aType == 'IMAGE_EDITOR':
            brush = bpy.data.brushes[self.brushName]
            paint = ts.image_paint
            if 'Fill' not in brush.name:
                wm.zbGradientSwitch = False
            else:
                brush.use_gradient = False
            ts.image_paint.brush = brush
            if 'Smear' in brush.name:
                brush.stroke_method = 'DOTS'
            if 'Soften' in brush.name:
                brush.stroke_method = 'DOTS'
            if 'Clone' in brush.name:
                brush.stroke_method = 'DOTS'
            if 'Mask' in brush.name:
                if not paint.stencil_image:
                    bpy.ops.image.new(gen_context='PAINT_STENCIL')
                wm.zbViewMaskMode = 1
            else:
                if aType == 'VIEW_3D':
                    sd.viewport_shade = 'MATERIAL'
            if 'Draw' in brush.name or 'Pen' in brush.name:
                paint.input_samples = 3
            else:
                paint.input_samples = 1
            if 'Graphic Pen' in brush.name:
                ups.use_pressure_size = True
            else:
                ups.use_pressure_size = False
        if mode == 'SCULPT':
            brush = bpy.data.brushes[self.brushName]
            ts.sculpt.brush = brush 
        if mode == 'PARTICLE':
            settings = ts.particle_edit
            settings.tool = self.brushName
            bpy.context.area.tag_redraw()
        if mode == 'PAINT_WEIGHT':
            sd.viewport_shade = 'SOLID'
            brush = bpy.data.brushes[self.brushName]
            ts.weight_paint.brush = brush 
        if mode == 'PAINT_VERTEX':
            brush = bpy.data.brushes[self.brushName]
            ts.vertex_paint.brush = brush 
        return{'FINISHED'}
def fu6(self,context):
    wm = bpy.context.window_manager
    sd = bpy.context.space_data
    sculpt = bpy.context.mode.startswith('SCULPT')
    paint = bpy.context.mode.startswith('PAINT')
    re = bpy.context.scene.render.engine
    if sculpt:
        type = bpy.context.tool_settings.sculpt
    if paint:
        type = bpy.context.tool_settings.image_paint
    try: 
        type.brush.strength = 1
        type.brush.use_pressure_strength = False
    except:
        pass
    if wm.zbViewMaskMode:
        if re == 'BLENDER_RENDER':
            sd.viewport_shade = 'SOLID'
        else:
            sd.viewport_shade = 'TEXTURED'
        if sculpt:
            sd.viewport_shade = 'SOLID'
    else:
        if sd.viewport_shade != 'TEXTURED':
            sd.viewport_shade = 'MATERIAL'
        if sculpt:
            try:
                type.brush = bpy.data.brushes['SculptDraw']
            except:
                pass
        if paint:
            try:
                type.brush = bpy.data.brushes['Draw']
            except:
                pass
def fu7():
    bpy.ops.object.mode_set(mode='OBJECT')
    realOb = bpy.context.active_object 
    mirror = len([mod for mod in realOb.modifiers if mod.type == 'MIRROR'])
    if mirror:
        try:
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
        except:
            pass
    armature = len([mod for mod in realOb.modifiers if mod.type == 'ARMATURE'])
    if armature < 1:
        bpy.ops.object.skin_armature_create(modifier="Skin") 
        ob = bpy.context.active_object 
        bones = bpy.context.object.data
        bones.use_auto_ik = True
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.armature.select_all(action='SELECT')
        bpy.ops.armature.calculate_roll(type='GLOBAL_POS_Z')
        bpy.ops.object.mode_set(mode='POSE')
        if not bpy.context.active_object.pose_library:
            bpy.ops.poselib.new()
        bpy.ops.object.mode_set(mode='OBJECT')
        ob.name = realOb.name + "sBones" 
        bpy.context.active_object.select = False 
        bpy.context.object.hide = True 
        bpy.context.scene.objects.active = realOb 
    try:
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Skin")
    except:
        pass
    realOb.select = True 
    bpy.context.space_data.use_occlude_geometry = True 
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.mesh.vert_connect_nonplanar()
    bpy.ops.mesh.tris_convert_to_quads()
    bpy.ops.object.mode_set(mode='OBJECT')
    for x in range(20):
        bpy.ops.object.modifier_move_up(modifier="Armature") 
    return{'FINISHED'}
class cl8(bpy.types.Operator):
    bl_idname =i_0[28]
    bl_label =i_0[29]
    bl_description =i_0[30]
    def execute(self,context):
        mode = bpy.context.mode
        bpy.ops.object.mode_set(mode='OBJECT')
        sel = bpy.context.selected_objects
        for ob in sel:
            removeMeta = False
            if ob.type == 'META':
                removeMeta = True
            try:                
                bpy.ops.object.convert(target='MESH')
                if removeMeta: 
                    for obj in bpy.data.objects:
                        if obj.type == 'META':
                            bpy.context.scene.objects.unlink(obj)
                    for obj in bpy.data.objects:    
                        if 'MBall' in obj.name:
                            obj.select = True
                            break
                bpy.ops.object.mode_set(mode='EDIT')                              
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.remove_doubles()
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.tris_convert_to_quads()
                bpy.ops.mesh.tris_convert_to_quads()
                bpy.ops.mesh.beautify_fill()
                if ob.type == 'FONT': 
                    bpy.ops.mesh.select_all(action='SELECT')
                    bpy.ops.uv.smart_project(island_margin = 0.03)
            except:
                pass
        fu1(mode)        
        return{'FINISHED'}
class cl9(bpy.types.Operator):
    bl_idname =i_0[31]
    bl_label =i_0[32]
    bl_description =i_0[33]
    modeButton = bpy.props.IntProperty()
    @classmethod
    def poll(cls, context):
        ob = bpy.context.active_object
        abortOp = False
        try:
            ob.library.users
            abortOp = True
        except:      
            try:
                ob.data.library.users
                abortOp = True
            except:
                pass        
        return abortOp == False
    def execute(self, context):
        scene = bpy.context.scene
        wm = bpy.context.window_manager
        re = scene.render.engine
        mode = bpy.context.mode        
        sd = bpy.context.space_data
        try:
            ob = bpy.context.active_object
            mat = ob.active_material
        except:
            ob = 0
        if ob:                        
            if self.modeButton != 3 and self.modeButton < 5:
                if bpy.context.image_paint_object:
                    if scene.zbAutoSaveLayers:                        
                        bpy.ops.object.zb_save_layers(save_only_active=True)
                        self.report({'INFO'}, "Paint layers saved.")
            if self.modeButton == 1:
                try: 
                    ob.modifiers["Multires"].show_viewport = True
                except:
                    pass
                bpy.ops.object.mode_set(mode='OBJECT')
            elif self.modeButton == 2:
                if scene.zbDisableShadows:
                    scene.zbDisableShadows = True
                else:
                    scene.zbDisableShadows = False
                if ob.type != 'MESH':
                    mType = ['SURFACE','FONT','META','CURVE']
                    for m in mType:
                        if m in ob.type:
                            bpy.ops.object.sf_convert()
                            ob = bpy.context.active_object
                            break
                if ob.type == 'MESH':
                    try: 
                        ob.modifiers["Multires"].show_viewport = True
                    except:
                        pass
                    try: 
                        bpy.ops.object.transform_apply(scale=True)
                    except:
                        pass
                    bpy.ops.object.mode_set(mode='SCULPT')
                    if scene.zbFastMode:
                        sd.viewport_shade = 'SOLID'
                else:
                    self.report({'INFO'}, "This mode is only for mesh objects.")
            elif self.modeButton == 3:
                if scene.zbDisableShadows:
                    scene.zbDisableShadows = True
                else:
                    scene.zbDisableShadows = False
                if ob.type != 'MESH':
                    mType = ['SURFACE','FONT','META','CURVE']
                    for m in mType:
                        if m in ob.type:
                            bpy.ops.object.sf_convert()
                            break
                if ob.type == 'MESH':
                    try: 
                        ob.modifiers["Multires"].show_viewport = True
                    except:
                        pass
                    if re == 'CYCLES':
                        if scene.zbGoCycles == False:
                            scene.zbGoCycles = True
                    else:
                        if scene.zbGoCycles:
                            scene.zbGoCycles = False
                    skin = len([mod for mod in ob.modifiers if mod.type == 'SKIN'])
                    if skin:
                        fu7()
                        self.report({'INFO'},
                        ("APPLIED SKIN: Click 'EYE' icon next to"
                        + ob.name + " in the outliner to see it."))
                    hasPaint = False
                    if mat is not None:
                        for ts in mat.texture_slots:
                            if ts is not None:
                                try:
                                    if ts.texture.image:
                                        if ts.texture_coords == 'UV':
                                            hasPaint = True
                                            break
                                except:
                                    pass
                        if hasPaint == False:
                            if mat.use_nodes:
                                if mat.node_tree.nodes:
                                    if 'Image Texture' in mat.node_tree.nodes:
                                        hasPaint = True   
                    if hasPaint:
                        try:
                            scene.game_settings.material_mode = 'GLSL'
                        except:
                            pass
                    else:
                        for sl in ob.material_slots:
                            if not sl.material:
                                i = 0
                                for sl in ob.material_slots:
                                    ob.active_material_index = i
                                    if not sl.material:
                                        break
                                    else:
                                        i += 1
                                break
                        bpy.ops.object.zb_paint_color()
                    if sd.viewport_shade != 'TEXTURED':
                        sd.viewport_shade = 'MATERIAL'
                    bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
                    try: 
                        ob = bpy.context.active_object
                        for mod in ob.modifiers:
                            if mod.type == 'BEVEL':
                                if mod.show_viewport == True:
                                    bpy.ops.object.mode_set(mode='OBJECT')
                                    mod.show_viewport = True
                                    bpy.ops.object.mode_set(mode='TEXTURE_PAINT')
                                    break
                    except:
                        pass
                else:
                    self.report({'INFO'}, "This mode is only for mesh objects.")
            elif self.modeButton == 4:
                if scene.zbFastMode:
                     try:
                         ob.modifiers["Multires"].show_viewport = False
                     except:
                         pass
                skin = len([mod for mod in ob.modifiers if mod.type == 'SKIN'])
                if skin:
                    fu7()
                    self.report({'INFO'},
                    ("APPLIED SKIN: Click 'EYE' icon next to"
                    + ob.name + " in the outliner to see it."))
                report = 0
                for type in ob.modifiers:
                    try:
                        if "Bones" not in type.object.name:
                            report = 1
                            break
                    except:
                        pass
                if report == 1:
                    self.report({'INFO'}, "Object already has armature. None created for it.")
                try: 
                    if bpy.context.active_object.type == 'MESH':
                        if context.active_object.particle_systems.active is None:
                            bpy.ops.object.zb_add_strands(option = 'NEW')
                        bpy.ops.object.mode_set(mode='PARTICLE_EDIT')
                    else:
                        self.report({'INFO'}, "This mode is not available for this type of object.")
                except:
                    pass
        else:
            if ob: 
                if bpy.context.mode != 'POSE':
                    bpy.ops.object.mode_set(mode='OBJECT')
            if self.modeButton != 1:
                if self.modeButton != 6:
                    self.report({'INFO'}, "This mode is only for mesh objects.")
        if scene.zbDisableShadows:
            if self.modeButton > 3 or self.modeButton < 2:
                for lamp in bpy.data.lamps:
                    try:
                       lamp.shadow_method = 'RAY_SHADOW'
                    except:
                        pass
        if self.modeButton == 6:
            bpy.ops.screen.screen_full_area()
        return{'FINISHED'}
def fu8(self, context):
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    sd = bpy.context.space_data
    ren = scene.render
    if self.zbFastMode:
        ren.use_simplify = True
        if wm.zbLampBufferSize == 0: 
            ren.simplify_child_particles = 0.0
            ren.simplify_shadow_samples = 1
            ren.simplify_ao_sss = 0.15
            ren.simplify_subdivision = 3
        for lamp in bpy.data.lamps:
            if lamp.type != 'HEMI':
                if lamp.shadow_buffer_size > 0:
                    if lamp.shadow_buffer_size != 128:
                        wm.zbLampBufferSize = lamp.shadow_buffer_size
                    lamp.shadow_buffer_size = 128
        scene.tool_settings.sculpt.show_low_resolution = True
        if context.sculpt_object:
            sd.viewport_shade = 'SOLID'
        if context.particle_edit_object:
            try:
                bpy.context.object.modifiers["Multires"].show_viewport = False
            except:
                pass
        else:
            try:
                bpy.context.object.modifiers["Multires"].show_viewport = True
            except:
                pass
        try: 
            sel = bpy.context.selected_objects
            bpy.ops.object.select_all(action='DESELECT')
            for ob in bpy.data.objects:
                for mod in ob.modifiers:
                    if mod.type == 'BEVEL':
                        mod.show_viewport = False
                        ob.select = True
                        bpy.ops.object.shade_flat()
            bpy.ops.object.select_all(action='DESELECT')
            for ob in sel:
                ob.select = True
        except:
            pass
        if len(bpy.context.screen.areas) < 3:
            bpy.ops.screen.screen_full_area() 
        if bpy.context.screen.name in {'Blender','Hacker'}:
            v3d_list = [area for area in bpy.context.screen.areas if area.type == 'VIEW_3D']
            if v3d_list:
                if len(v3d_list) > 1:
                    smallest_area = min(v3d_list, key=lambda area: area.width * area.height)
                    smallest_area.spaces.active.viewport_shade = 'BOUNDBOX'
                largest_area = max(v3d_list, key=lambda area: area.width * area.height)
                largest_area.spaces.active.show_backface_culling = True
    if self.zbFastMode == False:
        ren.use_simplify = False
        scene.tool_settings.sculpt.show_low_resolution = False
        try: 
            ob = bpy.context.active_object
            for mod in ob.modifiers:
                if mod.type == 'MULTIRES':
                    mod.show_viewport = True
                    break
        except:
            pass
        for lamp in bpy.data.lamps:
            if lamp.type != 'HEMI':
                if lamp.shadow_buffer_size > 0:
                    lamp.shadow_buffer_size = wm.zbLampBufferSize
        try: 
            sel = bpy.context.selected_objects
            bpy.ops.object.select_all(action='DESELECT')
            for ob in bpy.data.objects:
                for mod in ob.modifiers:
                    if mod.type == 'BEVEL':
                        mod.show_viewport = True
                        ob.select = True
                        bpy.ops.object.shade_smooth()
            bpy.ops.object.select_all(action='DESELECT')
            for ob in sel:
                ob.select = True
        except:
            pass
        if len(bpy.context.screen.areas) < 3:
            bpy.ops.screen.screen_full_area()            
        for screen in bpy.data.screens:
            for area in screen.areas:                
                if area.type == 'VIEW_3D':
                    if area.spaces.active.viewport_shade == 'BOUNDBOX':
                        area.spaces.active.viewport_shade = 'MATERIAL'
                        area.spaces.active.show_backface_culling = False
def fu9(ob):
    scene = bpy.context.scene
    ob.update_from_editmode()
    seamsUsed = False
    mesh = ob.data
    if ob.data.uv_textures:
        print('Used',ob.name+"'s existing uv map")
    else:
        for e in mesh.edges:
            if e.use_seam:
                seamsUsed = True
                break
        if seamsUsed:
            if bpy.context.mode != 'EDIT_MESH':
                bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.uv.unwrap()
            bpy.ops.object.editmode_toggle()
        else: 
            if scene.zbUseLightMap:
                bpy.ops.uv.lightmap_pack(PREF_MARGIN_DIV=0.3)
            else:
                bpy.ops.uv.smart_project(island_margin = 0.03, angle_limit = 15)
def fu10():
    try:
        ob = bpy.context.active_object
        mat = ob.active_material
        img = mat.active_texture.image
        x = -1
        for slot in mat.texture_paint_images:
            x += 1
            if slot == img:
                mat.paint_active_slot = x
                break
    except:
        pass
    return
def fu11(context,tn):
    try:
        ob = bpy.context.active_object
        me = ob.data
        mat = ob.active_material
        mat.active_texture_index = tn
        ts = mat.texture_slots[tn]
        try:  
            ts.use = True
        except:
            pass
        if not me.uv_textures:
            bpy.ops.mesh.uv_texture_add()
        if ts.texture_coords  == 'UV':
            if ts.uv_layer:
                uvtex = me.uv_textures[ts.uv_layer]
            else:
                uvtex = me.uv_textures.active
                me.uv_textures.active= uvtex
        else:
            uvtex = me.uv_textures.active
        uvtex = uvtex.data.values()
        img = ts.texture.image
        m_id = ob.active_material_index
        if img:
            for f in me.polygons:
                if f.material_index == m_id:
                    uvtex[f.index].image = img
        else:
            for f in me.polygons:
                if f.material_index == m_id:
                    uvtex[f.index].image = None
        fu10()
        me.update()
    except:
        pass
    try:
        if "color" in img.name.lower():
            node = mat.node_tree.nodes['Image Texture zbColor']
        if "bump" in img.name.lower():
            node = mat.node_tree.nodes['Image Texture zbBump']
        if "specular" in img.name.lower():
            node = mat.node_tree.nodes['Image Texture zbSpecular']
        if "glow" in img.name.lower():
            node = mat.node_tree.nodes['Image Texture zbGlow']
        if "alpha_mask" in img.name.lower():
            node = mat.node_tree.nodes['Image Texture zbAlpha_Mask']
        node.image = img
        node_tree = bpy.data.materials[mat.name].node_tree
        node_tree.nodes.active = node
        me.update()
    except:
        pass
    return
class cl10(bpy.types.Operator):
    bl_idname =i_0[34]
    bl_label =i_0[35]
    bl_description =i_0[36]
    tex_index = IntProperty(name = 'tex_index', default = 0)
    @classmethod
    def poll(cls, context):
        return context.active_object != None
    def execute(self, context):
        tn = self.tex_index
        fu11(context, tn)
        return {'FINISHED'}
class cl11(bpy.types.Operator):
    bl_idname =i_0[37]
    bl_label =i_0[38]
    bl_description =i_0[39]
    def modal(self, context, event):
        paint = bpy.context.mode.startswith('PAINT_TEXTURE')
        weight = bpy.context.mode.startswith('PAINT_WEIGHT')
        vertex = bpy.context.mode.startswith('PAINT_VERTEX')
        aType = bpy.context.area.type
        wm = bpy.context.window_manager
        if event.value == 'RELEASE':
            if paint or aType == 'IMAGE_EDITOR':
                brush = bpy.context.tool_settings.image_paint.brush
                brushBlend = wm.zbLastBrushBlend
                if brushBlend == "ERASE_ALPHA":
                    brushBlend = "MIX"
                try:
                    bpy.context.tool_settings.image_paint.brush.blend = brushBlend
                except:
                    pass
                if brush is not None:
                    if 'Mask' in brush.name:
                        brush.weight = 1
            if weight:
                brush = bpy.context.tool_settings.weight_paint.brush
                brush.vertex_tool = 'ADD'
            if vertex:
                brush = bpy.context.tool_settings.vertex_paint.brush
                brush.vertex_tool = 'MIX'
                if event.ctrl is False:
                    brush.color = (0,0,0)                        
            return {'FINISHED'}
        return {'RUNNING_MODAL'}
    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        paint = bpy.context.mode.startswith('PAINT_TEXTURE')
        weight = bpy.context.mode.startswith('PAINT_WEIGHT')
        vertex = bpy.context.mode.startswith('PAINT_VERTEX')
        aType = bpy.context.area.type
        wm = bpy.context.window_manager
        try:
            if paint or aType == 'IMAGE_EDITOR':
                mat = bpy.context.active_object.active_material
                img = mat.active_texture.image
                brush = bpy.context.tool_settings.image_paint.brush
                brushBlend = brush.blend
                wm.zbLastBrushBlend = brushBlend
                if 'Mask' in brush.name:
                    brush.weight = 0
                else:
                    if 'Bump' in img.name:
                        brush.blend = 'SUB'
                    else:
                        brush.blend = 'ERASE_ALPHA'
            if weight:
                brush = bpy.context.tool_settings.weight_paint.brush
                brush.vertex_tool = 'SUB'
            if vertex:
                brush = bpy.context.tool_settings.vertex_paint.brush
                if event.ctrl:
                    brush.vertex_tool = 'BLUR'
                else:                                        
                    brush.vertex_tool = 'MIX'  
                    brush.color = (1,1,1)
        except:
            pass
        if paint:
            bpy.ops.paint.image_paint('INVOKE_DEFAULT')
        if weight:
            bpy.ops.paint.weight_paint('INVOKE_DEFAULT')
        if vertex:
            bpy.ops.paint.vertex_paint('INVOKE_DEFAULT')
        return {'RUNNING_MODAL'}
class cl12(bpy.types.Operator):
    bl_idname =i_0[40]
    bl_label =i_0[41]
    bl_description =i_0[42]
    tex_move_up = IntProperty(default = 0)
    tex_move_down = IntProperty(default = 0)
    def execute(self, context):
        try:
            ob = bpy.context.active_object
            mat = ob.active_material
            slots = mat.texture_slots
            index = mat.active_texture_index
            ts = slots[index]
            ctx = bpy.context.copy()
            ctx['texture_slot'] = ts
        except:
            pass
        moveValue = 0
        moveType = "NONE"
        if self.tex_move_up == 1:
            if index > 0:
                moveType = "UP"
                moveValue = -1
        if self.tex_move_down == 1:
            if index < 17:
                moveType = "DOWN"
                moveValue = 1
        if moveType != "NONE":
            safety = 0
            while safety < 16:
                safety += 1
                try:
                    tex = slots[mat.active_texture_index + moveValue]
                    if tex is None or tex.texture_coords != 'UV':
                        bpy.ops.texture.slot_move(ctx, type= moveType)
                    else:
                        bpy.ops.texture.slot_move(ctx, type= moveType)
                        self.tex_move_down = 0
                        self.tex_move_up = 0
                        safety = 17
                except:
                    pass
            fu10()
        return {'FINISHED'}
class cl13(bpy.types.Operator):
    bl_idname =i_0[43]
    bl_label =i_0[44]
    bl_description =i_0[45]
    tex_kill = IntProperty(name="tex_kill", default = 0)
    def execute(self, context):
        ob = bpy.context.active_object
        mat = ob.active_material
        ts = mat.texture_slots[self.tex_kill]
        texName = mat.texture_slots[self.tex_kill].name
        if ts.use_map_alpha == True:
            mat.use_transparency = False
        if ts.use_map_color_spec == True:
            mat.specular_color = (1, 1, 1)
            mat.specular_intensity = 0.5
        try: 
            if "specular" in ts.texture.image.name.lower():
                node = mat.node_tree.nodes['Image Texture zbSpecular']
                node = mat.node_tree.nodes['Math zbSpecular']
                node.inputs[1].default_value = 0
            if "glow" in ts.texture.image.name.lower():
                node = mat.node_tree.nodes['Image Texture zbGlow']
                node = mat.node_tree.nodes['Math zbGlow']
                node.inputs[1].default_value = 0
            if "alpha_mask" in ts.texture.image.name.lower():
                node = mat.node_tree.nodes['Image Texture zbAlpha_Mask']
                node.mute = True
            if "transparent" in ts.texture.image.name.lower():
                if len(mat.texture_slots.items()) == 1:
                    node = mat.node_tree.nodes['Image Texture zbColor']
                    node.mute = True
        except:
            pass
        try: 
            if self.tex_kill > -1:
                if ts:
                    if mat.texture_slots[self.tex_kill]:
                        imgDie = mat.texture_slots[self.tex_kill].texture.image
                        try:
                            bpy.data.images.remove(imgDie, do_unlink = True)
                        except:
                            if imgDie.users:
                                imgDie.user_clear()
                            bpy.data.images.remove(imgDie)
                        ts.texture = None
                        mat.texture_slots.clear(self.tex_kill)
                if self.tex_kill == mat.active_texture_index:
                    x = 17
                    while x > -1:
                        if mat.texture_slots[x]:
                            bpy.ops.object.zb_set_active_layer(tex_index=x)
                            break
                        x -= 1
        except:
            pass        
        fu0()
        if hasattr(mat.node_tree,'nodes'):
            nodes = mat.node_tree.nodes
            if 'Image Texture zbColor' in nodes:                
                colNode = nodes['Image Texture zbColor']
                if not colNode.image:
                    for slot in mat.texture_slots:
                        try:
                            if slot is not None:
                                if slot.texture:                                
                                    if slot.texture.type == 'IMAGE':
                                        if slot.texture.image:
                                            img = slot.texture.image
                                            if 'Color' in slot.texture.image.name:
                                                colNode.image = img
                                                break
                        except:
                            pass
        return {'FINISHED'}
class cl14(bpy.types.Operator):
    bl_idname =i_0[46]
    bl_label =i_0[47]
    bl_description =i_0[48]
    def execute(self,context):
        for img in bpy.data.images:
            img.reload()
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                area.tag_redraw()
        return{'FINISHED'}
def fu12(self,context):
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    scene.zbSaveToHardDrive = True
    wm.zbNewSavePath = True
    return
def zbSaveType(self,context):
    wm = bpy.context.window_manager
    wm.zbNewSavePath = True
    return
class cl15(bpy.types.Operator):
    bl_idname =i_0[49]
    bl_label =i_0[50]
    bl_description =i_0[51]
    save_only_active = bpy.props.BoolProperty()
    def execute(self, context):
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        mode = bpy.context.mode              
        userMsg = ''
        aType = 0
        try:
            aType = bpy.context.area.type
        except:
            pass  
        try:
            if hasattr(scene,'active_object') is False:
                for obj in bpy.context.selected_objects:
                    scene.objects.active = obj
                    break
            ob = bpy.context.active_object
            mat = ob.active_material
            if mat:
                if scene.zbSaveToHardDrive:
                    if len(wm.zbSaveImagePath) < 3:
                        for ts in mat.texture_slots:
                            if ts is not None:
                                try:
                                    if ts.texture_coords == 'UV':
                                        if ts.texture.type == 'IMAGE':
                                            try:
                                                imgPath = bpy.path.abspath(ts.texture.image.filepath)
                                                if "\\..\\" not in imgPath:
                                                    imgDir = os.path.dirname(imgPath)
                                                    if len(imgDir) > 3:
                                                        wm.zbSaveImagePath = imgDir + "\\"
                                                        break
                                                    break
                                            except:
                                                pass
                                except:
                                    pass
                        if len(wm.zbSaveImagePath) < 3:
                            for ob in bpy.data.objects:
                                if ob.active_material:
                                    for ts in ob.active_material.texture_slots:
                                        try:
                                            if ts.texture_coords == 'UV':
                                                if ts.texture.image:
                                                    imgPath = bpy.path.abspath(ts.texture.image.filepath)
                                                    if len(imgPath) > 3:
                                                        if "\\..\\" not in imgPath:
                                                            imgDir = os.path.dirname(imgPath)
                                                            if len(imgDir) > 3:
                                                                wm.zbSaveImagePath = imgDir + "\\"
                                                                break
                                        except:
                                            pass
                    if len(wm.zbSaveImagePath) < 3:
                        userMsg = ("You must select a folder before saving to hard drive")
                    else:
                        for ts in mat.texture_slots:
                            if ts is not None: 
                                try:
                                    ts.texture.image
                                    texName = ts.texture.name
                                    imgName = ts.texture.image.name
                                    types = ['Color', 'Bump', 'Specular', 'Glow',
                                            'Transparent', 'Alpha_Mask']
                                    for type in types:         
                                        if type.lower() in imgName.lower():
                                            if type.lower() in texName.lower():
                                                newName = texName
                                            else:
                                                newName = texName + type                                                                                                                    
                                    ts.texture.image.name = newName                                    
                                except:
                                    pass                            
                        newSaveState = wm.zbNewSavePath
                        zbsip = wm.zbSaveImagePath
                        wm.zbSaveImagePath = bpy.path.abspath(zbsip)
                        wm.zbNewSavePath = newSaveState
                        aType = bpy.context.area.type
                        bpy.context.area.type = 'IMAGE_EDITOR'
                        i = 0
                        for slot in mat.texture_paint_slots:
                            newSaveLocation = True
                            img = mat.texture_paint_images[i]
                            mat.paint_active_slot = i
                            if "\\..\\" in img.filepath:
                                img.filepath_raw = ""
                            if len(img.filepath) > 3:
                                if wm.zbNewSavePath == False:
                                    print("Saving image at it's previous save location")
                                    newSaveLocation = False
                                    bpy.ops.image.save()
                            if self.save_only_active:
                                if not img.packed_file:
                                    newSaveLocation = False
                            if newSaveLocation:
                                print('Saving image using selected folder location')
                                override = bpy.context.copy()
                                override['edit_image'] = img
                                bpy.ops.image.pack(override, as_png = True)
                                ff = wm.zbSaveType
                                ff = ff.replace(".","")
                                if ff == 'TGA':
                                    ff = 'TARGA'
                                img.file_format = ff
                                path = bpy.path.abspath(wm.zbSaveImagePath)
                                imgPath = path + img.name + wm.zbSaveType
                                bpy.ops.image.save_as(filepath = imgPath)
                                if img.packed_file:
                                    bpy.ops.image.unpack(method = 'WRITE_ORIGINAL')
                                    img.filepath_raw = bpy.path.abspath(imgPath)
                                try: 
                                    blendFilePath = bpy.data.filepath
                                    blendFileDir = os.path.dirname(blendFilePath)
                                    imgToX = os.path.join(blendFileDir, img.name)
                                    if os.path.exists(imgToX):
                                        os.remove(imgToX)
                                except:
                                    pass                                
                            i += 1 
                    if aType:
                        bpy.context.area.type = aType
                else:
                    if self.save_only_active:
                        layersAmount = 0
                        for ts in mat.texture_slots:
                            if ts is not None:
                                try:
                                    if ts.texture.type == 'IMAGE':
                                        if ts.texture_coords  == 'UV':
                                            image = ts.texture.image
                                            override = bpy.context.copy()
                                            override['edit_image'] = image
                                            bpy.ops.image.pack(override, as_png = True)
                                            layersAmount += 1
                                except:
                                    pass
                        if mode != 'PAINT_TEXTURE':
                            userMsg = "Paint layers saved."
                    else:
                        layersAmount = 0
                        for ob in bpy.data.objects:
                            mat = ob.active_material
                            if mat:
                                for ts in mat.texture_slots:
                                    if ts is not None:
                                        try:
                                            if ts.texture.type == 'IMAGE':
                                                if ts.texture_coords  == 'UV':
                                                    image = ts.texture.image
                                                    override = bpy.context.copy()
                                                    override['edit_image'] = image
                                                    bpy.ops.image.pack(override, as_png = True)
                                                    layersAmount += 1
                                        except:
                                            pass                                        
                        userMsg = "All paint layers saved."
        except:
            userMsg = "Had trouble saving all images."
        if userMsg:
            self.report({'INFO'}, userMsg)
        if wm.zbNewSavePath:
            wm.zbNewSavePath = False
        return {'FINISHED'}
class cl16(bpy.types.Menu):
    bl_label =i_0[52]
    bl_idname =i_0[53]
    def draw(self, context):
        scene = bpy.context.scene
        re = scene.render.engine
        wm = bpy.context.window_manager
        layout = self.layout
        col = layout.column()
        col.prop(scene, 'zbAutoSaveLayers', text='Autosave Layers')
        col.prop(scene, 'zbSaveWhenSave', text= 'Autosave (with file)')
        col.prop(scene, 'zbUseLightMap', text= 'Use Lightmap UVs')
        col.prop(scene, 'zbLoadImgSculpt', text='Texture & Sculpt')
        col.prop(scene, 'zbAutoConvertLamps', text='Auto Convert Lamps')
class cl17(bpy.types.Menu):
    bl_label =i_0[54]
    bl_idname =i_0[55]
    def draw(self, context):
        re = bpy.context.scene.render.engine
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        ncIcon = 'LINK'   
        hIcon = 'INLINK'
        layout = self.layout
        col = layout.column()
        if fu20():
            try:
                mat = bpy.context.active_object.active_material
            except:
                mat = 0
            col.menu("menu.zb_system_options", text = 'ZB Options', icon=hIcon)
            col.prop(scene, "zbGoCycles", text="Use Cycles")
            if re == 'CYCLES':
                col.prop(scene, "zbQuickLights", text = "Quick Lights")
            col.prop(scene, "zbFastMode", text="Fast Mode")
            if re != 'CYCLES':
                col.prop(scene, "zbDisableShadows", text = "Disable Shadows")
            col.separator()
            col.menu("menu.zb_material_options_menu", text = 'Material Options',
            icon=hIcon) 
            col.separator()
            col.operator("object.zb_save_layers", text="Save My Layers",
            icon =ncIcon)
            col.prop(wm, "zbUseBrushColor", text="Color New Layers")
            col.prop(scene, "zbImgSize", text='        New Layer Size')
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
    bl_idname =i_0[56]
    bl_label =i_0[57]
    bl_description =i_0[58]
    def execute(self,context):
        ob = bpy.context.active_object
        mat = ob.active_material
        try: 
            if ob.dupli_type == 'GROUP':
                oldName = ob.dupli_group.name
                newGroupSel = []
                empty = 0
                bpy.ops.object.duplicates_make_real()
                sel = bpy.context.selected_objects
                for ob in sel:
                    if ob.type == 'EMPTY':
                        empty = ob
                        ob.select = False
                        newGroupSel = bpy.context.selected_objects
                bpy.ops.object.select_all(action='DESELECT')
                for ob in bpy.data.objects:
                    if ob.type == 'EMPTY':
                        if 'group' in ob.name:
                            ob.select = True
                bpy.ops.object.delete()
                for ob in newGroupSel:
                    ob.select = True
                    ob.data = ob.data.copy()
        except:
            pass
        sel = bpy.context.selected_objects
        mode = bpy.context.mode
        if 'PAINT' in mode:
            bpy.ops.object.mode_set(mode='OBJECT')
        for ob in sel:
            bpy.ops.object.select_all(action='DESELECT')
            bpy.context.scene.objects.active = ob
            ob.select = True
            mat = ob.active_material
            if mat:
                if mat.users < 2:
                    ob.active_material = mat.copy()
                bpy.ops.object.zb_save_layers(save_only_active=True)
                slot = ob.active_material_index
                newMat = ob.active_material.copy()
                ob.material_slots[slot].material = newMat
                mat = bpy.context.active_object.active_material
                for slot in mat.texture_slots:
                    try:
                        newTex = slot.texture.copy()
                        newImg = slot.texture.image.copy()
                        slot.texture = newTex
                        slot.texture.image = newImg
                    except:
                        pass
                try: 
                    tn = mat.active_texture_index
                    fu11(context, tn)
                except:
                    pass
        if mode == 'OBJECT':
            bpy.ops.object.select_all(action='DESELECT')
            for ob in sel:
                ob.select = True
        fu1(mode)
        bpy.context.scene.update_tag()
        bpy.context.scene.update()
        return{'FINISHED'}
def fu13(self, context):
    scene = bpy.context.scene
    wm = bpy.context.window_manager
    brushSettings = scene.tool_settings.image_paint
    mat = bpy.context.object.active_material
    if wm.zbPaintThrough == True:
        brushSettings.use_occlude = False
        brushSettings.use_normal_falloff = False
        brushSettings.use_backface_culling = False
    else:
        brushSettings.use_occlude = True
        brushSettings.use_normal_falloff = True
        brushSettings.use_backface_culling = True
    if scene.zbDisableShadows:
        for lamp in bpy.data.lamps:
            uses = False
            try:
                if lamp.shadow_method == 'RAY_SHADOW':
                    uses = True
                if lamp.shadow_method == 'BUFFER_SHADOW':
                    uses = True
            except:
                pass
            if uses:
                lamp.shadow_method = 'NOSHADOW'
    else:
        for lamp in bpy.data.lamps:
            try:
               lamp.shadow_method = 'RAY_SHADOW'
            except:
                pass
def fu14(self,context):
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    mode = bpy.context.mode
    sel = bpy.context.selected_objects
    if self.zbQuickLights:            
        world = scene.world
        if not world:
            bpy.ops.world.new()                
            world = bpy.data.worlds[0]
            scene.world = world
        worldWasUsingMist = False
        if world.mist_settings.use_mist:
            worldWasUsingMist = True
        try: 
            wName = scene.world.name
            scene.zbLastWorld = wName
            if 'ZB Quick Lights' in wName:
                try:
                    scene.zbLastWorld = bpy.data.worlds[2].name
                except:
                    scene.zbLastWorld = bpy.data.worlds[0].name
        except:
            w = bpy.context.data.worlds.new('Basic World')
            scene.zbLastWorld = w.name
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
            activeOb = bpy.context.active_object
            bpy.ops.object.select_all(action='DESELECT')
        except:
            pass
        needWorld = False
        for world in bpy.data.worlds:
            if 'ZB Quick Lights' in world.name:
                needWorld = False
                zbQuickLights = world
                scene.world = bpy.data.worlds[world.name]
                break
            else:
                needWorld = True
        if needWorld:
            zbQuickLights = bpy.data.worlds.new("ZB Quick Lights")
            zbQuickLights.horizon_color = [0,0,0]
            zbQuickLights.zenith_color = [0,0,0]
            zbQuickLights.ambient_color = [0,0,0]
            scene.world = zbQuickLights
            zbQuickLights.use_nodes = True
            zbQuickLights.use_fake_user = True
            bg = zbQuickLights.node_tree.nodes['Background']
            bg.inputs[0].default_value = (0,0,0,1)
        needPlanes = False
        if 'zbCyclesLight' not in bpy.data.objects:
            needPlanes = True
        if needPlanes:
            scene.cursor_location.xyz = [0,0,0]
            bpy.ops.mesh.primitive_plane_add()
            bpy.context.active_object.name = "zbCyclesLight"
            ob = bpy.context.active_object
            zbCyclesLight = bpy.context.active_object
            zbCyclesLight.scale = [17,17,17]
            zbCyclesLight.location.z = 100
            zbCyclesLight.active_material = bpy.data.materials.new("zbCyclesLight")
            bpy.ops.object.modifier_add(type='SUBSURF')
            zbCyclesLight.modifiers["Subsurf"].levels = 3
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subsurf")
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.dissolve_limited()
            bpy.ops.object.mode_set(mode='OBJECT')
            mat = ob.active_material
            mat.use_nodes = True
            mat.node_tree.nodes.clear()
            nodeEmission = mat.node_tree.nodes.new(type = 'ShaderNodeEmission')
            nodeEmission.inputs[1].default_value = 20
            nodeOutput = mat.node_tree.nodes.new(type = 'ShaderNodeOutputMaterial')
            mat.node_tree.links.new(nodeEmission.outputs['Emission'],
            nodeOutput.inputs['Surface'])
            nodeOutput.location = (250,0)
            ob.cycles_visibility.camera = False
            ob.cycles_visibility.shadow = False
            bpy.ops.object.duplicate_move()
            ob = bpy.context.active_object
            ob.location.xyz = [-75,-65,15]
            ob.rotation_euler.y = 115
            ob.rotation_euler.z = 45
            ob.scale = [15,15,15]
            bpy.ops.object.duplicate_move()
            ob = bpy.context.active_object
            ob.location.xyz = [75,-65,15]
            ob.rotation_euler.y = -115
            ob.rotation_euler.z = -45
            bpy.ops.object.duplicate_move()
            ob = bpy.context.active_object
            ob.location.xyz = [0,100,15]
            ob.rotation_euler[2] = 1.5708
            for ob in bpy.data.objects:
                if "zbCyclesLight" in ob.name:
                    scene.objects.active = ob
                    ob.select = True
            scene.objects.active = bpy.data.objects["zbCyclesLight"]
            bpy.ops.object.parent_set(type='OBJECT')
        for ob in bpy.data.objects:
            if "zbCyclesLight" in ob.name:               
                ob.select = False
                ob.hide = True
        try:  
            scene.objects.active = activeOb
            scene.objects.active.select = True
        except:
            pass
        try: 
            if worldWasUsingMist:
                bpy.ops.object.sf_cam_options(func="mist")
        except:
            pass
    else: 
        if scene.zbLastWorld:
            lastWorld = scene.zbLastWorld
            if lastWorld in bpy.data.worlds:
                scene.world = bpy.data.worlds[lastWorld]
            else:
                for world in bpy.data.worlds:
                    if 'ZB Quick Lights' not in world.name:
                        scene.world = world
                        break          
            if scene.world.name == 'ZB Quick Lights':
                bpy.ops.world.new()
                for world in bpy.data.worlds:
                    if world.name != 'ZB Quick Lights':
                        scene.world = world
                        break
        try:
            activeOb = bpy.context.active_object
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            for mat in bpy.data.materials:
                if "zbCyclesLight" in mat.name:
                    try:
                        bpy.data.materials.remove(mat, do_unlink = True)
                    except:
                        if mat.users:
                            mat.user_clear()
                        bpy.data.materials.remove(mat)
        except:
            pass
        try: 
            if 'ZB Quick Lights' in bpy.data.worlds:
                x = bpy.data.worlds["ZB Quick Lights"]
                try:
                    bpy.data.worlds.remove(x, do_unlink = True)
                except:
                    if x.users:
                        x.user_clear()
                    bpy.data.worlds.remove(x)
        except:
            pass
        for ob in bpy.data.objects:
            if "zbCyclesLight" in ob.name:
                scene.objects.unlink(ob)
        fu0()
        try: 
            bpy.ops.object.select_all(action='DESELECT')
            scene.objects.active = activeOb
            scene.objects.active.select = True
        except:
            pass
    try: 
        fu1(mode)
    except:
        pass
    for ob in sel:
        ob.select = True
class cl19(bpy.types.Operator):
    bl_idname =i_0[59]
    bl_label =i_0[60]
    bl_description =i_0[61]
    resetLayer = bpy.props.BoolProperty(default = True) 
    def execute(self, context):
        wm = bpy.context.window_manager
        scene = bpy.context.scene
        mode = bpy.context.mode
        userMsg = ''
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')        
        ob = bpy.context.active_object
        mesh = ob.data
        for obj in bpy.context.selected_objects:
            scene.objects.active = obj
            if hasattr(obj.data,'uv_textures'):
                for uv in obj.data.uv_textures:
                    bpy.ops.mesh.uv_texture_remove()        
        fu9(ob)
        if self.resetLayer:
            layers = len(ob.active_material.texture_paint_images)            
            if layers == 1:
                layer = 0
                for ts in ob.active_material.texture_slots:
                    try:
                        ts.texture.image
                        break
                    except:
                        pass
                    layer += 1
                bpy.ops.object.zb_delete_texture(tex_kill=layer)
                bpy.ops.object.zb_paint_color()
                userMsg = "Reset uvs and layer (this will also reset your image if only one layer)"
        fu1(mode)
        if userMsg:
            self.report({'INFO'}, userMsg)            
        return{'FINISHED'}
class cl20(bpy.types.Operator):
    bl_idname =i_0[62]
    bl_label =i_0[63]
    bl_description =i_0[64]
    vpShade = bpy.props.StringProperty(default='MATERIAL')    
    def execute(self, context):
        wm = bpy.data.window_managers["WinMan"]
        scene = bpy.context.scene
        mode = bpy.context.mode
        re = scene.render.engine
        farthestLeft = 0
        farthestLeftShade = 0
        if bpy.context.screen.name == 'Shader':
            v3d_list = [area for area in bpy.context.screen.areas if area.type == 'VIEW_3D']         
            if v3d_list:
                farthestRight = max(v3d_list, key=lambda area: area.x)               
                sd = farthestRight.spaces[0]
                farthestLeft = min(v3d_list, key=lambda area: area.x)
                farthestLeftShade = farthestLeft.spaces[0].viewport_shade 
                farthestLeft.spaces[0].viewport_shade = 'BOUNDBOX'                    
        else:
            sd = bpy.context.space_data
        turnOn = False
        if sd.viewport_shade != 'RENDERED':
            turnOn = True
        if bpy.context.screen.name == 'Shader':
            if scene.cycles.preview_pause:
                turnOn = True
        if turnOn:                  
            if re == 'CYCLES':
                try: 
                    if scene.cycles.feature_set == 'EXPERIMENTAL':                    
                        bpy.ops.object.editmode_toggle()
                        bpy.ops.object.editmode_toggle()
                except:
                    pass
            if farthestLeft == 0: 
                self.vpShade = sd.viewport_shade  
            else:
                if farthestLeftShade:
                    self.vpShade = farthestLeftShade
            if mode == 'PARTICLE':
                bpy.ops.object.mode_set(mode='OBJECT')
                wm.zbLastObjectMode = mode                
                self.report({'INFO'}, 
                "Blender does not support render preview in particle mode (temporarily switched modes).")
            scene.cycles.preview_pause = False
            if re == 'CYCLES':
                if scene.zbQuickLights:
                    try: 
                        scnLight = bpy.data.objects['-Scene Light']
                        shadows  = bpy.data.objects['-Shadows']                        
                        scnLight.hide_render = True
                        shadows.hide_render = True                        
                        shadows.hide = True
                        scnLight.hide = True
                    except:
                        pass                
            for ob in bpy.data.objects:
                if ob.type == 'LAMP':
                    if re != 'CYCLES':
                        if not ob.hide_render:
                            ob.hide = False
                    else:
                        if scene.zbAutoConvertLamps:
                            if not ob.hide_render:
                                ob.hide = False            
            if re == 'CYCLES':
                if scene.zbQuickLights:
                    for ob in bpy.data.objects:
                        if 'zbCyclesLight' in ob.name:
                            ob.hide = False
                            for i in range(20):
                                ob.layers[i] = True   
            try: 
                sd.use_render_border = True
                sd.viewport_shade = 'RENDERED'
            except:
                pass
        else: 
            if re == 'CYCLES':                
                if scene.zbQuickLights == True:
                    for ob in bpy.data.objects:
                        if "zbCyclesLight" in ob.name:
                            ob.hide = True
                            for i in range(19):                                
                                ob.layers[i] = False 
                            ob.layers[0] = True
                            ob.layers[19] = False
            for ob in bpy.data.objects:
                if ob.type == 'LAMP':
                    if "Shadows" in ob.name:
                        ob.hide = True
                    if "-Scene Light" in ob.name:
                        ob.hide = True
            if bpy.context.screen.name != 'Shader':                
                sd.viewport_shade = self.vpShade                
            else:
                if re != 'CYCLES':
                    sd.viewport_shade = self.vpShade
            sd.use_render_border = False
            scene.cycles.preview_pause = True
            if farthestLeft != 0:
                farthestLeft = min(v3d_list, key=lambda area: area.x)                 
                farthestLeft.spaces[0].viewport_shade = self.vpShade             
            if wm.zbLastObjectMode == 'PARTICLE':
                wm.zbLastObjectMode = ''
                bpy.ops.object.mode_set(mode='PARTICLE_EDIT')
        fu1(mode)    
        return{'FINISHED'}
def texLayerAdder(layerType, texCol, texOpas, alphaChoice,
    normalChoice):
    try: 
        fontState = bpy.context.user_preferences.system.use_translate_new_dataname
        bpy.context.user_preferences.system.use_translate_new_dataname = False
    except:
        pass
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    sd = bpy.context.space_data
    re = bpy.context.scene.render.engine
    ob = bpy.context.active_object
    mat = ob.active_material
    try:
        if layerType == "Transparent" or layerType == "Alpha_Mask":
            ob.show_transparent = True
            if mat:
                n = 0
                for ts in mat.texture_slots:
                    if ts is not None:
                        try:
                            if ts.use_map_alpha == True:
                                ts.texture.image = None
                                ts.texture = None
                                mat.texture_slots.clear(n)
                        except:
                            pass
                    n += 1
            try:
                if layerType == 'Alpha_Mask':
                    for node in bpy.data.materials[mat.name].node_tree.nodes:
                        if 'zbTransparent' in node.name:
                            tree = bpy.data.materials[mat.name].node_tree
                            mixed5 = tree.nodes['Mixed5']
                            mixed6 = tree.nodes['Mixed6']
                            mat.node_tree.links.new(mixed5.outputs['Shader'],
                            mixed6.inputs[1])
                            nodeColor = tree.nodes['Image Texture zbColor']
                            for img in bpy.data.images:
                                if "Color" in img.name:
                                    if ob.name[:4] in img.name:
                                        nodeColor.image = img
                                        break
            except:
                pass
        if mat is None or "None" in mat.name:
            mat = bpy.data.materials.new(ob.name)
            mat.diffuse_shader = 'LAMBERT'
            mat.darkness = 0.8
            mat.strand.use_tangent_shading = False
            mat.strand.root_size = 2.5
            mat.strand.tip_size = 0.25
            mat.strand.width_fade = 0.5
            ob.active_material = mat
        try:
            node = mat.node_tree.nodes['Mixed1']
        except:
            mat.use_nodes = True
            mat.node_tree.nodes.clear()
            mixedTotal = 8 
            locX = 250 
            mixedList =[] 
            for mixed in range(1,mixedTotal + 1):
                x = mixed
                mixed = mat.node_tree.nodes.new(type="ShaderNodeMixShader")
                mixed.name = "Mixed" + str(x)
                mixed.label = mixed.name
                mixedList.append(mixed)
                mixed.inputs['Fac'].default_value = 0
                locX += 250
                mixed.location = (locX,0)
            nodeOutput = mat.node_tree.nodes.new(type = 'ShaderNodeOutputMaterial')
            nodeOutput.location = (locX + 250,0) 
            node = mat.node_tree.nodes.new(type = 'ShaderNodeMath')
            node.label = node.name + ' zbDisplace'
            node.name = node.label
            nodeMath = node
            nodeMath.location = (locX + 250,-120)
            mat.node_tree.links.new(nodeMath.outputs['Value'],
            nodeOutput.inputs['Displacement'])
            x = 0
            for mixed in mixedList:
                x += 1
                if x < mixedTotal:
                    mixedNext = mixedList[x] 
                    mat.node_tree.links.new(mixed.outputs['Shader'],
                    mixedNext.inputs['Shader'])
                else:
                    mat.node_tree.links.new(mixed.outputs['Shader'],
                    nodeOutput.inputs['Surface'])
                if "5" in mixed.name:
                    mat.node_tree.links.new(mixed.outputs['Shader'],
                    mixedNext.inputs[2])
        xAndY = round(scene.zbImgSize)
        layerName = ob.name[:4] 
        img = bpy.data.images.new(layerName + layerType, xAndY, xAndY, alpha= alphaChoice)
        override = bpy.context.copy()
        override['edit_image'] = img
        bpy.ops.image.pack(override, as_png = True)
        img.pixels[:] = (texCol, texCol, texCol, texOpas) * xAndY * xAndY
        try: 
            brushCol = bpy.context.tool_settings.image_paint.brush.color
            if wm.zbUseBrushColor:
                l = layerType
                go = 0
                if "Bu" not in l:
                    if "Tr" not in l:
                        if "Ma" not in l:
                            go = 1
                if go:
                    img.pixels[:] = (brushCol.r, brushCol.g, brushCol.b, 1) * xAndY * xAndY
        except:
            pass
        cTexName = layerName + layerType
        cTex = bpy.data.textures.new( name = cTexName, type = 'IMAGE')
        activeTex = -1
        for ts in mat.texture_slots:
            activeTex += 1
            if ts is None:
                break
        mTex = mat.texture_slots.add()
        mTex.texture = cTex
        mTex.texture_coords = 'UV'
        if normalChoice == True:
            mTex.use_map_normal = True
            mTex.bump_method = 'BUMP_MEDIUM_QUALITY'
            mTex.normal_factor = 0.0
        cTex.image = img
        bpy.ops.object.mode_set(mode = 'EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        fu9(ob)
        for uv_face in ob.data.uv_textures.active.data:
            uv_face.image = img
        if sd.viewport_shade != 'TEXTURED':
            sd.viewport_shade = 'MATERIAL'
        try: 
            scene.game_settings.material_mode = 'GLSL'
        except:
            pass
        bpy.ops.object.mode_set(mode = 'TEXTURE_PAINT')
        bleed = 2 
        if xAndY > 512:
            bleed = 5
        if xAndY > 1024:
            bleed = 6
        if xAndY > 2048:
            bleed = 8
        bpy.context.scene.tool_settings.image_paint.seam_bleed = bleed
        bpy.ops.object.zb_set_active_layer(tex_index=activeTex)
        slots = mat.texture_slots
        ts = slots[mat.active_texture_index]
        ctx = bpy.context.copy()
        ctx['texture_slot'] = ts
        x = 0
        while x < 17:
            bpy.ops.texture.slot_move(ctx, type='DOWN')
            x += 1
    except:
        pass
    tn = mat.active_texture_index
    context = bpy.context
    fu11(context,tn)
    if layerType == "Color":
        try:
            nodeTex = mat.node_tree.nodes['Image Texture zbColor']
            nodeTex.mute = False
        except:
            node = mat.node_tree.nodes.new(type = 'ShaderNodeTexImage')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeTex = node
            node = mat.node_tree.nodes.new(type = 'ShaderNodeMixRGB')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeMixRGB = node
            nodeMixRGB.blend_type = 'MIX'
            nodeMixRGB.inputs['Fac'].default_value = 1
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBrightContrast')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBright = node
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBsdfDiffuse')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeDiffuse = node
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBump')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBump = node
            nodeBump.inputs[1].default_value = 0.015
            nodeBump.invert = True
            node = mat.node_tree.nodes.new(type='ShaderNodeRGBToBW')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBW = node
            node = mat.node_tree.nodes.new(type='ShaderNodeBsdfGlossy')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeGloss = node
            node = mat.node_tree.nodes.new(type='ShaderNodeMath')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeMath = node
            nodeMath.inputs[1].default_value = 0
            nodeMath.operation = 'MULTIPLY'
            node = mat.node_tree.nodes.new(type='ShaderNodeEmission')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeEmission = node
            nodeEmission.inputs[1].default_value = 10
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBsdfTransparent')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeAlpha = node
            mat.node_tree.nodes[nodeBump.name].hide = True
            mat.node_tree.nodes[nodeBW.name].hide = True
            mat.node_tree.nodes[nodeGloss.name].hide = True
            mat.node_tree.nodes[nodeMath.name].hide = True
            mat.node_tree.nodes[nodeBright.name].hide = True
            mat.node_tree.nodes[nodeMixRGB.name].hide = True
            nodeTex.location = (-50, 0)
            nodeMixRGB.location = (120, -5)
            nodeBright.location = (120, -55)
            nodeDiffuse.location = (250, 0)
            nodeMath.location = (250, -130)
            nodeBW.location = (250, -170)
            nodeBump.location = (500, -130)
            nodeGloss.location = (500, -170)
            nodeEmission.location = (750,-130)
            nodeAlpha.location = (1000, -130)
            colorMixed1 = mat.node_tree.nodes['Mixed1']
            colorMixed2 = mat.node_tree.nodes['Mixed2']
            colorMixed3 = mat.node_tree.nodes['Mixed3']
            nodeMath2 = mat.node_tree.nodes['Math zbDisplace']
            nodeMath2.inputs[0].default_value = 0
            mat.node_tree.links.new(nodeTex.outputs['Color'], nodeMixRGB.inputs['Color2'])
            mat.node_tree.links.new(nodeMixRGB.outputs['Color'], nodeBright.inputs['Color'])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeDiffuse.inputs['Color'])
            mat.node_tree.links.new(nodeDiffuse.outputs['BSDF'], colorMixed1.inputs['Shader'])
            mat.node_tree.links.new(nodeDiffuse.outputs['BSDF'], colorMixed1.inputs['Shader'])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeBW.inputs['Color'])
            mat.node_tree.links.new(nodeBW.outputs['Val'], nodeMath.inputs[0])
            mat.node_tree.links.new(nodeMath.outputs['Value'], nodeMath2.inputs[0])
            mat.node_tree.links.new(nodeBW.outputs['Val'], nodeGloss.inputs['Color'])
            mat.node_tree.links.new(nodeBW.outputs['Val'], nodeBump.inputs['Strength'])
            mat.node_tree.links.new(nodeBW.outputs['Val'], nodeBump.inputs['Height'])
            mat.node_tree.links.new(nodeBump.outputs['Normal'], nodeGloss.inputs['Normal'])
            mat.node_tree.links.new(nodeGloss.outputs['BSDF'], colorMixed1.inputs[2])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeEmission.inputs['Color'])
            mat.node_tree.links.new(nodeEmission.outputs['Emission'], colorMixed2.inputs[2])
            mat.node_tree.links.new(nodeAlpha.outputs['BSDF'], colorMixed3.inputs[2])
            mat.node_tree.links.new(colorMixed2.outputs['Shader'], nodeAlpha.inputs['Color'])
        nodeTex.image = img
        node_tree = bpy.data.materials[mat.name].node_tree
        node_tree.nodes.active = nodeTex
    if layerType == "Bump":
        try:
            nodeTex = mat.node_tree.nodes['Image Texture zbBump']
        except:
            node = mat.node_tree.nodes.new(type = 'ShaderNodeTexImage')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeTex = node
            nodeTex.color_space = 'NONE'
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBrightContrast')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBright = node
            node = mat.node_tree.nodes.new(type = 'ShaderNodeRGBToBW')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBW = node
            node = mat.node_tree.nodes.new(type='ShaderNodeMath')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            node.inputs[1].default_value = 2.5
            nodeMath = node
            nodeMath.operation = 'MULTIPLY'
            nodeOutput = mat.node_tree.nodes['Material Output']
            nodeMath2 = mat.node_tree.nodes['Math zbDisplace']
            mat.node_tree.links.new(nodeTex.outputs['Color'], nodeBright.inputs['Color'])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeBW.inputs['Color'])
            mat.node_tree.links.new(nodeBW.outputs['Val'], nodeMath.inputs[0])
            mat.node_tree.links.new(nodeMath.outputs['Value'], nodeMath2.inputs[1])
            nodeTex.location = (-50, -260)
            nodeBright.location = (120, -260)
            nodeBW.location = (120, -390)
            nodeMath.location = (285, -260)
        nodeTex.image = img
        node_tree = bpy.data.materials[mat.name].node_tree
        node_tree.nodes.active = nodeTex
        try: 
            brush = bpy.context.tool_settings.image_paint.brush
            brush.color = (1,1,1)
        except:
            pass
    if layerType == "Specular":
        try:
            nodeTex = mat.node_tree.nodes['Image Texture zbSpecular']
            mat.node_tree.nodes['Math zbSpecular'].inputs[1].default_value = 1
        except:
            node = mat.node_tree.nodes.new(type = 'ShaderNodeTexImage')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeTex = node
            node = mat.node_tree.nodes.new(type = 'ShaderNodeMixRGB')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeMixRGB = node
            nodeMixRGB.blend_type = 'MIX'
            nodeMixRGB.inputs['Fac'].default_value = 1
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBrightContrast')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBright = node
            node = mat.node_tree.nodes.new(type='ShaderNodeBsdfGlossy')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeGloss = node
            node = mat.node_tree.nodes.new(type='ShaderNodeRGBToBW')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBW = node
            node = mat.node_tree.nodes.new(type='ShaderNodeMath')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeMath = node
            nodeMath.operation = 'MULTIPLY'
            nodeMath.inputs[1].default_value = 1
            specularMixed5 = mat.node_tree.nodes['Mixed5']
            mat.node_tree.links.new(nodeTex.outputs['Color'], nodeMixRGB.inputs['Color2'])
            mat.node_tree.links.new(nodeMixRGB.outputs['Color'], nodeBright.inputs['Color'])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeBW.inputs['Color'])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeGloss.inputs['Color'])
            mat.node_tree.links.new(nodeBW.outputs['Val'], nodeMath.inputs['Value'])
            mat.node_tree.links.new(nodeGloss.outputs['BSDF'], specularMixed5.inputs[2])
            mat.node_tree.links.new(nodeMath.outputs['Value'], specularMixed5.inputs['Fac'])
            nodeTex.location = (-50, -515)
            nodeMixRGB.location = (120, -520)
            nodeBright.location = (120, -570)
            nodeBW.location = (250,-515)
            nodeMath.location = (250,-605)
            nodeGloss.location = (415,-515)
            mat.node_tree.nodes[nodeBright.name].hide = True
            mat.node_tree.nodes[nodeMixRGB.name].hide = True
        nodeTex.image = img
        node_tree = bpy.data.materials[mat.name].node_tree
        node_tree.nodes.active = nodeTex
    if layerType == "Glow":
        try: 
            nodeTex = mat.node_tree.nodes['Image Texture zbGlow']            
            mat.node_tree.nodes['Math zbGlow'].inputs[1].default_value = 6.5
        except:
            node = mat.node_tree.nodes.new(type = 'ShaderNodeTexImage')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeTex = node
            node = mat.node_tree.nodes.new(type = 'ShaderNodeMixRGB')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeMixRGB = node
            nodeMixRGB.blend_type = 'MIX'
            nodeMixRGB.inputs['Fac'].default_value = 1
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBrightContrast')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBright = node
            node = mat.node_tree.nodes.new(type='ShaderNodeEmission')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            node.inputs[1].default_value = 6.5
            nodeEmission = node
            node = mat.node_tree.nodes.new(type='ShaderNodeRGBToBW')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeBW = node
            node = mat.node_tree.nodes.new(type='ShaderNodeMath')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeMath = node
            nodeMath.operation = 'MULTIPLY'
            nodeMath.inputs[1].default_value = 6.5
            glowMixed7 = mat.node_tree.nodes['Mixed7']
            mat.node_tree.links.new(nodeTex.outputs['Color'], nodeMixRGB.inputs['Color2'])
            mat.node_tree.links.new(nodeMixRGB.outputs['Color'], nodeBright.inputs['Color'])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeBW.inputs['Color'])
            mat.node_tree.links.new(nodeBright.outputs['Color'], nodeEmission.inputs['Color'])
            mat.node_tree.links.new(nodeBW.outputs['Val'], nodeMath.inputs['Value'])
            mat.node_tree.links.new(nodeEmission.outputs['Emission'], glowMixed7.inputs[2])
            mat.node_tree.links.new(nodeMath.outputs['Value'], glowMixed7.inputs['Fac'])
            nodeTex.location = (-50, -790)
            nodeMixRGB.location = (120, -795)
            nodeBright.location = (120, -845)
            nodeBW.location = (250,-790)
            nodeMath.location = (250,-880)
            nodeEmission.location = (415,-790)
            mat.node_tree.nodes[nodeBright.name].hide = True
            mat.node_tree.nodes[nodeMixRGB.name].hide = True
        nodeTex.image = img
        node_tree = bpy.data.materials[mat.name].node_tree
        node_tree.nodes.active = nodeTex
    if layerType == "Transparent":
        try: 
            nodeTex = mat.node_tree.nodes['Image Texture zbColor']
            nodeTex.mute = False
        except:
            bpy.ops.object.zb_paint_color()
            nodeTex = mat.node_tree.nodes['Image Texture zbColor']
        if nodeTex.outputs['Alpha'].is_linked == False:
            try:
                nodeAlpha = mat.node_tree.nodes['Transparent BSDF zbTransparent']
            except:
                node = mat.node_tree.nodes.new(type = 'ShaderNodeBsdfTransparent')
                node.label = node.name + ' zb' + layerType
                node.name = node.label
                nodeAlpha = node
            Mixed5 = mat.node_tree.nodes['Mixed5']
            Mixed6 = mat.node_tree.nodes['Mixed6']
            mat.node_tree.links.new(nodeTex.outputs['Alpha'], Mixed6.inputs['Fac'])
            mat.node_tree.links.new(Mixed5.outputs['Shader'], nodeAlpha.inputs['Color'])
            mat.node_tree.links.new(nodeAlpha.outputs['BSDF'], Mixed6.inputs['Shader'])
            mat.node_tree.links.new(Mixed5.outputs['Shader'], Mixed6.inputs[2])
            nodeAlpha.location = (1750, -130)
        nodeTex.image = img
        node_tree = bpy.data.materials[mat.name].node_tree
        node_tree.nodes.active = nodeTex
    if layerType == "Alpha_Mask":
        try: 
            nodeTex = mat.node_tree.nodes['Image Texture zbAlpha_Mask']
            nodeTex.mute = False
        except:
            pass
        try:
            Mixed6 = mat.node_tree.nodes['Mixed6']
            nodeAlpha = mat.node_tree.nodes['Transparent BSDF zbAlpha_Mask']
            mat.node_tree.links.new(nodeTex.outputs['Alpha'], Mixed6.inputs['Fac'])
            mat.node_tree.links.new(nodeAlpha.outputs['BSDF'], Mixed6.inputs[2])
        except:
            node = mat.node_tree.nodes.new(type = 'ShaderNodeTexImage')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeTex = node
            node = mat.node_tree.nodes.new(type = 'ShaderNodeBsdfTransparent')
            node.label = node.name + ' zb' + layerType
            node.name = node.label
            nodeAlpha = node
            nodeTex.location = (-50, -1075)
            nodeAlpha.location = (250, -1075)
            Mixed6 = mat.node_tree.nodes['Mixed6']
            mat.node_tree.links.new(nodeTex.outputs['Alpha'], Mixed6.inputs['Fac'])
            mat.node_tree.links.new(nodeAlpha.outputs['BSDF'], Mixed6.inputs[2])
        nodeTex.image = img
        node_tree = bpy.data.materials[mat.name].node_tree
        node_tree.nodes.active = nodeTex
    if re != 'CYCLES':
        mat.use_nodes = False
    try: 
        bpy.context.user_preferences.system.use_translate_new_dataname = fontState
    except:
        pass
    return mTex
class cl21(bpy.types.Operator):
    bl_idname =i_0[65]
    bl_label =i_0[66]
    bl_description =i_0[67]
    def execute(self, context):
        re = bpy.context.scene.render.engine
        layerType = "Color"
        texCol = 0.9
        texOpas = 1
        try:
            ob = bpy.context.active_object
            if ob.active_material:
                if ob.active_material.texture_paint_images:
                    texOpas = 0
        except:
            pass
        alphaChoice = True
        normalChoice = True
        if re == 'CYCLES':
            texOpas = 1.0
            alphaChoice = True
        texLayerAdder(layerType, texCol, texOpas, alphaChoice,
        normalChoice)
        return {'FINISHED'}
class cl22(bpy.types.Operator):
    bl_idname =i_0[68]
    bl_label =i_0[69]
    bl_description =i_0[70]
    def execute(self, context):
        layerType = "Bump"
        texCol = 0.0
        texOpas = 1.0
        alphaChoice = True
        normalChoice = True
        mTex = texLayerAdder(layerType, texCol, texOpas, alphaChoice,
        normalChoice)
        mTex.use_map_color_diffuse = False
        mTex.normal_factor = 0.25
        re = bpy.context.scene.render.engine
        self.report({'INFO'}, "Use white when painting on bump layers")
        return {'FINISHED'}
class cl23(bpy.types.Operator):
    bl_idname =i_0[71]
    bl_label =i_0[72]
    bl_description =i_0[73]
    def execute(self, context):
        layerType = "Specular"
        texCol = 0.0
        texOpas = 0.0
        alphaChoice = True
        normalChoice = False
        mTex = texLayerAdder(layerType, texCol, texOpas, alphaChoice,
        normalChoice)
        ob = bpy.context.active_object
        mat = ob.active_material
        mat.specular_color = (0, 0, 0)
        mat.specular_intensity = 1
        mTex.use_map_color_diffuse = False
        mTex.use_map_color_spec = True
        return {'FINISHED'}
class cl24(bpy.types.Operator):
    bl_idname =i_0[74]
    bl_label =i_0[75]
    bl_description =i_0[76]
    def execute(self, context):
        layerType = "Transparent"
        texCol = 0.0
        texOpas = 0.0
        alphaChoice = True
        normalChoice = False
        mTex = texLayerAdder(layerType, texCol, texOpas, alphaChoice,
        normalChoice)
        ob = bpy.context.active_object
        mat = ob.active_material
        mat.use_transparency = True
        mat.transparency_method = 'Z_TRANSPARENCY'
        mat.alpha = 0
        mat.specular_intensity = 0
        mTex.use_map_alpha = True
        bpy.context.space_data.show_backface_culling = False
        return {'FINISHED'}
class cl25(bpy.types.Operator):
    bl_idname =i_0[77]
    bl_label =i_0[78]
    bl_description =i_0[79]
    def execute(self, context):
        layerType = "Alpha_Mask"
        texCol = 0.0
        texOpas = 0.0
        alphaChoice = True
        normalChoice = False
        mTex = texLayerAdder(layerType, texCol, texOpas, alphaChoice,
        normalChoice)
        ob = bpy.context.active_object
        mat = ob.active_material
        mat.use_transparency = True
        mat.transparency_method = 'Z_TRANSPARENCY'
        mat.alpha = 0
        mTex.use_map_alpha = True
        mTex.diffuse_color_factor = 0
        mTex.alpha_factor = -1
        bpy.context.space_data.show_backface_culling = False
        return {'FINISHED'}
class cl26(bpy.types.Operator):
    bl_idname =i_0[80]
    bl_label =i_0[81]
    bl_description =i_0[82]
    def execute(self, context):
        scene = bpy.context.scene
        wm = bpy.context.window_manager
        layerType = "Glow"
        texCol = 0.0
        texOpas = 0.0
        alphaChoice = True
        normalChoice = False
        mTex = texLayerAdder(layerType, texCol, texOpas, alphaChoice,
        normalChoice)
        mTex.use_map_emit = True
        mTex.emit_factor = 0.05
        mTex.texture.factor_red = 2
        mTex.texture.factor_green = 2
        mTex.texture.factor_blue = 2
        mTex.texture.contrast = 5
        world = scene.world
        ls = world.light_settings
        ls.gather_method = 'APPROXIMATE'
        ls.use_indirect_light = True
        ls.correction = 0.75
        ls.indirect_bounces = 3
        return {'FINISHED'}
class cl27(bpy.types.Operator):
    bl_idname =i_0[83]
    bl_label =i_0[84]
    bl_description =i_0[85]
    def execute(self, context):
        ob = bpy.context.active_object
        userMsg = ''
        for mod in ob.modifiers: 
            if 'Mirror' in mod.name or 'Bevel' in mod.name or 'Shrinkwrap' in mod.name:
                if 'Raise AE' not in mod.name:
                    try:
                        bpy.ops.object.modifier_apply(apply_as='DATA',
                        modifier = mod.name)
                    except:
                        pass
        ob = bpy.context.active_object
        skin = len([mod for mod in ob.modifiers if mod.type == 'SKIN'])
        if skin:
            fu7()
            userMsg = "APPLIED SKIN MODIFIER: Click 'EYE' icon next to"+ob.name+"sBones in the outliner to see it."
        for mod in ob.modifiers:
            if hasattr(mod,'object'):
                if "Bones" not in mod.object.name:
                    userMsg = "Object already has armature. None created for it."
            if mod.type == 'SOLIDIFY':  
                try:              
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
                except:
                    pass
                ob.show_x_ray = False
        adaptiveMod = fu15(ob)        
        subsurf = 0
        for mod in ob.modifiers:
            if mod.type == 'SUBSURF':
                if mod != adaptiveMod:
                    subsurf = mod
                    break
        if subsurf: 
            newLevels = subsurf.levels
            bpy.ops.object.modifier_remove(modifier=subsurf.name)
            multires = ob.modifiers.new(name='Multires',type='MULTIRES')
            while newLevels > 0:
                bpy.ops.object.multires_subdivide(modifier=multires.name)
                multires.levels += 1
                newLevels -= 1
        else:
            multires = ob.modifiers.new(name='Multires',type='MULTIRES')
            newLevels = 2
            while newLevels > 0:
                bpy.ops.object.multires_subdivide(modifier=multires.name)
                multires.levels += 1
                newLevels -= 1
        for mod in ob.modifiers:
            try:            
                bpy.ops.object.modifier_move_up(modifier="Multires")
            except:
                pass        
            try: 
                bpy.ops.object.modifier_move_up(modifier="Armature")
            except:
                pass
        bpy.ops.object.shade_smooth()
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='SCULPT')
        if userMsg:
            self.report({'INFO'}, userMsg)
        return {'FINISHED'}
def fu15(ob):
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
class cl28(bpy.types.Operator):
    bl_idname =i_0[86]
    bl_label =i_0[87]
    bl_description =i_0[88]
    def execute(self, context):
        scene = bpy.context.scene
        ob = bpy.context.active_object
        userMsg = ''
        mirror = len([mod for mod in ob.modifiers if mod.type == 'MIRROR'])
        if mirror:
            try:
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Mirror")
            except:
                pass
            scene.tool_settings.sculpt.use_symmetry_x = True
        ob = bpy.context.active_object
        skin = len([mod for mod in ob.modifiers if mod.type == 'SKIN'])
        if skin:
            fu7()
            userMsg = "APPLIED SKIN MODIFIER: Click 'EYE' icon next to "+ob.name+"sBones in the outliner to see it."
        adaptiveMod = fu15(ob)          
        for mod in ob.modifiers:
            try:
                if hasattr(mod,'object'):
                    if "Bones" not in type.object.name:
                        userMsg = "Object already has armature. None created for it."
                if mod.type == 'SOLIDIFY':
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
                    ob.show_x_ray = False
                if mod.type == 'SUBSURF':
                    if mod != adaptiveMod:
                        bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
                if mod.type == 'MULTIRES':
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod.name)
            except:
                pass
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.ops.object.mode_set(mode='SCULPT')
        bpy.ops.sculpt.dynamic_topology_toggle()
        scene.tool_settings.sculpt.detail_type_method = 'CONSTANT'
        scene.tool_settings.sculpt.detail_refine_method = 'SUBDIVIDE_COLLAPSE'
        scene.tool_settings.sculpt.constant_detail = 4.5
        bpy.ops.sculpt.optimize()
        bpy.context.tool_settings.sculpt.brush.auto_smooth_factor = 0.75
        scene.tool_settings.sculpt.use_smooth_shading = True
        bpy.context.tool_settings.sculpt.brush
        for brush in bpy.data.brushes:
            if brush.use_paint_sculpt:
                try:
                    brush.use_accumulate = True
                except:
                    pass
                try:
                    brush.sculpt_plane = 'VIEW'
                except:
                    pass
                try:
                    brush.auto_smooth_factor = 0.1
                except:
                    pass
        if userMsg:
            self.report({'INFO'},userMsg)
        return {'FINISHED'}
class cl29(bpy.types.Operator):
    bl_idname =i_0[89]
    bl_label =i_0[90]
    bl_description =i_0[91]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        ob = bpy.context.active_object
        multires = len([mod for mod in ob.modifiers if mod.type == 'MULTIRES'])
        if multires:
            val = bpy.context.object.modifiers["Multires"].levels
            bpy.context.object.modifiers["Multires"].levels += 1
            bpy.context.object.modifiers["Multires"].sculpt_levels += 1
            bpy.context.object.modifiers["Multires"].render_levels += 1
            val2 = bpy.context.object.modifiers["Multires"].sculpt_levels 
            if val == val2: 
                bpy.ops.object.multires_subdivide(modifier="Multires")
                bpy.context.object.modifiers["Multires"].levels += 1
                val2 = bpy.context.object.modifiers["Multires"].levels
            bpy.context.area.tag_redraw() 
            response = "Subdivision levels: " + str(val2)
            self.report({'INFO'}, response)
        if not multires: 
            bpy.ops.object.zb_multires_add()
        return {'FINISHED'}
class cl29Down(bpy.types.Operator):
    bl_idname =i_0[92]
    bl_label =i_0[93]
    bl_description =i_0[94]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        ob = bpy.context.active_object
        multires = len([mod for mod in ob.modifiers if mod.type == 'MULTIRES'])
        if multires:
            val = bpy.context.object.modifiers["Multires"].levels
            bpy.context.object.modifiers["Multires"].levels -= 1
            bpy.context.object.modifiers["Multires"].sculpt_levels -= 1
            bpy.context.object.modifiers["Multires"].render_levels -= 1
            val2 = bpy.context.object.modifiers["Multires"].sculpt_levels
            bpy.context.area.tag_redraw() 
            response = "Subdivision levels: " + str(val2)
            self.report({'INFO'}, response)
        return {'FINISHED'}
class cl30(bpy.types.Operator):
    bl_idname =i_0[95]
    bl_label =i_0[96]
    bl_description =i_0[97]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        ob = bpy.context.active_object
        multires = len([mod for mod in ob.modifiers if mod.type == 'MULTIRES'])
        if multires:
            lastLevels = ob.modifiers["Multires"].levels
            ob.modifiers["Multires"].sculpt_levels = 0
            bpy.ops.object.multires_higher_levels_delete(modifier="Multires")
            for x in range(lastLevels):
                bpy.ops.object.multires_subdivide(modifier="Multires")
            bpy.context.object.modifiers["Multires"].levels = lastLevels
            bpy.context.object.modifiers["Multires"].sculpt_levels = lastLevels
            bpy.context.object.modifiers["Multires"].render_levels = lastLevels
            bpy.context.area.tag_redraw() 
        return {'FINISHED'}
class cl31(bpy.types.Operator):
    bl_idname =i_0[98]
    bl_label =i_0[99]
    bl_description =i_0[100]
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        ob = bpy.context.active_object
        multires = len([mod for mod in ob.modifiers if mod.type == 'MULTIRES'])
        dynamic = bpy.context.active_object.use_dynamic_topology_sculpting
        if multires:
            bpy.ops.object.mode_set(mode='OBJECT')
            try:
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Multires")
            except:
                pass
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.remove_doubles()
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.particle_system_remove()
            bpy.ops.object.mode_set(mode='SCULPT')
        if dynamic:
            bpy.ops.sculpt.optimize()
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.remove_doubles()
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.particle_system_remove()
            bpy.ops.object.mode_set(mode='SCULPT')
            self.report({'INFO'}, "Recommend retopology as next step in design")
        return {'FINISHED'}
class cl32(bpy.types.Operator):
    bl_idname =i_0[101]
    bl_label =i_0[102]
    bl_description =i_0[103]
    bl_options = {'REGISTER', 'UNDO'}
    option = bpy.props.StringProperty()
    def execute(self, context):
        option = self.option
        scene = bpy.context.scene
        ob = bpy.context.active_object
        if option == 'NEW':
            par = str(len(ob.particle_systems))
            parSys = ob.name + "Strands" + par
            bpy.ops.object.particle_system_add()
            activeSys = ob.particle_systems.active
            activeSys.settings.name = parSys
            set = activeSys.settings
            set.type = 'HAIR'
            set.hair_length = 0.15
            set.count = 0
            set.adaptive_angle = 3
            set.use_strand_primitive = True
            set.use_hair_bspline = False
            set.render_step = 6
            set.draw_step = 4
            set.cycles.root_width = 0.25
            set.child_type = 'SIMPLE'    
            bpy.ops.object.mode_set(mode='PARTICLE_EDIT')
            set.child_nbr = 65
            set.rendered_child_count = 65
            set.child_length = 1
            set.child_radius = 0.10
            set.roughness_2 = 0.01
            set.draw_percentage = 5
            pe = scene.tool_settings.particle_edit
            pe.show_particles = True
            pe.draw_step = 3
            pe.tool = 'ADD'
            pe.brush.size = 30
            pe.brush.count = 3
            activeSys.use_hair_dynamics = True
            cloth = ob.particle_systems.active.cloth
            settings = cloth.settings
            settings.pin_stiffness = 4
            settings.mass = 0.25
            settings.bending_stiffness = 0.125
            settings.bending_damping = 0.125
            settings.internal_friction = 0
            settings.air_damping = 0.75
            settings.quality = 4
            activeSys.use_hair_dynamics = False
            pe.draw_step = 4
            lastBrush = pe.tool        
            bItems = ['COMB','SMOOTH','LENGTH','PUFF','CUT','WEIGHT']
            for item in bItems:
                pe.tool = item            
                if pe.brush.strength > 5:
                    pe.brush.strength = 0.75
            pe.tool = lastBrush        
        if option == 'COPY':
            renEn = scene.render.engine
            ob = bpy.context.active_object
            parSys = ob.particle_systems.active
            set = parSys.settings        
            lastSetName = set.name
            lastSysName = parSys.name
            copyPar = bpy.data.particles[set.name].copy()                        
            copyPar.name = lastSetName + '_COPY'            
            bpy.ops.object.particle_system_add()
            activeSys = ob.particle_systems.active                
            activeSys.name = lastSysName + '_COPY'        
            activeSys.settings = copyPar
            pe = scene.tool_settings.particle_edit
            pe.tool = 'ADD'
            for sys in bpy.data.particles:
                if sys.users == 0:
                    try:
                        bpy.data.particles.remove(sys, do_unlink = True) 
                    except:
                        bpy.data.particles.remove(sys) 
        if option == 'CHANGE_COLOR':
            renEn = scene.render.engine
            ob = bpy.context.active_object
            parSys = ob.particle_systems.active
            set = parSys.settings
            matName = set.material_slot
            mat = bpy.data.materials[matName]  
            if mat.node_tree:           
                nodes = mat.node_tree.nodes 
                if nodes: 
                    if 'Hair BSDF' in nodes:                          
                        hairNode = nodes['Hair BSDF']                
                        if renEn == 'CYCLES':               
                            mCol = hairNode.inputs['Color'].default_value
                            mat.diffuse_color = mCol[0], mCol[1], mCol[2]
                            mat.use_nodes = True            
                        else:                
                            mCol = mat.diffuse_color
                            hairNode.inputs['Color'].default_value = mCol[0],mCol[1],mCol[2], 1
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.mode_set(mode='PARTICLE_EDIT')            
        if option == 'ADD_BASIC_MATERIAL':
            renEn = scene.render.engine
            ob = bpy.context.active_object
            parSys = ob.particle_systems.active
            set = parSys.settings
            baseColor = (0.344312, 0.202204, 0.0661491)
            newMat = bpy.data.materials.new(name = ob.name + 'Hair')
            newMat.diffuse_color = baseColor
            newMat.strand.root_size = 0.5
            newMat.strand.tip_size = 0.25
            newMat.strand.use_tangent_shading = True
            newMat.translucency = 0.1            
            newMat.use_transparency = True
            newMat.alpha = 0.595
            rm = newMat.raytrace_mirror
            rm.use = True
            rm.reflect_factor = 0.5
            rm.fresnel = 4.25
            rm.fresnel_factor = 4.5
            rm.depth = 1
            mat = newMat
            newMat.use_nodes = True            
            mat.node_tree.nodes.clear()
            nodeOutput = mat.node_tree.nodes.new(type = 'ShaderNodeOutputMaterial')
            nodeOutput.location = (200,0)
            nodeHair = mat.node_tree.nodes.new(type = 'ShaderNodeBsdfHair')
            nodeHair.inputs['Color'].default_value = baseColor[0],baseColor[1],baseColor[2], 1
            links = mat.node_tree.links            
            links.new(nodeHair.outputs['BSDF'], nodeOutput.inputs['Surface'])
            if renEn == 'CYCLES':
                newMat.use_nodes = True
            else:
                newMat.use_nodes = False
            if len(ob.data.materials) == 0:
                if len(ob.material_slots) == 0:
                    bpy.ops.object.material_slot_add()            
            if newMat.name not in ob.data.materials:
                ob.data.materials.append(newMat)                        
            set.material_slot = newMat.name                                                                
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.mode_set(mode='PARTICLE_EDIT')  
        return {'FINISHED'}
def fu16(self,context):
    scene = bpy.context.scene
    wm = bpy.context.window_manager
    re = bpy.context.scene.render.engine
    mode = bpy.context.mode
    try:
        bpy.ops.object.mode_set(mode='OBJECT')
        ob = bpy.context.active_object
        mat = ob.active_material
        aTex = mat.active_texture.name
    except:
        pass
    if scene.zbGoCycles:
        bpy.context.scene.render.engine = 'CYCLES'
        if bpy.context.screen.name in {'Hacker', 'Blender', 'Shader'}:
            world = bpy.context.scene.world
            world.light_settings.ao_factor = 0
            try: 
                bpy.data.worlds['ZB Quick Lights'].ao_factor = 1
            except:
                pass
            if bpy.context.screen.name == 'Shader':
                for area in bpy.context.screen.areas:
                    if area.type == 'VIEW_3D':
                        area.spaces.active.viewport_shade = 'MATERIAL'
        if scene.zbAutoConvertLamps:
            for lamp in bpy.data.lamps:
                lamp.use_nodes = True
        else:
            try:
                bpy.data.objects['-Scene Light'].hide_render = True
            except:
                pass
        for mat in bpy.data.materials:
            try:
                nodes = mat.node_tree.nodes                
                for node in nodes:
                    if node.type == 'OUTPUT_MATERIAL':                        
                        mat.use_nodes = True
                        break
            except:
                pass
        for world in bpy.data.worlds:            
            world.use_nodes = True
    else:
        bpy.context.scene.render.engine = 'BLENDER_RENDER'
        if bpy.context.screen.name in {'Hacker', 'Blender', 'Shader'}:
            world = bpy.context.scene.world
            world.light_settings.ao_factor = 1
            try: 
                bpy.data.worlds['ZB Quick Lights'].ao_factor = 1
            except:
                pass
            if bpy.context.screen.name == 'Shader':
                for area in bpy.context.screen.areas:
                    if area.type == 'VIEW_3D':
                        area.spaces.active.viewport_shade = 'MATERIAL'
        if scene.zbQuickLights == True:
            try:
                lastWorld = scene.zbLastWorld
                bpy.context.scene.world = bpy.data.worlds[lastWorld]
            except:
                pass
        for mat in bpy.data.materials:
            if hasattr(mat.node_tree,'nodes'):
                if 'Material Output' in mat.node_tree.nodes:                    
                    for ts in mat.texture_slots:
                        if hasattr(ts,'texture'):
                            if ts.texture:
                                if hasattr(ts.texture,'image'):
                                    mat.use_nodes = False
                                    break
        try: 
            scnLight = bpy.data.objects['-Scene Light']
            scnLight.hide_render = False
        except:
            pass
    bpy.context.scene.update()
    try: 
        if len(scene.sfCFocus) > 0:
            for ob in bpy.data.objects:
                if ob.type == 'CAMERA':
                    cam = ob
                    break
            scene.sfCFocus = cam.data.dof_object.name
        world = bpy.context.scene.world
        if world.mist_settings.use_mist:
            bpy.ops.object.sf_cam_options(func="mist")
    except:
        pass
    bpy.context.scene.update()
    fu1(mode)
    fu10()
class cl33(bpy.types.Operator):
    bl_idname =i_0[104]
    bl_label =i_0[105]
    def execute(self,context):
        brush = bpy.context.tool_settings.sculpt.brush
        m = 'NORMAL'
        try:
            if brush.stroke_method != 'LINE':
                m = 'SMOOTH'
            bpy.ops.sculpt.brush_stroke('INVOKE_DEFAULT', mode=m)
        except:
            pass
        return{'FINISHED'}
class cl34(bpy.types.Operator):
    bl_idname =i_0[106]
    bl_label =i_0[107]
    def modal(self, context, event):
        if event.value == 'RELEASE':
            brush = bpy.context.tool_settings.sculpt.brush
            try:
                brush.direction = 'ADD'
            except:
                try:
                    brush.direction = 'INFLATE'
                except:
                    pass
                pass
            return {'FINISHED'}
        return {'RUNNING_MODAL'}
    def invoke(self, context, event):
        brush = bpy.context.tool_settings.sculpt.brush
        if brush.stroke_method == 'LINE':
            context.window_manager.modal_handler_add(self)
            try:
                brush.direction = 'SUBTRACT'
            except:
                try:
                    brush.direction = 'DEFLATE'
                except:
                    pass
                pass
            bpy.ops.sculpt.brush_stroke('INVOKE_DEFAULT')
        else:
            bpy.ops.sculpt.brush_stroke('INVOKE_DEFAULT',
            mode='INVERT')
            return {'FINISHED'}
        return {'RUNNING_MODAL'}
class cl35(bpy.types.Operator):
    bl_idname =i_0[108]
    bl_label =i_0[109]
    bl_description =i_0[110]
    shapeTool = bpy.props.StringProperty()
    lastBrush = bpy.props.StringProperty()
    def execute(self,context):
        aType = bpy.context.area.type
        paint = bpy.context.mode.startswith('PAINT_TEXTURE')
        weight = bpy.context.mode.startswith('PAINT_WEIGHT')
        vertex = bpy.context.mode.startswith('PAINT_VERTEX')
        sculpt = bpy.context.mode.startswith('SCULPT')
        ts = bpy.context.tool_settings
        if paint or aType == 'IMAGE_EDITOR':
            type = bpy.context.tool_settings.image_paint
            try:
                brush = bpy.context.tool_settings.image_paint.brush
                if brush.image_tool != 'MASK':
                    if bpy.context.space_data.viewport_shade == 'SOLID':
                        bpy.context.space_data.viewport_shade = 'MATERIAL'
            except:
                pass
        if sculpt:
            type = ts.sculpt
        if weight:
            type = ts.weight_paint
        if vertex:
            type = ts.vertex_paint
        if paint or aType == 'IMAGE_EDITOR':
            try:
                if brush.use_gradient:
                    if type.brush.name == 'Fill':
                        if self.shapeTool == 'SPACE':
                            type.brush = bpy.data.brushes['Draw']
                            type.brush.use_gradient = True
                    if self.shapeTool == 'LINE':
                        type.brush = bpy.data.brushes['Fill']
                        type.brush.use_gradient = True
                        type.brush.gradient_fill_mode = 'LINEAR'
                    if self.shapeTool == 'ANCHORED':
                        self.shapeTool = 'LINE'
                        type.brush = bpy.data.brushes['Fill']
                        type.brush.use_gradient = True
                        type.brush.gradient_fill_mode = 'RADIAL'
            except:
                pass
            if self.shapeTool == 'SPACE':
                type.input_samples = 3
            else:
                type.input_samples = 1
        if type.brush.texture:
            if self.shapeTool == 'SPACE':
                self.shapeTool = 'DOTS'
        if 'Decal' in type.brush.name:
            if self.shapeTool == 'DOTS':
                self.shapeTool = 'DRAG_DOT'
        type.brush.stroke_method = self.shapeTool
        return{'FINISHED'}
class cl36(bpy.types.Operator):
    bl_idname =i_0[111]
    bl_label =i_0[112]
    bl_description =i_0[113]
    def execute(self,context):
        bpy.ops.brush.stencil_reset_transform()
        bpy.ops.brush.stencil_fit_image_aspect()
        area = bpy.context.area
        x = area.width / 2
        y = area.height / 2
        try:
            if bpy.context.sculpt_object:
                brushName = bpy.context.tool_settings.sculpt.brush.name
            else:
                brushName = bpy.context.tool_settings.image_paint.brush.name
            brush = bpy.data.brushes[brushName]
            brush.stencil_pos.xy = x, y
            brush.texture_slot.scale.xyz = 1
        except:
                pass
        return{'FINISHED'}
class cl37(bpy.types.Operator):
    bl_idname =i_0[114]
    bl_label =i_0[115]
    bl_description = "Sync position, angle and scale of\
 texture brush and texture mask stencils"
    def execute(self,context):
        brush = bpy.context.tool_settings.image_paint.brush
        slot = brush.texture_slot
        mask = brush.mask_texture_slot
        mask.mask_map_mode = 'STENCIL'
        brush.mask_stencil_pos = brush.stencil_pos
        brush.mask_stencil_dimension = brush.stencil_dimension
        mask.offset.xyz = slot.offset.xyz
        mask.scale.xyz = slot.scale.xyz
        mask.angle = slot.angle
        return{'FINISHED'}
def zbGradientSwitch(self,context):
    wm = bpy.context.window_manager
    ts = bpy.context.tool_settings
    paint = ts.image_paint
    if self.zbGradientSwitch:
        try:
            wm.zbBeforeGradBrush = paint.brush.name
            paint.brush = bpy.data.brushes['Fill']
        except:
            pass
        paint.brush.use_gradient = True
    else:
        try:
            if paint.brush.name != 'Draw':
                paint.brush = bpy.data.brushes[wm.zbBeforeGradBrush]
        except:
            print("Couldn't change the brush")
        paint.brush.use_gradient = False
def fu17(panel, context, layout, brush, settings, projpaint=False):
    capabilities = brush.image_paint_capabilities
    sd = bpy.context.space_data
    try:
        shade = sd.viewport_shade
    except:
        pass
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    toolsettings = context.tool_settings
    ipaint = toolsettings.image_paint
    col = layout.column(align=True)
    if capabilities.has_radius:
        row = col.row(align=True)
        row.operator('object.sf_tn', text='',icon='BLANK1')
        panel.prop_unified_size(row, context, brush, "size", slider=True, text="Radius")
        panel.prop_unified_size(row, context, brush, "use_pressure_size")
    row = col.row(align=True)
    if capabilities.has_space_attenuation:
        row.prop(brush, "use_space_attenuation", toggle=True, icon_only=True)
    else:
        row.operator('object.sf_tn', text='',icon='BLANK1')
    panel.prop_unified_strength(row, context, brush, "strength", text="Strength")
    panel.prop_unified_strength(row, context, brush, "use_pressure_strength")
    if brush.image_tool == 'SOFTEN':
        col.separator()
        col = layout.column(align=True)
        col.row(align=True).prop(brush, "direction", expand=True)
        col.prop(brush, "sharp_threshold")
        col.prop(brush, "blur_kernel_radius")
    if brush.image_tool == 'CLONE':
        col.separator()
        layout.column(align=True)
        col.prop(settings, "use_clone_layer", text="Clone from paint slot", icon='BRUSH_CLONE')
        if projpaint:
            if settings.use_clone_layer:
                ob = context.active_object
                if len(ob.material_slots) > 1:
                    col.label("Materials")
                    col.template_list("MATERIAL_UL_matslots", "",
                                      ob, "material_slots",
                                      ob, "active_material_index", rows=2)
                mat = ob.active_material
                if mat:
                    col.template_list("TEXTURE_UL_texpaintslots", "",
                                      mat, "texture_paint_images",
                                      mat, "paint_clone_slot", rows=2)
        else:
            col.prop(brush, "clone_image", text="Image")
            col.prop(brush, "clone_alpha", text="Alpha")
    if brush.image_tool == 'FILL':
        row = col.row(align=True)
        row.operator('object.sf_tn', text='',icon='BLANK1')
        row.prop(brush, "fill_threshold", text='Threshold', slider=True)
        row.operator('object.sf_tn', text='',icon='BLANK1')
    if bpy.context.mode == 'PAINT_VERTEX':
        brush = bpy.context.tool_settings.vertex_paint.brush
    else:
        brush = bpy.context.tool_settings.image_paint.brush
    row = col.separator()
    row = col.row(align=True)
    row.label("Brush Stroke")
    row.operator("object.zb_stroke_buttons",
    text ="", icon='MOD_DYNAMICPAINT').shapeTool = 'SPACE'
    row.operator("object.zb_stroke_buttons", text='',
    icon='MOD_CURVE').shapeTool = 'CURVE'
    row.operator("object.zb_stroke_buttons",
    text ="", icon='IPO_LINEAR').shapeTool = 'LINE'
    if not bpy.context.mode.startswith('PAINT_VERTEX'):
        row.operator("object.zb_stroke_buttons",
        text ="", icon='PROP_ON').shapeTool = 'ANCHORED'
    if brush.stroke_method == 'LINE':
        row = col.row(align=True)
        row.label('(Hold alt to constrain line)')
    if brush.stroke_method == 'CURVE':
        row = col.separator()
        row = col.row(align=True)
        row.template_ID(brush, "paint_curve", new="paintcurve.new")
        if brush.paint_curve:
            row = col.separator()
            row = col.row(align=True)
            row.label("(Ctrl-Mouse)")
            row.operator("paintcurve.draw", text="Draw Curve")
        else:
            row = col.row(align=True)
            row.label("(Ctrl-click to make new curve)")
            row = col.row(align=True)
    if not bpy.context.mode.startswith('PAINT_VERTEX'):
        try:
            toolsettings = context.tool_settings
            ipaint = toolsettings.image_paint
            row = col.separator()
            row = col.row(align=True)
            row.scale_y = 0.8
            row.label("Mirror")
            row.separator()
            row.prop(ipaint, "use_symmetry_x", text="X", toggle=True)
            row.prop(ipaint, "use_symmetry_y", text="Y", toggle=True)
            row.prop(ipaint, "use_symmetry_z", text="Z", toggle=True)
        except:
            pass
    row = col.separator()
    if brush.image_tool == 'MASK':
        col.prop(brush, "weight", text="Mask Value", slider=True)
        row = col.separator()
        row = col.row(align=True)
        row.prop(ipaint, "invert_stencil", text="Invert", icon='IMAGE_ALPHA')
        if wm.zbViewMaskMode or shade == 'SOLID':
            maskIcon = 'RESTRICT_VIEW_OFF'
        else:
            maskIcon = 'RESTRICT_VIEW_ON'
        row.prop(wm,"zbViewMaskMode", text='View', icon= maskIcon)
        row = col.row(align=True)
        set = scene.tool_settings.image_paint
        row.prop(set, 'use_stencil_layer', text="", icon = 'CANCEL')
        row.operator('image.new', text = 'Reset Mask').gen_context = 'PAINT_STENCIL'
        row = col.separator()
        row = col.row(align=True)
    if brush.image_tool in {'DRAW', 'FILL'}:
        if bpy.context.mode.startswith('PAINT_VERTEX'):
            brush = bpy.context.tool_settings.vertex_paint.brush
        col.separator()
        box = col.box()
        if not brush.use_gradient:
            panel.prop_unified_color_picker(box, context, brush, "color", value_slider=True)
        if brush.use_gradient:
            box.template_color_ramp(brush, "gradient", expand=True)
            if settings.palette:
                sub = box.row(True)
                sub = box.row(True)
                sub.template_palette(settings, "palette", color=True)
            if brush.image_tool == 'DRAW':
                sub = box.row(True)
                sub.prop(wm, "zbHidePaintOptions", text = '', icon = 'COLLAPSEMENU')
                sub = sub.row(align=True)
                sub.scale_x = 0.05
                sub.prop(brush,'color',text='')
                sub = sub.row(align=True)
                sub.scale_x =10
                sub.prop(brush, "gradient_stroke_mode",text="")
                sub.prop(wm,"zbGradientSwitch", text ="Gradient", toggle=True)
                if brush.gradient_stroke_mode in {'SPACING_REPEAT', 'SPACING_CLAMP'}:
                    sub = box.row(True)
                    sub.prop(brush, "grad_spacing")
            elif brush.image_tool == 'FILL':
                sub = box.row(True)
                if bpy.context.mode.startswith('PAINT_VERTEX'):
                    sub.prop(brush, "vertex_tool", text="")
                else:
                    sub.prop(wm, "zbHidePaintOptions", text = '', icon = 'COLLAPSEMENU')
                    sub = sub.row(align=True)
                    sub.scale_x = 0.05
                    sub.prop(brush,'color',text='')
                    sub = sub.row(align=True)
                    sub.scale_x =10
                    sub.prop(brush, "gradient_fill_mode", text="")
                    sub.prop(wm,"zbGradientSwitch", text ="Gradient", toggle=True)
        else:
            if settings.palette:
                sub = box.row(True)
                sub.template_palette(settings, "palette", color=True)
            sub = box.row(True)
            sub.prop(wm, "zbHidePaintOptions", text = '', icon = 'COLLAPSEMENU')
            sub = sub.row(align=True)
            sub.scale_x = 0.05
            sub.prop(brush,'color',text='')
            sub = sub.row(align=True)
            sub.scale_x =10
            if bpy.context.mode.startswith('PAINT_VERTEX'):
                sub.prop(brush, "vertex_tool", text="")
            else:
                sub.prop(brush, "blend", text="")
                sub.prop(wm,"zbGradientSwitch", text ="Gradient", toggle=True)
        if wm.zbHidePaintOptions:
            row = layout.row()
            row.template_ID(settings, "palette", new="palette.new")
            row = layout.row(align=True)
            panel.prop_unified_color(row, context, brush, "color", text="")
            panel.prop_unified_color(row, context, brush, "secondary_color", text="")
            row.operator("paint.brush_colors_flip", icon='FILE_REFRESH', text="")
            col = layout.column(align=True)
            try:
                t = brush.texture
                col.prop(t, 'intensity')
                col.prop(t, 'contrast')
                col.prop(t, 'saturation')
            except:
                pass
            row = layout.row()
            row.prop(settings, "input_samples", text='Stroke Samples')
            row = layout.row(align=True)
            row.label('Curve')
            row.operator("brush.curve_preset", icon='SMOOTHCURVE', text="").shape = 'SMOOTH'
            row.operator("brush.curve_preset", icon='SPHERECURVE', text="").shape = 'ROUND'
            row.operator("brush.curve_preset", icon='ROOTCURVE', text="").shape = 'ROOT'
            row.operator("brush.curve_preset", icon='SHARPCURVE', text="").shape = 'SHARP'
            row.operator("brush.curve_preset", icon='LINCURVE', text="").shape = 'LINE'
            row.operator("brush.curve_preset", icon='NOCURVE', text="").shape = 'MAX'
            row = layout.row()
            row.prop(brush, "use_accumulate")
def fu18(self):
    wm = bpy.context.window_manager
    scene = bpy.context.scene
    context = bpy.context
    layout = self.layout
    aType = bpy.context.area.type
    ts = bpy.context.tool_settings
    try:
        brush = ts.image_paint.brush
        tex_slot = brush.texture_slot
        if context.image_paint_object:
            brush = ts.image_paint.brush
            tex_slot = brush.texture_slot
        if context.vertex_paint_object:
            brush = ts.vertex_paint.brush
            tex_slot = brush.texture_slot
        if context.weight_paint_object:
            brush = ts.weight_paint.brush
            tex_slot = brush.texture_slot
        if context.sculpt_object:
            brush = ts.sculpt.brush
            tex_slot = brush.texture_slot
    except:
        pass
    row = layout.row(align=True)
    row.alignment = 'LEFT'
    row.label('Load')
    row.operator('texture.zb_load_brush')
    row.operator('texture.zb_load_brushes')
    row = layout.row()
    showScale = False
    if 'Fill' in brush.name:
        showScale = True
    try:
        if 'Draw' in wm.zbBeforeGradBrush:
            showScale = False
        if 'Graphic Pen' in wm.zbBeforeGradBrush:
            showScale = False
    except:
        pass
    if tex_slot.texture:
        showScale = True
    if showScale:
        row = layout.row(align=True)
        row.prop(tex_slot, "tex_paint_map_mode", text="")
    if tex_slot.tex_paint_map_mode == 'STENCIL':
        row = layout.row(align=True)
        row.operator("object.zb_center_stencil", text="Center")
        row.operator("object.zb_stencil_sync", text="Sync Mask")
        row = layout.row()
        row.scale_y = 0.5
        row.label("MOVE: Right Mouse")
        row = layout.row()
        row.scale_y = 0.5
        row.label("SCALE: Shift+RMouse")
        row = layout.row()
        row.scale_y = 0.5
        row.label("ROTATE: Ctrl+X")
        row = layout.row()
class View3DPaintPanel(UnifiedPaintPanel):
    bl_space_type =i_0[116]
    bl_region_type =i_0[117]
class cl38(Panel, View3DPaintPanel):
    bl_category =i_0[118]
    bl_label =i_0[119]
    bl_region_type =i_0[120]
    @classmethod
    def poll(cls, context):
        return cls.paint_settings(context)
    def draw(self, context):
        scene = bpy.context.scene
        ob = bpy.context.active_object
        layout = self.layout
        toolsettings = context.tool_settings
        settings = self.paint_settings(context)
        brush = settings.brush
        wm = bpy.context.window_manager
        if fu20():
            if not context.particle_edit_object:
                col = layout.split().column()
                col.template_ID_preview(settings, "brush", new="brush.add", rows=3, cols=8)
                fu18(self)
            if context.particle_edit_object:
                tool = settings.tool
                box = layout.box()
                box.column().prop(settings, "tool", text = 'Brush')
                if tool != 'NONE':                
                    if tool != 'WEIGHT':
                        try:
                            sub1 = box.row(True)
                            sub1.scale_x = 0.7
                            sub1.scale_y = 0.8
                            sub1.label('Mirror')
                            sub1.separator()
                            sub1.prop(ob.data, "use_mirror_x", text="X", toggle=True)   
                            text1 = 'Can only x-mirror while in particle mode.'                 
                            sub1.operator('object.sf_tn', text = '   Y').message = text1
                            sub1.operator('object.sf_tn', text = '   Z').message = text1                    
                        except:
                            pass
                    col = box.column(True)   
                    col.separator()
                    set = ob.particle_systems.active.settings
                    col.prop(brush, "size", slider=True, text = 'Brush Radius')
                    col.prop(brush, "strength", slider=True, text = 'Brush Strength')
                if tool == 'ADD':
                    sub = col                 
                    sub.prop(brush, "count")
                    sub.separator()
                    sub.separator()
                    sub.prop(settings, "use_default_interpolate",toggle=True)
                    sub = sub.column(align=True)
                    sub.active = settings.use_default_interpolate
                    sub.prop(brush, "steps", slider=True)
                    sub.prop(settings, "default_key_count")
                elif tool == 'LENGTH':
                    col.separator()
                    col.separator()
                    col.prop(brush, "length_mode", expand = True)
                elif tool == 'PUFF':
                    col.separator()
                    col.separator()
                    sub = col.row(True)
                    sub.prop(brush, "puff_mode", expand=True)
                    col.prop(brush, "use_puff_volume", toggle=True)
                if tool != 'NONE':
                    col.separator() 
                    if set.child_type != 'NONE':                                   
                        col = layout.column()
                        col.separator()
                        col.label('Child Particles')
                        sub = col.column(True)
                        sub.scale_y = 1
                        sub.scale_y = 1.4
                        sub.prop(set, 'draw_percentage', text = 'Display')
                        sub = sub.column(True)
                        sub.scale_y = 1
                        sub = sub.row(True)
                        sub.scale_x = .95
                        sub.scale_y = 0.95
                        sub.operator('object.zb_particle_detail_select', text = '', 
                        icon = 'PARTICLEMODE').detailSelect = 'PARTICLE_EDIT'
                        sub.operator('object.zb_particle_detail_select', text = '', 
                        icon = 'OBJECT_DATAMODE').detailSelect = 'OBJECT'
                        sub.operator('object.zb_particle_detail_select', text = '', 
                        icon = 'RENDER_STILL').detailSelect = 'RENDER'
                        deSel = scene.zbParticleDetailSelect
                        if deSel == 'PARTICLE_EDIT':
                            pEdit = scene.tool_settings.particle_edit
                            sub.prop(pEdit, 'draw_step', text = 'Edit Detail', slider = True)                    
                        if deSel == 'OBJECT':      
                            sys = ob.particle_systems.active.settings                 
                            sub.prop(sys, 'draw_step', text = 'Object Detail', slider = True)                    
                        if deSel == 'RENDER':
                            sys = ob.particle_systems.active.settings
                            sub.prop(sys, 'render_step', text = 'Render Detail', slider = True)                        
                        sub = col.column(True)
                        sub.scale_y = 1
                        sub.prop(set, 'child_radius', text = 'Spread', slider=True)  
                        sub.prop(set, 'clump_factor', text = 'Clump', slider=True)
                        sub.prop(set, 'clump_shape', text = 'Clump Shape', slider=True)
                        sub.prop(set, 'roughness_1', text = 'Roughness', slider=True) 
                        sub.prop(set, 'roughness_endpoint', text = 'Ends', slider=True)    
                        sub.prop(set, 'child_length', text = 'Length', slider=True)  
                        sub.separator()
                        sub.separator()
                        sub.separator()
                        sub.prop(set,'kink', text = '')
                        if set.kink != 'NO':
                            if set.kink == 'SPIRAL':
                                sub.prop(set, 'kink_extra_steps', text ='Detail') 
                                sub1 = sub.row(True)
                                sub1.scale_x = 0.175
                                sub1.prop(set, 'kink_axis', text ='')  
                                sub1 = sub1.row(True)
                                sub1.scale_x = 2
                                sub1.prop(set, 'kink_axis_random', text ='Direction') 
                            sub.separator()                        
                            sub.prop(set, 'kink_frequency', slider=True)
                            sub.prop(set, 'kink_amplitude', text = 'Amplitude', slider=True)                          
                            if set.kink != 'SPIRAL':
                                sub.prop(set, 'kink_amplitude_clump', text = 'Kink Clump', slider=True)  
                                sub.separator()
                            sub.prop(set, 'kink_shape', slider=True) 
                            if set.kink != 'SPIRAL':
                                sub.prop(set, 'kink_flat', text = 'Flatness', slider=True)                
                            sub.prop(set, 'kink_amplitude_random', 
                            text = 'Random', slider=True)
                else:
                    col = box.column()
            elif context.sculpt_object and brush:
                capabilities = brush.sculpt_capabilities
                ups = toolsettings.unified_paint_settings
                brushName = bpy.context.tool_settings.sculpt.brush.name
                if 'Decal' in brushName or 'Stencil' in brushName:
                    row = layout.row()
                    texture = bpy.data.brushes[brushName].texture
                    row.prop(texture, "use_color_ramp", text = 'Use As Mask',
                    icon = 'MOD_MASK')
                col = layout.column(align=True)
                row = col.row(align=True)
                if ((ups.use_unified_size and ups.use_locked_size) or
                        ((not ups.use_unified_size) and brush.use_locked_size)):
                    self.prop_unified_size(row, context, brush, "use_locked_size", icon='LOCKED')
                    self.prop_unified_size(row, context, brush, "unprojected_radius", slider=True, text="Radius")
                else:
                    self.prop_unified_size(row, context, brush, "use_locked_size", icon='UNLOCKED')
                    self.prop_unified_size(row, context, brush, "size", slider=True, text="Radius")
                self.prop_unified_size(row, context, brush, "use_pressure_size")
                try:
                    if capabilities.has_strength_pressure:
                        row = col.row(align=True)
                        row.prop(brush, "use_space_attenuation", toggle=True, icon_only=True)
                        self.prop_unified_strength(row, context, brush, "strength", text="Strength")
                        self.prop_unified_strength(row, context, brush, "use_pressure_strength")
                    if capabilities.has_auto_smooth:
                        row = col.row(align=True)
                        row.operator('object.sf_tn', text='',icon='BLANK1')
                        row.prop(brush, "auto_smooth_factor", slider=True)
                        row.prop(brush, "use_inverse_smooth_pressure", toggle=True, text="")
                except:
                    pass
                if capabilities.has_pinch_factor:
                    row = col.row(align=True)
                    row.operator('object.sf_tn', text='',icon='BLANK1')
                    row.prop(brush, "crease_pinch_factor", slider=True, text="Pinch")
                    row.operator('object.sf_tn', text='',icon='BLANK1')
                if capabilities.has_normal_weight:
                    row = col.row(align=True)
                    row.operator('object.sf_tn', text='',icon='BLANK1')
                    row.prop(brush, "normal_weight", slider=True)
                    row.operator('object.sf_tn', text='',icon='BLANK1')
                if brush.sculpt_tool == 'MASK':
                    col.prop(brush, "mask_tool", text="")
                if capabilities.has_height:
                    row = col.row(align=True)
                    row.operator('object.sf_tn', text='',icon='BLANK1')
                    row.prop(brush, "height", slider=True, text="Height")
                    row.operator('object.sf_tn', text='',icon='BLANK1')
                if brush.name == 'Mask':
                    col.separator()
                    if wm.zbViewMaskMode:
                        maskIcon = 'RESTRICT_VIEW_OFF'
                    else:
                        maskIcon = 'RESTRICT_VIEW_ON'
                    col.prop(wm,"zbViewMaskMode", text='View', icon= maskIcon)
                row = col.separator()
                row = col.row(align=True)
                row.label("Brush Stroke")
                row.operator("object.zb_stroke_buttons",
                text ="", icon='MOD_DYNAMICPAINT').shapeTool = 'SPACE'
                row.operator("object.zb_stroke_buttons", text='',
                icon='MOD_CURVE').shapeTool = 'CURVE'
                row.operator("object.zb_stroke_buttons",
                text ="", icon='IPO_LINEAR').shapeTool = 'LINE'
                if not bpy.context.mode.startswith('PAINT_VERTEX'):
                    row.operator("object.zb_stroke_buttons",
                    text ="", icon='PROP_ON').shapeTool = 'ANCHORED'
                if brush.stroke_method == 'LINE':
                    row = col.row(align=True)
                    row.label('(Hold alt to constrain line)')
                if brush.stroke_method == 'CURVE':
                    row = col.separator()
                    row = col.row(align=True)
                    row.template_ID(brush, "paint_curve", new="paintcurve.new")
                    if brush.paint_curve:
                        row = col.separator()
                        row = col.row(align=True)
                        row.label("(Ctrl-Mouse)")
                        row.operator("paintcurve.draw", text="Draw Curve")
                    else:
                        row = col.row(align=True)
                        row.label("(Ctrl-click to make new curve)")
                    row = col.separator()
                row = col.separator()
                row = col.row(align=True)
                sculpt = context.tool_settings.sculpt
                row.scale_y = 0.8
                row.label("Mirror")
                row.separator()
                row.prop(sculpt, "use_symmetry_x", text="X", toggle=True)
                row.prop(sculpt, "use_symmetry_y", text="Y", toggle=True)
                row.prop(sculpt, "use_symmetry_z", text="Z", toggle=True)
                row = col.separator()
                row = col.row()
                row.prop(wm, 'zbHidePaintOptions',
                icon='COLLAPSEMENU', text='More Options',toggle=True)
                if wm.zbHidePaintOptions:
                    row = col.separator()
                    row = col.row(align=True)
                    row.label('Curve')
                    row.operator("brush.curve_preset", icon='SMOOTHCURVE', text="").shape = 'SMOOTH'
                    row.operator("brush.curve_preset", icon='SPHERECURVE', text="").shape = 'ROUND'
                    row.operator("brush.curve_preset", icon='ROOTCURVE', text="").shape = 'ROOT'
                    row.operator("brush.curve_preset", icon='SHARPCURVE', text="").shape = 'SHARP'
                    row.operator("brush.curve_preset", icon='LINCURVE', text="").shape = 'LINE'
                    row.operator("brush.curve_preset", icon='NOCURVE', text="").shape = 'MAX'
                    if capabilities.has_sculpt_plane:
                        col.separator()
                        row = col.row()
                        row = col.row(align=True)
                        row.prop(brush, "use_original_normal", toggle=True, icon_only=True)
                        row.prop(brush, "sculpt_plane", text="")
                    if capabilities.has_plane_offset:
                        row = col.row(align=True)
                        row.operator('object.sf_tn', text='',icon='BLANK1')
                        row.prop(brush, "plane_offset", slider=True)
                        row.prop(brush, "use_offset_pressure", text="")
                        row = col.row(align=True)
                        row.operator('object.sf_tn', text='',icon='BLANK1')
                        row.prop(brush, "plane_trim", slider=True, text="Distance")
                        row.operator('object.sf_tn', text='',icon='BLANK1')
                        row = col.separator()
                        row = col.row(align=True)
                        row.prop(brush, "use_plane_trim", text="Trim", icon='BLANK1')
                    if capabilities.has_persistence:
                        ob = context.sculpt_object
                        do_persistent = True
                        for md in ob.modifiers:
                            if md.type == 'MULTIRES':
                                do_persistent = False
                                break
                        if do_persistent:
                            row = col.row(align=True)
                            row.prop(brush, "use_persistent", icon='BLANK1')
                            row.operator("sculpt.set_persistent_base", text='Set Base')
                    col.separator()
                    col.row().prop(brush, "direction", expand=True)
                    col.separator()
                    row = col.row()
                    row.prop(brush, "use_frontface", text="Front Faces Only")
                    if capabilities.has_accumulate:
                        col.separator()
                        col.prop(brush, "use_accumulate")
            elif context.image_paint_object and brush:
                fu17(self, context, layout, brush, settings, True)
            elif context.weight_paint_object and brush:
                col = layout.column(align=True)
                row = col.row(align=True)
                row.operator('object.sf_tn', text='',icon='BLANK1')
                self.prop_unified_weight(row, context, brush, "weight", slider=True, text="Weight")
                row.operator('object.sf_tn', text='',icon='BLANK1')
                row = col.row(align=True)
                row.operator('object.sf_tn', text='',icon='BLANK1')
                self.prop_unified_size(row, context, brush, "size", slider=True, text="Radius")
                self.prop_unified_size(row, context, brush, "use_pressure_size")
                row = col.row(align=True)
                row.operator('object.sf_tn', text='',icon='BLANK1')
                self.prop_unified_strength(row, context, brush, "strength", text="Strength")
                self.prop_unified_strength(row, context, brush, "use_pressure_strength")
                row = col.row(align=True)
                row = layout.row()
                row = layout.row()
                row.prop(brush, "vertex_tool", text="")
                col = layout.column()
                col.prop(toolsettings, "use_auto_normalize", text="Auto Normalize")
                col.prop(toolsettings, "use_multipaint", text="Multi-Paint")
                brush = bpy.context.tool_settings.weight_paint.brush
                row = col.separator()
                row = col.row(align=True)
                row.label("Brush Stroke")
                row.operator("object.zb_stroke_buttons",
                text ="", icon='MOD_DYNAMICPAINT').shapeTool = 'SPACE'
                row.operator("object.zb_stroke_buttons", text='',
                icon='MOD_CURVE').shapeTool = 'CURVE'
                row.operator("object.zb_stroke_buttons",
                text ="", icon='IPO_LINEAR').shapeTool = 'LINE'
                if brush.stroke_method == 'LINE':
                    row = col.row(align=True)
                    row.label('(Hold alt to constrain line)')
                brush = bpy.context.tool_settings.weight_paint.brush
                if brush.stroke_method == 'CURVE':
                    row = col.separator()
                    row = col.row(align=True)
                    row.template_ID(brush, "paint_curve", new="paintcurve.new")
                    if brush.paint_curve:
                        row = col.separator()
                        row = col.row(align=True)
                        row.label("(Ctrl-Mouse)")
                        row.operator("paintcurve.draw", text="Draw Curve")
                    else:
                        row = col.row(align=True)
                        row.label("(Ctrl-click to make new curve)")
                    row = col.separator()
                row = col.row()
                row = col.row()
                row = col.row(align=True)
                row.scale_y = 0.8
                row.label('Mirror')
                row.separator()
                obData = ob.data
                row.prop(scene, "zbWeightMirror", text='X', toggle=True)
                row.operator("object.sf_tn", text='   Y')
                row.operator("object.sf_tn", text='   Z')
                if len(bpy.data.armatures) > 0:
                    displayWarning = 0
                    try:
                        for mod in ob.modifiers:
                            if mod.type == 'ARMATURE':
                                if mod.object:
                                    if mod.object.mode != 'POSE':
                                        displayWarning = 1
                                        col = layout.column(align=True)  
                                        col.separator()
                                        col = layout.column(align=True)                                
                                        col.scale_y = 0.65
                                        col.label('The armature bones can not')
                                        col.separator()  
                                        col.label('be selected from weight')
                                        col.separator()
                                        col.label('paint mode unless the arm-')
                                        col.separator()    
                                        col.label('-ature is set to pose mode.')
                                        col.separator()
                                        col = layout.column(align=True)
                                        col.scale_y = 2
                                        col.prop(wm,'zbMakeBonesSelectable', toggle=True)
                                        break
                    except:
                        pass 
                    if displayWarning == 0:
                        col = layout.column(align=True)
                        col.separator()
                        col.scale_y = 0.75
                        col.label('Ctrl-Click to select bones')
                        col.label('Shift-Ctrl-Click for multiple')
            elif context.vertex_paint_object and brush:
                fu17(self, context, layout, brush, settings, True)
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
def zbMakeBonesSelectable(self,context):    
    if self.zbMakeBonesSelectable:
        scene = bpy.context.scene    
        ob = bpy.context.active_object
        arm = 0
        if ob:
            if ob.modifiers:
                for mod in ob.modifiers:
                    if mod.type == 'ARMATURE':
                        if mod.object:
                            arm = mod.object
                            break    
        if arm:
            scene.objects.active = arm
            arm.select = True
            bpy.ops.object.mode_set(mode='POSE')
        ob.select = True
        scene.objects.active = ob
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        self.zbMakeBonesSelectable = False
def zbSelectParticleMat(self,context):
    ob = bpy.context.active_object        
    parSys = ob.particle_systems.active
    set = parSys.settings    
    mats = bpy.data.materials   
    newMat = bpy.data.materials[self.zbSelectParticleMat]
    if len(ob.data.materials) < 1:
        if len(ob.material_slots) == 0:
            bpy.ops.object.material_slot_add()
    if newMat.name not in ob.data.materials:        
        ob.data.materials.append(newMat)            
    if set.material_slot != newMat.name:
        set.material_slot = newMat.name
    self.zbSelectParticleMat = ''
class zbPaint(bpy.types.Panel):
    bl_label =i_0[121]
    bl_space_type =i_0[122]
    bl_region_type =i_0[123]
    def draw(self, context):
        layout = self.layout
        wm = context.window_manager
        scene = bpy.context.scene
        sd = bpy.context.space_data
        ob = bpy.context.image_paint_object
        re = bpy.context.scene.render.engine
        mode = bpy.context.mode
        if fu20():
            layout = self.layout
            row = layout.row(True)
            row.scale_y = .6
            row.scale_x = 1.75
            row.operator("object.zb_mode_buttons", text="", icon='OBJECT_DATA').modeButton  = 1
            row.operator("object.zb_mode_buttons", text="", icon='SCULPTMODE_HLT').modeButton  = 2
            row.operator("object.zb_mode_buttons", text="", icon='BRUSH_DATA').modeButton  = 3
            row.operator("object.zb_mode_buttons", text="", icon='PARTICLEMODE').modeButton = 4
            sub = row.row(True)
            sub.scale_y = .6
            sub.scale_x = 1.25
            sub.operator("wm.call_menu", text="", icon='BLANK1').name = "view3D.zb_layer_options_menu"
            sub = sub.row(True)
            sub.scale_y = .6
            sub.scale_x = 4
            sub.operator("screen.screen_full_area", text="", icon='FULLSCREEN_ENTER')
            row = layout.row(True)
            if mode == 'PAINT_TEXTURE':
                special= 0
                spacer = 0
                col = layout.column()
                row = layout.row(align=True)
                if ob.active_material:
                    n = ob.active_material.name
                    if 'ZB Painted' in n or 'ZBA Painted' in n:
                        row.label('Alchemy Mode (no switching)',icon = 'BOOKMARKS')
                    else:    
                        row.label('Blending Mode')
                        sub = row.row(align=True)
                        sub.scale_x = 0.7
                        sub.prop(scene, "zbGoCycles", icon='NODETREE', text="Cycles")
                col = layout.column(align=True)
                mat = ob.active_material
                ts = mat.texture_slots[mat.active_texture_index]
                if re != 'CYCLES':
                    if ts: 
                        col.prop(ts,'blend_type',text='', icon = 'POTATO')
                        if ts.use_map_diffuse:
                            spacer += 1
                            col.prop(ts,'diffuse_factor', text = "Color Brightness", slider = True)
                        if ts.use_map_color_diffuse:
                            spacer += 1
                            col.prop(ts,'diffuse_color_factor', text = "Layer Opacity", slider = True)
                        if ts.use_map_translucency:
                            spacer += 1
                            col.prop(ts,'translucency_factor', text = "Translucency", slider = True)
                        if ts.use_map_specular:
                            spacer += 1
                            col.prop(ts,'specular_factor', text = "Specular", slider = True)
                        if ts.use_map_color_spec:
                            spacer += 1
                            col.prop(ts,'specular_color_factor', text = "Shininess", slider = True)
                        if ts.use_map_hardness:
                            spacer += 1
                            col.prop(ts,'hardness_factor', text = "Hardness", slider = True)
                        if ts.use_map_alpha:
                            spacer += 1
                            col.prop(ts,'alpha_factor', text = "Transparency", slider = True)
                        if ts.use_map_normal:
                            try:
                                if ts.texture.use_normal_map:
                                    theText = 'Normal'
                                else:
                                    theText = 'Bumpiness'
                                spacer += 1
                                col.prop(ts,'normal_factor', text = theText, slider = True)
                            except:
                                pass
                        if ts.use_map_warp:
                            spacer += 1
                            col.prop(ts,'warp_factor', text = "Warp", slider = True)
                        if ts.use_map_displacement:
                            spacer += 1
                            col.prop(ts,'displacement_factor', text = "Displacement",  slider = True)
                        if ts.use_map_ambient:
                            spacer += 1
                            col.prop(ts,'ambient_factor', text = "Ambient", slider = True)
                        if ts.use_map_emit:
                            spacer += 1
                            col.prop(ts,'emit_factor', text = "Emit", slider = True)
                        if ts.use_map_mirror:
                            spacer += 1
                            col.prop(ts,'mirror_factor', text = "Mirror", slider = True)
                        if ts.use_map_raymir:
                            spacer += 1
                            col.prop(ts,'raymir_factor', text = "Ray Mirror", slider = True)
                    else:
                        special = 1
                        col.label('Cycles materials not created')
                        col.label('with Zero Brush can not be')
                        col.label('converted to Blender Render')
                        col.label('materials. Adding new layers')
                        col.label('may cause unexpected results.')
                        col.label('')
                else:
                    if ts:
                        name = ts.texture.image.name
                        if "color" in name.lower() or "transparent" in name.lower() or "alpha" in name.lower():
                            if 'specular' not in name.lower():
                                try:
                                    node = mat.node_tree.nodes['Mix zbColor']
                                    col.prop(node, "blend_type", text="", icon='POTATO')
                                except:
                                    pass
                                try:
                                    node = mat.node_tree.nodes['Mixed1']
                                    col.prop(node.inputs['Fac'], "default_value", text="Reflectivity")
                                    spacer +=1
                                except:
                                    pass
                                try:
                                    node = mat.node_tree.nodes['Glossy BSDF zbColor']
                                    col.prop(node.inputs['Roughness'], "default_value", text="Roughness")
                                    spacer +=1
                                except:
                                    pass
                                try:
                                    node = mat.node_tree.nodes['Mixed2']
                                    col.prop(node.inputs['Fac'], "default_value", text="Light Emission")
                                    spacer +=1
                                except:
                                    pass
                                try:
                                    node = mat.node_tree.nodes['Mixed3']
                                    col.prop(node.inputs['Fac'], "default_value", text="Transparency")
                                    spacer +=1
                                except:
                                    pass
                                col.separator()
                                col.separator()
                                try:
                                    node = mat.node_tree.nodes['Math zbColor']
                                    col.prop(node.inputs[1], "default_value", text="Bumpiness")
                                    spacer +=1
                                except:
                                    pass
                                try:
                                    node = mat.node_tree.nodes['Bright/Contrast zbColor']
                                    col.prop(node.inputs['Bright'], "default_value", text="Brightness")
                                    spacer +=1
                                except:
                                    pass
                                try:
                                    node = mat.node_tree.nodes['Bright/Contrast zbColor']
                                    col.prop(node.inputs['Contrast'], "default_value", text="Contrast")
                                    spacer +=1
                                except:
                                    pass
                        if "bump" in name.lower():
                            try:
                                node = mat.node_tree.nodes['Math zbBump']
                                col.prop(node, "operation", text = "", icon="POTATO")
                            except:
                                pass
                            try:
                                node = mat.node_tree.nodes['Math zbBump']
                                col.prop(node.inputs[1],"default_value", text="Bumpiness")
                                spacer +=1
                            except:
                                pass
                            col.separator()
                            col.separator()
                            try:
                                node = mat.node_tree.nodes['Bright/Contrast zbBump']
                                col.prop(node.inputs['Bright'], "default_value", text="Brightness")
                                spacer +=1
                            except:
                                pass
                            try:
                                node = mat.node_tree.nodes['Bright/Contrast zbBump']
                                col.prop(node.inputs['Contrast'], "default_value", text="Contrast")
                                spacer +=1
                            except:
                                pass
                        if "specular" in name.lower():
                            try:
                                node = mat.node_tree.nodes['Mix zbSpecular']
                                col.prop(node, "blend_type", text="", icon='POTATO')
                            except:
                                pass
                            try:
                                node = mat.node_tree.nodes['Glossy BSDF zbSpecular']
                                col.prop(node.inputs['Roughness'], "default_value", text="Roughness")
                                spacer +=1
                            except:
                                pass
                            try:
                                node = mat.node_tree.nodes['Math zbSpecular']
                                col.prop(node.inputs[1], "default_value", text="Shininess")
                                spacer +=1
                            except:
                                pass
                            col.separator()
                            col.separator()
                            try:
                                node = mat.node_tree.nodes['Bright/Contrast zbSpecular']
                                col.prop(node.inputs['Bright'], "default_value", text="Brightness")
                                spacer +=1
                            except:
                                pass
                            try:
                                node = mat.node_tree.nodes['Bright/Contrast zbSpecular']
                                col.prop(node.inputs['Contrast'], "default_value", text="Contrast")
                                spacer +=1
                            except:
                                pass
                        if "glow" in name.lower():
                            try:
                                node = mat.node_tree.nodes['Mix zbGlow']
                                col.prop(node, "blend_type", text="", icon='POTATO')
                            except:
                                pass
                            try:
                                node = mat.node_tree.nodes['Emission zbGlow']
                                col.prop(node.inputs['Strength'], "default_value",text="Strength")
                                spacer +=1
                            except:
                                pass
                            try:
                                node = mat.node_tree.nodes['Math zbGlow']
                                col.prop(node.inputs[1], "default_value",text="Intensity")
                                spacer +=1
                            except:
                                pass
                        if "normal" in name.lower():   
                            if 'bump' not in name.lower():
                                try:
                                    node = mat.node_tree.nodes['Mix zbColor']
                                    col.prop(node, "blend_type", text="", icon='POTATO')
                                except:
                                    pass
                                try:
                                    node = mat.node_tree.nodes['Normal Map zbNormal']
                                    col.prop(node.inputs[0], "default_value", text="Normal")
                                    spacer +=1
                                except:
                                    pass
                if spacer == 0:
                    if re == 'CYCLES':
                        col.label('ZB Full Version required to con-')
                        col.label('-vert Blender Render materials')  
                        col.label('not painted with ZB to Cycles.') 
                        col.separator()
                        col.label('Cannot display sliders for')
                        col.label('Cycles materials not created')  
                        col.label('with Zero Brush. Adding layers') 
                        col.label('via the ZB layer menu may')
                        col.label('produce unexpected results.')      
                        col.separator()
                    else:
                        spc = 32
                        if special == 0:
                            col.separator()
                            col.separator()
                        else:
                            col.separator()
                            col.separator()
                            spc = 8
                        for x in range(spc):
                            row = layout.row()
                if spacer == 1:
                    col.separator()
                    col.separator()
                    for x in range(24):
                        row = layout.row()
                if spacer == 2:
                    col.separator()
                    col.separator()
                    for x in range(20):
                        row = layout.row()
                if spacer == 3:
                    for x in range(16):
                        row = layout.row()
                if spacer == 4:
                    for x in range(12):
                        row = layout.row()
                row = layout.row(align=True)
                row = layout.row(align=True)
                row.scale_y = 1.5
                row.operator("wm.call_menu", icon = "COLLAPSEMENU",text="Options").name = "view3D.zb_layer_options_menu"
                row.prop(wm, "zbPaintThrough", text = "", icon ="TPAINT_HLT")
                if re != 'CYCLES':
                    if mat is not None:
                        row.prop(mat, "use_shadeless", text = "", icon ="TEXTURE_SHADED")
                else:
                    row.prop(scene, "zbQuickLights", text = "", icon ='LAMP_SUN')
                if sd.viewport_shade != 'RENDERED':
                    zbRendIcon = "MATERIAL"
                else:
                    zbRendIcon = "SMOOTH"
                row.operator("object.zb_render_prev", text="", icon = zbRendIcon)
                row.operator("object.zb_reset_uvs", text = "", icon ="FILE_REFRESH")
                row = layout.row()
                if sd.viewport_shade == 'RENDERED':
                    row.scale_y = 0.8
                    row.label('(Ctrl-B set preview border)')
                i = -1 
                for t in mat.texture_slots:
                    i+=1
                    try:
                        if t.texture.type =='IMAGE':
                            row = layout.row(align= True)
                            if t.texture == mat.active_texture:
                                ai =  'BRUSH_DATA'
                            else:
                                ai = 'BLANK1'
                            row.operator('object.zb_set_active_layer',
                                text = "", icon = ai).tex_index =i
                            row.prop(t.texture,'name', text = "")
                            if t.use:
                                ic = 'RESTRICT_VIEW_OFF'
                            else:
                                ic = 'RESTRICT_VIEW_ON'
                            if t.texture == mat.active_texture:
                                if len(mat.texture_slots.items()) > 1:
                                    row.operator("object.zb_move_texture", text = "",icon = "TRIA_UP").tex_move_up = 1
                                    row.operator("object.zb_move_texture", text = "",icon = "TRIA_DOWN").tex_move_down = 1
                                else:
                                    row.operator("object.zb_mode_buttons", text = "",icon = "TRIA_UP").modeButton = 100
                                    row.operator("object.zb_mode_buttons", text = "",icon = "TRIA_DOWN").modeButton = 100
                            row.operator("object.zb_delete_texture", text = "",icon = "X").tex_kill = i
                            if re != 'CYCLES':
                                row.prop(t,'use', text = "",icon = ic)
                            else:
                                row.operator('object.sf_tn',text='',icon='BLANK1')
                    except:
                        pass
                row = layout.row()
                row = layout.row()
                col = layout.column(align = True)
                box = col.box()
                sub = box.column(True)
                sub.operator("object.zb_paint_color", icon='TEXTURE')
                sub.operator("object.zb_paint_bump", icon='TEXTURE')
                sub.operator("object.zb_paint_specular", icon='TEXTURE')
                sub.operator("object.zb_paint_glow", icon='TEXTURE')
                sub = box.column()
                sub = box.column(True)
                sub.operator("object.zb_paint_transparent", icon='TEXTURE')
                sub.operator("object.zb_alpha_mask", icon='TEXTURE')
                multires = len([mod for mod in ob.modifiers if mod.type == 'MULTIRES'])
                sub = box.column()
                sub = box.column(True)
                sub.prop(scene, "zbImgSize")
                sub = sub.row(align=True)
                sub.scale_x = 1.2
                sub.prop(wm,'zbSaveLayerOptions',text='',icon='FILE_FOLDER')
                sub.operator("object.zb_save_layers")
                sub = box.column()
                if wm.zbSaveLayerOptions:
                    sub.scale_y = 0.5
                    sub.label('Save images to a folder')
                    sub.label('instead of internally')
                    sub = box.column()
                    sub.scale_y = 1
                    sub.prop(scene,'zbSaveToHardDrive',
                    text='Save To Hard Drive')
                    sub.prop(wm, 'zbSaveImagePath',text='')
                    sub = box.column(True)
                    sub = sub.row(align=True)
                    sub.label('as:')
                    sub.prop_enum(wm,"zbSaveType",value = '.PNG')
                    sub.prop_enum(wm,"zbSaveType",value = '.TIFF')
                    sub.prop_enum(wm,"zbSaveType",value = '.JPEG')
                    sub = box.column()
                    sub = sub.row()
                if scene.zbSaveToHardDrive:
                    sub.scale_y = 1.3
                    sub.operator('object.zb_reload_all_images',
                    text='Reload All Images', icon='FILE_REFRESH')
                    sub = box.column()
            if mode.startswith('SCULPT'):
                col = layout.column(align=True)
                ob = bpy.context.active_object
                multires = len([mod for mod in ob.modifiers if mod.type == 'MULTIRES'])
                dynamic = bpy.context.active_object.use_dynamic_topology_sculpting
                if not multires and not dynamic:
                    col.operator("object.zb_multires_add")
                    col.operator("object.zb_sculpt_dynamic")
                if multires:
                    row = col.row(align = True)
                    row.label("Detail")
                    row.operator("object.zb_sub_multires", text='more')
                    row.operator("object.zb_reset_detail", text='',icon ='FILE_REFRESH')
                    row.operator("object.zb_multires_down", text='less')
                    row = layout.row(align=True)
                    row.operator("object.zb_generate_base_mesh", text="Apply")
                    row = layout.row()
                if dynamic:
                    row = col.row(align = True)
                    row.operator("object.zb_generate_base_mesh", text="Apply Detail")
                    sub = col.row(align=True)
                    sub.operator("sculpt.sample_detail_size", text="", icon='EYEDROPPER')
                    toolsettings = context.tool_settings
                    sculpt = toolsettings.sculpt
                    sub.prop(sculpt, "constant_detail")
            if mode.startswith('PARTICLE'):
                ob = context.active_object
                if ob:                
                    sys = ob.particle_systems                
                    if sys:
                        row = layout.row()
                        row = layout.row()
                        row.template_list("PARTICLE_UL_particle_systems", "particle_systems", ob, "particle_systems",
                                  ob.particle_systems, "active_index", rows=1, maxrows = 25)
                        if sys.active:
                            col = layout.column()
                            row = col.row(True)
                            row.operator("object.zb_add_strands", text="New").option = 'NEW'
                            row.operator("object.zb_add_strands", text="Copy").option = 'COPY'
                            row.operator("object.particle_system_remove", text="Delete")
                            col = layout.column(True)
                            col.separator()
                            col.label('Layer Options')
                            col.separator()
                            col.prop(sys.active,'use_hair_dynamics', toggle = True,
                            icon = 'PHYSICS', text = 'Animate Strands')  
                            col.separator()
                            col.separator()
                            sub1 = col.row(True)     
                            sub1.scale_x = 0.11      
                            sub1.prop_search(wm, "zbSelectParticleMat", bpy.data, "materials",
                            text = '',icon="MATERIAL_DATA")
                            sub1 = sub1.row(True)
                            sub1.scale_x = 5
                            sub1.operator('object.zb_add_strands', 
                            text = 'Add Basic Material').option = 'ADD_BASIC_MATERIAL'
                            parMat = sys.active.settings.material_slot
                            sub = col.row(True)
                            sub.scale_x = 0.15
                            if parMat in ob.data.materials:                            
                                if len(ob.material_slots) > 1:
                                    parMat = bpy.data.materials[parMat]
                                    chngCol = True                            
                                    if re == 'CYCLES':
                                        if parMat.node_tree.nodes:
                                            try:
                                                nodeHair = parMat.node_tree.nodes['Hair BSDF']
                                                sub.prop(nodeHair.inputs['Color'], 'default_value',
                                                text = '')
                                            except:
                                                chngCol = False
                                    else:                                    
                                        if parMat.strand.use_tangent_shading:
                                            sub.prop(parMat, 'diffuse_color',text = '')
                                        else:
                                            chngCol = False
                                    if chngCol:
                                        sub = sub.row(True)
                                        sub.scale_x = 2
                                        sub.operator('object.zb_add_strands',
                                        text = 'Apply Color').option = 'CHANGE_COLOR'
                            col.separator()
                            col.separator()
            if mode.startswith('OBJECT'):
                if wm.showBrushLayerOptions:
                    for mat in bpy.data.materials:
                        if '_zb_proxy' in mat.name:
                            slot = mat.texture_slots[0]
                            break
                    col = layout.column()
                    sub = layout.column(align=True)
                    sub.scale_y = 1.4
                    sub.operator('object.zb_layer_from_brush',
                    icon='FILE_TICK',text='Finish Brush Layer').action = ''
                    sub = sub.column(align=True)
                    sub.scale_y = 1
                    sub.operator('object.zb_layer_from_brush',
                    icon='CANCEL', text='Cancel').action = 'cancel'
                    row = layout.row()
                    row.operator('object.zb_layer_from_brush', text='Re-Apply Brush').action = 'flip'
                    row = layout.row()
                    row.column().prop(slot, "offset", text= 'Position')
                    row.column().prop(slot, "scale", text='Scale')
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
def fu19(scene):
    try:
        bpy.ops.object.zb_save_layers(save_only_active=False)
    except:
        pass
class cl39(bpy.types.Operator):
    bl_idname =i_0[124]
    bl_label =i_0[125]
    def execute(self,context):
        scene = bpy.context.scene
        wm = bpy.context.window_manager
        if scene.zbSaveWhenSave:
            bpy.app.handlers.save_pre.append(fu19)
        for map in wm.keyconfigs.addon.keymaps:      
            ki = map.keymap_items                            
            for key in ki:
                if 'ZB Init Listener' in key.name:
                    key.active = False                                         
        return{'FINISHED'}
def zbWeightMirror(self,context):
    scene = bpy.context.scene
    wm = bpy.context.window_manager    
    km = wm.keyconfigs.addon.keymaps['Weight Paint']
    kmi = km.keymap_items["paint.zb_select_weight_mirror"]
    ob = bpy.context.active_object        
    if ob:
        if self.zbWeightMirror:            
            kmi.active = True
            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')        
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.normals_make_consistent()
            bpy.ops.mesh.symmetry_snap()                        
            bpy.ops.object.mode_set(mode='WEIGHT_PAINT')        
            ob.data.use_mirror_x = True
            ob.data.use_mirror_topology = False
            scene.tool_settings.use_multipaint = True
            if ob.modifiers:
                for mod in ob.modifiers:
                    if mod.type == 'ARMATURE':
                        if mod.object:
                            arm = mod.object.data                            
                            activeBone = arm.bones.active
                            mirrorBone = ''
                            if activeBone:
                                if '.l' in activeBone.name:
                                    mirrorBone = activeBone.name.replace('.l','.r')
                                if '.r' in activeBone.name:
                                    mirrorBone = activeBone.name.replace('.r','.l')
                            if mirrorBone:
                                arm.bones[mirrorBone].select = True                                                               
                        break
        else:            
            kmi.active = False
            ob.data.use_mirror_x = False
            ob.data.use_mirror_topology = False
            scene.tool_settings.use_multipaint = False
class cl40(bpy.types.Operator):
    bl_idname =i_0[126]
    bl_label =i_0[127]
    def execute(self,context):            
        scene = bpy.context.scene        
        bpy.ops.view3d.select('INVOKE_DEFAULT')
        ob = bpy.context.active_object
        if ob.modifiers:
            for mod in ob.modifiers:
                if mod.type == 'ARMATURE':
                    if mod.object:
                        arm = mod.object.data                            
                        activeBone = arm.bones.active
                        mirrorBone = ''
                        if activeBone:
                            if '.l' in activeBone.name:
                                mirrorBone = activeBone.name.replace('.l','.r')
                            if '.r' in activeBone.name:
                                mirrorBone = activeBone.name.replace('.r','.l')
                        if mirrorBone:
                            arm.bones[mirrorBone].select = True                                                               
                    break                
        if scene.tool_settings.use_multipaint:
            scene.tool_settings.use_multipaint = True        
        return{'FINISHED'}
class cl41(bpy.types.Operator):
    bl_idname =i_0[128]
    bl_label =i_0[129]
    bl_description =i_0[130]
    message = bpy.props.StringProperty()
    def execute(self, context):
        message = self.message
        if len(message) > 0:
            self.report({'INFO'}, message)
        else:
            self.report({'INFO'}, "This option is not available")
        pass
        return {'FINISHED'}
class cl42(bpy.types.PropertyGroup):
    wm = bpy.types.WindowManager
    scene = bpy.types.Scene
    text1 = 'Pressing this will mirror the weight paint of your object along the '
    text2 = 'X axis (if mesh is properly symmetrical). It will also activate, '
    text3 = '"Multi-Paint" option so you can select the bone (and opposite mirrored '
    text4 = 'bone), so you can see the effects of the mirror painting.'
    text5 = text1+text2+text3+text4
    scene.zbWeightMirror = bpy.props.BoolProperty(
    name = 'X Axis Mirror Editing',
    description = text5,
    default = False,
    update = zbWeightMirror
    )
    wm.zbMakeBonesSelectable = bpy.props.BoolProperty(
    name = 'Make Bones Selectable',
    description = 'Press this if unable to select bones while weight painting',
    default = False,
    update = zbMakeBonesSelectable
    )
    wm.zbLastObjectMode = bpy.props.StringProperty()
    wm.zbSelectParticleMat = bpy.props.StringProperty(
    name = 'Select Material',
    description = 'Select a material to use for this particle layer.',
    default = '',
    update = zbSelectParticleMat
    )
    scene.zbParticleDetailSelect = bpy.props.StringProperty(
    default = 'PARTICLE_EDIT'
    )
    scene.zbAutoConvertLamps = bpy.props.BoolProperty(default = False,
    description = 'Auto convert lamps to work for both Cycles and Blender \
 Render when switching between the two engines.')
    wm.zbGradientSwitch = bpy.props.BoolProperty(
    default= False,
    description= 'Switch between gradient and color wheel modes',
    update = zbGradientSwitch
    )
    wm.zbBeforeGradBrush = bpy.props.StringProperty()
    wm.zbLampBufferSize = bpy.props.IntProperty(default=0)
    wm.zbSaveLayerOptions = bpy.props.BoolProperty(default = False)
    scene.zbSaveToHardDrive = bpy.props.BoolProperty(default = False,
    description='Save images dynamically to a folder on your\
 hard drive so you can export or edit them externaly')
    wm.zbSaveImagePath = bpy.props.StringProperty(
    name = "ZB Save Image Path",
    description = "Choose path to save images to disk",
    subtype = 'DIR_PATH',
    update = fu12)
    wm.zbNewSavePath = bpy.props.BoolProperty()
    wm.zbSaveType = bpy.props.EnumProperty(
        update = zbSaveType,
        items=(
            ('.PNG', ".PNG", "",'NONE', 0),
            ('.TIFF', ".TIFF", "",'NONE', 1),
            ('.JPEG', ".JPEG", "",'NONE', 2),
        ))
    txt1 = 'Use "Lightmap Pack" to create the object uv map instead of '
    txt2 = '"Smart UV Project" (if no seams or existing uv-map found).'
    scene.zbUseLightMap = bpy.props.BoolProperty(default = False,
    description = txt1+txt2
    )
    wm.zbLastBrushBlend = bpy.props.StringProperty(
    name = "Last Brush Blend Mode",
    default = "MIX")
    scene.zbImgSize = bpy.props.FloatProperty(
    name="New Layer Size",
    description = "The size of the next layer you add (width and height)",
    default = 2048,
    min = 64,
    precision = 0,
    step = 6400)
    wm.zbHidePaintOptions = bpy.props.BoolProperty(
    description = 'Expand Brush Options')
    wm.showBrushLayerOptions = bpy.props.BoolProperty(default=False)
    scene.zbAutoSaveLayers = bpy.props.BoolProperty(
    name = "Auto Save layers", description = "Autosave paint layers when exiting\
 texture paint mode (via ZB's mode selection menu)",
    default = True)
    scene.zbSaveWhenSave = bpy.props.BoolProperty(
    name = 'Autosave (with file)',
    description = 'Ensure that layer images are saved whenever saving the Blend file',
    default = True
    )   
    wm.zbPaintThrough = bpy.props.BoolProperty(
    name = "Paint Through", description = "Paint or erase all the way through your object",
    update = fu13)
    scene.zbDisableShadows = bpy.props.BoolProperty(
    name = "Disable Shadows",
    default = True,
    description = "Disable shadows from lamps in this scene", update = fu13)
    scene.zbFastMode = bpy.props.BoolProperty(
    name = "Fast Mode Toggle", description = "Speed up performance in the 3D Viewport by lowering detail accross the scene",
    update = fu8)
    wm.zbViewMaskMode = bpy.props.BoolProperty(
    name = "View Mask Mode", description = "view your mask brush strokes",
    update = fu6)
    wm.zbUseBrushColor = bpy.props.BoolProperty(
    name = "Use Brush Color", description = "Use your brush's current color\
 as the base color for your next new layer")
    scene.zbLoadImgSculpt = bpy.props.BoolProperty(
    name = "Texture And Sculpt Brush", description = "Load brushes for sculpt\
 and texture paint modes instead of just the mode you're using")
    scene.zbGoCycles = bpy.props.BoolProperty(
    name = "Change To Cycles",
    description = "Switch between Cycles and Blender Internal Render Engine",
    update = fu16)
    scene.zbQuickLights = bpy.props.BoolProperty(
    name = "ZB Quick Lights",
    description = '"Quick Lights" Sets up a simple light rig and settings\
 for testing and rendering in Cycles',
    update = fu14)
    scene.zbLastWorld = bpy.props.StringProperty(
    name = "ZB Last World", description = "Remember the last world child",)
def fu20():
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
def fu21(kmi_props, attr, value):
    try:
        setattr(kmi_props, attr, value)
    except:
        pass
def register():
    bpy.utils.register_module(__name__)
    try:
        wm = bpy.context.window_manager
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("screen.sf_zb_init_listener", 'MOUSEMOVE', 'ANY')        
        kmi = km.keymap_items.new("wm.call_menu", 'Q','PRESS')
        fu21(kmi.properties, 'name', 'view3D.zb_layer_options_menu')
        km = wm.keyconfigs.addon.keymaps.new(name='Sculpt', space_type='EMPTY')
        kmi = km.keymap_items.new("wm.call_menu", 'SPACE','PRESS')
        fu21(kmi.properties, 'name', 'menu.zb_brush_menu')
        kmi = km.keymap_items.new("object.zb_sub_multires", 'W','PRESS')
        kmi = km.keymap_items.new('sculpt.zb_stroke_smooth', 'LEFTMOUSE', 'PRESS', ctrl=True)
        kmi = km.keymap_items.new('sculpt.zb_stroke_inverse', 'LEFTMOUSE', 'PRESS', shift=True)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS')
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.sculpt.brush.size')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.size')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_size')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.sculpt.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.sculpt.brush.cursor_color_add')
        fu21(kmi.properties, 'image_id', 'tool_settings.sculpt.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', shift=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.sculpt.brush.strength')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.strength')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_strength')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.sculpt.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.sculpt.brush.cursor_color_add')
        fu21(kmi.properties, 'image_id', 'tool_settings.sculpt.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', ctrl=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.sculpt.brush.texture_slot.angle')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.sculpt.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.sculpt.brush.cursor_color_add')
        fu21(kmi.properties, 'image_id', 'tool_settings.sculpt.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        km = wm.keyconfigs.addon.keymaps.new(name='Image Paint', space_type='EMPTY', modal=False)
        kmi = km.keymap_items.new("wm.call_menu", 'SPACE','PRESS')
        fu21(kmi.properties, 'name', 'menu.zb_brush_menu')
        kmi = km.keymap_items.new("paint.zb_erase_paint", 'LEFTMOUSE','PRESS', shift=True)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS')
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.image_paint.brush.size')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.size')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_size')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.image_paint.brush.mask_texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.image_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'fill_color_path', 'tool_settings.image_paint.brush.color')
        fu21(kmi.properties, 'zoom_path', 'space_data.zoom')
        fu21(kmi.properties, 'image_id', 'tool_settings.image_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', shift=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.image_paint.brush.strength')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.strength')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_strength')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.image_paint.brush.mask_texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.image_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'fill_color_path', 'tool_settings.image_paint.brush.color')
        fu21(kmi.properties, 'image_id', 'tool_settings.image_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', ctrl=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.image_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.image_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.image_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'fill_color_path', 'tool_settings.image_paint.brush.color')
        fu21(kmi.properties, 'image_id', 'tool_settings.image_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', ctrl=True, alt=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.image_paint.brush.mask_texture_slot.angle')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.image_paint.brush.mask_texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.image_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'fill_color_path', 'tool_settings.image_paint.brush.color')
        fu21(kmi.properties, 'image_id', 'tool_settings.image_paint.brush')
        fu21(kmi.properties, 'secondary_tex', True)
        kmi = km.keymap_items.new('paint.sample_color', 'I', 'PRESS')
        kmi = km.keymap_items.new('paint.brush_colors_flip', 'C', 'PRESS')
        km = wm.keyconfigs.addon.keymaps.new(name='Vertex Paint', space_type='EMPTY')
        kmi = km.keymap_items.new("wm.call_menu", 'SPACE','PRESS')
        fu21(kmi.properties, 'name', 'menu.zb_brush_menu')
        kmi = km.keymap_items.new("paint.zb_erase_paint", 'LEFTMOUSE','PRESS', shift=True)
        kmi = km.keymap_items.new("paint.zb_erase_paint", 'LEFTMOUSE','PRESS', ctrl=True)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS')
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.vertex_paint.brush.size')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.size')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_size')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.vertex_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.vertex_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'fill_color_path', 'tool_settings.vertex_paint.brush.color')
        fu21(kmi.properties, 'image_id', 'tool_settings.vertex_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', shift=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.vertex_paint.brush.strength')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.strength')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_strength')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.vertex_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.vertex_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'fill_color_path', 'tool_settings.vertex_paint.brush.color')
        fu21(kmi.properties, 'image_id', 'tool_settings.vertex_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', ctrl=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.vertex_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.vertex_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.vertex_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'fill_color_path', 'tool_settings.vertex_paint.brush.color')
        fu21(kmi.properties, 'image_id', 'tool_settings.vertex_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('paint.sample_color', 'I', 'PRESS')
        km = wm.keyconfigs.addon.keymaps.new(name='Weight Paint', space_type='EMPTY')
        kmi = km.keymap_items.new("paint.zb_select_weight_mirror", 'SELECTMOUSE', 'PRESS', ctrl = True)
        kmi.active = False
        kmi = km.keymap_items.new("wm.call_menu", 'SPACE','PRESS')
        fu21(kmi.properties, 'name', 'menu.zb_brush_menu')
        kmi = km.keymap_items.new("paint.zb_erase_paint", 'LEFTMOUSE','PRESS', shift=True)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS')
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.weight_paint.brush.size')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.size')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_size')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.weight_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.weight_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'image_id', 'tool_settings.weight_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        kmi = km.keymap_items.new('wm.radial_control', 'X', 'PRESS', shift=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.weight_paint.brush.strength')
        fu21(kmi.properties, 'data_path_secondary', 'tool_settings.unified_paint_settings.strength')
        fu21(kmi.properties, 'use_secondary', 'tool_settings.unified_paint_settings.use_unified_strength')
        fu21(kmi.properties, 'rotation_path', 'tool_settings.weight_paint.brush.texture_slot.angle')
        fu21(kmi.properties, 'color_path', 'tool_settings.weight_paint.brush.cursor_color_add')
        fu21(kmi.properties, 'image_id', 'tool_settings.weight_paint.brush')
        fu21(kmi.properties, 'secondary_tex', False)
        km = wm.keyconfigs.addon.keymaps.new(name='Paint Curve', space_type='EMPTY')
        kmi = km.keymap_items.new("paintcurve.add_point_slide", 'LEFTMOUSE','PRESS', ctrl=True)
        km = wm.keyconfigs.addon.keymaps.new(name='Particle', space_type='EMPTY')
        kmi = km.keymap_items.new("wm.call_menu", 'SPACE','PRESS')
        fu21(kmi.properties, 'name', 'menu.zb_brush_menu')
        kmi = km.keymap_items.new("wm.radial_control", 'X','PRESS')
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.particle_edit.brush.size')
        kmi = km.keymap_items.new("wm.radial_control", 'X','PRESS', shift=True)
        fu21(kmi.properties, 'data_path_primary', 'tool_settings.particle_edit.brush.strength')
        km = wm.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new("object.zb_render_prev", 'Z','PRESS', shift = True)
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