import bpy

class GNOptionsMenu(bpy.types.Menu):
    bl_label = "GN Options Menu"
    bl_idname = "NODE_MT_gn_options_menu"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        

        row = layout.row()

        col = row.column()
        col.label(text="Column_1")
        #col.operator("mesh.primitive_cube_add", text="Cube")
        #col.operator("mesh.primitive_cylinder_add", text="Cylinder")
        col.operator("node.add_node", text="EdgePathToSelection", icon='EDGESEL').type = 'GeometryNodeEdgePathToSelection'
        col.operator("node.add_node", text="EdgePathToCurves", icon='MOD_EDGESPLIT').type = 'GeometryNodeEdgePathToCurves'

        col = row.column()
        col.label(text="Column_2")
        #col.operator("mesh.primitive_cone_add", text="Cone")
        #col.operator("mesh.primitive_torus_add", text="Torus")
        col.operator("node.add_node", text="DualMesh", icon='SNAP_FACE_CENTER').type = 'GeometryNodeDualMesh'
        col.operator("node.add_node", text="ExtrudeMesh", icon='MOD_SOLIDIFY').type = 'GeometryNodeExtrudeMesh'

        col = row.column()
        col.label(text="Column_3")
        #col.operator("mesh.primitive_ico_sphere_add", text="Ico Sphere", icon='MESH_ICOSPHERE')
        #col.operator("mesh.primitive_uv_sphere_add", text="UV Sphere")
        col.operator("node.add_node", text="FlipFaces", icon='COLORSET_01_VEC').type = 'GeometryNodeFlipFaces'
        col.operator("node.add_node", text="MeshBoolean", icon='COLORSET_03_VEC').type = 'GeometryNodeMeshBoolean'

class GNCustomButtonOperator(bpy.types.Operator):
    bl_idname = "wm.gn_custom_button_operator"
    bl_label = "GN Custom Button"

    def execute(self, context):
        return {'FINISHED'}

    def invoke(self, context, event):
        bpy.ops.wm.call_menu(name=GNOptionsMenu.bl_idname)
        return {'FINISHED'}

def draw_gn_header(self, context):
    layout = self.layout
    layout.operator("wm.gn_custom_button_operator", text="GN Options")

def register():
    bpy.utils.register_class(GNOptionsMenu)
    bpy.utils.register_class(GNCustomButtonOperator)
    bpy.types.NODE_HT_header.append(draw_gn_header)

def unregister():
    bpy.utils.unregister_class(GNOptionsMenu)
    bpy.utils.unregister_class(GNCustomButtonOperator)
    bpy.types.NODE_HT_header.remove(draw_gn_header)

if __name__ == "__main__":
    register()
