# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _ObjectRootStat(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def flash(self, style=pythoncom.Empty):
        return _rsf.flash_object()

    def hide(self):
        return _rsf.hide_objects(self._rhino_id)

    def lock(self):
        return _rsf.lock_objects(self._rhino_id)

    def match_object_attributes(self, targets):
        return _rsf.match_object_attributes(map(lambda i: i._rhino_id, targets), self._rhino_id)

    def reset_object_attributes(self, source):
        return _rsf.match_object_attributes(self._rhino_id, source._rhino_id)

    def move_to_layout_space(self, layout=pythoncom.Empty, return_name=pythoncom.Empty):
        return _rsf.object_layout(self._rhino_id, layout, return_name)

    def select(self):
        return _rsf.select_objects(self._rhino_id)

    def show(self):
        return _rsf.show_objects(self._rhino_id)

    def unlock(self):
        return _rsf.unlock_objects(self._rhino_id)

    def unselect(self):
        return _rsf.unselect_objects(self._rhino_id)
