# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class ConstructionPlane(p2r._Entity):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def (cls, view=pythoncom.Empty):

        return p2r_f.add_named_c_plane(self.rhino_id, view)


    def delete_named_c_plane(self, ):

        return p2r_f.delete_named_c_plane(self.rhino_id)


    def named_c_planes(self):

        return p2r_f.named_c_planes()

