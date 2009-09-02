# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_arc(plane, radius, angle):

    return _rsf.add_arc(plane, radius, angle)

def add_arc_3_pt(start, end, point):

    return _rsf.add_arc_3_pt(start, end, point)

def add_circle(plane, radius):

    return _rsf.add_circle(plane, radius)

def add_circle_3_pt(first, second, third):

    return _rsf.add_circle_3_pt(first, second, third)

def add_curve(points, degree=pythoncom.Empty):

    return _rsf.add_curve(points, degree)

def add_ellipse(plane, x_radius, y_radius):

    return _rsf.add_ellipse(plane, x_radius, y_radius)

def add_ellipse_3_pt(center, second, third):

    return _rsf.add_ellipse_3_pt(center, second, third)

def add_fillet_curve(curve_0, curve_1, radius=pythoncom.Empty, point_0=pythoncom.Empty, point_1=pythoncom.Empty):

    return _rsf.add_fillet_curve(curve_0, curve_1, radius, point_0, point_1)

def add_interp_crv_on_srf(object, points):

    return _rsf.add_interp_crv_on_srf(object, points)

def add_interp_crv_on_srf_u_v(object, points):

    return _rsf.add_interp_crv_on_srf_u_v(object, points)

def add_interp_curve(points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):

    return _rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)

def add_interp_curve_ex(points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):

    return _rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)

def add_line(start, end):

    return _rsf.add_line(start, end)

def add_nurbs_curve(points, knots, degree, weights=pythoncom.Empty):

    return _rsf.add_nurbs_curve(points, knots, degree, weights)

def add_polyline(points):

    return _rsf.add_polyline(points)

def add_sub_crv(object, param_0, param_1):

    return _rsf.add_sub_crv(object, param_0, param_1)

def arc_angle(object, index=pythoncom.Empty):

    return _rsf.arc_angle(object, index)

def arc_center_point(object, index=pythoncom.Empty):

    return _rsf.arc_center_point(object, index)

def arc_mid_point(object, index=pythoncom.Empty):

    return _rsf.arc_mid_point(object, index)

def arc_radius(object, index=pythoncom.Empty):

    return _rsf.arc_radius(object, index)

def circle_center_point(object, index=pythoncom.Empty):

    return _rsf.circle_center_point(object, index)

def circle_circumference(object, index=pythoncom.Empty):

    return _rsf.circle_circumference(object, index)

def circle_radius(object, index=pythoncom.Empty):

    return _rsf.circle_radius(object, index)

def close_curve(object, tolerance=pythoncom.Empty):

    return _rsf.close_curve(object, tolerance)

def convert_curve_to_polyline(object, angle_tolerance=pythoncom.Empty, tolerance=pythoncom.Empty, delete_input=pythoncom.Empty):

    return _rsf.convert_curve_to_polyline(object, angle_tolerance, tolerance, delete_input)

def curve_arc_length_point(object, length, from_start=pythoncom.Empty):

    return _rsf.curve_arc_length_point(object, length, from_start)

def curve_area(objects):

    return _rsf.curve_area(objects)

def curve_area_centroid(objects):

    return _rsf.curve_area_centroid(objects)

def curve_arrows(object, style=pythoncom.Empty):

    return _rsf.curve_arrows(object, style)

def curve_boolean_difference(curve_a, curve_b):

    return _rsf.curve_boolean_difference(curve_a, curve_b)

def curve_boolean_intersection(curve_a, curve_b):

    return _rsf.curve_boolean_intersection(curve_a, curve_b)

def curve_boolean_union(curves):

    return _rsf.curve_boolean_union(curves)

def curve_brep_intersect(curve, brep, tolerance=pythoncom.Empty):

    return _rsf.curve_brep_intersect(curve, brep, tolerance)

def curve_closest_object(curve, objects):

    return _rsf.curve_closest_object(curve, objects)

def curve_closest_point(object, point, index=pythoncom.Empty):

    return _rsf.curve_closest_point(object, point, index)

def curve_contour_points(object, start_point, end_point, interval=pythoncom.Empty):

    return _rsf.curve_contour_points(object, start_point, end_point, interval)

def curve_curvature(object, parameter):

    return _rsf.curve_curvature(object, parameter)

def curve_curve_intersection(object_1, object_2=pythoncom.Empty, tolerance=pythoncom.Empty):

    return _rsf.curve_curve_intersection(object_1, object_2, tolerance)

