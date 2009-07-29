# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class DimLeader(p2r._Entity):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_leader(cls, points, view=pythoncom.Empty, text=pythoncom.Empty):

        return p2r_f.add_leader(points, view, text)


    def is_aligned_dimension(self, ):

        return p2r_f.is_aligned_dimension(self.rhino_id)


    def is_angular_dimension(self, ):

        return p2r_f.is_angular_dimension(self.rhino_id)


    def is_diameter_dimension(self, ):

        return p2r_f.is_diameter_dimension(self.rhino_id)


    def is_dim_style(self, ):

        return p2r_f.is_dim_style(self.rhino_id)


    def is_dim_style_reference(self, ):

        return p2r_f.is_dim_style_reference(self.rhino_id)


    def is_dimension(self, ):

        return p2r_f.is_dimension(self.rhino_id)


    def is_leader(self, ):

        return p2r_f.is_leader(self.rhino_id)


    def is_linear_dimension(self, ):

        return p2r_f.is_linear_dimension(self.rhino_id)


    def is_ordinate_dimension(self, ):

        return p2r_f.is_ordinate_dimension(self.rhino_id)


    def is_radial_dimension(self, ):

        return p2r_f.is_radial_dimension(self.rhino_id)


    def leader_text(self, text=pythoncom.Empty):

        return p2r_f.leader_text(self.rhino_id, text)

