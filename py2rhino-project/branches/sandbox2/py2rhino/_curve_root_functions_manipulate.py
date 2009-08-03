# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util


_rsf = None


class _CurveRootFunctionsManipulate(object):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def curve_arc_length_point(self, length, from_start=pythoncom.Empty):
        return _rsf.curve_arc_length_point(self.rhino_id, length, from_start)

    def closest_point(self, point):
        return _rsf.curve_closest_point(self.rhino_id, point, pythoncom.Empty)

    def contour_points(self, start_point, end_point, interval=pythoncom.Empty):
        return _rsf.curve_contour_points(self.rhino_id, start_point, end_point, interval)

    def deviation(self, curve_a):
        return _rsf.curve_deviation(self.rhino_id, curve_a)

    def directions_match(self, curve_1):
        return _rsf.curve_directions_match(self.rhino_id, curve_1)

    def radius(self, point):
        return _rsf.curve_radius(self.rhino_id, point, pythoncom.Empty)

    def divide_curve(self, segments, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve(self.rhino_id, segments, create, points)

    def divide_curve_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve_equidistant(self.rhino_id, distance, create, points)

    def divide_curve_length(self, length, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve_length(self.rhino_id, length, create, points)

    def line_fit_from_points(self):
        return _rsf.line_fit_from_points(self.rhino_id)
