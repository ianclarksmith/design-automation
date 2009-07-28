#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.
#===============================================================================
# DirectionalLight
#===============================================================================
add_directional_light = {#ed
    "method_location": "_Object._LightType.DirectionalLight",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("start_point","array of dbl","REQ"),("end_point","array of dbl","REQ")),
    "method_returns": ("_Object._LightType.DirectionalLight","null")
    }
#===============================================================================
# LinearLight
#===============================================================================
add_linear_light = {#ed
    "method_location": "_Object._LightType.LinearLight",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("start_point","array of dbl","REQ"),("end_point","array of dbl","REQ"),("width","dbl","OPT")),
    "method_returns": ("_Object._LightType.LinearLight","null")
    }
#===============================================================================
# PointLight
#===============================================================================
add_point_light = {#ed
    "method_location": "_Object._LightType.PointLight",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("point","array of dbl","REQ")),
    "method_returns": ("_Object._LightType.PointLight","null")
    }
#===============================================================================
# RectangularLight
#===============================================================================
add_rectangular_light = {#ed
    "method_location": "_Object._LightType.RectangularLight",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("origin","array of dbl","REQ"),("width","array of dbl","REQ"),("height","array of dbl","REQ")),
    "method_returns": ("_Object._LightType.RectangularLight","null")
    }
#===============================================================================
# SpotLight
#===============================================================================
add_spot_light = {#ed
    "method_location": "_Object._LightType.SpotLight",
    "method_type": "CONSTRUCTOR",
    "method_name": "",
    "method_parameters": (("origin","array of dbl","REQ"),("radius","dbl","REQ"),("apex","array of dbl","REQ")),
    "method_returns": ("_Object._LightType.SpotLight","null")
    }
#===============================================================================
# _LightType
#===============================================================================

enable_light = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "enable_light",
    "method_parameters": (("","self","REQ"),("enable","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
is_directional_light = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_directional_light",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_light = {#ed
    "method_location": "_Object",
    "method_type": "METHOD",
    "method_name": "is_light",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_light_enabled = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "is_light_enabled",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_light_reference = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "is_light_reference",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_linear_light = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "is_linear_light",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_point_light = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "is_point_light",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_rectangular_light = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "is_rectangular_light",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
is_spot_light = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "is_spot_light",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("boolean","null")
    }
light_color = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "light_color",
    "method_parameters": (("","self","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","null")
    }
light_count = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "light_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
light_direction = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "light_direction",
    "method_parameters": (("","self","REQ"),("direction","array of dbl","OPT")),
    "method_returns": ("array of dbl","array of dbl","null")
    }
light_location = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "light_location",
    "method_parameters": (("","self","REQ"),("location","array of dbl","OPT")),
    "method_returns": ("array of_dbl","array of dbl","null")
    }
light_name = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "light_name",
    "method_parameters": (("","self","REQ"),("name","str","OPT")),
    "method_returns": ("_Object._LightType","_Object._LightType","null")
    }
light_objects = {#ed
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "light_objects",
    "method_parameters": (),
    "method_returns": ("array of_Object._LightType","null")
    }
rectangular_light_plane = {
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "rectangular_light_plane",
    "method_parameters": (("","self","REQ")),
    "method_returns": ("Array of (array of dbl, array of dbl, array of dbl, array of dbl)","null")
    }
spot_light_hardness = {
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "spot_light_hardness",
    "method_parameters": (("","self","REQ"),("hardness","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
spot_light_radius = {
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "spot_light_radius",
    "method_parameters": (("","self","REQ"),("radius","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
spot_light_shadow_intensity = {
    "method_location": "_Object._LightType",
    "method_type": "METHOD",
    "method_name": "spot_light_shadow_intensity",
    "method_parameters": (("","self","REQ"),("intensity","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
