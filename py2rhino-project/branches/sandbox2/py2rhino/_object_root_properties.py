# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util

_rsf = None

class _ObjectRootProperties(object):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id


    def color(self, color=pythoncom.Empty):
        return _rsf.object_color(self.rhino_id, color)

    def color_source(self, source=pythoncom.Empty):
        return _rsf.object_color_source(self.rhino_id, source)

    def layer(self, layer=pythoncom.Empty):
        return _rsf.object_layer(self.rhino_id, layer.rhino_id)

    def linetype(self, layer=pythoncom.Empty):
        return _rsf.object_linetype(self.rhino_id, layer.rhino_id)

    def linetype_source(self, source=pythoncom.Empty):
        return _rsf.object_linetype_source(self.rhino_id, source)

    def name(self, names=pythoncom.Empty):
        return _rsf.object_names(self.rhino_id, names)

    def print_color(self, color=pythoncom.Empty):
        return _rsf.object_print_color(self.rhino_id, color)

    def print_color_source(self, source=pythoncom.Empty):
        return _rsf.object_print_color_source(self.rhino_id, source)

    def print_width(self, width=pythoncom.Empty):
        return _rsf.object_print_width(self.rhino_id, width)

    def print_width_source(self, source=pythoncom.Empty):
        return _rsf.object_print_width_source(self.rhino_id, source)
