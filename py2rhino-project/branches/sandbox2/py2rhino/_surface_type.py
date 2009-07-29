# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class _SurfaceType(_Object):    # Class constructor
    def __init__(self):
        pass
    def boolean_difference(input_0, input_1, delete=None):

        return _rsf.boolean_difference(input_0, input_1, delete)

    def boolean_intersection(input_0, input_1, delete=None):

        return _rsf.boolean_intersection(input_0, input_1, delete)

    def boolean_union(input, delete=None):

        return _rsf.boolean_union(input, delete)

    def brep_closest_point(, point):

        return _rsf.brep_closest_point(, point)

    def cap_planar_holes():

        return _rsf.cap_planar_holes()

    def duplicate_edge_curves(, select=None):

        return _rsf.duplicate_edge_curves(, select)

    def duplicate_surface_border():

        return _rsf.duplicate_surface_border()

    def evaluate_surface(, parameter):

        return _rsf.evaluate_surface(, parameter)

    def extract_iso_curve(, parameter, dir):

        return _rsf.extract_iso_curve(, parameter, dir)

    def extrude_curve(, path):

        return _rsf.extrude_curve(, path)

    def extrude_curve_point(, point):

        return _rsf.extrude_curve_point(, point)

    def extrude_curve_straight(, start_point, end_point):

        return _rsf.extrude_curve_straight(, start_point, end_point)

    def extrude_curve_tapered(, distance, direction, base_point, angle, corner_type=None):

        return _rsf.extrude_curve_tapered(, distance, direction, base_point, angle, corner_type)

    def extrude_surface(, curve, cap=None):

        return _rsf.extrude_surface(, curve, cap)

    def fit_surface(, degree=None, tolerance=None):

        return _rsf.fit_surface(, degree, tolerance)

    def flip_surface(, flip=None):

        return _rsf.flip_surface(, flip)

    def join_surfaces(, delete=None):

        return _rsf.join_surfaces(, delete)

    def make_surface_non_periodic(, direction, delete=None):

        return _rsf.make_surface_non_periodic(, direction, delete)

    def make_surface_periodic(, direction, delete=None):

        return _rsf.make_surface_periodic(, direction, delete)

    def offset_surface(, distance):

        return _rsf.offset_surface(, distance)

    def pull_curve(, curve, delete=None):

        return _rsf.pull_curve(, curve, delete)

    def rebuild_surface(, degree=None, point_count=None):

        return _rsf.rebuild_surface(, degree, point_count)

    def remove_surface_knot(, parameter, direction):

        return _rsf.remove_surface_knot(, parameter, direction)

    def reverse_surface(, direction):

        return _rsf.reverse_surface(, direction)

    def short_path(, start, end):

        return _rsf.short_path(, start, end)

    def shrink_trimmed_surface():

        return _rsf.shrink_trimmed_surface()

    def split_brep(, cutter, delete=None):

        return _rsf.split_brep(, cutter, delete)

    def surface_area():

        return _rsf.surface_area()

    def surface_area_centroid():

        return _rsf.surface_area_centroid()

    def surface_area_moments():

        return _rsf.surface_area_moments()

    def surface_closest_point(, point):

        return _rsf.surface_closest_point(, point)

    def surface_contour_points(, start_point, end_point, interval=None, angle=None):

        return _rsf.surface_contour_points(, start_point, end_point, interval, angle)

    def surface_curvature(, parameter):

        return _rsf.surface_curvature(, parameter)

    def surface_curvature_analysis():

        return _rsf.surface_curvature_analysis()

    def surface_degree(, direction=None):

        return _rsf.surface_degree(, direction)

    def surface_domain(, direction):

        return _rsf.surface_domain(, direction)

    def surface_edit_points(, return_parameters=None, return_all=None):

        return _rsf.surface_edit_points(, return_parameters, return_all)

    def surface_evaluate(, parameter, derivative):

        return _rsf.surface_evaluate(, parameter, derivative)

    def surface_frame(, parameter):

        return _rsf.surface_frame(, parameter)

    def surface_isocurve_density(, density=None):

        return _rsf.surface_isocurve_density(, density)

    def surface_knot_count():

        return _rsf.surface_knot_count()

    def surface_knots():

        return _rsf.surface_knots()

    def surface_normal(, parameter):

        return _rsf.surface_normal(, parameter)

    def surface_point_count():

        return _rsf.surface_point_count()

    def surface_points(, return_all=None):

        return _rsf.surface_points(, return_all)

    def surface_principal_curvature(, point):

        return _rsf.surface_principal_curvature(, point)

    def surface_seam(, direction, parameter):

        return _rsf.surface_seam(, direction, parameter)

    def surface_surface_intersection(, surface_a, tolerance=None, create=None):

        return _rsf.surface_surface_intersection(, surface_a, tolerance, create)

    def surface_volume():

        return _rsf.surface_volume()

    def surface_volume_centroid():

        return _rsf.surface_volume_centroid()

    def surface_volume_moments():

        return _rsf.surface_volume_moments()

    def surface_weights():

        return _rsf.surface_weights()

