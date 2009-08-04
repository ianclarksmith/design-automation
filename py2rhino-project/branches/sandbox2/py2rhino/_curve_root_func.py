# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _CurveRootFunc(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def crv_arc_length_point(self, length, from_start=pythoncom.Empty):
        return _rsf.curve_arc_length_point(self._rhino_id, length, from_start)

    def closest_point(self, point):
        return _rsf.curve_closest_point(self._rhino_id, point, pythoncom.Empty)

    def contour_points(self, start_point, end_point, interval=pythoncom.Empty):
        return _rsf.curve_contour_points(self._rhino_id, start_point, end_point, interval)

    def crv_intersection(self, curve=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.curve_curve_intersection(self._rhino_id, curve, tolerance)

    def deviation(self, curve_a):
        return _rsf.curve_deviation(self._rhino_id, curve_a)

    def directions_match(self, curve_1):
        return _rsf.curve_directions_match(self._rhino_id, curve_1)

    def radius(self, point):
        return _rsf.curve_radius(self._rhino_id, point, pythoncom.Empty)

    def srf_intersection(self, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        return _rsf.curve_surface_intersection(self._rhino_id, surface, tolerance, angle_tolerance)

    def divide_crv(self, segments, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve(self._rhino_id, segments, create, points)

    def divide_crv_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve_equidistant(self._rhino_id, distance, create, points)

    def divide_crv_length(self, length, create=pythoncom.Empty, points=pythoncom.Empty):
        return _rsf.divide_curve_length(self._rhino_id, length, create, points)

    def line_fit_from_points(self):
        return _rsf.line_fit_from_points(self._rhino_id)

    def planar_crv_collision(self, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.planar_curve_collision(self._rhino_id, curve, plane, tolerance)
