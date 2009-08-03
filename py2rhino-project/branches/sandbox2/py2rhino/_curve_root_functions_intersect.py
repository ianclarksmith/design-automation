# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util


_rsf = None


class _CurveRootFunctionsIntersect(object):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def brep_intersection(self, brep, tolerance=pythoncom.Empty):

        return map(lambda i: _CurveRoot(i), rhino_id)


    def curve_intersection(self, curve=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.curve_curve_intersection(self.rhino_id, curve, tolerance)

    def surface_intersection(self, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        return _rsf.curve_surface_intersection(self.rhino_id, surface, tolerance, angle_tolerance)
