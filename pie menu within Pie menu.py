import bpy

class Mesh1SubMenu(bpy.types.Menu):
    bl_label = "Mesh 1"
    bl_idname = "OBJECT_MT_mesh1_submenu"

    def draw(self, context):
        layout = self.layout

        # Mesh 1 submenu options
        pie = layout.menu_pie()
        pie.operator("mesh.primitive_cube_add", text="Cube")
        pie.operator("mesh.primitive_cone_add", text="Cone")
        pie.operator("mesh.primitive_cylinder_add", text="Cylinder")

class Mesh2SubMenu(bpy.types.Menu):
    bl_label = "Mesh 2"
    bl_idname = "OBJECT_MT_mesh2_submenu"

    def draw(self, context):
        layout = self.layout

        # Mesh 2 submenu options
        pie = layout.menu_pie()
        pie.operator("mesh.primitive_torus_add", text="Torus")
        pie.operator("mesh.primitive_ico_sphere_add", text="Ico Sphere")
        pie.operator("mesh.primitive_uv_sphere_add", text="UV Sphere")

class MainPieMenu(bpy.types.Menu):
    bl_label = "Main Pie Menu"
    bl_idname = "OBJECT_MT_main_pie_menu"

    def draw(self, context):
        layout = self.layout

        # Main pie menu with submenus
        pie = layout.menu_pie()
        pie.operator("wm.call_menu_pie", text="Mesh 1").name = "OBJECT_MT_mesh1_submenu"
        pie.operator("wm.call_menu_pie", text="Mesh 2").name = "OBJECT_MT_mesh2_submenu"

def register():
    bpy.utils.register_class(Mesh1SubMenu)
    bpy.utils.register_class(Mesh2SubMenu)
    bpy.utils.register_class(MainPieMenu)

    # Add keymap for Ctrl + LMB to show the main pie menu
    wm = bpy.context.window_manager.keyconfigs.addon.keymaps.new(name='3D View', space_type='VIEW_3D')
    kmi = wm.keymap_items.new("wm.call_menu_pie", 'LEFTMOUSE', 'PRESS', ctrl=True)
    kmi.properties.name = "OBJECT_MT_main_pie_menu"

def unregister():
    bpy.utils.unregister_class(Mesh1SubMenu)
    bpy.utils.unregister_class(Mesh2SubMenu)
    bpy.utils.unregister_class(MainPieMenu)

    # Remove the keymap when unregistering
    wm = bpy.context.window_manager.keyconfigs.addon.keymaps['3D View']
    kmis = [kmi for kmi in wm.keymap_items if kmi.idname == 'wm.call_menu_pie' and kmi.properties.name == "OBJECT_MT_main_pie_menu"]
    for kmi in kmis:
        wm.keymap_items.remove(kmi)

if __name__ == "__main__":
    register()
