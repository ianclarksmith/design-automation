# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._curve_root_prop import _CurveRootProp


_rsf = None


class _CircleProp(_CurveRootProp):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def center_point(self):
        return _rsf.circle_center_point(self._rhino_id, pythoncom.Empty)

    def circumference(self):
        return _rsf.circle_circumference(self._rhino_id, pythoncom.Empty)

    def radius(self):
        return _rsf.circle_radius(self._rhino_id, pythoncom.Empty)