def curve_degree(object, index=pythoncom.Empty):

    return _rsf.curve_degree(object, index)

def curve_deviation(curve_a, curve_b):

    return _rsf.curve_deviation(curve_a, curve_b)

def curve_dim(object, index=pythoncom.Empty):

    return _rsf.curve_dim(object, index)

def curve_directions_match(curve_1, curve_2):

    return _rsf.curve_directions_match(curve_1, curve_2)

def curve_discontinuity(object, style):

    return _rsf.curve_discontinuity(object, style)

def curve_domain(object, index=pythoncom.Empty):

    return _rsf.curve_domain(object, index)

def curve_edit_points(object, return_parameters=pythoncom.Empty, index=pythoncom.Empty):

    return _rsf.curve_edit_points(object, return_parameters, index)

def curve_end_point(object, index=pythoncom.Empty):

    return _rsf.curve_end_point(object, index)

def curve_evaluate(object, parameter, derivative):

    return _rsf.curve_evaluate(object, parameter, derivative)

def curve_fillet_points(curve_0, curve_1, radius=pythoncom.Empty, base_point_0=pythoncom.Empty, base_point_1=pythoncom.Empty):

    return _rsf.curve_fillet_points(curve_0, curve_1, radius, base_point_0, base_point_1)

def curve_frame(object, parameter):

    return _rsf.curve_frame(object, parameter)

def curve_knot_count(object, index=pythoncom.Empty):

    return _rsf.curve_knot_count(object, index)

def curve_knots(object, index=pythoncom.Empty):

    return _rsf.curve_knots(object, index)

def curve_length(object, index=pythoncom.Empty, sub_domain=pythoncom.Empty):

    return _rsf.curve_length(object, index, sub_domain)

def curve_mid_point(object):

    return _rsf.curve_mid_point(object)

def curve_normal(object):

    return _rsf.curve_normal(object)

def curve_perp_frame(object, parameter):

    return _rsf.curve_perp_frame(object, parameter)

def curve_plane(curve):

    return _rsf.curve_plane(curve)

def curve_point_count(object, index=pythoncom.Empty):

    return _rsf.curve_point_count(object, index)

def curve_points(object, index=pythoncom.Empty):

    return _rsf.curve_points(object, index)

def curve_radius(object, point, index=pythoncom.Empty):

    return _rsf.curve_radius(object, point, index)

def curve_seam(object, parameter):

    return _rsf.curve_seam(object, parameter)

def curve_start_point(object, index=pythoncom.Empty):

    return _rsf.curve_start_point(object, index)

def curve_surface_intersection(curve, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):

    return _rsf.curve_surface_intersection(curve, surface, tolerance, angle_tolerance)

def curve_tangent(object, parameter, index=pythoncom.Empty):

    return _rsf.curve_tangent(object, parameter, index)

def curve_weights(object, index=pythoncom.Empty):

    return _rsf.curve_weights(object, index)

def divide_curve(object, segments, create=pythoncom.Empty, points=pythoncom.Empty):

    return _rsf.divide_curve(object, segments, create, points)

def divide_curve_equidistant(object, distance, create=pythoncom.Empty, points=pythoncom.Empty):

    return _rsf.divide_curve_equidistant(object, distance, create, points)

def divide_curve_length(object, length, create=pythoncom.Empty, points=pythoncom.Empty):

    return _rsf.divide_curve_length(object, length, create, points)

def ellipse_center_point(object):

    return _rsf.ellipse_center_point(object)

def ellipse_quad_points(object):

    return _rsf.ellipse_quad_points(object)

def evaluate_curve(object, parameter, index=pythoncom.Empty):

    return _rsf.evaluate_curve(object, parameter, index)

def explode_curves(objects, delete=pythoncom.Empty):

    return _rsf.explode_curves(objects, delete)

def extend_curve(object, type, side, objects):

    return _rsf.extend_curve(object, type, side, objects)

def extend_curve_length(object, type, side, length):

    return _rsf.extend_curve_length(object, type, side, length)

def extend_curve_point(object, side, point):

    return _rsf.extend_curve_point(object, side, point)

def fair_curve(object, tolerance=pythoncom.Empty):

    return _rsf.fair_curve(object, tolerance)

def fit_curve(object, degree=pythoncom.Empty, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):

    return _rsf.fit_curve(object, degree, tolerance, angle_tolerance)

