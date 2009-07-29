# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class Curve(_CurveType):    # Class constructor
    def __init__(self):
        pass
    def (points, degree=None):

        return _rsf.add_curve(points, degree)

    def fillet_curve(, curve_0, radius=None, point_0=None, point_1=None):

        return _rsf.add_fillet_curve(, curve_0, radius, point_0, point_1)

    def interp_crv_on_srf(, points):

        return _rsf.add_interp_crv_on_srf(, points)

    def interp_crv_on_srf_u_v(, points):

        return _rsf.add_interp_crv_on_srf_u_v(, points)

    def interp_curve(points, degree=None, knot_style=None, start_tan=None, end_tan=None):

        return _rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)

    def interp_curve_ex(points, degree=None, knot_style=None, sharp=None, start_tangent=None, end_tangent=None):

        return _rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)

    def sub_crv(, param_0, param_1):

        return _rsf.add_sub_crv(, param_0, param_1)

    def divide_curve_equidistant(, distance, create=None, points=None):

        return _rsf.divide_curve_equidistant(, distance, create, points)

