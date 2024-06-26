import bpy

frame_end = bpy.data.scenes["Scene"].frame_end
frame_start = bpy.data.scenes["Scene"].frame_start 

for i in range(frame_end):
    bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Cloth")
    bpy.context.scene.frame_current = i+1


bpy.context.object.active_shape_key_index = 1
bpy.data.shape_keys["Key"].use_relative = False

obj = bpy.context.object.data.shape_keys

    # Insert keyframe 
bpy.context.scene.frame_current = frame_start
obj.keyframe_insert('''eval_time''')
bpy.data.shape_keys["Key"].eval_time = (frame_end*10)

bpy.context.scene.frame_current = frame_end
obj.keyframe_insert('''eval_time''')
#bpy.ops.action.interpolation_type(type='LINEAR')


