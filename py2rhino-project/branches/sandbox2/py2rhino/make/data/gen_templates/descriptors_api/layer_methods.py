#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

add_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "add_layer",
    "method_parameters": (("layer","str","OPT"),("color","lng","OPT"),("visible","bln","OPT"),("locked","bln","OPT"),("parent","str","OPT")),
    "method_returns": ("string","null")
    }
current_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "current_layer",
    "method_parameters": (("layer","str","OPT")),
    "method_returns": ("string","string","null")
    }
delete_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "delete_layer",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("boolean","null")
    }
expand_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "expand_layer",
    "method_parameters": (("layer","str","REQ"),("expand","bln","REQ")),
    "method_returns": ("boolean","null")
    }
is_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_changeable = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_changeable",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_child_of = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_child_of",
    "method_parameters": (("layer","str","REQ"),("test","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_layer_current = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_current",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_empty = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_empty",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_expanded = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_expanded",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_layer_locked = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_locked",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_on = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_on",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_parent_of = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_parent_of",
    "method_parameters": (("layer","str","REQ"),("test","str","REQ")),
    "method_returns": ("boolean","null")
    }
is_layer_reference = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_reference",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_selectable = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_selectable",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
is_layer_visible = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "is_layer_visible",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("null")
    }
layer_child_count = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_child_count",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("number","null")
    }
layer_children = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_children",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("array","null")
    }
layer_color = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_color",
    "method_parameters": (("layer","str","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","null")
    }
layer_count = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
layer_linetype = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_linetype",
    "method_parameters": (("layer","str","REQ"),("linetype","str","OPT")),
    "method_returns": ("string","string","null")
    }
layer_locked = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_locked",
    "method_parameters": (("layer","str","REQ"),("visible","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
layer_material_index = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_material_index",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("number","null")
    }
layer_mode = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_mode",
    "method_parameters": (("layer","str","REQ"),("mode","int","OPT")),
    "method_returns": ("number","number","null")
    }
layer_names = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_names",
    "method_parameters": (("sort","bln","OPT")),
    "method_returns": ("array","null")
    }
layer_order = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_order",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("number","null")
    }
layer_print_color = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_print_color",
    "method_parameters": (("layer","str","REQ"),("color","lng","OPT")),
    "method_returns": ("number","number","null")
    }
layer_print_width = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_print_width",
    "method_parameters": (("layer","str","REQ"),("width","dbl","OPT")),
    "method_returns": ("number","number","null")
    }
layer_visible = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "layer_visible",
    "method_parameters": (("layer","str","REQ"),("visible","bln","OPT")),
    "method_returns": ("boolean","boolean","null")
    }
parent_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "parent_layer",
    "method_parameters": (("layer","str","REQ"),("parent","str","OPT")),
    "method_returns": ("string","string","null")
    }
purge_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "purge_layer",
    "method_parameters": (("layer","str","REQ")),
    "method_returns": ("string","null")
    }
rename_layer = {
    "method_location": "Layer",
    "method_type": "METHOD",
    "method_name": "rename_layer",
    "method_parameters": (("old_name","str","REQ"),("new_name","str","REQ")),
    "method_returns": ("string","null")
    }
