# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _CurveRootAttributes(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def arrows(self, style=pythoncom.Empty):

        return _rsf.curve_arrows(self.rhino_id, style)


    def degree(self, index=pythoncom.Empty):

        return _rsf.curve_degree(self.rhino_id, index)


    def dim(self, index=pythoncom.Empty):

        return _rsf.curve_dim(self.rhino_id, index)


    def discontinuity(self, style):

        return _rsf.curve_discontinuity(self.rhino_id, style)


    def domain(self, index=pythoncom.Empty):

        return _rsf.curve_domain(self.rhino_id, index)


    def edit_points(self, return_parameters=pythoncom.Empty, index=pythoncom.Empty):

        return _rsf.curve_edit_points(self.rhino_id, return_parameters, index)


    def end_point(self, index=pythoncom.Empty):

        return _rsf.curve_end_point(self.rhino_id, index)


    def knot_count(self, index=pythoncom.Empty):

        return _rsf.curve_knot_count(self.rhino_id, index)


    def knots(self, index=pythoncom.Empty):

        return _rsf.curve_knots(self.rhino_id, index)


    def length(self, index=pythoncom.Empty, sub_domain=pythoncom.Empty):

        return _rsf.curve_length(self.rhino_id, index, sub_domain)


    def mid_point(self, ):

        return _rsf.curve_mid_point(self.rhino_id)


    def normal(self, ):

        return _rsf.curve_normal(self.rhino_id)


    def plane(self, ):

        return _rsf.curve_plane(self.rhino_id)


    def control_point_count(self, index=pythoncom.Empty):

        return _rsf.curve_point_count(self.rhino_id, index)


    def control_points(self, index=pythoncom.Empty):

        return _rsf.curve_points(self.rhino_id, index)


    def start_point(self, index=pythoncom.Empty):

        return _rsf.curve_start_point(self.rhino_id, index)


    def weights(self, index=pythoncom.Empty):

        return _rsf.curve_weights(self.rhino_id, index)

