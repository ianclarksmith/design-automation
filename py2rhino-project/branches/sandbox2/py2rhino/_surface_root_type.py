# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._object_root_test import _ObjectRootTest


_rsf = None


class _SurfaceRootType(_ObjectRootTest):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_cone(self):
        return _rsf.is_cone(self._rhino_id)

    def is_cylinder(self):
        return _rsf.is_cylinder(self._rhino_id)

    def is_sphere(self):
        return _rsf.is_sphere(self._rhino_id)

    def is_surface(self):
        return _rsf.is_surface(self._rhino_id)

    def is_torus(self):
        return _rsf.is_torus(self._rhino_id)
