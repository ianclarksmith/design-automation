# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_box(corners):

    return _rsf.add_box(corners)

def add_cone(base, height_pnt, radius, cap=pythoncom.Empty):

    return _rsf.add_cone(base, height_pnt, radius, cap)

def add_cone_2(plane, height, radius, cap=pythoncom.Empty):

    return _rsf.add_cone_2(plane, height, radius, cap)

def add_cut_plane(objects, start_point, end_point, normal=pythoncom.Empty):

    return _rsf.add_cut_plane(objects, start_point, end_point, normal)

def add_cylinder(base, height_pnt, radius, cap=pythoncom.Empty):

    return _rsf.add_cylinder(base, height_pnt, radius, cap)

def add_cylinder_2(plane, height, radius, cap=pythoncom.Empty):

    return _rsf.add_cylinder_2(plane, height, radius, cap)

def add_edge_srf(objects):

    return _rsf.add_edge_srf(objects)

def add_loft_srf(objects, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, type=pythoncom.Empty, style=pythoncom.Empty, value=pythoncom.Empty, closed=pythoncom.Empty):

    return _rsf.add_loft_srf(objects, start_pt, end_pt, type, style, value, closed)

def add_nurbs_surface(point_count, points, knots_u, knots_v, degree, weights):

    return _rsf.add_nurbs_surface(point_count, points, knots_u, knots_v, degree, weights)

def add_planar_srf(objects):

    return _rsf.add_planar_srf(objects)

def add_plane_surface(plane, d_u, d_v):

    return _rsf.add_plane_surface(plane, d_u, d_v)

def add_rail_rev_srf(profile, rail, axis):

    return _rsf.add_rail_rev_srf(profile, rail, axis)

def add_rev_srf(profile, axis, start_angle=pythoncom.Empty, end_angle=pythoncom.Empty):

    return _rsf.add_rev_srf(profile, axis, start_angle, end_angle)

def add_sphere(center, radius):

    return _rsf.add_sphere(center, radius)

def add_sphere_2(plane, radius):

    return _rsf.add_sphere_2(plane, radius)

def add_srf_contour_crvs(object, start_point, end_point, interval=pythoncom.Empty):

    return _rsf.add_srf_contour_crvs(object, start_point, end_point, interval)

def add_srf_contour_crvs_2(object, plane, interval=pythoncom.Empty):

    return _rsf.add_srf_contour_crvs_2(object, plane, interval)

def add_srf_control_pt_grid(count, points, degree=pythoncom.Empty):

    return _rsf.add_srf_control_pt_grid(count, points, degree)

def add_srf_pt(points):

    return _rsf.add_srf_pt(points)

def add_srf_pt_grid(count, points, degree=pythoncom.Empty, closed=pythoncom.Empty):

    return _rsf.add_srf_pt_grid(count, points, degree, closed)

def add_srf_section_crvs(object, plane):

    return _rsf.add_srf_section_crvs(object, plane)

def add_sweep_1(rail, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, style=pythoncom.Empty, style_arg=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):

    return _rsf.add_sweep_1(rail, shapes, start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg)

def add_sweep_2(rails, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, simple_sweep=pythoncom.Empty, maintain_height=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):

    return _rsf.add_sweep_2(rails, shapes, start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg)

def add_torus(base, major_radius, minor_radius, direction=pythoncom.Empty):

    return _rsf.add_torus(base, major_radius, minor_radius, direction)

def add_torus_2(plane, major_radius, minor_radius):

    return _rsf.add_torus_2(plane, major_radius, minor_radius)

def boolean_difference(input_0, input_1, delete=pythoncom.Empty):

    return _rsf.boolean_difference(input_0, input_1, delete)

def boolean_intersection(input_0, input_1, delete=pythoncom.Empty):

    return _rsf.boolean_intersection(input_0, input_1, delete)

