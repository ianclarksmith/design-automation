# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util

_rsf = None

class _ObjectRootFunctionsRender(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def add_mesh(self, quality=pythoncom.Empty, enable=pythoncom.Empty):
        return _rsf.add_object_mesh(self.rhino_id, quality, enable)

    def enable(self, enable=pythoncom.Empty):
        return _rsf.enable_object_mesh(self.rhino_id, enable)

    def has_mesh(self):
        return _rsf.object_has_mesh(self.rhino_id)

    def density(self, density=pythoncom.Empty):
        return _rsf.object_mesh_density(self.rhino_id, density)

    def max_angle(self, angle=pythoncom.Empty):
        return _rsf.object_mesh_max_angle(self.rhino_id, angle)

    def max_aspect_ratio(self, ratio=pythoncom.Empty):
        return _rsf.object_mesh_max_aspect_ratio(self.rhino_id, ratio)

    def max_dist_edge_to_srf(self, distance=pythoncom.Empty):
        return _rsf.object_mesh_max_dist_edge_to_srf(self.rhino_id, distance)

    def max_edge_length(self, length=pythoncom.Empty):
        return _rsf.object_mesh_max_edge_length(self.rhino_id, length)

    def min_edge_length(self, length=pythoncom.Empty):
        return _rsf.object_mesh_min_edge_length(self.rhino_id, length)

    def min_initial_grid_quads(self, quads=pythoncom.Empty):
        return _rsf.object_mesh_min_initial_grid_quads(self.rhino_id, quads)

    def quality(self, quality=pythoncom.Empty):
        return _rsf.object_mesh_quality(self.rhino_id, quality)

    def settings(self, settings=pythoncom.Empty):
        return _rsf.object_mesh_settings(self.rhino_id, settings)
