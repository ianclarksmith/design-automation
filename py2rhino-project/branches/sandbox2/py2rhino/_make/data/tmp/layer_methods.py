#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

#===============================================================================
# Layer
#===============================================================================

#constructors

add_layer = {
    "method_location": "_Entity.Layer",
    "method_type": "CONSTRUCTOR",
    "method_name": "create_layer",
    "method_parameters": (("","self","OPT"),("color","lng","OPT"),("visible","bln","OPT"),("locked","bln","OPT"),("parent","str","OPT"),),
    "method_returns": ("str","null")
    }

#methods / functions

current_layer = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "current_layer",
    "method_parameters": (("","self","OPT"),),
    "method_returns": ("str","str","null")
    }

#methods

delete_layer = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "delete_layer",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
expand_layer = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "expand_layer",
    "method_parameters": (("","self","REQ"),("expand","bln","REQ"),),
    "method_returns": ("bln","null")
    }
layer_child_count = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_child_count",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
layer_children = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_children",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("array of _Entity.Layer","null")
    }
layer_color = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_color",
    "method_parameters": (("","self","REQ"),("color","lng","OPT"),),
    "method_returns": ("number","number","null")
    }
layer_linetype = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_linetype",
    "method_parameters": (("","self","REQ"),("linetype","str","OPT"),),
    "method_returns": ("str","str","null")
    }
layer_locked = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_locked",
    "method_parameters": (("","self","REQ"),("visible","bln","OPT"),),
    "method_returns": ("bln","bln","null")
    }
layer_material_index = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_material_index",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
layer_mode = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_mode",
    "method_parameters": (("","self","REQ"),("mode","int","OPT"),),
    "method_returns": ("number","number","null")
    }
layer_order = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_order",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("number","null")
    }
layer_print_color = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_print_color",
    "method_parameters": (("","self","REQ"),("color","lng","OPT"),),
    "method_returns": ("number","number","null")
    }
layer_print_width = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_print_width",
    "method_parameters": (("","self","REQ"),("width","dbl","OPT"),),
    "method_returns": ("number","number","null")
    }
layer_visible = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "layer_visible",
    "method_parameters": (("","self","REQ"),("visible","bln","OPT"),),
    "method_returns": ("bln","bln","null")
    }
parent_layer = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "parent_layer",
    "method_parameters": (("","self","REQ"),("parent","str","OPT"),),
    "method_returns": ("str","str","null")
    }
purge_layer = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "purge_layer",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("str","null")
    }
rename_layer = {
    "method_location": "_Entity.Layer",
    "method_type": "METHOD",
    "method_name": "rename_layer",
    "method_parameters": (("","self","REQ"),("new_name","str","REQ"),),
    "method_returns": ("str","null")
    }
#===============================================================================
# _Entity
#===============================================================================

#methods

is_layer = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_changeable = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_changeable",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_child_of = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_child_of",
    "method_parameters": (("","self","REQ"),("test","str","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_current = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_current",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_empty = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_empty",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_expanded = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_expanded",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_locked = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_locked",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_on = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_on",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("null")
    }
is_layer_parent_of = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_parent_of",
    "method_parameters": (("","self","REQ"),("test","str","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_reference = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_reference",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_selectable = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_selectable",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
is_layer_visible = {
    "method_location": "_Entity",
    "method_type": "METHOD",
    "method_name": "is_layer_visible",
    "method_parameters": (("","self","REQ"),),
    "method_returns": ("bln","null")
    }
#===============================================================================
#Document
#===============================================================================

#functions

layer_count = {
    "method_location": "Document",
    "method_type": "METHOD",
    "method_name": "layer_count",
    "method_parameters": (),
    "method_returns": ("number")
    }
layer_names = {
    "method_location": "Document",
    "method_type": "METHOD",
    "method_name": "layer_names",
    "method_parameters": (("sort","bln","OPT"),),
    "method_returns": ("array of str","null")
    }