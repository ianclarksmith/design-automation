# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util


_rsf = None


class _ObjectRootFunctionsDeform(object):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def box_morph(self, box_points, copy=pythoncom.Empty):
        rhino_id = _rsf.box_morph_object(self.rhino_id, box_points, copy)
        if rhino_id:
            return _util.wrap(rhino_id)
        else:
            return None

    def shear(self, origin, ref_pt, scale, copy=pythoncom.Empty):
        rhino_id = _rsf.shear_object(self.rhino_id, origin, ref_pt, scale, copy)
        if rhino_id:
            return _util.wrap(rhino_id)
        else:
            return None

    def transform(self, matrix, copy=pythoncom.Empty):
        rhino_id = _rsf.transform_object(self.rhino_id, matrix, copy)
        if rhino_id:
            return _util.wrap(rhino_id)
        else:
            return None
