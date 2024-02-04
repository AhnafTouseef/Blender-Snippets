import bpy

class CustomButtonOperator(bpy.types.Operator):
    bl_idname = "wm.custom_button_operator"
    bl_label = "Custom Button"

    def execute(self, context):
        # Replace this with the functionality you want when the button is clicked
        self.report({'INFO'}, "Button Clicked!")
        return {'FINISHED'}

def draw_header(self, context):
    layout = self.layout
    layout.operator("wm.custom_button_operator", text="Custom Button")

def register():
    bpy.utils.register_class(CustomButtonOperator)
    bpy.types.VIEW3D_HT_header.append(draw_header)

def unregister():
    bpy.utils.unregister_class(CustomButtonOperator)
    bpy.types.VIEW3D_HT_header.remove(draw_header)

if __name__ == "__main__":
    register()
