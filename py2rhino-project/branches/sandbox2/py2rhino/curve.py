# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Curve(p2r._CurveType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    def divide_curve_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):

        return p2r_f.divide_curve_equidistant(self.rhino_id, distance, create, points)

