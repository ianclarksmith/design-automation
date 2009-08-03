# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def enable_object_grips(object, enable=pythoncom.Empty):

    return _rsf.enable_object_grips(object, enable)

def get_object_grip(message=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty):

    return _rsf.get_object_grip(message, pre_select, select)

def get_object_grips(message=pythoncom.Empty, pre_select=pythoncom.Empty, select=pythoncom.Empty):

    return _rsf.get_object_grips(message, pre_select, select)

def next_object_grip(object, index, direction=pythoncom.Empty, enable=pythoncom.Empty):

    return _rsf.next_object_grip(object, index, direction, enable)

def object_grip_count(object):

    return _rsf.object_grip_count(object)

def object_grip_location(object, index, point=pythoncom.Empty):

    return _rsf.object_grip_location(object, index, point)

def object_grip_locations(object, points=pythoncom.Empty):

    return _rsf.object_grip_locations(object, points)

def object_grips_on(object):

    return _rsf.object_grips_on(object)

def object_grips_selected(object):

    return _rsf.object_grips_selected(object)

def prev_object_grip(object, index, direction=pythoncom.Empty, enable=pythoncom.Empty):

    return _rsf.prev_object_grip(object, index, direction, enable)

def select_object_grip(object, index):

    return _rsf.select_object_grip(object, index)

def select_object_grips(object):

    return _rsf.select_object_grips(object)

def selected_object_grips(object):

    return _rsf.selected_object_grips(object)

def unselect_object_grip(object, index):

    return _rsf.unselect_object_grip(object, index)

def unselect_object_grips(object):

    return _rsf.unselect_object_grips(object)

