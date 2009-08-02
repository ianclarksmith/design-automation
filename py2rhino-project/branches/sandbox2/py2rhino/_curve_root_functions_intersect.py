# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _CurveRootFunctionsIntersect(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def brep_intersection(self, brep, tolerance=pythoncom.Empty):

        return _rsf.curve_brep_intersect(self.rhino_id, brep, tolerance)


    def curve_intersection(self, curve=pythoncom.Empty, tolerance=pythoncom.Empty):

        return _rsf.curve_curve_intersection(self.rhino_id, curve, tolerance)


    def surface_intersection(self, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):

        return _rsf.curve_surface_intersection(self.rhino_id, surface, tolerance, angle_tolerance)

