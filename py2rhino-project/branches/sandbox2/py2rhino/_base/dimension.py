# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_dim_style(dim_style=pythoncom.Empty):

    return _rsf.add_dim_style(dim_style)

def add_leader(points, view=pythoncom.Empty, text=pythoncom.Empty):

    return _rsf.add_leader(points, view, text)

def current_dim_style(dim_style=pythoncom.Empty):

    return _rsf.current_dim_style(dim_style)

def delete_dim_style(dim_style):

    return _rsf.delete_dim_style(dim_style)

def dim_scale(scale=pythoncom.Empty):

    return _rsf.dim_scale(scale)

def dim_style_angle_precision(dim_style, precision=pythoncom.Empty):

    return _rsf.dim_style_angle_precision(dim_style, precision)

def dim_style_arrow_size(dim_style, size=pythoncom.Empty):

    return _rsf.dim_style_arrow_size(dim_style, size)

def dim_style_count():

    return _rsf.dim_style_count()

def dim_style_extension(dim_style, extension=pythoncom.Empty):

    return _rsf.dim_style_extension(dim_style, extension)

def dim_style_font(dim_style, font=pythoncom.Empty):

    return _rsf.dim_style_font(dim_style, font)

def dim_style_leader_arrow_size(dim_style, size=pythoncom.Empty):

    return _rsf.dim_style_leader_arrow_size(dim_style, size)

def dim_style_linear_precision(dim_style, precision=pythoncom.Empty):

    return _rsf.dim_style_linear_precision(dim_style, precision)

def dim_style_names(sort=pythoncom.Empty):

    return _rsf.dim_style_names(sort)

def dim_style_number_format(dim_style, format=pythoncom.Empty):

    return _rsf.dim_style_number_format(dim_style, format)

def dim_style_offset(dim_style, offset=pythoncom.Empty):

    return _rsf.dim_style_offset(dim_style, offset)

def dim_style_text_alignment(dim_style, alignment=pythoncom.Empty):

    return _rsf.dim_style_text_alignment(dim_style, alignment)

def dim_style_text_gap(dim_style, gap=pythoncom.Empty):

    return _rsf.dim_style_text_gap(dim_style, gap)

def dim_style_text_height(dim_style, height=pythoncom.Empty):

    return _rsf.dim_style_text_height(dim_style, height)

def dimension_style(object, style=pythoncom.Empty):

    return _rsf.dimension_style(object, style)

def dimension_text(object):

    return _rsf.dimension_text(object)

def dimension_user_text(object, user_text=pythoncom.Empty):

    return _rsf.dimension_user_text(object, user_text)

def dimension_value(object):

    return _rsf.dimension_value(object)

def is_aligned_dimension(object):

    return _rsf.is_aligned_dimension(object)

def is_angular_dimension(object):

    return _rsf.is_angular_dimension(object)

def is_diameter_dimension(object):

    return _rsf.is_diameter_dimension(object)

def is_dim_style(dim_style):

    return _rsf.is_dim_style(dim_style)

def is_dim_style_reference(dim_style):

    return _rsf.is_dim_style_reference(dim_style)

def is_dimension(object):

    return _rsf.is_dimension(object)

def is_leader(object):

    return _rsf.is_leader(object)

def is_linear_dimension(object):

    return _rsf.is_linear_dimension(object)

def is_ordinate_dimension(object):

    return _rsf.is_ordinate_dimension(object)

def is_radial_dimension(object):

    return _rsf.is_radial_dimension(object)

def leader_text(object, text=pythoncom.Empty):

    return _rsf.leader_text(object, text)

def rename_dim_style(old_style, new_style):

    return _rsf.rename_dim_style(old_style, new_style)

