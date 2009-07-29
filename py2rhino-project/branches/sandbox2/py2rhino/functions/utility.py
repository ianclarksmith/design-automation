# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def all_procedures(all=pythoncom.Empty):

    return _rsf.all_procedures(all)

def clipboard_text(text=pythoncom.Empty):

    return _rsf.clipboard_text(text)

def color_adjust_luma(r_g_b, luma, scale=pythoncom.Empty):

    return _rsf.color_adjust_luma(r_g_b, luma, scale)

def color_blue_value(r_g_b):

    return _rsf.color_blue_value(r_g_b)

def color_green_value(r_g_b):

    return _rsf.color_green_value(r_g_b)

def color_h_l_s_to_r_g_b(r_g_b):

    return _rsf.color_h_l_s_to_r_g_b(r_g_b)

def color_r_g_b_to_h_l_s(r_g_b):

    return _rsf.color_r_g_b_to_h_l_s(r_g_b)

def color_red_value(r_g_b):

    return _rsf.color_red_value(r_g_b)

def cull_duplicate_numbers(numbers, tolerance=pythoncom.Empty):

    return _rsf.cull_duplicate_numbers(numbers, tolerance)

def cull_duplicate_points(points, tolerance=pythoncom.Empty):

    return _rsf.cull_duplicate_points(points, tolerance)

def cull_duplicate_strings(strings, case_sensitive=pythoncom.Empty):

    return _rsf.cull_duplicate_strings(strings, case_sensitive)

def current_printer(printer=pythoncom.Empty):

    return _rsf.current_printer(printer)

def get_settings(filename, section=pythoncom.Empty, entry=pythoncom.Empty):

    return _rsf.get_settings(filename, section, entry)

def is_procedure(sub_name):

    return _rsf.is_procedure(sub_name)

def printer_names():

    return _rsf.printer_names()

def pt_2_str(point, precision=pythoncom.Empty, space=pythoncom.Empty):

    return _rsf.pt_2_str(point, precision, space)

def save_settings(filename, section=pythoncom.Empty, entry=pythoncom.Empty, string=pythoncom.Empty):

    return _rsf.save_settings(filename, section, entry, string)

def simplify_array(points):

    return _rsf.simplify_array(points)

def sleep(milliseconds):

    return _rsf.sleep(milliseconds)

def spool_to_printer(file, printer):

    return _rsf.spool_to_printer(file, printer)

def str_2_pt(point):

    return _rsf.str_2_pt(point)

def str_2_pt_array(points):

    return _rsf.str_2_pt_array(points)

def strtok(text, delimiters=pythoncom.Empty):

    return _rsf.strtok(text, delimiters)

def text_out(text, title=pythoncom.Empty):

    return _rsf.text_out(text, title)

def version():

    return _rsf.version()

