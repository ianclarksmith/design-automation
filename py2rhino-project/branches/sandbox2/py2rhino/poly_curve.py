# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class PolyCurve(p2r._CurveType):


    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_polycurve(cls, curves, delete=pythoncom.Empty):

        rhino_id = p2r_f.join_curves(map(lambda i: i.rhino_id, curves), delete)


        return map(lambda i: cls(i), rhino_id)


    def count(self, index=pythoncom.Empty):

        return p2r_f.poly_curve_count(self.rhino_id, index)

