#The data below will be used to generate the Rhinoscript function wrappers


#===============================================================================
# 
#===============================================================================
class application(object):    
    folder = "app"

    class Functions(object):

        build_date = {
            "method_name": "build_date",
            "method_parameters": (),
            "method_returns": ("number","null")
            }
        default_renderer = {
            "method_name": "default_renderer",
            "method_parameters": (("renderer","str","OPT"),),
            "method_returns": ("str","null")
            }
        exit = {
            "method_name": "exit",
            "method_parameters": (),
            "method_returns": ()
            }
        help = {
            "method_name": "help",
            "method_parameters": (("topic","int","OPT"),),
            "method_returns": ("bln",)
            }
        locale_i_d = {
            "method_name": "locale_i_d",
            "method_parameters": (),
            "method_returns": ("number",)
            }
        print_ = {
            "method_name": "print_",
            "method_parameters": (("message","str","OPT"),),
            "method_returns": ()
            }
        print_ex = {
            "method_name": "print_ex",
            "method_parameters": (("message","str","OPT"),),
            "method_returns": ()
            }
        prompt = {
            "method_name": "prompt",
            "method_parameters": (("prompt","str","OPT"),),
            "method_returns": ()
            }
        registry_key = {
            "method_name": "registry_key",
            "method_parameters": (),
            "method_returns": ("str","null")
            }
        screen_size = {
            "method_name": "screen_size",
            "method_parameters": (),
            "method_returns": ("array_of number","null")
            }
        sdk_version = {
            "method_name": "sdk_version",
            "method_parameters": (),
            "method_returns": ("number","null")
            }
        send_keystrokes = {
            "method_name": "send_keystrokes",
            "method_parameters": (("keys","str","OPT"),("add_return","bln","OPT")),
            "method_returns": ()
            }
        window_handle = {
            "method_name": "window_handle",
            "method_parameters": (),
            "method_returns": ("number",)
            }
#===============================================================================
# 
#===============================================================================
class files(object):    
    folder = "app"
    
    class Functions(object):   
        add_search_path = {
            "method_name": "add_search_path",
            "method_parameters": (("folder","str","REQ"),("index","int","OPT")),
            "method_returns": ("number","null")
            }
        delete_search_path = {
            "method_name": "delete_search_path",
            "method_parameters": (("folder","str","REQ"),),
            "method_returns": ("bln","null")
            }    
          
        autosave_file = {
            "method_name": "autosave_file",
            "method_parameters": (("file","str","OPT"),),
            "method_returns": ("str","null")
            }
        autosave_interval = {
            "method_name": "autosave_interval",
            "method_parameters": (("minutes","int","OPT"),),
            "method_returns": ("number","null")
            }
        enable_autosave = {
            "method_name": "enable_autosave",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("bln",)
            }        
        find_file = {
            "method_name": "find_file",
            "method_parameters": (("filename","str","REQ"),),
            "method_returns": ("str","null")
            }
        install_folder = {
            "method_name": "install_folder",
            "method_parameters": (),
            "method_returns": ("str","null")
            }
        working_folder = {
            "method_name": "working_folder",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("str", )
            }
        search_path_count = {
            "method_name": "search_path_count",
            "method_parameters": (),
            "method_returns": ("number",)
            }
        search_path_list = {
            "method_name": "search_path_list",
            "method_parameters": (),
            "method_returns": ("array_of str",)
            }
        template_file = {
            "method_name": "template_file",
            "method_parameters": (("filename","str","OPT"),),
            "method_returns": ("str", )
            }
        template_folder = {
            "method_name": "template_folder",
            "method_parameters": (("folder","str","OPT"),),
            "method_returns": ("str", )
            }
        exe_folder = {
            "method_name": "exe_folder",
            "method_parameters": (),
            "method_returns": ("str","null")
            }
#===============================================================================
# 
#===============================================================================
class settings(object):    
    folder = "app"
    
    class Functions(object):   
    
        enable_history_recording = {
            "method_name": "enable_history_recording",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("bln", )
            }
        project_osnaps = {
            "method_name": "project_osnaps",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("bln", )
            }
        snap = {
            "method_name": "snap",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("bln", )
            }
        ortho = {
            "method_name": "ortho",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("bln", )
            }
        osnap = {
            "method_name": "osnap",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("bln", )
            }
        osnap_dialog = {
            "method_name": "osnap_dialog",
            "method_parameters": (("visible","bln","OPT"),),
            "method_returns": ("bln", )
            }
        osnap_mode = {
            "method_name": "osnap_mode",
            "method_parameters": (("mode","int","OPT"),),
            "method_returns": ("number","null")
            }
        planar = {
            "method_name": "planar",
            "method_parameters": (("enable","bln","OPT"),),
            "method_returns": ("bln", )
            }
        appearance_color = {
            "method_name": "appearance_color",
            "method_parameters": (("item","int","REQ"),("color","lng","OPT")),
            "method_returns": ("number","null")
            }
        appearance_display = {
            "method_name": "appearance_display",
            "method_parameters": (("item","int","REQ"),("show","bln","OPT")),
            "method_returns": ("number","null")
            }
        display_ole_alerts = {
            "method_name": "display_ole_alerts",
            "method_parameters": (("display","bln","REQ"),),
            "method_returns": ()
            }
        edge_analysis_color = {
            "method_name": "edge_analysis_color",
            "method_parameters": (("color","lng","OPT"),),
            "method_returns": ("number","null")
            }
        edge_analysis_mode = {
            "method_name": "edge_analysis_mode",
            "method_parameters": (("mode","int","OPT"),),
            "method_returns": ("number","null")
            }        
