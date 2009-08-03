# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._curve_root import _CurveRoot


_rsf = None
from py2rhino._curve_root_functions_area import _CurveRootFunctionsArea
from py2rhino._ellipse_attributes import _EllipseAttributes
from py2rhino._object_root_functions_deform import _ObjectRootFunctionsDeform
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


class Ellipse(_CurveRoot):

    # Class constructor
    def __init__(self, rhino_id):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id

        self.area = _CurveRootFunctionsArea(rhino_id, Ellipse, _rsf )
        self.attributes = _EllipseAttributes(rhino_id, Ellipse, _rsf )
        self.deform = _ObjectRootFunctionsDeform(rhino_id, Ellipse, _rsf )
        self.evaluate = _CurveRootFunctionsEvaluate(rhino_id, Ellipse, _rsf )
        self.groups = _ObjectRootFunctionsGroups(rhino_id, Ellipse, _rsf )
        self.intersect = _CurveRootFunctionsIntersect(rhino_id, Ellipse, _rsf )
        self.manipulate = _CurveRootFunctionsManipulate(rhino_id, Ellipse, _rsf )
        self.materials = _ObjectRootFunctionsMaterial(rhino_id, Ellipse, _rsf )
        self.modify = _CurveRootFunctionsModify(rhino_id, Ellipse, _rsf )
        self.properties = _ObjectRootProperties(rhino_id, Ellipse, _rsf )
        self.render = _ObjectRootFunctionsRender(rhino_id, Ellipse, _rsf )
        self.state = _ObjectRootFunctionsState(rhino_id, Ellipse, _rsf )
        self.test = _CurveRootFunctionsTest(rhino_id, Ellipse, _rsf )
        self.transform = _ObjectRootFunctionsTransform(rhino_id, Ellipse, _rsf )
        self.utility = _ObjectRootFunctionsUtil(rhino_id, Ellipse, _rsf )

    @classmethod
    def create_ellipse(cls, plane, x_radius, y_radius):

        rhino_id = _rsf.add_ellipse(plane, x_radius, y_radius)

        if rhino_id:
            return Ellipse(rhino_id)
        else:
            return None

    @classmethod
    def create_ellipse_3pt(cls, center, second, third):

        rhino_id = _rsf.add_ellipse_3_pt(center, second, third)

        if rhino_id:
            return Ellipse(rhino_id)
        else:
            return None
