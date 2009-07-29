#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_directional_light = {
    "function_location": "light",
    "function_com_id": 153,
    "function_vb_name": "AddDirectionalLight",
    "function_name": "add_directional_light",
    "function_parameters": (("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_linear_light = {
    "function_location": "light",
    "function_com_id": 154,
    "function_vb_name": "AddLinearLight",
    "function_name": "add_linear_light",
    "function_parameters": (("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("width","dbl","OPT")),
    "function_returns": ("string","null")
    }
add_point_light = {
    "function_location": "light",
    "function_com_id": 155,
    "function_vb_name": "AddPointLight",
    "function_name": "add_point_light",
    "function_parameters": (("point","array_of dbl","REQ"),),
    "function_returns": ("string","null")
    }
add_rectangular_light = {
    "function_location": "light",
    "function_com_id": 156,
    "function_vb_name": "AddRectangularLight",
    "function_name": "add_rectangular_light",
    "function_parameters": (("origin","array_of dbl","REQ"),("width","array_of dbl","REQ"),("height","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
add_spot_light = {
    "function_location": "light",
    "function_com_id": 157,
    "function_vb_name": "AddSpotLight",
    "function_name": "add_spot_light",
    "function_parameters": (("origin","array_of dbl","REQ"),("radius","dbl","REQ"),("apex","array_of dbl","REQ")),
    "function_returns": ("string","null")
    }
enable_light = {
    "function_location": "light",
    "function_com_id": 158,
    "function_vb_name": "EnableLight",
    "function_name": "enable_light",
    "function_parameters": (("object","str","REQ"),("enable","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
is_directional_light = {
    "function_location": "light",
    "function_com_id": 159,
    "function_vb_name": "IsDirectionalLight",
    "function_name": "is_directional_light",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_light = {
    "function_location": "light",
    "function_com_id": 160,
    "function_vb_name": "IsLight",
    "function_name": "is_light",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_light_enabled = {
    "function_location": "light",
    "function_com_id": 161,
    "function_vb_name": "IsLightEnabled",
    "function_name": "is_light_enabled",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_light_reference = {
    "function_location": "light",
    "function_com_id": 162,
    "function_vb_name": "IsLightReference",
    "function_name": "is_light_reference",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_linear_light = {
    "function_location": "light",
    "function_com_id": 163,
    "function_vb_name": "IsLinearLight",
    "function_name": "is_linear_light",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_point_light = {
    "function_location": "light",
    "function_com_id": 164,
    "function_vb_name": "IsPointLight",
    "function_name": "is_point_light",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_rectangular_light = {
    "function_location": "light",
    "function_com_id": 165,
    "function_vb_name": "IsRectangularLight",
    "function_name": "is_rectangular_light",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
is_spot_light = {
    "function_location": "light",
    "function_com_id": 166,
    "function_vb_name": "IsSpotLight",
    "function_name": "is_spot_light",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("boolean","null")
    }
light_color = {
    "function_location": "light",
    "function_com_id": 167,
    "function_vb_name": "LightColor",
    "function_name": "light_color",
    "function_parameters": (("object","str","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
light_count = {
    "function_location": "light",
    "function_com_id": 168,
    "function_vb_name": "LightCount",
    "function_name": "light_count",
    "function_parameters": (),
    "function_returns": ("number",)
    }
light_direction = {
    "function_location": "light",
    "function_com_id": 491,
    "function_vb_name": "LightDirection",
    "function_name": "light_direction",
    "function_parameters": (("object","str","REQ"),("direction","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
light_location = {
    "function_location": "light",
    "function_com_id": 490,
    "function_vb_name": "LightLocation",
    "function_name": "light_location",
    "function_parameters": (("object","str","REQ"),("location","array_of dbl","OPT")),
    "function_returns": ("array","array","null")
    }
light_name = {
    "function_location": "light",
    "function_com_id": 169,
    "function_vb_name": "LightName",
    "function_name": "light_name",
    "function_parameters": (("object","str","REQ"),("name","str","OPT")),
    "function_returns": ("string","string","null")
    }
light_objects = {
    "function_location": "light",
    "function_com_id": 170,
    "function_vb_name": "LightObjects",
    "function_name": "light_objects",
    "function_parameters": (),
    "function_returns": ("array","null")
    }
rectangular_light_plane = {
    "function_location": "light",
    "function_com_id": 776,
    "function_vb_name": "RectangularLightPlane",
    "function_name": "rectangular_light_plane",
    "function_parameters": (("object","str","REQ"),),
    "function_returns": ("array","array","array","array","array","null")
    }
spot_light_hardness = {
    "function_location": "light",
    "function_com_id": 171,
    "function_vb_name": "SpotLightHardness",
    "function_name": "spot_light_hardness",
    "function_parameters": (("object","str","REQ"),("hardness","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
spot_light_radius = {
    "function_location": "light",
    "function_com_id": 584,
    "function_vb_name": "SpotLightRadius",
    "function_name": "spot_light_radius",
    "function_parameters": (("object","str","REQ"),("radius","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
spot_light_shadow_intensity = {
    "function_location": "light",
    "function_com_id": 172,
    "function_vb_name": "SpotLightShadowIntensity",
    "function_name": "spot_light_shadow_intensity",
    "function_parameters": (("object","str","REQ"),("intensity","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
