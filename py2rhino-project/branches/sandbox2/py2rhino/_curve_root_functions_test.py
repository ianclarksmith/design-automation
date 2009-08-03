# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._object_root_functions_test import _ObjectRootFunctionsTest


_rsf = None


class _CurveRootFunctionsTest(_ObjectRootFunctionsTest):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_curve_closable(self, tolerance=pythoncom.Empty):
        return _rsf.is_curve_closable(self.rhino_id, tolerance)

    def is_curve_closed(self):
        return _rsf.is_curve_closed(self.rhino_id, pythoncom.Empty)

    def in_plane(self, plane=pythoncom.Empty):
        return _rsf.is_curve_in_plane(self.rhino_id, plane)

    def is_curve_linear(self):
        return _rsf.is_curve_linear(self.rhino_id, pythoncom.Empty)

    def is_curve_periodic(self):
        return _rsf.is_curve_periodic(self.rhino_id, pythoncom.Empty)

    def is_curve_planar(self):
        return _rsf.is_curve_planar(self.rhino_id, pythoncom.Empty)

    def is_curve_rational(self):
        return _rsf.is_curve_rational(self.rhino_id, pythoncom.Empty)

    def is_point_on_curve(self, point):
        return _rsf.is_point_on_curve(self.rhino_id, point, pythoncom.Empty)
