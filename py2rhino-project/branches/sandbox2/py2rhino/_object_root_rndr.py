# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _ObjectRootRndr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def add_mesh(self, quality=pythoncom.Empty, enable=pythoncom.Empty):
        return _rsf.add_object_mesh(self._rhino_id, quality, enable)

    def enable(self, enable=pythoncom.Empty):
        return _rsf.enable_object_mesh(self._rhino_id, enable)

    def has_mesh(self):
        return _rsf.object_has_mesh(self._rhino_id)

    def density(self, density=pythoncom.Empty):
        return _rsf.object_mesh_density(self._rhino_id, density)

    def max_angle(self, angle=pythoncom.Empty):
        return _rsf.object_mesh_max_angle(self._rhino_id, angle)

    def max_aspect_ratio(self, ratio=pythoncom.Empty):
        return _rsf.object_mesh_max_aspect_ratio(self._rhino_id, ratio)

    def max_dist_edge_to_srf(self, distance=pythoncom.Empty):
        return _rsf.object_mesh_max_dist_edge_to_srf(self._rhino_id, distance)

    def max_edge_length(self, length=pythoncom.Empty):
        return _rsf.object_mesh_max_edge_length(self._rhino_id, length)

    def min_edge_length(self, length=pythoncom.Empty):
        return _rsf.object_mesh_min_edge_length(self._rhino_id, length)

    def min_initial_grid_quads(self, quads=pythoncom.Empty):
        return _rsf.object_mesh_min_initial_grid_quads(self._rhino_id, quads)

    def quality(self, quality=pythoncom.Empty):
        return _rsf.object_mesh_quality(self._rhino_id, quality)

    def settings(self, settings=pythoncom.Empty):
        return _rsf.object_mesh_settings(self._rhino_id, settings)
