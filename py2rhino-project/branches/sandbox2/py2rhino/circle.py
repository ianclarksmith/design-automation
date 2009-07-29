# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class Circle(_CurveType):    # Class constructor
    def __init__(self):
        pass
    def (plane, radius):

        return _rsf.add_circle(plane, radius)

    def circle_3pt(first, second, third):

        return _rsf.add_circle_3_pt(first, second, third)

    def center_point(, index=None):

        return _rsf.center_point(, index)

    def circumference(, index=None):

        return _rsf.circle_circumference(, index)

    def radius(, index=None):

        return _rsf.circle_radius(, index)

