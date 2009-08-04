# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._surface_root import _SurfaceRoot


_rsf = None
from py2rhino._object_root_defm import _ObjectRootDefm
from py2rhino._surface_root_eval import _SurfaceRootEval
from py2rhino._surface_root_func_oorc import _SurfaceRootFuncOorc
from py2rhino._surface_root_genr import _SurfaceRootGenr
from py2rhino._object_root_grps import _ObjectRootGrps
from py2rhino._surface_root_mdfy import _SurfaceRootMdfy
from py2rhino._object_root_mtrl import _ObjectRootMtrl
from py2rhino._object_root_prop import _ObjectRootProp
from py2rhino._object_root_rndr import _ObjectRootRndr
from py2rhino._object_root_stat import _ObjectRootStat
from py2rhino._surface_root_test import _SurfaceRootTest
from py2rhino._object_root_trfm import _ObjectRootTrfm
from py2rhino._object_root_util import _ObjectRootUtil


class Box(_SurfaceRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, Box, _rsf )
        self.eval = _SurfaceRootEval(_rhino_id, Box, _rsf )
        self.func = _SurfaceRootFuncOorc(_rhino_id, Box, _rsf )
        self.genr = _SurfaceRootGenr(_rhino_id, Box, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, Box, _rsf )
        self.modf = _SurfaceRootMdfy(_rhino_id, Box, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, Box, _rsf )
        self.prop = _ObjectRootProp(_rhino_id, Box, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, Box, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, Box, _rsf )
        self.test = _SurfaceRootTest(_rhino_id, Box, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, Box, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, Box, _rsf )

    @classmethod
    def create(cls, corners):

        _rhino_id = _rsf.add_box(corners)

        if _rhino_id:
            return Box(_rhino_id)
        else:
            return None
