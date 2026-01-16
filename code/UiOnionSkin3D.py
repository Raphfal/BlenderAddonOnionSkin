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

class ONIONSKIN3D_PT_homeUi(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    """It is the Panel were you choose the meshes ou want to add for the onion skin"""
    bl_idname = "ONIONSKIN3D_PT_homeUi"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "OnionSKin3D"
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
        row.operator(restartButton_OT_restart.bl_idname)
        
        
class ONIONSKIN3D_PT_SettingPanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    """It is the Panel were you tweek the settings of the onion skin"""
    bl_idname = "ONIONSKIN3D_PT_SettingPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_label = "Setings"
    bl_category = 'Onion Skin 3D'
    bpy.types.Scene.interval = bpy.props.IntProperty( default = 0)
    bpy.types.Scene.nbrFrmBefore = bpy.props.IntProperty(default = 0)
    bpy.types.Scene.nbrFrmAfter = bpy.props.IntProperty(default = 0)
    bpy.types.Scene.opacity = bpy.props.FloatProperty(default=0)
    
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        text = "Settings for the Onion skin 3D"
        layout = self.layout
        layout.prop(context.scene, "interval")
        layout.prop(context.scene, "nbrFrmBefore")
        layout.prop(context.scene, "nbrFrmAfter")
        layout.prop(context.scene, "opacity")
        


      

class startButton_OT_addMesh(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "operator.startbutton_ot_addmesh"
    bl_label = "ADD  ONION SKIN"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        (copyAllData())
        return {'FINISHED'}

class restartButton_OT_restart(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "operator.restartbutton_ot_restart"
    bl_label = "CLEAR MESHES"


    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        (clearAllData())
        return {'FINISHED'}


def getMeshesList():
    """Retourne la liste des meshes sélectionnés pour l'onion skin"""
    return ONIONSKIN3D_PT_homeUi.meshes

def copyAllData():
    """Add mesh in meshes tab only if they aren't already in"""
    for mesh in bpy.context.selected_objects:
        if (mesh not in getMeshesList()) :  
            getMeshesList().append(mesh)
            print(mesh)
    return {'FINISHED'}


def clearAllData():
    """Vide la liste des meshes ET supprime tous les duplicatas"""
    print(len(getMeshesList()))
    
    # Vider la liste des meshes
    getMeshesList().clear()
    print(len(getMeshesList()))
    return {'FINISHED'}


def onionSkinMain(scene):
    current_frame = bpy.context.scene.frame_current
    interval = bpy.context.scene.interval
    nbr_before = bpy.context.scene.nbrFrmBefore
    nbr_after = bpy.context.scene.nbrFrmAfter
    
    # Créer les nouveaux duplicatas
    createOnionDuplicates(scene)
        

bpy.app.handlers.frame_change_post.append(onionSkinMain)

def createOnionDuplicates(scene):
    """Crée les duplicatas d'onion skin pour chaque mesh"""
    current_frame = bpy.context.scene.frame_current
    interval = bpy.context.scene.interval
    nbr_before = bpy.context.scene.nbrFrmBefore
    nbr_after = bpy.context.scene.nbrFrmAfter
    opacity = bpy.context.scene.opacity
    
    frames_before = [current_frame - (i * interval) for i in range(1, nbr_before + 1)]
    frames_after = [current_frame + (i * interval) for i in range(1, nbr_after + 1)]
    all_frames = frames_before + frames_after
    
    for mesh in getMeshesList(): 
        for frame in all_frames:
            bpy.context.scene.frame_set(frame)
            matrix = mesh.matrix_world.copy()
            new_obj = mesh.copy()
            new_obj.data = mesh.data.copy()
            new_obj.name = "{}_onion_{}".format(mesh.name,frame)
            bpy.context.collection.objects.link(new_obj)
            print("Created duplicate: {}".format(new_obj.name))

    bpy.context.scene.frame_set(current_frame)
    
classes = (
    ONIONSKIN3D_PT_homeUi, 
    startButton_OT_addMesh, 
    restartButton_OT_restart, 
    ONIONSKIN3D_PT_SettingPanel
)



def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.interval
    del bpy.types.Scene.nbrFrmBefore
    del bpy.types.Scene.nbrFrmAfter
    del bpy.types.Scene.opacity
    
    if onionSkinMain in bpy.app.handlers.frame_change_post:
        bpy.app.handlers.frame_change_post.remove(onionSkinMain)

if __name__ == "__main__":
    
    register()

