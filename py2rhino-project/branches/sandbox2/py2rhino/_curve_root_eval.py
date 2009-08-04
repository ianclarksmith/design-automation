# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _CurveRootEval(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def curvature(self, parameter):
        return _rsf.curve_curvature(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        return _rsf.curve_evaluate(self._rhino_id, parameter, derivative)

    def frame(self, parameter):
        return _rsf.curve_frame(self._rhino_id, parameter)

    def perp_frame(self, parameter):
        return _rsf.curve_perp_frame(self._rhino_id, parameter)

    def tangent(self, parameter):
        return _rsf.curve_tangent(self._rhino_id, parameter, pythoncom.Empty)

    def evaluate(self, parameter):
        return _rsf.evaluate_curve(self._rhino_id, parameter, pythoncom.Empty)
