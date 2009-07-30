# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Circle(p2r._CurveType):


    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_circle(cls, plane, radius):

        rhino_id = p2r_f.add_circle(plane, radius)


        return cls(rhino_id)


    @classmethod
    def create_circle_3pt(cls, first, second, third):

        rhino_id = p2r_f.add_circle_3_pt(first, second, third)


        return cls(rhino_id)


    def center_point(self, index=pythoncom.Empty):

        return p2r_f.circle_center_point(self.rhino_id, index)


    def circumference(self, index=pythoncom.Empty):

        return p2r_f.circle_circumference(self.rhino_id, index)


    def radius(self, index=pythoncom.Empty):

        return p2r_f.circle_radius(self.rhino_id, index)

