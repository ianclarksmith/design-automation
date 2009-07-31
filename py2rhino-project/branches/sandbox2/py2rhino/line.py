# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino._curve_type import _CurveType
from exceptions import Exception

_rsf = None

class Line(_CurveType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_line(cls, start, end):

        rhino_id = _rsf.add_line(start, end)


        return Line(rhino_id)

