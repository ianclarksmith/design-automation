# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util


_rsf = None


class _ObjectRootFunctionsType(object):

    # Class constructor
    def __init__(self, rhino_id, _class, _rsf_in):
        if rhino_id==None:
            raise Exception("rhino_id is required.")
        self.rhino_id = rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def object_type(self):
        return _rsf.object_type(self.rhino_id)
