#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

is_xform_identity = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "is_xform_identity",
    "method_parameters": (("xform","array_of dbl","REQ"),),
    "method_returns": ("boolean","null")
    }
is_xform_similarity = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "is_xform_similarity",
    "method_parameters": (("xform","array_of dbl","REQ"),),
    "method_returns": ("boolean","null")
    }
is_xform_zero = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "is_xform_zero",
    "method_parameters": (("xform","array_of dbl","REQ"),),
    "method_returns": ("boolean","null")
    }
xform_c_plane_to_world = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_c_plane_to_world",
    "method_parameters": (("point","array_of dbl","REQ"),("plane","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_change_basis = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_change_basis",
    "method_parameters": (("plane_1","array_of dbl","REQ"),("plane_2","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_change_basis_2 = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_change_basis_2",
    "method_parameters": (("x_0","array_of dbl","REQ"),("y_0","array_of dbl","REQ"),("z_0","array_of dbl","REQ"),("x_1","array_of dbl","REQ"),("y_1","array_of dbl","REQ"),("z_1","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_compare = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_compare",
    "method_parameters": (("xform_1","array_of dbl","REQ"),("xform_2","array_of dbl","REQ")),
    "method_returns": ("null",)
    }
xform_determinant = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_determinant",
    "method_parameters": (("xform","array_of dbl","REQ"),),
    "method_returns": ("number","null")
    }
xform_diagonal = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_diagonal",
    "method_parameters": (("value","dbl","REQ"),),
    "method_returns": ("array","null")
    }
xform_identity = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_identity",
    "method_parameters": (),
    "method_returns": ("array",)
    }
xform_inverse = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_inverse",
    "method_parameters": (("xform","array_of dbl","REQ"),),
    "method_returns": ("array","null")
    }
xform_mirror = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_mirror",
    "method_parameters": (("point","array_of dbl","REQ"),("normal","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_multiply = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_multiply",
    "method_parameters": (("xform_1","array_of dbl","REQ"),("xform_2","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_planar_projection = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_planar_projection",
    "method_parameters": (("plane","array_of dbl","REQ"),),
    "method_returns": ("array","null")
    }
xform_rotation = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_rotation",
    "method_parameters": (("plane_1","array_of dbl","REQ"),("plane_2","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_rotation_2 = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_rotation_2",
    "method_parameters": (("angle","dbl","REQ"),("axis","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_rotation_3 = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_rotation_3",
    "method_parameters": (("start_dir","array_of dbl","REQ"),("end_dir","array_of dbl","REQ"),("point","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_rotation_4 = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_rotation_4",
    "method_parameters": (("x_0","array_of dbl","REQ"),("y_0","array_of dbl","REQ"),("z_0","array_of dbl","REQ"),("x_1","array_of dbl","REQ"),("y_1","array_of dbl","REQ"),("z_1","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_scale = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_scale",
    "method_parameters": (("plane","array_of dbl","REQ"),("x_scale","dbl","REQ"),("y_scale","dbl","REQ"),("z_scale","dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_scale_2 = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_scale_2",
    "method_parameters": (("x_scale","dbl","REQ"),("y_scale","dbl","REQ"),("z_scale","dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_scale_3 = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_scale_3",
    "method_parameters": (("vector","array_of dbl","REQ"),),
    "method_returns": ("array","null")
    }
xform_scale_4 = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_scale_4",
    "method_parameters": (("point","array_of dbl","REQ"),("scale","dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_screen_to_world = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_screen_to_world",
    "method_parameters": (("point","array_of dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
    "method_returns": ("array","null")
    }
xform_shear = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_shear",
    "method_parameters": (("plane","array_of dbl","REQ"),("x_1","array_of dbl","REQ"),("y_1","array_of dbl","REQ"),("z_1","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_translation = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_translation",
    "method_parameters": (("vector","array_of dbl","REQ"),),
    "method_returns": ("array","null")
    }
xform_world_to_c_plane = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_world_to_c_plane",
    "method_parameters": (("point","array_of dbl","REQ"),("plane","array_of dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_world_to_screen = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_world_to_screen",
    "method_parameters": (("point","array_of dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
    "method_returns": ("array","array","null")
    }
xform_zero = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_zero",
    "method_parameters": (),
    "method_returns": ("array",)
    }
