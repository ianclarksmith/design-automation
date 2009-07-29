# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_clipping_plane(plane, d_u, d_v, views=pythoncom.Empty):

    return _rsf.add_clipping_plane(plane, d_u, d_v, views)

def add_point_cloud(points):

    return _rsf.add_point_cloud(points)

def add_points(points):

    return _rsf.add_points(points)

def add_text(text, point, height=pythoncom.Empty, font=pythoncom.Empty, style=pythoncom.Empty):

    return _rsf.add_text(text, point, height, font, style)

def add_text_2(text, plane, height=pythoncom.Empty, font=pythoncom.Empty, style=pythoncom.Empty):

    return _rsf.add_text_2(text, plane, height, font, style)

def add_text_dot(test, point):

    return _rsf.add_text_dot(test, point)

def bounding_box(objects, view=pythoncom.Empty, world_coords=pythoncom.Empty):

    return _rsf.bounding_box(objects, view, world_coords)

def compare_geometry(object_1, object_2):

    return _rsf.compare_geometry(object_1, object_2)

def is_clipping_plane(object):

    return _rsf.is_clipping_plane(object)

def is_point(object):

    return _rsf.is_point(object)

def is_point_cloud(object):

    return _rsf.is_point_cloud(object)

def is_text(object):

    return _rsf.is_text(object)

def is_text_dot(object):

    return _rsf.is_text_dot(object)

def point_cloud_count(object):

    return _rsf.point_cloud_count(object)

def point_cloud_points(object):

    return _rsf.point_cloud_points(object)

def point_coordinates(object, point=pythoncom.Empty):

    return _rsf.point_coordinates(object, point)

def text_dot_point(object, point=pythoncom.Empty):

    return _rsf.text_dot_point(object, point)

def text_dot_text(object, text=pythoncom.Empty):

    return _rsf.text_dot_text(object, text)

def text_object_font(object, font=pythoncom.Empty):

    return _rsf.text_object_font(object, font)

def text_object_height(object, height=pythoncom.Empty):

    return _rsf.text_object_height(object, height)

def text_object_plane(object, plane=pythoncom.Empty):

    return _rsf.text_object_plane(object, plane)

def text_object_point(object, point=pythoncom.Empty):

    return _rsf.text_object_point(object, point)

def text_object_style(object, style=pythoncom.Empty):

    return _rsf.text_object_style(object, style)

def text_object_text(object, text=pythoncom.Empty):

    return _rsf.text_object_text(object, text)

