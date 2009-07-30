# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Arc(p2r._CurveType):


    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_arc(cls, plane, radius, angle):

        rhino_id = p2r_f.add_arc(plane, radius, angle)


        return cls(rhino_id)


    @classmethod
    def create_arc_3pt(cls, start, end, point):

        rhino_id = p2r_f.add_arc_3_pt(start, end, point)


        return cls(rhino_id)


    def angle(self, index=pythoncom.Empty):

        return p2r_f.arc_angle(self.rhino_id, index)


    def center_point(self, index=pythoncom.Empty):

        return p2r_f.arc_center_point(self.rhino_id, index)


    def mid_point(self, index=pythoncom.Empty):

        return p2r_f.arc_mid_point(self.rhino_id, index)


    def radius(self, index=pythoncom.Empty):

        return p2r_f.arc_radius(self.rhino_id, index)

