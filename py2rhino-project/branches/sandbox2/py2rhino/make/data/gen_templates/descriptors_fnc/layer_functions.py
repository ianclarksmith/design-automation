#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_layer = {
    "function_location": "layer",
    "function_com_id": 3,
    "function_vb_name": "AddLayer",
    "function_name": "add_layer",
    "function_parameters": (("layer","str","OPT"),("color","lng","OPT"),("visible","bln","OPT"),("locked","bln","OPT"),("parent","str","OPT")),
    "function_returns": ("string","null")
    }
current_layer = {
    "function_location": "layer",
    "function_com_id": 5,
    "function_vb_name": "CurrentLayer",
    "function_name": "current_layer",
    "function_parameters": (("layer","str","OPT")),
    "function_returns": ("string","string","null")
    }
delete_layer = {
    "function_location": "layer",
    "function_com_id": 4,
    "function_vb_name": "DeleteLayer",
    "function_name": "delete_layer",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("boolean","null")
    }
expand_layer = {
    "function_location": "layer",
    "function_com_id": 690,
    "function_vb_name": "ExpandLayer",
    "function_name": "expand_layer",
    "function_parameters": (("layer","str","REQ"),("expand","bln","REQ")),
    "function_returns": ("boolean","null")
    }
is_layer = {
    "function_location": "layer",
    "function_com_id": 6,
    "function_vb_name": "IsLayer",
    "function_name": "is_layer",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_changeable = {
    "function_location": "layer",
    "function_com_id": 18,
    "function_vb_name": "IsLayerChangeable",
    "function_name": "is_layer_changeable",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_child_of = {
    "function_location": "layer",
    "function_com_id": 692,
    "function_vb_name": "IsLayerChildOf",
    "function_name": "is_layer_child_of",
    "function_parameters": (("layer","str","REQ"),("test","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_layer_current = {
    "function_location": "layer",
    "function_com_id": 313,
    "function_vb_name": "IsLayerCurrent",
    "function_name": "is_layer_current",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_empty = {
    "function_location": "layer",
    "function_com_id": 7,
    "function_vb_name": "IsLayerEmpty",
    "function_name": "is_layer_empty",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_expanded = {
    "function_location": "layer",
    "function_com_id": 689,
    "function_vb_name": "IsLayerExpanded",
    "function_name": "is_layer_expanded",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_layer_locked = {
    "function_location": "layer",
    "function_com_id": 8,
    "function_vb_name": "IsLayerLocked",
    "function_name": "is_layer_locked",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_on = {
    "function_location": "layer",
    "function_com_id": 9,
    "function_vb_name": "IsLayerOn",
    "function_name": "is_layer_on",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_parent_of = {
    "function_location": "layer",
    "function_com_id": 693,
    "function_vb_name": "IsLayerParentOf",
    "function_name": "is_layer_parent_of",
    "function_parameters": (("layer","str","REQ"),("test","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_layer_reference = {
    "function_location": "layer",
    "function_com_id": 10,
    "function_vb_name": "IsLayerReference",
    "function_name": "is_layer_reference",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_selectable = {
    "function_location": "layer",
    "function_com_id": 19,
    "function_vb_name": "IsLayerSelectable",
    "function_name": "is_layer_selectable",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
is_layer_visible = {
    "function_location": "layer",
    "function_com_id": 20,
    "function_vb_name": "IsLayerVisible",
    "function_name": "is_layer_visible",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("null")
    }
layer_child_count = {
    "function_location": "layer",
    "function_com_id": 694,
    "function_vb_name": "LayerChildCount",
    "function_name": "layer_child_count",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("number","null")
    }
layer_children = {
    "function_location": "layer",
    "function_com_id": 691,
    "function_vb_name": "LayerChildren",
    "function_name": "layer_children",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("array","null")
    }
layer_color = {
    "function_location": "layer",
    "function_com_id": 11,
    "function_vb_name": "LayerColor",
    "function_name": "layer_color",
    "function_parameters": (("layer","str","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
layer_count = {
    "function_location": "layer",
    "function_com_id": 12,
    "function_vb_name": "LayerCount",
    "function_name": "layer_count",
    "function_parameters": (),
    "function_returns": ("number")
    }
layer_linetype = {
    "function_location": "layer",
    "function_com_id": 602,
    "function_vb_name": "LayerLinetype",
    "function_name": "layer_linetype",
    "function_parameters": (("layer","str","REQ"),("linetype","str","OPT")),
    "function_returns": ("string","string","null")
    }
layer_locked = {
    "function_location": "layer",
    "function_com_id": 601,
    "function_vb_name": "LayerLocked",
    "function_name": "layer_locked",
    "function_parameters": (("layer","str","REQ"),("visible","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
layer_material_index = {
    "function_location": "layer",
    "function_com_id": 13,
    "function_vb_name": "LayerMaterialIndex",
    "function_name": "layer_material_index",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("number","null")
    }
layer_mode = {
    "function_location": "layer",
    "function_com_id": 14,
    "function_vb_name": "LayerMode",
    "function_name": "layer_mode",
    "function_parameters": (("layer","str","REQ"),("mode","int","OPT")),
    "function_returns": ("number","number","null")
    }
layer_names = {
    "function_location": "layer",
    "function_com_id": 15,
    "function_vb_name": "LayerNames",
    "function_name": "layer_names",
    "function_parameters": (("sort","bln","OPT")),
    "function_returns": ("array","null")
    }
layer_order = {
    "function_location": "layer",
    "function_com_id": 17,
    "function_vb_name": "LayerOrder",
    "function_name": "layer_order",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("number","null")
    }
layer_print_color = {
    "function_location": "layer",
    "function_com_id": 603,
    "function_vb_name": "LayerPrintColor",
    "function_name": "layer_print_color",
    "function_parameters": (("layer","str","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
layer_print_width = {
    "function_location": "layer",
    "function_com_id": 604,
    "function_vb_name": "LayerPrintWidth",
    "function_name": "layer_print_width",
    "function_parameters": (("layer","str","REQ"),("width","dbl","OPT")),
    "function_returns": ("number","number","null")
    }
layer_visible = {
    "function_location": "layer",
    "function_com_id": 600,
    "function_vb_name": "LayerVisible",
    "function_name": "layer_visible",
    "function_parameters": (("layer","str","REQ"),("visible","bln","OPT")),
    "function_returns": ("boolean","boolean","null")
    }
parent_layer = {
    "function_location": "layer",
    "function_com_id": 688,
    "function_vb_name": "ParentLayer",
    "function_name": "parent_layer",
    "function_parameters": (("layer","str","REQ"),("parent","str","OPT")),
    "function_returns": ("string","string","null")
    }
purge_layer = {
    "function_location": "layer",
    "function_com_id": 291,
    "function_vb_name": "PurgeLayer",
    "function_name": "purge_layer",
    "function_parameters": (("layer","str","REQ")),
    "function_returns": ("string","null")
    }
rename_layer = {
    "function_location": "layer",
    "function_com_id": 16,
    "function_vb_name": "RenameLayer",
    "function_name": "rename_layer",
    "function_parameters": (("old_name","str","REQ"),("new_name","str","REQ")),
    "function_returns": ("string","null")
    }
