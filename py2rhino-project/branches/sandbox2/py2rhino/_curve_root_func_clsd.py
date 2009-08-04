# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._curve_root_func import _CurveRootFunc


_rsf = None


class _CurveRootFuncClsd(_CurveRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def area(self, ):
        return _rsf.curve_area(map(lambda i: i._rhino_id, ))

    def crv_area_centroid(self, objects):
        return _rsf.curve_area_centroid(map(lambda i: i._rhino_id, objects))

    def boolean_difference(self, curve):

        return map(lambda i: p2r._CurveRoot(i), self._rhino_id)


    def boolean_intersection(self, curve_a):

        return map(lambda i: p2r._CurveRoot(i), self._rhino_id)


    def boolean_union(self, curves):

        return map(lambda i: p2r._CurveRoot(i), self._rhino_id)


    def planar_closed_crv_containment(self, curve__1, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.planar_closed_curve_containment(self._rhino_id, curve__1, plane, tolerance)

    def point_in_planar_closed_crv(self, point, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.point_in_planar_closed_curve(point, curve, plane, tolerance)
