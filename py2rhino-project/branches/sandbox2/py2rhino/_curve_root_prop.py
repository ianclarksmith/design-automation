# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _CurveRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def arrows(self, style=pythoncom.Empty):
        return _rsf.curve_arrows(self._rhino_id, style)

    def degree(self):
        return _rsf.curve_degree(self._rhino_id, pythoncom.Empty)

    def dim(self):
        return _rsf.curve_dim(self._rhino_id, pythoncom.Empty)

    def discontinuity(self, style):
        return _rsf.curve_discontinuity(self._rhino_id, style)

    def domain(self):

        return map(lambda i: p2r._CurveRoot(i), self._rhino_id)


    def edit_points(self, return_parameters=pythoncom.Empty):
        return _rsf.curve_edit_points(self._rhino_id, return_parameters, pythoncom.Empty)

    def end_point(self):
        return _rsf.curve_end_point(self._rhino_id, pythoncom.Empty)

    def knot_count(self):
        return _rsf.curve_knot_count(self._rhino_id, pythoncom.Empty)

    def knots(self):
        return _rsf.curve_knots(self._rhino_id, pythoncom.Empty)

    def length(self, sub_domain=pythoncom.Empty):
        return _rsf.curve_length(self._rhino_id, pythoncom.Empty, sub_domain)

    def mid_point(self):
        return _rsf.curve_mid_point(self._rhino_id)

    def normal(self):
        return _rsf.curve_normal(self._rhino_id)

    def plane(self):
        return _rsf.curve_plane(self._rhino_id)

    def control_point_count(self):
        return _rsf.curve_point_count(self._rhino_id, pythoncom.Empty)

    def control_points(self):
        return _rsf.curve_points(self._rhino_id, pythoncom.Empty)

    def start_point(self):
        return _rsf.curve_start_point(self._rhino_id, pythoncom.Empty)

    def weights(self):
        return _rsf.curve_weights(self._rhino_id, pythoncom.Empty)
