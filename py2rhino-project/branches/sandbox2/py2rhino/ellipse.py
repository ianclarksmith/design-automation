# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class Ellipse(_CurveType):    # Class constructor
    def __init__(self):
        pass
    def (plane, x_radius, y_radius):

        return _rsf.add_ellipse(plane, x_radius, y_radius)

    def ellipse_3pt(center, second, third):

        return _rsf.add_ellipse_3_pt(center, second, third)

    def center_point():

        return _rsf.ellipse_center_point()

    def quad_points():

        return _rsf.ellipse_quad_points()

