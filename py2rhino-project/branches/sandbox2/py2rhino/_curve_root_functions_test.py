# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._object_root_functions_test import _ObjectRootFunctionsTest

_rsf = None

class _CurveRootFunctionsTest(_ObjectRootFunctionsTest):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def is_curve_closable(self, tolerance=pythoncom.Empty):

        return _rsf.is_curve_closable(self.rhino_id, tolerance)


    def is_curve_closed(self, index=pythoncom.Empty):

        return _rsf.is_curve_closed(self.rhino_id, index)


    def in_plane(self, plane=pythoncom.Empty):

        return _rsf.is_curve_in_plane(self.rhino_id, plane)


    def is_curve_linear(self, index=pythoncom.Empty):

        return _rsf.is_curve_linear(self.rhino_id, index)


    def is_curve_periodic(self, index=pythoncom.Empty):

        return _rsf.is_curve_periodic(self.rhino_id, index)


    def is_curve_planar(self, index=pythoncom.Empty):

        return _rsf.is_curve_planar(self.rhino_id, index)


    def is_curve_rational(self, index=pythoncom.Empty):

        return _rsf.is_curve_rational(self.rhino_id, index)


    def is_point_on_curve(self, point, index=pythoncom.Empty):

        return _rsf.is_point_on_curve(self.rhino_id, point, index)

