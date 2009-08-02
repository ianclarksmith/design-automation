# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._curve_root_attributes import _CurveRootAttributes

_rsf = None

class _CircleAttributes(_CurveRootAttributes):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def center_point(self, index=pythoncom.Empty):

        return _rsf.circle_center_point(self.rhino_id, index)


    def circumference(self, index=pythoncom.Empty):

        return _rsf.circle_circumference(self.rhino_id, index)


    def radius(self, index=pythoncom.Empty):

        return _rsf.circle_radius(self.rhino_id, index)

