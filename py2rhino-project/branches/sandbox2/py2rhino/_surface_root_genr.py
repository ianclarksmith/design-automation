# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util


_rsf = None


class _SurfaceRootGenr(object):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def fit(self, degree=pythoncom.Empty, tolerance=pythoncom.Empty):
        _rhino_id = _rsf.fit_surface(self._rhino_id, degree, tolerance)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def make_non_periodic(self, direction, delete=pythoncom.Empty):
        _rhino_id = _rsf.make_surface_non_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def make_periodic(self, direction, delete=pythoncom.Empty):
        _rhino_id = _rsf.make_surface_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None

    def offset(self, distance):
        _rhino_id = _rsf.offset_surface(self._rhino_id, distance)
        if _rhino_id:
            return p2r.NurbsSurface(_rhino_id)
        else:
            return None
