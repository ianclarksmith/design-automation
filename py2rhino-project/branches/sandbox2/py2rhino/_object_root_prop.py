# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _ObjectRootProp(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def color(self, color=pythoncom.Empty):
        return _rsf.object_color(self._rhino_id, color)

    def color_source(self, source=pythoncom.Empty):
        return _rsf.object_color_source(self._rhino_id, source)

    def layer(self, layer=pythoncom.Empty):
        return _rsf.object_layer(self._rhino_id, layer._rhino_id)

    def linetype(self, layer=pythoncom.Empty):
        return _rsf.object_linetype(self._rhino_id, layer._rhino_id)

    def linetype_source(self, source=pythoncom.Empty):
        return _rsf.object_linetype_source(self._rhino_id, source)

    def name(self, names=pythoncom.Empty):
        return _rsf.object_names(self._rhino_id, names)

    def print_color(self, color=pythoncom.Empty):
        return _rsf.object_print_color(self._rhino_id, color)

    def print_color_source(self, source=pythoncom.Empty):
        return _rsf.object_print_color_source(self._rhino_id, source)

    def print_width(self, width=pythoncom.Empty):
        return _rsf.object_print_width(self._rhino_id, width)

    def print_width_source(self, source=pythoncom.Empty):
        return _rsf.object_print_width_source(self._rhino_id, source)
