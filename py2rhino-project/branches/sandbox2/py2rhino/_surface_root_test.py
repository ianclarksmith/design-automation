# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._object_root_type import _ObjectRootType


_rsf = None


class _SurfaceRootTest(_ObjectRootType):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_brep(self):
        return _rsf.is_brep(self._rhino_id)

    def is_brep_manifold(self):
        return _rsf.is_brep_manifold(self._rhino_id)

    def is_parameter_on_srf(self, parameter):
        return _rsf.is_parameter_on_surface(self._rhino_id, parameter)

    def is_plane_surface(self):
        return _rsf.is_plane_surface(self._rhino_id)

    def is_point_in_srf(self, point):
        return _rsf.is_point_in_surface(self._rhino_id, point)

    def is_point_on_srf(self, point):
        return _rsf.is_point_on_surface(self._rhino_id, point)

    def is_poly_srf(self):
        return _rsf.is_poly_surface(self._rhino_id)

    def is_poly_surface_closed(self):
        return _rsf.is_poly_surface_closed(self._rhino_id)

    def is_poly_srf_planar(self):
        return _rsf.is_poly_surface_planar(self._rhino_id)

    def is_srf_closed(self, direction):
        return _rsf.is_surface_closed(self._rhino_id, direction)

    def is_srf_periodic(self, direction):
        return _rsf.is_surface_periodic(self._rhino_id, direction)

    def is_srf_planar(self, tolerance=pythoncom.Empty):
        return _rsf.is_surface_planar(self._rhino_id, tolerance)

    def is_srf_rational(self):
        return _rsf.is_surface_rational(self._rhino_id)

    def is_srf_singular(self, direction):
        return _rsf.is_surface_singular(self._rhino_id, direction)

    def is_srf_trimmed(self):
        return _rsf.is_surface_trimmed(self._rhino_id)
