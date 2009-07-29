# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class DimStyle(p2r._Entity):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def create_dim_style(cls, ):

        return p2r_f.add_dim_style(self.rhino_id)


    def current_dim_style(self, ):

        return p2r_f.current_dim_style(self.rhino_id)


    def delete_dim_style(self, ):

        return p2r_f.delete_dim_style(self.rhino_id)


    def dim_scale(self, scale=pythoncom.Empty):

        return p2r_f.dim_scale(scale)


    def dim_style_angle_precision(self, precision=pythoncom.Empty):

        return p2r_f.dim_style_angle_precision(self.rhino_id, precision)


    def dim_style_arrow_size(self, size=pythoncom.Empty):

        return p2r_f.dim_style_arrow_size(self.rhino_id, size)


    def dim_style_count(self):

        return p2r_f.dim_style_count()


    def dim_style_extension(self, extension=pythoncom.Empty):

        return p2r_f.dim_style_extension(self.rhino_id, extension)


    def dim_style_font(self, dim_style, font=pythoncom.Empty):

        return p2r_f.dim_style_font(dim_style, font)


    def dim_style_leader_arrow_size(self, size=pythoncom.Empty):

        return p2r_f.dim_style_leader_arrow_size(self.rhino_id, size)


    def dim_style_linear_precision(self, precision=pythoncom.Empty):

        return p2r_f.dim_style_linear_precision(self.rhino_id, precision)


    def dim_style_names(self, sort=pythoncom.Empty):

        return p2r_f.dim_style_names(sort)


    def dim_style_number_format(self, format=pythoncom.Empty):

        return p2r_f.dim_style_number_format(self.rhino_id, format)


    def dim_style_offset(self, offset=pythoncom.Empty):

        return p2r_f.dim_style_offset(self.rhino_id, offset)


    def dim_style_text_alignment(self, alignment=pythoncom.Empty):

        return p2r_f.dim_style_text_alignment(self.rhino_id, alignment)


    def dim_style_text_gap(self, gap=pythoncom.Empty):

        return p2r_f.dim_style_text_gap(self.rhino_id, gap)


    def dim_style_text_height(self, height=pythoncom.Empty):

        return p2r_f.dim_style_text_height(self.rhino_id, height)


    def dimension_style(self, style=pythoncom.Empty):

        return p2r_f.dimension_style(self.rhino_id, style)


    def dimension_text(self, ):

        return p2r_f.dimension_text(self.rhino_id)


    def dimension_user_text(self, user_text=pythoncom.Empty):

        return p2r_f.dimension_user_text(self.rhino_id, user_text)


    def dimension_value(self, ):

        return p2r_f.dimension_value(self.rhino_id)


    def rename_dim_style(self, new_style):

        return p2r_f.rename_dim_style(self.rhino_id, new_style)

