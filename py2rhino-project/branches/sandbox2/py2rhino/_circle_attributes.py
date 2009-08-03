# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._curve_root_attributes import _CurveRootAttributes

_rsf = None

class _CircleAttributes(_CurveRootAttributes):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def center_point(self):
        return _rsf.circle_center_point(self.rhino_id, pythoncom.Empty)

    def circumference(self):
        return _rsf.circle_circumference(self.rhino_id, pythoncom.Empty)

    def radius(self):
        return _rsf.circle_radius(self.rhino_id, pythoncom.Empty)
