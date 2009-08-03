# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._object_root_functions_type import _ObjectRootFunctionsType


_rsf = None


class _CurveRootFunctionsType(_ObjectRootFunctionsType):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_arc(self):
        return _rsf.is_arc(self.rhino_id, pythoncom.Empty)

    def is_circle(self):
        return _rsf.is_circle(self.rhino_id, pythoncom.Empty)

    def is_curve(self):
        return _rsf.is_curve(self.rhino_id, pythoncom.Empty)

    def is_ellipse(self):
        return _rsf.is_ellipse(self.rhino_id)

    def is_line(self):
        return _rsf.is_line(self.rhino_id, pythoncom.Empty)

    def is_poly_curve(self):
        return _rsf.is_poly_curve(self.rhino_id, pythoncom.Empty)

    def is_polyline(self):
        return _rsf.is_polyline(self.rhino_id, pythoncom.Empty)
