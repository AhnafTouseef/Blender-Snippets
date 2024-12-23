#import bpy.utils.previews
import bpy
 
icons = bpy.utils.previews.new()

icons.load(name='CUBE', path=r'C:\Users\lenovo\Downloads\0442fe6060be23664a9b049d1e56c8c6.jpeg', path_type='IMAGE')

class OBJECT_PT_CustomPanel(bpy.types.Panel):
    bl_label = "Custom Mesh Panel"
    bl_idname = "PT_CustomPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    bl_context = "objectmode"
 
    def draw(self, context):
        self.layout.template_icon(icon_value=icons["CUBE"].icon_id, scale=8.0)
        self.layout.operator(operator='mesh.primitive_cube_add', text='Add Cube', icon_value=icons['CUBE'].icon_id, )
       
def register():
    bpy.utils.register_class(OBJECT_PT_CustomPanel)

def unregister():
    bpy.utilspreviews.remove(icons)
    
if __name__=="__main__":
    register()