def insert_curve_knot(object, parameter, symmetrical=pythoncom.Empty):

    return _rsf.insert_curve_knot(object, parameter, symmetrical)

def is_arc(object, index=pythoncom.Empty):

    return _rsf.is_arc(object, index)

def is_circle(object, index=pythoncom.Empty):

    return _rsf.is_circle(object, index)

def is_curve(object, index=pythoncom.Empty):

    return _rsf.is_curve(object, index)

def is_curve_closable(object, tolerance=pythoncom.Empty):

    return _rsf.is_curve_closable(object, tolerance)

def is_curve_closed(object, index=pythoncom.Empty):

    return _rsf.is_curve_closed(object, index)

def is_curve_in_plane(object, plane=pythoncom.Empty):

    return _rsf.is_curve_in_plane(object, plane)

def is_curve_linear(object, index=pythoncom.Empty):

    return _rsf.is_curve_linear(object, index)

def is_curve_periodic(object, index=pythoncom.Empty):

    return _rsf.is_curve_periodic(object, index)

def is_curve_planar(object, index=pythoncom.Empty):

    return _rsf.is_curve_planar(object, index)

def is_curve_rational(object, index=pythoncom.Empty):

    return _rsf.is_curve_rational(object, index)

def is_ellipse(object):

    return _rsf.is_ellipse(object)

def is_line(object, index=pythoncom.Empty):

    return _rsf.is_line(object, index)

def is_point_on_curve(object, point, index=pythoncom.Empty):

    return _rsf.is_point_on_curve(object, point, index)

def is_poly_curve(object, index=pythoncom.Empty):

    return _rsf.is_poly_curve(object, index)

def is_polyline(object, index=pythoncom.Empty):

    return _rsf.is_polyline(object, index)

def join_curves(objects, delete=pythoncom.Empty):

    return _rsf.join_curves(objects, delete)

def line_fit_from_points(object):

    return _rsf.line_fit_from_points(object)

def make_curve_non_periodic(object, delete=pythoncom.Empty):

    return _rsf.make_curve_non_periodic(object, delete)

def make_curve_periodic(object, delete=pythoncom.Empty):

    return _rsf.make_curve_periodic(object, delete)

def mesh_polyline(polyline):

    return _rsf.mesh_polyline(polyline)

def offset_curve(object, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):

    return _rsf.offset_curve(object, direction, distance, normal, style)

def offset_curve_on_surface(curve, surface, distance):

    return _rsf.offset_curve_on_surface(curve, surface, distance)

def offset_curve_on_surface_2(curve, surface, parameter):

    return _rsf.offset_curve_on_surface_2(curve, surface, parameter)

def planar_closed_curve_containment(curve_1, curve_2, plane=pythoncom.Empty, tolerance=pythoncom.Empty):

    return _rsf.planar_closed_curve_containment(curve_1, curve_2, plane, tolerance)

def planar_curve_collision(curve_1, curve_2, plane=pythoncom.Empty, tolerance=pythoncom.Empty):

    return _rsf.planar_curve_collision(curve_1, curve_2, plane, tolerance)

def point_in_planar_closed_curve(point, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):

    return _rsf.point_in_planar_closed_curve(point, curve, plane, tolerance)

def poly_curve_count(object, index=pythoncom.Empty):

    return _rsf.poly_curve_count(object, index)

def polyline_vertices(object, index=pythoncom.Empty):

    return _rsf.polyline_vertices(object, index)

def project_curve_to_mesh(curves, meshes, direction):

    return _rsf.project_curve_to_mesh(curves, meshes, direction)

def project_curve_to_surface(curves, surfaces, direction):

    return _rsf.project_curve_to_surface(curves, surfaces, direction)

def rebuild_curve(object, degree=pythoncom.Empty, point_count=pythoncom.Empty):

    return _rsf.rebuild_curve(object, degree, point_count)

def remove_curve_knot(object, parameter):

    return _rsf.remove_curve_knot(object, parameter)

def reverse_curve(object):

    return _rsf.reverse_curve(object)

def simplify_curve(object, flags=pythoncom.Empty):

    return _rsf.simplify_curve(object, flags)

def split_curve(object, parameters, delete=pythoncom.Empty):

    return _rsf.split_curve(object, parameters, delete)

def trim_curve(object, interval, delete=pythoncom.Empty):

    return _rsf.trim_curve(object, interval, delete)

