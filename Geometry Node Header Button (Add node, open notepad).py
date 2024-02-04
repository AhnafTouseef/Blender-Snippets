import bpy
import subprocess
import ctypes
import time

def refresh_ui():
    bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

# Constants
VK_G = 0x47  # Virtual key code for 'G'
KEY_DOWN = 0x0001
KEY_UP = 0x0002

# Load the user32.dll
user32 = ctypes.WinDLL('user32')

def press_key(key_code):
    # Simulate key press
    user32.keybd_event(key_code, 0, KEY_DOWN, 0)
    time.sleep(0.1)  # Adjust sleep time if needed
    user32.keybd_event(key_code, 0, KEY_UP, 0)

def type_G():
    press_key(VK_G)  # Press 'G' key 10 times

class GNNodeSelectionOperator(bpy.types.Operator):
    bl_idname = "wm.gn_node_selection_operator"
    bl_label = "GN Node Selection"

    node_type: bpy.props.StringProperty()

    def execute(self, context):
        bpy.ops.node.add_node(type=self.node_type, use_transform=True)
        bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')

        # Open Notepad (replace with the desired file or application)
        #subprocess.Popen(["notepad.exe"])
        #time.sleep(0.1)
        #type_G()
        #time.sleep(0.1)
        cursor = bpy.context.space_data.cursor_location
        self.report({'INFO'}, "Mouse coords are %d %d" % (cursor.x, cursor.y))
        context.active_node.location = (cursor.x, cursor.y)

        return {'FINISHED'}

class GNOptionsMenu(bpy.types.Menu):
    bl_label = "GN Options Menu"
    bl_idname = "NODE_MT_gn_options_menu"

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        

        row = layout.row()

        col = row.column()
        col.label(text="Column_1")
        col.operator("wm.gn_node_selection_operator", text="EdgePathToSelection").node_type = 'GeometryNodeEdgePathsToSelection'
        col.operator("wm.gn_node_selection_operator", text="EdgePathToCurves").node_type = 'GeometryNodeEdgePathsToCurves'
        
        col = row.column()
        col.label(text="Column_2")
        col.operator("wm.gn_node_selection_operator", text="DualMesh").node_type = 'GeometryNodeDualMesh'
        col.operator("wm.gn_node_selection_operator", text="ExtrudeMesh").node_type = 'GeometryNodeExtrudeMesh'
        
        col = row.column()
        col.label(text="Column_3")
        col.operator("wm.gn_node_selection_operator", text="FlipFaces").node_type = 'GeometryNodeFlipFaces'
        col.operator("wm.gn_node_selection_operator", text="MeshBoolean").node_type = 'GeometryNodeMeshBoolean'



def draw_gn_header(self, context):
    layout = self.layout
    layout.operator("wm.gn_custom_button_operator", text="GN Options")

def register():
    bpy.utils.register_class(GNOptionsMenu)
    bpy.utils.register_class(GNNodeSelectionOperator)
    bpy.types.NODE_HT_header.append(draw_gn_header)

def unregister():
    bpy.utils.unregister_class(GNOptionsMenu)
    bpy.utils.unregister_class(GNNodeSelectionOperator)
    bpy.types.NODE_HT_header.remove(draw_gn_header)

addon_keymaps = []

def register_handler():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    if kc:
        km = kc.keymaps.new(name='Node Editor', space_type='NODE_EDITOR')
        kmi = km.keymap_items.new('wm.call_menu', 'A', 'PRESS', ctrl=True)
        kmi.properties.name = "NODE_MT_gn_options_menu"
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
