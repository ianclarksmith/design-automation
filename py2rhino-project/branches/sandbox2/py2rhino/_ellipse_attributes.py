# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._curve_root_attributes import _CurveRootAttributes

_rsf = None

class _EllipseAttributes(_CurveRootAttributes):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def center_point(self, ):

        return _rsf.ellipse_center_point(self.rhino_id)


    def quad_points(self, ):

        return _rsf.ellipse_quad_points(self.rhino_id)

