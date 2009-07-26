#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class.
#For method type, insert either METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

application = {
    "add_alias": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "add_alias",
        "method_parameters": (("alias","str"),("macro","str")),
        "method_returns": ("boolean","null")
    },
    "add_search_path": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "add_search_path",
        "method_parameters": (("folder","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "add_startup_script": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "add_startup_script",
        "method_parameters": (("script_file","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "alias_count": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "alias_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "alias_macro": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "alias_macro",
        "method_parameters": (("alias","str"),("macro","str")),
        "method_returns": ("string","string","null")
    },
    "alias_names": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "alias_names",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "appearance_color": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "appearance_color",
        "method_parameters": (("item","int"),("color","lng")),
        "method_returns": ("number","number","null")
    },
    "appearance_display": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "appearance_display",
        "method_parameters": (("item","int"),("show","bln")),
        "method_returns": ("number","number","null")
    },
    "autosave_file": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "autosave_file",
        "method_parameters": (("file","str")),
        "method_returns": ("string","string","null")
    },
    "autosave_interval": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "autosave_interval",
        "method_parameters": (("minutes","int")),
        "method_returns": ("number","number","null")
    },
    "build_date": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "build_date",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "clear_command_history": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "clear_command_history",
        "method_parameters": (),
        "method_returns": ()
    },
    "command": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "command",
        "method_parameters": (("command","str"),("echo","bln")),
        "method_returns": ("boolean","null")
    },
    "command_history": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "command_history",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "default_renderer": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "default_renderer",
        "method_parameters": (("renderer","str")),
        "method_returns": ("string","string","null")
    },
    "delete_alias": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "delete_alias",
        "method_parameters": (("alias","str")),
        "method_returns": ("boolean","null")
    },
    "delete_search_path": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "delete_search_path",
        "method_parameters": (("folder","str")),
        "method_returns": ("boolean","null")
    },
    "delete_startup_script": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "delete_startup_script",
        "method_parameters": (("script_file","str")),
        "method_returns": ("boolean","null")
    },
    "display_ole_alerts": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "display_ole_alerts",
        "method_parameters": (("display","bln")),
        "method_returns": ("null")
    },
    "edge_analysis_color": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "edge_analysis_color",
        "method_parameters": (("color","lng")),
        "method_returns": ("number","number","null")
    },
    "edge_analysis_mode": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "edge_analysis_mode",
        "method_parameters": (("mode","int")),
        "method_returns": ("number","number","null")
    },
    "enable_autosave": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "enable_autosave",
        "method_parameters": (("enable","bln")),
        "method_returns": ("boolean")
    },
    "enable_history_recording": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "enable_history_recording",
        "method_parameters": (("enable","bln")),
        "method_returns": ("boolean","boolean")
    },
    "exe_folder": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "exe_folder",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "exit": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "exit",
        "method_parameters": (),
        "method_returns": ()
    },
    "find_file": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "find_file",
        "method_parameters": (("filename","str")),
        "method_returns": ("string","null")
    },
    "get_plug_in_object": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "get_plug_in_object",
        "method_parameters": (("plug_in","str")),
        "method_returns": ("null")
    },
    "help": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "help",
        "method_parameters": (("topic","int")),
        "method_returns": ("boolean")
    },
    "in_command": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "in_command",
        "method_parameters": (("ignore_runners","bln")),
        "method_returns": ("number")
    },
    "install_folder": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "install_folder",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "is_alias": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "is_alias",
        "method_parameters": (("alias","str")),
        "method_returns": ("boolean","null")
    },
    "is_command": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "is_command",
        "method_parameters": (("command_name","str")),
        "method_returns": ("boolean","null")
    },
    "last_command_name": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "last_command_name",
        "method_parameters": (),
        "method_returns": ("string")
    },
    "last_command_result": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "last_command_result",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "last_loaded_script_file": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "last_loaded_script_file",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "locale_i_d": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "locale_i_d",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "ortho": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "ortho",
        "method_parameters": (("enable","bln")),
        "method_returns": ("boolean","boolean")
    },
    "osnap": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "osnap",
        "method_parameters": (("enable","bln")),
        "method_returns": ("boolean","boolean")
    },
    "osnap_dialog": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "osnap_dialog",
        "method_parameters": (("visible","bln")),
        "method_returns": ("boolean","boolean")
    },
    "osnap_mode": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "osnap_mode",
        "method_parameters": (("mode","int")),
        "method_returns": ("number","number","null")
    },
    "planar": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "planar",
        "method_parameters": (("enable","bln")),
        "method_returns": ("boolean","boolean")
    },
    "plug_ins": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "plug_ins",
        "method_parameters": (("types","int"),("status","int")),
        "method_returns": ("array","null")
    },
    "print_": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "print_",
        "method_parameters": (("message","str")),
        "method_returns": ()
    },
    "print_ex": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "print_ex",
        "method_parameters": (("message","str")),
        "method_returns": ()
    },
    "project_osnaps": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "project_osnaps",
        "method_parameters": (("enable","bln")),
        "method_returns": ("boolean","boolean")
    },
    "prompt": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "prompt",
        "method_parameters": (("prompt","str")),
        "method_returns": ()
    },
    "registry_key": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "registry_key",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "screen_size": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "screen_size",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "sdk_version": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "sdk_version",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "search_path_count": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "search_path_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "search_path_list": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "search_path_list",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "send_keystrokes": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "send_keystrokes",
        "method_parameters": (("keys","str"),("add_return","bln")),
        "method_returns": ()
    },
    "snap": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "snap",
        "method_parameters": (("enable","bln")),
        "method_returns": ("boolean","boolean")
    },
    "startup_script_count": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "startup_script_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "startup_script_list": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "startup_script_list",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "status_bar_distance": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_distance",
        "method_parameters": (("distance","dbl")),
        "method_returns": ()
    },
    "status_bar_message": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_message",
        "method_parameters": (("message","str")),
        "method_returns": ()
    },
    "status_bar_number": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_number",
        "method_parameters": (("number","dbl")),
        "method_returns": ()
    },
    "status_bar_point": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_point",
        "method_parameters": (("point","arr_of_dbl")),
        "method_returns": ()
    },
    "template_file": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "template_file",
        "method_parameters": (("filename","str")),
        "method_returns": ("string","string")
    },
    "template_folder": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "template_folder",
        "method_parameters": (("folder","str")),
        "method_returns": ("string","string")
    },
    "window_handle": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "window_handle",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "working_folder": {
        "method_class": "Application",
        "method_type": "METHOD",
        "method_name": "working_folder",
        "method_parameters": (("enable","bln")),
        "method_returns": ("string","string")
    },
}
block = {
    "block_container_count": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_container_count",
        "method_parameters": (("block","str")),
        "method_returns": ("number","null")
    },
    "block_containers": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_containers",
        "method_parameters": (("block","str")),
        "method_returns": ("array","null")
    },
    "block_count": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_count",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "block_description": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_description",
        "method_parameters": (("block","str"),("text","str")),
        "method_returns": ("string","string","null")
    },
    "block_instance_count": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_count",
        "method_parameters": (("block","str")),
        "method_returns": ("number","null")
    },
    "block_instance_insert_point": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_insert_point",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "block_instance_name": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_name",
        "method_parameters": (("object","str")),
        "method_returns": ("string","null")
    },
    "block_instance_xform": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_xform",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "block_instances": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_instances",
        "method_parameters": (("block","str")),
        "method_returns": ("array","null")
    },
    "block_names": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_names",
        "method_parameters": (("sort","bln")),
        "method_returns": ("array","null")
    },
    "block_object_count": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_object_count",
        "method_parameters": (("block","str")),
        "method_returns": ("number","null")
    },
    "block_objects": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_objects",
        "method_parameters": (("block","str")),
        "method_returns": ("array","null")
    },
    "block_path": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_path",
        "method_parameters": (("block","str")),
        "method_returns": ("string","null")
    },
    "block_u_r_l": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_u_r_l",
        "method_parameters": (("block","str"),("u_r_l","str")),
        "method_returns": ("string","string","null")
    },
    "block_u_r_l_tag": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "block_u_r_l_tag",
        "method_parameters": (("block","str"),("u_r_l","str")),
        "method_returns": ("string","string","null")
    },
    "delete_block": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "delete_block",
        "method_parameters": (("block","str")),
        "method_returns": ("boolean","null")
    },
    "explode_block_instance": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "explode_block_instance",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "insert_block": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "insert_block",
        "method_parameters": (("name","str"),("point","arr_of_dbl"),("scale","arr_of_int"),("angle","dbl"),("normal","arr_of_dbl"),("xform","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "is_block": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "is_block",
        "method_parameters": (("block","str")),
        "method_returns": ("boolean","null")
    },
    "is_block_embedded": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_embedded",
        "method_parameters": (("block","str")),
        "method_returns": ("boolean","null")
    },
    "is_block_in_use": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_in_use",
        "method_parameters": (("block","str"),("where","int")),
        "method_returns": ("boolean","null")
    },
    "is_block_instance": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_instance",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_block_reference": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_reference",
        "method_parameters": (("block","str")),
        "method_returns": ("boolean","null")
    },
    "rename_block": {
        "method_class": "Block",
        "method_type": "METHOD",
        "method_name": "rename_block",
        "method_parameters": (("old_block","str"),("new_block","str")),
        "method_returns": ("string","null")
    },
}
curve = {
    "add_arc": {
        "method_class": "Object.Curves.Arc",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_arc",
        "method_parameters": (("plane","arr_of_dbl"),("radius","dbl"),("angle","dbl")),
        "method_returns": ("Object.Curve.Arc","null")#ed
    },
    "add_arc3_pt": {
        "method_class": "Object.Curves.Arc",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_arc3_pt",
        "method_parameters": (("start","arr_of_dbl"),("end","arr_of_dbl"),("point","arr_of_dbl")),
        "method_returns": ("Object.Curve.Arc","null")#ed
    },
    "add_circle": {
        "method_class": "Object.Curves.Circle",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_circle",
        "method_parameters": (("plane","arr_of_dbl"),("radius","dbl")),
        "method_returns": ("Object.Curve.Circle","null")#ed
    },
    "add_circle3_pt": {
        "method_class": "Object.Curves.Circle",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_circle3_pt",
        "method_parameters": (("first","arr_of_dbl"),("second","arr_of_dbl"),("third","arr_of_dbl")),
        "method_returns": ("Object.Curve.Circle","null")#ed
    },
    "add_curve": {
        "method_class": "Object.Curves.Curve",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_curve",
        "method_parameters": (("points","arr_of_dbl"),("degree","int")),
        "method_returns": ("Object.Curves.Curve","null")#ed
    },
    "add_ellipse": {
        "method_class": "Object.Curves.Ellipse",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_ellipse",
        "method_parameters": (("plane","arr_of_dbl"),("x_radius","dbl"),("y_radius","dbl")),
        "method_returns": ("Object.Curves.Ellipse","null")#ed
    },
    "add_ellipse3_pt": {
        "method_class": "Object.Curves.Ellipse",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_ellipse3_pt",
        "method_parameters": (("center","arr_of_dbl"),("second","arr_of_dbl"),("third","arr_of_dbl")),
        "method_returns": ("Object.Curves.Ellipse","null")#ed
    },
    "add_fillet_curve": {#TODO:does this create an arc?
        "method_class": "Object.Curves.Curve",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_fillet_curve",
        "method_parameters": (("curve0","Object.Curves.Curve"),("curve1","Object.Curves.Curve"),("radius","dbl"),("point0","arr_of_dbl"),("point1","arr_of_dbl")),#ed
        "method_returns": ("Object.Curves.Curve","null")
    },
    "add_interp_crv_on_srf": {
        "method_class": "Object.Curves.Curve",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_interp_crv_on_srf",
        "method_parameters": (("object","Object.Surfaces.Surface"),("points","arr_of_dbl")),#ed
        "method_returns": ("Object.Curves.Curve","null")#ed
    },
    "add_interp_crv_on_srf_u_v": {
        "method_class": "Object.Curves.Curve",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_interp_crv_on_srf_u_v",
        "method_parameters": (("object","Object.Surfaces.Surface"),("points","arr_of_dbl")),#ed
        "method_returns": ("Object.Curves.Curve","null")#ed
    },
    "add_interp_curve": {
        "method_class": "Object.Curves.Curve",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_interp_curve",
        "method_parameters": (("points","arr_of_dbl"),("degree","int"),("knot_style","int"),("start_tan","arr_of_dbl"),("end_tan","arr_of_dbl")),
        "method_returns": ("Object.Curves.Curve","null")#ed
    },
    "add_interp_curve_ex": {
        "method_class": "Object.Curves.Curve",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_interp_curve_ex",
        "method_parameters": (("points","arr_of_dbl"),("degree","int"),("knot_style","int"),("sharp","bln"),("start_tangent","arr_of_dbl"),("end_tangent","arr_of_dbl")),
        "method_returns": ("Object.Curves.Curve","null")#ed
    },
    "add_line": {
        "method_class": "Object.Curves.Line",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_line",
        "method_parameters": (("start","arr_of_dbl"),("end","arr_of_dbl")),
        "method_returns": ("Object.Curves.Line","null")#ed
    },
    "add_nurbs_curve": {
        "method_class": "Object.Curves.NurbsCurve",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_nurbs_curve",
        "method_parameters": (("points","arr_of_dbl"),("knots","arr_of_int"),("degree","int"),("weights","arr_of_int")),
        "method_returns": ("Object.Curves.NurbsCurve","null")#ed
    },
    "add_polyline": {
        "method_class": "Object.Curves.Polyline",#ed
        "method_type": "CONSTRUCTOR",#ed
        "method_name": "add_polyline",
        "method_parameters": (("points","arr_of_dbl")),
        "method_returns": ("Object.Curves.Polyline","null")#ed
    },#this is where I got to
    "add_sub_crv": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "add_sub_crv",
        "method_parameters": (("object","str"),("param0","dbl"),("param1","dbl")),
        "method_returns": ("string","null")
    },
    "arc_angle": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_angle",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "arc_center_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_center_point",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("null")
    },
    "arc_mid_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_mid_point",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("null")
    },
    "arc_radius": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_radius",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "circle_center_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "circle_center_point",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "circle_circumference": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "circle_circumference",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "circle_radius": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "circle_radius",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "close_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "close_curve",
        "method_parameters": (("object","str"),("tolerance","dbl")),
        "method_returns": ("string","null")
    },
    "convert_curve_to_polyline": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "convert_curve_to_polyline",
        "method_parameters": (("object","str"),("angle_tolerance","dbl"),("tolerance","dbl"),("delete_input","bln")),
        "method_returns": ("string","null")
    },
    "curve_arc_length_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_arc_length_point",
        "method_parameters": (("object","str"),("length","dbl"),("from_start","bln")),
        "method_returns": ("array","null")
    },
    "curve_area": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_area",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("array","number","number","null")
    },
    "curve_area_centroid": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_area_centroid",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("array","null")
    },
    "curve_arrows": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_arrows",
        "method_parameters": (("object","str"),("style","int")),
        "method_returns": ("number","number","null")
    },
    "curve_boolean_difference": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_boolean_difference",
        "method_parameters": (("curve_a","str"),("curve_b","str")),
        "method_returns": ("array","null")
    },
    "curve_boolean_intersection": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_boolean_intersection",
        "method_parameters": (("curve_a","str"),("curve_b","str")),
        "method_returns": ("array","null")
    },
    "curve_boolean_union": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_boolean_union",
        "method_parameters": (("curves","arr_of_str")),
        "method_returns": ("array","null")
    },
    "curve_brep_intersect": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_brep_intersect",
        "method_parameters": (("curve","str"),("brep","str"),("tolerance","dbl")),
        "method_returns": ("array","null")
    },
    "curve_closest_object": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_closest_object",
        "method_parameters": (("curve","str"),("objects","arr_of_str")),
        "method_returns": ("array","string","array","array","null")
    },
    "curve_closest_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_closest_point",
        "method_parameters": (("object","str"),("point","arr_of_dbl"),("index","int")),
        "method_returns": ("number","null")
    },
    "curve_contour_points": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_contour_points",
        "method_parameters": (("object","str"),("start_point","arr_of_dbl"),("end_point","arr_of_dbl"),("interval","dbl")),
        "method_returns": ("array","null")
    },
    "curve_curvature": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_curvature",
        "method_parameters": (("object","str"),("parameter","dbl")),
        "method_returns": ("array","number","null")
    },
    "curve_curve_intersection": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_curve_intersection",
        "method_parameters": (("object1","str"),("object2","str"),("tolerance","dbl")),
        "method_returns": ("array","number","number","number","number","number","null")
    },
    "curve_degree": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_degree",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "curve_deviation": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_deviation",
        "method_parameters": (("curve_a","str"),("curve_b","str")),
        "method_returns": ("array","number","number","number","number","number","number","null")
    },
    "curve_dim": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_dim",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "curve_directions_match": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_directions_match",
        "method_parameters": (("curve1","str"),("curve2","str")),
        "method_returns": ("boolean","null")
    },
    "curve_discontinuity": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_discontinuity",
        "method_parameters": (("object","str"),("style","int")),
        "method_returns": ("array","null")
    },
    "curve_domain": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_domain",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "curve_edit_points": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_edit_points",
        "method_parameters": (("object","str"),("return_parameters","bln"),("index","int")),
        "method_returns": ("array","array","null")
    },
    "curve_end_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_end_point",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "curve_evaluate": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_evaluate",
        "method_parameters": (("object","str"),("parameter","dbl"),("derivative","int")),
        "method_returns": ("array","array","array","array","array","null")
    },
    "curve_fillet_points": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_fillet_points",
        "method_parameters": (("curve0","str"),("curve1","str"),("radius","dbl"),("base_point0","arr_of_dbl"),("base_point1","arr_of_dbl")),
        "method_returns": ("array","string","null")
    },
    "curve_frame": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_frame",
        "method_parameters": (("object","str"),("parameter","dbl")),
        "method_returns": ("array","null")
    },
    "curve_knot_count": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_knot_count",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "curve_knots": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_knots",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "curve_length": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_length",
        "method_parameters": (("object","str"),("index","int"),("sub_domain","arr_of_int")),
        "method_returns": ("number","null")
    },
    "curve_mid_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_mid_point",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "curve_normal": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_normal",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "curve_perp_frame": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_perp_frame",
        "method_parameters": (("object","str"),("parameter","dbl")),
        "method_returns": ("array","null")
    },
    "curve_plane": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_plane",
        "method_parameters": (("curve","str")),
        "method_returns": ("array","null")
    },
    "curve_point_count": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_point_count",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "curve_points": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_points",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "curve_radius": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_radius",
        "method_parameters": (("object","str"),("point","arr_of_dbl"),("index","int")),
        "method_returns": ("number","null")
    },
    "curve_seam": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_seam",
        "method_parameters": (("object","str"),("parameter","dbl")),
        "method_returns": ("boolean","null")
    },
    "curve_start_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_start_point",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "curve_surface_intersection": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_surface_intersection",
        "method_parameters": (("curve","str"),("surface","str"),("tolerance","dbl"),("angle_tolerance","dbl")),
        "method_returns": ("array","number","number","number","number","number","number","number","null")
    },
    "curve_tangent": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_tangent",
        "method_parameters": (("object","str"),("parameter","dbl"),("index","int")),
        "method_returns": ("array","null")
    },
    "curve_weights": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_weights",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "divide_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "divide_curve",
        "method_parameters": (("object","str"),("segments","lng"),("create","bln"),("points","bln")),
        "method_returns": ("array","array","null")
    },
    "divide_curve_equidistant": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "divide_curve_equidistant",
        "method_parameters": (("object","str"),("distance","dbl"),("create","bln"),("points","bln")),
        "method_returns": ("array","array","null")
    },
    "divide_curve_length": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "divide_curve_length",
        "method_parameters": (("object","str"),("length","dbl"),("create","bln"),("points","bln")),
        "method_returns": ("array","array","null")
    },
    "ellipse_center_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "ellipse_center_point",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "ellipse_quad_points": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "ellipse_quad_points",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "evaluate_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "evaluate_curve",
        "method_parameters": (("object","str"),("parameter","dbl"),("index","int")),
        "method_returns": ("array","null")
    },
    "explode_curves": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "explode_curves",
        "method_parameters": (("objects","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "extend_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "extend_curve",
        "method_parameters": (("object","str"),("type","int"),("side","int"),("objects","arr_of_str")),
        "method_returns": ("string","null")
    },
    "extend_curve_length": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "extend_curve_length",
        "method_parameters": (("object","str"),("type","int"),("side","int"),("length","dbl")),
        "method_returns": ("string","null")
    },
    "extend_curve_point": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "extend_curve_point",
        "method_parameters": (("object","str"),("side","int"),("point","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "fair_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "fair_curve",
        "method_parameters": (("object","str"),("tolerance","dbl")),
        "method_returns": ("boolean","null")
    },
    "fit_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "fit_curve",
        "method_parameters": (("object","str"),("degree","int"),("tolerance","dbl"),("angle_tolerance","dbl")),
        "method_returns": ("string","null")
    },
    "insert_curve_knot": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "insert_curve_knot",
        "method_parameters": (("object","str"),("parameter","dbl"),("symmetrical","bln")),
        "method_returns": ("boolean","null")
    },
    "is_arc": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_arc",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_circle": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_circle",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_curve_closable": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_closable",
        "method_parameters": (("object","str"),("tolerance","dbl")),
        "method_returns": ("boolean","null")
    },
    "is_curve_closed": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_closed",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_curve_in_plane": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_in_plane",
        "method_parameters": (("object","str"),("plane","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_curve_linear": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_linear",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_curve_periodic": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_periodic",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_curve_planar": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_planar",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_curve_rational": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_rational",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_ellipse": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_ellipse",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_line": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_line",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_point_on_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_point_on_curve",
        "method_parameters": (("object","str"),("point","arr_of_int"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_poly_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_poly_curve",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "is_polyline": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "is_polyline",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("boolean","null")
    },
    "join_curves": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "join_curves",
        "method_parameters": (("object","str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "line_fit_from_points": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "line_fit_from_points",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "make_curve_non_periodic": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "make_curve_non_periodic",
        "method_parameters": (("object","str"),("delete","bln")),
        "method_returns": ("string","string","null")
    },
    "make_curve_periodic": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "make_curve_periodic",
        "method_parameters": (("object","str"),("delete","bln")),
        "method_returns": ("string","string","null")
    },
    "mesh_polyline": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "mesh_polyline",
        "method_parameters": (("polyline","str")),
        "method_returns": ("string","null")
    },
    "offset_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "offset_curve",
        "method_parameters": (("object","str"),("direction","arr_of_dbl"),("distance","dbl"),("normal","arr_of_dbl"),("style","int")),
        "method_returns": ("array","null")
    },
    "offset_curve_on_surface": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "offset_curve_on_surface",
        "method_parameters": (("curve","str"),("surface","str"),("distance","dbl"),("parameter","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "planar_closed_curve_containment": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "planar_closed_curve_containment",
        "method_parameters": (("curve1","str"),("curve2","str"),("plane","arr_of_dbl"),("tolerance","dbl")),
        "method_returns": ("number","null")
    },
    "planar_curve_collision": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "planar_curve_collision",
        "method_parameters": (("curve1","str"),("curve2","str"),("plane","arr_of_dbl"),("tolerance","dbl")),
        "method_returns": ("null")
    },
    "point_in_planar_closed_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "point_in_planar_closed_curve",
        "method_parameters": (("point","arr_of_dbl"),("curve","str"),("plane","arr_of_dbl"),("tolerance","dbl")),
        "method_returns": ("number","null")
    },
    "poly_curve_count": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "poly_curve_count",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("number","null")
    },
    "polyline_vertices": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "polyline_vertices",
        "method_parameters": (("object","str"),("index","int")),
        "method_returns": ("array","null")
    },
    "project_curve_to_mesh": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "project_curve_to_mesh",
        "method_parameters": (("curves","arr_of_str"),("meshes","arr_of_str"),("direction","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "project_curve_to_surface": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "project_curve_to_surface",
        "method_parameters": (("curves","arr_of_str"),("surfaces","arr_of_str"),("direction","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "rebuild_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "rebuild_curve",
        "method_parameters": (("object","str"),("degree","int"),("point_count","int")),
        "method_returns": ("boolean","null")
    },
    "remove_curve_knot": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "remove_curve_knot",
        "method_parameters": (("object","str"),("parameter","dbl")),
        "method_returns": ("boolean","null")
    },
    "reverse_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "reverse_curve",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "simplify_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "simplify_curve",
        "method_parameters": (("object","str"),("flags","int")),
        "method_returns": ("boolean","null")
    },
    "split_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "split_curve",
        "method_parameters": (("object","str"),("parameters","arr_of_dbl"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "trim_curve": {
        "method_class": "Curve",
        "method_type": "METHOD",
        "method_name": "trim_curve",
        "method_parameters": (("object","str"),("interval","arr_of_int"),("delete","bln")),
        "method_returns": ("string","null")
    },
}
dimension = {
    "add_dim_style": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "add_dim_style",
        "method_parameters": (("dim_style","str")),
        "method_returns": ("string","null")
    },
    "add_leader": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "add_leader",
        "method_parameters": (("points","arr_of_dbl"),("view","str"),("text","str")),
        "method_returns": ("string","null")
    },
    "current_dim_style": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "current_dim_style",
        "method_parameters": (("dim_style","str")),
        "method_returns": ("string","string","null")
    },
    "delete_dim_style": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "delete_dim_style",
        "method_parameters": (("dim_style","str")),
        "method_returns": ("string","null")
    },
    "dim_scale": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_scale",
        "method_parameters": (("scale","dbl")),
        "method_returns": ("number","number","null")
    },
    "dim_style_angle_precision": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_angle_precision",
        "method_parameters": (("dim_style","str"),("precision","int")),
        "method_returns": ("number","number","null")
    },
    "dim_style_arrow_size": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_arrow_size",
        "method_parameters": (("dim_style","str"),("size","dbl")),
        "method_returns": ("number","number","null")
    },
    "dim_style_count": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "dim_style_extension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_extension",
        "method_parameters": (("dim_style","str"),("extension","dbl")),
        "method_returns": ("number","number","null")
    },
    "dim_style_font": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_font",
        "method_parameters": (("dim_style","str"),("font","str")),
        "method_returns": ("string","string","null")
    },
    "dim_style_leader_arrow_size": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_leader_arrow_size",
        "method_parameters": (("dim_style","str"),("size","dbl")),
        "method_returns": ("number","number","null")
    },
    "dim_style_linear_precision": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_linear_precision",
        "method_parameters": (("dim_style","str"),("precision","int")),
        "method_returns": ("number","number","null")
    },
    "dim_style_names": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_names",
        "method_parameters": (("sort","bln")),
        "method_returns": ("array","null")
    },
    "dim_style_number_format": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_number_format",
        "method_parameters": (("dim_style","str"),("format","int")),
        "method_returns": ("number","number","null")
    },
    "dim_style_offset": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_offset",
        "method_parameters": (("dim_style","str"),("offset","dbl")),
        "method_returns": ("number","number","null")
    },
    "dim_style_text_alignment": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_text_alignment",
        "method_parameters": (("dim_style","str"),("alignment","int")),
        "method_returns": ("number","number","null")
    },
    "dim_style_text_gap": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_text_gap",
        "method_parameters": (("dim_style","str"),("gap","dbl")),
        "method_returns": ("number","number","null")
    },
    "dim_style_text_height": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_text_height",
        "method_parameters": (("dim_style","str"),("height","dbl")),
        "method_returns": ("number","number","null")
    },
    "dimension_style": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_style",
        "method_parameters": (("object","str"),("style","str")),
        "method_returns": ("string","string","null")
    },
    "dimension_text": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_text",
        "method_parameters": (("object","str")),
        "method_returns": ("string","null")
    },
    "dimension_user_text": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_user_text",
        "method_parameters": (("object","str"),("user_text","str")),
        "method_returns": ("string","string","null")
    },
    "dimension_value": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_value",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "is_aligned_dimension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_aligned_dimension",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_angular_dimension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_angular_dimension",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_diameter_dimension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_diameter_dimension",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_dim_style": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_dim_style",
        "method_parameters": (("dim_style","str")),
        "method_returns": ("null")
    },
    "is_dim_style_reference": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_dim_style_reference",
        "method_parameters": (("dim_style","str")),
        "method_returns": ("null")
    },
    "is_dimension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_dimension",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_leader": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_leader",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_linear_dimension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_linear_dimension",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_ordinate_dimension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_ordinate_dimension",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_radial_dimension": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_radial_dimension",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "leader_text": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "leader_text",
        "method_parameters": (("object","str"),("text","str")),
        "method_returns": ("string","string","null")
    },
    "rename_dim_style": {
        "method_class": "Dimension",
        "method_type": "METHOD",
        "method_name": "rename_dim_style",
        "method_parameters": (("old_style","str"),("new_style","str")),
        "method_returns": ("string","null")
    },
}
document = {
    "create_preview_image": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "create_preview_image",
        "method_parameters": (("file","str"),("view","str"),("size","arr_of_int"),("flags","int"),("wireframe","bln")),
        "method_returns": ("boolean")
    },
    "document_modified": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "document_modified",
        "method_parameters": (("modified","bln")),
        "method_returns": ("boolean","boolean")
    },
    "document_name": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "document_name",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "document_path": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "document_path",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "document_u_r_l": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "document_u_r_l",
        "method_parameters": (("u_r_l","str")),
        "method_returns": ("string","string","null")
    },
    "enable_redraw": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "enable_redraw",
        "method_parameters": (("select","bln")),
        "method_returns": ("boolean")
    },
    "extract_preview_image": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "extract_preview_image",
        "method_parameters": (("file_name","str"),("model_name","str")),
        "method_returns": ("boolean")
    },
    "is_document_modified": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "is_document_modified",
        "method_parameters": (),
        "method_returns": ("boolean")
    },
    "notes": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "notes",
        "method_parameters": (("notes","str")),
        "method_returns": ("string","string","null")
    },
    "read_file_version": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "read_file_version",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "redraw": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "redraw",
        "method_parameters": (),
        "method_returns": ()
    },
    "render_antialias": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_antialias",
        "method_parameters": (("style","int")),
        "method_returns": ("number","number","number")
    },
    "render_color": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_color",
        "method_parameters": (("item","int"),("color","lng")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_density": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_density",
        "method_parameters": (("density","dbl")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_angle": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_angle",
        "method_parameters": (("angle","dbl")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_aspect_ratio": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_aspect_ratio",
        "method_parameters": (("ratio","dbl")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_dist_edge_to_srf": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_dist_edge_to_srf",
        "method_parameters": (("distance","dbl")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_edge_length": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_edge_length",
        "method_parameters": (("length","dbl")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_min_edge_length": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_min_edge_length",
        "method_parameters": (("length","dbl")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_min_initial_grid_quads": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_min_initial_grid_quads",
        "method_parameters": (("quads","int")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_quality": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_quality",
        "method_parameters": (("quality","int")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_settings": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_settings",
        "method_parameters": (("settings","int")),
        "method_returns": ("number","number","null")
    },
    "render_resolution": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_resolution",
        "method_parameters": (("resolution","arr_of_int")),
        "method_returns": ("array","array","null")
    },
    "render_settings": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "render_settings",
        "method_parameters": (("settings","int")),
        "method_returns": ("number","number","number")
    },
    "unit_absolute_tolerance": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_absolute_tolerance",
        "method_parameters": (("abs_tol","dbl")),
        "method_returns": ("number","number","null")
    },
    "unit_angle_tolerance": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_angle_tolerance",
        "method_parameters": (("angle_tol","dbl")),
        "method_returns": ("number","number","null")
    },
    "unit_custom_unit_system": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_custom_unit_system",
        "method_parameters": (("units","dbl"),("scale","bln"),("name","str")),
        "method_returns": ("number","null")
    },
    "unit_distance_display_mode": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_distance_display_mode",
        "method_parameters": (("mode","int")),
        "method_returns": ("number","number","null")
    },
    "unit_distance_display_precision": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_distance_display_precision",
        "method_parameters": (("precision","int")),
        "method_returns": ("number","number","null")
    },
    "unit_relative_tolerance": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_relative_tolerance",
        "method_parameters": (("rel_tol","dbl")),
        "method_returns": ("number","number","null")
    },
    "unit_scale": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_scale",
        "method_parameters": (("to_system","int"),("from_system","int")),
        "method_returns": ("number","null")
    },
    "unit_system": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_system",
        "method_parameters": (("system","int"),("scale","bln")),
        "method_returns": ("number","null")
    },
    "unit_system_name": {
        "method_class": "Document",
        "method_type": "METHOD",
        "method_name": "unit_system_name",
        "method_parameters": (("capitalize","bln"),("singular","bln"),("abbreviate","bln")),
        "method_returns": ("string")
    },
}
geometry = {
    "add_clipping_plane": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_clipping_plane",
        "method_parameters": (("plane","arr_of_dbl"),("d_u","dbl"),("d_v","dbl"),("views","arr_of_str")),
        "method_returns": ("string","null")
    },
    "add_point_cloud": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_point_cloud",
        "method_parameters": (("points","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_points": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_points",
        "method_parameters": (("points","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "add_text": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_text",
        "method_parameters": (("text","str"),("point","arr_of_dbl"),("plane","arr_of_dbl"),("height","dbl"),("font","str"),("style","int")),
        "method_returns": ("string","null")
    },
    "add_text_dot": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_text_dot",
        "method_parameters": (("test","str"),("point","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "bounding_box": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "bounding_box",
        "method_parameters": (("objects","arr_of_str"),("view","str"),("world_coords","bln")),
        "method_returns": ("array","null")
    },
    "compare_geometry": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "compare_geometry",
        "method_parameters": (("object1","str"),("object2","str")),
        "method_returns": ("boolean","null")
    },
    "is_clipping_plane": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_clipping_plane",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_point": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_point",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_point_cloud": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_point_cloud",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_text": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_text",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_text_dot": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_text_dot",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "point_cloud_count": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "point_cloud_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "point_cloud_points": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "point_cloud_points",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "point_coordinates": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "point_coordinates",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "text_dot_point": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_dot_point",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "text_dot_text": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_dot_text",
        "method_parameters": (("object","str"),("text","str")),
        "method_returns": ("string","string","null")
    },
    "text_object_font": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_font",
        "method_parameters": (("object","str"),("font","str")),
        "method_returns": ("string","string","null")
    },
    "text_object_height": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_height",
        "method_parameters": (("object","str"),("height","dbl")),
        "method_returns": ("string","string","null")
    },
    "text_object_plane": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_plane",
        "method_parameters": (("object","str"),("plane","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "text_object_point": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_point",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("string","string","null")
    },
    "text_object_style": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_style",
        "method_parameters": (("object","str"),("style","int")),
        "method_returns": ("number","number","null")
    },
    "text_object_text": {
        "method_class": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_text",
        "method_parameters": (("object","str"),("text","str")),
        "method_returns": ("string","string","null")
    },
}
group = {
    "add_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "add_group",
        "method_parameters": (("group","str")),
        "method_returns": ("string","null")
    },
    "add_object_to_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "add_object_to_group",
        "method_parameters": (("object","str"),("group","str")),
        "method_returns": ("boolean","null")
    },
    "add_objects_to_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "add_objects_to_group",
        "method_parameters": (("objects","arr_of_str"),("group","str")),
        "method_returns": ("number","null")
    },
    "delete_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "delete_group",
        "method_parameters": (("group","str")),
        "method_returns": ("boolean","null")
    },
    "group_count": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "group_count",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "group_names": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "group_names",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "hide_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "hide_group",
        "method_parameters": (("group","str")),
        "method_returns": ("number","null")
    },
    "is_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "is_group",
        "method_parameters": (("group","str")),
        "method_returns": ("boolean","null")
    },
    "is_group_empty": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "is_group_empty",
        "method_parameters": (("group","str")),
        "method_returns": ("boolean","null")
    },
    "lock_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "lock_group",
        "method_parameters": (("group","str")),
        "method_returns": ("number","null")
    },
    "remove_object_from_all_groups": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "remove_object_from_all_groups",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "remove_object_from_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "remove_object_from_group",
        "method_parameters": (("object","str"),("group","str")),
        "method_returns": ("boolean","null")
    },
    "remove_object_from_top_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "remove_object_from_top_group",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "remove_objects_from_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "remove_objects_from_group",
        "method_parameters": (("objects","arr_of_str"),("group","str")),
        "method_returns": ("number","null")
    },
    "rename_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "rename_group",
        "method_parameters": (("old_group","str"),("new_group","str")),
        "method_returns": ("string","null")
    },
    "show_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "show_group",
        "method_parameters": (("group","str")),
        "method_returns": ("number","null")
    },
    "unlock_group": {
        "method_class": "Group",
        "method_type": "METHOD",
        "method_name": "unlock_group",
        "method_parameters": (("group","str")),
        "method_returns": ("number","null")
    },
}
hatch = {
    "add_hatch": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "add_hatch",
        "method_parameters": (("curve","str"),("hatch","str"),("scale","dbl"),("rotation","dbl")),
        "method_returns": ("string","null")
    },
    "add_hatch_patterns": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "add_hatch_patterns",
        "method_parameters": (("file_name","str"),("replace","bln")),
        "method_returns": ("array","null")
    },
    "add_hatches": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "add_hatches",
        "method_parameters": (("curves","arr_of_str"),("hatch","str"),("scale","dbl"),("rotation","dbl")),
        "method_returns": ("array","null")
    },
    "current_hatch_pattern": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "current_hatch_pattern",
        "method_parameters": (("hatch","str")),
        "method_returns": ("string","string","null")
    },
    "explode_hatch": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "explode_hatch",
        "method_parameters": (("hatch","str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "hatch_pattern": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern",
        "method_parameters": (("object","str"),("hatch","str")),
        "method_returns": ("string","string","null")
    },
    "hatch_pattern_count": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "hatch_pattern_description": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_description",
        "method_parameters": (("hatch","str")),
        "method_returns": ("string","null")
    },
    "hatch_pattern_fill_type": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_fill_type",
        "method_parameters": (("hatch","str")),
        "method_returns": ("number","null")
    },
    "hatch_pattern_names": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_names",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "hatch_rotation": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_rotation",
        "method_parameters": (("object","str"),("rotation","dbl")),
        "method_returns": ("number","number","null")
    },
    "hatch_scale": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_scale",
        "method_parameters": (("object","str"),("scale","dbl")),
        "method_returns": ("number","number","null")
    },
    "is_hatch": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_hatch_pattern": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch_pattern",
        "method_parameters": (("hatch","str")),
        "method_returns": ("null")
    },
    "is_hatch_pattern_current": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch_pattern_current",
        "method_parameters": (("hatch","str")),
        "method_returns": ("null")
    },
    "is_hatch_pattern_reference": {
        "method_class": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch_pattern_reference",
        "method_parameters": (("hatch","str")),
        "method_returns": ("null")
    },
}
layer = {
    "add_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "add_layer",
        "method_parameters": (("layer","str"),("color","lng"),("visible","bln"),("locked","bln"),("parent","str")),
        "method_returns": ("string","null")
    },
    "current_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "current_layer",
        "method_parameters": (("layer","str")),
        "method_returns": ("string","string","null")
    },
    "delete_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "delete_layer",
        "method_parameters": (("layer","str")),
        "method_returns": ("boolean","null")
    },
    "expand_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "expand_layer",
        "method_parameters": (("layer","str"),("expand","bln")),
        "method_returns": ("boolean","null")
    },
    "is_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_changeable": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_changeable",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_child_of": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_child_of",
        "method_parameters": (("layer","str"),("test","str")),
        "method_returns": ("boolean","null")
    },
    "is_layer_current": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_current",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_empty": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_empty",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_expanded": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_expanded",
        "method_parameters": (("layer","str")),
        "method_returns": ("boolean","null")
    },
    "is_layer_locked": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_locked",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_on": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_on",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_parent_of": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_parent_of",
        "method_parameters": (("layer","str"),("test","str")),
        "method_returns": ("boolean","null")
    },
    "is_layer_reference": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_reference",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_selectable": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_selectable",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "is_layer_visible": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_visible",
        "method_parameters": (("layer","str")),
        "method_returns": ("null")
    },
    "layer_child_count": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_child_count",
        "method_parameters": (("layer","str")),
        "method_returns": ("number","null")
    },
    "layer_children": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_children",
        "method_parameters": (("layer","str")),
        "method_returns": ("array","null")
    },
    "layer_color": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_color",
        "method_parameters": (("layer","str"),("color","lng")),
        "method_returns": ("number","number","null")
    },
    "layer_count": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "layer_linetype": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_linetype",
        "method_parameters": (("layer","str"),("linetype","str")),
        "method_returns": ("string","string","null")
    },
    "layer_locked": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_locked",
        "method_parameters": (("layer","str"),("visible","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "layer_material_index": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_material_index",
        "method_parameters": (("layer","str")),
        "method_returns": ("number","null")
    },
    "layer_mode": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_mode",
        "method_parameters": (("layer","str"),("mode","int")),
        "method_returns": ("number","number","null")
    },
    "layer_names": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_names",
        "method_parameters": (("sort","bln")),
        "method_returns": ("array","null")
    },
    "layer_order": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_order",
        "method_parameters": (("layer","str")),
        "method_returns": ("number","null")
    },
    "layer_print_color": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_print_color",
        "method_parameters": (("layer","str"),("color","lng")),
        "method_returns": ("number","number","null")
    },
    "layer_print_width": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_print_width",
        "method_parameters": (("layer","str"),("width","dbl")),
        "method_returns": ("number","number","null")
    },
    "layer_visible": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_visible",
        "method_parameters": (("layer","str"),("visible","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "parent_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "parent_layer",
        "method_parameters": (("layer","str"),("parent","str")),
        "method_returns": ("string","string","null")
    },
    "purge_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "purge_layer",
        "method_parameters": (("layer","str")),
        "method_returns": ("string","null")
    },
    "rename_layer": {
        "method_class": "Layer",
        "method_type": "METHOD",
        "method_name": "rename_layer",
        "method_parameters": (("old_name","str"),("new_name","str")),
        "method_returns": ("string","null")
    },
}
light = {
    "add_directional_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "add_directional_light",
        "method_parameters": (("start_point","arr_of_dbl"),("end_point","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_linear_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "add_linear_light",
        "method_parameters": (("start_point","arr_of_dbl"),("end_point","arr_of_dbl"),("width","dbl")),
        "method_returns": ("string","null")
    },
    "add_point_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "add_point_light",
        "method_parameters": (("point","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_rectangular_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "add_rectangular_light",
        "method_parameters": (("origin","arr_of_dbl"),("width","arr_of_dbl"),("height","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_spot_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "add_spot_light",
        "method_parameters": (("origin","arr_of_dbl"),("radius","dbl"),("apex","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "enable_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "enable_light",
        "method_parameters": (("object","str"),("enable","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "is_directional_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_directional_light",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_light",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_light_enabled": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_light_enabled",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_light_reference": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_light_reference",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_linear_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_linear_light",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_point_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_point_light",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_rectangular_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_rectangular_light",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_spot_light": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "is_spot_light",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "light_color": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "light_color",
        "method_parameters": (("object","str"),("color","lng")),
        "method_returns": ("number","number","null")
    },
    "light_count": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "light_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "light_direction": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "light_direction",
        "method_parameters": (("object","str"),("direction","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "light_location": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "light_location",
        "method_parameters": (("object","str"),("location","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "light_name": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "light_name",
        "method_parameters": (("object","str"),("name","str")),
        "method_returns": ("string","string","null")
    },
    "light_objects": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "light_objects",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "rectangular_light_plane": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "rectangular_light_plane",
        "method_parameters": (("object","str")),
        "method_returns": ("array","array","array","array","array","null")
    },
    "spot_light_hardness": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "spot_light_hardness",
        "method_parameters": (("object","str"),("hardness","dbl")),
        "method_returns": ("number","number","null")
    },
    "spot_light_radius": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "spot_light_radius",
        "method_parameters": (("object","str"),("radius","dbl")),
        "method_returns": ("number","number","null")
    },
    "spot_light_shadow_intensity": {
        "method_class": "Light",
        "method_type": "METHOD",
        "method_name": "spot_light_shadow_intensity",
        "method_parameters": (("object","str"),("intensity","dbl")),
        "method_returns": ("number","number","null")
    },
}
line_and_plane = {
    "distance_to_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "distance_to_plane",
        "method_parameters": (("plane","arr_of_dbl"),("point","arr_of_dbl")),
        "method_returns": ("number","null")
    },
    "evaluate_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "evaluate_plane",
        "method_parameters": (("plane","arr_of_dbl"),("parameter","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "intersect_planes": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "intersect_planes",
        "method_parameters": (("plane1","arr_of_dbl"),("plane2","arr_of_dbl"),("plane3","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "line_closest_point": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_closest_point",
        "method_parameters": (("line","arr_of_dbl"),("point","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "line_is_farther_than": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_is_farther_than",
        "method_parameters": (("line","arr_of_dbl"),("distance","dbl"),("point","arr_of_dbl"),("line2","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "line_line_intersection": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_line_intersection",
        "method_parameters": (("line_a","arr_of_dbl"),("line_b","arr_of_dbl"),("planar","bln")),
        "method_returns": ("array","array","null")
    },
    "line_max_distance_to": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_max_distance_to",
        "method_parameters": (("line","arr_of_dbl"),("point","arr_of_dbl"),("line2","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "line_min_distance_to": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_min_distance_to",
        "method_parameters": (("line","arr_of_dbl"),("point","arr_of_dbl"),("line2","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "line_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_plane",
        "method_parameters": (("line","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "line_plane_intersection": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_plane_intersection",
        "method_parameters": (("line","arr_of_dbl"),("point","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "line_transform": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_transform",
        "method_parameters": (("line","arr_of_dbl"),("xform","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "move_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "move_plane",
        "method_parameters": (("plane","arr_of_dbl"),("origin","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "plane_closest_point": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_closest_point",
        "method_parameters": (("plane","arr_of_dbl"),("point","arr_of_dbl"),("return_point","bln")),
        "method_returns": ("array","null")
    },
    "plane_equation": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_equation",
        "method_parameters": (("plane","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "plane_fit_from_points": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_fit_from_points",
        "method_parameters": (("points","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "plane_from_frame": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_from_frame",
        "method_parameters": (("origin","arr_of_dbl"),("xaxis","arr_of_dbl"),("yaxis","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "plane_from_normal": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_from_normal",
        "method_parameters": (("origin","arr_of_dbl"),("normal","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "plane_from_points": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_from_points",
        "method_parameters": (("origin","arr_of_dbl"),("point_x","arr_of_dbl"),("point_y","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "plane_plane_intersection": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_plane_intersection",
        "method_parameters": (("plane1","arr_of_dbl"),("point2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "plane_transform": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_transform",
        "method_parameters": (("plane","arr_of_dbl"),("xform","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "rotate_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "rotate_plane",
        "method_parameters": (("plane","arr_of_dbl"),("angle","dbl"),("axis","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "world_x_y_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "world_x_y_plane",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "world_y_z_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "world_y_z_plane",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "world_z_x_plane": {
        "method_class": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "world_z_x_plane",
        "method_parameters": (),
        "method_returns": ("array")
    },
}
linetype = {
    "is_linetype": {
        "method_class": "Linetype",
        "method_type": "METHOD",
        "method_name": "is_linetype",
        "method_parameters": (("linetype","str")),
        "method_returns": ("boolean","null")
    },
    "is_linetype_reference": {
        "method_class": "Linetype",
        "method_type": "METHOD",
        "method_name": "is_linetype_reference",
        "method_parameters": (("linetype","str")),
        "method_returns": ("boolean","null")
    },
    "linetype_count": {
        "method_class": "Linetype",
        "method_type": "METHOD",
        "method_name": "linetype_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "linetype_names": {
        "method_class": "Linetype",
        "method_type": "METHOD",
        "method_name": "linetype_names",
        "method_parameters": (("sort","bln")),
        "method_returns": ("array","null")
    },
}
material = {
    "add_material_to_layer": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "add_material_to_layer",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "add_material_to_object": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "add_material_to_object",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "copy_material": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "copy_material",
        "method_parameters": (("src_index","int"),("dst_index","int")),
        "method_returns": ("boolean","null")
    },
    "is_material_default": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "is_material_default",
        "method_parameters": (("material_index","int")),
        "method_returns": ("null")
    },
    "is_material_reference": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "is_material_reference",
        "method_parameters": (("material_index","int")),
        "method_returns": ("boolean","null")
    },
    "match_material": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "match_material",
        "method_parameters": (("src_material_index","int"),("src_object","str"),("dest_objects","arr_of_str")),
        "method_returns": ("number","null")
    },
    "material_bump": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_bump",
        "method_parameters": (("material_index","int"),("file_name","str")),
        "method_returns": ("string","string","null")
    },
    "material_color": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_color",
        "method_parameters": (("material_index","int"),("color","lng")),
        "method_returns": ("number","number","null")
    },
    "material_environment_map": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_environment_map",
        "method_parameters": (("material_index","int"),("file_name","str")),
        "method_returns": ("string","string","null")
    },
    "material_name": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_name",
        "method_parameters": (("material_index","int"),("name","str")),
        "method_returns": ("string","string","null")
    },
    "material_reflective_color": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_reflective_color",
        "method_parameters": (("material_index","int"),("color","lng")),
        "method_returns": ("number","number","null")
    },
    "material_shine": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_shine",
        "method_parameters": (("material_index","int"),("shine","dbl")),
        "method_returns": ("number","number","null")
    },
    "material_texture": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_texture",
        "method_parameters": (("material_index","int"),("file_name","str")),
        "method_returns": ("string","string","null")
    },
    "material_transparency": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_transparency",
        "method_parameters": (("material_index","int"),("transparency","dbl")),
        "method_returns": ("number","number","null")
    },
    "material_transparency_map": {
        "method_class": "Material",
        "method_type": "METHOD",
        "method_name": "material_transparency_map",
        "method_parameters": (("material_index","int"),("file_name","str")),
        "method_returns": ("string","string","null")
    },
}
math = {
    "angle": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "angle",
        "method_parameters": (("point1","arr_of_dbl"),("point2","arr_of_dbl"),("world","bln")),
        "method_returns": ("array","null")
    },
    "angle2": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "angle2",
        "method_parameters": (("point1","arr_of_dbl"),("point2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "deviation": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "deviation",
        "method_parameters": (("numbers","arr_of_int")),
        "method_returns": ("number","null")
    },
    "distance": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "distance",
        "method_parameters": (("point1","arr_of_dbl"),("point2","arr_of_dbl"),("point_array","arr_of_dbl")),
        "method_returns": ("number","array","null")
    },
    "hypot": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "hypot",
        "method_parameters": (("number_x","dbl"),("number_y","dbl")),
        "method_returns": ("number","null")
    },
    "max": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "max",
        "method_parameters": (("numbers","arr_of_int")),
        "method_returns": ("number","null")
    },
    "mean": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "mean",
        "method_parameters": (("numbers","arr_of_int")),
        "method_returns": ("number","null")
    },
    "median": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "median",
        "method_parameters": (("numbers","arr_of_int")),
        "method_returns": ("number","null")
    },
    "min": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "min",
        "method_parameters": (("numbers","arr_of_int")),
        "method_returns": ("number","null")
    },
    "polar": {
        "method_class": "Math",
        "method_type": "METHOD",
        "method_name": "polar",
        "method_parameters": (("point","arr_of_dbl"),("angle","dbl"),("distance","dbl"),("plane","arr_of_dbl")),
        "method_returns": ("array","null")
    },
}
mesh = {
    "add_mesh": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "add_mesh",
        "method_parameters": (("vertices","arr_of_dbl"),("face_vertices","arr_of_int"),("vertex_normals","arr_of_dbl"),("texture_coordinates","arr_of_dbl"),("vertex_colors","arr_of_int")),
        "method_returns": ("string","null")
    },
    "add_planar_mesh": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "add_planar_mesh",
        "method_parameters": (("object","str"),("delete","bln")),
        "method_returns": ("string","null")
    },
    "curve_mesh_intersection": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "curve_mesh_intersection",
        "method_parameters": (("curve","str"),("mesh","str"),("return_faces","bln")),
        "method_returns": ("array","array","array","number","null")
    },
    "disjoint_mesh_count": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "disjoint_mesh_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "duplicate_mesh_border": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "duplicate_mesh_border",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "explode_meshes": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "explode_meshes",
        "method_parameters": (("objects","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "is_mesh": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "is_mesh",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_mesh_closed": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "is_mesh_closed",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_mesh_manifold": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "is_mesh_manifold",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "mesh_area": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_area",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("array","number","number","number","null")
    },
    "mesh_area_centroid": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_area_centroid",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_difference": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_difference",
        "method_parameters": (("input0","arr_of_str"),("input1","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_intersection": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_intersection",
        "method_parameters": (("input0","arr_of_str"),("input1","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_split": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_split",
        "method_parameters": (("input0","arr_of_str"),("input1","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_union": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_union",
        "method_parameters": (("input","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "mesh_closest_point": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_closest_point",
        "method_parameters": (("object","str"),("point","arr_of_dbl"),("tolerance","dbl")),
        "method_returns": ("array","array","number","null")
    },
    "mesh_contour_points": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_contour_points",
        "method_parameters": (("object","str"),("start_point","arr_of_dbl"),("end_point","arr_of_dbl"),("interval","dbl"),("remove_coincident_points","bln")),
        "method_returns": ("array","null")
    },
    "mesh_face_centers": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_centers",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_face_count": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "mesh_face_normals": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_normals",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_face_vertices": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_vertices",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_faces": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_faces",
        "method_parameters": (("object","str"),("face_type","bln")),
        "method_returns": ("array","null")
    },
    "mesh_has_face_normals": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_face_normals",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "mesh_has_texture_coordinates": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_texture_coordinates",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "mesh_has_vertex_colors": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_vertex_colors",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "mesh_has_vertex_normals": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_vertex_normals",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "mesh_mesh_intersection": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_mesh_intersection",
        "method_parameters": (("mesh1","str"),("mesh2","str"),("tolerance","dbl")),
        "method_returns": ("array","null")
    },
    "mesh_naked_edge_points": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_naked_edge_points",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_offset": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_offset",
        "method_parameters": (("mesh","str"),("distance","dbl")),
        "method_returns": ("string","null")
    },
    "mesh_quad_count": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_quad_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "mesh_quads_to_triangles": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_quads_to_triangles",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "mesh_texture_coordinates": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_texture_coordinates",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_triangle_count": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_triangle_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "mesh_vertex_colors": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertex_colors",
        "method_parameters": (("object","str"),("vertex_colors","arr_of_int")),
        "method_returns": ("array","array","null")
    },
    "mesh_vertex_count": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertex_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "mesh_vertex_normals": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertex_normals",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_vertices": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertices",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "mesh_volume": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_volume",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("array","number","number","number","null")
    },
    "mesh_volume_centroid": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_volume_centroid",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "pull_curve_to_mesh": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "pull_curve_to_mesh",
        "method_parameters": (("mesh","str"),("curve","str")),
        "method_returns": ("string","null")
    },
    "split_disjoint_mesh": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "split_disjoint_mesh",
        "method_parameters": (("object","str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "unify_mesh_normals": {
        "method_class": "Mesh",
        "method_type": "METHOD",
        "method_name": "unify_mesh_normals",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
}
object = {
    "add_object_mesh": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "add_object_mesh",
        "method_parameters": (("object","str"),("quality","int"),("enable","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "box_morph_object": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "box_morph_object",
        "method_parameters": (("objects","arr_of_str"),("box_points","arr_of_dbl"),("copy","bln")),
        "method_returns": ("string","array","null")
    },
    "copy_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "copy_objects",
        "method_parameters": (("objects","arr_of_str"),("start","arr_of_dbl"),("end","arr_of_dbl"),("translation","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "delete_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "delete_objects",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("number","null")
    },
    "enable_object_mesh": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "enable_object_mesh",
        "method_parameters": (("objects","arr_of_str"),("enable","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "flash_object": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "flash_object",
        "method_parameters": (("objects","arr_of_str"),("style","bln")),
        "method_returns": ()
    },
    "hide_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "hide_objects",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("number","null")
    },
    "is_layout_object": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_layout_object",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object",
        "method_parameters": (("object","str")),
        "method_returns": ()
    },
    "is_object_hidden": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_hidden",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object_in_box": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_in_box",
        "method_parameters": (("object","str"),("box","arr_of_dbl"),("mode","bln")),
        "method_returns": ("null")
    },
    "is_object_in_group": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_in_group",
        "method_parameters": (("object","str"),("group","str")),
        "method_returns": ("null")
    },
    "is_object_locked": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_locked",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object_normal": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_normal",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object_reference": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_reference",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object_selectable": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_selectable",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object_selected": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_selected",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object_solid": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_solid",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_object_valid": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_valid",
        "method_parameters": (("object","str")),
        "method_returns": ("null")
    },
    "is_visible_in_view": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "is_visible_in_view",
        "method_parameters": (("object","str"),("view","str")),
        "method_returns": ("null")
    },
    "lock_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "lock_objects",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("number","null")
    },
    "match_object_attributes": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "match_object_attributes",
        "method_parameters": (("targets","arr_of_str"),("source","str")),
        "method_returns": ("number","null")
    },
    "mirror_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "mirror_objects",
        "method_parameters": (("objects","arr_of_str"),("start_pt","arr_of_dbl"),("end_pt","arr_of_dbl"),("copy","bln")),
        "method_returns": ("string","null")
    },
    "move_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "move_objects",
        "method_parameters": (("objects","arr_of_str"),("start","arr_of_dbl"),("end","arr_of_dbl"),("translation","arr_of_dbl")),
        "method_returns": ("number","null")
    },
    "object_color": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_color",
        "method_parameters": (("objects","arr_of_str"),("color","lng")),
        "method_returns": ("number","number","number","null")
    },
    "object_color_source": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_color_source",
        "method_parameters": (("objects","arr_of_str"),("source","int")),
        "method_returns": ("number","number","number","null")
    },
    "object_description": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_description",
        "method_parameters": (("object","str")),
        "method_returns": ("string","null")
    },
    "object_dump": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_dump",
        "method_parameters": (("object","str"),("type","int")),
        "method_returns": ("string","null")
    },
    "object_groups": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_groups",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "object_has_mesh": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_has_mesh",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "object_layer": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_layer",
        "method_parameters": (("objects","arr_of_str"),("layer","str")),
        "method_returns": ("number","number","number","null")
    },
    "object_layout": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_layout",
        "method_parameters": (("object","str"),("layout","str"),("return_name","bln")),
        "method_returns": ("string","string","null")
    },
    "object_linetype": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_linetype",
        "method_parameters": (("objects","arr_of_str"),("layer","str")),
        "method_returns": ("number","number","number","null")
    },
    "object_linetype_source": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_linetype_source",
        "method_parameters": (("objects","arr_of_str"),("source","int")),
        "method_returns": ("number","number","number","null")
    },
    "object_material_index": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_material_index",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "object_material_source": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_material_source",
        "method_parameters": (("objects","arr_of_str"),("source","int")),
        "method_returns": ("number","number","number","null")
    },
    "object_mesh_density": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_density",
        "method_parameters": (("object","str"),("density","dbl")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_angle": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_angle",
        "method_parameters": (("object","str"),("angle","dbl")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_aspect_ratio": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_aspect_ratio",
        "method_parameters": (("object","str"),("ratio","dbl")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_dist_edge_to_srf": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_dist_edge_to_srf",
        "method_parameters": (("object","str"),("distance","dbl")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_edge_length": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_edge_length",
        "method_parameters": (("object","str"),("length","dbl")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_min_edge_length": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_min_edge_length",
        "method_parameters": (("object","str"),("length","dbl")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_min_initial_grid_quads": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_min_initial_grid_quads",
        "method_parameters": (("object","str"),("quads","int")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_quality": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_quality",
        "method_parameters": (("object","str"),("quality","int")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_settings": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_settings",
        "method_parameters": (("object","str"),("settings","int")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_names": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_names",
        "method_parameters": (("objects","arr_of_str"),("names","arr_of_str")),
        "method_returns": ("array","array","null")
    },
    "object_print_color": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_color",
        "method_parameters": (("objects","arr_of_str"),("color","lng")),
        "method_returns": ("number","number","number","null")
    },
    "object_print_color_source": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_color_source",
        "method_parameters": (("objects","arr_of_str"),("source","int")),
        "method_returns": ("number","number","number","null")
    },
    "object_print_width": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_width",
        "method_parameters": (("objects","arr_of_str"),("width","dbl")),
        "method_returns": ("number","number","number","null")
    },
    "object_print_width_source": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_width_source",
        "method_parameters": (("objects","arr_of_str"),("source","int")),
        "method_returns": ("number","number","number","null")
    },
    "object_top_group": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_top_group",
        "method_parameters": (("object","str")),
        "method_returns": ("string","null")
    },
    "object_type": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_type",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "object_u_r_l": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "object_u_r_l",
        "method_parameters": (("objects","arr_of_str"),("u_r_l","str")),
        "method_returns": ("string","string","number","null")
    },
    "orient_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "orient_objects",
        "method_parameters": (("objects","arr_of_str"),("reference","arr_of_dbl"),("target","arr_of_dbl"),("flags","int")),
        "method_returns": ("array","null")
    },
    "remap_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "remap_objects",
        "method_parameters": (("object","arr_of_str"),("src_plane","arr_of_dbl"),("dst_plane","arr_of_dbl"),("copy","bln")),
        "method_returns": ("array","null")
    },
    "rotate_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "rotate_objects",
        "method_parameters": (("objects","arr_of_str"),("point","arr_of_dbl"),("angle","dbl"),("axis","arr_of_dbl"),("copy","bln")),
        "method_returns": ("string","null")
    },
    "scale_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "scale_objects",
        "method_parameters": (("objects","arr_of_str"),("origin","arr_of_dbl"),("scale","arr_of_dbl"),("copy","bln")),
        "method_returns": ("array","null")
    },
    "select_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "select_objects",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("number","null")
    },
    "shear_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "shear_objects",
        "method_parameters": (("objects","arr_of_str"),("origin","arr_of_dbl"),("ref_pt","arr_of_dbl"),("scale","arr_of_int"),("copy","bln")),
        "method_returns": ("array","null")
    },
    "show_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "show_objects",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("number","null")
    },
    "transform_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "transform_objects",
        "method_parameters": (("objects","arr_of_str"),("matrix","arr_of_str"),("copy","bln")),
        "method_returns": ("array","null")
    },
    "unlock_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "unlock_objects",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("number","null")
    },
    "unselect_objects": {
        "method_class": "Object",
        "method_type": "METHOD",
        "method_name": "unselect_objects",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("number","null")
    },
}
object_grip = {
    "enable_object_grips": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "enable_object_grips",
        "method_parameters": (("object","str"),("enable","bln")),
        "method_returns": ("boolean","null")
    },
    "get_object_grips": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "get_object_grips",
        "method_parameters": (("message","str"),("pre_select","bln"),("select","bln")),
        "method_returns": ("array","string","number","array","null")
    },
    "next_object_grip": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "next_object_grip",
        "method_parameters": (("object","str"),("index","int"),("direction","int"),("enable","bln")),
        "method_returns": ("number","null")
    },
    "object_grip_count": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grip_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "object_grip_locations": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grip_locations",
        "method_parameters": (("object","str"),("points","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "object_grips_on": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grips_on",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "object_grips_selected": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grips_selected",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "prev_object_grip": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "prev_object_grip",
        "method_parameters": (("object","str"),("index","int"),("direction","int"),("enable","bln")),
        "method_returns": ("number","null")
    },
    "select_object_grips": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "select_object_grips",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "selected_object_grips": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "selected_object_grips",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "unselect_object_grips": {
        "method_class": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "unselect_object_grips",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
}
point_and_vector = {
    "is_vector_parallel_to": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_parallel_to",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("number","null")
    },
    "is_vector_perpendicular_to": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_perpendicular_to",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_vector_tiny": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_tiny",
        "method_parameters": (("vector","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_vector_zero": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_zero",
        "method_parameters": (("vector","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "point_add": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_add",
        "method_parameters": (("point1","arr_of_dbl"),("point2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "point_array_bounding_box": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_array_bounding_box",
        "method_parameters": (("points","arr_of_dbl"),("view","str"),("world_coords","bln")),
        "method_returns": ("array","null")
    },
    "point_array_closest_point": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_array_closest_point",
        "method_parameters": (("points","arr_of_dbl"),("point","arr_of_dbl")),
        "method_returns": ("number","null")
    },
    "point_array_transform": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_array_transform",
        "method_parameters": (("points","arr_of_dbl"),("xform","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "point_compare": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_compare",
        "method_parameters": (("point1","arr_of_dbl"),("point2","arr_of_dbl"),("tolerance","dbl")),
        "method_returns": ("boolean","null")
    },
    "point_divide": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_divide",
        "method_parameters": (("point","arr_of_dbl"),("scale","dbl")),
        "method_returns": ("array","null")
    },
    "point_scale": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_scale",
        "method_parameters": (("point","arr_of_dbl"),("scale","dbl")),
        "method_returns": ("array","null")
    },
    "point_subtract": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_subtract",
        "method_parameters": (("point1","arr_of_dbl"),("point2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "point_transform": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_transform",
        "method_parameters": (("point","arr_of_dbl"),("xform","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "points_are_coplanar": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "points_are_coplanar",
        "method_parameters": (("points","arr_of_dbl"),("tolerance","dbl")),
        "method_returns": ("boolean","null")
    },
    "project_point_to_mesh": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "project_point_to_mesh",
        "method_parameters": (("points","arr_of_dbl"),("meshes","arr_of_str"),("direction","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "project_point_to_surface": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "project_point_to_surface",
        "method_parameters": (("points","arr_of_dbl"),("surfaces","arr_of_str"),("direction","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "pull_points": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "pull_points",
        "method_parameters": (("object","str"),("points","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_add": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_add",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_compare": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_compare",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("null")
    },
    "vector_create": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_create",
        "method_parameters": (("point1","arr_of_dbl"),("point2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_cross_product": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_cross_product",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_divide": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_divide",
        "method_parameters": (("vector","arr_of_dbl"),("divide","dbl")),
        "method_returns": ("array","null")
    },
    "vector_dot_product": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_dot_product",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("null")
    },
    "vector_length": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_length",
        "method_parameters": (("vector","arr_of_dbl")),
        "method_returns": ("null")
    },
    "vector_multiply": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_multiply",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("number","null")
    },
    "vector_reverse": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_reverse",
        "method_parameters": (("vector","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_rotate": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_rotate",
        "method_parameters": (("vector","arr_of_dbl"),("angle","dbl"),("axis","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_scale": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_scale",
        "method_parameters": (("vector","arr_of_dbl"),("scale","dbl")),
        "method_returns": ("array","null")
    },
    "vector_subtract": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_subtract",
        "method_parameters": (("vector1","arr_of_dbl"),("vector2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_transform": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_transform",
        "method_parameters": (("vector","arr_of_dbl"),("xform","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "vector_unitize": {
        "method_class": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_unitize",
        "method_parameters": (("vector","arr_of_dbl")),
        "method_returns": ("array","null")
    },
}
selection = {
    "all_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "all_objects",
        "method_parameters": (("select","bln"),("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "first_object": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "first_object",
        "method_parameters": (("select","bln"),("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("string","null")
    },
    "get_curve_object": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "get_curve_object",
        "method_parameters": (("message","str"),("pre_select","bln"),("select","bln")),
        "method_returns": ("array","null")
    },
    "get_object_ex": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "get_object_ex",
        "method_parameters": (("message","str"),("type","int"),("pre_select","bln"),("select","bln"),("objects","arr_of_str")),
        "method_returns": ("array","null")
    },
    "get_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "get_objects",
        "method_parameters": (("message","str"),("type","int"),("group","bln"),("pre_select","bln"),("select","bln"),("objects","arr_of_str")),
        "method_returns": ("array","null")
    },
    "get_objects_ex": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "get_objects_ex",
        "method_parameters": (("message","str"),("type","int"),("group","bln"),("pre_select","bln"),("select","bln"),("objects","arr_of_str")),
        "method_returns": ("array","null")
    },
    "get_point_coordinates": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "get_point_coordinates",
        "method_parameters": (("message","str"),("pre_select","bln")),
        "method_returns": ("array","null")
    },
    "get_surface_object": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "get_surface_object",
        "method_parameters": (("message","str"),("pre_select","bln"),("select","bln")),
        "method_returns": ("array","null")
    },
    "hidden_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "hidden_objects",
        "method_parameters": (("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "invert_selected_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "invert_selected_objects",
        "method_parameters": (("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "last_created_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "last_created_objects",
        "method_parameters": (("select","bln")),
        "method_returns": ("array","null")
    },
    "last_object": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "last_object",
        "method_parameters": (("select","bln"),("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("string","null")
    },
    "locked_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "locked_objects",
        "method_parameters": (("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "next_object": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "next_object",
        "method_parameters": (("object","str"),("select","bln"),("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("string","null")
    },
    "normal_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "normal_objects",
        "method_parameters": (("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "objects_by_color": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_color",
        "method_parameters": (("color","lng"),("select","bln"),("include_lights","bln")),
        "method_returns": ("array","null")
    },
    "objects_by_group": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_group",
        "method_parameters": (("group","str"),("select","bln")),
        "method_returns": ("array","null")
    },
    "objects_by_layer": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_layer",
        "method_parameters": (("layer","str"),("select","bln")),
        "method_returns": ("array","null")
    },
    "objects_by_name": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_name",
        "method_parameters": (("name","str"),("select","bln"),("include_lights","bln")),
        "method_returns": ("array","null")
    },
    "objects_by_type": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_type",
        "method_parameters": (("type","int"),("select","bln")),
        "method_returns": ("array","null")
    },
    "objects_by_u_r_l": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_u_r_l",
        "method_parameters": (("u_r_l","str"),("select","bln"),("include_lights","bln")),
        "method_returns": ("array","null")
    },
    "prev_selected_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "prev_selected_objects",
        "method_parameters": (("select","bln")),
        "method_returns": ("array","null")
    },
    "reference_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "reference_objects",
        "method_parameters": (("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "selected_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "selected_objects",
        "method_parameters": (("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "unselect_all_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "unselect_all_objects",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "unselected_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "unselected_objects",
        "method_parameters": (("select","bln"),("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
    "visible_objects": {
        "method_class": "Selection",
        "method_type": "METHOD",
        "method_name": "visible_objects",
        "method_parameters": (("view","str"),("select","bln"),("include_lights","bln"),("include_grips","bln")),
        "method_returns": ("array","null")
    },
}
surface_and_polysurface = {
    "add_box": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_box",
        "method_parameters": (("corners","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_cone": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_cone",
        "method_parameters": (("base","arr_of_dbl"),("plane","arr_of_dbl"),("height","dbl"),("height","dbl"),("radius","dbl"),("cap","bln")),
        "method_returns": ("string","null")
    },
    "add_cut_plane": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_cut_plane",
        "method_parameters": (("objects","arr_of_str"),("start_point","arr_of_dbl"),("end_point","arr_of_dbl"),("normal","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_cylinder": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_cylinder",
        "method_parameters": (("base","arr_of_dbl"),("plane","arr_of_dbl"),("height","dbl"),("height","dbl"),("radius","dbl"),("cap","bln")),
        "method_returns": ("string","null")
    },
    "add_edge_srf": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_edge_srf",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("string","null")
    },
    "add_loft_srf": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_loft_srf",
        "method_parameters": (("objects","arr_of_str"),("start_pt","arr_of_dbl"),("end_pt","arr_of_dbl"),("type","int"),("style","int"),("value","n"),("closed","bln")),
        "method_returns": ("array","null")
    },
    "add_nurbs_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_nurbs_surface",
        "method_parameters": (("point_count","arr_of_int"),("points","arr_of_dbl"),("knots_u","arr_of_int"),("knots_v","arr_of_int"),("degree","arr_of_int"),("weights","arr_of_int")),
        "method_returns": ("string","null")
    },
    "add_planar_srf": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_planar_srf",
        "method_parameters": (("objects","arr_of_str")),
        "method_returns": ("array","null")
    },
    "add_plane_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_plane_surface",
        "method_parameters": (("plane","arr_of_dbl"),("d_u","dbl"),("d_v","dbl")),
        "method_returns": ("string","null")
    },
    "add_rail_rev_srf": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_rail_rev_srf",
        "method_parameters": (("profile","str"),("rail","str"),("axis","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_rev_srf": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_rev_srf",
        "method_parameters": (("profile","str"),("axis","arr_of_dbl"),("start_angle","dbl"),("end_angle","dbl")),
        "method_returns": ("string","null")
    },
    "add_sphere": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_sphere",
        "method_parameters": (("center","arr_of_dbl"),("plane","arr_of_dbl"),("radius","dbl")),
        "method_returns": ("string","null")
    },
    "add_srf_contour_crvs": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_contour_crvs",
        "method_parameters": (("object","str"),("start_point","arr_of_dbl"),("end_point","arr_of_dbl"),("plane","arr_of_dbl"),("interval","dbl")),
        "method_returns": ("array","null")
    },
    "add_srf_control_pt_grid": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_control_pt_grid",
        "method_parameters": (("count","arr_of_int"),("points","arr_of_dbl"),("degree","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_srf_pt": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_pt",
        "method_parameters": (("points","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "add_srf_pt_grid": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_pt_grid",
        "method_parameters": (("count","arr_of_int"),("points","arr_of_dbl"),("degree","arr_of_int"),("closed","arr_of_bln")),
        "method_returns": ("string","null")
    },
    "add_srf_section_crvs": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_section_crvs",
        "method_parameters": (("object","str"),("plane","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "add_sweep1": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_sweep1",
        "method_parameters": (("rail","str"),("shapes","arr_of_str"),("start_pt","arr_of_dbl"),("end_pt","arr_of_dbl"),("closed","bln"),("style","int"),("style_arg","va"),("simplify","int"),("simplify_arg","va")),
        "method_returns": ("array","null")
    },
    "add_sweep2": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_sweep2",
        "method_parameters": (("rails","arr_of_str"),("shapes","arr_of_str"),("start_pt","arr_of_dbl"),("end_pt","arr_of_dbl"),("closed","bln"),("simple_sweep","bln"),("maintain_height","bln"),("simplify","int"),("simplify_arg","va")),
        "method_returns": ("array","null")
    },
    "add_torus": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_torus",
        "method_parameters": (("base","arr_of_dbl"),("plane","arr_of_dbl"),("major_radius","dbl"),("minor_radius","dbl"),("direction","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "boolean_difference": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "boolean_difference",
        "method_parameters": (("input0","arr_of_str"),("input1","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "boolean_intersection": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "boolean_intersection",
        "method_parameters": (("input0","arr_of_str"),("input1","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "boolean_union": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "boolean_union",
        "method_parameters": (("input","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "brep_closest_point": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "brep_closest_point",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "cap_planar_holes": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "cap_planar_holes",
        "method_parameters": (("surface","str")),
        "method_returns": ("boolean","null")
    },
    "duplicate_edge_curves": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "duplicate_edge_curves",
        "method_parameters": (("object","str"),("select","bln")),
        "method_returns": ("array","null")
    },
    "duplicate_surface_border": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "duplicate_surface_border",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "evaluate_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "evaluate_surface",
        "method_parameters": (("object","str"),("parameter","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "explode_polysurfaces": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "explode_polysurfaces",
        "method_parameters": (("objects","arr_of_str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "extract_iso_curve": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extract_iso_curve",
        "method_parameters": (("object","str"),("parameter","arr_of_dbl"),("dir","int")),
        "method_returns": ("array","null")
    },
    "extrude_curve": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve",
        "method_parameters": (("curve","str"),("path","str")),
        "method_returns": ("string","null")
    },
    "extrude_curve_point": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve_point",
        "method_parameters": (("curve","str"),("point","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "extrude_curve_straight": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve_straight",
        "method_parameters": (("curve","str"),("start_point","arr_of_dbl"),("end_point","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "extrude_curve_tapered": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve_tapered",
        "method_parameters": (("curve","str"),("distance","dbl"),("direction","arr_of_dbl"),("base_point","arr_of_dbl"),("angle","dbl"),("corner_type","int")),
        "method_returns": ("array","null")
    },
    "extrude_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_surface",
        "method_parameters": (("surface","str"),("curve","str"),("cap","bln")),
        "method_returns": ("string","null")
    },
    "fit_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "fit_surface",
        "method_parameters": (("object","str"),("degree","arr_of_int"),("tolerance","dbl")),
        "method_returns": ("string","null")
    },
    "flip_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "flip_surface",
        "method_parameters": (("object","str"),("flip","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "insert_surface_knot": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "insert_surface_knot",
        "method_parameters": (("object","str"),("parameter","dbl"),("direction","int"),("symmetrical","bln")),
        "method_returns": ("boolean","null")
    },
    "intersect_breps": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "intersect_breps",
        "method_parameters": (("brep1","str"),("brep2","str"),("tolerance","dbl")),
        "method_returns": ("array","null")
    },
    "is_brep": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_brep",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_brep_manifold": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_brep_manifold",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_cone": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_cone",
        "method_parameters": (("surface","str")),
        "method_returns": ("boolean","null")
    },
    "is_cylinder": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_cylinder",
        "method_parameters": (("surface","str")),
        "method_returns": ("boolean","null")
    },
    "is_parameter_on_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_parameter_on_surface",
        "method_parameters": (("object","str"),("parameter","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_plane_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_plane_surface",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_point_in_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_point_in_surface",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_point_on_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_point_on_surface",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_poly_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_poly_surface",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_poly_surface_closed": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_poly_surface_closed",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_poly_surface_planar": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_poly_surface_planar",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_sphere": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_sphere",
        "method_parameters": (("surface","str")),
        "method_returns": ("boolean","null")
    },
    "is_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_surface_closed": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_closed",
        "method_parameters": (("object","str"),("direction","int")),
        "method_returns": ("boolean","null")
    },
    "is_surface_periodic": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_periodic",
        "method_parameters": (("object","str"),("direction","int")),
        "method_returns": ("boolean","null")
    },
    "is_surface_planar": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_planar",
        "method_parameters": (("object","str"),("tolerance","dbl")),
        "method_returns": ("boolean","null")
    },
    "is_surface_rational": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_rational",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_surface_singular": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_singular",
        "method_parameters": (("object","str"),("direction","int")),
        "method_returns": ("boolean","null")
    },
    "is_surface_trimmed": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_trimmed",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_torus": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_torus",
        "method_parameters": (("surface","str")),
        "method_returns": ("boolean","null")
    },
    "join_surfaces": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "join_surfaces",
        "method_parameters": (("object","str"),("delete","bln")),
        "method_returns": ("string","null")
    },
    "make_surface_non_periodic": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "make_surface_non_periodic",
        "method_parameters": (("object","str"),("direction","int"),("delete","bln")),
        "method_returns": ("string","string","null")
    },
    "make_surface_periodic": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "make_surface_periodic",
        "method_parameters": (("object","str"),("direction","int"),("delete","bln")),
        "method_returns": ("string","string","null")
    },
    "offset_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "offset_surface",
        "method_parameters": (("object","str"),("distance","dbl")),
        "method_returns": ("string","null")
    },
    "pull_curve": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "pull_curve",
        "method_parameters": (("surface","str"),("curve","str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "rebuild_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "rebuild_surface",
        "method_parameters": (("object","str"),("degree","arr_of_int"),("point_count","arr_of_int")),
        "method_returns": ("boolean","null")
    },
    "remove_surface_knot": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "remove_surface_knot",
        "method_parameters": (("object","str"),("parameter","dbl"),("direction","int")),
        "method_returns": ("boolean","null")
    },
    "reverse_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "reverse_surface",
        "method_parameters": (("object","str"),("direction","int")),
        "method_returns": ("boolean","null")
    },
    "short_path": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "short_path",
        "method_parameters": (("surface","str"),("start","arr_of_dbl"),("end","arr_of_dbl")),
        "method_returns": ("string","null")
    },
    "shrink_trimmed_surface": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "shrink_trimmed_surface",
        "method_parameters": (("surface","str")),
        "method_returns": ("boolean","null")
    },
    "split_brep": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "split_brep",
        "method_parameters": (("brep","str"),("cutter","str"),("delete","bln")),
        "method_returns": ("array","null")
    },
    "surface_area": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_area",
        "method_parameters": (("object","str")),
        "method_returns": ("array","number","number","null")
    },
    "surface_area_centroid": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_area_centroid",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "surface_area_moments": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_area_moments",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "surface_closest_point": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_closest_point",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "surface_cone": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_cone",
        "method_parameters": (("surface","str")),
        "method_returns": ("array","array","number","number","null")
    },
    "surface_contour_points": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_contour_points",
        "method_parameters": (("object","str"),("start_point","arr_of_dbl"),("end_point","arr_of_dbl"),("interval","dbl"),("angle","dbl")),
        "method_returns": ("array","null")
    },
    "surface_curvature": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_curvature",
        "method_parameters": (("object","str"),("parameter","arr_of_dbl")),
        "method_returns": ("array","number","number","number","number","null")
    },
    "surface_curvature_analysis": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_curvature_analysis",
        "method_parameters": (("object","str")),
        "method_returns": ("array","array","array","array","array","null")
    },
    "surface_cylinder": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_cylinder",
        "method_parameters": (("surface","str")),
        "method_returns": ("array","array","number","number","null")
    },
    "surface_degree": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_degree",
        "method_parameters": (("object","str"),("direction","int")),
        "method_returns": ("array","number","null")
    },
    "surface_domain": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_domain",
        "method_parameters": (("object","str"),("direction","int")),
        "method_returns": ("array","null")
    },
    "surface_edit_points": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_edit_points",
        "method_parameters": (("object","str"),("return_parameters","bln"),("return_all","bln")),
        "method_returns": ("array","array","null")
    },
    "surface_evaluate": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_evaluate",
        "method_parameters": (("object","str"),("parameter","arr_of_dbl"),("derivative","int")),
        "method_returns": ("array","array","array","array","array","array","array","array","null")
    },
    "surface_frame": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_frame",
        "method_parameters": (("object","str"),("parameter","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "surface_isocurve_density": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_isocurve_density",
        "method_parameters": (("object","str"),("density","int")),
        "method_returns": ("number","number","null")
    },
    "surface_knot_count": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_knot_count",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "surface_knots": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_knots",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "surface_normal": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_normal",
        "method_parameters": (("object","str"),("parameter","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "surface_point_count": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_point_count",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "surface_points": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_points",
        "method_parameters": (("object","str"),("return_all","bln")),
        "method_returns": ("array","null")
    },
    "surface_principal_curvature": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_principal_curvature",
        "method_parameters": (("object","str"),("point","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "surface_seam": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_seam",
        "method_parameters": (("object","str"),("direction","int"),("parameter","dbl")),
        "method_returns": ("boolean","null")
    },
    "surface_sphere": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_sphere",
        "method_parameters": (("surface","str")),
        "method_returns": ("array","array","number","null")
    },
    "surface_surface_intersection": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_surface_intersection",
        "method_parameters": (("surface_a","str"),("surface_b","str"),("tolerance","dbl"),("create","bln")),
        "method_returns": ("array","array","number","string","null")
    },
    "surface_torus": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_torus",
        "method_parameters": (("surface","str")),
        "method_returns": ("array","array","number","number","null")
    },
    "surface_volume": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_volume",
        "method_parameters": (("object","str")),
        "method_returns": ("array","number","number","null")
    },
    "surface_volume_centroid": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_volume_centroid",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "surface_volume_moments": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_volume_moments",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
    "surface_weights": {
        "method_class": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_weights",
        "method_parameters": (("object","str")),
        "method_returns": ("array","null")
    },
}
transformation = {
    "is_xform_identity": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "is_xform_identity",
        "method_parameters": (("xform","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_xform_similarity": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "is_xform_similarity",
        "method_parameters": (("xform","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "is_xform_zero": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "is_xform_zero",
        "method_parameters": (("xform","arr_of_dbl")),
        "method_returns": ("boolean","null")
    },
    "xform_c_plane_to_world": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_c_plane_to_world",
        "method_parameters": (("point","arr_of_dbl"),("plane","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_change_basis": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_change_basis",
        "method_parameters": (("plane1","arr_of_dbl"),("plane2","arr_of_dbl"),("x0","arr_of_dbl"),("y0","arr_of_dbl"),("z0","arr_of_dbl"),("x1","arr_of_dbl"),("y1","arr_of_dbl"),("z1","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_compare": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_compare",
        "method_parameters": (("xform1","arr_of_dbl"),("xform2","arr_of_dbl")),
        "method_returns": ("null")
    },
    "xform_determinant": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_determinant",
        "method_parameters": (("xform","arr_of_dbl")),
        "method_returns": ("number","null")
    },
    "xform_diagonal": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_diagonal",
        "method_parameters": (("value","dbl")),
        "method_returns": ("array","null")
    },
    "xform_identity": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_identity",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "xform_inverse": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_inverse",
        "method_parameters": (("xform","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_mirror": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_mirror",
        "method_parameters": (("point","arr_of_dbl"),("normal","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_multiply": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_multiply",
        "method_parameters": (("xform1","arr_of_dbl"),("xform2","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_planar_projection": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_planar_projection",
        "method_parameters": (("plane","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_rotation": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_rotation",
        "method_parameters": (("plane1","arr_of_dbl"),("plane2","arr_of_dbl"),("angle","dbl"),("axis","arr_of_dbl"),("start_dir","arr_of_dbl"),("end_dir","arr_of_dbl"),("point","arr_of_dbl"),("x0","arr_of_dbl"),("y0","arr_of_dbl"),("z0","arr_of_dbl"),("x1","arr_of_dbl"),("y1","arr_of_dbl"),("z1","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_scale": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_scale",
        "method_parameters": (("plane","arr_of_dbl"),("x_scale","dbl"),("y_scale","dbl"),("z_scale","dbl"),("vector","arr_of_dbl"),("point","arr_of_dbl"),("scale","dbl")),
        "method_returns": ("array","null")
    },
    "xform_screen_to_world": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_screen_to_world",
        "method_parameters": (("point","arr_of_dbl"),("view","str"),("convert","bln")),
        "method_returns": ("array","null")
    },
    "xform_shear": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_shear",
        "method_parameters": (("plane","arr_of_dbl"),("x1","arr_of_dbl"),("y1","arr_of_dbl"),("z1","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_translation": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_translation",
        "method_parameters": (("vector","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_world_to_c_plane": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_world_to_c_plane",
        "method_parameters": (("point","arr_of_dbl"),("plane","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "xform_world_to_screen": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_world_to_screen",
        "method_parameters": (("point","arr_of_dbl"),("view","str"),("convert","bln")),
        "method_returns": ("array","array","null")
    },
    "xform_zero": {
        "method_class": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_zero",
        "method_parameters": (),
        "method_returns": ("array")
    },
}
user_data = {
    "attribute_data_count": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "attribute_data_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "delete_attribute_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "delete_attribute_data",
        "method_parameters": (("object","str"),("section","str"),("entry","str")),
        "method_returns": ("boolean","null")
    },
    "delete_document_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "delete_document_data",
        "method_parameters": (("section","str"),("entry","str")),
        "method_returns": ("boolean","null")
    },
    "delete_object_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "delete_object_data",
        "method_parameters": (("object","str"),("section","str"),("entry","str")),
        "method_returns": ("boolean","null")
    },
    "document_data_count": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "document_data_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "get_attribute_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_attribute_data",
        "method_parameters": (("object","str"),("section","str"),("entry","str")),
        "method_returns": ("array","array","string","null")
    },
    "get_document_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_document_data",
        "method_parameters": (("section","str"),("entry","str")),
        "method_returns": ("array","array","string","null")
    },
    "get_object_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_object_data",
        "method_parameters": (("object","str"),("section","str"),("entry","str")),
        "method_returns": ("array","array","string","null")
    },
    "get_user_text": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_user_text",
        "method_parameters": (("object","str"),("key","str"),("attach_to_geometry","bln")),
        "method_returns": ("string","array","null")
    },
    "is_attribute_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_attribute_data",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_document_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_document_data",
        "method_parameters": (),
        "method_returns": ("boolean")
    },
    "is_object_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_object_data",
        "method_parameters": (("object","str")),
        "method_returns": ("boolean","null")
    },
    "is_user_text": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_user_text",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "object_data_count": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "object_data_count",
        "method_parameters": (("object","str")),
        "method_returns": ("number","null")
    },
    "set_attribute_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_attribute_data",
        "method_parameters": (("object","str"),("section","str"),("entry","str"),("value","str")),
        "method_returns": ("string","null")
    },
    "set_document_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_document_data",
        "method_parameters": (("section","str"),("entry","str"),("value","str")),
        "method_returns": ("string","null")
    },
    "set_object_data": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_object_data",
        "method_parameters": (("object","str"),("section","str"),("entry","str"),("value","str")),
        "method_returns": ("string","null")
    },
    "set_user_text": {
        "method_class": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_user_text",
        "method_parameters": (("object","str"),("key","str"),("value","str"),("attach_to_geometry","bln")),
        "method_returns": ("boolean","null")
    },
}
user_interface = {
    "browse_for_folder": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "browse_for_folder",
        "method_parameters": (("folder","str"),("message","str"),("title","str")),
        "method_returns": ("string","null")
    },
    "check_list_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "check_list_box",
        "method_parameters": (("items","arr_of_str"),("values","arr_of_bln"),("message","str"),("title","str")),
        "method_returns": ("array","null")
    },
    "combo_list_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "combo_list_box",
        "method_parameters": (("items","arr_of_str"),("message","str"),("title","str")),
        "method_returns": ("string","null")
    },
    "edit_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "edit_box",
        "method_parameters": (("string","str"),("message","str"),("title","str")),
        "method_returns": ("string","null")
    },
    "get_angle": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_angle",
        "method_parameters": (("point","arr_of_dbl"),("reference","arr_of_dbl"),("angle","dbl"),("message","str")),
        "method_returns": ("number","null")
    },
    "get_boolean": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_boolean",
        "method_parameters": (("message","str"),("items","arr_of_str"),("defaults","arr_of_bln")),
        "method_returns": ("array","null")
    },
    "get_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_box",
        "method_parameters": (("mode","int"),("point","arr_of_dbl"),("prompt1","str"),("prompt2","str"),("prompt3","str")),
        "method_returns": ("array","null")
    },
    "get_color": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_color",
        "method_parameters": (("color","lng")),
        "method_returns": ("number","null")
    },
    "get_distance": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_distance",
        "method_parameters": (("point","arr_of_dbl"),("distance","dbl"),("message1","str"),("message2","str")),
        "method_returns": ("number","null")
    },
    "get_integer": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_integer",
        "method_parameters": (("message","str"),("number","int"),("min","int"),("max","int")),
        "method_returns": ("number","null")
    },
    "get_layer": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_layer",
        "method_parameters": (("title","str"),("layer","str"),("show_new_layer","bln"),("show_set_current","bln")),
        "method_returns": ("string","null")
    },
    "get_linetype": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_linetype",
        "method_parameters": (("linetype","str")),
        "method_returns": ("string","null")
    },
    "get_point_on_curve": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_curve",
        "method_parameters": (("object","str"),("message","str")),
        "method_returns": ("array","null")
    },
    "get_point_on_line": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_line",
        "method_parameters": (("message","str"),("start","arr_of_dbl"),("end","arr_of_dbl"),("track","bln")),
        "method_returns": ("array","null")
    },
    "get_point_on_mesh": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_mesh",
        "method_parameters": (("object","str"),("message","str")),
        "method_returns": ("array","null")
    },
    "get_point_on_plane": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_plane",
        "method_parameters": (("message","str"),("plane","arr_of_dbl"),("point","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "get_point_on_surface": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_surface",
        "method_parameters": (("object","str"),("message","str")),
        "method_returns": ("array","null")
    },
    "get_points": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_points",
        "method_parameters": (("draw","bln"),("plane","bln"),("message1","str"),("message2","str"),("max_points","int"),("base_point","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "get_print_width": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_print_width",
        "method_parameters": (("print_width","dbl")),
        "method_returns": ("number","null")
    },
    "get_real": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_real",
        "method_parameters": (("message","str"),("number","dbl"),("min","dbl"),("max","dbl")),
        "method_returns": ("number","null")
    },
    "get_rectangle": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_rectangle",
        "method_parameters": (("mode","int"),("point","arr_of_dbl"),("prompt1","str"),("prompt2","str"),("prompt3","str")),
        "method_returns": ("array","null")
    },
    "get_string": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_string",
        "method_parameters": (("message","str"),("string","str"),("strings","arr_of_str")),
        "method_returns": ("string","null")
    },
    "get_surface_iso_param_point": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_surface_iso_param_point",
        "method_parameters": (("object","str"),("message","str")),
        "method_returns": ("array","null")
    },
    "html_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "html_box",
        "method_parameters": (("file_name","str"),("arguments","va"),("options","str"),("modal","bln")),
        "method_returns": ("boolean","null")
    },
    "integer_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "integer_box",
        "method_parameters": (("message","str"),("number","int"),("title","str")),
        "method_returns": ("number","null")
    },
    "list_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "list_box",
        "method_parameters": (("items","arr_of_str"),("message","str"),("title","str")),
        "method_returns": ("string","null")
    },
    "message_beep": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "message_beep",
        "method_parameters": (("beep","int")),
        "method_returns": ()
    },
    "message_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "message_box",
        "method_parameters": (("message","str"),("buttons","int"),("title","str")),
        "method_returns": ("number")
    },
    "multi_list_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "multi_list_box",
        "method_parameters": (("items","arr_of_str"),("message","str"),("title","str")),
        "method_returns": ("array","null")
    },
    "open_file_names": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "open_file_names",
        "method_parameters": (("title","str"),("filter","str"),("folder","str"),("filename","str"),("extension","str")),
        "method_returns": ("array","null")
    },
    "popup_menu": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "popup_menu",
        "method_parameters": (("items","arr_of_str"),("modes","arr_of_int"),("point","arr_of_dbl"),("view","str")),
        "method_returns": ("number","number","null")
    },
    "property_list_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "property_list_box",
        "method_parameters": (("items","arr_of_str"),("values","arr_of_str"),("message","str"),("title","str")),
        "method_returns": ("array","null")
    },
    "real_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "real_box",
        "method_parameters": (("message","str"),("number","dbl"),("title","str")),
        "method_returns": ("number","null")
    },
    "save_file_name": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "save_file_name",
        "method_parameters": (("title","str"),("filter","str"),("folder","str"),("filename","str"),("extension","str")),
        "method_returns": ("string","null")
    },
    "string_box": {
        "method_class": "User_Interface",
        "method_type": "METHOD",
        "method_name": "string_box",
        "method_parameters": (("message","str"),("string","str"),("title","str")),
        "method_returns": ("string","null")
    },
}
utility = {
    "all_procedures": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "all_procedures",
        "method_parameters": (("all","bln")),
        "method_returns": ("array","null")
    },
    "clipboard_text": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "clipboard_text",
        "method_parameters": (("text","str")),
        "method_returns": ("string","string","null")
    },
    "color_adjust_luma": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "color_adjust_luma",
        "method_parameters": (("r_g_b","lng"),("luma","int"),("scale","bln")),
        "method_returns": ("number","null")
    },
    "color_blue_value": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "color_blue_value",
        "method_parameters": (("r_g_b","lng")),
        "method_returns": ("number","null")
    },
    "color_green_value": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "color_green_value",
        "method_parameters": (("r_g_b","lng")),
        "method_returns": ("number","null")
    },
    "color_h_l_s_to_r_g_b": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "color_h_l_s_to_r_g_b",
        "method_parameters": (("r_g_b","lng")),
        "method_returns": ("number","null")
    },
    "color_r_g_b_to_h_l_s": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "color_r_g_b_to_h_l_s",
        "method_parameters": (("r_g_b","lng")),
        "method_returns": ("array","null")
    },
    "color_red_value": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "color_red_value",
        "method_parameters": (("r_g_b","lng")),
        "method_returns": ("number","null")
    },
    "cull_duplicate_numbers": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "cull_duplicate_numbers",
        "method_parameters": (("numbers","arr_of_int"),("tolerance","dbl")),
        "method_returns": ("array","null")
    },
    "cull_duplicate_points": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "cull_duplicate_points",
        "method_parameters": (("points","arr_of_dbl"),("tolerance","dbl")),
        "method_returns": ("array","null")
    },
    "cull_duplicate_strings": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "cull_duplicate_strings",
        "method_parameters": (("strings","arr_of_int"),("case_sensitive","bln")),
        "method_returns": ("array","null")
    },
    "current_printer": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "current_printer",
        "method_parameters": (("printer","str")),
        "method_returns": ("string","string","null")
    },
    "get_settings": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "get_settings",
        "method_parameters": (("filename","str"),("section","str"),("entry","str")),
        "method_returns": ("array","array","string","null")
    },
    "is_procedure": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "is_procedure",
        "method_parameters": (("sub_name","str")),
        "method_returns": ("boolean","null")
    },
    "printer_names": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "printer_names",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "pt2_str": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "pt2_str",
        "method_parameters": (("point","arr_of_dbl"),("precision","n"),("space","bln")),
        "method_returns": ("string","null")
    },
    "save_settings": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "save_settings",
        "method_parameters": (("filename","str"),("section","str"),("entry","str"),("string","str")),
        "method_returns": ("boolean","null")
    },
    "simplify_array": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "simplify_array",
        "method_parameters": (("points","arr_of_dbl")),
        "method_returns": ("array","null")
    },
    "sleep": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "sleep",
        "method_parameters": (("milliseconds","lng")),
        "method_returns": ("null")
    },
    "spool_to_printer": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "spool_to_printer",
        "method_parameters": (("file","str"),("printer","str")),
        "method_returns": ("string","null")
    },
    "str2_pt": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "str2_pt",
        "method_parameters": (("point","str")),
        "method_returns": ("array","null")
    },
    "str2_pt_array": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "str2_pt_array",
        "method_parameters": (("points","str")),
        "method_returns": ("array","null")
    },
    "strtok": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "strtok",
        "method_parameters": (("text","str"),("delimiters","str")),
        "method_returns": ("array","null")
    },
    "text_out": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "text_out",
        "method_parameters": (("text","str"),("title","str")),
        "method_returns": ("null")
    },
    "version": {
        "method_class": "Utility",
        "method_type": "METHOD",
        "method_name": "version",
        "method_parameters": (),
        "method_returns": ("number")
    },
}
view = {
    "add_named_c_plane": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "add_named_c_plane",
        "method_parameters": (("name","str"),("view","str")),
        "method_returns": ("string","null")
    },
    "add_named_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "add_named_view",
        "method_parameters": (("name","str"),("view","str")),
        "method_returns": ("string","null")
    },
    "background_bitmap": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "background_bitmap",
        "method_parameters": (("view","str"),("file_name","str"),("point","arr_of_dbl"),("width","dbl")),
        "method_returns": ("string","string","null")
    },
    "current_detail": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "current_detail",
        "method_parameters": (("layout","str"),("detail","str"),("return_names","bln")),
        "method_returns": ("string","string","null")
    },
    "current_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "current_view",
        "method_parameters": (("view","str"),("return_name","bln")),
        "method_returns": ("string","string","null")
    },
    "delete_named_c_plane": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "delete_named_c_plane",
        "method_parameters": (("name","str")),
        "method_returns": ("boolean","null")
    },
    "delete_named_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "delete_named_view",
        "method_parameters": (("name","str")),
        "method_returns": ("boolean","null")
    },
    "detail_names": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "detail_names",
        "method_parameters": (("layout","str"),("return_names","bln")),
        "method_returns": ("array","null")
    },
    "is_background_bitmap": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_background_bitmap",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "is_detail": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_detail",
        "method_parameters": (("layout","str"),("detail","str")),
        "method_returns": ("null")
    },
    "is_layout": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_layout",
        "method_parameters": (("layout","str")),
        "method_returns": ("null")
    },
    "is_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_view",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "is_view_current": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_view_current",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "is_view_maximized": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_view_maximized",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "is_view_perspective": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_view_perspective",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "is_view_title_visible": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_view_title_visible",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "is_wallpaper": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "is_wallpaper",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "maximize_restore_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "maximize_restore_view",
        "method_parameters": (("view","str")),
        "method_returns": ()
    },
    "named_c_planes": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "named_c_planes",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "named_views": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "named_views",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "rename_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "rename_view",
        "method_parameters": (("old_title","str"),("new_title","str")),
        "method_returns": ("string","null")
    },
    "restore_named_c_plane": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "restore_named_c_plane",
        "method_parameters": (("name","str"),("view","str")),
        "method_returns": ("string","null")
    },
    "restore_named_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "restore_named_view",
        "method_parameters": (("name","str"),("view","str"),("restore_bitmap","bln")),
        "method_returns": ("string","null")
    },
    "rotate_camera": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "rotate_camera",
        "method_parameters": (("view","str"),("direction","int"),("angle","dbl")),
        "method_returns": ("boolean","null")
    },
    "rotate_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "rotate_view",
        "method_parameters": (("view","str"),("direction","int"),("angle","dbl")),
        "method_returns": ("boolean","null")
    },
    "show_grid": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "show_grid",
        "method_parameters": (("view","str"),("show","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "show_grid_axes": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "show_grid_axes",
        "method_parameters": (("view","str"),("show","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "show_view_title": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "show_view_title",
        "method_parameters": (("view","str"),("state","bln")),
        "method_returns": ()
    },
    "show_world_axes": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "show_world_axes",
        "method_parameters": (("view","str"),("show","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "synchronize_c_planes": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "synchronize_c_planes",
        "method_parameters": (("view","str")),
        "method_returns": ("boolean","null")
    },
    "tilt_view": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "tilt_view",
        "method_parameters": (("view","str"),("direction","int"),("angle","dbl")),
        "method_returns": ("boolean","null")
    },
    "view_c_plane": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_c_plane",
        "method_parameters": (("view","str"),("plane","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "view_camera": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_camera",
        "method_parameters": (("view","str"),("camera","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "view_camera_lens": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_lens",
        "method_parameters": (("view","str"),("length","dbl")),
        "method_returns": ("number","number","null")
    },
    "view_camera_plane": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_plane",
        "method_parameters": (("view","str")),
        "method_returns": ("array","null")
    },
    "view_camera_target": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_target",
        "method_parameters": (("view","str"),("camera","arr_of_dbl"),("target","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "view_camera_up": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_up",
        "method_parameters": (("view","str"),("up_vector","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "view_display_mode_ex": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_display_mode_ex",
        "method_parameters": (("view","str"),("mode","str"),("return_names","bln")),
        "method_returns": ("number","number","null")
    },
    "view_display_mode_name": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_display_mode_name",
        "method_parameters": (("mode","str")),
        "method_returns": ("string","null")
    },
    "view_display_modes": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_display_modes",
        "method_parameters": (("return_name","bln")),
        "method_returns": ("array","null")
    },
    "view_names": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_names",
        "method_parameters": (("return_names","bln"),("type","int")),
        "method_returns": ("array","null")
    },
    "view_near_corners": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_near_corners",
        "method_parameters": (("view","str")),
        "method_returns": ("array","null")
    },
    "view_projection": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_projection",
        "method_parameters": (("view","str"),("mode","int")),
        "method_returns": ("number","number","null")
    },
    "view_radius": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_radius",
        "method_parameters": (("view","str"),("radius","dbl")),
        "method_returns": ("number","number","null")
    },
    "view_size": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_size",
        "method_parameters": (("view","str")),
        "method_returns": ("array","null")
    },
    "view_target": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_target",
        "method_parameters": (("view","str"),("target","arr_of_dbl")),
        "method_returns": ("array","array","null")
    },
    "view_title": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "view_title",
        "method_parameters": (("mode","str")),
        "method_returns": ("string","null")
    },
    "wallpaper": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "wallpaper",
        "method_parameters": (("view","str"),("file_name","str")),
        "method_returns": ("string","string","null")
    },
    "wallpaper_gray_scale": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "wallpaper_gray_scale",
        "method_parameters": (("view","str"),("gray_scale","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "wallpaper_hidden": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "wallpaper_hidden",
        "method_parameters": (("view","str"),("hidden","bln")),
        "method_returns": ("boolean","boolean","null")
    },
    "zoom_bounding_box": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "zoom_bounding_box",
        "method_parameters": (("corners","arr_of_dbl"),("view","str"),("all","bln")),
        "method_returns": ()
    },
    "zoom_extents": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "zoom_extents",
        "method_parameters": (("view","str"),("all","bln")),
        "method_returns": ()
    },
    "zoom_selected": {
        "method_class": "View",
        "method_type": "METHOD",
        "method_name": "zoom_selected",
        "method_parameters": (("view","str"),("all","bln")),
        "method_returns": ()
    },
}
