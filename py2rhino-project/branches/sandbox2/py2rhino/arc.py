# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._curve_root import _CurveRoot
from py2rhino._arc_attributes import _ArcAttributes
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

class Arc(_CurveRoot):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id

        self.attributes = _ArcAttributes(rhino_id)
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
    def create_arc(cls, plane, radius, angle):

        rhino_id = _rsf.add_arc(plane, radius, angle)


        return Arc(rhino_id)


    @classmethod
    def create_arc_3pt(cls, start, end, point):

        rhino_id = _rsf.add_arc_3_pt(start, end, point)


        return Arc(rhino_id)


    @classmethod
    def create_arc_fillet(cls, curve_0, curve_1, radius=pythoncom.Empty, point_0=pythoncom.Empty, point_1=pythoncom.Empty):

        rhino_id = _rsf.add_fillet_curve(curve_0.rhino_id, curve_1.rhino_id, radius, point_0, point_1)


        return Arc(rhino_id)

