# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._surface_root_func import _SurfaceRootFunc


_rsf = None


class _SurfaceRootFuncClsd(_SurfaceRootFunc):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def boolean_difference(self, input_1, delete=pythoncom.Empty):

        return map(lambda i: p2r._SurfaceRoot(i), self._rhino_id)


    def boolean_intersection(self, input_1, delete=pythoncom.Empty):

        return map(lambda i: p2r._SurfaceRoot(i), self._rhino_id)


    def boolean_union(self, input, delete=pythoncom.Empty):

        return map(lambda i: p2r._SurfaceRoot(i), self._rhino_id)


    def brep_closest_point(self, point):
        return _rsf.brep_closest_point(self._rhino_id, point)

    def intersect_breps(self, brep_1, tolerance=pythoncom.Empty):

        return map(lambda i: p2r._SurfaceRoot(i), self._rhino_id)


    def split_brep(self, cutter, delete=pythoncom.Empty):

        return map(lambda i: p2r._SurfaceRoot(i), self._rhino_id)


    def volume(self):
        return _rsf.surface_volume(self._rhino_id)

    def volume_centroid(self):
        return _rsf.surface_volume_centroid(self._rhino_id)

    def volume_moments(self):
        return _rsf.surface_volume_moments(self._rhino_id)
