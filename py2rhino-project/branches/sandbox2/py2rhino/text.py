# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Text(p2r._TextType):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_text(cls, text, point, plane, height=pythoncom.Empty, font=pythoncom.Empty, style=pythoncom.Empty):

        return p2r_f.add_text(text, point, plane, height, font, style)


    def font(self, font=pythoncom.Empty):

        return p2r_f.text_object_font(self.rhino_id, font)


    def height(self, height=pythoncom.Empty):

        return p2r_f.text_object_height(self.rhino_id, height)


    def plane(self, plane=pythoncom.Empty):

        return p2r_f.text_object_plane(self.rhino_id, plane)


    def point(self, point=pythoncom.Empty):

        return p2r_f.text_object_point(self.rhino_id, point)


    def style(self, style=pythoncom.Empty):

        return p2r_f.text_object_style(self.rhino_id, style)


    def text(self, text=pythoncom.Empty):

        return p2r_f.text_object_text(self.rhino_id, text)

