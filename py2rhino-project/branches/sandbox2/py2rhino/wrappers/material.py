# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_material_to_layer(object):

    return _rsf.add_material_to_layer(object)

def add_material_to_object(object):

    return _rsf.add_material_to_object(object)

def copy_material(src_index, dst_index):

    return _rsf.copy_material(src_index, dst_index)

def is_material_default(material_index):

    return _rsf.is_material_default(material_index)

def is_material_reference(material_index):

    return _rsf.is_material_reference(material_index)

def match_material(src_material_index):

    return _rsf.match_material(src_material_index)

def match_material_2(src_object, dest_objects):

    return _rsf.match_material_2(src_object, dest_objects)

def material_bump(material_index, file_name=pythoncom.Empty):

    return _rsf.material_bump(material_index, file_name)

def material_color(material_index, color=pythoncom.Empty):

    return _rsf.material_color(material_index, color)

def material_environment_map(material_index, file_name=pythoncom.Empty):

    return _rsf.material_environment_map(material_index, file_name)

def material_name(material_index, name=pythoncom.Empty):

    return _rsf.material_name(material_index, name)

def material_reflective_color(material_index, color=pythoncom.Empty):

    return _rsf.material_reflective_color(material_index, color)

def material_shine(material_index, shine=pythoncom.Empty):

    return _rsf.material_shine(material_index, shine)

def material_texture(material_index, file_name=pythoncom.Empty):

    return _rsf.material_texture(material_index, file_name)

def material_transparency(material_index, transparency=pythoncom.Empty):

    return _rsf.material_transparency(material_index, transparency)

def material_transparency_map(material_index, file_name=pythoncom.Empty):

    return _rsf.material_transparency_map(material_index, file_name)

