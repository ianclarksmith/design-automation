# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Polysurface(p2r._SurfaceType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def (cls, corners):

        return p2r_f.add_box(corners)


    def explode_polysurfaces(self, objects, delete=pythoncom.Empty):

        return p2r_f.explode_polysurfaces(trouble, delete)