def boolean_union(input, delete=pythoncom.Empty):

    return _rsf.boolean_union(input, delete)

def brep_closest_point(object, point):

    return _rsf.brep_closest_point(object, point)

def cap_planar_holes(surface):

    return _rsf.cap_planar_holes(surface)

def duplicate_edge_curves(object, select=pythoncom.Empty):

    return _rsf.duplicate_edge_curves(object, select)

def duplicate_surface_border(object):

    return _rsf.duplicate_surface_border(object)

def evaluate_surface(object, parameter):

    return _rsf.evaluate_surface(object, parameter)

def explode_polysurfaces(objects, delete=pythoncom.Empty):

    return _rsf.explode_polysurfaces(objects, delete)

def extract_iso_curve(object, parameter, dir):

    return _rsf.extract_iso_curve(object, parameter, dir)

def extrude_curve(curve, path):

    return _rsf.extrude_curve(curve, path)

def extrude_curve_point(curve, point):

    return _rsf.extrude_curve_point(curve, point)

def extrude_curve_straight(curve, start_point, end_point):

    return _rsf.extrude_curve_straight(curve, start_point, end_point)

def extrude_curve_tapered(curve, distance, direction, base_point, angle, corner_type=pythoncom.Empty):

    return _rsf.extrude_curve_tapered(curve, distance, direction, base_point, angle, corner_type)

def extrude_surface(surface, curve, cap=pythoncom.Empty):

    return _rsf.extrude_surface(surface, curve, cap)

def fit_surface(object, degree=pythoncom.Empty, tolerance=pythoncom.Empty):

    return _rsf.fit_surface(object, degree, tolerance)

def flip_surface(object, flip=pythoncom.Empty):

    return _rsf.flip_surface(object, flip)

def insert_surface_knot(object, parameter, direction, symmetrical=pythoncom.Empty):

    return _rsf.insert_surface_knot(object, parameter, direction, symmetrical)

def intersect_breps(brep_1, brep_2, tolerance=pythoncom.Empty):

    return _rsf.intersect_breps(brep_1, brep_2, tolerance)

def is_brep(object):

    return _rsf.is_brep(object)

def is_brep_manifold(object):

    return _rsf.is_brep_manifold(object)

def is_cone(surface):

    return _rsf.is_cone(surface)

def is_cylinder(surface):

    return _rsf.is_cylinder(surface)

def is_parameter_on_surface(object, parameter):

    return _rsf.is_parameter_on_surface(object, parameter)

def is_plane_surface(object):

    return _rsf.is_plane_surface(object)

def is_point_in_surface(object, point):

    return _rsf.is_point_in_surface(object, point)

def is_point_on_surface(object, point):

    return _rsf.is_point_on_surface(object, point)

def is_poly_surface(object):

    return _rsf.is_poly_surface(object)

def is_poly_surface_closed(object):

    return _rsf.is_poly_surface_closed(object)

def is_poly_surface_planar(object):

    return _rsf.is_poly_surface_planar(object)

def is_sphere(surface):

    return _rsf.is_sphere(surface)

def is_surface(object):

    return _rsf.is_surface(object)

def is_surface_closed(object, direction):

    return _rsf.is_surface_closed(object, direction)

def is_surface_periodic(object, direction):

    return _rsf.is_surface_periodic(object, direction)

def is_surface_planar(object, tolerance=pythoncom.Empty):

    return _rsf.is_surface_planar(object, tolerance)

def is_surface_rational(object):

    return _rsf.is_surface_rational(object)

def is_surface_singular(object, direction):

    return _rsf.is_surface_singular(object, direction)

def is_surface_trimmed(object):

    return _rsf.is_surface_trimmed(object)

def is_torus(surface):

    return _rsf.is_torus(surface)

def join_surfaces(object, delete=pythoncom.Empty):

    return _rsf.join_surfaces(object, delete)

