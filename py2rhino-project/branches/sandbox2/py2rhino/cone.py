# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Cone(p2r._SurfaceType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_cone(cls, base, plane, height, height, radius, cap=pythoncom.Empty):

        return p2r_f.add_cone(base, plane, height, height, radius, cap)


    def definition(self, ):

        return p2r_f.surface_cone(self.rhino_id)

