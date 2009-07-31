# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino._curve_type import _CurveType
from exceptions import Exception

_rsf = None

class Ellipse(_CurveType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_ellipse(cls, plane, x_radius, y_radius):

        rhino_id = _rsf.add_ellipse(plane, x_radius, y_radius)


        return Ellipse(rhino_id)


    @classmethod
    def create_ellipse_3pt(cls, center, second, third):

        rhino_id = _rsf.add_ellipse_3_pt(center, second, third)


        return Ellipse(rhino_id)


    def center_point(self, ):

        return _rsf.ellipse_center_point(self.rhino_id)


    def quad_points(self, ):

        return _rsf.ellipse_quad_points(self.rhino_id)

