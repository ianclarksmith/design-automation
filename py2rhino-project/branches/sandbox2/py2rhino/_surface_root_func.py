# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _SurfaceRootFunc(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def cap_planar_holes(self):
        return _rsf.cap_planar_holes(self._rhino_id)

    def closest_point(self, point):
        return _rsf.surface_closest_point(self._rhino_id, point)
