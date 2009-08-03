# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def all_objects(select=pythoncom.Empty, include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.all_objects(select, include_lights, include_grips)

def first_object(select=pythoncom.Empty, include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.first_object(select, include_lights, include_grips)

def get_curve_object(message=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty):

    return _rsf.get_curve_object(message, pre_select, select)

def get_object(message=pythoncom.Empty, type=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty, objects=pythoncom.Empty):

    return _rsf.get_object(message, type, pre_select, select, objects)

def get_object_ex(message=pythoncom.Empty, type=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty, objects=pythoncom.Empty):

    return _rsf.get_object_ex(message, type, pre_select, select, objects)

def get_objects(message=pythoncom.Empty, type=pythoncom.Empty, group=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty, objects=pythoncom.Empty):

    return _rsf.get_objects(message, type, group, pre_select, select, objects)

def get_objects_ex(message=pythoncom.Empty, type=pythoncom.Empty, group=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty, objects=pythoncom.Empty):

    return _rsf.get_objects_ex(message, type, group, pre_select, select, objects)

def get_point_coordinates(message=pythoncom.Empty, pre_select=pythoncom.Empty):

    return _rsf.get_point_coordinates(message, pre_select)

def get_surface_object(message=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty):

    return _rsf.get_surface_object(message, pre_select, select)

def hidden_objects(include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.hidden_objects(include_lights, include_grips)

def invert_selected_objects(include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.invert_selected_objects(include_lights, include_grips)

def last_created_objects(select=pythoncom.Empty):

    return _rsf.last_created_objects(select)

def last_object(select=pythoncom.Empty, include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.last_object(select, include_lights, include_grips)

def locked_objects(include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.locked_objects(include_lights, include_grips)

def next_object(object, select=pythoncom.Empty, include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.next_object(object, select, include_lights, include_grips)

def normal_objects(include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.normal_objects(include_lights, include_grips)

def objects_by_color(color, select=pythoncom.Empty, include_lights=pythoncom.Empty):

    return _rsf.objects_by_color(color, select, include_lights)

def objects_by_group(group, select=pythoncom.Empty):

    return _rsf.objects_by_group(group, select)

def objects_by_layer(layer, select=pythoncom.Empty):

    return _rsf.objects_by_layer(layer, select)

def objects_by_name(name, select=pythoncom.Empty, include_lights=pythoncom.Empty):

    return _rsf.objects_by_name(name, select, include_lights)

def objects_by_type(type, select=pythoncom.Empty):

    return _rsf.objects_by_type(type, select)

def objects_by_u_r_l(u_r_l, select=pythoncom.Empty, include_lights=pythoncom.Empty):

    return _rsf.objects_by_u_r_l(u_r_l, select, include_lights)

def prev_selected_objects(select=pythoncom.Empty):

    return _rsf.prev_selected_objects(select)

def reference_objects(include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.reference_objects(include_lights, include_grips)

def selected_objects(include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.selected_objects(include_lights, include_grips)

def unselect_all_objects():

    return _rsf.unselect_all_objects()

def unselected_objects(select=pythoncom.Empty, include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.unselected_objects(select, include_lights, include_grips)

def visible_objects(view=pythoncom.Empty, select=pythoncom.Empty, include_lights=pythoncom.Empty, include_grips=pythoncom.Empty):

    return _rsf.visible_objects(view, select, include_lights, include_grips)

