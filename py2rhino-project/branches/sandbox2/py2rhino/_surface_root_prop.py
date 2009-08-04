# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _SurfaceRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def area(self):
        return _rsf.surface_area(self._rhino_id)

    def area_centroid(self):
        return _rsf.surface_area_centroid(self._rhino_id)

    def area_moments(self):
        return _rsf.surface_area_moments(self._rhino_id)

    def contour_points(self, start_point, end_point, interval=pythoncom.Empty, angle=pythoncom.Empty):
        return _rsf.surface_contour_points(self._rhino_id, start_point, end_point, interval, angle)

    def curvature(self, parameter):
        return _rsf.surface_curvature(self._rhino_id, parameter)

    def curvature_analysis(self):
        return _rsf.surface_curvature_analysis(self._rhino_id)

    def degree(self, direction=pythoncom.Empty):
        return _rsf.surface_degree(self._rhino_id, direction)

    def domain(self, direction):
        return _rsf.surface_domain(self._rhino_id, direction)

    def edit_points(self, return_parameters=pythoncom.Empty, return_all=pythoncom.Empty):
        return _rsf.surface_edit_points(self._rhino_id, return_parameters, return_all)

    def isocurve_density(self, density=pythoncom.Empty):
        return _rsf.surface_isocurve_density(self._rhino_id, density)

    def knot_count(self):
        return _rsf.surface_knot_count(self._rhino_id)

    def knots(self):
        return _rsf.surface_knots(self._rhino_id)

    def normal(self, parameter):
        return _rsf.surface_normal(self._rhino_id, parameter)

    def point_count(self):
        return _rsf.surface_point_count(self._rhino_id)

    def points(self, return_all=pythoncom.Empty):
        return _rsf.surface_points(self._rhino_id, return_all)

    def weights(self):
        return _rsf.surface_weights(self._rhino_id)
