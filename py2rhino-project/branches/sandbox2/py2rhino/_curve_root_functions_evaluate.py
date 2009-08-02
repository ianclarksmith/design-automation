# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _CurveRootFunctionsEvaluate(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def curvature(self, parameter):

        return _rsf.curve_curvature(self.rhino_id, parameter)


    def evaluate_derivatives(self, parameter, derivative):

        return _rsf.curve_evaluate(self.rhino_id, parameter, derivative)


    def frame(self, parameter):

        return _rsf.curve_frame(self.rhino_id, parameter)


    def perp_frame(self, parameter):

        return _rsf.curve_perp_frame(self.rhino_id, parameter)


    def tangent(self, parameter, index=pythoncom.Empty):

        return _rsf.curve_tangent(self.rhino_id, parameter, index)


    def evaluate(self, parameter, index=pythoncom.Empty):

        return _rsf.evaluate_curve(self.rhino_id, parameter, index)

