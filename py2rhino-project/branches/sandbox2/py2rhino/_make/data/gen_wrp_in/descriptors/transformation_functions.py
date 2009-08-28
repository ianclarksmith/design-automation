#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

is_xform_identity = {
    "function_location": "transformation",
    "function_com_id": 786,
    "function_vb_name": "IsXformIdentity",
    "function_name": "is_xform_identity",
    "function_parameters": (("xform","array_of dbl","REQ"),),
    "function_returns": ("boolean","null")
    }
is_xform_similarity = {
    "function_location": "transformation",
    "function_com_id": 787,
    "function_vb_name": "IsXformSimilarity",
    "function_name": "is_xform_similarity",
    "function_parameters": (("xform","array_of dbl","REQ"),),
    "function_returns": ("boolean","null")
    }
is_xform_zero = {
    "function_location": "transformation",
    "function_com_id": 785,
    "function_vb_name": "IsXformZero",
    "function_name": "is_xform_zero",
    "function_parameters": (("xform","array_of dbl","REQ"),),
    "function_returns": ("boolean","null")
    }
xform_c_plane_to_world = {
    "function_location": "transformation",
    "function_com_id": 131,
    "function_vb_name": "XformCPlaneToWorld",
    "function_name": "xform_c_plane_to_world",
    "function_parameters": (("point","array_of dbl","REQ"),("plane","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_change_basis = {
    "function_location": "transformation",
    "function_com_id": 796,
    "function_vb_name": "XformChangeBasis",
    "function_name": "xform_change_basis",
    "function_parameters": (("plane_1","array_of dbl","REQ"),("plane_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_change_basis_2 = {
    "function_location": "transformation",
    "function_com_id": 796,
    "function_vb_name": "XformChangeBasis",
    "function_name": "xform_change_basis_2",
    "function_parameters": (("x_0","array_of dbl","REQ"),("y_0","array_of dbl","REQ"),("z_0","array_of dbl","REQ"),("x_1","array_of dbl","REQ"),("y_1","array_of dbl","REQ"),("z_1","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_compare = {
    "function_location": "transformation",
    "function_com_id": 789,
    "function_vb_name": "XformCompare",
    "function_name": "xform_compare",
    "function_parameters": (("xform_1","array_of dbl","REQ"),("xform_2","array_of dbl","REQ")),
    "function_returns": ("null",)
    }
xform_determinant = {
    "function_location": "transformation",
    "function_com_id": 818,
    "function_vb_name": "XformDeterminant",
    "function_name": "xform_determinant",
    "function_parameters": (("xform","array_of dbl","REQ"),),
    "function_returns": ("number","null")
    }
xform_diagonal = {
    "function_location": "transformation",
    "function_com_id": 784,
    "function_vb_name": "XformDiagonal",
    "function_name": "xform_diagonal",
    "function_parameters": (("value","dbl","REQ"),),
    "function_returns": ("array","null")
    }
xform_identity = {
    "function_location": "transformation",
    "function_com_id": 783,
    "function_vb_name": "XformIdentity",
    "function_name": "xform_identity",
    "function_parameters": (),
    "function_returns": ("array",)
    }
xform_inverse = {
    "function_location": "transformation",
    "function_com_id": 817,
    "function_vb_name": "XformInverse",
    "function_name": "xform_inverse",
    "function_parameters": (("xform","array_of dbl","REQ"),),
    "function_returns": ("array","null")
    }
xform_mirror = {
    "function_location": "transformation",
    "function_com_id": 795,
    "function_vb_name": "XformMirror",
    "function_name": "xform_mirror",
    "function_parameters": (("point","array_of dbl","REQ"),("normal","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_multiply = {
    "function_location": "transformation",
    "function_com_id": 788,
    "function_vb_name": "XformMultiply",
    "function_name": "xform_multiply",
    "function_parameters": (("xform_1","array_of dbl","REQ"),("xform_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_planar_projection = {
    "function_location": "transformation",
    "function_com_id": 793,
    "function_vb_name": "XformPlanarProjection",
    "function_name": "xform_planar_projection",
    "function_parameters": (("plane","array_of dbl","REQ"),),
    "function_returns": ("array","null")
    }
xform_rotation = {
    "function_location": "transformation",
    "function_com_id": 794,
    "function_vb_name": "XformRotation",
    "function_name": "xform_rotation",
    "function_parameters": (("plane_1","array_of dbl","REQ"),("plane_2","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_rotation_2 = {
    "function_location": "transformation",
    "function_com_id": 794,
    "function_vb_name": "XformRotation",
    "function_name": "xform_rotation_2",
    "function_parameters": (("angle","dbl","REQ"),("axis","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_rotation_3 = {
    "function_location": "transformation",
    "function_com_id": 794,
    "function_vb_name": "XformRotation",
    "function_name": "xform_rotation_3",
    "function_parameters": (("start_dir","array_of dbl","REQ"),("end_dir","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_rotation_4 = {
    "function_location": "transformation",
    "function_com_id": 794,
    "function_vb_name": "XformRotation",
    "function_name": "xform_rotation_4",
    "function_parameters": (("x_0","array_of dbl","REQ"),("y_0","array_of dbl","REQ"),("z_0","array_of dbl","REQ"),("x_1","array_of dbl","REQ"),("y_1","array_of dbl","REQ"),("z_1","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_scale = {
    "function_location": "transformation",
    "function_com_id": 790,
    "function_vb_name": "XformScale",
    "function_name": "xform_scale",
    "function_parameters": (("plane","array_of dbl","REQ"),("x_scale","dbl","REQ"),("y_scale","dbl","REQ"),("z_scale","dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_scale_2 = {
    "function_location": "transformation",
    "function_com_id": 790,
    "function_vb_name": "XformScale",
    "function_name": "xform_scale_2",
    "function_parameters": (("x_scale","dbl","REQ"),("y_scale","dbl","REQ"),("z_scale","dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_scale_3 = {
    "function_location": "transformation",
    "function_com_id": 790,
    "function_vb_name": "XformScale",
    "function_name": "xform_scale_3",
    "function_parameters": (("vector","array_of dbl","REQ"),),
    "function_returns": ("array","null")
    }
xform_scale_4 = {
    "function_location": "transformation",
    "function_com_id": 790,
    "function_vb_name": "XformScale",
    "function_name": "xform_scale_4",
    "function_parameters": (("point","array_of dbl","REQ"),("scale","dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_screen_to_world = {
    "function_location": "transformation",
    "function_com_id": 581,
    "function_vb_name": "XformScreenToWorld",
    "function_name": "xform_screen_to_world",
    "function_parameters": (("point","array_of dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
    "function_returns": ("array","null")
    }
xform_shear = {
    "function_location": "transformation",
    "function_com_id": 791,
    "function_vb_name": "XformShear",
    "function_name": "xform_shear",
    "function_parameters": (("plane","array_of dbl","REQ"),("x_1","array_of dbl","REQ"),("y_1","array_of dbl","REQ"),("z_1","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_translation = {
    "function_location": "transformation",
    "function_com_id": 792,
    "function_vb_name": "XformTranslation",
    "function_name": "xform_translation",
    "function_parameters": (("vector","array_of dbl","REQ"),),
    "function_returns": ("array","null")
    }
xform_world_to_c_plane = {
    "function_location": "transformation",
    "function_com_id": 132,
    "function_vb_name": "XformWorldToCPlane",
    "function_name": "xform_world_to_c_plane",
    "function_parameters": (("point","array_of dbl","REQ"),("plane","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
xform_world_to_screen = {
    "function_location": "transformation",
    "function_com_id": 582,
    "function_vb_name": "XformWorldToScreen",
    "function_name": "xform_world_to_screen",
    "function_parameters": (("point","array_of dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
    "function_returns": ("array","array","null")
    }
xform_zero = {
    "function_location": "transformation",
    "function_com_id": 782,
    "function_vb_name": "XformZero",
    "function_name": "xform_zero",
    "function_parameters": (),
    "function_returns": ("array",)
    }
