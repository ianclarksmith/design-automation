#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

browse_for_folder = {
    "function_location": "user_interface",
    "function_com_id": 146,
    "function_vb_name": "BrowseForFolder",
    "function_name": "browse_for_folder",
    "function_parameters": (("folder","str","OPT"),("message","str","OPT"),("title","str","OPT")),
    "function_returns": ("string","null")
    }
check_list_box = {
    "function_location": "user_interface",
    "function_com_id": 52,
    "function_vb_name": "CheckListBox",
    "function_name": "check_list_box",
    "function_parameters": (("items","array_of str","REQ"),("values","array_of bln","REQ"),("message","str","OPT"),("title","str","OPT")),
    "function_returns": ("array","null")
    }
combo_list_box = {
    "function_location": "user_interface",
    "function_com_id": 53,
    "function_vb_name": "ComboListBox",
    "function_name": "combo_list_box",
    "function_parameters": (("items","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "function_returns": ("string","null")
    }
edit_box = {
    "function_location": "user_interface",
    "function_com_id": 54,
    "function_vb_name": "EditBox",
    "function_name": "edit_box",
    "function_parameters": (("string","str","OPT"),("message","str","OPT"),("title","str","OPT")),
    "function_returns": ("string","null")
    }
get_angle = {
    "function_location": "user_interface",
    "function_com_id": 277,
    "function_vb_name": "GetAngle",
    "function_name": "get_angle",
    "function_parameters": (("point","array_of dbl","OPT"),("reference","array_of dbl","OPT"),("angle","dbl","OPT"),("message","str","OPT")),
    "function_returns": ("number","null")
    }
get_boolean = {
    "function_location": "user_interface",
    "function_com_id": 622,
    "function_vb_name": "GetBoolean",
    "function_name": "get_boolean",
    "function_parameters": (("message","str","REQ"),("items","array_of str","REQ"),("defaults","array_of bln","REQ")),
    "function_returns": ("array","null")
    }
get_box = {
    "function_location": "user_interface",
    "function_com_id": 342,
    "function_vb_name": "GetBox",
    "function_name": "get_box",
    "function_parameters": (("mode","int","OPT"),("point","array_of dbl","OPT"),("prompt_1","str","OPT"),("prompt_2","str","OPT"),("prompt_3","str","OPT")),
    "function_returns": ("array","null")
    }
get_color = {
    "function_location": "user_interface",
    "function_com_id": 65,
    "function_vb_name": "GetColor",
    "function_name": "get_color",
    "function_parameters": (("color","lng","OPT"),),
    "function_returns": ("number","null")
    }
get_distance = {
    "function_location": "user_interface",
    "function_com_id": 66,
    "function_vb_name": "GetDistance",
    "function_name": "get_distance",
    "function_parameters": (("point","array_of dbl","OPT"),("distance","dbl","OPT"),("message_1","str","OPT"),("message_2","str","OPT")),
    "function_returns": ("number","null")
    }
get_integer = {
    "function_location": "user_interface",
    "function_com_id": 64,
    "function_vb_name": "GetInteger",
    "function_name": "get_integer",
    "function_parameters": (("message","str","OPT"),("number","int","OPT"),("min","int","OPT"),("max","int","OPT")),
    "function_returns": ("number","null")
    }
get_layer = {
    "function_location": "user_interface",
    "function_com_id": 672,
    "function_vb_name": "GetLayer",
    "function_name": "get_layer",
    "function_parameters": (("title","str","OPT"),("layer","str","OPT"),("show_new_layer","bln","OPT"),("show_set_current","bln","OPT")),
    "function_returns": ("string","null")
    }
get_linetype = {
    "function_location": "user_interface",
    "function_com_id": 673,
    "function_vb_name": "GetLinetype",
    "function_name": "get_linetype",
    "function_parameters": (("linetype","str","OPT"),),
    "function_returns": ("string","null")
    }
get_point = {
    "function_location": "user_interface",
    "function_com_id": 61,
    "function_vb_name": "GetPoint",
    "function_name": "get_point",
    "function_parameters": (("message","str","OPT"),("point","arr","OPT"),("distance","dbl","OPT"),("plane","bln","OPT")),
    "function_returns": ("array","null")
    }
get_point_on_curve = {
    "function_location": "user_interface",
    "function_com_id": 147,
    "function_vb_name": "GetPointOnCurve",
    "function_name": "get_point_on_curve",
    "function_parameters": (("object","str","REQ"),("message","str","OPT")),
    "function_returns": ("array","null")
    }
get_point_on_line = {
    "function_location": "user_interface",
    "function_com_id": 798,
    "function_vb_name": "GetPointOnLine",
    "function_name": "get_point_on_line",
    "function_parameters": (("message","str","REQ"),("start","array_of dbl","REQ"),("end","array_of dbl","REQ"),("track","bln","OPT")),
    "function_returns": ("array","null")
    }
get_point_on_mesh = {
    "function_location": "user_interface",
    "function_com_id": 401,
    "function_vb_name": "GetPointOnMesh",
    "function_name": "get_point_on_mesh",
    "function_parameters": (("object","str","REQ"),("message","str","OPT")),
    "function_returns": ("array","null")
    }
get_point_on_plane = {
    "function_location": "user_interface",
    "function_com_id": 797,
    "function_vb_name": "GetPointOnPlane",
    "function_name": "get_point_on_plane",
    "function_parameters": (("message","str","OPT"),("plane","array_of dbl","OPT"),("point","array_of dbl","OPT")),
    "function_returns": ("array","null")
    }
get_point_on_surface = {
    "function_location": "user_interface",
    "function_com_id": 148,
    "function_vb_name": "GetPointOnSurface",
    "function_name": "get_point_on_surface",
    "function_parameters": (("object","str","REQ"),("message","str","OPT")),
    "function_returns": ("array","null")
    }
get_points = {
    "function_location": "user_interface",
    "function_com_id": 67,
    "function_vb_name": "GetPoints",
    "function_name": "get_points",
    "function_parameters": (("draw","bln","OPT"),("plane","bln","OPT"),("message_1","str","OPT"),("message_2","str","OPT"),("max_points","int","OPT"),("base_point","array_of dbl","OPT")),
    "function_returns": ("array","null")
    }
get_print_width = {
    "function_location": "user_interface",
    "function_com_id": 674,
    "function_vb_name": "GetPrintWidth",
    "function_name": "get_print_width",
    "function_parameters": (("print_width","dbl","OPT"),),
    "function_returns": ("number","null")
    }
get_real = {
    "function_location": "user_interface",
    "function_com_id": 63,
    "function_vb_name": "GetReal",
    "function_name": "get_real",
    "function_parameters": (("message","str","OPT"),("number","dbl","OPT"),("min","dbl","OPT"),("max","dbl","OPT")),
    "function_returns": ("number","null")
    }
get_rectangle = {
    "function_location": "user_interface",
    "function_com_id": 341,
    "function_vb_name": "GetRectangle",
    "function_name": "get_rectangle",
    "function_parameters": (("mode","int","OPT"),("point","array_of dbl","OPT"),("prompt_1","str","OPT"),("prompt_2","str","OPT"),("prompt_3","str","OPT")),
    "function_returns": ("array","null")
    }
get_string = {
    "function_location": "user_interface",
    "function_com_id": 62,
    "function_vb_name": "GetString",
    "function_name": "get_string",
    "function_parameters": (("message","str","OPT"),("string","str","OPT"),("strings","array_of str","OPT")),
    "function_returns": ("string","null")
    }
get_surface_iso_param_point = {
    "function_location": "user_interface",
    "function_com_id": 775,
    "function_vb_name": "GetSurfaceIsoParamPoint",
    "function_name": "get_surface_iso_param_point",
    "function_parameters": (("object","str","REQ"),("message","str","OPT")),
    "function_returns": ("array","null")
    }
html_box = {
    "function_location": "user_interface",
    "function_com_id": 276,
    "function_vb_name": "HtmlBox",
    "function_name": "html_box",
    "function_parameters": (("file_name","str","REQ"),("arguments","va","OPT"),("options","str","OPT"),("modal","bln","OPT")),
    "function_returns": ("boolean","null")
    }
integer_box = {
    "function_location": "user_interface",
    "function_com_id": 55,
    "function_vb_name": "IntegerBox",
    "function_name": "integer_box",
    "function_parameters": (("message","str","OPT"),("number","int","OPT"),("title","str","OPT")),
    "function_returns": ("number","null")
    }
list_box = {
    "function_location": "user_interface",
    "function_com_id": 56,
    "function_vb_name": "ListBox",
    "function_name": "list_box",
    "function_parameters": (("items","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "function_returns": ("string","null")
    }
message_beep = {
    "function_location": "user_interface",
    "function_com_id": 149,
    "function_vb_name": "MessageBeep",
    "function_name": "message_beep",
    "function_parameters": (("beep","int","OPT"),),
    "function_returns": ()
    }
message_box = {
    "function_location": "user_interface",
    "function_com_id": 150,
    "function_vb_name": "MessageBox",
    "function_name": "message_box",
    "function_parameters": (("message","str","REQ"),("buttons","int","OPT"),("title","str","OPT")),
    "function_returns": ("number",)
    }
multi_list_box = {
    "function_location": "user_interface",
    "function_com_id": 57,
    "function_vb_name": "MultiListBox",
    "function_name": "multi_list_box",
    "function_parameters": (("items","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "function_returns": ("array","null")
    }
open_file_name = {
    "function_location": "user_interface",
    "function_com_id": 151,
    "function_vb_name": "OpenFileName",
    "function_name": "open_file_name",
    "function_parameters": (("title","str","OPT"),("filter","str","OPT"),("folder","str","OPT"),("filename","str","OPT"),("extension","str","OPT")),
    "function_returns": ("string","null")
    }
open_file_names = {
    "function_location": "user_interface",
    "function_com_id": 821,
    "function_vb_name": "OpenFileNames",
    "function_name": "open_file_names",
    "function_parameters": (("title","str","OPT"),("filter","str","OPT"),("folder","str","OPT"),("filename","str","OPT"),("extension","str","OPT")),
    "function_returns": ("array","null")
    }
popup_menu = {
    "function_location": "user_interface",
    "function_com_id": 595,
    "function_vb_name": "PopupMenu",
    "function_name": "popup_menu",
    "function_parameters": (("items","array_of str","REQ"),("modes","array_of int","OPT"),("point","array_of dbl","OPT"),("view","str","OPT")),
    "function_returns": ("number","number","null")
    }
property_list_box = {
    "function_location": "user_interface",
    "function_com_id": 58,
    "function_vb_name": "PropertyListBox",
    "function_name": "property_list_box",
    "function_parameters": (("items","array_of str","REQ"),("values","array_of str","REQ"),("message","str","OPT"),("title","str","OPT")),
    "function_returns": ("array","null")
    }
real_box = {
    "function_location": "user_interface",
    "function_com_id": 59,
    "function_vb_name": "RealBox",
    "function_name": "real_box",
    "function_parameters": (("message","str","OPT"),("number","dbl","OPT"),("title","str","OPT")),
    "function_returns": ("number","null")
    }
save_file_name = {
    "function_location": "user_interface",
    "function_com_id": 152,
    "function_vb_name": "SaveFileName",
    "function_name": "save_file_name",
    "function_parameters": (("title","str","OPT"),("filter","str","OPT"),("folder","str","OPT"),("filename","str","OPT"),("extension","str","OPT")),
    "function_returns": ("string","null")
    }
string_box = {
    "function_location": "user_interface",
    "function_com_id": 60,
    "function_vb_name": "StringBox",
    "function_name": "string_box",
    "function_parameters": (("message","str","OPT"),("string","str","OPT"),("title","str","OPT")),
    "function_returns": ("string","null")
    }
