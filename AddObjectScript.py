bl_info = {
    "name" : "Object Adder",
    "author" : "Kornel Toth",
    "version" : (1, 0),
    "blender" : (2, 80, 0),
    "location" : "View3d > Tool",
    "description" : "Adds objects and other functions",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
}

import bpy

class MainPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_MainPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My Panel"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="Add an object",                        icon='CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cube_add",                        icon='CUBE')
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add",                        icon='SPHERE')
        row = layout.row()
        row.operator("object.text_add",                        icon='TEXT')
        
def register():
    bpy.utils.register_class(MainPanel)

def unregister():
    bpy.utils.unregister_class(MainPanel)
    
if __name__ == "__main__":
    register()