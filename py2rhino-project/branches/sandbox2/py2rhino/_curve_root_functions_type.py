# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._object_root_functions_type import _ObjectRootFunctionsType

_rsf = None

class _CurveRootFunctionsType(_ObjectRootFunctionsType):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def is_arc(self, index=pythoncom.Empty):

        return _rsf.is_arc(self.rhino_id, index)


    def is_circle(self, index=pythoncom.Empty):

        return _rsf.is_circle(self.rhino_id, index)


    def is_curve(self, index=pythoncom.Empty):

        return _rsf.is_curve(self.rhino_id, index)


    def is_ellipse(self, ):

        return _rsf.is_ellipse(self.rhino_id)


    def is_line(self, index=pythoncom.Empty):

        return _rsf.is_line(self.rhino_id, index)


    def is_poly_curve(self, index=pythoncom.Empty):

        return _rsf.is_poly_curve(self.rhino_id, index)


    def is_polyline(self, index=pythoncom.Empty):

        return _rsf.is_polyline(self.rhino_id, index)