#===============================================================================
# 
#===============================================================================
class scripts(object):    
    folder = "app"
    
    class Functions(object):    
        
        add_startup_script = {
            "method_name": "add_startup_script",
            "method_parameters": (("script_file","str","REQ"),("index","int","OPT")),
            "method_returns": ("number","null")
            }
        delete_startup_script = {
            "method_name": "delete_startup_script",
            "method_parameters": (("script_file","str","REQ"),),
            "method_returns": ("bln","null")
            }
        startup_script_count = {
            "method_name": "startup_script_count",
            "method_parameters": (),
            "method_returns": ("number",)
            }
        startup_script_list = {
            "method_name": "startup_script_list",
            "method_parameters": (),
            "method_returns": ("array_of str",)
            }
        last_loaded_script_file = {
            "method_name": "last_loaded_script_file",
            "method_parameters": (),
            "method_returns": ("str","null")
            }
        plug_ins = {
            "method_name": "plug_ins",
            "method_parameters": (("types","int","OPT"),("status","int","OPT")),
            "method_returns": ("array_of str","null")
            }
        get_plug_in_object = {
            "method_name": "get_plug_in_object",
            "method_parameters": (("plug_in","str","REQ"),),
            "method_returns": ("number", "null")
            }        
#===============================================================================
# 
#===============================================================================
class status_bar(object):    
    folder = "app"

    class Functions(object):
        
        status_bar_distance = {
            "method_name": "status_bar_distance",
            "method_parameters": (("distance","dbl","OPT"),),
            "method_returns": ()
            }
        status_bar_message = {
            "method_name": "status_bar_message",
            "method_parameters": (("message","str","OPT"),),
            "method_returns": ()
            }
        status_bar_number = {
            "method_name": "status_bar_number",
            "method_parameters": (("number","dbl","OPT"),),
            "method_returns": ()
            }
        status_bar_point = {
            "method_name": "status_bar_point",
            "method_parameters": (("point","array_of dbl","OPT"),),
            "method_returns": ()
            }

#===============================================================================
# 
#===============================================================================
class commands(object):    
    folder = "app"

    class Functions(object):
        clear_command_history = {
            "method_name": "clear_command_history",
            "method_parameters": (),
            "method_returns": ()
            }
        command = {
            "method_name": "command",
            "method_parameters": (("command","str","REQ"),("echo","bln","OPT")),
            "method_returns": ("bln","null")
            }
        command_history = {
            "method_name": "command_history",
            "method_parameters": (),
            "method_returns": ("str","null")
            }
        in_command = {
            "method_name": "in_command",
            "method_parameters": (("ignore_runners","bln","OPT"),),
            "method_returns": ("number",)
            }
        is_command = {
            "method_name": "is_command",
            "method_parameters": (("command_name","str","REQ"),),
            "method_returns": ("bln","null")
            }
        last_command_name = {
            "method_name": "last_command_name",
            "method_parameters": (),
            "method_returns": ("str",)
            }
        last_command_result = {
            "method_name": "last_command_result",
            "method_parameters": (),
            "method_returns": ("number",)
            }
        add_alias = {
            "method_name": "add_alias",
            "method_parameters": (("alias","str","REQ"),("macro","str","REQ")),
            "method_returns": ("bln","null")
            }
        alias_count = {
            "method_name": "alias_count",
            "method_parameters": (),
            "method_returns": ("number",)
            }
        alias_macro = {
            "method_name": "alias_macro",
            "method_parameters": (("alias","str","REQ"),("macro","str","OPT")),
            "method_returns": ("str","null")
            }
        alias_names = {
            "method_name": "alias_names",
            "method_parameters": (),
            "method_returns": ("array_of str",)
            }
        delete_alias = {
            "method_name": "delete_alias",
            "method_parameters": (("alias","str","REQ"),),
            "method_returns": ("bln","null")
            }        
        is_alias = {
            "method_name": "is_alias",
            "method_parameters": (("alias","str","REQ"),),
            "method_returns": ("bln","null")
            }