# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util

_rsf = None

class _CurveRootAttributes(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def arrows(self, style=pythoncom.Empty):
        return _rsf.curve_arrows(self.rhino_id, style)

    def degree(self):
        return _rsf.curve_degree(self.rhino_id, pythoncom.Empty)

    def dim(self):
        return _rsf.curve_dim(self.rhino_id, pythoncom.Empty)

    def discontinuity(self, style):
        return _rsf.curve_discontinuity(self.rhino_id, style)

    def domain(self):

        return map(lambda i: _CurveRoot(i), rhino_id)


    def edit_points(self, return_parameters=pythoncom.Empty):
        return _rsf.curve_edit_points(self.rhino_id, return_parameters, pythoncom.Empty)

    def end_point(self):
        return _rsf.curve_end_point(self.rhino_id, pythoncom.Empty)

    def knot_count(self):
        return _rsf.curve_knot_count(self.rhino_id, pythoncom.Empty)

    def knots(self):
        return _rsf.curve_knots(self.rhino_id, pythoncom.Empty)

    def length(self, sub_domain=pythoncom.Empty):
        return _rsf.curve_length(self.rhino_id, pythoncom.Empty, sub_domain)

    def mid_point(self):
        return _rsf.curve_mid_point(self.rhino_id)

    def normal(self):
        return _rsf.curve_normal(self.rhino_id)

    def plane(self):
        return _rsf.curve_plane(self.rhino_id)

    def control_point_count(self):
        return _rsf.curve_point_count(self.rhino_id, pythoncom.Empty)

    def control_points(self):
        return _rsf.curve_points(self.rhino_id, pythoncom.Empty)

    def start_point(self):
        return _rsf.curve_start_point(self.rhino_id, pythoncom.Empty)

    def weights(self):
        return _rsf.curve_weights(self.rhino_id, pythoncom.Empty)