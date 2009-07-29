# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Hatch(p2r._OtherType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_hatch(cls, hatch=pythoncom.Empty, scale=pythoncom.Empty, rotation=pythoncom.Empty):

        return p2r_f.add_hatch(self.rhino_id, hatch, scale, rotation)


    @classmethod
    def create_hatches(cls, curves, hatch=pythoncom.Empty, scale=pythoncom.Empty, rotation=pythoncom.Empty):

        return p2r_f.add_hatches(curves, hatch, scale, rotation)


    def explode(self, delete=pythoncom.Empty):

        return p2r_f.explode_hatch(self.rhino_id, delete)


    def rotation(self, rotation=pythoncom.Empty):

        return p2r_f.hatch_rotation(self.rhino_id, rotation)


    def scale(self, scale=pythoncom.Empty):

        return p2r_f.hatch_scale(self.rhino_id, scale)

