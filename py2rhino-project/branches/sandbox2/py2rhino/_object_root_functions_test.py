# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util


_rsf = None


class _ObjectRootFunctionsTest(object):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def is_in_layout_space(self):
        return _rsf.is_layout_object(self.rhino_id)

    def is_hidden(self):
        return _rsf.is_object_hidden(self.rhino_id)

    def is_in_box(self, box, mode=pythoncom.Empty):
        return _rsf.is_object_in_box(self.rhino_id, box, mode)

    def is_in_group(self, group=pythoncom.Empty):
        return _rsf.is_object_in_group(self.rhino_id, group)

    def is_locked(self):
        return _rsf.is_object_locked(self.rhino_id)

    def is_normal(self):
        return _rsf.is_object_normal(self.rhino_id)

    def is_reference(self):
        return _rsf.is_object_reference(self.rhino_id)

    def is_selectable(self):
        return _rsf.is_object_selectable(self.rhino_id)

    def is_selected(self):
        return _rsf.is_object_selected(self.rhino_id)

    def is_solid(self):
        return _rsf.is_object_solid(self.rhino_id)

    def is_valid(self):
        return _rsf.is_object_valid(self.rhino_id)

    def is_visible_in_view(self, view=pythoncom.Empty):
        return _rsf.is_visible_in_view(self.rhino_id, view)
