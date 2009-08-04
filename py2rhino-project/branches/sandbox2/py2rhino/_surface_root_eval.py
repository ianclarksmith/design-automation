# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _SurfaceRootEval(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def evaluate(self, parameter):
        return _rsf.evaluate_surface(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        return _rsf.surface_evaluate(self._rhino_id, parameter, derivative)

    def evaluate_frame(self, parameter):
        return _rsf.surface_frame(self._rhino_id, parameter)
