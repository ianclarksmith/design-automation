#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.
#===============================================================================
# Point
#===============================================================================
add_points = {#ed
    "method_location": "_Object._PointType.Point",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("points","array of dbl","REQ")),
    "method_returns": ("array of _Object._PointType.PointCloud","null")
    }
#===============================================================================
# PointCloud
#===============================================================================
add_point_cloud = {#ed
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("points","array of dbl","REQ")),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }
point_cloud_count = {#ed
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "METHOD",
    "method_name": "point_cloud_count",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("number","null")
    }
point_cloud_points = {#ed
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "METHOD",
    "method_name": "point_cloud_points",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("array of dbl","null")
    }
#===============================================================================
# _PointType
#===============================================================================
point_coordinates = {#ed
    "method_location": "_Object._PointType",
    "method_type": "METHOD",
    "method_name": "point_coordinates",
    "method_parameters": (("","self","REQ"),("point","array of dbl","OPT")),
    "method_returns": ("array of dbl","array of dbl","null")
    }
#===============================================================================
# Text
#===============================================================================
add_text = {
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("text","str","REQ"),("point","array of dbl","REQ"),("plane","array of dbl","REQ"),("height","dbl","OPT"),("font","str","OPT"),("style","int","OPT")),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }
#===============================================================================
# TextDot
#===============================================================================
add_text_dot = {
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("test","str","REQ"),("point","array of dbl","REQ")),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }
#===============================================================================
# _TextType
#===============================================================================

text_dot_point = {#ed
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_dot_point",
    "method_parameters": (("","self","REQ"),("point","array of dbl","OPT")),
    "method_returns": ("array of dbl","array of dbl","null")
    }
text_dot_text = {
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_dot_text",
    "method_parameters": (("","self","REQ"),("text","str","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_font = {#ed
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_object_font",
    "method_parameters": (("","self","REQ"),("font","str","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_height = {#ed
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_object_height",
    "method_parameters": (("","self","REQ"),("height","dbl","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_plane = {#ed
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_object_plane",
    "method_parameters": (("","self","REQ"),("plane","array of dbl","OPT")),
    "method_returns": ("array of _Object._TextType","array of _Object._TextType","null")
    }
text_object_point = {#ed
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_object_point",
    "method_parameters": (("","self","REQ"),("point","arr_of_dbl","OPT")),
    "method_returns": ("string","string","null")
    }
text_object_style = {#ed
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_object_style",
    "method_parameters": (("","self","REQ"),("style","int","OPT")),
    "method_returns": ("number","number","null")
    }
text_object_text = {#ed
    "method_location": "_Object._TextType",
    "method_type": "METHOD",
    "method_name": "text_object_text",
    "method_parameters": (("","self","REQ"),("text","str","OPT")),
    "method_returns": ("string","string","null")
    }
#===============================================================================
# ClippingPlane
#===============================================================================
add_clipping_plane = {#ed
    "method_location": "_Object._OtherType.ClippingPlane",
    "method_type": "METHOD",
    "method_name": "add_clipping_plane",
    "method_parameters": (("plane","array of dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),("views","array of str","OPT")),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }
#===============================================================================
# _Object
#===============================================================================
bounding_box = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "bounding_box",
    "method_parameters": (("objects","array of str","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
    "method_returns": ("array of dbl","null")
    }
compare_geometry = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "compare_geometry",
    "method_parameters": (("","self","REQ"),("object_0","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_clipping_plane = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_clipping_plane",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_point = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_point",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_point_cloud = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_point_cloud",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_text = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_text",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_text_dot = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_text_dot",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
