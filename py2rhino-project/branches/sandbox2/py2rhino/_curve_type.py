# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class _CurveType(p2r._Object):


    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    def close_curve(self, tolerance=pythoncom.Empty):

        return p2r_f.close_curve(self.rhino_id, tolerance)


    def convert_curve_to_polyline(self, angle_tolerance=pythoncom.Empty, tolerance=pythoncom.Empty, delete_input=pythoncom.Empty):

        return p2r_f.convert_curve_to_polyline(self.rhino_id, angle_tolerance, tolerance, delete_input)


    def curve_arc_length_point(self, length, from_start=pythoncom.Empty):

        return p2r_f.curve_arc_length_point(self.rhino_id, length, from_start)


    def area(self, ):

        return p2r_f.curve_area(map(lambda i: i.rhino_id, ))


    def curve_area_centroid(self, objects):

        return p2r_f.curve_area_centroid(map(lambda i: i.rhino_id, objects))


    def arrows(self, style=pythoncom.Empty):

        return p2r_f.curve_arrows(self.rhino_id, style)


    def boolean_difference(self, curve):

        return p2r_f.curve_boolean_difference(self.rhino_id, curve)


    def boolean_intersection(self, curve_a):

        return p2r_f.curve_boolean_intersection(self.rhino_id, curve_a)


    def boolean_union(self, curves):

        return p2r_f.curve_boolean_union(map(lambda i: i.rhino_id, curves))


    def brep_intersect(self, brep, tolerance=pythoncom.Empty):

        return p2r_f.curve_brep_intersect(self.rhino_id, brep, tolerance)


    def closest_object(self, objects):

        return p2r_f.curve_closest_object(self.rhino_id, map(lambda i: i.rhino_id, objects))


    def closest_point(self, point, index=pythoncom.Empty):

        return p2r_f.curve_closest_point(self.rhino_id, point, index)


    def contour_points(self, start_point, end_point, interval=pythoncom.Empty):

        return p2r_f.curve_contour_points(self.rhino_id, start_point, end_point, interval)


    def curvature(self, parameter):

        return p2r_f.curve_curvature(self.rhino_id, parameter)


    def curve_curve_intersection(self, object_1=pythoncom.Empty, tolerance=pythoncom.Empty):

        return p2r_f.curve_curve_intersection(self.rhino_id, object_1, tolerance)


    def degree(self, index=pythoncom.Empty):

        return p2r_f.curve_degree(self.rhino_id, index)


    def deviation(self, curve_a):

        return p2r_f.curve_deviation(self.rhino_id, curve_a)


    def dim(self, index=pythoncom.Empty):

        return p2r_f.curve_dim(self.rhino_id, index)


    def directions_match(self, curve_1):

        return p2r_f.curve_directions_match(self.rhino_id, curve_1)


    def discontinuity(self, style):

        return p2r_f.curve_discontinuity(self.rhino_id, style)


    def domain(self, index=pythoncom.Empty):

        return p2r_f.curve_domain(self.rhino_id, index)


    def edit_points(self, return_parameters=pythoncom.Empty, index=pythoncom.Empty):

        return p2r_f.curve_edit_points(self.rhino_id, return_parameters, index)


    def end_point(self, index=pythoncom.Empty):

        return p2r_f.curve_end_point(self.rhino_id, index)


    def evaluate(self, parameter, derivative):

        return p2r_f.curve_evaluate(self.rhino_id, parameter, derivative)


    def fillet_points(self, curve_0, radius=pythoncom.Empty, base_point_0=pythoncom.Empty, base_point__1=pythoncom.Empty):

        return p2r_f.curve_fillet_points(self.rhino_id, curve_0, radius, base_point_0, base_point__1)


    def frame(self, parameter):

        return p2r_f.curve_frame(self.rhino_id, parameter)


    def knot_count(self, index=pythoncom.Empty):

        return p2r_f.curve_knot_count(self.rhino_id, index)


    def knots(self, index=pythoncom.Empty):

        return p2r_f.curve_knots(self.rhino_id, index)


    def length(self, index=pythoncom.Empty, sub_domain=pythoncom.Empty):

        return p2r_f.curve_length(self.rhino_id, index, sub_domain)


    def mid_point(self, ):

        return p2r_f.curve_mid_point(self.rhino_id)


    def normal(self, ):

        return p2r_f.curve_normal(self.rhino_id)


    def curve_perp_frame(self, parameter):

        return p2r_f.curve_perp_frame(self.rhino_id, parameter)


    def curve_plane(self, ):

        return p2r_f.curve_plane(self.rhino_id)


    def curve_point_count(self, index=pythoncom.Empty):

        return p2r_f.curve_point_count(self.rhino_id, index)


    def curve_points(self, index=pythoncom.Empty):

        return p2r_f.curve_points(self.rhino_id, index)


    def radius(self, point, index=pythoncom.Empty):

        return p2r_f.curve_radius(self.rhino_id, point, index)


    def seam(self, parameter):

        return p2r_f.curve_seam(self.rhino_id, parameter)


    def start_point(self, index=pythoncom.Empty):

        return p2r_f.curve_start_point(self.rhino_id, index)


    def surface_intersection(self, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):

        return p2r_f.curve_surface_intersection(self.rhino_id, surface, tolerance, angle_tolerance)


    def tangent(self, parameter, index=pythoncom.Empty):

        return p2r_f.curve_tangent(self.rhino_id, parameter, index)


    def weights(self, index=pythoncom.Empty):

        return p2r_f.curve_weights(self.rhino_id, index)


    def divide_curve(self, segments, create=pythoncom.Empty, points=pythoncom.Empty):

        return p2r_f.divide_curve(self.rhino_id, segments, create, points)


    def divide_curve_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):

        return p2r_f.divide_curve_equidistant(self.rhino_id, distance, create, points)


    def divide_curve_length(self, length, create=pythoncom.Empty, points=pythoncom.Empty):

        return p2r_f.divide_curve_length(self.rhino_id, length, create, points)


    def evaluate_curve(self, parameter, index=pythoncom.Empty):

        return p2r_f.evaluate_curve(self.rhino_id, parameter, index)


    def explode(self, delete=pythoncom.Empty):

        return p2r_f.explode_curves(self.rhino_id, delete)


    def extend_curve(self, type, side, objects):

        return p2r_f.extend_curve(self.rhino_id, type, side, objects)


    def extend_curve_length(self, type, side, length):

        return p2r_f.extend_curve_length(self.rhino_id, type, side, length)


    def extend_curve_point(self, side, point):

        return p2r_f.extend_curve_point(self.rhino_id, side, point)


    def fair_curve(self, tolerance=pythoncom.Empty):

        return p2r_f.fair_curve(self.rhino_id, tolerance)


    def fit_curve(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):

        return p2r_f.fit_curve(self.rhino_id, degree, tolerance, angle_tolerance)


    def insert_curve_knot(self, parameter, symmetrical=pythoncom.Empty):

        return p2r_f.insert_curve_knot(self.rhino_id, parameter, symmetrical)


    def line_fit_from_points(self, ):

        return p2r_f.line_fit_from_points(self.rhino_id)


    def make_curve_non_periodic(self, delete=pythoncom.Empty):

        return p2r_f.make_curve_non_periodic(self.rhino_id, delete)


    def make_curve_periodic(self, delete=pythoncom.Empty):

        return p2r_f.make_curve_periodic(self.rhino_id, delete)


    def offset_curve(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):

        return p2r_f.offset_curve(self.rhino_id, direction, distance, normal, style)


    def offset_curve_on_surface(self, surface, distance, parameter):

        return p2r_f.offset_curve_on_surface(self.rhino_id, surface, distance, parameter)


    def planar_closed_curve_containment(self, curve__1, plane=pythoncom.Empty, tolerance=pythoncom.Empty):

        return p2r_f.planar_closed_curve_containment(self.rhino_id, curve__1, plane, tolerance)


    def planar_curve_collision(self, curve_0, plane=pythoncom.Empty, tolerance=pythoncom.Empty):

        return p2r_f.planar_curve_collision(self.rhino_id, curve_0, plane, tolerance)


    def point_in_planar_closed_curve(self, point, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):

        return p2r_f.point_in_planar_closed_curve(point, curve, plane, tolerance)


    def project_curve_to_mesh(self, curves, meshes, direction):

        return p2r_f.project_curve_to_mesh(map(lambda i: i.rhino_id, curves), meshes, direction)


    def project_to_surface(self, surfaces, direction):

        return p2r_f.project_curve_to_surface(self.rhino_id, surfaces, direction)


    def rebuild_curve(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return p2r_f.rebuild_curve(self.rhino_id, degree, point_count)


    def remove_curve_knot(self, parameter):

        return p2r_f.remove_curve_knot(self.rhino_id, parameter)


    def reverse_curve(self, ):

        return p2r_f.reverse_curve(self.rhino_id)


    def simplify_curve(self, flags=pythoncom.Empty):

        return p2r_f.simplify_curve(self.rhino_id, flags)


    def split_curve(self, parameters, delete=pythoncom.Empty):

        return p2r_f.split_curve(self.rhino_id, parameters, delete)


    def trim_curve(self, interval, delete=pythoncom.Empty):

        return p2r_f.trim_curve(self.rhino_id, interval, delete)
