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
import asyncio

tracemalloc.start()

class ONIONSKIN3D_PT_homeUi(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    """It is the Panel were you choose the meshes ou want to use for the onion skin"""
    bl_idname = "ONIONSKIN3D_PT_homeUi"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "OnionSkin3dHomeUi"
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
        row.label(text="Selcted meshes are :" )
        row = layout.row()
        box = row.box();
        for mesh in bpy.context.selected_objects:                
                  row = box.row();
                  row.label(text=mesh.name)
        row = layout.row()
        row.operator(startButton_OT_addMesh.bl_idname)
        row = layout.row()
        

class ONIONSKIN3D_PT_startedUi(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_idname = "ONIONSKIN3D_PT_startedUi"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "OnionSkin3dInUseUi"
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
        row.label(text="Selcted meshes are :" )
        row = layout.row()
        box = row.box();
        for mesh in bpy.context.selected_objects:                
                  row = box.row();
                  row.label(text=mesh.name)
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
        asyncio.run(copyAllData())
        return {'FINISHED'}

        


async def copyAllData():
    """if(len(ONIONSKIN3D_PT_homeUi.meshes) != 0) :"""
    for mesh in bpy.context.selected_objects:
        ONIONSKIN3D_PT_homeUi.meshes.append(mesh)
        print(mesh)
    return {'FINISHED'}
    
def register():
    bpy.utils.register_class(startButton_OT_addMesh)
    bpy.utils.register_class(ONIONSKIN3D_PT_homeUi)


def unregister():
    bpy.utils.register_class(startButton_OT_addMesh)
    bpy.utils.unregister_class(ONIONSKIN3D_PT_homeUi)




if __name__ == "__main__":
    register()
    

