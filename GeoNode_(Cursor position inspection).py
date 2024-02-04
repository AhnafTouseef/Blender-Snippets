import bpy

# Define a panel class
class NODE_PT_CursorPositionPanel(bpy.types.Panel):
    bl_label = "Cursor Position"
    bl_idname = "NODE_PT_CursorPositionPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'

    def draw(self, context):
        layout = self.layout

        # Get the cursor location in the node editor
        cursor_location = bpy.context.space_data.cursor_location

        # Display the cursor position in the side panel
        layout.label(text=f"X: {cursor_location.x:.2f}, Y: {cursor_location.y:.2f}")

# Register the panel
def register():
    bpy.utils.register_class(NODE_PT_CursorPositionPanel)

# Unregister the panel
def unregister():
    bpy.utils.unregister_class(NODE_PT_CursorPositionPanel)

# For testing within Blender's text editor
if __name__ == "__main__":
    register()
