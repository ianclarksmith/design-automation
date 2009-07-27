#The data below will be used to generate the Rhinoscript functions

#Errors can be fixed by hand here

all_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "all_objects",
    "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
first_object = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "first_object",
    "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("string","null")
    }
get_curve_object = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "get_curve_object",
    "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "method_returns": ("array","null")
    }
get_object_ex = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "get_object_ex",
    "method_parameters": (("message","str","OPT"),("type","int","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","arr_of_str","OPT")),
    "method_returns": ("array","null")
    }
get_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "get_objects",
    "method_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","arr_of_str","OPT")),
    "method_returns": ("array","null")
    }
get_objects_ex = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "get_objects_ex",
    "method_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","arr_of_str","OPT")),
    "method_returns": ("array","null")
    }
get_point_coordinates = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "get_point_coordinates",
    "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT")),
    "method_returns": ("array","null")
    }
get_surface_object = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "get_surface_object",
    "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
    "method_returns": ("array","null")
    }
hidden_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "hidden_objects",
    "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
invert_selected_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "invert_selected_objects",
    "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
last_created_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "last_created_objects",
    "method_parameters": (("select","bln","OPT")),
    "method_returns": ("array","null")
    }
last_object = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "last_object",
    "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("string","null")
    }
locked_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "locked_objects",
    "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
next_object = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "next_object",
    "method_parameters": (("object","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("string","null")
    }
normal_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "normal_objects",
    "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
objects_by_color = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "objects_by_color",
    "method_parameters": (("color","lng","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
    "method_returns": ("array","null")
    }
objects_by_group = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "objects_by_group",
    "method_parameters": (("group","str","REQ"),("select","bln","OPT")),
    "method_returns": ("array","null")
    }
objects_by_layer = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "objects_by_layer",
    "method_parameters": (("layer","str","REQ"),("select","bln","OPT")),
    "method_returns": ("array","null")
    }
objects_by_name = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "objects_by_name",
    "method_parameters": (("name","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
    "method_returns": ("array","null")
    }
objects_by_type = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "objects_by_type",
    "method_parameters": (("type","int","REQ"),("select","bln","OPT")),
    "method_returns": ("array","null")
    }
objects_by_u_r_l = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "objects_by_u_r_l",
    "method_parameters": (("u_r_l","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
    "method_returns": ("array","null")
    }
prev_selected_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "prev_selected_objects",
    "method_parameters": (("select","bln","OPT")),
    "method_returns": ("array","null")
    }
reference_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "reference_objects",
    "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
selected_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "selected_objects",
    "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
unselect_all_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "unselect_all_objects",
    "method_parameters": (),
    "method_returns": ("number")
    }
unselected_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "unselected_objects",
    "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
visible_objects = {
    "method_location": "Selection",
    "method_type": "METHOD",
    "method_name": "visible_objects",
    "method_parameters": (("view","str","OPT"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
    "method_returns": ("array","null")
    }
