# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class TextDot(p2r._TextType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_text_dot(cls, test, point):

        return p2r_f.add_text_dot(test, point)


    def point(self, point=pythoncom.Empty):

        return p2r_f.text_dot_point(self.rhino_id, point)


    def text(self, text=pythoncom.Empty):

        return p2r_f.text_dot_text(self.rhino_id, text)

