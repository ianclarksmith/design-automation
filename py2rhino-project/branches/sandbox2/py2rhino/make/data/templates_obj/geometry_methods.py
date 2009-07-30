#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

#===============================================================================
# Point
#===============================================================================

#constructors

add_points = {#ed
    "method_location": "_Object._PointType.Point",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_point",
    "method_parameters": (("points","array_of dbl","REQ"),),
    "method_returns": ("array_of _Object._PointType.PointCloud","null")
    }

#methods

point_coordinates = {#ed
    "method_location": "_Object._PointType",
    "method_type": "METHOD",
    "method_name": "coordinates",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }

#===============================================================================
# PointCloud
#===============================================================================

#constructors

add_point_cloud = {#ed
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_point_cloud",
    "method_parameters": (("points","array_of dbl","REQ"),),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }

#methods

point_cloud_count = {#ed
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "METHOD",
    "method_name": "count",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
point_cloud_points = {#ed
    "method_location": "_Object._PointType.PointCloud",
    "method_type": "METHOD",
    "method_name": "points",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array_of dbl","null")
    }

#===============================================================================
# _PointType
#===============================================================================

#===============================================================================
# Text
#===============================================================================

#constructor

add_text = {
    "method_location": "_Object._TextType.Text",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_text",
    "method_parameters": (("text","str","REQ"),("point","array_of dbl","REQ"),("plane","array_of dbl","REQ"),("height","dbl","OPT"),("font","str","OPT"),("style","int","OPT"),),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }

#methods

text_object_font = {#ed
    "method_location": "_Object._TextType.Text",
    "method_type": "METHOD",
    "method_name": "font",
    "method_parameters": (("","self","REQ"),("font","str","OPT"),),
    "method_returns": ("string","string","null")
    }
text_object_height = {#ed
    "method_location": "_Object._TextType.Text",
    "method_type": "METHOD",
    "method_name": "height",
    "method_parameters": (("","self","REQ"),("height","dbl","OPT"),),
    "method_returns": ("string","string","null")
    }
text_object_plane = {#ed
    "method_location": "_Object._TextType.Text",
    "method_type": "METHOD",
    "method_name": "plane",
    "method_parameters": (("","self","REQ"),("plane","array_of dbl","OPT"),),
    "method_returns": ("array_of _Object._TextType","array_of _Object._TextType","null")
    }
text_object_point = {#ed
    "method_location": "_Object._TextType.Text",
    "method_type": "METHOD",
    "method_name": "point",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","OPT"),),
    "method_returns": ("string","string","null")
    }
text_object_style = {#ed
    "method_location": "_Object._TextType.Text",
    "method_type": "METHOD",
    "method_name": "style",
    "method_parameters": (("","self","REQ"),("style","int","OPT"),),
    "method_returns": ("number","number","null")
    }
text_object_text = {#ed
    "method_location": "_Object._TextType.Text",
    "method_type": "METHOD",
    "method_name": "text",
    "method_parameters": (("","self","REQ"),("text","str","OPT"),),
    "method_returns": ("string","string","null")
    }
#===============================================================================
# TextDot
#===============================================================================

#constructor

add_text_dot = {
    "method_location": "_Object._TextType.TextDot",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_text_dot",
    "method_parameters": (("test","str","REQ"),("point","array_of dbl","REQ"),),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }

#methods

text_dot_point = {#ed
    "method_location": "_Object._TextType.TextDot",
    "method_type": "METHOD",
    "method_name": "point",
    "method_parameters": (("","self","REQ"),("point","array_of dbl","OPT"),),
    "method_returns": ("array_of dbl","array_of dbl","null")
    }
text_dot_text = {
    "method_location": "_Object._TextType.TextDot",
    "method_type": "METHOD",
    "method_name": "text",
    "method_parameters": (("","self","REQ"),("text","str","OPT"),),
    "method_returns": ("string","string","null")
    }
#===============================================================================
# _TextType
#===============================================================================



#===============================================================================
# ClippingPlane
#===============================================================================

#constructor

add_clipping_plane = {#ed
    "method_location": "_Object._OtherType.ClippingPlane",
    "method_type": "METHOD",
    "method_name": "create_clipping_plane",
    "method_parameters": (("plane","array_of dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),("views","array_of str","OPT"),),
    "method_returns": ("_Object._PointType.PointCloud","null")
    }

#===============================================================================
# _Object
#===============================================================================

#methods

bounding_box = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "bounding_box",
    "method_parameters": (("objects","array_of str","REQ"),("view","str","OPT"),("world_coords","bln","OPT"),),
    "method_returns": ("array_of dbl","null")
    }
compare_geometry = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "compare_geometry",
    "method_parameters": (("","self","REQ"),("object_0","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_clipping_plane = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_clipping_plane",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_point = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_point",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_point_cloud = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_point_cloud",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_text = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_text",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
is_text_dot = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_text_dot",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("boolean","null")
    }
