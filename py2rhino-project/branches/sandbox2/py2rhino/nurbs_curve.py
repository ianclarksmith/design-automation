# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class NurbsCurve(p2r._CurveType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_crv_by_points(cls, points, degree=pythoncom.Empty):

        return p2r_f.add_curve(points, degree)


    @classmethod
    def create_fillet_crv(cls, curve_0, curve_1, radius=pythoncom.Empty, point_0=pythoncom.Empty, point_1=pythoncom.Empty):

        return p2r_f.add_fillet_curve(curve_0.rhino_id, curve_1.rhino_id, radius, point_0, point_1)


    @classmethod
    def create_interp_crv_on_srf(cls, surface, points):

        return p2r_f.add_interp_crv_on_srf(surface.rhino_id, points)


    @classmethod
    def create_interp_crv_on_srf_uv(cls, surface, points):

        return p2r_f.add_interp_crv_on_srf_u_v(surface.rhino_id, points)


    @classmethod
    def create_interp_crv(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):

        return p2r_f.add_interp_curve(points, degree, knot_style, start_tan, end_tan)


    @classmethod
    def create_interp_crv_ex(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):

        return p2r_f.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)


    @classmethod
    def create_crv(cls, points, knots, degree, weights=pythoncom.Empty):

        return p2r_f.add_nurbs_curve(points, knots, degree, weights)


    @classmethod
    def create_sub_crv(cls, curve, param_0, param_1):

        return p2r_f.add_sub_crv(curve.rhino_id, param_0, param_1)

