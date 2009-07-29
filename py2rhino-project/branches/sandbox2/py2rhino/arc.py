# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class Arc(_CurveType):    # Class constructor
    def __init__(self):
        pass
    def (plane, radius, angle):

        return _rsf.add_arc(plane, radius, angle)

    def arc_3pt(start, end, point):

        return _rsf.add_arc_3_pt(start, end, point)

    def angle(, index=None):

        return _rsf.arc_angle(, index)

    def center_point(, index=None):

        return _rsf.arc_center_point(, index)

    def mid_point(, index=None):

        return _rsf.arc_mid_point(, index)

    def radius(, index=None):

        return _rsf.arc_radius(, index)

