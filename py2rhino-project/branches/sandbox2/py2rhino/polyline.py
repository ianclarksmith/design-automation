# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Polyline(p2r._CurveType):


    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_polyline(cls, points):

        rhino_id = p2r_f.add_polyline(points)


        return cls(rhino_id)


    def mesh(self, ):

        return p2r_f.mesh_polyline(self.rhino_id)


    def vertices(self, index=pythoncom.Empty):

        return p2r_f.polyline_vertices(self.rhino_id, index)

