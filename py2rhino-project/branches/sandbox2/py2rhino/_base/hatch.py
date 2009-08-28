# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_hatch(curve, hatch=pythoncom.Empty, scale=pythoncom.Empty, rotation=pythoncom.Empty):

    return _rsf.add_hatch(curve, hatch, scale, rotation)

def add_hatch_patterns(file_name, replace=pythoncom.Empty):

    return _rsf.add_hatch_patterns(file_name, replace)

def add_hatches(curves, hatch=pythoncom.Empty, scale=pythoncom.Empty, rotation=pythoncom.Empty):

    return _rsf.add_hatches(curves, hatch, scale, rotation)

def current_hatch_pattern(hatch=pythoncom.Empty):

    return _rsf.current_hatch_pattern(hatch)

def explode_hatch(hatch, delete=pythoncom.Empty):

    return _rsf.explode_hatch(hatch, delete)

def hatch_pattern(object, hatch=pythoncom.Empty):

    return _rsf.hatch_pattern(object, hatch)

def hatch_pattern_count():

    return _rsf.hatch_pattern_count()

def hatch_pattern_description(hatch):

    return _rsf.hatch_pattern_description(hatch)

def hatch_pattern_fill_type(hatch):

    return _rsf.hatch_pattern_fill_type(hatch)

def hatch_pattern_names():

    return _rsf.hatch_pattern_names()

def hatch_rotation(object, rotation=pythoncom.Empty):

    return _rsf.hatch_rotation(object, rotation)

def hatch_scale(object, scale=pythoncom.Empty):

    return _rsf.hatch_scale(object, scale)

def is_hatch(object):

    return _rsf.is_hatch(object)

def is_hatch_pattern(hatch):

    return _rsf.is_hatch_pattern(hatch)

def is_hatch_pattern_current(hatch):

    return _rsf.is_hatch_pattern_current(hatch)

def is_hatch_pattern_reference(hatch):

    return _rsf.is_hatch_pattern_reference(hatch)

