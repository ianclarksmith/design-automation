# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._object_root import _ObjectRoot

_rsf = None

class _CurveRoot(_ObjectRoot):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    @classmethod
    def create_by_offset(cls, curve, direction, distance, normal=pythoncom.Empty, style=pythoncom.Empty):

        rhino_id = _rsf.offset_curve(curve.rhino_id, direction, distance, normal, style)


        return map(lambda i: _CurveRoot(i), rhino_id)

