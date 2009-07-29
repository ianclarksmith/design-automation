# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def browse_for_folder(folder=pythoncom.Empty, message=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.browse_for_folder(folder, message, title)

def check_list_box(items, values, message=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.check_list_box(items, values, message, title)

def combo_list_box(items, message=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.combo_list_box(items, message, title)

def edit_box(string=pythoncom.Empty, message=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.edit_box(string, message, title)

def get_angle(point=pythoncom.Empty, reference=pythoncom.Empty, angle=pythoncom.Empty, message=pythoncom.Empty):

    return _rsf.get_angle(point, reference, angle, message)

def get_boolean(message, items, defaults):

    return _rsf.get_boolean(message, items, defaults)

def get_box(mode=pythoncom.Empty, point=pythoncom.Empty, prompt_1=pythoncom.Empty, prompt_2=pythoncom.Empty, prompt_3=pythoncom.Empty):

    return _rsf.get_box(mode, point, prompt_1, prompt_2, prompt_3)

def get_color(color=pythoncom.Empty):

    return _rsf.get_color(color)

def get_distance(point=pythoncom.Empty, distance=pythoncom.Empty, message_1=pythoncom.Empty, message_2=pythoncom.Empty):

    return _rsf.get_distance(point, distance, message_1, message_2)

def get_integer(message=pythoncom.Empty, number=pythoncom.Empty, min=pythoncom.Empty, max=pythoncom.Empty):

    return _rsf.get_integer(message, number, min, max)

def get_layer(title=pythoncom.Empty, layer=pythoncom.Empty, show_new_layer=pythoncom.Empty, show_set_current=pythoncom.Empty):

    return _rsf.get_layer(title, layer, show_new_layer, show_set_current)

def get_linetype(linetype=pythoncom.Empty):

    return _rsf.get_linetype(linetype)

def get_point_on_curve(object, message=pythoncom.Empty):

    return _rsf.get_point_on_curve(object, message)

def get_point_on_line(message, start, end, track=pythoncom.Empty):

    return _rsf.get_point_on_line(message, start, end, track)

def get_point_on_mesh(object, message=pythoncom.Empty):

    return _rsf.get_point_on_mesh(object, message)

def get_point_on_plane(message=pythoncom.Empty, plane=pythoncom.Empty, point=pythoncom.Empty):

    return _rsf.get_point_on_plane(message, plane, point)

def get_point_on_surface(object, message=pythoncom.Empty):

    return _rsf.get_point_on_surface(object, message)

def get_points(draw=pythoncom.Empty, plane=pythoncom.Empty, message_1=pythoncom.Empty, message_2=pythoncom.Empty, max_points=pythoncom.Empty, base_point=pythoncom.Empty):

    return _rsf.get_points(draw, plane, message_1, message_2, max_points, base_point)

def get_print_width(print_width=pythoncom.Empty):

    return _rsf.get_print_width(print_width)

def get_real(message=pythoncom.Empty, number=pythoncom.Empty, min=pythoncom.Empty, max=pythoncom.Empty):

    return _rsf.get_real(message, number, min, max)

def get_rectangle(mode=pythoncom.Empty, point=pythoncom.Empty, prompt_1=pythoncom.Empty, prompt_2=pythoncom.Empty, prompt_3=pythoncom.Empty):

    return _rsf.get_rectangle(mode, point, prompt_1, prompt_2, prompt_3)

def get_string(message=pythoncom.Empty, string=pythoncom.Empty, strings=pythoncom.Empty):

    return _rsf.get_string(message, string, strings)

def get_surface_iso_param_point(object, message=pythoncom.Empty):

    return _rsf.get_surface_iso_param_point(object, message)

def html_box(file_name, arguments=pythoncom.Empty, options=pythoncom.Empty, modal=pythoncom.Empty):

    return _rsf.html_box(file_name, arguments, options, modal)

def integer_box(message=pythoncom.Empty, number=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.integer_box(message, number, title)

def list_box(items, message=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.list_box(items, message, title)

def message_beep(beep=pythoncom.Empty):

    return _rsf.message_beep(beep)

def message_box(message, buttons=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.message_box(message, buttons, title)

def multi_list_box(items, message=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.multi_list_box(items, message, title)

def open_file_names(title=pythoncom.Empty, filter=pythoncom.Empty, folder=pythoncom.Empty, filename=pythoncom.Empty, extension=pythoncom.Empty):

    return _rsf.open_file_names(title, filter, folder, filename, extension)

def popup_menu(items, modes=pythoncom.Empty, point=pythoncom.Empty, view=pythoncom.Empty):

    return _rsf.popup_menu(items, modes, point, view)

def property_list_box(items, values, message=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.property_list_box(items, values, message, title)

def real_box(message=pythoncom.Empty, number=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.real_box(message, number, title)

def save_file_name(title=pythoncom.Empty, filter=pythoncom.Empty, folder=pythoncom.Empty, filename=pythoncom.Empty, extension=pythoncom.Empty):

    return _rsf.save_file_name(title, filter, folder, filename, extension)

def string_box(message=pythoncom.Empty, string=pythoncom.Empty, title=pythoncom.Empty):

    return _rsf.string_box(message, string, title)

