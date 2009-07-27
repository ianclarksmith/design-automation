#The data below will be used to generate the Rhinoscript functions

#Errors can be fixed by hand here

add_alias = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "add_alias",
    "method_parameters": (("alias","str","REQ"),("macro","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
add_search_path = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "add_search_path",
    "method_parameters": (("folder","str","REQ"),("index","int","OPT")),
    "method_returns": (""number"",""null"")
    }
add_startup_script = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "add_startup_script",
    "method_parameters": (("script_file","str","REQ"),("index","int","OPT")),
    "method_returns": (""number"",""null"")
    }
alias_count = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "alias_count",
    "method_parameters": (),
    "method_returns": (""number"")
    }
alias_macro = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "alias_macro",
    "method_parameters": (("alias","str","REQ"),("macro","str","OPT")),
    "method_returns": (""string"",""string"",""null"")
    }
alias_names = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "alias_names",
    "method_parameters": (),
    "method_returns": (""array"")
    }
appearance_color = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "appearance_color",
    "method_parameters": (("item","int","REQ"),("color","lng","OPT")),
    "method_returns": (""number"",""number"",""null"")
    }
appearance_display = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "appearance_display",
    "method_parameters": (("item","int","REQ"),("show","bln","OPT")),
    "method_returns": (""number"",""number"",""null"")
    }
autosave_file = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "autosave_file",
    "method_parameters": (("file","str","OPT")),
    "method_returns": (""string"",""string"",""null"")
    }
autosave_interval = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "autosave_interval",
    "method_parameters": (("minutes","int","OPT")),
    "method_returns": (""number"",""number"",""null"")
    }
build_date = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "build_date",
    "method_parameters": (),
    "method_returns": (""number"",""null"")
    }
clear_command_history = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "clear_command_history",
    "method_parameters": (),
    "method_returns": ()
    }
command = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "command",
    "method_parameters": (("command","str","REQ"),("echo","bln","OPT")),
    "method_returns": (""boolean"",""null"")
    }
command_history = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "command_history",
    "method_parameters": (),
    "method_returns": (""string"",""null"")
    }
default_renderer = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "default_renderer",
    "method_parameters": (("renderer","str","OPT")),
    "method_returns": (""string"",""string"",""null"")
    }
delete_alias = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "delete_alias",
    "method_parameters": (("alias","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
delete_search_path = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "delete_search_path",
    "method_parameters": (("folder","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
delete_startup_script = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "delete_startup_script",
    "method_parameters": (("script_file","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
display_ole_alerts = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "display_ole_alerts",
    "method_parameters": (("display","bln","REQ")),
    "method_returns": (""null"")
    }
edge_analysis_color = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "edge_analysis_color",
    "method_parameters": (("color","lng","OPT")),
    "method_returns": (""number"",""number"",""null"")
    }
edge_analysis_mode = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "edge_analysis_mode",
    "method_parameters": (("mode","int","OPT")),
    "method_returns": (""number"",""number"",""null"")
    }
enable_autosave = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "enable_autosave",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""boolean"")
    }
enable_history_recording = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "enable_history_recording",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""boolean"",""boolean"")
    }
exe_folder = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "exe_folder",
    "method_parameters": (),
    "method_returns": (""string"",""null"")
    }
exit = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "exit",
    "method_parameters": (),
    "method_returns": ()
    }
find_file = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "find_file",
    "method_parameters": (("filename","str","REQ")),
    "method_returns": (""string"",""null"")
    }
get_plug_in_object = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "get_plug_in_object",
    "method_parameters": (("plug_in","str","REQ")),
    "method_returns": (""null"")
    }
help = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "help",
    "method_parameters": (("topic","int","OPT")),
    "method_returns": (""boolean"")
    }
in_command = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "in_command",
    "method_parameters": (("ignore_runners","bln","OPT")),
    "method_returns": (""number"")
    }
