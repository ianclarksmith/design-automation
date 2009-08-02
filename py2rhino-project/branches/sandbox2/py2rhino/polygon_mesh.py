# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._mesh_root import _MeshRoot

_rsf = None

class PolygonMesh(_MeshRoot):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    def create_mesh_from_closed_polyline(self, polyline):

        return _rsf.mesh_polyline(polyline.rhino_id)

