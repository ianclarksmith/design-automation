#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

add_directional_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "add_directional_light",
    "method_parameters": (("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_linear_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "add_linear_light",
    "method_parameters": (("start_point","array_of dbl","REQ"),("end_point","array_of dbl","REQ"),("width","dbl","OPT")),
    "method_returns": ("string","null")
    }
add_point_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "add_point_light",
    "method_parameters": (("point","array_of dbl","REQ"),),
    "method_returns": ("string","null")
    }
add_rectangular_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "add_rectangular_light",
    "method_parameters": (("origin","array_of dbl","REQ"),("width","array_of dbl","REQ"),("height","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
add_spot_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "add_spot_light",
    "method_parameters": (("origin","array_of dbl","REQ"),("radius","dbl","REQ"),("apex","array_of dbl","REQ")),
    "method_returns": ("string","null")
    }
enable_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "enable_light",
    "method_parameters": (("object","str","REQ"),("enable","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
is_directional_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_directional_light",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_light",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_light_enabled = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_light_enabled",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_light_reference = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_light_reference",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_linear_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_linear_light",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_point_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_point_light",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_rectangular_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_rectangular_light",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
is_spot_light = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "is_spot_light",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("boolean","null")
    }
light_color = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "light_color",
    "method_parameters": (("object","str","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","null")
    }
light_count = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "light_count",
    "method_parameters": (),
    "method_returns": ("number",)
    }
light_direction = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "light_direction",
    "method_parameters": (("object","str","REQ"),("direction","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
light_location = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "light_location",
    "method_parameters": (("object","str","REQ"),("location","array_of dbl","OPT")),
    "method_returns": ("array","array","null")
    }
light_name = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "light_name",
    "method_parameters": (("object","str","REQ"),("name","str","OPT")),
    "method_returns": ("string","string","null")
    }
light_objects = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "light_objects",
    "method_parameters": (),
    "method_returns": ("array","null")
    }
rectangular_light_plane = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "rectangular_light_plane",
    "method_parameters": (("object","str","REQ"),),
    "method_returns": ("array","array","array","array","array","null")
    }
spot_light_hardness = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "spot_light_hardness",
    "method_parameters": (("object","str","REQ"),("hardness","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
spot_light_radius = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "spot_light_radius",
    "method_parameters": (("object","str","REQ"),("radius","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
spot_light_shadow_intensity = {
    "method_location": "Light",
    "method_type": "METHOD",
    "method_name": "spot_light_shadow_intensity",
    "method_parameters": (("object","str","REQ"),("intensity","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
