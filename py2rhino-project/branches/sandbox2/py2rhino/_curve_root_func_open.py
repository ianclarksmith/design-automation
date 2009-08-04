# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._curve_root_func import _CurveRootFunc


_rsf = None


class _CurveRootFuncOpen(_CurveRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def close(self, tolerance=pythoncom.Empty):
        return _rsf.close_curve(self._rhino_id, tolerance)

    def extend(self, type, side, objects):
        return _rsf.extend_curve(self._rhino_id, type, side, objects)

    def extend_length(self, type, side, length):
        return _rsf.extend_curve_length(self._rhino_id, type, side, length)

    def extend_point(self, side, point):
        return _rsf.extend_curve_point(self._rhino_id, side, point)