def make_surface_non_periodic(object, direction, delete=pythoncom.Empty):

    return _rsf.make_surface_non_periodic(object, direction, delete)

def make_surface_periodic(object, direction, delete=pythoncom.Empty):

    return _rsf.make_surface_periodic(object, direction, delete)

def offset_surface(object, distance):

    return _rsf.offset_surface(object, distance)

def pull_curve(surface, curve, delete=pythoncom.Empty):

    return _rsf.pull_curve(surface, curve, delete)

def rebuild_surface(object, degree=pythoncom.Empty, point_count=pythoncom.Empty):

    return _rsf.rebuild_surface(object, degree, point_count)

def remove_surface_knot(object, parameter, direction):

    return _rsf.remove_surface_knot(object, parameter, direction)

def reverse_surface(object, direction):

    return _rsf.reverse_surface(object, direction)

def short_path(surface, start, end):

    return _rsf.short_path(surface, start, end)

def shrink_trimmed_surface(surface):

    return _rsf.shrink_trimmed_surface(surface)

def split_brep(brep, cutter, delete=pythoncom.Empty):

    return _rsf.split_brep(brep, cutter, delete)

def surface_area(object):

    return _rsf.surface_area(object)

def surface_area_centroid(object):

    return _rsf.surface_area_centroid(object)

def surface_area_moments(object):

    return _rsf.surface_area_moments(object)

def surface_closest_point(object, point):

    return _rsf.surface_closest_point(object, point)

def surface_cone(surface):

    return _rsf.surface_cone(surface)

def surface_contour_points(object, start_point, end_point, interval=pythoncom.Empty, angle=pythoncom.Empty):

    return _rsf.surface_contour_points(object, start_point, end_point, interval, angle)

def surface_curvature(object, parameter):

    return _rsf.surface_curvature(object, parameter)

def surface_curvature_analysis(object):

    return _rsf.surface_curvature_analysis(object)

def surface_cylinder(surface):

    return _rsf.surface_cylinder(surface)

def surface_degree(object, direction=pythoncom.Empty):

    return _rsf.surface_degree(object, direction)

def surface_domain(object, direction):

    return _rsf.surface_domain(object, direction)

def surface_edit_points(object, return_parameters=pythoncom.Empty, return_all=pythoncom.Empty):

    return _rsf.surface_edit_points(object, return_parameters, return_all)

def surface_evaluate(object, parameter, derivative):

    return _rsf.surface_evaluate(object, parameter, derivative)

def surface_frame(object, parameter):

    return _rsf.surface_frame(object, parameter)

def surface_isocurve_density(object, density=pythoncom.Empty):

    return _rsf.surface_isocurve_density(object, density)

def surface_knot_count(object):

    return _rsf.surface_knot_count(object)

def surface_knots(object):

    return _rsf.surface_knots(object)

def surface_normal(object, parameter):

    return _rsf.surface_normal(object, parameter)

def surface_point_count(object):

    return _rsf.surface_point_count(object)

def surface_points(object, return_all=pythoncom.Empty):

    return _rsf.surface_points(object, return_all)

def surface_principal_curvature(object, point):

    return _rsf.surface_principal_curvature(object, point)

def surface_seam(object, direction, parameter):

    return _rsf.surface_seam(object, direction, parameter)

def surface_sphere(surface):

    return _rsf.surface_sphere(surface)

def surface_surface_intersection(surface_a, surface_b, tolerance=pythoncom.Empty, create=pythoncom.Empty):

    return _rsf.surface_surface_intersection(surface_a, surface_b, tolerance, create)

def surface_torus(surface):

    return _rsf.surface_torus(surface)

def surface_volume(object):

    return _rsf.surface_volume(object)

def surface_volume_centroid(object):

    return _rsf.surface_volume_centroid(object)

def surface_volume_moments(object):

    return _rsf.surface_volume_moments(object)

def surface_weights(object):

    return _rsf.surface_weights(object)

