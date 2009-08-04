# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._curve_root_genr import _CurveRootGenr


_rsf = None


class _PolylineGenr(_CurveRootGenr):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def sub(self, param_0, param_1):
        _rhino_id = _rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.Polyline(_rhino_id)
        else:
            return None

    def offset(self, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):

        return map(lambda i: p2r.Polyline(i), self._rhino_id)


    def split(self, parameters, delete=pythoncom.Empty):

        return map(lambda i: p2r.Polyline(i), self._rhino_id)


    def trim(self, interval, delete=pythoncom.Empty):
        _rhino_id = _rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.Polyline(_rhino_id)
        else:
            return None
