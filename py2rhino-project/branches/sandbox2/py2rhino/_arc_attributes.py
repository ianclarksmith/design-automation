# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._curve_root_attributes import _CurveRootAttributes

_rsf = None

class _ArcAttributes(_CurveRootAttributes):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def angle(self, index=pythoncom.Empty):

        return _rsf.arc_angle(self.rhino_id, index)


    def center_point(self, index=pythoncom.Empty):

        return _rsf.arc_center_point(self.rhino_id, index)


    def mid_point(self, index=pythoncom.Empty):

        return _rsf.arc_mid_point(self.rhino_id, index)


    def radius(self, index=pythoncom.Empty):

        return _rsf.arc_radius(self.rhino_id, index)

