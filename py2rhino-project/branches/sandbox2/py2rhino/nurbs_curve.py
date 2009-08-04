# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._curve_root import _CurveRoot


_rsf = None
from py2rhino._object_root_defm import _ObjectRootDefm
from py2rhino._curve_root_eval import _CurveRootEval
from py2rhino._curve_root_func_oorc import _CurveRootFuncOorc
from py2rhino._nurbs_curve_genr import _NurbsCurveGenr
from py2rhino._object_root_grps import _ObjectRootGrps
from py2rhino._curve_root_mdfy import _CurveRootMdfy
from py2rhino._object_root_mtrl import _ObjectRootMtrl
from py2rhino._object_root_prop import _ObjectRootProp
from py2rhino._object_root_rndr import _ObjectRootRndr
from py2rhino._object_root_stat import _ObjectRootStat
from py2rhino._curve_root_test import _CurveRootTest
from py2rhino._object_root_trfm import _ObjectRootTrfm
from py2rhino._object_root_util import _ObjectRootUtil


class NurbsCurve(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, NurbsCurve, _rsf )
        self.eval = _CurveRootEval(_rhino_id, NurbsCurve, _rsf )
        self.func = _CurveRootFuncOorc(_rhino_id, NurbsCurve, _rsf )
        self.genr = _NurbsCurveGenr(_rhino_id, NurbsCurve, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, NurbsCurve, _rsf )
        self.modf = _CurveRootMdfy(_rhino_id, NurbsCurve, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, NurbsCurve, _rsf )
        self.prop = _ObjectRootProp(_rhino_id, NurbsCurve, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, NurbsCurve, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, NurbsCurve, _rsf )
        self.test = _CurveRootTest(_rhino_id, NurbsCurve, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, NurbsCurve, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, NurbsCurve, _rsf )

    @classmethod
    def create_by_points(cls, points, degree=pythoncom.Empty):

        _rhino_id = _rsf.add_curve(points, degree)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv_on_srf(cls, surface, points):

        _rhino_id = _rsf.add_interp_crv_on_srf(surface._rhino_id, points)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv_on_srf_uv(cls, surface, points):

        _rhino_id = _rsf.add_interp_crv_on_srf_u_v(surface._rhino_id, points)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):

        _rhino_id = _rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_interp_crv_ex(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):

        _rhino_id = _rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create(cls, points, knots, degree, weights=pythoncom.Empty):

        _rhino_id = _rsf.add_nurbs_curve(points, knots, degree, weights)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_srf_contour(cls, surface, start_point, end_point, plane, interval=pythoncom.Empty):

        _rhino_id = _rsf.add_srf_contour_crvs(surface._rhino_id, start_point, end_point, plane, interval)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_section(cls, surface, plane):

        _rhino_id = _rsf.add_srf_section_crvs(surface._rhino_id, plane)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_edge(cls, surface, select=pythoncom.Empty):

        _rhino_id = _rsf.duplicate_edge_curves(surface._rhino_id, select)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_border(cls, surface):

        _rhino_id = _rsf.duplicate_surface_border(surface._rhino_id)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_iso_curve(cls, surface, parameter, dir):

        _rhino_id = _rsf.extract_iso_curve(surface._rhino_id, parameter, dir)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_projection_to_mesh(cls, curves, meshes, direction):

        _rhino_id = _rsf.project_curve_to_mesh(map(lambda i: i._rhino_id, curves), meshes, direction)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_projection_to_srf(cls, curve, surfaces, direction):

        _rhino_id = _rsf.project_curve_to_surface(curve._rhino_id, surfaces, direction)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_pull(cls, surface, curve, delete=pythoncom.Empty):

        _rhino_id = _rsf.pull_curve(surface._rhino_id, curve._rhino_id, delete)


        return map(lambda i: NurbsCurve(i), _rhino_id)


    @classmethod
    def create_by_srf_short_path(cls, surface, start, end):

        _rhino_id = _rsf.short_path(surface._rhino_id, start, end)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_srf_principal_curvature(cls, surface, point):

        _rhino_id = _rsf.surface_principal_curvature(surface._rhino_id, point)


        return map(lambda i: NurbsCurve(i), _rhino_id)

