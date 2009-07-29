# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Surface_and_Polysurface(p2r.object):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    def insert_surface_knot(self, parameter, direction, symmetrical=pythoncom.Empty):

        return p2r_f.insert_surface_knot(self.rhino_id, parameter, direction, symmetrical)


    def intersect_breps(self, brep_1, tolerance=pythoncom.Empty):

        return p2r_f.intersect_breps(self.rhino_id, brep_1, tolerance)

