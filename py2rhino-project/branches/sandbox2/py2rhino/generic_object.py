# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._object_root import _ObjectRoot


_rsf = None
from py2rhino._object_root_functions_deform import _ObjectRootFunctionsDeform
from py2rhino._object_root_functions_groups import _ObjectRootFunctionsGroups
from py2rhino._object_root_functions_material import _ObjectRootFunctionsMaterial
from py2rhino._object_root_properties import _ObjectRootProperties
from py2rhino._object_root_functions_render import _ObjectRootFunctionsRender
from py2rhino._object_root_functions_state import _ObjectRootFunctionsState
from py2rhino._object_root_functions_test import _ObjectRootFunctionsTest
from py2rhino._object_root_functions_transform import _ObjectRootFunctionsTransform
from py2rhino._object_root_functions_type import _ObjectRootFunctionsType
from py2rhino._object_root_functions_util import _ObjectRootFunctionsUtil


class GenericObject(_ObjectRoot):

    # Class constructor
    def __init__(self, rhino_id):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id

        self.deform = _ObjectRootFunctionsDeform(rhino_id, GenericObject, _rsf )
        self.groups = _ObjectRootFunctionsGroups(rhino_id, GenericObject, _rsf )
        self.materials = _ObjectRootFunctionsMaterial(rhino_id, GenericObject, _rsf )
        self.properties = _ObjectRootProperties(rhino_id, GenericObject, _rsf )
        self.render = _ObjectRootFunctionsRender(rhino_id, GenericObject, _rsf )
        self.state = _ObjectRootFunctionsState(rhino_id, GenericObject, _rsf )
        self.test = _ObjectRootFunctionsTest(rhino_id, GenericObject, _rsf )
        self.transform = _ObjectRootFunctionsTransform(rhino_id, GenericObject, _rsf )
        self.type = _ObjectRootFunctionsType(rhino_id, GenericObject, _rsf )
        self.utility = _ObjectRootFunctionsUtil(rhino_id, GenericObject, _rsf )
