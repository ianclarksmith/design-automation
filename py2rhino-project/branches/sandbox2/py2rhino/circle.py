# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino._curve_type import _CurveType
from exceptions import Exception

_rsf = None

class Circle(_CurveType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_circle(cls, plane, radius):

        rhino_id = _rsf.add_circle(plane, radius)


        return Circle(rhino_id)


    @classmethod
    def create_circle_3pt(cls, first, second, third):

        rhino_id = _rsf.add_circle_3_pt(first, second, third)


        return Circle(rhino_id)


    def center_point(self, index=pythoncom.Empty):

        return _rsf.circle_center_point(self.rhino_id, index)


    def circumference(self, index=pythoncom.Empty):

        return _rsf.circle_circumference(self.rhino_id, index)


    def radius(self, index=pythoncom.Empty):

        return _rsf.circle_radius(self.rhino_id, index)

