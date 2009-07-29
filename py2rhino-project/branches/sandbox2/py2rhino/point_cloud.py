# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class PointCloud(p2r._PointType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_point_cloud(cls, points):

        return p2r_f.add_point_cloud(points)


    def count(self, ):

        return p2r_f.point_cloud_count(self.rhino_id)


    def points(self, ):

        return p2r_f.point_cloud_points(self.rhino_id)

