# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._curve_root import _CurveRoot
from py2rhino._curve_root_functions_area import _CurveRootFunctionsArea
from py2rhino._circle_attributes import _CircleAttributes
from py2rhino._curve_root_functions_evaluate import _CurveRootFunctionsEvaluate
from py2rhino._object_root_functions_groups import _ObjectRootFunctionsGroups
from py2rhino._curve_root_functions_intersect import _CurveRootFunctionsIntersect
from py2rhino._curve_root_functions_manipulate import _CurveRootFunctionsManipulate
from py2rhino._object_root_functions_material import _ObjectRootFunctionsMaterial
from py2rhino._curve_root_functions_modify import _CurveRootFunctionsModify
from py2rhino._object_root_properties import _ObjectRootProperties
from py2rhino._object_root_functions_render import _ObjectRootFunctionsRender
from py2rhino._object_root_functions_state import _ObjectRootFunctionsState
from py2rhino._curve_root_functions_test import _CurveRootFunctionsTest
from py2rhino._object_root_functions_transform import _ObjectRootFunctionsTransform
from py2rhino._object_root_functions_util import _ObjectRootFunctionsUtil

_rsf = None

class Circle(_CurveRoot):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id

        self.area = _CurveRootFunctionsArea(rhino_id)
        self.attributes = _CircleAttributes(rhino_id)
        self.evaluate = _CurveRootFunctionsEvaluate(rhino_id)
        self.groups = _ObjectRootFunctionsGroups(rhino_id)
        self.intersect = _CurveRootFunctionsIntersect(rhino_id)
        self.manipulate = _CurveRootFunctionsManipulate(rhino_id)
        self.materials = _ObjectRootFunctionsMaterial(rhino_id)
        self.modify = _CurveRootFunctionsModify(rhino_id)
        self.properties = _ObjectRootProperties(rhino_id)
        self.render = _ObjectRootFunctionsRender(rhino_id)
        self.state = _ObjectRootFunctionsState(rhino_id)
        self.test = _CurveRootFunctionsTest(rhino_id)
        self.transform = _ObjectRootFunctionsTransform(rhino_id)
        self.utility = _ObjectRootFunctionsUtil(rhino_id)

    @classmethod
    def create_circle(cls, plane, radius):

        rhino_id = _rsf.add_circle(plane, radius)

        if rhino_id:
            return Circle(rhino_id)
        else:
            return None

    @classmethod
    def create_circle_3pt(cls, first, second, third):

        rhino_id = _rsf.add_circle_3_pt(first, second, third)

        if rhino_id:
            return Circle(rhino_id)
        else:
            return None
