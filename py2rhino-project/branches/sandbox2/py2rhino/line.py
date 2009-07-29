# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Line(p2r._CurveType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_line(cls, start, end):

        return p2r_f.add_line(start, end)

