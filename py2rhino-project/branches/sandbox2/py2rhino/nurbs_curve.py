# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from exceptions import Exception
from py2rhino import _util
from py2rhino._curve_root import _CurveRoot


_rsf = None
from py2rhino._curve_root_functions_area import _CurveRootFunctionsArea
from py2rhino._arc_attributes import _ArcAttributes
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


class NurbsCurve(_CurveRoot):

    # Class constructor
    def __init__(self, rhino_id):
        if rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self.rhino_id = rhino_id

        self.area = _CurveRootFunctionsArea(rhino_id, NurbsCurve, _rsf )
        self.attributes = _ArcAttributes(rhino_id, NurbsCurve, _rsf )
        self.deform = _ObjectRootFunctionsDeform(rhino_id, NurbsCurve, _rsf )
        self.evaluate = _CurveRootFunctionsEvaluate(rhino_id, NurbsCurve, _rsf )
        self.groups = _ObjectRootFunctionsGroups(rhino_id, NurbsCurve, _rsf )
        self.intersect = _CurveRootFunctionsIntersect(rhino_id, NurbsCurve, _rsf )
        self.manipulate = _CurveRootFunctionsManipulate(rhino_id, NurbsCurve, _rsf )
        self.materials = _ObjectRootFunctionsMaterial(rhino_id, NurbsCurve, _rsf )
        self.modify = _CurveRootFunctionsModify(rhino_id, NurbsCurve, _rsf )
        self.properties = _ObjectRootProperties(rhino_id, NurbsCurve, _rsf )
        self.render = _ObjectRootFunctionsRender(rhino_id, NurbsCurve, _rsf )
        self.state = _ObjectRootFunctionsState(rhino_id, NurbsCurve, _rsf )
        self.test = _CurveRootFunctionsTest(rhino_id, NurbsCurve, _rsf )
        self.transform = _ObjectRootFunctionsTransform(rhino_id, NurbsCurve, _rsf )
        self.utility = _ObjectRootFunctionsUtil(rhino_id, NurbsCurve, _rsf )

    @classmethod
    def create_by_points(cls, points, degree=pythoncom.Empty):

        rhino_id = _rsf.add_curve(points, degree)

        if rhino_id:
            return NurbsCurve(rhino_id)
        else:
            return None

    @classmethod
    def create_interp_curve_on_surface(cls, surface, points):

        rhino_id = _rsf.add_interp_crv_on_srf(surface.rhino_id, points)

        if rhino_id:
            return NurbsCurve(rhino_id)
        else:
            return None

    @classmethod
    def create_interp_curve_on_surface_uv(cls, surface, points):

        rhino_id = _rsf.add_interp_crv_on_srf_u_v(surface.rhino_id, points)

        if rhino_id:
            return NurbsCurve(rhino_id)
        else:
            return None

    @classmethod
    def create_interp_curve(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):

        rhino_id = _rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)

        if rhino_id:
            return NurbsCurve(rhino_id)
        else:
            return None

    @classmethod
    def create_interp_curve_ex(cls, points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):

        rhino_id = _rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)

        if rhino_id:
            return NurbsCurve(rhino_id)
        else:
            return None

    @classmethod
    def create(cls, points, knots, degree, weights=pythoncom.Empty):

        rhino_id = _rsf.add_nurbs_curve(points, knots, degree, weights)

        if rhino_id:
            return NurbsCurve(rhino_id)
        else:
            return None

    @classmethod
    def create_by_offset_on_surface(cls, curve, surface, distance, parameter):

        rhino_id = _rsf.offset_curve_on_surface(curve.rhino_id, surface, distance, parameter)

        if rhino_id:
            return NurbsCurve(rhino_id)
        else:
            return None

    @classmethod
    def create_by_projection_to_mesh(cls, curves, meshes, direction):

        rhino_id = _rsf.project_curve_to_mesh(map(lambda i: i.rhino_id, curves), meshes, direction)


        return map(lambda i: NurbsCurve(i), rhino_id)


    @classmethod
    def create_by_projection_to_surface(cls, curve, surfaces, direction):

        rhino_id = _rsf.project_curve_to_surface(curve.rhino_id, surfaces, direction)


        return map(lambda i: NurbsCurve(i), rhino_id)

