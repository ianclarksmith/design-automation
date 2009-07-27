#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

is_xform_identity = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "is_xform_identity",
    "method_parameters": (("xform","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
is_xform_similarity = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "is_xform_similarity",
    "method_parameters": (("xform","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
is_xform_zero = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "is_xform_zero",
    "method_parameters": (("xform","arr_of_dbl","REQ")),
    "method_returns": ("boolean","null")
    }
xform_c_plane_to_world = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_c_plane_to_world",
    "method_parameters": (("point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_change_basis = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_change_basis",
    "method_parameters": (("plane1","arr_of_dbl","REQ"),("plane2","arr_of_dbl","REQ"),("x0","arr_of_dbl","REQ"),("y0","arr_of_dbl","REQ"),("z0","arr_of_dbl","REQ"),("x1","arr_of_dbl","REQ"),("y1","arr_of_dbl","REQ"),("z1","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_compare = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_compare",
    "method_parameters": (("xform1","arr_of_dbl","REQ"),("xform2","arr_of_dbl","REQ")),
    "method_returns": ("null")
    }
xform_determinant = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_determinant",
    "method_parameters": (("xform","arr_of_dbl","REQ")),
    "method_returns": ("number","null")
    }
xform_diagonal = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_diagonal",
    "method_parameters": (("value","dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_identity = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_identity",
    "method_parameters": (),
    "method_returns": ("array")
    }
xform_inverse = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_inverse",
    "method_parameters": (("xform","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_mirror = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_mirror",
    "method_parameters": (("point","arr_of_dbl","REQ"),("normal","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_multiply = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_multiply",
    "method_parameters": (("xform1","arr_of_dbl","REQ"),("xform2","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_planar_projection = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_planar_projection",
    "method_parameters": (("plane","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_rotation = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_rotation",
    "method_parameters": (("plane1","arr_of_dbl","REQ"),("plane2","arr_of_dbl","REQ"),("angle","dbl","REQ"),("axis","arr_of_dbl","REQ"),("start_dir","arr_of_dbl","REQ"),("end_dir","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("x0","arr_of_dbl","REQ"),("y0","arr_of_dbl","REQ"),("z0","arr_of_dbl","REQ"),("x1","arr_of_dbl","REQ"),("y1","arr_of_dbl","REQ"),("z1","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_scale = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_scale",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("x_scale","dbl","REQ"),("y_scale","dbl","REQ"),("z_scale","dbl","REQ"),("vector","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("scale","dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_screen_to_world = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_screen_to_world",
    "method_parameters": (("point","arr_of_dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
    "method_returns": ("array","null")
    }
xform_shear = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_shear",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("x1","arr_of_dbl","REQ"),("y1","arr_of_dbl","REQ"),("z1","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_translation = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_translation",
    "method_parameters": (("vector","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_world_to_c_plane = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_world_to_c_plane",
    "method_parameters": (("point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
xform_world_to_screen = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_world_to_screen",
    "method_parameters": (("point","arr_of_dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
    "method_returns": ("array","array","null")
    }
xform_zero = {
    "method_location": "Transformation",
    "method_type": "METHOD",
    "method_name": "xform_zero",
    "method_parameters": (),
    "method_returns": ("array")
    }
