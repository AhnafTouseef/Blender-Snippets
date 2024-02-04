import bpy

class GNCustomButtonOperator(bpy.types.Operator):
    bl_idname = "wm.gn_custom_button_operator"
    bl_label = "GN Custom Button"

    def execute(self, context):
        # Your button's functionality here
        return {'FINISHED'}

    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=200)

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.label(text="Column 1")
        col.operator("mesh.primitive_cube_add", text="Cube")
        col.operator("mesh.primitive_cylinder_add", text="Cylinder")

        col = row.column()
        col.label(text="Column 2")
        col.operator("mesh.primitive_cone_add", text="Cone")
        col.operator("mesh.primitive_torus_add", text="Torus")

        col = row.column()
        col.label(text="Column 3")
        col.operator("mesh.primitive_ico_sphere_add", text="Ico Sphere")
        col.operator("mesh.primitive_uv_sphere_add", text="UV Sphere")
        col.operator("node.add_node", text="Extrude").type = 'GeometryNodeDualMesh'

def draw_gn_header(self, context):
    layout = self.layout
    layout.operator("wm.gn_custom_button_operator", text="GN Options")

def register():
    bpy.utils.register_class(GNCustomButtonOperator)
    bpy.types.NODE_HT_header.append(draw_gn_header)

def unregister():
    bpy.utils.unregister_class(GNCustomButtonOperator)
    bpy.types.NODE_HT_header.remove(draw_gn_header)

if __name__ == "__main__":
    register()
