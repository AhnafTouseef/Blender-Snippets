import bpy
#######################################################
                #Set variables                        #
frame_current= bpy.data.scenes["Scene"].frame_current #
frame_start = bpy.data.scenes["Scene"].frame_start    #
frame_end = bpy.data.scenes["Scene"].frame_end        #
frame_skip = 0                                        #
#######################################################


######################################################
            #Define required functions               #
def insert_keyframe(frame):                          #
    obj = bpy.context.object.data.shape_keys         #
    obj.keyframe_insert("eval_time", frame = frame)  #
    pass                                             #
                                                     #
                                                     #
def go_to_frame(frame):                              #
    bpy.context.scene.frame_current = frame          #
    pass                                             #
######################################################

#################################################################
        #Removes previous shape keys, if there is any           #
try:                                                            #
    bpy.ops.object.shape_key_remove(all=True, apply_mix=False)  #
except Exception:                                               #
    pass                                                        #
#################################################################

###################################################################
    #Enables modifier in viewport, if unenabled                   #
if bpy.context.object.modifiers["Cloth"].show_viewport == False:  #
    bpy.context.object.modifiers["Cloth"].show_viewport = True    #
###################################################################

######################################################################################
                                #Set up shape keys                                   #
for i in range(frame_start, frame_end+1):                                            #
    bpy.ops.object.modifier_apply_as_shapekey(keep_modifier=True, modifier="Cloth")  #
    bpy.context.scene.frame_current = i+1                                            #
######################################################################################

#################################################
    #Set up shape key interpolation mode        #
bpy.context.object.active_shape_key_index = 0   #
bpy.data.shape_keys["Key"].use_relative = False #
#################################################

def main():
 #####################################################################
                #Interpolation keyframe method                       #
    if frame_skip == 0:                                              #
        insert_keyframe(frame_start)                                 #
        bpy.data.shape_keys["Key"].eval_time = (frame_end*10)        #
        insert_keyframe(frame_end)                                   #
        bpy.context.object.modifiers["Cloth"].show_viewport = False  #
        go_to_frame(frame_current)                                   #
######################################################################

##########################################################################################################
                        #Continoius keyframe method                                                      #
    else:                                                                                                #
        bpy.context.scene.frame_current = 1                                                              #
        obj = bpy.context.object.data.shape_keys                                                         #
        while bpy.data.scenes["Scene"].frame_current <= frame_end:                                       #
            bpy.data.shape_keys["Key"].eval_time = (bpy.data.scenes["Scene"].frame_current*10)           #
            obj.keyframe_insert("eval_time")                                                             #
            bpy.data.scenes["Scene"].frame_current = bpy.data.scenes["Scene"].frame_current + frame_skip #
        bpy.context.object.modifiers["Cloth"].show_viewport = False                                      #
        go_to_frame(frame_current)                                                                       #
##########################################################################################################
        
main()
