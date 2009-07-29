# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.functions._rhinoscript_functions import _RhinoscriptFunctions as p2r_f
import py2rhino as p2r
from exceptions import Exception


class Layer(p2r._Entity):


    # Class constructor
    def __init__(self):
        raise Exception("Use the create... methods to create instances of this class.")


    @classmethod
    def (cls, color=pythoncom.Empty, visible=pythoncom.Empty, locked=pythoncom.Empty, parent=pythoncom.Empty):

        return p2r_f.add_layer(self.rhino_id, color, visible, locked, parent)


    def current_layer(self, ):

        return p2r_f.current_layer(self.rhino_id)


    def delete_layer(self, ):

        return p2r_f.delete_layer(self.rhino_id)


    def expand_layer(self, expand):

        return p2r_f.expand_layer(self.rhino_id, expand)


    def layer_child_count(self, ):

        return p2r_f.layer_child_count(self.rhino_id)


    def layer_children(self, ):

        return p2r_f.layer_children(self.rhino_id)


    def layer_color(self, color=pythoncom.Empty):

        return p2r_f.layer_color(self.rhino_id, color)


    def layer_count(self):

        return p2r_f.layer_count()


    def layer_linetype(self, linetype=pythoncom.Empty):

        return p2r_f.layer_linetype(self.rhino_id, linetype)


    def layer_locked(self, visible=pythoncom.Empty):

        return p2r_f.layer_locked(self.rhino_id, visible)


    def layer_material_index(self, ):

        return p2r_f.layer_material_index(self.rhino_id)


    def layer_mode(self, mode=pythoncom.Empty):

        return p2r_f.layer_mode(self.rhino_id, mode)


    def layer_names(self, sort=pythoncom.Empty):

        return p2r_f.layer_names(sort)


    def layer_order(self, ):

        return p2r_f.layer_order(self.rhino_id)


    def layer_print_color(self, color=pythoncom.Empty):

        return p2r_f.layer_print_color(self.rhino_id, color)


    def layer_print_width(self, width=pythoncom.Empty):

        return p2r_f.layer_print_width(self.rhino_id, width)


    def layer_visible(self, visible=pythoncom.Empty):

        return p2r_f.layer_visible(self.rhino_id, visible)


    def parent_layer(self, parent=pythoncom.Empty):

        return p2r_f.parent_layer(self.rhino_id, parent)


    def purge_layer(self, ):

        return p2r_f.purge_layer(self.rhino_id)


    def rename_layer(self, new_name):

        return p2r_f.rename_layer(self.rhino_id, new_name)

