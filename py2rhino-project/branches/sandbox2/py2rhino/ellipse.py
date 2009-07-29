# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Ellipse(p2r._CurveType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_ellipse(cls, plane, x_radius, y_radius):

        return p2r_f.add_ellipse(plane, x_radius, y_radius)


    @classmethod
    def create_ellipse_3pt(cls, center, second, third):

        return p2r_f.add_ellipse_3_pt(center, second, third)


    def center_point(self, ):

        return p2r_f.ellipse_center_point(self.rhino_id)


    def quad_points(self, ):

        return p2r_f.ellipse_quad_points(self.rhino_id)

