# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class ClippingPlane(p2r._OtherType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    def create_clipping_plane(self, plane, d_u, d_v, views=pythoncom.Empty):

        return p2r_f.add_clipping_plane(plane, d_u, d_v, views)

