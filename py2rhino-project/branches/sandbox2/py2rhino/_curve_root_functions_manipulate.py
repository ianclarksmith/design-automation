# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _CurveRootFunctionsManipulate(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def curve_arc_length_point(self, length, from_start=pythoncom.Empty):

        return _rsf.curve_arc_length_point(self.rhino_id, length, from_start)


    def closest_ObjectRoot(self, objects):

        return _rsf.curve_closest_ObjectRoot(self.rhino_id, map(lambda i: i.rhino_id, objects))


    def closest_point(self, point, index=pythoncom.Empty):

        return _rsf.curve_closest_point(self.rhino_id, point, index)


    def contour_points(self, start_point, end_point, interval=pythoncom.Empty):

        return _rsf.curve_contour_points(self.rhino_id, start_point, end_point, interval)


    def deviation(self, curve_a):

        return _rsf.curve_deviation(self.rhino_id, curve_a)


    def directions_match(self, curve_1):

        return _rsf.curve_directions_match(self.rhino_id, curve_1)


    def fillet_points(self, curve_0, radius=pythoncom.Empty, base_point_0=pythoncom.Empty, base_point__1=pythoncom.Empty):

        return _rsf.curve_fillet_points(self.rhino_id, curve_0, radius, base_point_0, base_point__1)


    def radius(self, point, index=pythoncom.Empty):

        return _rsf.curve_radius(self.rhino_id, point, index)


    def divide_curve(self, segments, create=pythoncom.Empty, points=pythoncom.Empty):

        return _rsf.divide_curve(self.rhino_id, segments, create, points)


    def divide_curve_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):

        return _rsf.divide_curve_equidistant(self.rhino_id, distance, create, points)


    def divide_curve_length(self, length, create=pythoncom.Empty, points=pythoncom.Empty):

        return _rsf.divide_curve_length(self.rhino_id, length, create, points)


    def line_fit_from_points(self, ):

        return _rsf.line_fit_from_points(self.rhino_id)

