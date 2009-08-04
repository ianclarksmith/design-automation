# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._object_root_modf import _ObjectRootModf


_rsf = None


class _CurveRootMdfy(_ObjectRootModf):

    # Class constructor
    def __init__(self, _rhino_id, _class, _rsf_in):
        if _rhino_id==None:
            raise Exception("_rhino_id is required.")
        self._rhino_id = _rhino_id
        self._class = _class
        global _rsf
        _rsf = _rsf_in

    def seam(self, parameter):

        return _rsf.curve_seam(self._rhino_id, parameter)


    def fair(self, tolerance=pythoncom.Empty):

        return _rsf.fair_curve(self._rhino_id, tolerance)


    def insert_knot(self, parameter, symmetrical=pythoncom.Empty):

        return _rsf.insert_curve_knot(self._rhino_id, parameter, symmetrical)


    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):

        return _rsf.rebuild_curve(self._rhino_id, degree, point_count)


    def remove_knot(self, parameter):

        return _rsf.remove_curve_knot(self._rhino_id, parameter)


    def reverse(self):

        return _rsf.reverse_curve(self._rhino_id)


    def simplify(self, flags=pythoncom.Empty):

        return _rsf.simplify_curve(self._rhino_id, flags)

