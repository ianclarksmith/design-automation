# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino._curve_type import _CurveType
from exceptions import Exception

_rsf = None

class NurbsCurve(_CurveType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_curve_by_points(cls, points, degree=pythoncom.Empty):

        rhino_id = _rsf.add_curve(points, degree)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_fillet_curve(cls, curve_0, curve_1, radius=pythoncom.Empty, point_0=pythoncom.Empty, point_1=pythoncom.Empty):

        rhino_id = _rsf.add_fillet_curve(curve_0.rhino_id, curve_1.rhino_id, radius, point_0, point_1)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve_on_srf(cls, surface, points):

        rhino_id = _rsf.add_interp_crv_on_srf(surface.rhino_id, points)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve_on_srf_uv(cls, surface, points):

        rhino_id = _rsf.add_interp_crv_on_srf_u_v(surface.rhino_id, points)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):

        rhino_id = _rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve_ex(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):

        rhino_id = _rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_curve(cls, points, knots, degree, weights=pythoncom.Empty):

        rhino_id = _rsf.add_nurbs_curve(points, knots, degree, weights)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_sub_curve(cls, curve, param_0, param_1):

        rhino_id = _rsf.add_sub_crv(curve.rhino_id, param_0, param_1)


        return NurbsCurve(rhino_id)

