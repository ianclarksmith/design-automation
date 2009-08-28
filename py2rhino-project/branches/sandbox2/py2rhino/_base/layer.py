# Auto-generated module that wraps the RhinoscriptFunctions class

import pythoncom

_rsf = None

def add_layer(layer=pythoncom.Empty, color=pythoncom.Empty, visible=pythoncom.Empty, locked=pythoncom.Empty, parent=pythoncom.Empty):

    return _rsf.add_layer(layer, color, visible, locked, parent)

def current_layer(layer=pythoncom.Empty):

    return _rsf.current_layer(layer)

def delete_layer(layer):

    return _rsf.delete_layer(layer)

def expand_layer(layer, expand):

    return _rsf.expand_layer(layer, expand)

def is_layer(layer):

    return _rsf.is_layer(layer)

def is_layer_changeable(layer):

    return _rsf.is_layer_changeable(layer)

def is_layer_child_of(layer, test):

    return _rsf.is_layer_child_of(layer, test)

def is_layer_current(layer):

    return _rsf.is_layer_current(layer)

def is_layer_empty(layer):

    return _rsf.is_layer_empty(layer)

def is_layer_expanded(layer):

    return _rsf.is_layer_expanded(layer)

def is_layer_locked(layer):

    return _rsf.is_layer_locked(layer)

def is_layer_on(layer):

    return _rsf.is_layer_on(layer)

def is_layer_parent_of(layer, test):

    return _rsf.is_layer_parent_of(layer, test)

def is_layer_reference(layer):

    return _rsf.is_layer_reference(layer)

def is_layer_selectable(layer):

    return _rsf.is_layer_selectable(layer)

def is_layer_visible(layer):

    return _rsf.is_layer_visible(layer)

def layer_child_count(layer):

    return _rsf.layer_child_count(layer)

def layer_children(layer):

    return _rsf.layer_children(layer)

def layer_color(layer, color=pythoncom.Empty):

    return _rsf.layer_color(layer, color)

def layer_count():

    return _rsf.layer_count()

def layer_linetype(layer, linetype=pythoncom.Empty):

    return _rsf.layer_linetype(layer, linetype)

def layer_locked(layer, visible=pythoncom.Empty):

    return _rsf.layer_locked(layer, visible)

def layer_material_index(layer):

    return _rsf.layer_material_index(layer)

def layer_mode(layer, mode=pythoncom.Empty):

    return _rsf.layer_mode(layer, mode)

def layer_names(sort=pythoncom.Empty):

    return _rsf.layer_names(sort)

def layer_order(layer):

    return _rsf.layer_order(layer)

def layer_print_color(layer, color=pythoncom.Empty):

    return _rsf.layer_print_color(layer, color)

def layer_print_width(layer, width=pythoncom.Empty):

    return _rsf.layer_print_width(layer, width)

def layer_visible(layer, visible=pythoncom.Empty):

    return _rsf.layer_visible(layer, visible)

def parent_layer(layer, parent=pythoncom.Empty):

    return _rsf.parent_layer(layer, parent)

def purge_layer(layer):

    return _rsf.purge_layer(layer)

def rename_layer(old_name, new_name):

    return _rsf.rename_layer(old_name, new_name)

