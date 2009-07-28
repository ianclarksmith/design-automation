#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

add_hatch = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "add_hatch",
    "method_parameters": (("curve","str","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT")),
    "method_returns": ("string","null")
    }
add_hatch_patterns = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "add_hatch_patterns",
    "method_parameters": (("file_name","str","REQ"),("replace","bln","OPT")),
    "method_returns": ("array","null")
    }
add_hatches = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "add_hatches",
    "method_parameters": (("curves","arr_of_str","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT")),
    "method_returns": ("array","null")
    }
current_hatch_pattern = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "current_hatch_pattern",
    "method_parameters": (("hatch","str","OPT")),
    "method_returns": ("string","string","null")
    }
explode_hatch = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "explode_hatch",
    "method_parameters": (("hatch","str","REQ"),("delete","bln","OPT")),
    "method_returns": ("array","null")
    }
hatch_pattern = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern",
    "method_parameters": (("object","str","REQ"),("hatch","str","OPT")),
    "method_returns": ("string","string","null")
    }
hatch_pattern_count = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
hatch_pattern_description = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_description",
    "method_parameters": (("hatch","str","REQ")),
    "method_returns": ("string","null")
    }
hatch_pattern_fill_type = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_fill_type",
    "method_parameters": (("hatch","str","REQ")),
    "method_returns": ("number","null")
    }
hatch_pattern_names = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_pattern_names",
    "method_parameters": (),
    "method_returns": ("array","null")
    }
hatch_rotation = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_rotation",
    "method_parameters": (("object","str","REQ"),("rotation","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
hatch_scale = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "hatch_scale",
    "method_parameters": (("object","str","REQ"),("scale","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
is_hatch = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "is_hatch",
    "method_parameters": (("object","str","REQ")),
    "method_returns": ("null")
    }
is_hatch_pattern = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "is_hatch_pattern",
    "method_parameters": (("hatch","str","REQ")),
    "method_returns": ("null")
    }
is_hatch_pattern_current = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "is_hatch_pattern_current",
    "method_parameters": (("hatch","str","REQ")),
    "method_returns": ("null")
    }
is_hatch_pattern_reference = {
    "method_location": "Hatch",
    "method_type": "METHOD",
    "method_name": "is_hatch_pattern_reference",
    "method_parameters": (("hatch","str","REQ")),
    "method_returns": ("null")
    }
