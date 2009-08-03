# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util

_rsf = None

class _CurveRootFunctionsArea(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def area(self, ):
        return _rsf.curve_area(map(lambda i: i.rhino_id, ))

    def curve_area_centroid(self, objects):
        return _rsf.curve_area_centroid(map(lambda i: i.rhino_id, objects))

    def boolean_difference(self, curve):

        return map(lambda i: _CurveRoot(i), rhino_id)


    def boolean_intersection(self, curve_a):

        return map(lambda i: _CurveRoot(i), rhino_id)


    def boolean_union(self, curves):

        return map(lambda i: _CurveRoot(i), rhino_id)


    def planar_closed_curve_containment(self, curve__1, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.planar_closed_curve_containment(self.rhino_id, curve__1, plane, tolerance)

    def planar_curve_collision(self, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.planar_curve_collision(self.rhino_id, curve, plane, tolerance)

    def point_in_planar_closed_curve(self, point, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        return _rsf.point_in_planar_closed_curve(point, curve, plane, tolerance)
