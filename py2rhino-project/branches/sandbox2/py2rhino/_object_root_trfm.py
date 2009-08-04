# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _ObjectRootTrfm(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def copy(self, start=pythoncom.Empty, end=pythoncom.Empty):
        _rhino_id = _rsf.copy_object(self._rhino_id, start, end)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def copy_and_xform(self, translation=pythoncom.Empty):
        _rhino_id = _rsf.copy_object_2(self._rhino_id, translation)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def mirror(self, start_pt, end_pt, copy=pythoncom.Empty):
        _rhino_id = _rsf.mirror_object(self._rhino_id, start_pt, end_pt, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move(self, start, end):
        _rhino_id = _rsf.move_object(self._rhino_id, start, end)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move_and_xform(self, translation):
        _rhino_id = _rsf.move_object_2(self._rhino_id, translation)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def orient(self, reference, target, flags=pythoncom.Empty):
        _rhino_id = _rsf.orient_object(self._rhino_id, reference, target, flags)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def remap(self, src_plane, dst_plane, copy=pythoncom.Empty):
        _rhino_id = _rsf.remap_object(self._rhino_id, src_plane, dst_plane, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def rotate(self, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):
        _rhino_id = _rsf.rotate_object(self._rhino_id, point, angle, axis, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def scale(self, origin, scale, copy=pythoncom.Empty):
        _rhino_id = _rsf.scale_object(self._rhino_id, origin, scale, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None
