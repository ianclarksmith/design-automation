#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

add_clipping_plane = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "add_clipping_plane",
    "method_parameters": (("plane","arr_of_dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),("views","arr_of_str","OPT")),
    "method_returns": ("string","null")
    }
add_point_cloud = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "add_point_cloud",
    "method_parameters": (("points","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
add_points = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "add_points",
    "method_parameters": (("points","arr_of_dbl","REQ")),
    "method_returns": ("array","null")
    }
add_text = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "add_text",
    "method_parameters": (("text","str","REQ"),("point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("height","dbl","OPT"),("font","str","OPT"),("style","int","OPT")),
    "method_returns": ("string","null")
    }
add_text_dot = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "add_text_dot",
    "method_parameters": (("test","str","REQ"),("point","arr_of_dbl","REQ")),
    "method_returns": ("string","null")
    }
bounding_box = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "bounding_box",
    "method_parameters": (("objects","arr_of_str","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
    "method_returns": ("array","null")
    }
compare_geometry = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "compare_geometry",
    "method_parameters": (("object1","str","REQ"),("object2","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_clipping_plane = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "is_clipping_plane",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_point = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "is_point",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_point_cloud = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "is_point_cloud",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_text = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "is_text",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_text_dot = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "is_text_dot",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("boolean","null")
    }
point_cloud_count = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "point_cloud_count",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("number","null")
    }
point_cloud_points = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "point_cloud_points",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("array","null")
    }
point_coordinates = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "point_coordinates",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","OPT")),
    "method_returns": ("array","array","null")
    }
text_dot_point = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_dot_point",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","OPT")),
    "method_returns": ("array","array","null")
    }
text_dot_text = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_dot_text",
    "method_parameters": (("object","str","REQ"),("text","str","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_font = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_object_font",
    "method_parameters": (("object","str","REQ"),("font","str","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_height = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_object_height",
    "method_parameters": (("object","str","REQ"),("height","dbl","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_plane = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_object_plane",
    "method_parameters": (("object","str","REQ"),("plane","arr_of_dbl","OPT")),
    "method_returns": ("array","array","null")
    }
text_object_point = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_object_point",
    "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_style = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_object_style",
    "method_parameters": (("object","str","REQ"),("style","int","OPT")),
    "method_returns": ("number","number","null")
    }
text_object_text = {
    "method_location": "Geometry",
    "method_type": "METHOD",
    "method_name": "text_object_text",
    "method_parameters": (("object","str","REQ"),("text","str","OPT")),
    "method_returns": ("string","string","null")
    }
