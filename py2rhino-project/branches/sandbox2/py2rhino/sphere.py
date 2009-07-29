# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Sphere(p2r._SurfaceType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def (cls, center, plane, radius):

        return p2r_f.add_sphere(center, plane, radius)


    def surface_sphere(self, ):

        return p2r_f.surface_sphere(self.rhino_id)

