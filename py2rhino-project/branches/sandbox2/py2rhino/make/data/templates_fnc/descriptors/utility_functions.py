#The data below will be used to generate the Rhinoscript api

#Errors can be fixed by hand here

all_procedures = {
    "function_location": "utility",
    "function_com_id": 503,
    "function_vb_name": "AllProcedures",
    "function_name": "all_procedures",
    "function_parameters": (("all","bln","OPT")),
    "function_returns": ("array","null")
    }
clipboard_text = {
    "function_location": "utility",
    "function_com_id": 245,
    "function_vb_name": "ClipboardText",
    "function_name": "clipboard_text",
    "function_parameters": (("text","str","OPT")),
    "function_returns": ("string","string","null")
    }
color_adjust_luma = {
    "function_location": "utility",
    "function_com_id": 878,
    "function_vb_name": "ColorAdjustLuma",
    "function_name": "color_adjust_luma",
    "function_parameters": (("r_g_b","lng","REQ"),("luma","int","REQ"),("scale","bln","OPT")),
    "function_returns": ("number","null")
    }
color_blue_value = {
    "function_location": "utility",
    "function_com_id": 882,
    "function_vb_name": "ColorBlueValue",
    "function_name": "color_blue_value",
    "function_parameters": (("r_g_b","lng","REQ")),
    "function_returns": ("number","null")
    }
color_green_value = {
    "function_location": "utility",
    "function_com_id": 881,
    "function_vb_name": "ColorGreenValue",
    "function_name": "color_green_value",
    "function_parameters": (("r_g_b","lng","REQ")),
    "function_returns": ("number","null")
    }
color_h_l_s_to_r_g_b = {
    "function_location": "utility",
    "function_com_id": 877,
    "function_vb_name": "ColorHLSToRGB",
    "function_name": "color_h_l_s_to_r_g_b",
    "function_parameters": (("r_g_b","lng","REQ")),
    "function_returns": ("number","null")
    }
color_r_g_b_to_h_l_s = {
    "function_location": "utility",
    "function_com_id": 876,
    "function_vb_name": "ColorRGBToHLS",
    "function_name": "color_r_g_b_to_h_l_s",
    "function_parameters": (("r_g_b","lng","REQ")),
    "function_returns": ("array","null")
    }
color_red_value = {
    "function_location": "utility",
    "function_com_id": 880,
    "function_vb_name": "ColorRedValue",
    "function_name": "color_red_value",
    "function_parameters": (("r_g_b","lng","REQ")),
    "function_returns": ("number","null")
    }
cull_duplicate_numbers = {
    "function_location": "utility",
    "function_com_id": 550,
    "function_vb_name": "CullDuplicateNumbers",
    "function_name": "cull_duplicate_numbers",
    "function_parameters": (("numbers","array_of int","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("array","null")
    }
cull_duplicate_points = {
    "function_location": "utility",
    "function_com_id": 548,
    "function_vb_name": "CullDuplicatePoints",
    "function_name": "cull_duplicate_points",
    "function_parameters": (("points","array_of dbl","REQ"),("tolerance","dbl","OPT")),
    "function_returns": ("array","null")
    }
cull_duplicate_strings = {
    "function_location": "utility",
    "function_com_id": 549,
    "function_vb_name": "CullDuplicateStrings",
    "function_name": "cull_duplicate_strings",
    "function_parameters": (("strings","array_of int","REQ"),("case_sensitive","bln","OPT")),
    "function_returns": ("array","null")
    }
current_printer = {
    "function_location": "utility",
    "function_com_id": 358,
    "function_vb_name": "CurrentPrinter",
    "function_name": "current_printer",
    "function_parameters": (("printer","str","OPT")),
    "function_returns": ("string","string","null")
    }
get_settings = {
    "function_location": "utility",
    "function_com_id": 246,
    "function_vb_name": "GetSettings",
    "function_name": "get_settings",
    "function_parameters": (("filename","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "function_returns": ("array","array","string","null")
    }
is_procedure = {
    "function_location": "utility",
    "function_com_id": 287,
    "function_vb_name": "IsProcedure",
    "function_name": "is_procedure",
    "function_parameters": (("sub_name","str","REQ")),
    "function_returns": ("boolean","null")
    }
printer_names = {
    "function_location": "utility",
    "function_com_id": 356,
    "function_vb_name": "PrinterNames",
    "function_name": "printer_names",
    "function_parameters": (),
    "function_returns": ("array","null")
    }
pt2_str = {
    "function_location": "utility",
    "function_com_id": 297,
    "function_vb_name": "Pt2Str",
    "function_name": "pt2_str",
    "function_parameters": (("point","array_of dbl","REQ"),("precision","n","OPT"),("space","bln","OPT")),
    "function_returns": ("string","null")
    }
save_settings = {
    "function_location": "utility",
    "function_com_id": 247,
    "function_vb_name": "SaveSettings",
    "function_name": "save_settings",
    "function_parameters": (("filename","str","REQ"),("section","str","OPT"),("entry","str","OPT"),("string","str","OPT")),
    "function_returns": ("boolean","null")
    }
simplify_array = {
    "function_location": "utility",
    "function_com_id": 597,
    "function_vb_name": "SimplifyArray",
    "function_name": "simplify_array",
    "function_parameters": (("points","array_of dbl","REQ")),
    "function_returns": ("array","null")
    }
sleep = {
    "function_location": "utility",
    "function_com_id": 248,
    "function_vb_name": "Sleep",
    "function_name": "sleep",
    "function_parameters": (("milliseconds","lng","REQ")),
    "function_returns": ("null")
    }
spool_to_printer = {
    "function_location": "utility",
    "function_com_id": 357,
    "function_vb_name": "SpoolToPrinter",
    "function_name": "spool_to_printer",
    "function_parameters": (("file","str","REQ"),("printer","str","REQ")),
    "function_returns": ("string","null")
    }
str2_pt = {
    "function_location": "utility",
    "function_com_id": 409,
    "function_vb_name": "Str2Pt",
    "function_name": "str2_pt",
    "function_parameters": (("point","str","REQ")),
    "function_returns": ("array","null")
    }
str2_pt_array = {
    "function_location": "utility",
    "function_com_id": 410,
    "function_vb_name": "Str2PtArray",
    "function_name": "str2_pt_array",
    "function_parameters": (("points","str","REQ")),
    "function_returns": ("array","null")
    }
strtok = {
    "function_location": "utility",
    "function_com_id": 250,
    "function_vb_name": "Strtok",
    "function_name": "strtok",
    "function_parameters": (("text","str","REQ"),("delimiters","str","OPT")),
    "function_returns": ("array","null")
    }
text_out = {
    "function_location": "utility",
    "function_com_id": 755,
    "function_vb_name": "TextOut",
    "function_name": "text_out",
    "function_parameters": (("text","str","REQ"),("title","str","OPT")),
    "function_returns": ("null")
    }
version = {
    "function_location": "utility",
    "function_com_id": 288,
    "function_vb_name": "Version",
    "function_name": "version",
    "function_parameters": (),
    "function_returns": ("number")
    }
