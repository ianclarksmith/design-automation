# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _ObjectRootDefm(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def box_morph(self, box_points, copy=pythoncom.Empty):
        _rhino_id = _rsf.box_morph_object(self._rhino_id, box_points, copy)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None

    def shear(self, origin, ref_pt, scale, copy=pythoncom.Empty):
        _rhino_id = _rsf.shear_object(self._rhino_id, origin, ref_pt, scale, copy)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None

    def trfm(self, matrix, copy=pythoncom.Empty):
        _rhino_id = _rsf.transform_object(self._rhino_id, matrix, copy)
        if _rhino_id:
            return _util.wrap(_rhino_id)
        else:
            return None
