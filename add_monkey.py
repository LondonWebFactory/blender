import bpy

bpy.ops.mesh.primitive_monkey_add(size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0), scale=(0.0, 0.0, 0.0))

# Ref:
# https://docs.blender.org/api/current/bpy.ops.mesh.html
