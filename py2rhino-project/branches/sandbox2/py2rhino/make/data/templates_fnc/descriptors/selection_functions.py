#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

all_objects = {
    "function_location": "selection",
    "function_com_id": 30,
    "function_vb_name": "AllObjects",
    "function_name": "all_objects",
    "function_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
first_object = {
    "function_location": "selection",
    "function_com_id": 31,
    "function_vb_name": "FirstObject",
    "function_name": "first_object",
    "function_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("string","null")
    }
get_curve_object = {
    "function_location": "selection",
    "function_com_id": 575,
    "function_vb_name": "GetCurveObject",
    "function_name": "get_curve_object",
    "function_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "function_returns": ("array","null")
    }
get_object_ex = {
    "function_location": "selection",
    "function_com_id": 819,
    "function_vb_name": "GetObjectEx",
    "function_name": "get_object_ex",
    "function_parameters": (("message","str","OPT"),("type","int","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","array_of str","OPT")),
    "function_returns": ("array","null")
    }
get_objects = {
    "function_location": "selection",
    "function_com_id": 33,
    "function_vb_name": "GetObjects",
    "function_name": "get_objects",
    "function_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","array_of str","OPT")),
    "function_returns": ("array","null")
    }
get_objects_ex = {
    "function_location": "selection",
    "function_com_id": 820,
    "function_vb_name": "GetObjectsEx",
    "function_name": "get_objects_ex",
    "function_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","array_of str","OPT")),
    "function_returns": ("array","null")
    }
get_point_coordinates = {
    "function_location": "selection",
    "function_com_id": 645,
    "function_vb_name": "GetPointCoordinates",
    "function_name": "get_point_coordinates",
    "function_parameters": (("message","str","OPT"),("pre_select","bln","OPT")),
    "function_returns": ("array","null")
    }
get_surface_object = {
    "function_location": "selection",
    "function_com_id": 576,
    "function_vb_name": "GetSurfaceObject",
    "function_name": "get_surface_object",
    "function_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "function_returns": ("array","null")
    }
hidden_objects = {
    "function_location": "selection",
    "function_com_id": 366,
    "function_vb_name": "HiddenObjects",
    "function_name": "hidden_objects",
    "function_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
invert_selected_objects = {
    "function_location": "selection",
    "function_com_id": 34,
    "function_vb_name": "InvertSelectedObjects",
    "function_name": "invert_selected_objects",
    "function_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
last_created_objects = {
    "function_location": "selection",
    "function_com_id": 485,
    "function_vb_name": "LastCreatedObjects",
    "function_name": "last_created_objects",
    "function_parameters": (("select","bln","OPT"),),
    "function_returns": ("array","null")
    }
last_object = {
    "function_location": "selection",
    "function_com_id": 35,
    "function_vb_name": "LastObject",
    "function_name": "last_object",
    "function_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("string","null")
    }
locked_objects = {
    "function_location": "selection",
    "function_com_id": 365,
    "function_vb_name": "LockedObjects",
    "function_name": "locked_objects",
    "function_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
next_object = {
    "function_location": "selection",
    "function_com_id": 36,
    "function_vb_name": "NextObject",
    "function_name": "next_object",
    "function_parameters": (("object","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("string","null")
    }
normal_objects = {
    "function_location": "selection",
    "function_com_id": 364,
    "function_vb_name": "NormalObjects",
    "function_name": "normal_objects",
    "function_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
objects_by_color = {
    "function_location": "selection",
    "function_com_id": 37,
    "function_vb_name": "ObjectsByColor",
    "function_name": "objects_by_color",
    "function_parameters": (("color","lng","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
    "function_returns": ("array","null")
    }
objects_by_group = {
    "function_location": "selection",
    "function_com_id": 38,
    "function_vb_name": "ObjectsByGroup",
    "function_name": "objects_by_group",
    "function_parameters": (("group","str","REQ"),("select","bln","OPT")),
    "function_returns": ("array","null")
    }
objects_by_layer = {
    "function_location": "selection",
    "function_com_id": 39,
    "function_vb_name": "ObjectsByLayer",
    "function_name": "objects_by_layer",
    "function_parameters": (("layer","str","REQ"),("select","bln","OPT")),
    "function_returns": ("array","null")
    }
objects_by_name = {
    "function_location": "selection",
    "function_com_id": 40,
    "function_vb_name": "ObjectsByName",
    "function_name": "objects_by_name",
    "function_parameters": (("name","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
    "function_returns": ("array","null")
    }
objects_by_type = {
    "function_location": "selection",
    "function_com_id": 41,
    "function_vb_name": "ObjectsByType",
    "function_name": "objects_by_type",
    "function_parameters": (("type","int","REQ"),("select","bln","OPT")),
    "function_returns": ("array","null")
    }
objects_by_u_r_l = {
    "function_location": "selection",
    "function_com_id": 42,
    "function_vb_name": "ObjectsByURL",
    "function_name": "objects_by_u_r_l",
    "function_parameters": (("u_r_l","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
    "function_returns": ("array","null")
    }
prev_selected_objects = {
    "function_location": "selection",
    "function_com_id": 486,
    "function_vb_name": "PrevSelectedObjects",
    "function_name": "prev_selected_objects",
    "function_parameters": (("select","bln","OPT"),),
    "function_returns": ("array","null")
    }
reference_objects = {
    "function_location": "selection",
    "function_com_id": 367,
    "function_vb_name": "ReferenceObjects",
    "function_name": "reference_objects",
    "function_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
selected_objects = {
    "function_location": "selection",
    "function_com_id": 43,
    "function_vb_name": "SelectedObjects",
    "function_name": "selected_objects",
    "function_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
unselect_all_objects = {
    "function_location": "selection",
    "function_com_id": 44,
    "function_vb_name": "UnselectAllObjects",
    "function_name": "unselect_all_objects",
    "function_parameters": (),
    "function_returns": ("number",)
    }
unselected_objects = {
    "function_location": "selection",
    "function_com_id": 45,
    "function_vb_name": "UnselectedObjects",
    "function_name": "unselected_objects",
    "function_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
visible_objects = {
    "function_location": "selection",
    "function_com_id": 825,
    "function_vb_name": "VisibleObjects",
    "function_name": "visible_objects",
    "function_parameters": (("view","str","OPT"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "function_returns": ("array","null")
    }
