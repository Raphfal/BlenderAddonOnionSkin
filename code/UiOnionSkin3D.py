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
meshes = []
class OnionSkin3d(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_idname = "OnionSkinAddon"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "OnionSkin3d"
    bl_category = 'Onion Skin 3D'
    
    

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
        row.operator(startButton.bl_idname)
        row = layout.row()
        



class startButton(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "START ONION SKIN"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        copyAllData()
        return {'FINISHED'}
    

def copyAllData():
        for mesh in bpy.context.selected_objects:
            meshes.append(mesh)

def register():
    bpy.utils.register_class(startButton)
    bpy.utils.register_class(OnionSkin3d)


def unregister():
    bpy.utils.register_class(startButton)
    bpy.utils.unregister_class(OnionSkin3d)


if __name__ == "__main__":
    register()
    

