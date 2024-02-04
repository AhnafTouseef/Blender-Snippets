import bpy


class NODE_MT_AddExtrudeMeshMenu(bpy.types.Menu):
    bl_idname = "NODE_MT_add_extrude_mesh_menu"
    bl_label = "Add ExtrudeMesh Node"

    def draw(self, context):
        layout = self.layout
        layout.operator("node.add_node", text="ExtrudeMesh", icon='MOD_SOLIDIFY').type = 'GeometryNodeExtrudeMesh'
       
        

def register():
    bpy.utils.register_class(NODE_MT_AddExtrudeMeshMenu)

def unregister():
    bpy.utils.unregister_class(NODE_MT_AddExtrudeMeshMenu)

def keymap_item(self, context):
    self.layout.menu(NODE_MT_AddExtrudeMeshMenu.bl_idname, text="Add ExtrudeMesh Node")

addon_keymaps = []

def register_handler():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu', 'LEFTMOUSE', 'PRESS', ctrl=True)
        kmi.properties.name = "NODE_MT_add_extrude_mesh_menu"
        addon_keymaps.append((km, kmi))

def unregister_handler():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        for km, kmi in addon_keymaps:
            km.keymap_items.remove(kmi)
        addon_keymaps.clear()

if __name__ == "__main__":
    register()
    register_handler()
