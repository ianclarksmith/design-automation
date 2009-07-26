#Fill in the data as follows:

#For method class, give a list of class names, starting from parent class, or in the case of a function, then the module name.
#For method type, insert either FUNCTION, METHOD, CONSTRUCTOR, GET_PROPERTY, or SET_PROPERTY.
#For method name, you may suggest a shorter name when the method has been moved to a sub-class.
#For method parameters, any parameters that are IDs of Rhino objects will need to be changed to classes.
#For method returns, any returns that are IDs of Rhino objects will need to be changed to classes.

application = {
    "add_alias": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "add_alias",
        "method_parameters": (("alias","str","REQ"),("macro","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "add_search_path": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "add_search_path",
        "method_parameters": (("folder","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "add_startup_script": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "add_startup_script",
        "method_parameters": (("script_file","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "alias_count": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "alias_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "alias_macro": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "alias_macro",
        "method_parameters": (("alias","str","REQ"),("macro","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "alias_names": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "alias_names",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "appearance_color": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "appearance_color",
        "method_parameters": (("item","int","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "appearance_display": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "appearance_display",
        "method_parameters": (("item","int","REQ"),("show","bln","OPT")),
        "method_returns": ("number","number","null")
    },
    "autosave_file": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "autosave_file",
        "method_parameters": (("file","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "autosave_interval": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "autosave_interval",
        "method_parameters": (("minutes","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "build_date": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "build_date",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "clear_command_history": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "clear_command_history",
        "method_parameters": (),
        "method_returns": ()
    },
    "command": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "command",
        "method_parameters": (("command","str","REQ"),("echo","bln","OPT")),
        "method_returns": ("boolean","null")
    },
    "command_history": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "command_history",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "default_renderer": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "default_renderer",
        "method_parameters": (("renderer","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "delete_alias": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "delete_alias",
        "method_parameters": (("alias","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "delete_search_path": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "delete_search_path",
        "method_parameters": (("folder","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "delete_startup_script": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "delete_startup_script",
        "method_parameters": (("script_file","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "display_ole_alerts": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "display_ole_alerts",
        "method_parameters": (("display","bln","REQ")),
        "method_returns": ("null")
    },
    "edge_analysis_color": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "edge_analysis_color",
        "method_parameters": (("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "edge_analysis_mode": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "edge_analysis_mode",
        "method_parameters": (("mode","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "enable_autosave": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "enable_autosave",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("boolean")
    },
    "enable_history_recording": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "enable_history_recording",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "exe_folder": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "exe_folder",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "exit": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "exit",
        "method_parameters": (),
        "method_returns": ()
    },
    "find_file": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "find_file",
        "method_parameters": (("filename","str","REQ")),
        "method_returns": ("string","null")
    },
    "get_plug_in_object": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "get_plug_in_object",
        "method_parameters": (("plug_in","str","REQ")),
        "method_returns": ("null")
    },
    "help": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "help",
        "method_parameters": (("topic","int","OPT")),
        "method_returns": ("boolean")
    },
    "in_command": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "in_command",
        "method_parameters": (("ignore_runners","bln","OPT")),
        "method_returns": ("number")
    },
    "install_folder": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "install_folder",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "is_alias": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "is_alias",
        "method_parameters": (("alias","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_command": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "is_command",
        "method_parameters": (("command_name","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "last_command_name": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "last_command_name",
        "method_parameters": (),
        "method_returns": ("string")
    },
    "last_command_result": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "last_command_result",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "last_loaded_script_file": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "last_loaded_script_file",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "locale_i_d": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "locale_i_d",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "ortho": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "ortho",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "osnap": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "osnap",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "osnap_dialog": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "osnap_dialog",
        "method_parameters": (("visible","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "osnap_mode": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "osnap_mode",
        "method_parameters": (("mode","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "planar": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "planar",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "plug_ins": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "plug_ins",
        "method_parameters": (("types","int","OPT"),("status","int","OPT")),
        "method_returns": ("array","null")
    },
    "print_": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "print_",
        "method_parameters": (("message","str","OPT")),
        "method_returns": ()
    },
    "print_ex": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "print_ex",
        "method_parameters": (("message","str","OPT")),
        "method_returns": ()
    },
    "project_osnaps": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "project_osnaps",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "prompt": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "prompt",
        "method_parameters": (("prompt","str","OPT")),
        "method_returns": ()
    },
    "registry_key": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "registry_key",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "screen_size": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "screen_size",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "sdk_version": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "sdk_version",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "search_path_count": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "search_path_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "search_path_list": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "search_path_list",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "send_keystrokes": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "send_keystrokes",
        "method_parameters": (("keys","str","OPT"),("add_return","bln","OPT")),
        "method_returns": ()
    },
    "snap": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "snap",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "startup_script_count": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "startup_script_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "startup_script_list": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "startup_script_list",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "status_bar_distance": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_distance",
        "method_parameters": (("distance","dbl","OPT")),
        "method_returns": ()
    },
    "status_bar_message": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_message",
        "method_parameters": (("message","str","OPT")),
        "method_returns": ()
    },
    "status_bar_number": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_number",
        "method_parameters": (("number","dbl","OPT")),
        "method_returns": ()
    },
    "status_bar_point": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "status_bar_point",
        "method_parameters": (("point","arr_of_dbl","OPT")),
        "method_returns": ()
    },
    "template_file": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "template_file",
        "method_parameters": (("filename","str","OPT")),
        "method_returns": ("string","string")
    },
    "template_folder": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "template_folder",
        "method_parameters": (("folder","str","OPT")),
        "method_returns": ("string","string")
    },
    "window_handle": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "window_handle",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "working_folder": {
        "method_location": "Application",
        "method_type": "METHOD",
        "method_name": "working_folder",
        "method_parameters": (("enable","bln","OPT")),
        "method_returns": ("string","string")
    },
}
block = {
    "block_container_count": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_container_count",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("number","null")
    },
    "block_containers": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_containers",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("array","null")
    },
    "block_count": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_count",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "block_description": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_description",
        "method_parameters": (("block","str","REQ"),("text","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "block_instance_count": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_count",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("number","null")
    },
    "block_instance_insert_point": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_insert_point",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "block_instance_name": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_name",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("string","null")
    },
    "block_instance_xform": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_instance_xform",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "block_instances": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_instances",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("array","null")
    },
    "block_names": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_names",
        "method_parameters": (("sort","bln","OPT")),
        "method_returns": ("array","null")
    },
    "block_object_count": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_object_count",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("number","null")
    },
    "block_objects": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_objects",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("array","null")
    },
    "block_path": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_path",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("string","null")
    },
    "block_u_r_l": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_u_r_l",
        "method_parameters": (("block","str","REQ"),("u_r_l","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "block_u_r_l_tag": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "block_u_r_l_tag",
        "method_parameters": (("block","str","REQ"),("u_r_l","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "delete_block": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "delete_block",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "explode_block_instance": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "explode_block_instance",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "insert_block": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "insert_block",
        "method_parameters": (("name","str","REQ"),("point","arr_of_dbl","REQ"),("scale","arr_of_int","OPT"),("angle","dbl","OPT"),("normal","arr_of_dbl","OPT"),("xform","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "is_block": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "is_block",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_block_embedded": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_embedded",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_block_in_use": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_in_use",
        "method_parameters": (("block","str","REQ"),("where","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_block_instance": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_instance",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_block_reference": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "is_block_reference",
        "method_parameters": (("block","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "rename_block": {
        "method_location": "Block",
        "method_type": "METHOD",
        "method_name": "rename_block",
        "method_parameters": (("old_block","str","REQ"),("new_block","str","REQ")),
        "method_returns": ("string","null")
    },
}
curve = {
    "add_arc": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_arc",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("radius","dbl","REQ"),("angle","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_arc3_pt": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_arc3_pt",
        "method_parameters": (("start","arr_of_dbl","REQ"),("end","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_circle": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_circle",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("radius","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_circle3_pt": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_circle3_pt",
        "method_parameters": (("first","arr_of_dbl","REQ"),("second","arr_of_dbl","REQ"),("third","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_curve",
        "method_parameters": (("points","arr_of_dbl","REQ"),("degree","int","OPT")),
        "method_returns": ("string","null")
    },
    "add_ellipse": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_ellipse",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("x_radius","dbl","REQ"),("y_radius","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_ellipse3_pt": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_ellipse3_pt",
        "method_parameters": (("center","arr_of_dbl","REQ"),("second","arr_of_dbl","REQ"),("third","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_fillet_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_fillet_curve",
        "method_parameters": (("curve0","str","REQ"),("curve1","str","REQ"),("radius","dbl","OPT"),("point0","arr_of_dbl","OPT"),("point1","arr_of_dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_interp_crv_on_srf": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_interp_crv_on_srf",
        "method_parameters": (("object","str","REQ"),("points","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_interp_crv_on_srf_u_v": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_interp_crv_on_srf_u_v",
        "method_parameters": (("object","str","REQ"),("points","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_interp_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_interp_curve",
        "method_parameters": (("points","arr_of_dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("start_tan","arr_of_dbl","OPT"),("end_tan","arr_of_dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_interp_curve_ex": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_interp_curve_ex",
        "method_parameters": (("points","arr_of_dbl","REQ"),("degree","int","OPT"),("knot_style","int","OPT"),("sharp","bln","OPT"),("start_tangent","arr_of_dbl","OPT"),("end_tangent","arr_of_dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_line": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_line",
        "method_parameters": (("start","arr_of_dbl","REQ"),("end","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_nurbs_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_nurbs_curve",
        "method_parameters": (("points","arr_of_dbl","REQ"),("knots","arr_of_int","REQ"),("degree","int","REQ"),("weights","arr_of_int","OPT")),
        "method_returns": ("string","null")
    },
    "add_polyline": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_polyline",
        "method_parameters": (("points","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_sub_crv": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "add_sub_crv",
        "method_parameters": (("object","str","REQ"),("param0","dbl","REQ"),("param1","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "arc_angle": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_angle",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "arc_center_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_center_point",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("null")
    },
    "arc_mid_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_mid_point",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("null")
    },
    "arc_radius": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "arc_radius",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "circle_center_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "circle_center_point",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "circle_circumference": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "circle_circumference",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "circle_radius": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "circle_radius",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "close_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "close_curve",
        "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("string","null")
    },
    "convert_curve_to_polyline": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "convert_curve_to_polyline",
        "method_parameters": (("object","str","REQ"),("angle_tolerance","dbl","OPT"),("tolerance","dbl","OPT"),("delete_input","bln","OPT")),
        "method_returns": ("string","null")
    },
    "curve_arc_length_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_arc_length_point",
        "method_parameters": (("object","str","REQ"),("length","dbl","REQ"),("from_start","bln","OPT")),
        "method_returns": ("array","null")
    },
    "curve_area": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_area",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("array","number","number","null")
    },
    "curve_area_centroid": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_area_centroid",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("array","null")
    },
    "curve_arrows": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_arrows",
        "method_parameters": (("object","str","REQ"),("style","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "curve_boolean_difference": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_boolean_difference",
        "method_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
        "method_returns": ("array","null")
    },
    "curve_boolean_intersection": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_boolean_intersection",
        "method_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
        "method_returns": ("array","null")
    },
    "curve_boolean_union": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_boolean_union",
        "method_parameters": (("curves","arr_of_str","REQ")),
        "method_returns": ("array","null")
    },
    "curve_brep_intersect": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_brep_intersect",
        "method_parameters": (("curve","str","REQ"),("brep","str","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "curve_closest_object": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_closest_object",
        "method_parameters": (("curve","str","REQ"),("objects","arr_of_str","REQ")),
        "method_returns": ("array","string","array","array","null")
    },
    "curve_closest_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_closest_point",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "curve_contour_points": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_contour_points",
        "method_parameters": (("object","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("interval","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "curve_curvature": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_curvature",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
        "method_returns": ("array","number","null")
    },
    "curve_curve_intersection": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_curve_intersection",
        "method_parameters": (("object1","str","REQ"),("object2","str","OPT"),("tolerance","dbl","OPT")),
        "method_returns": ("array","number","number","number","number","number","null")
    },
    "curve_degree": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_degree",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "curve_deviation": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_deviation",
        "method_parameters": (("curve_a","str","REQ"),("curve_b","str","REQ")),
        "method_returns": ("array","number","number","number","number","number","number","null")
    },
    "curve_dim": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_dim",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "curve_directions_match": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_directions_match",
        "method_parameters": (("curve1","str","REQ"),("curve2","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "curve_discontinuity": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_discontinuity",
        "method_parameters": (("object","str","REQ"),("style","int","REQ")),
        "method_returns": ("array","null")
    },
    "curve_domain": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_domain",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "curve_edit_points": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_edit_points",
        "method_parameters": (("object","str","REQ"),("return_parameters","bln","OPT"),("index","int","OPT")),
        "method_returns": ("array","array","null")
    },
    "curve_end_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_end_point",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "curve_evaluate": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_evaluate",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("derivative","int","REQ")),
        "method_returns": ("array","array","array","array","array","null")
    },
    "curve_fillet_points": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_fillet_points",
        "method_parameters": (("curve0","str","REQ"),("curve1","str","REQ"),("radius","dbl","OPT"),("base_point0","arr_of_dbl","OPT"),("base_point1","arr_of_dbl","OPT")),
        "method_returns": ("array","string","null")
    },
    "curve_frame": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_frame",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "curve_knot_count": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_knot_count",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "curve_knots": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_knots",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "curve_length": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_length",
        "method_parameters": (("object","str","REQ"),("index","int","OPT"),("sub_domain","arr_of_int","OPT")),
        "method_returns": ("number","null")
    },
    "curve_mid_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_mid_point",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "curve_normal": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_normal",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "curve_perp_frame": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_perp_frame",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "curve_plane": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_plane",
        "method_parameters": (("curve","str","REQ")),
        "method_returns": ("array","null")
    },
    "curve_point_count": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_point_count",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "curve_points": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_points",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "curve_radius": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_radius",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "curve_seam": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_seam",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "curve_start_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_start_point",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "curve_surface_intersection": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_surface_intersection",
        "method_parameters": (("curve","str","REQ"),("surface","str","REQ"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT")),
        "method_returns": ("array","number","number","number","number","number","number","number","null")
    },
    "curve_tangent": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_tangent",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "curve_weights": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "curve_weights",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "divide_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "divide_curve",
        "method_parameters": (("object","str","REQ"),("segments","lng","REQ"),("create","bln","OPT"),("points","bln","OPT")),
        "method_returns": ("array","array","null")
    },
    "divide_curve_equidistant": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "divide_curve_equidistant",
        "method_parameters": (("object","str","REQ"),("distance","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT")),
        "method_returns": ("array","array","null")
    },
    "divide_curve_length": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "divide_curve_length",
        "method_parameters": (("object","str","REQ"),("length","dbl","REQ"),("create","bln","OPT"),("points","bln","OPT")),
        "method_returns": ("array","array","null")
    },
    "ellipse_center_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "ellipse_center_point",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "ellipse_quad_points": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "ellipse_quad_points",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "evaluate_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "evaluate_curve",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "explode_curves": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "explode_curves",
        "method_parameters": (("objects","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "extend_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "extend_curve",
        "method_parameters": (("object","str","REQ"),("type","int","REQ"),("side","int","REQ"),("objects","arr_of_str","REQ")),
        "method_returns": ("string","null")
    },
    "extend_curve_length": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "extend_curve_length",
        "method_parameters": (("object","str","REQ"),("type","int","REQ"),("side","int","REQ"),("length","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "extend_curve_point": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "extend_curve_point",
        "method_parameters": (("object","str","REQ"),("side","int","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "fair_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "fair_curve",
        "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "fit_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "fit_curve",
        "method_parameters": (("object","str","REQ"),("degree","int","OPT"),("tolerance","dbl","OPT"),("angle_tolerance","dbl","OPT")),
        "method_returns": ("string","null")
    },
    "insert_curve_knot": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "insert_curve_knot",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("symmetrical","bln","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_arc": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_arc",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_circle": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_circle",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve_closable": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_closable",
        "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve_closed": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_closed",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve_in_plane": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_in_plane",
        "method_parameters": (("object","str","REQ"),("plane","arr_of_dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve_linear": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_linear",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve_periodic": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_periodic",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve_planar": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_planar",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_curve_rational": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_curve_rational",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_ellipse": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_ellipse",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_line": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_line",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_point_on_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_point_on_curve",
        "method_parameters": (("object","str","REQ"),("point","arr_of_int","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_poly_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_poly_curve",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_polyline": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "is_polyline",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "join_curves": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "join_curves",
        "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "line_fit_from_points": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "line_fit_from_points",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "make_curve_non_periodic": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "make_curve_non_periodic",
        "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("string","string","null")
    },
    "make_curve_periodic": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "make_curve_periodic",
        "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("string","string","null")
    },
    "mesh_polyline": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "mesh_polyline",
        "method_parameters": (("polyline","str","REQ")),
        "method_returns": ("string","null")
    },
    "offset_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "offset_curve",
        "method_parameters": (("object","str","REQ"),("direction","arr_of_dbl","REQ"),("distance","dbl","REQ"),("normal","arr_of_dbl","OPT"),("style","int","OPT")),
        "method_returns": ("array","null")
    },
    "offset_curve_on_surface": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "offset_curve_on_surface",
        "method_parameters": (("curve","str","REQ"),("surface","str","REQ"),("distance","dbl","REQ"),("parameter","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "planar_closed_curve_containment": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "planar_closed_curve_containment",
        "method_parameters": (("curve1","str","REQ"),("curve2","str","REQ"),("plane","arr_of_dbl","OPT"),("tolerance","dbl","OPT")),
        "method_returns": ("number","null")
    },
    "planar_curve_collision": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "planar_curve_collision",
        "method_parameters": (("curve1","str","REQ"),("curve2","str","REQ"),("plane","arr_of_dbl","OPT"),("tolerance","dbl","OPT")),
        "method_returns": ("null")
    },
    "point_in_planar_closed_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "point_in_planar_closed_curve",
        "method_parameters": (("point","arr_of_dbl","REQ"),("curve","str","REQ"),("plane","arr_of_dbl","OPT"),("tolerance","dbl","OPT")),
        "method_returns": ("number","null")
    },
    "poly_curve_count": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "poly_curve_count",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("number","null")
    },
    "polyline_vertices": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "polyline_vertices",
        "method_parameters": (("object","str","REQ"),("index","int","OPT")),
        "method_returns": ("array","null")
    },
    "project_curve_to_mesh": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "project_curve_to_mesh",
        "method_parameters": (("curves","arr_of_str","REQ"),("meshes","arr_of_str","REQ"),("direction","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "project_curve_to_surface": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "project_curve_to_surface",
        "method_parameters": (("curves","arr_of_str","REQ"),("surfaces","arr_of_str","REQ"),("direction","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "rebuild_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "rebuild_curve",
        "method_parameters": (("object","str","REQ"),("degree","int","OPT"),("point_count","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "remove_curve_knot": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "remove_curve_knot",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "reverse_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "reverse_curve",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "simplify_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "simplify_curve",
        "method_parameters": (("object","str","REQ"),("flags","int","OPT")),
        "method_returns": ("boolean","null")
    },
    "split_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "split_curve",
        "method_parameters": (("object","str","REQ"),("parameters","arr_of_dbl","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "trim_curve": {
        "method_location": "Curve",
        "method_type": "METHOD",
        "method_name": "trim_curve",
        "method_parameters": (("object","str","REQ"),("interval","arr_of_int","REQ"),("delete","bln","OPT")),
        "method_returns": ("string","null")
    },
}
dimension = {
    "add_dim_style": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "add_dim_style",
        "method_parameters": (("dim_style","str","OPT")),
        "method_returns": ("string","null")
    },
    "add_leader": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "add_leader",
        "method_parameters": (("points","arr_of_dbl","REQ"),("view","str","OPT"),("text","str","OPT")),
        "method_returns": ("string","null")
    },
    "current_dim_style": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "current_dim_style",
        "method_parameters": (("dim_style","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "delete_dim_style": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "delete_dim_style",
        "method_parameters": (("dim_style","str","REQ")),
        "method_returns": ("string","null")
    },
    "dim_scale": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_scale",
        "method_parameters": (("scale","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_angle_precision": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_angle_precision",
        "method_parameters": (("dim_style","str","REQ"),("precision","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_arrow_size": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_arrow_size",
        "method_parameters": (("dim_style","str","REQ"),("size","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_count": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "dim_style_extension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_extension",
        "method_parameters": (("dim_style","str","REQ"),("extension","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_font": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_font",
        "method_parameters": (("dim_style","str","REQ"),("font","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "dim_style_leader_arrow_size": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_leader_arrow_size",
        "method_parameters": (("dim_style","str","REQ"),("size","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_linear_precision": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_linear_precision",
        "method_parameters": (("dim_style","str","REQ"),("precision","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_names": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_names",
        "method_parameters": (("sort","bln","OPT")),
        "method_returns": ("array","null")
    },
    "dim_style_number_format": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_number_format",
        "method_parameters": (("dim_style","str","REQ"),("format","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_offset": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_offset",
        "method_parameters": (("dim_style","str","REQ"),("offset","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_text_alignment": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_text_alignment",
        "method_parameters": (("dim_style","str","REQ"),("alignment","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_text_gap": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_text_gap",
        "method_parameters": (("dim_style","str","REQ"),("gap","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "dim_style_text_height": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dim_style_text_height",
        "method_parameters": (("dim_style","str","REQ"),("height","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "dimension_style": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_style",
        "method_parameters": (("object","str","REQ"),("style","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "dimension_text": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_text",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("string","null")
    },
    "dimension_user_text": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_user_text",
        "method_parameters": (("object","str","REQ"),("user_text","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "dimension_value": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "dimension_value",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "is_aligned_dimension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_aligned_dimension",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_angular_dimension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_angular_dimension",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_diameter_dimension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_diameter_dimension",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_dim_style": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_dim_style",
        "method_parameters": (("dim_style","str","REQ")),
        "method_returns": ("null")
    },
    "is_dim_style_reference": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_dim_style_reference",
        "method_parameters": (("dim_style","str","REQ")),
        "method_returns": ("null")
    },
    "is_dimension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_dimension",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_leader": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_leader",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_linear_dimension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_linear_dimension",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_ordinate_dimension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_ordinate_dimension",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_radial_dimension": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "is_radial_dimension",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "leader_text": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "leader_text",
        "method_parameters": (("object","str","REQ"),("text","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "rename_dim_style": {
        "method_location": "Dimension",
        "method_type": "METHOD",
        "method_name": "rename_dim_style",
        "method_parameters": (("old_style","str","REQ"),("new_style","str","REQ")),
        "method_returns": ("string","null")
    },
}
document = {
    "create_preview_image": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "create_preview_image",
        "method_parameters": (("file","str","REQ"),("view","str","OPT"),("size","arr_of_int","OPT"),("flags","int","OPT"),("wireframe","bln","OPT")),
        "method_returns": ("boolean")
    },
    "document_modified": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "document_modified",
        "method_parameters": (("modified","bln","OPT")),
        "method_returns": ("boolean","boolean")
    },
    "document_name": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "document_name",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "document_path": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "document_path",
        "method_parameters": (),
        "method_returns": ("string","null")
    },
    "document_u_r_l": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "document_u_r_l",
        "method_parameters": (("u_r_l","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "enable_redraw": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "enable_redraw",
        "method_parameters": (("select","bln","OPT")),
        "method_returns": ("boolean")
    },
    "extract_preview_image": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "extract_preview_image",
        "method_parameters": (("file_name","str","REQ"),("model_name","str","OPT")),
        "method_returns": ("boolean")
    },
    "is_document_modified": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "is_document_modified",
        "method_parameters": (),
        "method_returns": ("boolean")
    },
    "notes": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "notes",
        "method_parameters": (("notes","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "read_file_version": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "read_file_version",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "redraw": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "redraw",
        "method_parameters": (),
        "method_returns": ()
    },
    "render_antialias": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_antialias",
        "method_parameters": (("style","int","OPT")),
        "method_returns": ("number","number","number")
    },
    "render_color": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_color",
        "method_parameters": (("item","int","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_density": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_density",
        "method_parameters": (("density","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_angle": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_angle",
        "method_parameters": (("angle","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_aspect_ratio": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_aspect_ratio",
        "method_parameters": (("ratio","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_dist_edge_to_srf": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_dist_edge_to_srf",
        "method_parameters": (("distance","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_max_edge_length": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_max_edge_length",
        "method_parameters": (("length","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_min_edge_length": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_min_edge_length",
        "method_parameters": (("length","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_min_initial_grid_quads": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_min_initial_grid_quads",
        "method_parameters": (("quads","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_quality": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_quality",
        "method_parameters": (("quality","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_mesh_settings": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_mesh_settings",
        "method_parameters": (("settings","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "render_resolution": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_resolution",
        "method_parameters": (("resolution","arr_of_int","REQ")),
        "method_returns": ("array","array","null")
    },
    "render_settings": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "render_settings",
        "method_parameters": (("settings","int","OPT")),
        "method_returns": ("number","number","number")
    },
    "unit_absolute_tolerance": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_absolute_tolerance",
        "method_parameters": (("abs_tol","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "unit_angle_tolerance": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_angle_tolerance",
        "method_parameters": (("angle_tol","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "unit_custom_unit_system": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_custom_unit_system",
        "method_parameters": (("units","dbl","REQ"),("scale","bln","OPT"),("name","str","OPT")),
        "method_returns": ("number","null")
    },
    "unit_distance_display_mode": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_distance_display_mode",
        "method_parameters": (("mode","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "unit_distance_display_precision": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_distance_display_precision",
        "method_parameters": (("precision","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "unit_relative_tolerance": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_relative_tolerance",
        "method_parameters": (("rel_tol","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "unit_scale": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_scale",
        "method_parameters": (("to_system","int","REQ"),("from_system","int","OPT")),
        "method_returns": ("number","null")
    },
    "unit_system": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_system",
        "method_parameters": (("system","int","OPT"),("scale","bln","OPT")),
        "method_returns": ("number","null")
    },
    "unit_system_name": {
        "method_location": "Document",
        "method_type": "METHOD",
        "method_name": "unit_system_name",
        "method_parameters": (("capitalize","bln","OPT"),("singular","bln","OPT"),("abbreviate","bln","OPT")),
        "method_returns": ("string")
    },
}
geometry = {
    "add_clipping_plane": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_clipping_plane",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ"),("views","arr_of_str","OPT")),
        "method_returns": ("string","null")
    },
    "add_point_cloud": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_point_cloud",
        "method_parameters": (("points","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_points": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_points",
        "method_parameters": (("points","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "add_text": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_text",
        "method_parameters": (("text","str","REQ"),("point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("height","dbl","OPT"),("font","str","OPT"),("style","int","OPT")),
        "method_returns": ("string","null")
    },
    "add_text_dot": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "add_text_dot",
        "method_parameters": (("test","str","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "bounding_box": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "bounding_box",
        "method_parameters": (("objects","arr_of_str","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
        "method_returns": ("array","null")
    },
    "compare_geometry": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "compare_geometry",
        "method_parameters": (("object1","str","REQ"),("object2","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_clipping_plane": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_clipping_plane",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_point": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_point",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_point_cloud": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_point_cloud",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_text": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_text",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_text_dot": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "is_text_dot",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "point_cloud_count": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "point_cloud_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "point_cloud_points": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "point_cloud_points",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "point_coordinates": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "point_coordinates",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "text_dot_point": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_dot_point",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "text_dot_text": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_dot_text",
        "method_parameters": (("object","str","REQ"),("text","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "text_object_font": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_font",
        "method_parameters": (("object","str","REQ"),("font","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "text_object_height": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_height",
        "method_parameters": (("object","str","REQ"),("height","dbl","OPT")),
        "method_returns": ("string","string","null")
    },
    "text_object_plane": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_plane",
        "method_parameters": (("object","str","REQ"),("plane","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "text_object_point": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_point",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","OPT")),
        "method_returns": ("string","string","null")
    },
    "text_object_style": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_style",
        "method_parameters": (("object","str","REQ"),("style","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "text_object_text": {
        "method_location": "Geometry",
        "method_type": "METHOD",
        "method_name": "text_object_text",
        "method_parameters": (("object","str","REQ"),("text","str","OPT")),
        "method_returns": ("string","string","null")
    },
}
group = {
    "add_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "add_group",
        "method_parameters": (("group","str","OPT")),
        "method_returns": ("string","null")
    },
    "add_object_to_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "add_object_to_group",
        "method_parameters": (("object","str","REQ"),("group","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "add_objects_to_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "add_objects_to_group",
        "method_parameters": (("objects","arr_of_str","REQ"),("group","str","REQ")),
        "method_returns": ("number","null")
    },
    "delete_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "delete_group",
        "method_parameters": (("group","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "group_count": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "group_count",
        "method_parameters": (),
        "method_returns": ("number","null")
    },
    "group_names": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "group_names",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "hide_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "hide_group",
        "method_parameters": (("group","str","REQ")),
        "method_returns": ("number","null")
    },
    "is_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "is_group",
        "method_parameters": (("group","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_group_empty": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "is_group_empty",
        "method_parameters": (("group","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "lock_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "lock_group",
        "method_parameters": (("group","str","REQ")),
        "method_returns": ("number","null")
    },
    "remove_object_from_all_groups": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "remove_object_from_all_groups",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "remove_object_from_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "remove_object_from_group",
        "method_parameters": (("object","str","REQ"),("group","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "remove_object_from_top_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "remove_object_from_top_group",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "remove_objects_from_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "remove_objects_from_group",
        "method_parameters": (("objects","arr_of_str","REQ"),("group","str","REQ")),
        "method_returns": ("number","null")
    },
    "rename_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "rename_group",
        "method_parameters": (("old_group","str","REQ"),("new_group","str","REQ")),
        "method_returns": ("string","null")
    },
    "show_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "show_group",
        "method_parameters": (("group","str","REQ")),
        "method_returns": ("number","null")
    },
    "unlock_group": {
        "method_location": "Group",
        "method_type": "METHOD",
        "method_name": "unlock_group",
        "method_parameters": (("group","str","REQ")),
        "method_returns": ("number","null")
    },
}
hatch = {
    "add_hatch": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "add_hatch",
        "method_parameters": (("curve","str","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_hatch_patterns": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "add_hatch_patterns",
        "method_parameters": (("file_name","str","REQ"),("replace","bln","OPT")),
        "method_returns": ("array","null")
    },
    "add_hatches": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "add_hatches",
        "method_parameters": (("curves","arr_of_str","REQ"),("hatch","str","OPT"),("scale","dbl","OPT"),("rotation","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "current_hatch_pattern": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "current_hatch_pattern",
        "method_parameters": (("hatch","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "explode_hatch": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "explode_hatch",
        "method_parameters": (("hatch","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "hatch_pattern": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern",
        "method_parameters": (("object","str","REQ"),("hatch","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "hatch_pattern_count": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "hatch_pattern_description": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_description",
        "method_parameters": (("hatch","str","REQ")),
        "method_returns": ("string","null")
    },
    "hatch_pattern_fill_type": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_fill_type",
        "method_parameters": (("hatch","str","REQ")),
        "method_returns": ("number","null")
    },
    "hatch_pattern_names": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_pattern_names",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "hatch_rotation": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_rotation",
        "method_parameters": (("object","str","REQ"),("rotation","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "hatch_scale": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "hatch_scale",
        "method_parameters": (("object","str","REQ"),("scale","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "is_hatch": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_hatch_pattern": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch_pattern",
        "method_parameters": (("hatch","str","REQ")),
        "method_returns": ("null")
    },
    "is_hatch_pattern_current": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch_pattern_current",
        "method_parameters": (("hatch","str","REQ")),
        "method_returns": ("null")
    },
    "is_hatch_pattern_reference": {
        "method_location": "Hatch",
        "method_type": "METHOD",
        "method_name": "is_hatch_pattern_reference",
        "method_parameters": (("hatch","str","REQ")),
        "method_returns": ("null")
    },
}
layer = {
    "add_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "add_layer",
        "method_parameters": (("layer","str","OPT"),("color","lng","OPT"),("visible","bln","OPT"),("locked","bln","OPT"),("parent","str","OPT")),
        "method_returns": ("string","null")
    },
    "current_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "current_layer",
        "method_parameters": (("layer","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "delete_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "delete_layer",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "expand_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "expand_layer",
        "method_parameters": (("layer","str","REQ"),("expand","bln","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_changeable": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_changeable",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_child_of": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_child_of",
        "method_parameters": (("layer","str","REQ"),("test","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_layer_current": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_current",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_empty": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_empty",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_expanded": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_expanded",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_layer_locked": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_locked",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_on": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_on",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_parent_of": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_parent_of",
        "method_parameters": (("layer","str","REQ"),("test","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_layer_reference": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_reference",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_selectable": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_selectable",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "is_layer_visible": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "is_layer_visible",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("null")
    },
    "layer_child_count": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_child_count",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("number","null")
    },
    "layer_children": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_children",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("array","null")
    },
    "layer_color": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_color",
        "method_parameters": (("layer","str","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "layer_count": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "layer_linetype": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_linetype",
        "method_parameters": (("layer","str","REQ"),("linetype","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "layer_locked": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_locked",
        "method_parameters": (("layer","str","REQ"),("visible","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "layer_material_index": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_material_index",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("number","null")
    },
    "layer_mode": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_mode",
        "method_parameters": (("layer","str","REQ"),("mode","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "layer_names": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_names",
        "method_parameters": (("sort","bln","OPT")),
        "method_returns": ("array","null")
    },
    "layer_order": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_order",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("number","null")
    },
    "layer_print_color": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_print_color",
        "method_parameters": (("layer","str","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "layer_print_width": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_print_width",
        "method_parameters": (("layer","str","REQ"),("width","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "layer_visible": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "layer_visible",
        "method_parameters": (("layer","str","REQ"),("visible","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "parent_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "parent_layer",
        "method_parameters": (("layer","str","REQ"),("parent","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "purge_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "purge_layer",
        "method_parameters": (("layer","str","REQ")),
        "method_returns": ("string","null")
    },
    "rename_layer": {
        "method_location": "Layer",
        "method_type": "METHOD",
        "method_name": "rename_layer",
        "method_parameters": (("old_name","str","REQ"),("new_name","str","REQ")),
        "method_returns": ("string","null")
    },
}
light = {
    "add_directional_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "add_directional_light",
        "method_parameters": (("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_linear_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "add_linear_light",
        "method_parameters": (("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("width","dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_point_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "add_point_light",
        "method_parameters": (("point","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_rectangular_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "add_rectangular_light",
        "method_parameters": (("origin","arr_of_dbl","REQ"),("width","arr_of_dbl","REQ"),("height","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_spot_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "add_spot_light",
        "method_parameters": (("origin","arr_of_dbl","REQ"),("radius","dbl","REQ"),("apex","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "enable_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "enable_light",
        "method_parameters": (("object","str","REQ"),("enable","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "is_directional_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_directional_light",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_light",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_light_enabled": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_light_enabled",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_light_reference": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_light_reference",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_linear_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_linear_light",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_point_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_point_light",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_rectangular_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_rectangular_light",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_spot_light": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "is_spot_light",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "light_color": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "light_color",
        "method_parameters": (("object","str","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "light_count": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "light_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "light_direction": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "light_direction",
        "method_parameters": (("object","str","REQ"),("direction","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "light_location": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "light_location",
        "method_parameters": (("object","str","REQ"),("location","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "light_name": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "light_name",
        "method_parameters": (("object","str","REQ"),("name","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "light_objects": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "light_objects",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "rectangular_light_plane": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "rectangular_light_plane",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","array","array","array","array","null")
    },
    "spot_light_hardness": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "spot_light_hardness",
        "method_parameters": (("object","str","REQ"),("hardness","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "spot_light_radius": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "spot_light_radius",
        "method_parameters": (("object","str","REQ"),("radius","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "spot_light_shadow_intensity": {
        "method_location": "Light",
        "method_type": "METHOD",
        "method_name": "spot_light_shadow_intensity",
        "method_parameters": (("object","str","REQ"),("intensity","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
}
line_and_plane = {
    "distance_to_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "distance_to_plane",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("number","null")
    },
    "evaluate_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "evaluate_plane",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("parameter","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "intersect_planes": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "intersect_planes",
        "method_parameters": (("plane1","arr_of_dbl","REQ"),("plane2","arr_of_dbl","REQ"),("plane3","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "line_closest_point": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_closest_point",
        "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "line_is_farther_than": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_is_farther_than",
        "method_parameters": (("line","arr_of_dbl","REQ"),("distance","dbl","REQ"),("point","arr_of_dbl","REQ"),("line2","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "line_line_intersection": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_line_intersection",
        "method_parameters": (("line_a","arr_of_dbl","REQ"),("line_b","arr_of_dbl","REQ"),("planar","bln","OPT")),
        "method_returns": ("array","array","null")
    },
    "line_max_distance_to": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_max_distance_to",
        "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("line2","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "line_min_distance_to": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_min_distance_to",
        "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("line2","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "line_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_plane",
        "method_parameters": (("line","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "line_plane_intersection": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_plane_intersection",
        "method_parameters": (("line","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "line_transform": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "line_transform",
        "method_parameters": (("line","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "move_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "move_plane",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("origin","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "plane_closest_point": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_closest_point",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("return_point","bln","OPT")),
        "method_returns": ("array","null")
    },
    "plane_equation": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_equation",
        "method_parameters": (("plane","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "plane_fit_from_points": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_fit_from_points",
        "method_parameters": (("points","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "plane_from_frame": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_from_frame",
        "method_parameters": (("origin","arr_of_dbl","REQ"),("xaxis","arr_of_dbl","REQ"),("yaxis","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "plane_from_normal": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_from_normal",
        "method_parameters": (("origin","arr_of_dbl","REQ"),("normal","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "plane_from_points": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_from_points",
        "method_parameters": (("origin","arr_of_dbl","REQ"),("point_x","arr_of_dbl","REQ"),("point_y","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "plane_plane_intersection": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_plane_intersection",
        "method_parameters": (("plane1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "plane_transform": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "plane_transform",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "rotate_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "rotate_plane",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("angle","dbl","REQ"),("axis","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "world_x_y_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "world_x_y_plane",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "world_y_z_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "world_y_z_plane",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "world_z_x_plane": {
        "method_location": "Line_and_Plane",
        "method_type": "METHOD",
        "method_name": "world_z_x_plane",
        "method_parameters": (),
        "method_returns": ("array")
    },
}
linetype = {
    "is_linetype": {
        "method_location": "Linetype",
        "method_type": "METHOD",
        "method_name": "is_linetype",
        "method_parameters": (("linetype","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_linetype_reference": {
        "method_location": "Linetype",
        "method_type": "METHOD",
        "method_name": "is_linetype_reference",
        "method_parameters": (("linetype","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "linetype_count": {
        "method_location": "Linetype",
        "method_type": "METHOD",
        "method_name": "linetype_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "linetype_names": {
        "method_location": "Linetype",
        "method_type": "METHOD",
        "method_name": "linetype_names",
        "method_parameters": (("sort","bln","OPT")),
        "method_returns": ("array","null")
    },
}
material = {
    "add_material_to_layer": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "add_material_to_layer",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "add_material_to_object": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "add_material_to_object",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "copy_material": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "copy_material",
        "method_parameters": (("src_index","int","REQ"),("dst_index","int","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_material_default": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "is_material_default",
        "method_parameters": (("material_index","int","REQ")),
        "method_returns": ("null")
    },
    "is_material_reference": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "is_material_reference",
        "method_parameters": (("material_index","int","REQ")),
        "method_returns": ("boolean","null")
    },
    "match_material": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "match_material",
        "method_parameters": (("src_material_index","int","REQ"),("src_object","str","REQ"),("dest_objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
    "material_bump": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_bump",
        "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "material_color": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_color",
        "method_parameters": (("material_index","int","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "material_environment_map": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_environment_map",
        "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "material_name": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_name",
        "method_parameters": (("material_index","int","REQ"),("name","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "material_reflective_color": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_reflective_color",
        "method_parameters": (("material_index","int","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","null")
    },
    "material_shine": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_shine",
        "method_parameters": (("material_index","int","REQ"),("shine","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "material_texture": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_texture",
        "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "material_transparency": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_transparency",
        "method_parameters": (("material_index","int","REQ"),("transparency","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "material_transparency_map": {
        "method_location": "Material",
        "method_type": "METHOD",
        "method_name": "material_transparency_map",
        "method_parameters": (("material_index","int","REQ"),("file_name","str","OPT")),
        "method_returns": ("string","string","null")
    },
}
math = {
    "angle": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "angle",
        "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ"),("world","bln","OPT")),
        "method_returns": ("array","null")
    },
    "angle2": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "angle2",
        "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "deviation": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "deviation",
        "method_parameters": (("numbers","arr_of_int","REQ")),
        "method_returns": ("number","null")
    },
    "distance": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "distance",
        "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ"),("point_array","arr_of_dbl","REQ")),
        "method_returns": ("number","array","null")
    },
    "hypot": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "hypot",
        "method_parameters": (("number_x","dbl","REQ"),("number_y","dbl","REQ")),
        "method_returns": ("number","null")
    },
    "max": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "max",
        "method_parameters": (("numbers","arr_of_int","REQ")),
        "method_returns": ("number","null")
    },
    "mean": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "mean",
        "method_parameters": (("numbers","arr_of_int","REQ")),
        "method_returns": ("number","null")
    },
    "median": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "median",
        "method_parameters": (("numbers","arr_of_int","REQ")),
        "method_returns": ("number","null")
    },
    "min": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "min",
        "method_parameters": (("numbers","arr_of_int","REQ")),
        "method_returns": ("number","null")
    },
    "polar": {
        "method_location": "Math",
        "method_type": "METHOD",
        "method_name": "polar",
        "method_parameters": (("point","arr_of_dbl","REQ"),("angle","dbl","REQ"),("distance","dbl","REQ"),("plane","arr_of_dbl","OPT")),
        "method_returns": ("array","null")
    },
}
mesh = {
    "add_mesh": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "add_mesh",
        "method_parameters": (("vertices","arr_of_dbl","REQ"),("face_vertices","arr_of_int","REQ"),("vertex_normals","arr_of_dbl","OPT"),("texture_coordinates","arr_of_dbl","OPT"),("vertex_colors","arr_of_int","OPT")),
        "method_returns": ("string","null")
    },
    "add_planar_mesh": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "add_planar_mesh",
        "method_parameters": (("object","str","REQ"),("delete","bln","REQ")),
        "method_returns": ("string","null")
    },
    "curve_mesh_intersection": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "curve_mesh_intersection",
        "method_parameters": (("curve","str","REQ"),("mesh","str","REQ"),("return_faces","bln","OPT")),
        "method_returns": ("array","array","array","number","null")
    },
    "disjoint_mesh_count": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "disjoint_mesh_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "duplicate_mesh_border": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "duplicate_mesh_border",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "explode_meshes": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "explode_meshes",
        "method_parameters": (("objects","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "is_mesh": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "is_mesh",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_mesh_closed": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "is_mesh_closed",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_mesh_manifold": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "is_mesh_manifold",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "mesh_area": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_area",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("array","number","number","number","null")
    },
    "mesh_area_centroid": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_area_centroid",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_difference": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_difference",
        "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_intersection": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_intersection",
        "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_split": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_split",
        "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "mesh_boolean_union": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_boolean_union",
        "method_parameters": (("input","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "mesh_closest_point": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_closest_point",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("array","array","number","null")
    },
    "mesh_contour_points": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_contour_points",
        "method_parameters": (("object","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("interval","dbl","OPT"),("remove_coincident_points","bln","OPT")),
        "method_returns": ("array","null")
    },
    "mesh_face_centers": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_centers",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_face_count": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "mesh_face_normals": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_normals",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_face_vertices": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_face_vertices",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_faces": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_faces",
        "method_parameters": (("object","str","REQ"),("face_type","bln","OPT")),
        "method_returns": ("array","null")
    },
    "mesh_has_face_normals": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_face_normals",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "mesh_has_texture_coordinates": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_texture_coordinates",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "mesh_has_vertex_colors": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_vertex_colors",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "mesh_has_vertex_normals": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_has_vertex_normals",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "mesh_mesh_intersection": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_mesh_intersection",
        "method_parameters": (("mesh1","str","REQ"),("mesh2","str","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "mesh_naked_edge_points": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_naked_edge_points",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_offset": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_offset",
        "method_parameters": (("mesh","str","REQ"),("distance","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "mesh_quad_count": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_quad_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "mesh_quads_to_triangles": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_quads_to_triangles",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "mesh_texture_coordinates": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_texture_coordinates",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_triangle_count": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_triangle_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "mesh_vertex_colors": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertex_colors",
        "method_parameters": (("object","str","REQ"),("vertex_colors","arr_of_int","OPT")),
        "method_returns": ("array","array","null")
    },
    "mesh_vertex_count": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertex_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "mesh_vertex_normals": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertex_normals",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_vertices": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_vertices",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "mesh_volume": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_volume",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("array","number","number","number","null")
    },
    "mesh_volume_centroid": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "mesh_volume_centroid",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "pull_curve_to_mesh": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "pull_curve_to_mesh",
        "method_parameters": (("mesh","str","REQ"),("curve","str","REQ")),
        "method_returns": ("string","null")
    },
    "split_disjoint_mesh": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "split_disjoint_mesh",
        "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "unify_mesh_normals": {
        "method_location": "Mesh",
        "method_type": "METHOD",
        "method_name": "unify_mesh_normals",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
}
object = {
    "add_object_mesh": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "add_object_mesh",
        "method_parameters": (("object","str","REQ"),("quality","int","OPT"),("enable","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "box_morph_object": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "box_morph_object",
        "method_parameters": (("objects","arr_of_str","REQ"),("box_points","arr_of_dbl","REQ"),("copy","bln","OPT")),
        "method_returns": ("string","array","null")
    },
    "copy_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "copy_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("start","arr_of_dbl","OPT"),("end","arr_of_dbl","OPT"),("translation","arr_of_dbl","OPT")),
        "method_returns": ("array","null")
    },
    "delete_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "delete_objects",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
    "enable_object_mesh": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "enable_object_mesh",
        "method_parameters": (("objects","arr_of_str","REQ"),("enable","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "flash_object": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "flash_object",
        "method_parameters": (("objects","arr_of_str","REQ"),("style","bln","OPT")),
        "method_returns": ()
    },
    "hide_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "hide_objects",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
    "is_layout_object": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_layout_object",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ()
    },
    "is_object_hidden": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_hidden",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object_in_box": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_in_box",
        "method_parameters": (("object","str","REQ"),("box","arr_of_dbl","REQ"),("mode","bln","OPT")),
        "method_returns": ("null")
    },
    "is_object_in_group": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_in_group",
        "method_parameters": (("object","str","REQ"),("group","str","OPT")),
        "method_returns": ("null")
    },
    "is_object_locked": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_locked",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object_normal": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_normal",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object_reference": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_reference",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object_selectable": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_selectable",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object_selected": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_selected",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object_solid": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_solid",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_object_valid": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_object_valid",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("null")
    },
    "is_visible_in_view": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "is_visible_in_view",
        "method_parameters": (("object","str","REQ"),("view","str","OPT")),
        "method_returns": ("null")
    },
    "lock_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "lock_objects",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
    "match_object_attributes": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "match_object_attributes",
        "method_parameters": (("targets","arr_of_str","REQ"),("source","str","OPT")),
        "method_returns": ("number","null")
    },
    "mirror_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "mirror_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("start_pt","arr_of_dbl","REQ"),("end_pt","arr_of_dbl","REQ"),("copy","bln","OPT")),
        "method_returns": ("string","null")
    },
    "move_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "move_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("start","arr_of_dbl","REQ"),("end","arr_of_dbl","REQ"),("translation","arr_of_dbl","REQ")),
        "method_returns": ("number","null")
    },
    "object_color": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_color",
        "method_parameters": (("objects","arr_of_str","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_color_source": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_color_source",
        "method_parameters": (("objects","arr_of_str","REQ"),("source","int","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_description": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_description",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("string","null")
    },
    "object_dump": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_dump",
        "method_parameters": (("object","str","REQ"),("type","int","OPT")),
        "method_returns": ("string","null")
    },
    "object_groups": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_groups",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "object_has_mesh": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_has_mesh",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "object_layer": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_layer",
        "method_parameters": (("objects","arr_of_str","REQ"),("layer","str","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_layout": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_layout",
        "method_parameters": (("object","str","REQ"),("layout","str","OPT"),("return_name","bln","OPT")),
        "method_returns": ("string","string","null")
    },
    "object_linetype": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_linetype",
        "method_parameters": (("objects","arr_of_str","REQ"),("layer","str","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_linetype_source": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_linetype_source",
        "method_parameters": (("objects","arr_of_str","REQ"),("source","int","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_material_index": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_material_index",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "object_material_source": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_material_source",
        "method_parameters": (("objects","arr_of_str","REQ"),("source","int","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_mesh_density": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_density",
        "method_parameters": (("object","str","REQ"),("density","dbl","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_angle": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_angle",
        "method_parameters": (("object","str","REQ"),("angle","dbl","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_aspect_ratio": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_aspect_ratio",
        "method_parameters": (("object","str","REQ"),("ratio","dbl","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_dist_edge_to_srf": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_dist_edge_to_srf",
        "method_parameters": (("object","str","REQ"),("distance","dbl","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_max_edge_length": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_max_edge_length",
        "method_parameters": (("object","str","REQ"),("length","dbl","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_min_edge_length": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_min_edge_length",
        "method_parameters": (("object","str","REQ"),("length","dbl","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_min_initial_grid_quads": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_min_initial_grid_quads",
        "method_parameters": (("object","str","REQ"),("quads","int","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_quality": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_quality",
        "method_parameters": (("object","str","REQ"),("quality","int","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_mesh_settings": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_mesh_settings",
        "method_parameters": (("object","str","REQ"),("settings","int","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "object_names": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_names",
        "method_parameters": (("objects","arr_of_str","REQ"),("names","arr_of_str","OPT")),
        "method_returns": ("array","array","null")
    },
    "object_print_color": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_color",
        "method_parameters": (("objects","arr_of_str","REQ"),("color","lng","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_print_color_source": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_color_source",
        "method_parameters": (("objects","arr_of_str","REQ"),("source","int","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_print_width": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_width",
        "method_parameters": (("objects","arr_of_str","REQ"),("width","dbl","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_print_width_source": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_print_width_source",
        "method_parameters": (("objects","arr_of_str","REQ"),("source","int","OPT")),
        "method_returns": ("number","number","number","null")
    },
    "object_top_group": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_top_group",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("string","null")
    },
    "object_type": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_type",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "object_u_r_l": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "object_u_r_l",
        "method_parameters": (("objects","arr_of_str","REQ"),("u_r_l","str","OPT")),
        "method_returns": ("string","string","number","null")
    },
    "orient_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "orient_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("reference","arr_of_dbl","REQ"),("target","arr_of_dbl","REQ"),("flags","int","OPT")),
        "method_returns": ("array","null")
    },
    "remap_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "remap_objects",
        "method_parameters": (("object","arr_of_str","REQ"),("src_plane","arr_of_dbl","REQ"),("dst_plane","arr_of_dbl","REQ"),("copy","bln","OPT")),
        "method_returns": ("array","null")
    },
    "rotate_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "rotate_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("point","arr_of_dbl","REQ"),("angle","dbl","REQ"),("axis","arr_of_dbl","OPT"),("copy","bln","OPT")),
        "method_returns": ("string","null")
    },
    "scale_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "scale_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("origin","arr_of_dbl","REQ"),("scale","arr_of_dbl","REQ"),("copy","bln","OPT")),
        "method_returns": ("array","null")
    },
    "select_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "select_objects",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
    "shear_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "shear_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("origin","arr_of_dbl","REQ"),("ref_pt","arr_of_dbl","REQ"),("scale","arr_of_int","REQ"),("copy","bln","OPT")),
        "method_returns": ("array","null")
    },
    "show_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "show_objects",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
    "transform_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "transform_objects",
        "method_parameters": (("objects","arr_of_str","REQ"),("matrix","arr_of_str","REQ"),("copy","bln","OPT")),
        "method_returns": ("array","null")
    },
    "unlock_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "unlock_objects",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
    "unselect_objects": {
        "method_location": "Object",
        "method_type": "METHOD",
        "method_name": "unselect_objects",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("number","null")
    },
}
object_grip = {
    "enable_object_grips": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "enable_object_grips",
        "method_parameters": (("object","str","REQ"),("enable","bln","OPT")),
        "method_returns": ("boolean","null")
    },
    "get_object_grips": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "get_object_grips",
        "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
        "method_returns": ("array","string","number","array","null")
    },
    "next_object_grip": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "next_object_grip",
        "method_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
        "method_returns": ("number","null")
    },
    "object_grip_count": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grip_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "object_grip_locations": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grip_locations",
        "method_parameters": (("object","str","REQ"),("points","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "object_grips_on": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grips_on",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "object_grips_selected": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "object_grips_selected",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "prev_object_grip": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "prev_object_grip",
        "method_parameters": (("object","str","REQ"),("index","int","REQ"),("direction","int","OPT"),("enable","bln","OPT")),
        "method_returns": ("number","null")
    },
    "select_object_grips": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "select_object_grips",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "selected_object_grips": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "selected_object_grips",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "unselect_object_grips": {
        "method_location": "Object_Grip",
        "method_type": "METHOD",
        "method_name": "unselect_object_grips",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
}
point_and_vector = {
    "is_vector_parallel_to": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_parallel_to",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("number","null")
    },
    "is_vector_perpendicular_to": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_perpendicular_to",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_vector_tiny": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_tiny",
        "method_parameters": (("vector","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_vector_zero": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "is_vector_zero",
        "method_parameters": (("vector","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "point_add": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_add",
        "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "point_array_bounding_box": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_array_bounding_box",
        "method_parameters": (("points","arr_of_dbl","REQ"),("view","str","OPT"),("world_coords","bln","OPT")),
        "method_returns": ("array","null")
    },
    "point_array_closest_point": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_array_closest_point",
        "method_parameters": (("points","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("number","null")
    },
    "point_array_transform": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_array_transform",
        "method_parameters": (("points","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "point_compare": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_compare",
        "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "point_divide": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_divide",
        "method_parameters": (("point","arr_of_dbl","REQ"),("scale","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "point_scale": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_scale",
        "method_parameters": (("point","arr_of_dbl","REQ"),("scale","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "point_subtract": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_subtract",
        "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "point_transform": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "point_transform",
        "method_parameters": (("point","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "points_are_coplanar": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "points_are_coplanar",
        "method_parameters": (("points","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "project_point_to_mesh": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "project_point_to_mesh",
        "method_parameters": (("points","arr_of_dbl","REQ"),("meshes","arr_of_str","REQ"),("direction","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "project_point_to_surface": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "project_point_to_surface",
        "method_parameters": (("points","arr_of_dbl","REQ"),("surfaces","arr_of_str","REQ"),("direction","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "pull_points": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "pull_points",
        "method_parameters": (("object","str","REQ"),("points","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_add": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_add",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_compare": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_compare",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("null")
    },
    "vector_create": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_create",
        "method_parameters": (("point1","arr_of_dbl","REQ"),("point2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_cross_product": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_cross_product",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_divide": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_divide",
        "method_parameters": (("vector","arr_of_dbl","REQ"),("divide","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_dot_product": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_dot_product",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("null")
    },
    "vector_length": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_length",
        "method_parameters": (("vector","arr_of_dbl","REQ")),
        "method_returns": ("null")
    },
    "vector_multiply": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_multiply",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("number","null")
    },
    "vector_reverse": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_reverse",
        "method_parameters": (("vector","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_rotate": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_rotate",
        "method_parameters": (("vector","arr_of_dbl","REQ"),("angle","dbl","REQ"),("axis","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_scale": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_scale",
        "method_parameters": (("vector","arr_of_dbl","REQ"),("scale","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_subtract": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_subtract",
        "method_parameters": (("vector1","arr_of_dbl","REQ"),("vector2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_transform": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_transform",
        "method_parameters": (("vector","arr_of_dbl","REQ"),("xform","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "vector_unitize": {
        "method_location": "Point_and_Vector",
        "method_type": "METHOD",
        "method_name": "vector_unitize",
        "method_parameters": (("vector","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
}
selection = {
    "all_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "all_objects",
        "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "first_object": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "first_object",
        "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("string","null")
    },
    "get_curve_object": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "get_curve_object",
        "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "get_object_ex": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "get_object_ex",
        "method_parameters": (("message","str","OPT"),("type","int","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","arr_of_str","OPT")),
        "method_returns": ("array","null")
    },
    "get_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "get_objects",
        "method_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","arr_of_str","OPT")),
        "method_returns": ("array","null")
    },
    "get_objects_ex": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "get_objects_ex",
        "method_parameters": (("message","str","OPT"),("type","int","OPT"),("group","bln","OPT"),("pre_select","bln","OPT"),("select","bln","OPT"),("objects","arr_of_str","OPT")),
        "method_returns": ("array","null")
    },
    "get_point_coordinates": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "get_point_coordinates",
        "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "get_surface_object": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "get_surface_object",
        "method_parameters": (("message","str","OPT"),("pre_select","bln","OPT"),("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "hidden_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "hidden_objects",
        "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "invert_selected_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "invert_selected_objects",
        "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "last_created_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "last_created_objects",
        "method_parameters": (("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "last_object": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "last_object",
        "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("string","null")
    },
    "locked_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "locked_objects",
        "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "next_object": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "next_object",
        "method_parameters": (("object","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("string","null")
    },
    "normal_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "normal_objects",
        "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "objects_by_color": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_color",
        "method_parameters": (("color","lng","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
        "method_returns": ("array","null")
    },
    "objects_by_group": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_group",
        "method_parameters": (("group","str","REQ"),("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "objects_by_layer": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_layer",
        "method_parameters": (("layer","str","REQ"),("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "objects_by_name": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_name",
        "method_parameters": (("name","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
        "method_returns": ("array","null")
    },
    "objects_by_type": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_type",
        "method_parameters": (("type","int","REQ"),("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "objects_by_u_r_l": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "objects_by_u_r_l",
        "method_parameters": (("u_r_l","str","REQ"),("select","bln","OPT"),("include_lights","bln","OPT")),
        "method_returns": ("array","null")
    },
    "prev_selected_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "prev_selected_objects",
        "method_parameters": (("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "reference_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "reference_objects",
        "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "selected_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "selected_objects",
        "method_parameters": (("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "unselect_all_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "unselect_all_objects",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "unselected_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "unselected_objects",
        "method_parameters": (("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
    "visible_objects": {
        "method_location": "Selection",
        "method_type": "METHOD",
        "method_name": "visible_objects",
        "method_parameters": (("view","str","OPT"),("select","bln","OPT"),("include_lights","bln","OPT"),("include_grips","bln","OPT")),
        "method_returns": ("array","null")
    },
}
surface_and_polysurface = {
    "add_box": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_box",
        "method_parameters": (("corners","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_cone": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_cone",
        "method_parameters": (("base","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("height","dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
        "method_returns": ("string","null")
    },
    "add_cut_plane": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_cut_plane",
        "method_parameters": (("objects","arr_of_str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("normal","arr_of_dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_cylinder": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_cylinder",
        "method_parameters": (("base","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("height","dbl","REQ"),("height","dbl","REQ"),("radius","dbl","REQ"),("cap","bln","OPT")),
        "method_returns": ("string","null")
    },
    "add_edge_srf": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_edge_srf",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("string","null")
    },
    "add_loft_srf": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_loft_srf",
        "method_parameters": (("objects","arr_of_str","REQ"),("start_pt","arr_of_dbl","OPT"),("end_pt","arr_of_dbl","OPT"),("type","int","OPT"),("style","int","OPT"),("value","n","OPT"),("closed","bln","OPT")),
        "method_returns": ("array","null")
    },
    "add_nurbs_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_nurbs_surface",
        "method_parameters": (("point_count","arr_of_int","REQ"),("points","arr_of_dbl","REQ"),("knots_u","arr_of_int","REQ"),("knots_v","arr_of_int","REQ"),("degree","arr_of_int","REQ"),("weights","arr_of_int","REQ")),
        "method_returns": ("string","null")
    },
    "add_planar_srf": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_planar_srf",
        "method_parameters": (("objects","arr_of_str","REQ")),
        "method_returns": ("array","null")
    },
    "add_plane_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_plane_surface",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("d_u","dbl","REQ"),("d_v","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_rail_rev_srf": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_rail_rev_srf",
        "method_parameters": (("profile","str","REQ"),("rail","str","REQ"),("axis","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_rev_srf": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_rev_srf",
        "method_parameters": (("profile","str","REQ"),("axis","arr_of_dbl","REQ"),("start_angle","dbl","OPT"),("end_angle","dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_sphere": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_sphere",
        "method_parameters": (("center","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("radius","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_srf_contour_crvs": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_contour_crvs",
        "method_parameters": (("object","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("interval","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "add_srf_control_pt_grid": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_control_pt_grid",
        "method_parameters": (("count","arr_of_int","REQ"),("points","arr_of_dbl","REQ"),("degree","arr_of_dbl","OPT")),
        "method_returns": ("string","null")
    },
    "add_srf_pt": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_pt",
        "method_parameters": (("points","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "add_srf_pt_grid": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_pt_grid",
        "method_parameters": (("count","arr_of_int","REQ"),("points","arr_of_dbl","REQ"),("degree","arr_of_int","OPT"),("closed","arr_of_bln","OPT")),
        "method_returns": ("string","null")
    },
    "add_srf_section_crvs": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_srf_section_crvs",
        "method_parameters": (("object","str","REQ"),("plane","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "add_sweep1": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_sweep1",
        "method_parameters": (("rail","str","REQ"),("shapes","arr_of_str","REQ"),("start_pt","arr_of_dbl","OPT"),("end_pt","arr_of_dbl","OPT"),("closed","bln","OPT"),("style","int","OPT"),("style_arg","va","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT")),
        "method_returns": ("array","null")
    },
    "add_sweep2": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_sweep2",
        "method_parameters": (("rails","arr_of_str","REQ"),("shapes","arr_of_str","REQ"),("start_pt","arr_of_dbl","OPT"),("end_pt","arr_of_dbl","OPT"),("closed","bln","OPT"),("simple_sweep","bln","OPT"),("maintain_height","bln","OPT"),("simplify","int","OPT"),("simplify_arg","va","OPT")),
        "method_returns": ("array","null")
    },
    "add_torus": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "add_torus",
        "method_parameters": (("base","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ"),("major_radius","dbl","REQ"),("minor_radius","dbl","REQ"),("direction","arr_of_dbl","OPT")),
        "method_returns": ("string","null")
    },
    "boolean_difference": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "boolean_difference",
        "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "boolean_intersection": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "boolean_intersection",
        "method_parameters": (("input0","arr_of_str","REQ"),("input1","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "boolean_union": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "boolean_union",
        "method_parameters": (("input","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "brep_closest_point": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "brep_closest_point",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "cap_planar_holes": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "cap_planar_holes",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "duplicate_edge_curves": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "duplicate_edge_curves",
        "method_parameters": (("object","str","REQ"),("select","bln","OPT")),
        "method_returns": ("array","null")
    },
    "duplicate_surface_border": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "duplicate_surface_border",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "evaluate_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "evaluate_surface",
        "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "explode_polysurfaces": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "explode_polysurfaces",
        "method_parameters": (("objects","arr_of_str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "extract_iso_curve": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extract_iso_curve",
        "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ"),("dir","int","REQ")),
        "method_returns": ("array","null")
    },
    "extrude_curve": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve",
        "method_parameters": (("curve","str","REQ"),("path","str","REQ")),
        "method_returns": ("string","null")
    },
    "extrude_curve_point": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve_point",
        "method_parameters": (("curve","str","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "extrude_curve_straight": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve_straight",
        "method_parameters": (("curve","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "extrude_curve_tapered": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_curve_tapered",
        "method_parameters": (("curve","str","REQ"),("distance","dbl","REQ"),("direction","arr_of_dbl","REQ"),("base_point","arr_of_dbl","REQ"),("angle","dbl","REQ"),("corner_type","int","OPT")),
        "method_returns": ("array","null")
    },
    "extrude_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "extrude_surface",
        "method_parameters": (("surface","str","REQ"),("curve","str","REQ"),("cap","bln","OPT")),
        "method_returns": ("string","null")
    },
    "fit_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "fit_surface",
        "method_parameters": (("object","str","REQ"),("degree","arr_of_int","OPT"),("tolerance","dbl","OPT")),
        "method_returns": ("string","null")
    },
    "flip_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "flip_surface",
        "method_parameters": (("object","str","REQ"),("flip","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "insert_surface_knot": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "insert_surface_knot",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("direction","int","REQ"),("symmetrical","bln","OPT")),
        "method_returns": ("boolean","null")
    },
    "intersect_breps": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "intersect_breps",
        "method_parameters": (("brep1","str","REQ"),("brep2","str","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "is_brep": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_brep",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_brep_manifold": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_brep_manifold",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_cone": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_cone",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_cylinder": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_cylinder",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_parameter_on_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_parameter_on_surface",
        "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_plane_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_plane_surface",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_point_in_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_point_in_surface",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_point_on_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_point_on_surface",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_poly_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_poly_surface",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_poly_surface_closed": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_poly_surface_closed",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_poly_surface_planar": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_poly_surface_planar",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_sphere": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_sphere",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_surface_closed": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_closed",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_surface_periodic": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_periodic",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_surface_planar": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_planar",
        "method_parameters": (("object","str","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_surface_rational": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_rational",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_surface_singular": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_singular",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_surface_trimmed": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_surface_trimmed",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_torus": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "is_torus",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "join_surfaces": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "join_surfaces",
        "method_parameters": (("object","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("string","null")
    },
    "make_surface_non_periodic": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "make_surface_non_periodic",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ"),("delete","bln","OPT")),
        "method_returns": ("string","string","null")
    },
    "make_surface_periodic": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "make_surface_periodic",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ"),("delete","bln","OPT")),
        "method_returns": ("string","string","null")
    },
    "offset_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "offset_surface",
        "method_parameters": (("object","str","REQ"),("distance","dbl","REQ")),
        "method_returns": ("string","null")
    },
    "pull_curve": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "pull_curve",
        "method_parameters": (("surface","str","REQ"),("curve","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "rebuild_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "rebuild_surface",
        "method_parameters": (("object","str","REQ"),("degree","arr_of_int","OPT"),("point_count","arr_of_int","OPT")),
        "method_returns": ("boolean","null")
    },
    "remove_surface_knot": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "remove_surface_knot",
        "method_parameters": (("object","str","REQ"),("parameter","dbl","REQ"),("direction","int","REQ")),
        "method_returns": ("boolean","null")
    },
    "reverse_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "reverse_surface",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
        "method_returns": ("boolean","null")
    },
    "short_path": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "short_path",
        "method_parameters": (("surface","str","REQ"),("start","arr_of_dbl","REQ"),("end","arr_of_dbl","REQ")),
        "method_returns": ("string","null")
    },
    "shrink_trimmed_surface": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "shrink_trimmed_surface",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "split_brep": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "split_brep",
        "method_parameters": (("brep","str","REQ"),("cutter","str","REQ"),("delete","bln","OPT")),
        "method_returns": ("array","null")
    },
    "surface_area": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_area",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","number","number","null")
    },
    "surface_area_centroid": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_area_centroid",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "surface_area_moments": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_area_moments",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "surface_closest_point": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_closest_point",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "surface_cone": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_cone",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("array","array","number","number","null")
    },
    "surface_contour_points": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_contour_points",
        "method_parameters": (("object","str","REQ"),("start_point","arr_of_dbl","REQ"),("end_point","arr_of_dbl","REQ"),("interval","dbl","OPT"),("angle","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "surface_curvature": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_curvature",
        "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
        "method_returns": ("array","number","number","number","number","null")
    },
    "surface_curvature_analysis": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_curvature_analysis",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","array","array","array","array","null")
    },
    "surface_cylinder": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_cylinder",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("array","array","number","number","null")
    },
    "surface_degree": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_degree",
        "method_parameters": (("object","str","REQ"),("direction","int","OPT")),
        "method_returns": ("array","number","null")
    },
    "surface_domain": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_domain",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ")),
        "method_returns": ("array","null")
    },
    "surface_edit_points": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_edit_points",
        "method_parameters": (("object","str","REQ"),("return_parameters","bln","OPT"),("return_all","bln","OPT")),
        "method_returns": ("array","array","null")
    },
    "surface_evaluate": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_evaluate",
        "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ"),("derivative","int","REQ")),
        "method_returns": ("array","array","array","array","array","array","array","array","null")
    },
    "surface_frame": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_frame",
        "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "surface_isocurve_density": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_isocurve_density",
        "method_parameters": (("object","str","REQ"),("density","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "surface_knot_count": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_knot_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "surface_knots": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_knots",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "surface_normal": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_normal",
        "method_parameters": (("object","str","REQ"),("parameter","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "surface_point_count": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_point_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "surface_points": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_points",
        "method_parameters": (("object","str","REQ"),("return_all","bln","OPT")),
        "method_returns": ("array","null")
    },
    "surface_principal_curvature": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_principal_curvature",
        "method_parameters": (("object","str","REQ"),("point","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "surface_seam": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_seam",
        "method_parameters": (("object","str","REQ"),("direction","int","REQ"),("parameter","dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "surface_sphere": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_sphere",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("array","array","number","null")
    },
    "surface_surface_intersection": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_surface_intersection",
        "method_parameters": (("surface_a","str","REQ"),("surface_b","str","REQ"),("tolerance","dbl","OPT"),("create","bln","OPT")),
        "method_returns": ("array","array","number","string","null")
    },
    "surface_torus": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_torus",
        "method_parameters": (("surface","str","REQ")),
        "method_returns": ("array","array","number","number","null")
    },
    "surface_volume": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_volume",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","number","number","null")
    },
    "surface_volume_centroid": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_volume_centroid",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "surface_volume_moments": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_volume_moments",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
    "surface_weights": {
        "method_location": "Surface_and_Polysurface",
        "method_type": "METHOD",
        "method_name": "surface_weights",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("array","null")
    },
}
transformation = {
    "is_xform_identity": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "is_xform_identity",
        "method_parameters": (("xform","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_xform_similarity": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "is_xform_similarity",
        "method_parameters": (("xform","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_xform_zero": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "is_xform_zero",
        "method_parameters": (("xform","arr_of_dbl","REQ")),
        "method_returns": ("boolean","null")
    },
    "xform_c_plane_to_world": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_c_plane_to_world",
        "method_parameters": (("point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_change_basis": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_change_basis",
        "method_parameters": (("plane1","arr_of_dbl","REQ"),("plane2","arr_of_dbl","REQ"),("x0","arr_of_dbl","REQ"),("y0","arr_of_dbl","REQ"),("z0","arr_of_dbl","REQ"),("x1","arr_of_dbl","REQ"),("y1","arr_of_dbl","REQ"),("z1","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_compare": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_compare",
        "method_parameters": (("xform1","arr_of_dbl","REQ"),("xform2","arr_of_dbl","REQ")),
        "method_returns": ("null")
    },
    "xform_determinant": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_determinant",
        "method_parameters": (("xform","arr_of_dbl","REQ")),
        "method_returns": ("number","null")
    },
    "xform_diagonal": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_diagonal",
        "method_parameters": (("value","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_identity": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_identity",
        "method_parameters": (),
        "method_returns": ("array")
    },
    "xform_inverse": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_inverse",
        "method_parameters": (("xform","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_mirror": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_mirror",
        "method_parameters": (("point","arr_of_dbl","REQ"),("normal","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_multiply": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_multiply",
        "method_parameters": (("xform1","arr_of_dbl","REQ"),("xform2","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_planar_projection": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_planar_projection",
        "method_parameters": (("plane","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_rotation": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_rotation",
        "method_parameters": (("plane1","arr_of_dbl","REQ"),("plane2","arr_of_dbl","REQ"),("angle","dbl","REQ"),("axis","arr_of_dbl","REQ"),("start_dir","arr_of_dbl","REQ"),("end_dir","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("x0","arr_of_dbl","REQ"),("y0","arr_of_dbl","REQ"),("z0","arr_of_dbl","REQ"),("x1","arr_of_dbl","REQ"),("y1","arr_of_dbl","REQ"),("z1","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_scale": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_scale",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("x_scale","dbl","REQ"),("y_scale","dbl","REQ"),("z_scale","dbl","REQ"),("vector","arr_of_dbl","REQ"),("point","arr_of_dbl","REQ"),("scale","dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_screen_to_world": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_screen_to_world",
        "method_parameters": (("point","arr_of_dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
        "method_returns": ("array","null")
    },
    "xform_shear": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_shear",
        "method_parameters": (("plane","arr_of_dbl","REQ"),("x1","arr_of_dbl","REQ"),("y1","arr_of_dbl","REQ"),("z1","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_translation": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_translation",
        "method_parameters": (("vector","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_world_to_c_plane": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_world_to_c_plane",
        "method_parameters": (("point","arr_of_dbl","REQ"),("plane","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "xform_world_to_screen": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_world_to_screen",
        "method_parameters": (("point","arr_of_dbl","REQ"),("view","str","OPT"),("convert","bln","OPT")),
        "method_returns": ("array","array","null")
    },
    "xform_zero": {
        "method_location": "Transformation",
        "method_type": "METHOD",
        "method_name": "xform_zero",
        "method_parameters": (),
        "method_returns": ("array")
    },
}
user_data = {
    "attribute_data_count": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "attribute_data_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "delete_attribute_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "delete_attribute_data",
        "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "delete_document_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "delete_document_data",
        "method_parameters": (("section","str","OPT"),("entry","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "delete_object_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "delete_object_data",
        "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "document_data_count": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "document_data_count",
        "method_parameters": (),
        "method_returns": ("number")
    },
    "get_attribute_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_attribute_data",
        "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
        "method_returns": ("array","array","string","null")
    },
    "get_document_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_document_data",
        "method_parameters": (("section","str","OPT"),("entry","str","OPT")),
        "method_returns": ("array","array","string","null")
    },
    "get_object_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_object_data",
        "method_parameters": (("object","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
        "method_returns": ("array","array","string","null")
    },
    "get_user_text": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "get_user_text",
        "method_parameters": (("object","str","REQ"),("key","str","OPT"),("attach_to_geometry","bln","OPT")),
        "method_returns": ("string","array","null")
    },
    "is_attribute_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_attribute_data",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_document_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_document_data",
        "method_parameters": (),
        "method_returns": ("boolean")
    },
    "is_object_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_object_data",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_user_text": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "is_user_text",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "object_data_count": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "object_data_count",
        "method_parameters": (("object","str","REQ")),
        "method_returns": ("number","null")
    },
    "set_attribute_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_attribute_data",
        "method_parameters": (("object","str","REQ"),("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
        "method_returns": ("string","null")
    },
    "set_document_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_document_data",
        "method_parameters": (("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
        "method_returns": ("string","null")
    },
    "set_object_data": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_object_data",
        "method_parameters": (("object","str","REQ"),("section","str","REQ"),("entry","str","REQ"),("value","str","REQ")),
        "method_returns": ("string","null")
    },
    "set_user_text": {
        "method_location": "User_Data",
        "method_type": "METHOD",
        "method_name": "set_user_text",
        "method_parameters": (("object","str","REQ"),("key","str","REQ"),("value","str","OPT"),("attach_to_geometry","bln","OPT")),
        "method_returns": ("boolean","null")
    },
}
user_interface = {
    "browse_for_folder": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "browse_for_folder",
        "method_parameters": (("folder","str","OPT"),("message","str","OPT"),("title","str","OPT")),
        "method_returns": ("string","null")
    },
    "check_list_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "check_list_box",
        "method_parameters": (("items","arr_of_str","REQ"),("values","arr_of_bln","REQ"),("message","str","OPT"),("title","str","OPT")),
        "method_returns": ("array","null")
    },
    "combo_list_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "combo_list_box",
        "method_parameters": (("items","arr_of_str","REQ"),("message","str","OPT"),("title","str","OPT")),
        "method_returns": ("string","null")
    },
    "edit_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "edit_box",
        "method_parameters": (("string","str","OPT"),("message","str","OPT"),("title","str","OPT")),
        "method_returns": ("string","null")
    },
    "get_angle": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_angle",
        "method_parameters": (("point","arr_of_dbl","OPT"),("reference","arr_of_dbl","OPT"),("angle","dbl","OPT"),("message","str","OPT")),
        "method_returns": ("number","null")
    },
    "get_boolean": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_boolean",
        "method_parameters": (("message","str","REQ"),("items","arr_of_str","REQ"),("defaults","arr_of_bln","REQ")),
        "method_returns": ("array","null")
    },
    "get_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_box",
        "method_parameters": (("mode","int","OPT"),("point","arr_of_dbl","OPT"),("prompt1","str","OPT"),("prompt2","str","OPT"),("prompt3","str","OPT")),
        "method_returns": ("array","null")
    },
    "get_color": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_color",
        "method_parameters": (("color","lng","OPT")),
        "method_returns": ("number","null")
    },
    "get_distance": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_distance",
        "method_parameters": (("point","arr_of_dbl","OPT"),("distance","dbl","OPT"),("message1","str","OPT"),("message2","str","OPT")),
        "method_returns": ("number","null")
    },
    "get_integer": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_integer",
        "method_parameters": (("message","str","OPT"),("number","int","OPT"),("min","int","OPT"),("max","int","OPT")),
        "method_returns": ("number","null")
    },
    "get_layer": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_layer",
        "method_parameters": (("title","str","OPT"),("layer","str","OPT"),("show_new_layer","bln","OPT"),("show_set_current","bln","OPT")),
        "method_returns": ("string","null")
    },
    "get_linetype": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_linetype",
        "method_parameters": (("linetype","str","OPT")),
        "method_returns": ("string","null")
    },
    "get_point_on_curve": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_curve",
        "method_parameters": (("object","str","REQ"),("message","str","OPT")),
        "method_returns": ("array","null")
    },
    "get_point_on_line": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_line",
        "method_parameters": (("message","str","REQ"),("start","arr_of_dbl","REQ"),("end","arr_of_dbl","REQ"),("track","bln","OPT")),
        "method_returns": ("array","null")
    },
    "get_point_on_mesh": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_mesh",
        "method_parameters": (("object","str","REQ"),("message","str","OPT")),
        "method_returns": ("array","null")
    },
    "get_point_on_plane": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_plane",
        "method_parameters": (("message","str","OPT"),("plane","arr_of_dbl","OPT"),("point","arr_of_dbl","OPT")),
        "method_returns": ("array","null")
    },
    "get_point_on_surface": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_point_on_surface",
        "method_parameters": (("object","str","REQ"),("message","str","OPT")),
        "method_returns": ("array","null")
    },
    "get_points": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_points",
        "method_parameters": (("draw","bln","OPT"),("plane","bln","OPT"),("message1","str","OPT"),("message2","str","OPT"),("max_points","int","OPT"),("base_point","arr_of_dbl","OPT")),
        "method_returns": ("array","null")
    },
    "get_print_width": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_print_width",
        "method_parameters": (("print_width","dbl","OPT")),
        "method_returns": ("number","null")
    },
    "get_real": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_real",
        "method_parameters": (("message","str","OPT"),("number","dbl","OPT"),("min","dbl","OPT"),("max","dbl","OPT")),
        "method_returns": ("number","null")
    },
    "get_rectangle": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_rectangle",
        "method_parameters": (("mode","int","OPT"),("point","arr_of_dbl","OPT"),("prompt1","str","OPT"),("prompt2","str","OPT"),("prompt3","str","OPT")),
        "method_returns": ("array","null")
    },
    "get_string": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_string",
        "method_parameters": (("message","str","OPT"),("string","str","OPT"),("strings","arr_of_str","OPT")),
        "method_returns": ("string","null")
    },
    "get_surface_iso_param_point": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "get_surface_iso_param_point",
        "method_parameters": (("object","str","REQ"),("message","str","OPT")),
        "method_returns": ("array","null")
    },
    "html_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "html_box",
        "method_parameters": (("file_name","str","REQ"),("arguments","va","OPT"),("options","str","OPT"),("modal","bln","OPT")),
        "method_returns": ("boolean","null")
    },
    "integer_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "integer_box",
        "method_parameters": (("message","str","OPT"),("number","int","OPT"),("title","str","OPT")),
        "method_returns": ("number","null")
    },
    "list_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "list_box",
        "method_parameters": (("items","arr_of_str","REQ"),("message","str","OPT"),("title","str","OPT")),
        "method_returns": ("string","null")
    },
    "message_beep": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "message_beep",
        "method_parameters": (("beep","int","OPT")),
        "method_returns": ()
    },
    "message_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "message_box",
        "method_parameters": (("message","str","REQ"),("buttons","int","OPT"),("title","str","OPT")),
        "method_returns": ("number")
    },
    "multi_list_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "multi_list_box",
        "method_parameters": (("items","arr_of_str","REQ"),("message","str","OPT"),("title","str","OPT")),
        "method_returns": ("array","null")
    },
    "open_file_names": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "open_file_names",
        "method_parameters": (("title","str","OPT"),("filter","str","OPT"),("folder","str","OPT"),("filename","str","OPT"),("extension","str","OPT")),
        "method_returns": ("array","null")
    },
    "popup_menu": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "popup_menu",
        "method_parameters": (("items","arr_of_str","REQ"),("modes","arr_of_int","OPT"),("point","arr_of_dbl","OPT"),("view","str","OPT")),
        "method_returns": ("number","number","null")
    },
    "property_list_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "property_list_box",
        "method_parameters": (("items","arr_of_str","REQ"),("values","arr_of_str","REQ"),("message","str","OPT"),("title","str","OPT")),
        "method_returns": ("array","null")
    },
    "real_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "real_box",
        "method_parameters": (("message","str","OPT"),("number","dbl","OPT"),("title","str","OPT")),
        "method_returns": ("number","null")
    },
    "save_file_name": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "save_file_name",
        "method_parameters": (("title","str","OPT"),("filter","str","OPT"),("folder","str","OPT"),("filename","str","OPT"),("extension","str","OPT")),
        "method_returns": ("string","null")
    },
    "string_box": {
        "method_location": "User_Interface",
        "method_type": "METHOD",
        "method_name": "string_box",
        "method_parameters": (("message","str","OPT"),("string","str","OPT"),("title","str","OPT")),
        "method_returns": ("string","null")
    },
}
utility = {
    "all_procedures": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "all_procedures",
        "method_parameters": (("all","bln","OPT")),
        "method_returns": ("array","null")
    },
    "clipboard_text": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "clipboard_text",
        "method_parameters": (("text","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "color_adjust_luma": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "color_adjust_luma",
        "method_parameters": (("r_g_b","lng","REQ"),("luma","int","REQ"),("scale","bln","OPT")),
        "method_returns": ("number","null")
    },
    "color_blue_value": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "color_blue_value",
        "method_parameters": (("r_g_b","lng","REQ")),
        "method_returns": ("number","null")
    },
    "color_green_value": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "color_green_value",
        "method_parameters": (("r_g_b","lng","REQ")),
        "method_returns": ("number","null")
    },
    "color_h_l_s_to_r_g_b": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "color_h_l_s_to_r_g_b",
        "method_parameters": (("r_g_b","lng","REQ")),
        "method_returns": ("number","null")
    },
    "color_r_g_b_to_h_l_s": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "color_r_g_b_to_h_l_s",
        "method_parameters": (("r_g_b","lng","REQ")),
        "method_returns": ("array","null")
    },
    "color_red_value": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "color_red_value",
        "method_parameters": (("r_g_b","lng","REQ")),
        "method_returns": ("number","null")
    },
    "cull_duplicate_numbers": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "cull_duplicate_numbers",
        "method_parameters": (("numbers","arr_of_int","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "cull_duplicate_points": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "cull_duplicate_points",
        "method_parameters": (("points","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
        "method_returns": ("array","null")
    },
    "cull_duplicate_strings": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "cull_duplicate_strings",
        "method_parameters": (("strings","arr_of_int","REQ"),("case_sensitive","bln","OPT")),
        "method_returns": ("array","null")
    },
    "current_printer": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "current_printer",
        "method_parameters": (("printer","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "get_settings": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "get_settings",
        "method_parameters": (("filename","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
        "method_returns": ("array","array","string","null")
    },
    "is_procedure": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "is_procedure",
        "method_parameters": (("sub_name","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "printer_names": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "printer_names",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "pt2_str": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "pt2_str",
        "method_parameters": (("point","arr_of_dbl","REQ"),("precision","n","OPT"),("space","bln","OPT")),
        "method_returns": ("string","null")
    },
    "save_settings": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "save_settings",
        "method_parameters": (("filename","str","REQ"),("section","str","OPT"),("entry","str","OPT"),("string","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "simplify_array": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "simplify_array",
        "method_parameters": (("points","arr_of_dbl","REQ")),
        "method_returns": ("array","null")
    },
    "sleep": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "sleep",
        "method_parameters": (("milliseconds","lng","REQ")),
        "method_returns": ("null")
    },
    "spool_to_printer": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "spool_to_printer",
        "method_parameters": (("file","str","REQ"),("printer","str","REQ")),
        "method_returns": ("string","null")
    },
    "str2_pt": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "str2_pt",
        "method_parameters": (("point","str","REQ")),
        "method_returns": ("array","null")
    },
    "str2_pt_array": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "str2_pt_array",
        "method_parameters": (("points","str","REQ")),
        "method_returns": ("array","null")
    },
    "strtok": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "strtok",
        "method_parameters": (("text","str","REQ"),("delimiters","str","OPT")),
        "method_returns": ("array","null")
    },
    "text_out": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "text_out",
        "method_parameters": (("text","str","REQ"),("title","str","OPT")),
        "method_returns": ("null")
    },
    "version": {
        "method_location": "Utility",
        "method_type": "METHOD",
        "method_name": "version",
        "method_parameters": (),
        "method_returns": ("number")
    },
}
view = {
    "add_named_c_plane": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "add_named_c_plane",
        "method_parameters": (("name","str","REQ"),("view","str","OPT")),
        "method_returns": ("string","null")
    },
    "add_named_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "add_named_view",
        "method_parameters": (("name","str","REQ"),("view","str","OPT")),
        "method_returns": ("string","null")
    },
    "background_bitmap": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "background_bitmap",
        "method_parameters": (("view","str","OPT"),("file_name","str","OPT"),("point","arr_of_dbl","OPT"),("width","dbl","OPT")),
        "method_returns": ("string","string","null")
    },
    "current_detail": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "current_detail",
        "method_parameters": (("layout","str","REQ"),("detail","str","OPT"),("return_names","bln","OPT")),
        "method_returns": ("string","string","null")
    },
    "current_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "current_view",
        "method_parameters": (("view","str","OPT"),("return_name","bln","OPT")),
        "method_returns": ("string","string","null")
    },
    "delete_named_c_plane": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "delete_named_c_plane",
        "method_parameters": (("name","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "delete_named_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "delete_named_view",
        "method_parameters": (("name","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "detail_names": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "detail_names",
        "method_parameters": (("layout","str","REQ"),("return_names","bln","OPT")),
        "method_returns": ("array","null")
    },
    "is_background_bitmap": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_background_bitmap",
        "method_parameters": (("view","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_detail": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_detail",
        "method_parameters": (("layout","str","REQ"),("detail","str","REQ")),
        "method_returns": ("null")
    },
    "is_layout": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_layout",
        "method_parameters": (("layout","str","REQ")),
        "method_returns": ("null")
    },
    "is_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_view",
        "method_parameters": (("view","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_view_current": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_view_current",
        "method_parameters": (("view","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "is_view_maximized": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_view_maximized",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_view_perspective": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_view_perspective",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_view_title_visible": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_view_title_visible",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "is_wallpaper": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "is_wallpaper",
        "method_parameters": (("view","str","REQ")),
        "method_returns": ("boolean","null")
    },
    "maximize_restore_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "maximize_restore_view",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ()
    },
    "named_c_planes": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "named_c_planes",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "named_views": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "named_views",
        "method_parameters": (),
        "method_returns": ("array","null")
    },
    "rename_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "rename_view",
        "method_parameters": (("old_title","str","REQ"),("new_title","str","REQ")),
        "method_returns": ("string","null")
    },
    "restore_named_c_plane": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "restore_named_c_plane",
        "method_parameters": (("name","str","REQ"),("view","str","OPT")),
        "method_returns": ("string","null")
    },
    "restore_named_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "restore_named_view",
        "method_parameters": (("name","str","REQ"),("view","str","OPT"),("restore_bitmap","bln","OPT")),
        "method_returns": ("string","null")
    },
    "rotate_camera": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "rotate_camera",
        "method_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "rotate_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "rotate_view",
        "method_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "show_grid": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "show_grid",
        "method_parameters": (("view","str","OPT"),("show","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "show_grid_axes": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "show_grid_axes",
        "method_parameters": (("view","str","OPT"),("show","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "show_view_title": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "show_view_title",
        "method_parameters": (("view","str","OPT"),("state","bln","OPT")),
        "method_returns": ()
    },
    "show_world_axes": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "show_world_axes",
        "method_parameters": (("view","str","OPT"),("show","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "synchronize_c_planes": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "synchronize_c_planes",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ("boolean","null")
    },
    "tilt_view": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "tilt_view",
        "method_parameters": (("view","str","OPT"),("direction","int","OPT"),("angle","dbl","OPT")),
        "method_returns": ("boolean","null")
    },
    "view_c_plane": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_c_plane",
        "method_parameters": (("view","str","OPT"),("plane","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "view_camera": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_camera",
        "method_parameters": (("view","str","OPT"),("camera","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "view_camera_lens": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_lens",
        "method_parameters": (("view","str","OPT"),("length","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "view_camera_plane": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_plane",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ("array","null")
    },
    "view_camera_target": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_target",
        "method_parameters": (("view","str","OPT"),("camera","arr_of_dbl","OPT"),("target","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "view_camera_up": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_camera_up",
        "method_parameters": (("view","str","OPT"),("up_vector","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "view_display_mode_ex": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_display_mode_ex",
        "method_parameters": (("view","str","OPT"),("mode","str","OPT"),("return_names","bln","OPT")),
        "method_returns": ("number","number","null")
    },
    "view_display_mode_name": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_display_mode_name",
        "method_parameters": (("mode","str","REQ")),
        "method_returns": ("string","null")
    },
    "view_display_modes": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_display_modes",
        "method_parameters": (("return_name","bln","OPT")),
        "method_returns": ("array","null")
    },
    "view_names": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_names",
        "method_parameters": (("return_names","bln","OPT"),("type","int","OPT")),
        "method_returns": ("array","null")
    },
    "view_near_corners": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_near_corners",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ("array","null")
    },
    "view_projection": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_projection",
        "method_parameters": (("view","str","OPT"),("mode","int","OPT")),
        "method_returns": ("number","number","null")
    },
    "view_radius": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_radius",
        "method_parameters": (("view","str","OPT"),("radius","dbl","OPT")),
        "method_returns": ("number","number","null")
    },
    "view_size": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_size",
        "method_parameters": (("view","str","OPT")),
        "method_returns": ("array","null")
    },
    "view_target": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_target",
        "method_parameters": (("view","str","OPT"),("target","arr_of_dbl","OPT")),
        "method_returns": ("array","array","null")
    },
    "view_title": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "view_title",
        "method_parameters": (("mode","str","REQ")),
        "method_returns": ("string","null")
    },
    "wallpaper": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "wallpaper",
        "method_parameters": (("view","str","OPT"),("file_name","str","OPT")),
        "method_returns": ("string","string","null")
    },
    "wallpaper_gray_scale": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "wallpaper_gray_scale",
        "method_parameters": (("view","str","OPT"),("gray_scale","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "wallpaper_hidden": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "wallpaper_hidden",
        "method_parameters": (("view","str","OPT"),("hidden","bln","OPT")),
        "method_returns": ("boolean","boolean","null")
    },
    "zoom_bounding_box": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "zoom_bounding_box",
        "method_parameters": (("corners","arr_of_dbl","REQ"),("view","str","OPT"),("all","bln","OPT")),
        "method_returns": ()
    },
    "zoom_extents": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "zoom_extents",
        "method_parameters": (("view","str","OPT"),("all","bln","OPT")),
        "method_returns": ()
    },
    "zoom_selected": {
        "method_location": "View",
        "method_type": "METHOD",
        "method_name": "zoom_selected",
        "method_parameters": (("view","str","OPT"),("all","bln","OPT")),
        "method_returns": ()
    },
}
