import bpy
import subprocess

class MeshSubMenu(bpy.types.Menu):
    bl_label = "Mesh Submenu"
    bl_idname = "VIEW3D_MT_mesh_submenu"

    def draw(self, context):
        layout = self.layout

        col = layout.column(align=True)
        col.label(text="Mesh Options")

        row = layout.row(align=True)

        col = row.column()
        col.operator("mesh.primitive_cube_add", text="Cube")
        col.operator("mesh.primitive_cylinder_add", text="Cylinder")

        col = row.column()
        col.operator("mesh.primitive_cone_add", text="Cone")
        col.operator("mesh.primitive_torus_add", text="Torus")

        col = row.column()
        col.operator("mesh.primitive_ico_sphere_add", text="Ico Sphere")
        col.operator("mesh.primitive_uv_sphere_add", text="UV Sphere")

class CustomButtonOperator(bpy.types.Operator):
    bl_idname = "wm.custom_button_operator"
    bl_label = "Custom Button"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        bpy.ops.wm.call_menu(name=MeshSubMenu.bl_idname)
        return {'FINISHED'}

def draw_header(self, context):
    layout = self.layout
    layout.operator("wm.custom_button_operator", text="Mesh Options")

def register():
    bpy.utils.register_class(MeshSubMenu)
    bpy.utils.register_class(CustomButtonOperator)
    bpy.types.VIEW3D_HT_header.append(draw_header)

def unregister():
    bpy.utils.unregister_class(MeshSubMenu)
    bpy.utils.unregister_class(CustomButtonOperator)
    bpy.types.VIEW3D_HT_header.remove(draw_header)

if __name__ == "__main__":
    register()
