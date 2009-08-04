# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._curve_root import _CurveRoot


_rsf = None
from py2rhino._object_root_defm import _ObjectRootDefm
from py2rhino._curve_root_eval import _CurveRootEval
from py2rhino._curve_root_func_open import _CurveRootFuncOpen
from py2rhino._elliptical_arc_genr import _EllipticalArcGenr
from py2rhino._object_root_grps import _ObjectRootGrps
from py2rhino._curve_root_mdfy import _CurveRootMdfy
from py2rhino._object_root_mtrl import _ObjectRootMtrl
from py2rhino._object_root_prop import _ObjectRootProp
from py2rhino._object_root_rndr import _ObjectRootRndr
from py2rhino._object_root_stat import _ObjectRootStat
from py2rhino._curve_root_test import _CurveRootTest
from py2rhino._object_root_trfm import _ObjectRootTrfm
from py2rhino._object_root_util import _ObjectRootUtil


class EllipticalArc(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, EllipticalArc, _rsf )
        self.eval = _CurveRootEval(_rhino_id, EllipticalArc, _rsf )
        self.func = _CurveRootFuncOpen(_rhino_id, EllipticalArc, _rsf )
        self.genr = _EllipticalArcGenr(_rhino_id, EllipticalArc, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, EllipticalArc, _rsf )
        self.modf = _CurveRootMdfy(_rhino_id, EllipticalArc, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, EllipticalArc, _rsf )
        self.prop = _ObjectRootProp(_rhino_id, EllipticalArc, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, EllipticalArc, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, EllipticalArc, _rsf )
        self.test = _CurveRootTest(_rhino_id, EllipticalArc, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, EllipticalArc, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, EllipticalArc, _rsf )
