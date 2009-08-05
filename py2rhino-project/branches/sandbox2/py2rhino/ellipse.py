# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._rhinoscript_classes import _CurveRoot


_rsf = None
from py2rhino._rhinoscript_classes import _ObjectRootDefm
from py2rhino._rhinoscript_classes import _CurveRootEval
from py2rhino._rhinoscript_classes import _CurveRootFuncClsd
from py2rhino._rhinoscript_classes import _EllipseGenr
from py2rhino._rhinoscript_classes import _ObjectRootGrps
from py2rhino._rhinoscript_classes import _CurveRootMdfy
from py2rhino._rhinoscript_classes import _ObjectRootMtrl
from py2rhino._rhinoscript_classes import _EllipseProp
from py2rhino._rhinoscript_classes import _ObjectRootRndr
from py2rhino._rhinoscript_classes import _ObjectRootStat
from py2rhino._rhinoscript_classes import _CurveRootTest
from py2rhino._rhinoscript_classes import _ObjectRootTrfm
from py2rhino._rhinoscript_classes import _ObjectRootUtil


class Ellipse(_CurveRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Ellipse, _rsf )
        self.eval = _CurveRootEval(_rhino_id, Ellipse, _rsf )
        self.func = _CurveRootFuncClsd(_rhino_id, Ellipse, _rsf )
        self.genr = _EllipseGenr(_rhino_id, Ellipse, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, Ellipse, _rsf )
        self.modf = _CurveRootMdfy(_rhino_id, Ellipse, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, Ellipse, _rsf )
        self.prop = _EllipseProp(_rhino_id, Ellipse, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, Ellipse, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, Ellipse, _rsf )
        self.test = _CurveRootTest(_rhino_id, Ellipse, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, Ellipse, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, Ellipse, _rsf )

    @classmethod
    def create(cls, plane, x_radius, y_radius):

        _rhino_id = _rsf.add_ellipse(plane, x_radius, y_radius)

        if _rhino_id:
            return Ellipse(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_3pt(cls, center, second, third):

        _rhino_id = _rsf.add_ellipse_3_pt(center, second, third)

        if _rhino_id:
            return Ellipse(_rhino_id)
        else:
            return None
