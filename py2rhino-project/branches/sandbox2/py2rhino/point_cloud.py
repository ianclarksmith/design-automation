# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class PointCloud(_PointType):    # Class constructor
    def __init__(self):
        pass
    def (points):

        return _rsf.add_point_cloud(points)

    def (text, point, plane, height=None, font=None, style=None):

        return _rsf.add_text(text, point, plane, height, font, style)

    def (test, point):

        return _rsf.add_text_dot(test, point)

    def point_cloud_count():

        return _rsf.point_cloud_count()

    def point_cloud_points():

        return _rsf.point_cloud_points()

