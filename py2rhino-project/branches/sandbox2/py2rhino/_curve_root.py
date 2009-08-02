# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._object_root import _ObjectRoot

_rsf = None

class _CurveRoot(_ObjectRoot):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    @classmethod
    def create_by_sub(cls, curve, param_0, param_1):

        rhino_id = _rsf.add_sub_crv(curve.rhino_id, param_0, param_1)


        return _CurveRoot(rhino_id)


    @classmethod
    def create_by_offset(cls, curve, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):

        rhino_id = _rsf.offset_curve(curve.rhino_id, direction, distance, normal, style)


        return map(lambda i: _CurveRoot(i), rhino_id)


    @classmethod
    def create_by_split(cls, curve, parameters, delete=pythoncom.Empty):

        rhino_id = _rsf.split_curve(curve.rhino_id, parameters, delete)


        return map(lambda i: _CurveRoot(i), rhino_id)

