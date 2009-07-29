# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Cylinder(p2r._SurfaceType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def (cls, base, plane, height, height, radius, cap=pythoncom.Empty):

        return p2r_f.add_cylinder(base, plane, height, height, radius, cap)


    def surface_cylinder(self, ):

        return p2r_f.surface_cylinder(self.rhino_id)

