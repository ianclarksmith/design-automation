# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino._curve_root import _CurveRoot
from py2rhino._curve_root_functions_area import _CurveRootFunctionsArea
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

class NurbsCurve(_CurveRoot):

    # Class constructor
    def __init__(self, rhino_id=None):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id

        self.area = _CurveRootFunctionsArea(rhino_id)
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
    def create_curve_by_points(cls, points, degree=pythoncom.Empty):

        rhino_id = _rsf.add_curve(points, degree)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve_on_surface(cls, surface, points):

        rhino_id = _rsf.add_interp_crv_on_srf(surface.rhino_id, points)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve_on_surface_uv(cls, surface, points):

        rhino_id = _rsf.add_interp_crv_on_srf_u_v(surface.rhino_id, points)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):

        rhino_id = _rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_interp_curve_ex(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):

        rhino_id = _rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_curve(cls, points, knots, degree, weights=pythoncom.Empty):

        rhino_id = _rsf.add_nurbs_curve(points, knots, degree, weights)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_offset_curve_on_surface(cls, curve, surface, distance, parameter):

        rhino_id = _rsf.offset_curve_on_surface(curve.rhino_id, surface, distance, parameter)


        return NurbsCurve(rhino_id)


    @classmethod
    def create_project_curve_to_surface(cls, curve, surfaces, direction):

        rhino_id = _rsf.project_curve_to_surface(curve.rhino_id, surfaces, direction)


        return NurbsCurve(rhino_id)

