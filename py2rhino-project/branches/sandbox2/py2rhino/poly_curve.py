# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino._curve_type import _CurveType
from exceptions import Exception

_rsf = None

class PolyCurve(_CurveType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id


    @classmethod
    def create_polycurve(cls, curves, delete=pythoncom.Empty):

        rhino_id = _rsf.join_curves(map(lambda i: i.rhino_id, curves), delete)


        return map(lambda i: PolyCurve(i), rhino_id)


    def count(self, index=pythoncom.Empty):

        return _rsf.poly_curve_count(self.rhino_id, index)

