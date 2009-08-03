# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util

_rsf = None

class _CurveRootFunctionsModify(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def close_curve(self, tolerance=pythoncom.Empty):
        rhino_id = _rsf.close_curve(self.rhino_id, tolerance)
        if rhino_id:
            return True
        else:
            return False

    def seam(self, parameter):

        return _rsf.curve_seam(self.rhino_id, parameter)


    def extend_curve(self, type, side, objects):
        rhino_id = _rsf.extend_curve(self.rhino_id, type, side, objects)
        if rhino_id:
            return True
        else:
            return False

    def extend_curve_length(self, type, side, length):
        rhino_id = _rsf.extend_curve_length(self.rhino_id, type, side, length)
        if rhino_id:
            return True
        else:
            return False

    def extend_curve_point(self, side, point):
        rhino_id = _rsf.extend_curve_point(self.rhino_id, side, point)
        if rhino_id:
            return True
        else:
            return False

    def fair_curve(self, tolerance=pythoncom.Empty):

        return _rsf.fair_curve(self.rhino_id, tolerance)


    def fit_curve(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        rhino_id = _rsf.fit_curve(self.rhino_id, degree, tolerance, angle_tolerance)
        if rhino_id:
            return True
        else:
            return False

    def insert_curve_knot(self, parameter, symmetrical=pythoncom.Empty):

        return _rsf.insert_curve_knot(self.rhino_id, parameter, symmetrical)


    def make_curve_non_periodic(self):
        rhino_id = _rsf.make_curve_non_periodic(self.rhino_id, False)
        if rhino_id:
            return True
        else:
            return False

    def make_curve_periodic(self):
        rhino_id = _rsf.make_curve_periodic(self.rhino_id, False)
        if rhino_id:
            return True
        else:
            return False

    def rebuild_curve(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return _rsf.rebuild_curve(self.rhino_id, degree, point_count)


    def remove_curve_knot(self, parameter):

        return _rsf.remove_curve_knot(self.rhino_id, parameter)


    def reverse_curve(self):

        return _rsf.reverse_curve(self.rhino_id)


    def simplify_curve(self, flags=pythoncom.Empty):

        return _rsf.simplify_curve(self.rhino_id, flags)


    def trim_curve(self, interval, delete=pythoncom.Empty):
        rhino_id = _rsf.trim_curve(self.rhino_id, interval, delete)
        if rhino_id:
            return True
        else:
            return False