install_folder = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "install_folder",
    "method_parameters": (),
    "method_returns": (""string"",""null"")
    }
is_alias = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "is_alias",
    "method_parameters": (("alias","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
is_command = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "is_command",
    "method_parameters": (("command_name","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
last_command_name = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "last_command_name",
    "method_parameters": (),
    "method_returns": (""string"")
    }
last_command_result = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "last_command_result",
    "method_parameters": (),
    "method_returns": (""number"")
    }
last_loaded_script_file = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "last_loaded_script_file",
    "method_parameters": (),
    "method_returns": (""string"",""null"")
    }
locale_i_d = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "locale_i_d",
    "method_parameters": (),
    "method_returns": (""number"")
    }
ortho = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "ortho",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""boolean"",""boolean"")
    }
osnap = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "osnap",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""boolean"",""boolean"")
    }
osnap_dialog = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "osnap_dialog",
    "method_parameters": (("visible","bln","OPT")),
    "method_returns": (""boolean"",""boolean"")
    }
osnap_mode = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "osnap_mode",
    "method_parameters": (("mode","int","OPT")),
    "method_returns": (""number"",""number"",""null"")
    }
planar = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "planar",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""boolean"",""boolean"")
    }
plug_ins = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "plug_ins",
    "method_parameters": (("types","int","OPT"),("status","int","OPT")),
    "method_returns": (""array"",""null"")
    }
print_ = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "print_",
    "method_parameters": (("message","str","OPT")),
    "method_returns": ()
    }
print_ex = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "print_ex",
    "method_parameters": (("message","str","OPT")),
    "method_returns": ()
    }
project_osnaps = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "project_osnaps",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""boolean"",""boolean"")
    }
prompt = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "prompt",
    "method_parameters": (("prompt","str","OPT")),
    "method_returns": ()
    }
registry_key = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "registry_key",
    "method_parameters": (),
    "method_returns": (""string"",""null"")
    }
screen_size = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "screen_size",
    "method_parameters": (),
    "method_returns": (""array"",""null"")
    }
sdk_version = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "sdk_version",
    "method_parameters": (),
    "method_returns": (""number"",""null"")
    }
search_path_count = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "search_path_count",
    "method_parameters": (),
    "method_returns": (""number"")
    }
search_path_list = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "search_path_list",
    "method_parameters": (),
    "method_returns": (""array"")
    }
send_keystrokes = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "send_keystrokes",
    "method_parameters": (("keys","str","OPT"),("add_return","bln","OPT")),
    "method_returns": ()
    }
snap = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "snap",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""boolean"",""boolean"")
    }
startup_script_count = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "startup_script_count",
    "method_parameters": (),
    "method_returns": (""number"")
    }
startup_script_list = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "startup_script_list",
    "method_parameters": (),
    "method_returns": (""array"")
    }
status_bar_distance = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "status_bar_distance",
    "method_parameters": (("distance","dbl","OPT")),
    "method_returns": ()
    }
status_bar_message = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "status_bar_message",
    "method_parameters": (("message","str","OPT")),
    "method_returns": ()
    }
status_bar_number = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "status_bar_number",
    "method_parameters": (("number","dbl","OPT")),
    "method_returns": ()
    }
status_bar_point = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "status_bar_point",
    "method_parameters": (("point","arr_of_dbl","OPT")),
    "method_returns": ()
    }
template_file = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "template_file",
    "method_parameters": (("filename","str","OPT")),
    "method_returns": (""string"",""string"")
    }
template_folder = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "template_folder",
    "method_parameters": (("folder","str","OPT")),
    "method_returns": (""string"",""string"")
    }
window_handle = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "window_handle",
    "method_parameters": (),
    "method_returns": (""number"")
    }
working_folder = {
    "method_location": "Application",
    "method_type": "METHOD",
    "method_name": "working_folder",
    "method_parameters": (("enable","bln","OPT")),
    "method_returns": (""string"",""string"")
    }
