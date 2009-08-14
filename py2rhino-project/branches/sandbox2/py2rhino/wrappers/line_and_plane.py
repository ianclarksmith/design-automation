# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def distance_to_plane(plane, point):

    return _rsf.distance_to_plane(plane, point)

def evaluate_plane(plane, parameter):

    return _rsf.evaluate_plane(plane, parameter)

def intersect_planes(plane_1, plane_2, plane_3):

    return _rsf.intersect_planes(plane_1, plane_2, plane_3)

def line_closest_point(line, point):

    return _rsf.line_closest_point(line, point)

def line_is_farther_than(line, distance, point):

    return _rsf.line_is_farther_than(line, distance, point)

def line_is_farther_than_2(line, distance, line_2):

    return _rsf.line_is_farther_than_2(line, distance, line_2)

def line_line_intersection(line_a, line_b, planar=pythoncom.Empty):

    return _rsf.line_line_intersection(line_a, line_b, planar)

def line_max_distance_to(line, point):

    return _rsf.line_max_distance_to(line, point)

def line_max_distance_to_2(line, line_2):

    return _rsf.line_max_distance_to_2(line, line_2)

def line_min_distance_to(line, point):

    return _rsf.line_min_distance_to(line, point)

def line_min_distance_to_2(line, line_2):

    return _rsf.line_min_distance_to_2(line, line_2)

def line_plane(line):

    return _rsf.line_plane(line)

def line_plane_intersection(line, point):

    return _rsf.line_plane_intersection(line, point)

def line_transform(line, xform):

    return _rsf.line_transform(line, xform)

def move_plane(plane, origin):

    return _rsf.move_plane(plane, origin)

def plane_closest_point(plane, point, return_point=pythoncom.Empty):

    return _rsf.plane_closest_point(plane, point, return_point)

def plane_equation(plane):

    return _rsf.plane_equation(plane)

def plane_fit_from_points(points):

    return _rsf.plane_fit_from_points(points)

def plane_from_frame(origin, xaxis, yaxis):

    return _rsf.plane_from_frame(origin, xaxis, yaxis)

def plane_from_normal(origin, normal):

    return _rsf.plane_from_normal(origin, normal)

def plane_from_points(origin, point_x, point_y):

    return _rsf.plane_from_points(origin, point_x, point_y)

def plane_plane_intersection(plane_1, point_2):

    return _rsf.plane_plane_intersection(plane_1, point_2)

def plane_transform(plane, xform):

    return _rsf.plane_transform(plane, xform)

def rotate_plane(plane, angle, axis):

    return _rsf.rotate_plane(plane, angle, axis)

def world_x_y_plane():

    return _rsf.world_x_y_plane()

def world_y_z_plane():

    return _rsf.world_y_z_plane()

def world_z_x_plane():

    return _rsf.world_z_x_plane()

