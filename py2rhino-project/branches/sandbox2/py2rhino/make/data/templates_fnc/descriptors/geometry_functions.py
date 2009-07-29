#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_clipping_plane = {
    "function_location": "geometry",
    "function_com_id": 904,
    "function_vb_name": "AddClippingPlane",
    "function_name": "add_clipping_plane",
    "function_parameters": (("plane","array_of dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),("views","array_of str","OPT")),
    "function_returns": ("string","null")
    }
add_point_cloud = {
    "function_location": "geometry",
    "function_com_id": 69,
    "function_vb_name": "AddPointCloud",
    "function_name": "add_point_cloud",
    "function_parameters": (("points","array_of dbl","REQ"),),
    "function_returns": ("string","null")
    }
add_points = {
    "function_location": "geometry",
    "function_com_id": 526,
    "function_vb_name": "AddPoints",
    "function_name": "add_points",
    "function_parameters": (("points","array_of dbl","REQ"),),
    "function_returns": ("array","null")
    }
add_text = {
    "function_location": "geometry",
    "function_com_id": 76,
    "function_vb_name": "AddText",
    "function_name": "add_text",
    "function_parameters": (("text","str","REQ"),("point","array_of dbl","REQ"),("height","dbl","OPT"),("font","str","OPT"),("style","int","OPT")),
    "function_returns": ("string","null")
    }
add_text_2 = {
    "function_location": "geometry",
    "function_com_id": 76,
    "function_vb_name": "AddText",
    "function_name": "add_text_2",
    "function_parameters": (("text","str","REQ"),("plane","array_of dbl","REQ"),("height","dbl","OPT"),("font","str","OPT"),("style","int","OPT")),
    "function_returns": ("string","null")
    }
add_text_dot = {
    "function_location": "geometry",
    "function_com_id": 320,
    "function_vb_name": "AddTextDot",
    "function_name": "add_text_dot",
    "function_parameters": (("test","str","REQ"),("point","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
bounding_box = {
    "function_location": "geometry",
    "function_com_id": 117,
    "function_vb_name": "BoundingBox",
    "function_name": "bounding_box",
    "function_parameters": (("objects","array_of str","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
    "function_returns": ("array","null")
    }
compare_geometry = {
    "function_location": "geometry",
    "function_com_id": 598,
    "function_vb_name": "CompareGeometry",
    "function_name": "compare_geometry",
    "function_parameters": (("object_1","str","REQ"),("object_2","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_clipping_plane = {
    "function_location": "geometry",
    "function_com_id": 905,
    "function_vb_name": "IsClippingPlane",
    "function_name": "is_clipping_plane",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_point = {
    "function_location": "geometry",
    "function_com_id": 120,
    "function_vb_name": "IsPoint",
    "function_name": "is_point",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_point_cloud = {
    "function_location": "geometry",
    "function_com_id": 121,
    "function_vb_name": "IsPointCloud",
    "function_name": "is_point_cloud",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_text = {
    "function_location": "geometry",
    "function_com_id": 122,
    "function_vb_name": "IsText",
    "function_name": "is_text",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_text_dot = {
    "function_location": "geometry",
    "function_com_id": 336,
    "function_vb_name": "IsTextDot",
    "function_name": "is_text_dot",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
point_cloud_count = {
    "function_location": "geometry",
    "function_com_id": 128,
    "function_vb_name": "PointCloudCount",
    "function_name": "point_cloud_count",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("number","null")
    }
point_cloud_points = {
    "function_location": "geometry",
    "function_com_id": 129,
    "function_vb_name": "PointCloudPoints",
    "function_name": "point_cloud_points",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","null")
    }
point_coordinates = {
    "function_location": "geometry",
    "function_com_id": 130,
    "function_vb_name": "PointCoordinates",
    "function_name": "point_coordinates",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
text_dot_point = {
    "function_location": "geometry",
    "function_com_id": 422,
    "function_vb_name": "TextDotPoint",
    "function_name": "text_dot_point",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
text_dot_text = {
    "function_location": "geometry",
    "function_com_id": 421,
    "function_vb_name": "TextDotText",
    "function_name": "text_dot_text",
    "function_parameters": (("object","str","REQ"),("text","str","OPT")),
    "function_returns": ("string","string","null")
    }
text_object_font = {
    "function_location": "geometry",
    "function_com_id": 474,
    "function_vb_name": "TextObjectFont",
    "function_name": "text_object_font",
    "function_parameters": (("object","str","REQ"),("font","str","OPT")),
    "function_returns": ("string","string","null")
    }
text_object_height = {
    "function_location": "geometry",
    "function_com_id": 473,
    "function_vb_name": "TextObjectHeight",
    "function_name": "text_object_height",
    "function_parameters": (("object","str","REQ"),("height","dbl","OPT")),
    "function_returns": ("string","string","null")
    }
text_object_plane = {
    "function_location": "geometry",
    "function_com_id": 476,
    "function_vb_name": "TextObjectPlane",
    "function_name": "text_object_plane",
    "function_parameters": (("object","str","REQ"),("plane","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
text_object_point = {
    "function_location": "geometry",
    "function_com_id": 471,
    "function_vb_name": "TextObjectPoint",
    "function_name": "text_object_point",
    "function_parameters": (("object","str","REQ"),("point","array_of dbl","OPT")),
    "function_returns": ("string","string","null")
    }
text_object_style = {
    "function_location": "geometry",
    "function_com_id": 475,
    "function_vb_name": "TextObjectStyle",
    "function_name": "text_object_style",
    "function_parameters": (("object","str","REQ"),("style","int","OPT")),
    "function_returns": ("number","number","null")
    }
text_object_text = {
    "function_location": "geometry",
    "function_com_id": 472,
    "function_vb_name": "TextObjectText",
    "function_name": "text_object_text",
    "function_parameters": (("object","str","REQ"),("text","str","OPT")),
    "function_returns": ("string","string","null")
    }
