# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _SurfaceRootMdfy(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def flip(self, flip=pythoncom.Empty):

        return _rsf.flip_surface(self._rhino_id, flip)


    def insert_knot(self, parameter, direction, symmetrical=pythoncom.Empty):

        return _rsf.insert_surface_knot(self._rhino_id, parameter, direction, symmetrical)


    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return _rsf.rebuild_surface(self._rhino_id, degree, point_count)


    def remove_knot(self, parameter, direction):

        return _rsf.remove_surface_knot(self._rhino_id, parameter, direction)


    def reverse(self, direction):

        return _rsf.reverse_surface(self._rhino_id, direction)


    def shrink_trimmed(self):

        return _rsf.shrink_trimmed_surface(self._rhino_id)


    def seam(self, direction, parameter):

        return _rsf.surface_seam(self._rhino_id, direction, parameter)

