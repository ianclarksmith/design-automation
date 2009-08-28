#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_object_mesh = {
    "function_location": "object",
    "function_com_id": 866,
    "function_vb_name": "AddObjectMesh",
    "function_name": "add_object_mesh",
    "function_parameters": (("object","str","REQ"),("quality","int","OPT"),("enable","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
box_morph_object = {
    "function_location": "object",
    "function_com_id": 918,
    "function_vb_name": "BoxMorphObject",
    "function_name": "box_morph_object",
    "function_parameters": (("objects","array_of str","REQ"),("box_points","array_of dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("string","array","null")
    }
copy_object = {
    "function_location": "object",
    "function_com_id": 184,
    "function_vb_name": "CopyObject",
    "function_name": "copy_object",
    "function_parameters": (("object","str","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
copy_object_2 = {
    "function_location": "object",
    "function_com_id": 184,
    "function_vb_name": "CopyObject",
    "function_name": "copy_object_2",
    "function_parameters": (("object","str","REQ"),("translation","array_of dbl","OPT")),
    "function_returns": ("string","null")
    }
copy_objects = {
    "function_location": "object",
    "function_com_id": 295,
    "function_vb_name": "CopyObjects",
    "function_name": "copy_objects",
    "function_parameters": (("objects","array_of str","REQ"),("start","array_of dbl","OPT"),("end","array_of dbl","OPT")),
    "function_returns": ("array","null")
    }
copy_objects_2 = {
    "function_location": "object",
    "function_com_id": 295,
    "function_vb_name": "CopyObjects",
    "function_name": "copy_objects_2",
    "function_parameters": (("translation","array_of dbl","OPT"),),
    "function_returns": ("array","null")
    }
delete_object = {
    "function_location": "object",
    "function_com_id": 185,
    "function_vb_name": "DeleteObject",
    "function_name": "delete_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
delete_objects = {
    "function_location": "object",
    "function_com_id": 186,
    "function_vb_name": "DeleteObjects",
    "function_name": "delete_objects",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("number","null")
    }
enable_object_mesh = {
    "function_location": "object",
    "function_com_id": 856,
    "function_vb_name": "EnableObjectMesh",
    "function_name": "enable_object_mesh",
    "function_parameters": (("objects","array_of str","REQ"),("enable","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
flash_object = {
    "function_location": "object",
    "function_com_id": 869,
    "function_vb_name": "FlashObject",
    "function_name": "flash_object",
    "function_parameters": (("objects","array_of str","REQ"),("style","bln","OPT")),
    "function_returns": ()
    }
hide_object = {
    "function_location": "object",
    "function_com_id": 187,
    "function_vb_name": "HideObject",
    "function_name": "hide_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
hide_objects = {
    "function_location": "object",
    "function_com_id": 303,
    "function_vb_name": "HideObjects",
    "function_name": "hide_objects",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("number","null")
    }
is_layout_object = {
    "function_location": "object",
    "function_com_id": 919,
    "function_vb_name": "IsLayoutObject",
    "function_name": "is_layout_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object = {
    "function_location": "object",
    "function_com_id": 46,
    "function_vb_name": "IsObject",
    "function_name": "is_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ()
    }
is_object_hidden = {
    "function_location": "object",
    "function_com_id": 47,
    "function_vb_name": "IsObjectHidden",
    "function_name": "is_object_hidden",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object_in_box = {
    "function_location": "object",
    "function_com_id": 799,
    "function_vb_name": "IsObjectInBox",
    "function_name": "is_object_in_box",
    "function_parameters": (("object","str","REQ"),("box","array_of dbl","REQ"),("mode","bln","OPT")),
    "function_returns": ("null",)
    }
is_object_in_group = {
    "function_location": "object",
    "function_com_id": 188,
    "function_vb_name": "IsObjectInGroup",
    "function_name": "is_object_in_group",
    "function_parameters": (("object","str","REQ"),("group","str","OPT")),
    "function_returns": ("null",)
    }
is_object_locked = {
    "function_location": "object",
    "function_com_id": 48,
    "function_vb_name": "IsObjectLocked",
    "function_name": "is_object_locked",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object_normal = {
    "function_location": "object",
    "function_com_id": 49,
    "function_vb_name": "IsObjectNormal",
    "function_name": "is_object_normal",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object_reference = {
    "function_location": "object",
    "function_com_id": 271,
    "function_vb_name": "IsObjectReference",
    "function_name": "is_object_reference",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object_selectable = {
    "function_location": "object",
    "function_com_id": 307,
    "function_vb_name": "IsObjectSelectable",
    "function_name": "is_object_selectable",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object_selected = {
    "function_location": "object",
    "function_com_id": 50,
    "function_vb_name": "IsObjectSelected",
    "function_name": "is_object_selected",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object_solid = {
    "function_location": "object",
    "function_com_id": 189,
    "function_vb_name": "IsObjectSolid",
    "function_name": "is_object_solid",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_object_valid = {
    "function_location": "object",
    "function_com_id": 522,
    "function_vb_name": "IsObjectValid",
    "function_name": "is_object_valid",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("null",)
    }
is_visible_in_view = {
    "function_location": "object",
    "function_com_id": 727,
    "function_vb_name": "IsVisibleInView",
    "function_name": "is_visible_in_view",
    "function_parameters": (("object","str","REQ"),("view","str","OPT")),
    "function_returns": ("null",)
    }
lock_object = {
    "function_location": "object",
    "function_com_id": 190,
    "function_vb_name": "LockObject",
    "function_name": "lock_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
lock_objects = {
    "function_location": "object",
    "function_com_id": 304,
    "function_vb_name": "LockObjects",
    "function_name": "lock_objects",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("number","null")
    }
match_object_attributes = {
    "function_location": "object",
    "function_com_id": 781,
    "function_vb_name": "MatchObjectAttributes",
    "function_name": "match_object_attributes",
    "function_parameters": (("targets","array_of str","REQ"),("source","str","OPT")),
    "function_returns": ("number","null")
    }
mirror_object = {
    "function_location": "object",
    "function_com_id": 589,
    "function_vb_name": "MirrorObject",
    "function_name": "mirror_object",
    "function_parameters": (("object","str","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("string","null")
    }
mirror_objects = {
    "function_location": "object",
    "function_com_id": 590,
    "function_vb_name": "MirrorObjects",
    "function_name": "mirror_objects",
    "function_parameters": (("objects","array_of str","REQ"),("start_pt","array_of dbl","REQ"),("end_pt","array_of dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("string","null")
    }
move_object = {
    "function_location": "object",
    "function_com_id": 270,
    "function_vb_name": "MoveObject",
    "function_name": "move_object",
    "function_parameters": (("object","str","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
move_object_2 = {
    "function_location": "object",
    "function_com_id": 270,
    "function_vb_name": "MoveObject",
    "function_name": "move_object_2",
    "function_parameters": (("object","str","REQ"),("translation","array_of dbl","REQ")),
    "function_returns": ("boolean","null")
    }
move_objects = {
    "function_location": "object",
    "function_com_id": 296,
    "function_vb_name": "MoveObjects",
    "function_name": "move_objects",
    "function_parameters": (("objects","array_of str","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ")),
    "function_returns": ("number","null")
    }
move_objects_2 = {
    "function_location": "object",
    "function_com_id": 296,
    "function_vb_name": "MoveObjects",
    "function_name": "move_objects_2",
    "function_parameters": (("translation","array_of dbl","REQ"),),
    "function_returns": ("number","null")
    }
object_color = {
    "function_location": "object",
    "function_com_id": 191,
    "function_vb_name": "ObjectColor",
    "function_name": "object_color",
    "function_parameters": (("objects","array_of str","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_color_source = {
    "function_location": "object",
    "function_com_id": 192,
    "function_vb_name": "ObjectColorSource",
    "function_name": "object_color_source",
    "function_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_description = {
    "function_location": "object",
    "function_com_id": 470,
    "function_vb_name": "ObjectDescription",
    "function_name": "object_description",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("string","null")
    }
object_dump = {
    "function_location": "object",
    "function_com_id": 705,
    "function_vb_name": "ObjectDump",
    "function_name": "object_dump",
    "function_parameters": (("object","str","REQ"),("type","int","OPT")),
    "function_returns": ("string","null")
    }
object_groups = {
    "function_location": "object",
    "function_com_id": 193,
    "function_vb_name": "ObjectGroups",
    "function_name": "object_groups",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
object_has_mesh = {
    "function_location": "object",
    "function_com_id": 867,
    "function_vb_name": "ObjectHasMesh",
    "function_name": "object_has_mesh",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
object_layer = {
    "function_location": "object",
    "function_com_id": 51,
    "function_vb_name": "ObjectLayer",
    "function_name": "object_layer",
    "function_parameters": (("objects","array_of str","REQ"),("layer","str","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_layout = {
    "function_location": "object",
    "function_com_id": 924,
    "function_vb_name": "ObjectLayout",
    "function_name": "object_layout",
    "function_parameters": (("object","str","REQ"),("layout","str","OPT"),("return_name","bln","OPT")),
    "function_returns": ("string","string","null")
    }
object_linetype = {
    "function_location": "object",
    "function_com_id": 646,
    "function_vb_name": "ObjectLinetype",
    "function_name": "object_linetype",
    "function_parameters": (("objects","array_of str","REQ"),("layer","str","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_linetype_source = {
    "function_location": "object",
    "function_com_id": 647,
    "function_vb_name": "ObjectLinetypeSource",
    "function_name": "object_linetype_source",
    "function_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_material_index = {
    "function_location": "object",
    "function_com_id": 194,
    "function_vb_name": "ObjectMaterialIndex",
    "function_name": "object_material_index",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
object_material_source = {
    "function_location": "object",
    "function_com_id": 195,
    "function_vb_name": "ObjectMaterialSource",
    "function_name": "object_material_source",
    "function_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_mesh_density = {
    "function_location": "object",
    "function_com_id": 858,
    "function_vb_name": "ObjectMeshDensity",
    "function_name": "object_mesh_density",
    "function_parameters": (("object","str","REQ"),("density","dbl","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_max_angle = {
    "function_location": "object",
    "function_com_id": 859,
    "function_vb_name": "ObjectMeshMaxAngle",
    "function_name": "object_mesh_max_angle",
    "function_parameters": (("object","str","REQ"),("angle","dbl","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_max_aspect_ratio = {
    "function_location": "object",
    "function_com_id": 860,
    "function_vb_name": "ObjectMeshMaxAspectRatio",
    "function_name": "object_mesh_max_aspect_ratio",
    "function_parameters": (("object","str","REQ"),("ratio","dbl","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_max_dist_edge_to_srf = {
    "function_location": "object",
    "function_com_id": 863,
    "function_vb_name": "ObjectMeshMaxDistEdgeToSrf",
    "function_name": "object_mesh_max_dist_edge_to_srf",
    "function_parameters": (("object","str","REQ"),("distance","dbl","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_max_edge_length = {
    "function_location": "object",
    "function_com_id": 862,
    "function_vb_name": "ObjectMeshMaxEdgeLength",
    "function_name": "object_mesh_max_edge_length",
    "function_parameters": (("object","str","REQ"),("length","dbl","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_min_edge_length = {
    "function_location": "object",
    "function_com_id": 861,
    "function_vb_name": "ObjectMeshMinEdgeLength",
    "function_name": "object_mesh_min_edge_length",
    "function_parameters": (("object","str","REQ"),("length","dbl","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_min_initial_grid_quads = {
    "function_location": "object",
    "function_com_id": 864,
    "function_vb_name": "ObjectMeshMinInitialGridQuads",
    "function_name": "object_mesh_min_initial_grid_quads",
    "function_parameters": (("object","str","REQ"),("quads","int","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_quality = {
    "function_location": "object",
    "function_com_id": 857,
    "function_vb_name": "ObjectMeshQuality",
    "function_name": "object_mesh_quality",
    "function_parameters": (("object","str","REQ"),("quality","int","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_mesh_settings = {
    "function_location": "object",
    "function_com_id": 865,
    "function_vb_name": "ObjectMeshSettings",
    "function_name": "object_mesh_settings",
    "function_parameters": (("object","str","REQ"),("settings","int","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
object_name = {
    "function_location": "object",
    "function_com_id": 196,
    "function_vb_name": "ObjectName",
    "function_name": "object_name",
    "function_parameters": (("objects","array_of str","REQ"),("name","str","OPT")),
    "function_returns": ("string","string","number","null")
    }
object_names = {
    "function_location": "object",
    "function_com_id": 639,
    "function_vb_name": "ObjectNames",
    "function_name": "object_names",
    "function_parameters": (("objects","array_of str","REQ"),("names","array_of str","OPT")),
    "function_returns": ("array","array","null")
    }
object_print_color = {
    "function_location": "object",
    "function_com_id": 805,
    "function_vb_name": "ObjectPrintColor",
    "function_name": "object_print_color",
    "function_parameters": (("objects","array_of str","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_print_color_source = {
    "function_location": "object",
    "function_com_id": 806,
    "function_vb_name": "ObjectPrintColorSource",
    "function_name": "object_print_color_source",
    "function_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_print_width = {
    "function_location": "object",
    "function_com_id": 807,
    "function_vb_name": "ObjectPrintWidth",
    "function_name": "object_print_width",
    "function_parameters": (("objects","array_of str","REQ"),("width","dbl","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_print_width_source = {
    "function_location": "object",
    "function_com_id": 808,
    "function_vb_name": "ObjectPrintWidthSource",
    "function_name": "object_print_width_source",
    "function_parameters": (("objects","array_of str","REQ"),("source","int","OPT")),
    "function_returns": ("number","number","number","null")
    }
object_top_group = {
    "function_location": "object",
    "function_com_id": 197,
    "function_vb_name": "ObjectTopGroup",
    "function_name": "object_top_group",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("string","null")
    }
object_type = {
    "function_location": "object",
    "function_com_id": 198,
    "function_vb_name": "ObjectType",
    "function_name": "object_type",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
object_u_r_l = {
    "function_location": "object",
    "function_com_id": 199,
    "function_vb_name": "ObjectURL",
    "function_name": "object_u_r_l",
    "function_parameters": (("objects","array_of str","REQ"),("u_r_l","str","OPT")),
    "function_returns": ("string","string","number","null")
    }
orient_object = {
    "function_location": "object",
    "function_com_id": 390,
    "function_vb_name": "OrientObject",
    "function_name": "orient_object",
    "function_parameters": (("object","str","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
    "function_returns": ("string","null")
    }
orient_objects = {
    "function_location": "object",
    "function_com_id": 391,
    "function_vb_name": "OrientObjects",
    "function_name": "orient_objects",
    "function_parameters": (("objects","array_of str","REQ"),("reference","array_of dbl","REQ"),("target","array_of dbl","REQ"),("flags","int","OPT")),
    "function_returns": ("array","null")
    }
remap_object = {
    "function_location": "object",
    "function_com_id": 655,
    "function_vb_name": "RemapObject",
    "function_name": "remap_object",
    "function_parameters": (("object","str","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("string","null")
    }
remap_objects = {
    "function_location": "object",
    "function_com_id": 656,
    "function_vb_name": "RemapObjects",
    "function_name": "remap_objects",
    "function_parameters": (("object","array_of str","REQ"),("src_plane","array_of dbl","REQ"),("dst_plane","array_of dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("array","null")
    }
rotate_object = {
    "function_location": "object",
    "function_com_id": 392,
    "function_vb_name": "RotateObject",
    "function_name": "rotate_object",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
    "function_returns": ("string","null")
    }
rotate_objects = {
    "function_location": "object",
    "function_com_id": 393,
    "function_vb_name": "RotateObjects",
    "function_name": "rotate_objects",
    "function_parameters": (("objects","array_of str","REQ"),("point","array_of dbl","REQ"),("angle","dbl","REQ"),("axis","array_of dbl","OPT"),("copy","bln","OPT")),
    "function_returns": ("string","null")
    }
scale_object = {
    "function_location": "object",
    "function_com_id": 585,
    "function_vb_name": "ScaleObject",
    "function_name": "scale_object",
    "function_parameters": (("object","str","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("string","null")
    }
scale_objects = {
    "function_location": "object",
    "function_com_id": 586,
    "function_vb_name": "ScaleObjects",
    "function_name": "scale_objects",
    "function_parameters": (("objects","array_of str","REQ"),("origin","array_of dbl","REQ"),("scale","array_of dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("array","null")
    }
select_object = {
    "function_location": "object",
    "function_com_id": 200,
    "function_vb_name": "SelectObject",
    "function_name": "select_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
select_objects = {
    "function_location": "object",
    "function_com_id": 298,
    "function_vb_name": "SelectObjects",
    "function_name": "select_objects",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("number","null")
    }
shear_object = {
    "function_location": "object",
    "function_com_id": 587,
    "function_vb_name": "ShearObject",
    "function_name": "shear_object",
    "function_parameters": (("object","str","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("string","null")
    }
shear_objects = {
    "function_location": "object",
    "function_com_id": 588,
    "function_vb_name": "ShearObjects",
    "function_name": "shear_objects",
    "function_parameters": (("objects","array_of str","REQ"),("origin","array_of dbl","REQ"),("ref_pt","array_of dbl","REQ"),("scale","dbl","REQ"),("copy","bln","OPT")),
    "function_returns": ("array","null")
    }
show_object = {
    "function_location": "object",
    "function_com_id": 201,
    "function_vb_name": "ShowObject",
    "function_name": "show_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
show_objects = {
    "function_location": "object",
    "function_com_id": 305,
    "function_vb_name": "ShowObjects",
    "function_name": "show_objects",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("number","null")
    }
transform_object = {
    "function_location": "object",
    "function_com_id": 272,
    "function_vb_name": "TransformObject",
    "function_name": "transform_object",
    "function_parameters": (("object","str","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),
    "function_returns": ("boolean","null")
    }
transform_objects = {
    "function_location": "object",
    "function_com_id": 302,
    "function_vb_name": "TransformObjects",
    "function_name": "transform_objects",
    "function_parameters": (("objects","array_of str","REQ"),("matrix","array_of str","REQ"),("copy","bln","OPT")),
    "function_returns": ("array","null")
    }
unlock_object = {
    "function_location": "object",
    "function_com_id": 202,
    "function_vb_name": "UnlockObject",
    "function_name": "unlock_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
unlock_objects = {
    "function_location": "object",
    "function_com_id": 306,
    "function_vb_name": "UnlockObjects",
    "function_name": "unlock_objects",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("number","null")
    }
unselect_object = {
    "function_location": "object",
    "function_com_id": 299,
    "function_vb_name": "UnselectObject",
    "function_name": "unselect_object",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
unselect_objects = {
    "function_location": "object",
    "function_com_id": 300,
    "function_vb_name": "UnselectObjects",
    "function_name": "unselect_objects",
    "function_parameters": (("objects","array_of str","REQ"),),
    "function_returns": ("number","null")
    }
