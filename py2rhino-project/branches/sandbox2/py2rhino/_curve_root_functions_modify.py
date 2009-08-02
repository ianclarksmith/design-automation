# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception

_rsf = None

class _CurveRootFunctionsModify(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def close_curve(self, tolerance=pythoncom.Empty):

        return _rsf.close_curve(self.rhino_id, tolerance)


    def seam(self, parameter):

        return _rsf.curve_seam(self.rhino_id, parameter)


    def extend_curve(self, type, side, objects):

        return _rsf.extend_curve(self.rhino_id, type, side, objects)


    def extend_curve_length(self, type, side, length):

        return _rsf.extend_curve_length(self.rhino_id, type, side, length)


    def extend_curve_point(self, side, point):

        return _rsf.extend_curve_point(self.rhino_id, side, point)


    def fair_curve(self, tolerance=pythoncom.Empty):

        return _rsf.fair_curve(self.rhino_id, tolerance)


    def fit_curve(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):

        return _rsf.fit_curve(self.rhino_id, degree, tolerance, angle_tolerance)


    def insert_curve_knot(self, parameter, symmetrical=pythoncom.Empty):

        return _rsf.insert_curve_knot(self.rhino_id, parameter, symmetrical)


    def make_curve_non_periodic(self, delete=pythoncom.Empty):

        return _rsf.make_curve_non_periodic(self.rhino_id, delete)


    def make_curve_periodic(self, delete=pythoncom.Empty):

        return _rsf.make_curve_periodic(self.rhino_id, delete)


    def project_curve_to_mesh(self, curves, meshes, direction):

        return _rsf.project_curve_to_mesh(map(lambda i: i.rhino_id, curves), meshes, direction)


    def rebuild_curve(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return _rsf.rebuild_curve(self.rhino_id, degree, point_count)


    def remove_curve_knot(self, parameter):

        return _rsf.remove_curve_knot(self.rhino_id, parameter)


    def reverse_curve(self, ):

        return _rsf.reverse_curve(self.rhino_id)


    def simplify_curve(self, flags=pythoncom.Empty):

        return _rsf.simplify_curve(self.rhino_id, flags)


    def trim_curve(self, interval, delete=pythoncom.Empty):

        return _rsf.trim_curve(self.rhino_id, interval, delete)

