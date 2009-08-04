# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._curve_root import _CurveRoot


_rsf = None
from py2rhino._object_root_defm import _ObjectRootDefm
from py2rhino._curve_root_eval import _CurveRootEval
from py2rhino._curve_root_func_oorc import _CurveRootFuncOorc
from py2rhino._object_root_grps import _ObjectRootGrps
from py2rhino._curve_root_mdfy import _CurveRootMdfy
from py2rhino._object_root_mtrl import _ObjectRootMtrl
from py2rhino._polyline_genr import _PolylineGenr
from py2rhino._object_root_rndr import _ObjectRootRndr
from py2rhino._object_root_stat import _ObjectRootStat
from py2rhino._curve_root_test import _CurveRootTest
from py2rhino._object_root_trfm import _ObjectRootTrfm
from py2rhino._object_root_util import _ObjectRootUtil


class Polyline(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Polyline, _rsf )
        self.eval = _CurveRootEval(_rhino_id, Polyline, _rsf )
        self.func = _CurveRootFuncOorc(_rhino_id, Polyline, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, Polyline, _rsf )
        self.modf = _CurveRootMdfy(_rhino_id, Polyline, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, Polyline, _rsf )
        self.prop = _PolylineGenr(_rhino_id, Polyline, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, Polyline, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, Polyline, _rsf )
        self.test = _CurveRootTest(_rhino_id, Polyline, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, Polyline, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, Polyline, _rsf )

    @classmethod
    def create(cls, points):

        _rhino_id = _rsf.add_polyline(points)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_crv(cls, curve, angle_tolerance=pythoncom.Empty, tolerance=pythoncom.Empty, delete_input=pythoncom.Empty):

        _rhino_id = _rsf.convert_curve_to_polyline(curve._rhino_id, angle_tolerance, tolerance, delete_input)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None
