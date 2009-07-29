# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class NurbsSurface(_SurfaceType):    # Class constructor
    def __init__(self):
        pass
    def cut_plane(objects, start_point, end_point, normal=None):

        return _rsf.add_cut_plane(objects, start_point, end_point, normal)

    def edge_srf(objects):

        return _rsf.add_edge_srf(objects)

    def loft_srf(objects, start_pt=None, end_pt=None, type=None, style=None, value=None, closed=None):

        return _rsf.add_loft_srf(objects, start_pt, end_pt, type, style, value, closed)

    def (point_count, points, knots_u, knots_v, degree, weights):

        return _rsf.add_nurbs_surface(point_count, points, knots_u, knots_v, degree, weights)

    def planar_srf(objects):

        return _rsf.add_planar_srf(objects)

    def (plane, d_u, d_v):

        return _rsf.add_plane_surface(plane, d_u, d_v)

    def rail_rev_srf(, rail, axis):

        return _rsf.add_rail_rev_srf(, rail, axis)

    def rev_srf(, axis, start_angle=None, end_angle=None):

        return _rsf.add_rev_srf(, axis, start_angle, end_angle)

    def srf_contour_crvs(, start_point, end_point, plane, interval=None):

        return _rsf.add_srf_contour_crvs(, start_point, end_point, plane, interval)

    def srf_control_pt_grid(count, points, degree=None):

        return _rsf.add_srf_control_pt_grid(count, points, degree)

    def srf_pt(points):

        return _rsf.add_srf_pt(points)

    def srf_pt_grid(count, points, degree=None, closed=None):

        return _rsf.add_srf_pt_grid(count, points, degree, closed)

    def srf_section_crvs(, plane):

        return _rsf.add_srf_section_crvs(, plane)

    def sweep_1(, shapes, start_pt=None, end_pt=None, closed=None, style=None, style_arg=None, simplify=None, simplify_arg=None):

        return _rsf.add_sweep_1(, shapes, start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg)

    def sweep_2(rails, shapes, start_pt=None, end_pt=None, closed=None, simple_sweep=None, maintain_height=None, simplify=None, simplify_arg=None):

        return _rsf.add_sweep_2(rails, shapes, start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg)

