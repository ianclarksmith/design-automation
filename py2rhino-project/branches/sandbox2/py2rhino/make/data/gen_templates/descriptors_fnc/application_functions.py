#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

add_alias = {
    "function_location": "application",
    "function_com_id": 709,
    "function_vb_name": "AddAlias",
    "function_name": "add_alias",
    "function_parameters": (("alias","str","REQ"),("macro","str","REQ")),
    "function_returns": ("boolean","null")
    }
add_search_path = {
    "function_location": "application",
    "function_com_id": 511,
    "function_vb_name": "AddSearchPath",
    "function_name": "add_search_path",
    "function_parameters": (("folder","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
add_startup_script = {
    "function_location": "application",
    "function_com_id": 714,
    "function_vb_name": "AddStartupScript",
    "function_name": "add_startup_script",
    "function_parameters": (("script_file","str","REQ"),("index","int","OPT")),
    "function_returns": ("number","null")
    }
alias_count = {
    "function_location": "application",
    "function_com_id": 706,
    "function_vb_name": "AliasCount",
    "function_name": "alias_count",
    "function_parameters": (),
    "function_returns": ("number")
    }
alias_macro = {
    "function_location": "application",
    "function_com_id": 708,
    "function_vb_name": "AliasMacro",
    "function_name": "alias_macro",
    "function_parameters": (("alias","str","REQ"),("macro","str","OPT")),
    "function_returns": ("string","string","null")
    }
alias_names = {
    "function_location": "application",
    "function_com_id": 707,
    "function_vb_name": "AliasNames",
    "function_name": "alias_names",
    "function_parameters": (),
    "function_returns": ("array")
    }
appearance_color = {
    "function_location": "application",
    "function_com_id": 335,
    "function_vb_name": "AppearanceColor",
    "function_name": "appearance_color",
    "function_parameters": (("item","int","REQ"),("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
appearance_display = {
    "function_location": "application",
    "function_com_id": 752,
    "function_vb_name": "AppearanceDisplay",
    "function_name": "appearance_display",
    "function_parameters": (("item","int","REQ"),("show","bln","OPT")),
    "function_returns": ("number","number","null")
    }
autosave_file = {
    "function_location": "application",
    "function_com_id": 428,
    "function_vb_name": "AutosaveFile",
    "function_name": "autosave_file",
    "function_parameters": (("file","str","OPT")),
    "function_returns": ("string","string","null")
    }
autosave_interval = {
    "function_location": "application",
    "function_com_id": 429,
    "function_vb_name": "AutosaveInterval",
    "function_name": "autosave_interval",
    "function_parameters": (("minutes","int","OPT")),
    "function_returns": ("number","number","null")
    }
build_date = {
    "function_location": "application",
    "function_com_id": 360,
    "function_vb_name": "BuildDate",
    "function_name": "build_date",
    "function_parameters": (),
    "function_returns": ("number","null")
    }
clear_command_history = {
    "function_location": "application",
    "function_com_id": 592,
    "function_vb_name": "ClearCommandHistory",
    "function_name": "clear_command_history",
    "function_parameters": (),
    "function_returns": ()
    }
command = {
    "function_location": "application",
    "function_com_id": 1,
    "function_vb_name": "Command",
    "function_name": "command",
    "function_parameters": (("command","str","REQ"),("echo","bln","OPT")),
    "function_returns": ("boolean","null")
    }
command_history = {
    "function_location": "application",
    "function_com_id": 591,
    "function_vb_name": "CommandHistory",
    "function_name": "command_history",
    "function_parameters": (),
    "function_returns": ("string","null")
    }
default_renderer = {
    "function_location": "application",
    "function_com_id": 316,
    "function_vb_name": "DefaultRenderer",
    "function_name": "default_renderer",
    "function_parameters": (("renderer","str","OPT")),
    "function_returns": ("string","string","null")
    }
delete_alias = {
    "function_location": "application",
    "function_com_id": 710,
    "function_vb_name": "DeleteAlias",
    "function_name": "delete_alias",
    "function_parameters": (("alias","str","REQ")),
    "function_returns": ("boolean","null")
    }
delete_search_path = {
    "function_location": "application",
    "function_com_id": 512,
    "function_vb_name": "DeleteSearchPath",
    "function_name": "delete_search_path",
    "function_parameters": (("folder","str","REQ")),
    "function_returns": ("boolean","null")
    }
delete_startup_script = {
    "function_location": "application",
    "function_com_id": 715,
    "function_vb_name": "DeleteStartupScript",
    "function_name": "delete_startup_script",
    "function_parameters": (("script_file","str","REQ")),
    "function_returns": ("boolean","null")
    }
display_ole_alerts = {
    "function_location": "application",
    "function_com_id": 896,
    "function_vb_name": "DisplayOleAlerts",
    "function_name": "display_ole_alerts",
    "function_parameters": (("display","bln","REQ")),
    "function_returns": ("null")
    }
edge_analysis_color = {
    "function_location": "application",
    "function_com_id": 449,
    "function_vb_name": "EdgeAnalysisColor",
    "function_name": "edge_analysis_color",
    "function_parameters": (("color","lng","OPT")),
    "function_returns": ("number","number","null")
    }
edge_analysis_mode = {
    "function_location": "application",
    "function_com_id": 448,
    "function_vb_name": "EdgeAnalysisMode",
    "function_name": "edge_analysis_mode",
    "function_parameters": (("mode","int","OPT")),
    "function_returns": ("number","number","null")
    }
enable_autosave = {
    "function_location": "application",
    "function_com_id": 430,
    "function_vb_name": "EnableAutosave",
    "function_name": "enable_autosave",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("boolean")
    }
enable_history_recording = {
    "function_location": "application",
    "function_com_id": 735,
    "function_vb_name": "EnableHistoryRecording",
    "function_name": "enable_history_recording",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
exe_folder = {
    "function_location": "application",
    "function_com_id": 21,
    "function_vb_name": "ExeFolder",
    "function_name": "exe_folder",
    "function_parameters": (),
    "function_returns": ("string","null")
    }
exit = {
    "function_location": "application",
    "function_com_id": 537,
    "function_vb_name": "Exit",
    "function_name": "exit",
    "function_parameters": (),
    "function_returns": ()
    }
find_file = {
    "function_location": "application",
    "function_com_id": 81,
    "function_vb_name": "FindFile",
    "function_name": "find_file",
    "function_parameters": (("filename","str","REQ")),
    "function_returns": ("string","null")
    }
get_plug_in_object = {
    "function_location": "application",
    "function_com_id": 636,
    "function_vb_name": "GetPlugInObject",
    "function_name": "get_plug_in_object",
    "function_parameters": (("plug_in","str","REQ")),
    "function_returns": ("null")
    }
help = {
    "function_location": "application",
    "function_com_id": 22,
    "function_vb_name": "Help",
    "function_name": "help",
    "function_parameters": (("topic","int","OPT")),
    "function_returns": ("boolean")
    }
in_command = {
    "function_location": "application",
    "function_com_id": 596,
    "function_vb_name": "InCommand",
    "function_name": "in_command",
    "function_parameters": (("ignore_runners","bln","OPT")),
    "function_returns": ("number")
    }
install_folder = {
    "function_location": "application",
    "function_com_id": 23,
    "function_vb_name": "InstallFolder",
    "function_name": "install_folder",
    "function_parameters": (),
    "function_returns": ("string","null")
    }
is_alias = {
    "function_location": "application",
    "function_com_id": 711,
    "function_vb_name": "IsAlias",
    "function_name": "is_alias",
    "function_parameters": (("alias","str","REQ")),
    "function_returns": ("boolean","null")
    }
is_command = {
    "function_location": "application",
    "function_com_id": 530,
    "function_vb_name": "IsCommand",
    "function_name": "is_command",
    "function_parameters": (("command_name","str","REQ")),
    "function_returns": ("boolean","null")
    }
last_command_name = {
    "function_location": "application",
    "function_com_id": 594,
    "function_vb_name": "LastCommandName",
    "function_name": "last_command_name",
    "function_parameters": (),
    "function_returns": ("string")
    }
last_command_result = {
    "function_location": "application",
    "function_com_id": 292,
    "function_vb_name": "LastCommandResult",
    "function_name": "last_command_result",
    "function_parameters": (),
    "function_returns": ("number")
    }
last_loaded_script_file = {
    "function_location": "application",
    "function_com_id": 373,
    "function_vb_name": "LastLoadedScriptFile",
    "function_name": "last_loaded_script_file",
    "function_parameters": (),
    "function_returns": ("string","null")
    }
locale_i_d = {
    "function_location": "application",
    "function_com_id": 450,
    "function_vb_name": "LocaleID",
    "function_name": "locale_i_d",
    "function_parameters": (),
    "function_returns": ("number")
    }
ortho = {
    "function_location": "application",
    "function_com_id": 345,
    "function_vb_name": "Ortho",
    "function_name": "ortho",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
osnap = {
    "function_location": "application",
    "function_com_id": 347,
    "function_vb_name": "Osnap",
    "function_name": "osnap",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
osnap_dialog = {
    "function_location": "application",
    "function_com_id": 349,
    "function_vb_name": "OsnapDialog",
    "function_name": "osnap_dialog",
    "function_parameters": (("visible","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
osnap_mode = {
    "function_location": "application",
    "function_com_id": 343,
    "function_vb_name": "OsnapMode",
    "function_name": "osnap_mode",
    "function_parameters": (("mode","int","OPT")),
    "function_returns": ("number","number","null")
    }
planar = {
    "function_location": "application",
    "function_com_id": 346,
    "function_vb_name": "Planar",
    "function_name": "planar",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
plug_ins = {
    "function_location": "application",
    "function_com_id": 315,
    "function_vb_name": "PlugIns",
    "function_name": "plug_ins",
    "function_parameters": (("types","int","OPT"),("status","int","OPT")),
    "function_returns": ("array","null")
    }
print_ = {
    "function_location": "application",
    "function_com_id": 2,
    "function_vb_name": "Print",
    "function_name": "print_",
    "function_parameters": (("message","str","OPT")),
    "function_returns": ()
    }
print_ex = {
    "function_location": "application",
    "function_com_id": 370,
    "function_vb_name": "PrintEx",
    "function_name": "print_ex",
    "function_parameters": (("message","str","OPT")),
    "function_returns": ()
    }
project_osnaps = {
    "function_location": "application",
    "function_com_id": 348,
    "function_vb_name": "ProjectOsnaps",
    "function_name": "project_osnaps",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
prompt = {
    "function_location": "application",
    "function_com_id": 24,
    "function_vb_name": "Prompt",
    "function_name": "prompt",
    "function_parameters": (("prompt","str","OPT")),
    "function_returns": ()
    }
registry_key = {
    "function_location": "application",
    "function_com_id": 25,
    "function_vb_name": "RegistryKey",
    "function_name": "registry_key",
    "function_parameters": (),
    "function_returns": ("string","null")
    }
screen_size = {
    "function_location": "application",
    "function_com_id": 553,
    "function_vb_name": "ScreenSize",
    "function_name": "screen_size",
    "function_parameters": (),
    "function_returns": ("array","null")
    }
sdk_version = {
    "function_location": "application",
    "function_com_id": 359,
    "function_vb_name": "SdkVersion",
    "function_name": "sdk_version",
    "function_parameters": (),
    "function_returns": ("number","null")
    }
search_path_count = {
    "function_location": "application",
    "function_com_id": 509,
    "function_vb_name": "SearchPathCount",
    "function_name": "search_path_count",
    "function_parameters": (),
    "function_returns": ("number")
    }
search_path_list = {
    "function_location": "application",
    "function_com_id": 510,
    "function_vb_name": "SearchPathList",
    "function_name": "search_path_list",
    "function_parameters": (),
    "function_returns": ("array")
    }
send_keystrokes = {
    "function_location": "application",
    "function_com_id": 496,
    "function_vb_name": "SendKeystrokes",
    "function_name": "send_keystrokes",
    "function_parameters": (("keys","str","OPT"),("add_return","bln","OPT")),
    "function_returns": ()
    }
snap = {
    "function_location": "application",
    "function_com_id": 344,
    "function_vb_name": "Snap",
    "function_name": "snap",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("boolean","boolean")
    }
startup_script_count = {
    "function_location": "application",
    "function_com_id": 712,
    "function_vb_name": "StartupScriptCount",
    "function_name": "startup_script_count",
    "function_parameters": (),
    "function_returns": ("number")
    }
startup_script_list = {
    "function_location": "application",
    "function_com_id": 713,
    "function_vb_name": "StartupScriptList",
    "function_name": "startup_script_list",
    "function_parameters": (),
    "function_returns": ("array")
    }
status_bar_distance = {
    "function_location": "application",
    "function_com_id": 26,
    "function_vb_name": "StatusBarDistance",
    "function_name": "status_bar_distance",
    "function_parameters": (("distance","dbl","OPT")),
    "function_returns": ()
    }
status_bar_message = {
    "function_location": "application",
    "function_com_id": 28,
    "function_vb_name": "StatusBarMessage",
    "function_name": "status_bar_message",
    "function_parameters": (("message","str","OPT")),
    "function_returns": ()
    }
status_bar_number = {
    "function_location": "application",
    "function_com_id": 312,
    "function_vb_name": "StatusBarNumber",
    "function_name": "status_bar_number",
    "function_parameters": (("number","dbl","OPT")),
    "function_returns": ()
    }
status_bar_point = {
    "function_location": "application",
    "function_com_id": 27,
    "function_vb_name": "StatusBarPoint",
    "function_name": "status_bar_point",
    "function_parameters": (("point","array_of dbl","OPT")),
    "function_returns": ()
    }
template_file = {
    "function_location": "application",
    "function_com_id": 529,
    "function_vb_name": "TemplateFile",
    "function_name": "template_file",
    "function_parameters": (("filename","str","OPT")),
    "function_returns": ("string","string")
    }
template_folder = {
    "function_location": "application",
    "function_com_id": 528,
    "function_vb_name": "TemplateFolder",
    "function_name": "template_folder",
    "function_parameters": (("folder","str","OPT")),
    "function_returns": ("string","string")
    }
window_handle = {
    "function_location": "application",
    "function_com_id": 29,
    "function_vb_name": "WindowHandle",
    "function_name": "window_handle",
    "function_parameters": (),
    "function_returns": ("number")
    }
working_folder = {
    "function_location": "application",
    "function_com_id": 439,
    "function_vb_name": "WorkingFolder",
    "function_name": "working_folder",
    "function_parameters": (("enable","bln","OPT")),
    "function_returns": ("string","string")
    }
