#The data below will be used to generate the Rhinoscript function wrappers

#Errors can be fixed by hand here

browse_for_folder = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "browse_for_folder",
    "method_parameters": (("folder","str","OPT"),("message","str","OPT"),("title","str","OPT")),
    "method_returns": ("string","null")
    }
check_list_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "check_list_box",
    "method_parameters": (("items","array_of str","REQ"),("values","array_of bln","REQ"),("message","str","OPT"),("title","str","OPT")),
    "method_returns": ("array","null")
    }
combo_list_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "combo_list_box",
    "method_parameters": (("items","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "method_returns": ("string","null")
    }
edit_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "edit_box",
    "method_parameters": (("string","str","OPT"),("message","str","OPT"),("title","str","OPT")),
    "method_returns": ("string","null")
    }
get_angle = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_angle",
    "method_parameters": (("point","array_of dbl","OPT"),("reference","array_of dbl","OPT"),("angle","dbl","OPT"),("message","str","OPT")),
    "method_returns": ("number","null")
    }
get_boolean = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_boolean",
    "method_parameters": (("message","str","REQ"),("items","array_of str","REQ"),("defaults","array_of bln","REQ")),
    "method_returns": ("array","null")
    }
get_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_box",
    "method_parameters": (("mode","int","OPT"),("point","array_of dbl","OPT"),("prompt_1","str","OPT"),("prompt_2","str","OPT"),("prompt_3","str","OPT")),
    "method_returns": ("array","null")
    }
get_color = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_color",
    "method_parameters": (("color","lng","OPT"),),
    "method_returns": ("number","null")
    }
get_distance = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_distance",
    "method_parameters": (("point","array_of dbl","OPT"),("distance","dbl","OPT"),("message_1","str","OPT"),("message_2","str","OPT")),
    "method_returns": ("number","null")
    }
get_integer = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_integer",
    "method_parameters": (("message","str","OPT"),("number","int","OPT"),("min","int","OPT"),("max","int","OPT")),
    "method_returns": ("number","null")
    }
get_layer = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_layer",
    "method_parameters": (("title","str","OPT"),("layer","str","OPT"),("show_new_layer","bln","OPT"),("show_set_current","bln","OPT")),
    "method_returns": ("string","null")
    }
get_linetype = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_linetype",
    "method_parameters": (("linetype","str","OPT"),),
    "method_returns": ("string","null")
    }
get_point_on_curve = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_point_on_curve",
    "method_parameters": (("object","str","REQ"),("message","str","OPT")),
    "method_returns": ("array","null")
    }
get_point_on_line = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_point_on_line",
    "method_parameters": (("message","str","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),("track","bln","OPT")),
    "method_returns": ("array","null")
    }
get_point_on_mesh = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_point_on_mesh",
    "method_parameters": (("object","str","REQ"),("message","str","OPT")),
    "method_returns": ("array","null")
    }
get_point_on_plane = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_point_on_plane",
    "method_parameters": (("message","str","OPT"),("plane","array_of dbl","OPT"),("point","array_of dbl","OPT")),
    "method_returns": ("array","null")
    }
get_point_on_surface = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_point_on_surface",
    "method_parameters": (("object","str","REQ"),("message","str","OPT")),
    "method_returns": ("array","null")
    }
get_points = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_points",
    "method_parameters": (("draw","bln","OPT"),("plane","bln","OPT"),("message_1","str","OPT"),("message_2","str","OPT"),("max_points","int","OPT"),("base_point","array_of dbl","OPT")),
    "method_returns": ("array","null")
    }
get_print_width = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_print_width",
    "method_parameters": (("print_width","dbl","OPT"),),
    "method_returns": ("number","null")
    }
get_real = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_real",
    "method_parameters": (("message","str","OPT"),("number","dbl","OPT"),("min","dbl","OPT"),("max","dbl","OPT")),
    "method_returns": ("number","null")
    }
get_rectangle = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_rectangle",
    "method_parameters": (("mode","int","OPT"),("point","array_of dbl","OPT"),("prompt_1","str","OPT"),("prompt_2","str","OPT"),("prompt_3","str","OPT")),
    "method_returns": ("array","null")
    }
get_string = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_string",
    "method_parameters": (("message","str","OPT"),("string","str","OPT"),("strings","array_of str","OPT")),
    "method_returns": ("string","null")
    }
get_surface_iso_param_point = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "get_surface_iso_param_point",
    "method_parameters": (("object","str","REQ"),("message","str","OPT")),
    "method_returns": ("array","null")
    }
html_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "html_box",
    "method_parameters": (("file_name","str","REQ"),("arguments","va","OPT"),("options","str","OPT"),("modal","bln","OPT")),
    "method_returns": ("boolean","null")
    }
integer_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "integer_box",
    "method_parameters": (("message","str","OPT"),("number","int","OPT"),("title","str","OPT")),
    "method_returns": ("number","null")
    }
list_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "list_box",
    "method_parameters": (("items","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "method_returns": ("string","null")
    }
message_beep = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "message_beep",
    "method_parameters": (("beep","int","OPT"),),
    "method_returns": ()
    }
message_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "message_box",
    "method_parameters": (("message","str","REQ"),("buttons","int","OPT"),("title","str","OPT")),
    "method_returns": ("number",)
    }
multi_list_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "multi_list_box",
    "method_parameters": (("items","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "method_returns": ("array","null")
    }
open_file_names = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "open_file_names",
    "method_parameters": (("title","str","OPT"),("filter","str","OPT"),("folder","str","OPT"),("filename","str","OPT"),("extension","str","OPT")),
    "method_returns": ("array","null")
    }
popup_menu = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "popup_menu",
    "method_parameters": (("items","array_of str","REQ"),("modes","array_of int","OPT"),("point","array_of dbl","OPT"),("view","str","OPT")),
    "method_returns": ("number","number","null")
    }
property_list_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "property_list_box",
    "method_parameters": (("items","array_of str","REQ"),("values","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "method_returns": ("array","null")
    }
real_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "real_box",
    "method_parameters": (("message","str","OPT"),("number","dbl","OPT"),("title","str","OPT")),
    "method_returns": ("number","null")
    }
save_file_name = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "save_file_name",
    "method_parameters": (("title","str","OPT"),("filter","str","OPT"),("folder","str","OPT"),("filename","str","OPT"),("extension","str","OPT")),
    "method_returns": ("string","null")
    }
string_box = {
    "method_location": "UserInterface",
    "method_type": "METHOD",
    "method_name": "string_box",
    "method_parameters": (("message","str","OPT"),("string","str","OPT"),("title","str","OPT")),
    "method_returns": ("string","null")
    }
