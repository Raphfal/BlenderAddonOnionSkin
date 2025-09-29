bl_info = {
    "name": "Onion Skin For 3D animation free",
    "author": "H.Raph",
    "version": (1, 0),
    "blender": (4, 5, 3),
    "location": "",
    "description": "An onion skin for 3d animation",
    "category": "",
}


import bpy
import tracemalloc

tracemalloc.start()

class OnionSkin3d_PT_startPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_idname = "OnionSkin3d_PT_startPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "OnionSkin3d"
    bl_category = 'Onion Skin 3D'
    meshes = [] 
    
    def draw(self, context):
        layout = self.layout
        
        obj = context.object
        text = "Onion skin 3D"
        
        row = layout.row()
        row.label(text = 'Onion Skin addon')
        row = layout.row()
        row = layout.row()
        row.label(text = 'Select the meshes ')
        row = layout.row()
        row.label(text = 'you want to use ')
        row = layout.row()
        row.label(text = 'for the onion skin')
        row = layout.row()
        row = layout.row()
        row.label(text="Active object is : " + obj.name)
        row = layout.row()
        row.operator(startButton_OT_addMesh.bl_idname)
        row = layout.row()
        



class startButton_OT_addMesh(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "operator.startbutton_ot_addmesh"
    bl_label = "START ONION SKIN"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        copyAllData()
        return {'FINISHED'}
    

async def copyAllData():
    if(len(OnionSkin3d.meshes) != 0) :
        for mesh in bpy.context.selected_objects:
            OnionSkin3d.meshes.append(mesh)
            print(mesh)
            
    
def register():
    bpy.utils.register_class(startButton_OT_addMesh)
    bpy.utils.register_class(OnionSkin3d_PT_startPanel)


def unregister():
    bpy.utils.register_class(startButton_OT_addMesh)
    bpy.utils.unregister_class(OnionSkin3d_PT_startPanel)


if __name__ == "__main__":
    register()
    

