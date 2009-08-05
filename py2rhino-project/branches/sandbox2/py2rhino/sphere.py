# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._rhinoscript_classes import _SurfaceRoot


_rsf = None
from py2rhino._rhinoscript_classes import _ObjectRootDefm
from py2rhino._rhinoscript_classes import _SurfaceRootEval
from py2rhino._rhinoscript_classes import _SurfaceRootFuncOorc
from py2rhino._rhinoscript_classes import _SurfaceRootGenr
from py2rhino._rhinoscript_classes import _ObjectRootGrps
from py2rhino._rhinoscript_classes import _SurfaceRootMdfy
from py2rhino._rhinoscript_classes import _ObjectRootMtrl
from py2rhino._rhinoscript_classes import _SphereProp
from py2rhino._rhinoscript_classes import _ObjectRootRndr
from py2rhino._rhinoscript_classes import _ObjectRootStat
from py2rhino._rhinoscript_classes import _SurfaceRootTest
from py2rhino._rhinoscript_classes import _ObjectRootTrfm
from py2rhino._rhinoscript_classes import _ObjectRootUtil


class Sphere(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Sphere, _rsf )
        self.eval = _SurfaceRootEval(_rhino_id, Sphere, _rsf )
        self.func = _SurfaceRootFuncOorc(_rhino_id, Sphere, _rsf )
        self.genr = _SurfaceRootGenr(_rhino_id, Sphere, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, Sphere, _rsf )
        self.modf = _SurfaceRootMdfy(_rhino_id, Sphere, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, Sphere, _rsf )
        self.prop = _SphereProp(_rhino_id, Sphere, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, Sphere, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, Sphere, _rsf )
        self.test = _SurfaceRootTest(_rhino_id, Sphere, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, Sphere, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, Sphere, _rsf )

    @classmethod
    def create(cls, center, radius):

        _rhino_id = _rsf.add_sphere(center, radius)

        if _rhino_id:
            return Sphere(_rhino_id)
        else:
            return None

    @classmethod
    def create_by_plane(cls, center, radius):

        _rhino_id = _rsf.add_sphere_2(center, radius)

        if _rhino_id:
            return Sphere(_rhino_id)
        else:
            return None
