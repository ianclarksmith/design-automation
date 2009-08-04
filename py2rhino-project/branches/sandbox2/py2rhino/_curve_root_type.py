# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._object_root_type import _ObjectRootType


_rsf = None


class _CurveRootType(_ObjectRootType):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_arc(self):
        return _rsf.is_arc(self._rhino_id, pythoncom.Empty)

    def is_circle(self):
        return _rsf.is_circle(self._rhino_id, pythoncom.Empty)

    def is_crv(self):
        return _rsf.is_curve(self._rhino_id, pythoncom.Empty)

    def is_ellipse(self):
        return _rsf.is_ellipse(self._rhino_id)

    def is_line(self):
        return _rsf.is_line(self._rhino_id, pythoncom.Empty)

    def is_poly_crv(self):
        return _rsf.is_poly_curve(self._rhino_id, pythoncom.Empty)

    def is_polyline(self):
        return _rsf.is_polyline(self._rhino_id, pythoncom.Empty)
