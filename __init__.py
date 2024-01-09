import bpy
from bpy.props import BoolProperty, FloatProperty

from . import SourceCats


bl_info = {
    "name": "Source Cats",
    "blender": (3, 0, 0),
    "version": (1, 0),
    'location': 'View 3D > Tool Shelf > SourceCats',
    'category': '3D View',
    "author": "Starfelll",
    "url": "https://steamcommunity.com/profiles/76561198859761739"
}


def register():
    bpy.utils.register_class(SourceCats.OP_MergeBones_GetThreshold)
    bpy.utils.register_class(SourceCats.OP_MergeBones)
    bpy.utils.register_class(SourceCats.OP_ClearLRFlexs)
    bpy.utils.register_class(SourceCats.OP_GenLRFlexs)
    bpy.utils.register_class(SourceCats.SourceCats_PT_MainPanel)

    scene = bpy.types.Scene
    scene.keep_merged_bones = BoolProperty(
        name='Keep Merged Bones',
        description='',
        default=False
    )
    scene.merge_bones_threshold = FloatProperty(
        name='Threshold',
        description="",
        default=0.00001,
        min=0,
        max=10,
        step=0.0001,
        precision=8,
        subtype='FACTOR'
    )


def unregister():
    bpy.utils.unregister_class(SourceCats.SourceCats_PT_MainPanel)
    bpy.utils.unregister_class(SourceCats.OP_GenLRFlexs)
    bpy.utils.unregister_class(SourceCats.OP_ClearLRFlexs)
    bpy.utils.unregister_class(SourceCats.OP_MergeBones)
    bpy.utils.unregister_class(SourceCats.OP_MergeBones_GetThreshold)


if __name__ == "__main__":
    register()
