# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._rhinoscript_classes import _CurveRoot


_rsf = None
from py2rhino._rhinoscript_classes import _ObjectRootDefm
from py2rhino._rhinoscript_classes import _CurveRootEval
from py2rhino._rhinoscript_classes import _CurveRootFuncOpen
from py2rhino._rhinoscript_classes import _ArcGenr
from py2rhino._rhinoscript_classes import _ObjectRootGrps
from py2rhino._rhinoscript_classes import _CurveRootMdfy
from py2rhino._rhinoscript_classes import _ObjectRootMtrl
from py2rhino._rhinoscript_classes import _ArcProp
from py2rhino._rhinoscript_classes import _ObjectRootRndr
from py2rhino._rhinoscript_classes import _ObjectRootStat
from py2rhino._rhinoscript_classes import _CurveRootTest
from py2rhino._rhinoscript_classes import _ObjectRootTrfm
from py2rhino._rhinoscript_classes import _ObjectRootUtil


class Arc(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Arc, _rsf )
        self.eval = _CurveRootEval(_rhino_id, Arc, _rsf )
        self.func = _CurveRootFuncOpen(_rhino_id, Arc, _rsf )
        self.genr = _ArcGenr(_rhino_id, Arc, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, Arc, _rsf )
        self.modf = _CurveRootMdfy(_rhino_id, Arc, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, Arc, _rsf )
        self.prop = _ArcProp(_rhino_id, Arc, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, Arc, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, Arc, _rsf )
        self.test = _CurveRootTest(_rhino_id, Arc, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, Arc, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, Arc, _rsf )

    @classmethod
    def create(cls, plane, radius, angle):

        _rhino_id = _rsf.add_arc(plane, radius, angle)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_3pt(cls, start, end, point):

        _rhino_id = _rsf.add_arc_3_pt(start, end, point)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_fillet(cls, curve_0, curve_1, radius=pythoncom.Empty, point_0=pythoncom.Empty, point_1=pythoncom.Empty):

        _rhino_id = _rsf.add_fillet_curve(curve_0._rhino_id, curve_1._rhino_id, radius, point_0, point_1)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None
