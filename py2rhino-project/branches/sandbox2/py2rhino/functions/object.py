# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_object_mesh(object, quality=pythoncom.Empty, enable=pythoncom.Empty):

    return _rsf.add_object_mesh(object, quality, enable)

def box_morph_object(objects, box_points, copy=pythoncom.Empty):

    return _rsf.box_morph_object(objects, box_points, copy)

def copy_objects(objects, start=pythoncom.Empty, end=pythoncom.Empty):

    return _rsf.copy_objects(objects, start, end)

def copy_objects_2(translation=pythoncom.Empty):

    return _rsf.copy_objects_2(translation)

def delete_objects(objects):

    return _rsf.delete_objects(objects)

def enable_object_mesh(objects, enable=pythoncom.Empty):

    return _rsf.enable_object_mesh(objects, enable)

def flash_object(objects, style=pythoncom.Empty):

    return _rsf.flash_object(objects, style)

def hide_objects(objects):

    return _rsf.hide_objects(objects)

def is_layout_object(object):

    return _rsf.is_layout_object(object)

def is_object(object):

    return _rsf.is_object(object)

def is_object_hidden(object):

    return _rsf.is_object_hidden(object)

def is_object_in_box(object, box, mode=pythoncom.Empty):

    return _rsf.is_object_in_box(object, box, mode)

def is_object_in_group(object, group=pythoncom.Empty):

    return _rsf.is_object_in_group(object, group)

def is_object_locked(object):

    return _rsf.is_object_locked(object)

def is_object_normal(object):

    return _rsf.is_object_normal(object)

def is_object_reference(object):

    return _rsf.is_object_reference(object)

def is_object_selectable(object):

    return _rsf.is_object_selectable(object)

def is_object_selected(object):

    return _rsf.is_object_selected(object)

def is_object_solid(object):

    return _rsf.is_object_solid(object)

def is_object_valid(object):

    return _rsf.is_object_valid(object)

def is_visible_in_view(object, view=pythoncom.Empty):

    return _rsf.is_visible_in_view(object, view)

def lock_objects(objects):

    return _rsf.lock_objects(objects)

def match_object_attributes(targets, source=pythoncom.Empty):

    return _rsf.match_object_attributes(targets, source)

def mirror_objects(objects, start_pt, end_pt, copy=pythoncom.Empty):

    return _rsf.mirror_objects(objects, start_pt, end_pt, copy)

def move_objects(objects, start, end):

    return _rsf.move_objects(objects, start, end)

def move_objects_2(translation):

    return _rsf.move_objects_2(translation)

def object_color(objects, color=pythoncom.Empty):

    return _rsf.object_color(objects, color)

def object_color_source(objects, source=pythoncom.Empty):

    return _rsf.object_color_source(objects, source)

def object_description(object):

    return _rsf.object_description(object)

def object_dump(object, type=pythoncom.Empty):

    return _rsf.object_dump(object, type)

def object_groups(object):

    return _rsf.object_groups(object)

def object_has_mesh(object):

    return _rsf.object_has_mesh(object)

def object_layer(objects, layer=pythoncom.Empty):

    return _rsf.object_layer(objects, layer)

def object_layout(object, layout=pythoncom.Empty, return_name=pythoncom.Empty):

    return _rsf.object_layout(object, layout, return_name)

def object_linetype(objects, layer=pythoncom.Empty):

    return _rsf.object_linetype(objects, layer)

def object_linetype_source(objects, source=pythoncom.Empty):

    return _rsf.object_linetype_source(objects, source)

def object_material_index(object):

    return _rsf.object_material_index(object)

def object_material_source(objects, source=pythoncom.Empty):

    return _rsf.object_material_source(objects, source)

def object_mesh_density(object, density=pythoncom.Empty):

    return _rsf.object_mesh_density(object, density)

def object_mesh_max_angle(object, angle=pythoncom.Empty):

    return _rsf.object_mesh_max_angle(object, angle)

def object_mesh_max_aspect_ratio(object, ratio=pythoncom.Empty):

    return _rsf.object_mesh_max_aspect_ratio(object, ratio)

def object_mesh_max_dist_edge_to_srf(object, distance=pythoncom.Empty):

    return _rsf.object_mesh_max_dist_edge_to_srf(object, distance)

def object_mesh_max_edge_length(object, length=pythoncom.Empty):

    return _rsf.object_mesh_max_edge_length(object, length)

def object_mesh_min_edge_length(object, length=pythoncom.Empty):

    return _rsf.object_mesh_min_edge_length(object, length)

def object_mesh_min_initial_grid_quads(object, quads=pythoncom.Empty):

    return _rsf.object_mesh_min_initial_grid_quads(object, quads)

def object_mesh_quality(object, quality=pythoncom.Empty):

    return _rsf.object_mesh_quality(object, quality)

def object_mesh_settings(object, settings=pythoncom.Empty):

    return _rsf.object_mesh_settings(object, settings)

def object_names(objects, names=pythoncom.Empty):

    return _rsf.object_names(objects, names)

def object_print_color(objects, color=pythoncom.Empty):

    return _rsf.object_print_color(objects, color)

def object_print_color_source(objects, source=pythoncom.Empty):

    return _rsf.object_print_color_source(objects, source)

def object_print_width(objects, width=pythoncom.Empty):

    return _rsf.object_print_width(objects, width)

def object_print_width_source(objects, source=pythoncom.Empty):

    return _rsf.object_print_width_source(objects, source)

def object_top_group(object):

    return _rsf.object_top_group(object)

def object_type(object):

    return _rsf.object_type(object)

def object_u_r_l(objects, u_r_l=pythoncom.Empty):

    return _rsf.object_u_r_l(objects, u_r_l)

def orient_objects(objects, reference, target, flags=pythoncom.Empty):

    return _rsf.orient_objects(objects, reference, target, flags)

def remap_objects(object, src_plane, dst_plane, copy=pythoncom.Empty):

    return _rsf.remap_objects(object, src_plane, dst_plane, copy)

def rotate_objects(objects, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):

    return _rsf.rotate_objects(objects, point, angle, axis, copy)

def scale_objects(objects, origin, scale, copy=pythoncom.Empty):

    return _rsf.scale_objects(objects, origin, scale, copy)

def select_objects(objects):

    return _rsf.select_objects(objects)

def shear_objects(objects, origin, ref_pt, scale, copy=pythoncom.Empty):

    return _rsf.shear_objects(objects, origin, ref_pt, scale, copy)

def show_objects(objects):

    return _rsf.show_objects(objects)

def transform_objects(objects, matrix, copy=pythoncom.Empty):

    return _rsf.transform_objects(objects, matrix, copy)

def unlock_objects(objects):

    return _rsf.unlock_objects(objects)

def unselect_objects(objects):

    return _rsf.unselect_objects(objects)

