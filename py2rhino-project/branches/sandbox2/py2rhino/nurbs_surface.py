# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._surface_root import _SurfaceRoot


_rsf = None
from py2rhino._object_root_defm import _ObjectRootDefm
from py2rhino._surface_root_eval import _SurfaceRootEval
from py2rhino._surface_root_func_oorc import _SurfaceRootFuncOorc
from py2rhino._surface_root_genr import _SurfaceRootGenr
from py2rhino._object_root_grps import _ObjectRootGrps
from py2rhino._surface_root_mdfy import _SurfaceRootMdfy
from py2rhino._object_root_mtrl import _ObjectRootMtrl
from py2rhino._object_root_prop import _ObjectRootProp
from py2rhino._object_root_rndr import _ObjectRootRndr
from py2rhino._object_root_stat import _ObjectRootStat
from py2rhino._surface_root_test import _SurfaceRootTest
from py2rhino._object_root_trfm import _ObjectRootTrfm
from py2rhino._object_root_util import _ObjectRootUtil


class NurbsSurface(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, NurbsSurface, _rsf )
        self.eval = _SurfaceRootEval(_rhino_id, NurbsSurface, _rsf )
        self.func = _SurfaceRootFuncOorc(_rhino_id, NurbsSurface, _rsf )
        self.genr = _SurfaceRootGenr(_rhino_id, NurbsSurface, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, NurbsSurface, _rsf )
        self.modf = _SurfaceRootMdfy(_rhino_id, NurbsSurface, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, NurbsSurface, _rsf )
        self.prop = _ObjectRootProp(_rhino_id, NurbsSurface, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, NurbsSurface, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, NurbsSurface, _rsf )
        self.test = _SurfaceRootTest(_rhino_id, NurbsSurface, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, NurbsSurface, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, NurbsSurface, _rsf )

    @classmethod
    def create_by_cut_plane(cls, objects, start_point, end_point, normal=pythoncom.Empty):

        _rhino_id = _rsf.add_cut_plane(map(lambda i: i._rhino_id, objects), start_point, end_point, normal)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_edge(cls, objects):

        _rhino_id = _rsf.add_edge_srf(map(lambda i: i._rhino_id, objects))

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_loft(cls, objects, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, type=pythoncom.Empty, style=pythoncom.Empty, value=pythoncom.Empty, closed=pythoncom.Empty):

        _rhino_id = _rsf.add_loft_srf(map(lambda i: i._rhino_id, objects), start_pt, end_pt, type, style, value, closed)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create(cls, point_count, points, knots_u, knots_v, degree, weights):

        _rhino_id = _rsf.add_nurbs_surface(point_count, points, knots_u, knots_v, degree, weights)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_planar_crv(cls, objects):

        _rhino_id = _rsf.add_planar_srf(map(lambda i: i._rhino_id, objects))


        return map(lambda i: NurbsSurface(i), _rhino_id)


    @classmethod
    def create_by_rail_rev(cls, profile, rail, axis):

        _rhino_id = _rsf.add_rail_rev_srf(profile._rhino_id, rail._rhino_id, axis)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_rev(cls, profile, axis, start_angle=pythoncom.Empty, end_angle=pythoncom.Empty):

        _rhino_id = _rsf.add_rev_srf(profile._rhino_id, axis, start_angle, end_angle)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_control_pt_grid(cls, count, points, degree=pythoncom.Empty):

        _rhino_id = _rsf.add_srf_control_pt_grid(count, points, degree)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_corner_pts(cls, points):

        _rhino_id = _rsf.add_srf_pt(points)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_pt_grid(cls, count, points, degree=pythoncom.Empty, closed=pythoncom.Empty):

        _rhino_id = _rsf.add_srf_pt_grid(count, points, degree, closed)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_sweep_1(cls, rail, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, style=pythoncom.Empty, style_arg=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):

        _rhino_id = _rsf.add_sweep_1(rail._rhino_id, map(lambda i: i._rhino_id, shapes), start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg)


        return map(lambda i: NurbsSurface(i), _rhino_id)


    @classmethod
    def create_by_sweep_2(cls, rails, shapes, start_pt=pythoncom.Empty, end_pt=pythoncom.Empty, closed=pythoncom.Empty, simple_sweep=pythoncom.Empty, maintain_height=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):

        _rhino_id = _rsf.add_sweep_2(map(lambda i: i._rhino_id, rails), map(lambda i: i._rhino_id, shapes), start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg)


        return map(lambda i: NurbsSurface(i), _rhino_id)


    @classmethod
    def create_by_extrude_crv(cls, curve, path):

        _rhino_id = _rsf.extrude_curve(curve._rhino_id, path)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_extrude_crv_point(cls, curve, point):

        _rhino_id = _rsf.extrude_curve_point(curve._rhino_id, point)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_extrude_crv_straight(cls, curve, start_point, end_point):

        _rhino_id = _rsf.extrude_curve_straight(curve._rhino_id, start_point, end_point)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_extrude_crv_tapered(cls, curve, distance, direction, base_point, angle, corner_type=pythoncom.Empty):

        _rhino_id = _rsf.extrude_curve_tapered(curve._rhino_id, distance, direction, base_point, angle, corner_type)


        return map(lambda i: NurbsSurface(i), _rhino_id)

