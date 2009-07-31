# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _Object(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    def add_object_mesh(self, quality=pythoncom.Empty, enable=pythoncom.Empty):

        return _rsf.add_object_mesh(self.rhino_id, quality, enable)


    def box_morph(self, box_points, copy=pythoncom.Empty):

        return _rsf.box_morph_object(self.rhino_id, box_points, copy)


    def copy(self, start=pythoncom.Empty, end=pythoncom.Empty):

        return _rsf.copy_objects(self.rhino_id, start, end)


    def copy_and_xform(self, translation=pythoncom.Empty):

        return _rsf.copy_objects_2(self.rhino_id, translation)


    def delete(self, ):

        return _rsf.delete_objects(self.rhino_id)


    def enable_render_mesh(self, enable=pythoncom.Empty):

        return _rsf.enable_object_mesh(self.rhino_id, enable)


    def flash(self, style=pythoncom.Empty):

        return _rsf.flash_object(self.rhino_id, style)


    def hide(self, ):

        return _rsf.hide_objects(self.rhino_id)


    def is_arc(self, index=pythoncom.Empty):

        return _rsf.is_arc(self.rhino_id, index)


    def is_circle(self, index=pythoncom.Empty):

        return _rsf.is_circle(self.rhino_id, index)


    def is_curve(self, index=pythoncom.Empty):

        return _rsf.is_curve(self.rhino_id, index)


    def is_curve_closable(self, tolerance=pythoncom.Empty):

        return _rsf.is_curve_closable(self.rhino_id, tolerance)


    def is_curve_closed(self, index=pythoncom.Empty):

        return _rsf.is_curve_closed(self.rhino_id, index)


    def in_plane(self, plane=pythoncom.Empty):

        return _rsf.is_curve_in_plane(self.rhino_id, plane)


    def is_curve_linear(self, index=pythoncom.Empty):

        return _rsf.is_curve_linear(self.rhino_id, index)


    def is_curve_periodic(self, index=pythoncom.Empty):

        return _rsf.is_curve_periodic(self.rhino_id, index)


    def is_curve_planar(self, index=pythoncom.Empty):

        return _rsf.is_curve_planar(self.rhino_id, index)


    def is_curve_rational(self, index=pythoncom.Empty):

        return _rsf.is_curve_rational(self.rhino_id, index)


    def is_ellipse(self, ):

        return _rsf.is_ellipse(self.rhino_id)


    def is_in_layout_space(self, ):

        return _rsf.is_layout_object(self.rhino_id)


    def is_line(self, index=pythoncom.Empty):

        return _rsf.is_line(self.rhino_id, index)


    def is_object(self, ):

        return _rsf.is_object(self.rhino_id)


    def is_hidden(self, ):

        return _rsf.is_object_hidden(self.rhino_id)


    def is_in_box(self, box, mode=pythoncom.Empty):

        return _rsf.is_object_in_box(self.rhino_id, box, mode)


    def is_in_group(self, group=pythoncom.Empty):

        return _rsf.is_object_in_group(self.rhino_id, group)


    def is_locked(self, ):

        return _rsf.is_object_locked(self.rhino_id)


    def is_normal(self, ):

        return _rsf.is_object_normal(self.rhino_id)


    def is_reference(self, ):

        return _rsf.is_object_reference(self.rhino_id)


    def is_selectable(self, ):

        return _rsf.is_object_selectable(self.rhino_id)


    def is_selected(self, ):

        return _rsf.is_object_selected(self.rhino_id)


    def is_solid(self, ):

        return _rsf.is_object_solid(self.rhino_id)


    def is_valid(self, ):

        return _rsf.is_object_valid(self.rhino_id)


    def is_point_on_curve(self, point, index=pythoncom.Empty):

        return _rsf.is_point_on_curve(self.rhino_id, point, index)


    def is_poly_curve(self, index=pythoncom.Empty):

        return _rsf.is_poly_curve(self.rhino_id, index)


    def is_polyline(self, index=pythoncom.Empty):

        return _rsf.is_polyline(self.rhino_id, index)


    def is_visible_in_view(self, view=pythoncom.Empty):

        return _rsf.is_visible_in_view(self.rhino_id, view)


    def lock(self, ):

        return _rsf.lock_objects(self.rhino_id)


    def reset_object_attributes(self, source):

        return _rsf.match_object_attributes(self.rhino_id, source.rhino_id)


    def mirror(self, start_pt, end_pt, copy=pythoncom.Empty):

        return _rsf.mirror_objects(self.rhino_id, start_pt, end_pt, copy)


    def move(self, start, end):

        return _rsf.move_objects(self.rhino_id, start, end)


    def move_and_xform(self, translation):

        return _rsf.move_objects_2(self.rhino_id, translation)


    def color(self, color=pythoncom.Empty):

        return _rsf.object_color(self.rhino_id, color)


    def color_source(self, source=pythoncom.Empty):

        return _rsf.object_color_source(self.rhino_id, source)


    def description(self, ):

        return _rsf.object_description(self.rhino_id)


    def dump(self, type=pythoncom.Empty):

        return _rsf.object_dump(self.rhino_id, type)


    def groups(self, ):

        return _rsf.object_groups(self.rhino_id)


    def has_mesh(self, ):

        return _rsf.object_has_mesh(self.rhino_id)


    def layer(self, layer=pythoncom.Empty):

        return _rsf.object_layer(self.rhino_id, layer.rhino_id)


    def move_to_layout_space(self, layout=pythoncom.Empty, return_name=pythoncom.Empty):

        return _rsf.object_layout(self.rhino_id, layout, return_name)


    def linetype(self, layer=pythoncom.Empty):

        return _rsf.object_linetype(self.rhino_id, layer.rhino_id)


    def linetype_source(self, source=pythoncom.Empty):

        return _rsf.object_linetype_source(self.rhino_id, source)


    def material_index(self, ):

        return _rsf.object_material_index(self.rhino_id)


    def material_source(self, source=pythoncom.Empty):

        return _rsf.object_material_source(self.rhino_id, source)


    def omesh_density(self, density=pythoncom.Empty):

        return _rsf.object_mesh_density(self.rhino_id, density)


    def mesh_max_angle(self, angle=pythoncom.Empty):

        return _rsf.object_mesh_max_angle(self.rhino_id, angle)


    def mesh_max_aspect_ratio(self, ratio=pythoncom.Empty):

        return _rsf.object_mesh_max_aspect_ratio(self.rhino_id, ratio)


    def mesh_max_dist_edge_to_srf(self, distance=pythoncom.Empty):

        return _rsf.object_mesh_max_dist_edge_to_srf(self.rhino_id, distance)


    def mesh_max_edge_length(self, length=pythoncom.Empty):

        return _rsf.object_mesh_max_edge_length(self.rhino_id, length)


    def mesh_min_edge_length(self, length=pythoncom.Empty):

        return _rsf.object_mesh_min_edge_length(self.rhino_id, length)


    def mesh_min_initial_grid_quads(self, quads=pythoncom.Empty):

        return _rsf.object_mesh_min_initial_grid_quads(self.rhino_id, quads)


    def mesh_quality(self, quality=pythoncom.Empty):

        return _rsf.object_mesh_quality(self.rhino_id, quality)


    def mesh_settings(self, settings=pythoncom.Empty):

        return _rsf.object_mesh_settings(self.rhino_id, settings)


    def name(self, names=pythoncom.Empty):

        return _rsf.object_names(self.rhino_id, names)


    def print_color(self, color=pythoncom.Empty):

        return _rsf.object_print_color(self.rhino_id, color)


    def print_color_source(self, source=pythoncom.Empty):

        return _rsf.object_print_color_source(self.rhino_id, source)


    def print_width(self, width=pythoncom.Empty):

        return _rsf.object_print_width(self.rhino_id, width)


    def print_width_source(self, source=pythoncom.Empty):

        return _rsf.object_print_width_source(self.rhino_id, source)


    def top_group(self, ):

        return _rsf.object_top_group(self.rhino_id)


    def object_type(self, ):

        return _rsf.object_type(self.rhino_id)


    def url(self, url=pythoncom.Empty):

        return _rsf.object_u_r_l(self.rhino_id, url)


    def orient(self, reference, target, flags=pythoncom.Empty):

        return _rsf.orient_objects(self.rhino_id, reference, target, flags)


    def remap(self, src_plane, dst_plane, copy=pythoncom.Empty):

        return _rsf.remap_objects(self.rhino_id, src_plane, dst_plane, copy)


    def rotate(self, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):

        return _rsf.rotate_objects(self.rhino_id, point, angle, axis, copy)


    def scale(self, origin, scale, copy=pythoncom.Empty):

        return _rsf.scale_objects(self.rhino_id, origin, scale, copy)


    def select(self, ):

        return _rsf.select_objects(self.rhino_id)


    def shear(self, origin, ref_pt, scale, copy=pythoncom.Empty):

        return _rsf.shear_objects(self.rhino_id, origin, ref_pt, scale, copy)


    def show(self, ):

        return _rsf.show_objects(self.rhino_id)


    def transform(self, matrix, copy=pythoncom.Empty):

        return _rsf.transform_objects(self.rhino_id, matrix, copy)


    def unlock(self, ):

        return _rsf.unlock_objects(self.rhino_id)


    def unselect(self, ):

        return _rsf.unselect_objects(self.rhino_id)

