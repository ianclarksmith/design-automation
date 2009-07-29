# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class _SurfaceType(p2r._Object):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    def boolean_difference(self, input_0, input_1, delete=pythoncom.Empty):

        return p2r_f.boolean_difference(trouble, input_1, delete)


    def boolean_intersection(self, input_0, input_1, delete=pythoncom.Empty):

        return p2r_f.boolean_intersection(trouble, input_1, delete)


    def boolean_union(self, input, delete=pythoncom.Empty):

        return p2r_f.boolean_union(trouble, delete)


    def brep_closest_point(self, point):

        return p2r_f.brep_closest_point(self.rhino_id, point)


    def cap_planar_holes(self, ):

        return p2r_f.cap_planar_holes(self.rhino_id)


    def duplicate_edge_curves(self, select=pythoncom.Empty):

        return p2r_f.duplicate_edge_curves(self.rhino_id, select)


    def duplicate_surface_border(self, ):

        return p2r_f.duplicate_surface_border(self.rhino_id)


    def evaluate_surface(self, parameter):

        return p2r_f.evaluate_surface(self.rhino_id, parameter)


    def extract_iso_curve(self, parameter, dir):

        return p2r_f.extract_iso_curve(self.rhino_id, parameter, dir)


    @classmethod
    def extrude_curve(cls, path):

        return p2r_f.extrude_curve(self.rhino_id, path)


    @classmethod
    def extrude_curve_point(cls, point):

        return p2r_f.extrude_curve_point(self.rhino_id, point)


    @classmethod
    def extrude_curve_straight(cls, start_point, end_point):

        return p2r_f.extrude_curve_straight(self.rhino_id, start_point, end_point)


    def extrude_curve_tapered(self, distance, direction, base_point, angle, corner_type=pythoncom.Empty):

        return p2r_f.extrude_curve_tapered(self.rhino_id, distance, direction, base_point, angle, corner_type)


    @classmethod
    def extrude_surface(cls, curve, cap=pythoncom.Empty):

        return p2r_f.extrude_surface(self.rhino_id, curve, cap)


    @classmethod
    def fit_surface(cls, degree=pythoncom.Empty, tolerance=pythoncom.Empty):

        return p2r_f.fit_surface(self.rhino_id, degree, tolerance)


    def flip_surface(self, flip=pythoncom.Empty):

        return p2r_f.flip_surface(self.rhino_id, flip)


    @classmethod
    def join_surfaces(cls, delete=pythoncom.Empty):

        return p2r_f.join_surfaces(self.rhino_id, delete)


    @classmethod
    def make_surface_non_periodic(cls, direction, delete=pythoncom.Empty):

        return p2r_f.make_surface_non_periodic(self.rhino_id, direction, delete)


    @classmethod
    def make_surface_periodic(cls, direction, delete=pythoncom.Empty):

        return p2r_f.make_surface_periodic(self.rhino_id, direction, delete)


    @classmethod
    def offset_surface(cls, distance):

        return p2r_f.offset_surface(self.rhino_id, distance)


    def pull_curve(self, curve, delete=pythoncom.Empty):

        return p2r_f.pull_curve(self.rhino_id, curve, delete)


    def rebuild_surface(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return p2r_f.rebuild_surface(self.rhino_id, degree, point_count)


    def remove_surface_knot(self, parameter, direction):

        return p2r_f.remove_surface_knot(self.rhino_id, parameter, direction)


    def reverse_surface(self, direction):

        return p2r_f.reverse_surface(self.rhino_id, direction)


    @classmethod
    def short_path(cls, start, end):

        return p2r_f.short_path(self.rhino_id, start, end)


    def shrink_trimmed_surface(self, ):

        return p2r_f.shrink_trimmed_surface(self.rhino_id)


    def split_brep(self, cutter, delete=pythoncom.Empty):

        return p2r_f.split_brep(self.rhino_id, cutter, delete)


    def surface_area(self, ):

        return p2r_f.surface_area(self.rhino_id)


    def surface_area_centroid(self, ):

        return p2r_f.surface_area_centroid(self.rhino_id)


    def surface_area_moments(self, ):

        return p2r_f.surface_area_moments(self.rhino_id)


    def surface_closest_point(self, point):

        return p2r_f.surface_closest_point(self.rhino_id, point)


    def surface_contour_points(self, start_point, end_point, interval=pythoncom.Empty, angle=pythoncom.Empty):

        return p2r_f.surface_contour_points(self.rhino_id, start_point, end_point, interval, angle)


    def surface_curvature(self, parameter):

        return p2r_f.surface_curvature(self.rhino_id, parameter)


    def surface_curvature_analysis(self, ):

        return p2r_f.surface_curvature_analysis(self.rhino_id)


    def surface_degree(self, direction=pythoncom.Empty):

        return p2r_f.surface_degree(self.rhino_id, direction)


    def surface_domain(self, direction):

        return p2r_f.surface_domain(self.rhino_id, direction)


    def surface_edit_points(self, return_parameters=pythoncom.Empty, return_all=pythoncom.Empty):

        return p2r_f.surface_edit_points(self.rhino_id, return_parameters, return_all)


    def surface_evaluate(self, parameter, derivative):

        return p2r_f.surface_evaluate(self.rhino_id, parameter, derivative)


    def surface_frame(self, parameter):

        return p2r_f.surface_frame(self.rhino_id, parameter)


    def surface_isocurve_density(self, density=pythoncom.Empty):

        return p2r_f.surface_isocurve_density(self.rhino_id, density)


    def surface_knot_count(self, ):

        return p2r_f.surface_knot_count(self.rhino_id)


    def surface_knots(self, ):

        return p2r_f.surface_knots(self.rhino_id)


    def surface_normal(self, parameter):

        return p2r_f.surface_normal(self.rhino_id, parameter)


    def surface_point_count(self, ):

        return p2r_f.surface_point_count(self.rhino_id)


    def surface_points(self, return_all=pythoncom.Empty):

        return p2r_f.surface_points(self.rhino_id, return_all)


    def surface_principal_curvature(self, point):

        return p2r_f.surface_principal_curvature(self.rhino_id, point)


    def surface_seam(self, direction, parameter):

        return p2r_f.surface_seam(self.rhino_id, direction, parameter)


    def surface_surface_intersection(self, surface_a, tolerance=pythoncom.Empty, create=pythoncom.Empty):

        return p2r_f.surface_surface_intersection(self.rhino_id, surface_a, tolerance, create)


    def surface_volume(self, ):

        return p2r_f.surface_volume(self.rhino_id)


    def surface_volume_centroid(self, ):

        return p2r_f.surface_volume_centroid(self.rhino_id)


    def surface_volume_moments(self, ):

        return p2r_f.surface_volume_moments(self.rhino_id)


    def surface_weights(self, ):

        return p2r_f.surface_weights(self.rhino_id)

