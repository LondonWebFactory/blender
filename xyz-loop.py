import bpy
import time

for z in range(3):
    for y in range(3):
        for x in range(3):
            #bpy.ops.mesh.primitive_monkey_add(0.0, 0.0, 0.0)
            #bpy.ops.mesh.primitive_monkey_add(float(x)*2, float(y)*2, float(z)*2))
            #bpy.ops.mesh.primitive_uv_sphere_add(location=(float(x)*2, float(y)*2, float(z)*2))
            
            # Functions With All Options
            #bpy.ops.mesh.primitive_monkey_add(size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))
            #bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=200.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))
            #bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))
