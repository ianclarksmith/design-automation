# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._object_root_test import _ObjectRootTest


_rsf = None


class _CurveRootTest(_ObjectRootTest):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_closable(self, tolerance=pythoncom.Empty):
        return _rsf.is_curve_closable(self._rhino_id, tolerance)

    def is_closed(self):
        return _rsf.is_curve_closed(self._rhino_id, pythoncom.Empty)

    def in_plane(self, plane=pythoncom.Empty):
        return _rsf.is_curve_in_plane(self._rhino_id, plane)

    def is_linear(self):
        return _rsf.is_curve_linear(self._rhino_id, pythoncom.Empty)

    def is_periodic(self):
        return _rsf.is_curve_periodic(self._rhino_id, pythoncom.Empty)

    def is_planar(self):
        return _rsf.is_curve_planar(self._rhino_id, pythoncom.Empty)

    def is_rational(self):
        return _rsf.is_curve_rational(self._rhino_id, pythoncom.Empty)

    def is_on_crv(self, point):
        return _rsf.is_point_on_curve(self._rhino_id, point, pythoncom.Empty)
