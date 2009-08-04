# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _ObjectRootTest(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_in_layout_space(self):
        return _rsf.is_layout_object(self._rhino_id)

    def is_hidden(self):
        return _rsf.is_object_hidden(self._rhino_id)

    def is_in_box(self, box, mode=pythoncom.Empty):
        return _rsf.is_object_in_box(self._rhino_id, box, mode)

    def is_in_group(self, group=pythoncom.Empty):
        return _rsf.is_object_in_group(self._rhino_id, group)

    def is_locked(self):
        return _rsf.is_object_locked(self._rhino_id)

    def is_normal(self):
        return _rsf.is_object_normal(self._rhino_id)

    def is_reference(self):
        return _rsf.is_object_reference(self._rhino_id)

    def is_selectable(self):
        return _rsf.is_object_selectable(self._rhino_id)

    def is_selected(self):
        return _rsf.is_object_selected(self._rhino_id)

    def is_solid(self):
        return _rsf.is_object_solid(self._rhino_id)

    def is_valid(self):
        return _rsf.is_object_valid(self._rhino_id)

    def is_visible_in_view(self, view=pythoncom.Empty):
        return _rsf.is_visible_in_view(self._rhino_id, view)
