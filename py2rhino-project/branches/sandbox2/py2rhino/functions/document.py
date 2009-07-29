# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def create_preview_image(file, view=pythoncom.Empty, size=pythoncom.Empty, flags=pythoncom.Empty, wireframe=pythoncom.Empty):

    return _rsf.create_preview_image(file, view, size, flags, wireframe)

def document_modified(modified=pythoncom.Empty):

    return _rsf.document_modified(modified)

def document_name():

    return _rsf.document_name()

def document_path():

    return _rsf.document_path()

def document_u_r_l(u_r_l=pythoncom.Empty):

    return _rsf.document_u_r_l(u_r_l)

def enable_redraw(select=pythoncom.Empty):

    return _rsf.enable_redraw(select)

def extract_preview_image(file_name, model_name=pythoncom.Empty):

    return _rsf.extract_preview_image(file_name, model_name)

def is_document_modified():

    return _rsf.is_document_modified()

def notes(notes=pythoncom.Empty):

    return _rsf.notes(notes)

def read_file_version():

    return _rsf.read_file_version()

def redraw():

    return _rsf.redraw()

def render_antialias(style=pythoncom.Empty):

    return _rsf.render_antialias(style)

def render_color(item, color=pythoncom.Empty):

    return _rsf.render_color(item, color)

def render_mesh_density(density=pythoncom.Empty):

    return _rsf.render_mesh_density(density)

def render_mesh_max_angle(angle=pythoncom.Empty):

    return _rsf.render_mesh_max_angle(angle)

def render_mesh_max_aspect_ratio(ratio=pythoncom.Empty):

    return _rsf.render_mesh_max_aspect_ratio(ratio)

def render_mesh_max_dist_edge_to_srf(distance=pythoncom.Empty):

    return _rsf.render_mesh_max_dist_edge_to_srf(distance)

def render_mesh_max_edge_length(length=pythoncom.Empty):

    return _rsf.render_mesh_max_edge_length(length)

def render_mesh_min_edge_length(length=pythoncom.Empty):

    return _rsf.render_mesh_min_edge_length(length)

def render_mesh_min_initial_grid_quads(quads=pythoncom.Empty):

    return _rsf.render_mesh_min_initial_grid_quads(quads)

def render_mesh_quality(quality=pythoncom.Empty):

    return _rsf.render_mesh_quality(quality)

def render_mesh_settings(settings=pythoncom.Empty):

    return _rsf.render_mesh_settings(settings)

def render_resolution(resolution):

    return _rsf.render_resolution(resolution)

def render_settings(settings=pythoncom.Empty):

    return _rsf.render_settings(settings)

def unit_absolute_tolerance(abs_tol=pythoncom.Empty):

    return _rsf.unit_absolute_tolerance(abs_tol)

def unit_angle_tolerance(angle_tol=pythoncom.Empty):

    return _rsf.unit_angle_tolerance(angle_tol)

def unit_custom_unit_system(units, scale=pythoncom.Empty, name=pythoncom.Empty):

    return _rsf.unit_custom_unit_system(units, scale, name)

def unit_distance_display_mode(mode=pythoncom.Empty):

    return _rsf.unit_distance_display_mode(mode)

def unit_distance_display_precision(precision=pythoncom.Empty):

    return _rsf.unit_distance_display_precision(precision)

def unit_relative_tolerance(rel_tol=pythoncom.Empty):

    return _rsf.unit_relative_tolerance(rel_tol)

def unit_scale(to_system, from_system=pythoncom.Empty):

    return _rsf.unit_scale(to_system, from_system)

def unit_system(system=pythoncom.Empty, scale=pythoncom.Empty):

    return _rsf.unit_system(system, scale)

def unit_system_name(capitalize=pythoncom.Empty, singular=pythoncom.Empty, abbreviate=pythoncom.Empty):

    return _rsf.unit_system_name(capitalize, singular, abbreviate)

