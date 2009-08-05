# Auto-generated wrapper for Rhino4 RhinoScript classes
import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
_rsf = None


class _CurveRoot(_ObjectRoot):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in


class _ObjectRoot(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in


class _SurfaceRoot(_ObjectRoot):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in


class _CurveRootEval(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def curvature(self, parameter):
        return _rsf.curve_curvature(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        return _rsf.curve_evaluate(self._rhino_id, parameter, derivative)

    def frame(self, parameter):
        return _rsf.curve_frame(self._rhino_id, parameter)

    def perp_frame(self, parameter):
        return _rsf.curve_perp_frame(self._rhino_id, parameter)

    def tangent(self, parameter):
        return _rsf.curve_tangent(self._rhino_id, parameter, pythoncom.Empty)

    def evaluate(self, parameter):
        return _rsf.evaluate_curve(self._rhino_id, parameter, pythoncom.Empty)


class _CurveRootFunc(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def crv_arc_length_point(self, length, from_start=pythoncom.Empty):
        return _rsf.curve_arc_length_point(self._rhino_id, length, from_start)

    def closest_point(self, point):
        return _rsf.curve_closest_point(self._rhino_id, point, pythoncom.Empty)

    def contour_points(self, start_point, end_point, interval=pythoncom.Empty):
        return _rsf.curve_contour_points(self._rhino_id, start_point, end_point, interval)

    def crv_intersection(self, curve=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.curve_curve_intersection(self._rhino_id, curve, tolerance)

    def deviation(self, curve_a):
        return _rsf.curve_deviation(self._rhino_id, curve_a)

    def directions_match(self, curve_1):
        return _rsf.curve_directions_match(self._rhino_id, curve_1)

    def radius(self, point):
        return _rsf.curve_radius(self._rhino_id, point, pythoncom.Empty)

    def srf_intersection(self, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        return _rsf.curve_surface_intersection(self._rhino_id, surface, tolerance, angle_tolerance)

    def divide_crv(self, segments, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve(self._rhino_id, segments, create, points)

    def divide_crv_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve_equidistant(self._rhino_id, distance, create, points)

    def divide_crv_length(self, length, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve_length(self._rhino_id, length, create, points)

    def line_fit_from_points(self):
        return _rsf.line_fit_from_points(self._rhino_id)

    def planar_crv_collision(self, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.planar_curve_collision(self._rhino_id, curve, plane, tolerance)


class _CurveRootFuncClsd(_CurveRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def closed_crv_area(self, objects):
        return _rsf.curve_area(map(lambda i: i._rhino_id, objects))

    def pclosed_crv_area_centroid(self, objects):
        return _rsf.curve_area_centroid(map(lambda i: i._rhino_id, objects))

    def boolean_difference(self, curve):
        _rhino_ids = _rsf.curve_boolean_difference(self._rhino_id, curve)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_intersection(self, curve_a):
        _rhino_ids = _rsf.curve_boolean_intersection(self._rhino_id, curve_a)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_union(self, curves):
        _rhino_ids = _rsf.curve_boolean_union(map(lambda i: i._rhino_id, curves))
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def closed_crv_containment(self, curve__1, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.planar_closed_curve_containment(self._rhino_id, curve__1, plane, tolerance)

    def closed_crv_point_inside(self, point, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.point_in_planar_closed_curve(point, self._rhino_id, plane, tolerance)


class _CurveRootFuncOorc(_CurveRootFuncClsd,_CurveRootFuncClsd):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in


class _CurveRootFuncOpen(_CurveRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def open_crv_close(self, tolerance=pythoncom.Empty):
        return _rsf.close_curve(self._rhino_id, tolerance)

    def open_crv_extend(self, type, side, objects):
        return _rsf.extend_curve(self._rhino_id, type, side, objects)

    def open_crv_extend_length(self, type, side, length):
        return _rsf.extend_curve_length(self._rhino_id, type, side, length)

    def open_crv_extend_point(self, side, point):
        return _rsf.extend_curve_point(self._rhino_id, side, point)


class _CurveRootGenr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def fit(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        _rhino_id = _rsf.fit_curve(self._rhino_id, degree, tolerance, angle_tolerance)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def make_non_periodic(self):
        _rhino_id = _rsf.make_curve_non_periodic(self._rhino_id, False)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def make_periodic(self):
        _rhino_id = _rsf.make_curve_periodic(self._rhino_id, False)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None


class _CurveRootMdfy(_ObjectRootModf):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def seam(self, parameter):

        return _rsf.curve_seam(self._rhino_id, parameter)


    def fair(self, tolerance=pythoncom.Empty):

        return _rsf.fair_curve(self._rhino_id, tolerance)


    def insert_knot(self, parameter, symmetrical=pythoncom.Empty):

        return _rsf.insert_curve_knot(self._rhino_id, parameter, symmetrical)


    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return _rsf.rebuild_curve(self._rhino_id, degree, point_count)


    def remove_knot(self, parameter):

        return _rsf.remove_curve_knot(self._rhino_id, parameter)


    def reverse(self):

        return _rsf.reverse_curve(self._rhino_id)


    def simplify(self, flags=pythoncom.Empty):

        return _rsf.simplify_curve(self._rhino_id, flags)



class _CurveRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def arrows(self, style=pythoncom.Empty):
        return _rsf.curve_arrows(self._rhino_id, style)

    def degree(self):
        return _rsf.curve_degree(self._rhino_id, pythoncom.Empty)

    def dim(self):
        return _rsf.curve_dim(self._rhino_id, pythoncom.Empty)

    def discontinuity(self, style):
        return _rsf.curve_discontinuity(self._rhino_id, style)

    def domain(self):
        return _rsf.curve_domain(self._rhino_id, pythoncom.Empty)

    def edit_points(self, return_parameters=pythoncom.Empty):
        return _rsf.curve_edit_points(self._rhino_id, return_parameters, pythoncom.Empty)

    def end_point(self):
        return _rsf.curve_end_point(self._rhino_id, pythoncom.Empty)

    def knot_count(self):
        return _rsf.curve_knot_count(self._rhino_id, pythoncom.Empty)

    def knots(self):
        return _rsf.curve_knots(self._rhino_id, pythoncom.Empty)

    def length(self, sub_domain=pythoncom.Empty):
        return _rsf.curve_length(self._rhino_id, pythoncom.Empty, sub_domain)

    def mid_point(self):
        return _rsf.curve_mid_point(self._rhino_id)

    def normal(self):
        return _rsf.curve_normal(self._rhino_id)

    def plane(self):
        return _rsf.curve_plane(self._rhino_id)

    def control_point_count(self):
        return _rsf.curve_point_count(self._rhino_id, pythoncom.Empty)

    def control_points(self):
        return _rsf.curve_points(self._rhino_id, pythoncom.Empty)

    def start_point(self):
        return _rsf.curve_start_point(self._rhino_id, pythoncom.Empty)

    def weights(self):
        return _rsf.curve_weights(self._rhino_id, pythoncom.Empty)


class _CurveRootTest(_ObjectRootTest):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_closable(self, tolerance=pythoncom.Empty):
        return _rsf.is_curve_closable(self._rhino_id, tolerance)

    def is_closed(self):
        return _rsf.is_curve_closed(self._rhino_id, pythoncom.Empty)

    def in_plane(self, plane=pythoncom.Empty):
        return _rsf.is_curve_in_plane(self._rhino_id, plane)

    def is_linear(self):
        return _rsf.is_curve_linear(self._rhino_id, pythoncom.Empty)

    def is_periodic(self):
        return _rsf.is_curve_periodic(self._rhino_id, pythoncom.Empty)

    def is_planar(self):
        return _rsf.is_curve_planar(self._rhino_id, pythoncom.Empty)

    def is_rational(self):
        return _rsf.is_curve_rational(self._rhino_id, pythoncom.Empty)

    def is_on_crv(self, point):
        return _rsf.is_point_on_curve(self._rhino_id, point, pythoncom.Empty)


class _CurveRootType(_ObjectRootType):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_arc(self):
        return _rsf.is_arc(self._rhino_id, pythoncom.Empty)

    def is_circle(self):
        return _rsf.is_circle(self._rhino_id, pythoncom.Empty)

    def is_crv(self):
        return _rsf.is_curve(self._rhino_id, pythoncom.Empty)

    def is_ellipse(self):
        return _rsf.is_ellipse(self._rhino_id)

    def is_line(self):
        return _rsf.is_line(self._rhino_id, pythoncom.Empty)

    def is_poly_crv(self):
        return _rsf.is_poly_curve(self._rhino_id, pythoncom.Empty)

    def is_polyline(self):
        return _rsf.is_polyline(self._rhino_id, pythoncom.Empty)


class _ObjectRootDefm(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def box_morph(self, box_points, copy=pythoncom.Empty):
        _rhino_id = _rsf.box_morph_object(self._rhino_id, box_points, copy)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None

    def shear(self, origin, ref_pt, scale, copy=pythoncom.Empty):
        _rhino_id = _rsf.shear_object(self._rhino_id, origin, ref_pt, scale, copy)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None

    def trfm(self, matrix, copy=pythoncom.Empty):
        _rhino_id = _rsf.transform_object(self._rhino_id, matrix, copy)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None


class _ObjectRootGrps(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def groups(self):
        return _rsf.object_groups(self._rhino_id)

    def top_group(self):
        return _rsf.object_top_group(self._rhino_id)


class _ObjectRootModf(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def delete(self):
        return _rsf.delete_objects(self._rhino_id)


class _ObjectRootMtrl(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def index(self):
        return _rsf.object_material_index(self._rhino_id)

    def source(self, source=pythoncom.Empty):
        return _rsf.object_material_source(self._rhino_id, source)


class _ObjectRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def color(self, color=pythoncom.Empty):
        return _rsf.object_color(self._rhino_id, color)

    def color_source(self, source=pythoncom.Empty):
        return _rsf.object_color_source(self._rhino_id, source)

    def layer(self, layer=pythoncom.Empty):
        return _rsf.object_layer(self._rhino_id, layer._rhino_id)

    def linetype(self, layer=pythoncom.Empty):
        return _rsf.object_linetype(self._rhino_id, layer._rhino_id)

    def linetype_source(self, source=pythoncom.Empty):
        return _rsf.object_linetype_source(self._rhino_id, source)

    def name(self, names=pythoncom.Empty):
        return _rsf.object_names(self._rhino_id, names)

    def print_color(self, color=pythoncom.Empty):
        return _rsf.object_print_color(self._rhino_id, color)

    def print_color_source(self, source=pythoncom.Empty):
        return _rsf.object_print_color_source(self._rhino_id, source)

    def print_width(self, width=pythoncom.Empty):
        return _rsf.object_print_width(self._rhino_id, width)

    def print_width_source(self, source=pythoncom.Empty):
        return _rsf.object_print_width_source(self._rhino_id, source)


class _ObjectRootRndr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def add_mesh(self, quality=pythoncom.Empty, enable=pythoncom.Empty):
        return _rsf.add_object_mesh(self._rhino_id, quality, enable)

    def enable(self, enable=pythoncom.Empty):
        return _rsf.enable_object_mesh(self._rhino_id, enable)

    def has_mesh(self):
        return _rsf.object_has_mesh(self._rhino_id)

    def density(self, density=pythoncom.Empty):
        return _rsf.object_mesh_density(self._rhino_id, density)

    def max_angle(self, angle=pythoncom.Empty):
        return _rsf.object_mesh_max_angle(self._rhino_id, angle)

    def max_aspect_ratio(self, ratio=pythoncom.Empty):
        return _rsf.object_mesh_max_aspect_ratio(self._rhino_id, ratio)

    def max_dist_edge_to_srf(self, distance=pythoncom.Empty):
        return _rsf.object_mesh_max_dist_edge_to_srf(self._rhino_id, distance)

    def max_edge_length(self, length=pythoncom.Empty):
        return _rsf.object_mesh_max_edge_length(self._rhino_id, length)

    def min_edge_length(self, length=pythoncom.Empty):
        return _rsf.object_mesh_min_edge_length(self._rhino_id, length)

    def min_initial_grid_quads(self, quads=pythoncom.Empty):
        return _rsf.object_mesh_min_initial_grid_quads(self._rhino_id, quads)

    def quality(self, quality=pythoncom.Empty):
        return _rsf.object_mesh_quality(self._rhino_id, quality)

    def settings(self, settings=pythoncom.Empty):
        return _rsf.object_mesh_settings(self._rhino_id, settings)


class _ObjectRootStat(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def flash(self, style=pythoncom.Empty):
        return _rsf.flash_object()

    def hide(self):
        return _rsf.hide_objects(self._rhino_id)

    def lock(self):
        return _rsf.lock_objects(self._rhino_id)

    def match_object_attributes(self, targets):
        return _rsf.match_object_attributes(map(lambda i: i._rhino_id, targets), self._rhino_id)

    def reset_object_attributes(self, source):
        return _rsf.match_object_attributes(self._rhino_id, source._rhino_id)

    def move_to_layout_space(self, layout=pythoncom.Empty, return_name=pythoncom.Empty):
        return _rsf.object_layout(self._rhino_id, layout, return_name)

    def select(self):
        return _rsf.select_objects(self._rhino_id)

    def show(self):
        return _rsf.show_objects(self._rhino_id)

    def unlock(self):
        return _rsf.unlock_objects(self._rhino_id)

    def unselect(self):
        return _rsf.unselect_objects(self._rhino_id)


class _ObjectRootTest(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_in_layout_space(self):
        return _rsf.is_layout_object(self._rhino_id)

    def is_hidden(self):
        return _rsf.is_object_hidden(self._rhino_id)

    def is_in_box(self, box, mode=pythoncom.Empty):
        return _rsf.is_object_in_box(self._rhino_id, box, mode)

    def is_in_group(self, group=pythoncom.Empty):
        return _rsf.is_object_in_group(self._rhino_id, group)

    def is_locked(self):
        return _rsf.is_object_locked(self._rhino_id)

    def is_normal(self):
        return _rsf.is_object_normal(self._rhino_id)

    def is_reference(self):
        return _rsf.is_object_reference(self._rhino_id)

    def is_selectable(self):
        return _rsf.is_object_selectable(self._rhino_id)

    def is_selected(self):
        return _rsf.is_object_selected(self._rhino_id)

    def is_solid(self):
        return _rsf.is_object_solid(self._rhino_id)

    def is_valid(self):
        return _rsf.is_object_valid(self._rhino_id)

    def is_visible_in_view(self, view=pythoncom.Empty):
        return _rsf.is_visible_in_view(self._rhino_id, view)


class _ObjectRootTrfm(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def copy(self, start=pythoncom.Empty, end=pythoncom.Empty):
        _rhino_id = _rsf.copy_object(self._rhino_id, start, end)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def copy_and_xform(self, translation=pythoncom.Empty):
        _rhino_id = _rsf.copy_object_2(self._rhino_id, translation)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def mirror(self, start_pt, end_pt, copy=pythoncom.Empty):
        _rhino_id = _rsf.mirror_object(self._rhino_id, start_pt, end_pt, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move(self, start, end):
        _rhino_id = _rsf.move_object(self._rhino_id, start, end)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move_and_xform(self, translation):
        _rhino_id = _rsf.move_object_2(self._rhino_id, translation)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def orient(self, reference, target, flags=pythoncom.Empty):
        _rhino_id = _rsf.orient_object(self._rhino_id, reference, target, flags)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def remap(self, src_plane, dst_plane, copy=pythoncom.Empty):
        _rhino_id = _rsf.remap_object(self._rhino_id, src_plane, dst_plane, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def rotate(self, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):
        _rhino_id = _rsf.rotate_object(self._rhino_id, point, angle, axis, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def scale(self, origin, scale, copy=pythoncom.Empty):
        _rhino_id = _rsf.scale_object(self._rhino_id, origin, scale, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None


class _ObjectRootType(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def object_type(self):
        return _rsf.object_type(self._rhino_id)


class _ObjectRootUtil(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def description(self):
        return _rsf.object_description(self._rhino_id)

    def dump(self, type=pythoncom.Empty):
        return _rsf.object_dump(self._rhino_id, type)


class _SurfaceRootEval(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def evaluate(self, parameter):
        return _rsf.evaluate_surface(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        return _rsf.surface_evaluate(self._rhino_id, parameter, derivative)

    def evaluate_frame(self, parameter):
        return _rsf.surface_frame(self._rhino_id, parameter)


class _SurfaceRootFunc(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def cap_planar_holes(self):
        return _rsf.cap_planar_holes(self._rhino_id)

    def closest_point(self, point):
        return _rsf.surface_closest_point(self._rhino_id, point)


class _SurfaceRootFuncClsd(_SurfaceRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def boolean_difference(self, input_1, delete=pythoncom.Empty):
        _rhino_ids = _rsf.boolean_difference(self._rhino_id, map(lambda i: i._rhino_id, input_1), delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_intersection(self, input_1, delete=pythoncom.Empty):
        _rhino_ids = _rsf.boolean_intersection(self._rhino_id, map(lambda i: i._rhino_id, input_1), delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def boolean_union(self, input, delete=pythoncom.Empty):
        _rhino_ids = _rsf.boolean_union(map(lambda i: i._rhino_id, input), delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def brep_closest_point(self, point):
        return _rsf.brep_closest_point(self._rhino_id, point)

    def intersect_breps(self, brep_1, tolerance=pythoncom.Empty):
        _rhino_ids = _rsf.intersect_breps(self._rhino_id, brep_1, tolerance)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def split_brep(self, cutter, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_brep(self._rhino_id, cutter, delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def volume(self):
        return _rsf.surface_volume(self._rhino_id)

    def volume_centroid(self):
        return _rsf.surface_volume_centroid(self._rhino_id)

    def volume_moments(self):
        return _rsf.surface_volume_moments(self._rhino_id)


class _SurfaceRootFuncOorc(_SurfaceRootFuncOpen,_SurfaceRootFuncClsd):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in


class _SurfaceRootFuncOpen(_SurfaceRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in


class _SurfaceRootGenr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def fit(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty):
        _rhino_id = _rsf.fit_surface(self._rhino_id, degree, tolerance)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def make_non_periodic(self, direction, delete=pythoncom.Empty):
        _rhino_id = _rsf.make_surface_non_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def make_periodic(self, direction, delete=pythoncom.Empty):
        _rhino_id = _rsf.make_surface_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def offset(self, distance):
        _rhino_id = _rsf.offset_surface(self._rhino_id, distance)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None


class _SurfaceRootMdfy(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def flip(self, flip=pythoncom.Empty):

        return _rsf.flip_surface(self._rhino_id, flip)


    def insert_knot(self, parameter, direction, symmetrical=pythoncom.Empty):

        return _rsf.insert_surface_knot(self._rhino_id, parameter, direction, symmetrical)


    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return _rsf.rebuild_surface(self._rhino_id, degree, point_count)


    def remove_knot(self, parameter, direction):

        return _rsf.remove_surface_knot(self._rhino_id, parameter, direction)


    def reverse(self, direction):

        return _rsf.reverse_surface(self._rhino_id, direction)


    def shrink_trimmed(self):

        return _rsf.shrink_trimmed_surface(self._rhino_id)


    def seam(self, direction, parameter):

        return _rsf.surface_seam(self._rhino_id, direction, parameter)



class _SurfaceRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def area(self):
        return _rsf.surface_area(self._rhino_id)

    def area_centroid(self):
        return _rsf.surface_area_centroid(self._rhino_id)

    def area_moments(self):
        return _rsf.surface_area_moments(self._rhino_id)

    def contour_points(self, start_point, end_point, interval=pythoncom.Empty, angle=pythoncom.Empty):
        return _rsf.surface_contour_points(self._rhino_id, start_point, end_point, interval, angle)

    def curvature(self, parameter):
        return _rsf.surface_curvature(self._rhino_id, parameter)

    def curvature_analysis(self):
        return _rsf.surface_curvature_analysis(self._rhino_id)

    def degree(self, direction=pythoncom.Empty):
        return _rsf.surface_degree(self._rhino_id, direction)

    def domain(self, direction):
        return _rsf.surface_domain(self._rhino_id, direction)

    def edit_points(self, return_parameters=pythoncom.Empty, return_all=pythoncom.Empty):
        return _rsf.surface_edit_points(self._rhino_id, return_parameters, return_all)

    def isocurve_density(self, density=pythoncom.Empty):
        return _rsf.surface_isocurve_density(self._rhino_id, density)

    def knot_count(self):
        return _rsf.surface_knot_count(self._rhino_id)

    def knots(self):
        return _rsf.surface_knots(self._rhino_id)

    def normal(self, parameter):
        return _rsf.surface_normal(self._rhino_id, parameter)

    def point_count(self):
        return _rsf.surface_point_count(self._rhino_id)

    def points(self, return_all=pythoncom.Empty):
        return _rsf.surface_points(self._rhino_id, return_all)

    def weights(self):
        return _rsf.surface_weights(self._rhino_id)


class _SurfaceRootTest(_ObjectRootType):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_brep(self):
        return _rsf.is_brep(self._rhino_id)

    def is_brep_manifold(self):
        return _rsf.is_brep_manifold(self._rhino_id)

    def is_parameter_on_srf(self, parameter):
        return _rsf.is_parameter_on_surface(self._rhino_id, parameter)

    def is_plane_surface(self):
        return _rsf.is_plane_surface(self._rhino_id)

    def is_point_in_srf(self, point):
        return _rsf.is_point_in_surface(self._rhino_id, point)

    def is_point_on_srf(self, point):
        return _rsf.is_point_on_surface(self._rhino_id, point)

    def is_poly_srf(self):
        return _rsf.is_poly_surface(self._rhino_id)

    def is_poly_surface_closed(self):
        return _rsf.is_poly_surface_closed(self._rhino_id)

    def is_poly_srf_planar(self):
        return _rsf.is_poly_surface_planar(self._rhino_id)

    def is_srf_closed(self, direction):
        return _rsf.is_surface_closed(self._rhino_id, direction)

    def is_srf_periodic(self, direction):
        return _rsf.is_surface_periodic(self._rhino_id, direction)

    def is_srf_planar(self, tolerance=pythoncom.Empty):
        return _rsf.is_surface_planar(self._rhino_id, tolerance)

    def is_srf_rational(self):
        return _rsf.is_surface_rational(self._rhino_id)

    def is_srf_singular(self, direction):
        return _rsf.is_surface_singular(self._rhino_id, direction)

    def is_srf_trimmed(self):
        return _rsf.is_surface_trimmed(self._rhino_id)


class _SurfaceRootType(_ObjectRootTest):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_cone(self):
        return _rsf.is_cone(self._rhino_id)

    def is_cylinder(self):
        return _rsf.is_cylinder(self._rhino_id)

    def is_sphere(self):
        return _rsf.is_sphere(self._rhino_id)

    def is_surface(self):
        return _rsf.is_surface(self._rhino_id)

    def is_torus(self):
        return _rsf.is_torus(self._rhino_id)


class _ArcGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.Arc(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.Arc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None


class _ArcProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def angle(self):
        return _rsf.arc_angle(self._rhino_id, pythoncom.Empty)

    def center_point(self):
        return _rsf.arc_center_point(self._rhino_id, pythoncom.Empty)

    def mid_point(self):
        return _rsf.arc_mid_point(self._rhino_id, pythoncom.Empty)

    def radius(self):
        return _rsf.arc_radius(self._rhino_id, pythoncom.Empty)


class _CircleGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.Circle(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.Arc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.Arc(_rhino_id)
        else:
            return None


class _CircleProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def center_point(self):
        return _rsf.circle_center_point(self._rhino_id, pythoncom.Empty)

    def circumference(self):
        return _rsf.circle_circumference(self._rhino_id, pythoncom.Empty)

    def radius(self):
        return _rsf.circle_radius(self._rhino_id, pythoncom.Empty)


class _ConeProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def cone_definition(self):
        return _rsf.surface_cone(self._rhino_id)


class _CylinderProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def cylinder_definition(self):
        return _rsf.surface_cylinder(self._rhino_id)


class _EllipseGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def plit(self, parameters, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None


class _EllipseProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def center_point(self):
        return _rsf.ellipse_center_point(self._rhino_id)

    def quad_points(self):
        return _rsf.ellipse_quad_points(self._rhino_id)


class _EllipticalArcGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.EllipticalArc(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.EllipticalArc(_rhino_id)
        else:
            return None


class _LineGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r._util.wrap(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None


class _NurbsCurveGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.NurbsCurve(i), _rhino_ids)

    def offset_on_srf(self, surface, distance, parameter):
        _rhino_id = _rsf.offset_curve_on_surface(self._rhino_id, surface._rhino_id, distance, parameter)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None

    def split(self, parameters, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.NurbsCurve(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.NurbsCurve(_rhino_id)
        else:
            return None


class _PolySurfaceProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def explode(self, objects, delete=pythoncom.Empty):
        _rhino_ids = _rsf.explode_polysurfaces(map(lambda i: i._rhino_id, objects), delete)
        return map(lambda i: p2r.NurbsSurface(i), _rhino_ids)


class _PolylineGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.Polyline(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        _rhino_ids = _rsf.offset_curve(self._rhino_id, direction, distance, normal, style)
        return map(lambda i: p2r.Polyline(i), _rhino_ids)

    def split(self, parameters, delete=pythoncom.Empty):
        _rhino_ids = _rsf.split_curve(self._rhino_id, parameters, delete)
        return map(lambda i: p2r.Polyline(i), _rhino_ids)

    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.Polyline(_rhino_id)
        else:
            return None


class _PolylineProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def vertices(self):
        return _rsf.polyline_vertices(self._rhino_id, pythoncom.Empty)


class _SphereProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def cylinder_definition(self):
        return _rsf.surface_sphere(self._rhino_id)


class _TorusProp(_SurfaceRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def torus_definition(self):
        return _rsf.surface_torus(self._rhino_id)
