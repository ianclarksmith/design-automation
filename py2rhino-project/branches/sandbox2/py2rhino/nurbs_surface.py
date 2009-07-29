# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class NurbsSurface(p2r._SurfaceType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def cut_plane(cls, objects, start_point, end_point, normal=pythoncom.Empty):

        return p2r_f.add_cut_plane(trouble, start_point, end_point, normal)


    @classmethod
    def edge_srf(cls, objects):

        return p2r_f.add_edge_srf(trouble)


    @classmethod
    def loft_srf(cls, objects, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, type=pythoncom.Empty, style=pythoncom.Empty, value=pythoncom.Empty, closed=pythoncom.Empty):

        return p2r_f.add_loft_srf(trouble, start_pt, end_pt, type, style, value, closed)


    @classmethod
    def (cls, point_count, points, knots_u, knots_v, degree, weights):

        return p2r_f.add_nurbs_surface(point_count, points, knots_u, knots_v, degree, weights)


    @classmethod
    def planar_srf(cls, objects):

        return p2r_f.add_planar_srf(trouble)


    @classmethod
    def (cls, plane, d_u, d_v):

        return p2r_f.add_plane_surface(plane, d_u, d_v)


    @classmethod
    def rail_rev_srf(cls, rail, axis):

        return p2r_f.add_rail_rev_srf(self.rhino_id, rail, axis)


    @classmethod
    def rev_srf(cls, axis, start_angle=pythoncom.Empty, end_angle=pythoncom.Empty):

        return p2r_f.add_rev_srf(self.rhino_id, axis, start_angle, end_angle)


    @classmethod
    def srf_contour_crvs(cls, start_point, end_point, plane, interval=pythoncom.Empty):

        return p2r_f.add_srf_contour_crvs(self.rhino_id, start_point, end_point, plane, interval)


    @classmethod
    def srf_control_pt_grid(cls, count, points, degree=pythoncom.Empty):

        return p2r_f.add_srf_control_pt_grid(count, points, degree)


    @classmethod
    def srf_pt(cls, points):

        return p2r_f.add_srf_pt(points)


    @classmethod
    def srf_pt_grid(cls, count, points, degree=pythoncom.Empty, closed=pythoncom.Empty):

        return p2r_f.add_srf_pt_grid(count, points, degree, closed)


    @classmethod
    def srf_section_crvs(cls, plane):

        return p2r_f.add_srf_section_crvs(self.rhino_id, plane)


    @classmethod
    def sweep_1(cls, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, style=pythoncom.Empty, style_arg=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):

        return p2r_f.add_sweep_1(self.rhino_id, shapes, start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg)


    @classmethod
    def sweep_2(cls, rails, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, simple_sweep=pythoncom.Empty, maintain_height=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):

        return p2r_f.add_sweep_2(trouble, trouble, start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg)

