# Auto-generated wrapper for Rhino4 RhinoScript functions

import py2rhino.functions as rf
class Layer(_Entity):    # Class constructor
    def __init__(self):
        pass
    def (=None, color=None, visible=None, locked=None, parent=None):

        return _rsf.add_layer(, color, visible, locked, parent)

    def current_layer(=None):

        return _rsf.current_layer()

    def delete_layer():

        return _rsf.delete_layer()

    def expand_layer(, expand):

        return _rsf.expand_layer(, expand)

    def layer_child_count():

        return _rsf.layer_child_count()

    def layer_children():

        return _rsf.layer_children()

    def layer_color(, color=None):

        return _rsf.layer_color(, color)

    def layer_count():

        return _rsf.layer_count()

    def layer_linetype(, linetype=None):

        return _rsf.layer_linetype(, linetype)

    def layer_locked(, visible=None):

        return _rsf.layer_locked(, visible)

    def layer_material_index():

        return _rsf.layer_material_index()

    def layer_mode(, mode=None):

        return _rsf.layer_mode(, mode)

    def layer_names(sort=None):

        return _rsf.layer_names(sort)

    def layer_order():

        return _rsf.layer_order()

    def layer_print_color(, color=None):

        return _rsf.layer_print_color(, color)

    def layer_print_width(, width=None):

        return _rsf.layer_print_width(, width)

    def layer_visible(, visible=None):

        return _rsf.layer_visible(, visible)

    def parent_layer(, parent=None):

        return _rsf.parent_layer(, parent)

    def purge_layer():

        return _rsf.purge_layer()

    def rename_layer(, new_name):

        return _rsf.rename_layer(, new_name)

