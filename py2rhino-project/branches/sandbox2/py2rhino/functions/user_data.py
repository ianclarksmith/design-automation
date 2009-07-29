# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def attribute_data_count(object):

    return _rsf.attribute_data_count(object)

def delete_attribute_data(object, section=pythoncom.Empty, entry=pythoncom.Empty):

    return _rsf.delete_attribute_data(object, section, entry)

def delete_document_data(section=pythoncom.Empty, entry=pythoncom.Empty):

    return _rsf.delete_document_data(section, entry)

def delete_object_data(object, section=pythoncom.Empty, entry=pythoncom.Empty):

    return _rsf.delete_object_data(object, section, entry)

def document_data_count():

    return _rsf.document_data_count()

def get_attribute_data(object, section=pythoncom.Empty, entry=pythoncom.Empty):

    return _rsf.get_attribute_data(object, section, entry)

def get_document_data(section=pythoncom.Empty, entry=pythoncom.Empty):

    return _rsf.get_document_data(section, entry)

def get_object_data(object, section=pythoncom.Empty, entry=pythoncom.Empty):

    return _rsf.get_object_data(object, section, entry)

def get_user_text(object, key=pythoncom.Empty, attach_to_geometry=pythoncom.Empty):

    return _rsf.get_user_text(object, key, attach_to_geometry)

def is_attribute_data(object):

    return _rsf.is_attribute_data(object)

def is_document_data():

    return _rsf.is_document_data()

def is_object_data(object):

    return _rsf.is_object_data(object)

def is_user_text(object):

    return _rsf.is_user_text(object)

def object_data_count(object):

    return _rsf.object_data_count(object)

def set_attribute_data(object, section, entry, value):

    return _rsf.set_attribute_data(object, section, entry, value)

def set_document_data(section, entry, value):

    return _rsf.set_document_data(section, entry, value)

def set_object_data(object, section, entry, value):

    return _rsf.set_object_data(object, section, entry, value)

def set_user_text(object, key, value=pythoncom.Empty, attach_to_geometry=pythoncom.Empty):

    return _rsf.set_user_text(object, key, value, attach_to_geometry)

