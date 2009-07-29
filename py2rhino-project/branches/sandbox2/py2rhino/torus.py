# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Torus(p2r._SurfaceType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def (cls, base, plane, major_radius, minor_radius, direction=pythoncom.Empty):

        return p2r_f.add_torus(trouble, plane, major_radius, minor_radius, direction)


    def surface_torus(self, ):

        return p2r_f.surface_torus(self.rhino_id)

