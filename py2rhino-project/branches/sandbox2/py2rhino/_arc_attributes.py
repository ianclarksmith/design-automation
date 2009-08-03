# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._curve_root_attributes import _CurveRootAttributes


_rsf = None


class _ArcAttributes(_CurveRootAttributes):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def angle(self):
        return _rsf.arc_angle(self.rhino_id, pythoncom.Empty)

    def center_point(self):
        return _rsf.arc_center_point(self.rhino_id, pythoncom.Empty)

    def mid_point(self):
        return _rsf.arc_mid_point(self.rhino_id, pythoncom.Empty)

    def radius(self):
        return _rsf.arc_radius(self.rhino_id, pythoncom.Empty)
