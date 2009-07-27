#The data below will be used to generate the Rhinoscript functions

#Errors can be fixed by hand here

all_procedures = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "all_procedures",
    "method_parameters": (("all","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
clipboard_text = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "clipboard_text",
    "method_parameters": (("text","str","OPT")),
    "method_returns": (""string"",""string"",""null"")
    }
color_adjust_luma = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "color_adjust_luma",
    "method_parameters": (("r_g_b","lng","REQ"),("luma","int","REQ"),("scale","bln","OPT")),
    "method_returns": (""number"",""null"")
    }
color_blue_value = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "color_blue_value",
    "method_parameters": (("r_g_b","lng","REQ")),
    "method_returns": (""number"",""null"")
    }
color_green_value = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "color_green_value",
    "method_parameters": (("r_g_b","lng","REQ")),
    "method_returns": (""number"",""null"")
    }
color_h_l_s_to_r_g_b = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "color_h_l_s_to_r_g_b",
    "method_parameters": (("r_g_b","lng","REQ")),
    "method_returns": (""number"",""null"")
    }
color_r_g_b_to_h_l_s = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "color_r_g_b_to_h_l_s",
    "method_parameters": (("r_g_b","lng","REQ")),
    "method_returns": (""array"",""null"")
    }
color_red_value = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "color_red_value",
    "method_parameters": (("r_g_b","lng","REQ")),
    "method_returns": (""number"",""null"")
    }
cull_duplicate_numbers = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "cull_duplicate_numbers",
    "method_parameters": (("numbers","arr_of_int","REQ"),("tolerance","dbl","OPT")),
    "method_returns": (""array"",""null"")
    }
cull_duplicate_points = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "cull_duplicate_points",
    "method_parameters": (("points","arr_of_dbl","REQ"),("tolerance","dbl","OPT")),
    "method_returns": (""array"",""null"")
    }
cull_duplicate_strings = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "cull_duplicate_strings",
    "method_parameters": (("strings","arr_of_int","REQ"),("case_sensitive","bln","OPT")),
    "method_returns": (""array"",""null"")
    }
current_printer = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "current_printer",
    "method_parameters": (("printer","str","OPT")),
    "method_returns": (""string"",""string"",""null"")
    }
get_settings = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "get_settings",
    "method_parameters": (("filename","str","REQ"),("section","str","OPT"),("entry","str","OPT")),
    "method_returns": (""array"",""array"",""string"",""null"")
    }
is_procedure = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "is_procedure",
    "method_parameters": (("sub_name","str","REQ")),
    "method_returns": (""boolean"",""null"")
    }
printer_names = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "printer_names",
    "method_parameters": (),
    "method_returns": (""array"",""null"")
    }
pt2_str = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "pt2_str",
    "method_parameters": (("point","arr_of_dbl","REQ"),("precision","n","OPT"),("space","bln","OPT")),
    "method_returns": (""string"",""null"")
    }
save_settings = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "save_settings",
    "method_parameters": (("filename","str","REQ"),("section","str","OPT"),("entry","str","OPT"),("string","str","OPT")),
    "method_returns": (""boolean"",""null"")
    }
simplify_array = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "simplify_array",
    "method_parameters": (("points","arr_of_dbl","REQ")),
    "method_returns": (""array"",""null"")
    }
sleep = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "sleep",
    "method_parameters": (("milliseconds","lng","REQ")),
    "method_returns": (""null"")
    }
spool_to_printer = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "spool_to_printer",
    "method_parameters": (("file","str","REQ"),("printer","str","REQ")),
    "method_returns": (""string"",""null"")
    }
str2_pt = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "str2_pt",
    "method_parameters": (("point","str","REQ")),
    "method_returns": (""array"",""null"")
    }
str2_pt_array = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "str2_pt_array",
    "method_parameters": (("points","str","REQ")),
    "method_returns": (""array"",""null"")
    }
strtok = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "strtok",
    "method_parameters": (("text","str","REQ"),("delimiters","str","OPT")),
    "method_returns": (""array"",""null"")
    }
text_out = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "text_out",
    "method_parameters": (("text","str","REQ"),("title","str","OPT")),
    "method_returns": (""null"")
    }
version = {
    "method_location": "Utility",
    "method_type": "METHOD",
    "method_name": "version",
    "method_parameters": (),
    "method_returns": (""number"")
    }
