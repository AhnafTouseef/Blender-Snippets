import bpy

class GNModalOperator(bpy.types.Operator):
    bl_idname = "wm.gn_modal_operator"
    bl_label = "Add Geometry Node and Move Operator"

    def __init__(self):
        print("Start")

    def __del__(self):
        print("End")

    def execute(self, context):
        # Move the active node based on the cursor position
        context.active_node.location.x = self.x_value / 1
        context.active_node.location.y = self.y_value / 1
        return {'FINISHED'}

    def modal(self, context, event):
        if event.type == 'MOUSEMOVE':  # Apply
            self.x_value = event.mouse_x
            self.y_value = event.mouse_y
            #self.execute(context)
            bpy.ops.node.translate_attach_remove_on_cancel('INVOKE_DEFAULT')
            return {'CANCELLED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        # Add a Geometry Node to the active Geometry Node Editor
        bpy.ops.node.add_node(type='GeometryNodeExtrudeMesh')
        new_node = context.active_node
        context.space_data.node_tree.nodes.active = new_node

        # Move the node based on the cursor position in the Geometry Node Editor window
        #new_node.location.x = event.mouse_x
        #new_node.location.y = event.mouse_y
        #self.x_value = event.mouse_x
        #self.y_value = event.mouse_y

        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}


class GN_PT_ModalPanel(bpy.types.Panel):
    bl_label = "Geometry Node Modal Panel"
    bl_idname = "GN_PT_ModalPanel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        layout.operator(GNModalOperator.bl_idname, text="Add GN Node and Move")


# Register and add to the Node Editor menu.
bpy.utils.register_class(GNModalOperator)
bpy.utils.register_class(GN_PT_ModalPanel)

# Only needed if you want to add into a dynamic menu.
def menu_func(self, context):
    self.layout.operator(GNModalOperator.bl_idname, text="Add GN Node and Move")

bpy.types.NODE_MT_add.append(menu_func)
