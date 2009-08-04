# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
import py2rhino as p2r
from py2rhino import _util
from py2rhino._object_root import _ObjectRoot


_rsf = None
from py2rhino._object_root_defm import _ObjectRootDefm
from py2rhino._object_root_grps import _ObjectRootGrps
from py2rhino._object_root_mtrl import _ObjectRootMtrl
from py2rhino._object_root_prop import _ObjectRootProp
from py2rhino._object_root_rndr import _ObjectRootRndr
from py2rhino._object_root_stat import _ObjectRootStat
from py2rhino._object_root_test import _ObjectRootTest
from py2rhino._object_root_trfm import _ObjectRootTrfm
from py2rhino._object_root_type import _ObjectRootType
from py2rhino._object_root_util import _ObjectRootUtil


class GenericObject(_ObjectRoot):

    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = _ObjectRootDefm(_rhino_id, GenericObject, _rsf )
        self.grps = _ObjectRootGrps(_rhino_id, GenericObject, _rsf )
        self.mtrl = _ObjectRootMtrl(_rhino_id, GenericObject, _rsf )
        self.prop = _ObjectRootProp(_rhino_id, GenericObject, _rsf )
        self.rndr = _ObjectRootRndr(_rhino_id, GenericObject, _rsf )
        self.stat = _ObjectRootStat(_rhino_id, GenericObject, _rsf )
        self.test = _ObjectRootTest(_rhino_id, GenericObject, _rsf )
        self.trfm = _ObjectRootTrfm(_rhino_id, GenericObject, _rsf )
        self.type = _ObjectRootType(_rhino_id, GenericObject, _rsf )
        self.util = _ObjectRootUtil(_rhino_id, GenericObject, _rsf )
