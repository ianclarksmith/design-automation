# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._curve_root_attributes import _CurveRootAttributes

_rsf = None

class _PolylineAttributes(_CurveRootAttributes):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def vertices(self):
        return _rsf.polyline_vertices(self.rhino_id, pythoncom.Empty)
