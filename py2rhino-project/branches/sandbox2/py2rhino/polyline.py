# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino._curve_type import _CurveType
from exceptions import Exception

_rsf = None

class Polyline(_CurveType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_polyline(cls, points):

        rhino_id = _rsf.add_polyline(points)


        return Polyline(rhino_id)


    def mesh(self, ):

        return _rsf.mesh_polyline(self.rhino_id)


    def vertices(self, index=pythoncom.Empty):

        return _rsf.polyline_vertices(self.rhino_id, index)

