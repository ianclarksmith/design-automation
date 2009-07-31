# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino._curve_type import _CurveType
from exceptions import Exception

_rsf = None

class Arc(_CurveType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_arc(cls, plane, radius, angle):

        rhino_id = _rsf.add_arc(plane, radius, angle)


        return Arc(rhino_id)


    @classmethod
    def create_arc_3pt(cls, start, end, point):

        rhino_id = _rsf.add_arc_3_pt(start, end, point)


        return Arc(rhino_id)


    def angle(self, index=pythoncom.Empty):

        return _rsf.arc_angle(self.rhino_id, index)


    def center_point(self, index=pythoncom.Empty):

        return _rsf.arc_center_point(self.rhino_id, index)


    def mid_point(self, index=pythoncom.Empty):

        return _rsf.arc_mid_point(self.rhino_id, index)


    def radius(self, index=pythoncom.Empty):

        return _rsf.arc_radius(self.rhino_id, index)

