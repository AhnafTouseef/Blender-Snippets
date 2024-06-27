import bpy

frame_current= bpy.data.scenes["Scene"].frame_current
frame_start = bpy.data.scenes["Scene"].frame_start 
frame_end = bpy.data.scenes["Scene"].frame_end

for i in range(frame_end):
    bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Cloth")
    bpy.context.scene.frame_current = i+1


bpy.context.object.active_shape_key_index = 1
bpy.data.shape_keys["Key"].use_relative = False

obj = bpy.context.object.data.shape_keys

def insert_keyframe():
    obj.keyframe_insert("eval_time")
    return 'Finished'


def go_to_frame(frame):
    bpy.context.scene.frame_current = frame
    return 'Finished'
    # Insert keyframe 
go_to_frame(frame_start)
insert_keyframe()

go_to_frame(frame_end)
bpy.data.shape_keys["Key"].eval_time = (frame_end*10)
insert_keyframe()
#bpy.ops.action.interpolation_type(type='LINEAR')

