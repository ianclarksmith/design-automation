# Auto-generated wrapper for Rhino4 RhinoScript classes
import pythoncom
from exceptions import Exception
import _util
import _wrap
import py2rhino as p2r
from py2rhino import _base
class _ArcDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.Arc(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Arc(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Arc(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.Arc(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Arc(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.Arc(_rhino_id)
        else:
            return None
class _BoxDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Box(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Box(_rhino_id)
        else:
            return None
class _CircleDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.Arc(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Circle(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Circle(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.Circle(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Arc(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.Arc(_rhino_id)
        else:
            return None
class _ConeDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Cone(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Cone(_rhino_id)
        else:
            return None
class _CurveRootEval(object):

    def curvature(self, parameter):
        """
        
        Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.

        Returns
        =======
        list - A list of curvature information if successful.  The list will contain the following information:
        number - Radius of curvature
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveCurvature
        """
        return _base._rsf.curve_curvature(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        """
        
        A general purpose curve evaluator.

        Parameters
        ==========
        parameter  (float, Required) - The evaluation parameter.
        derivative  (integer, Required) - The number of derivatives to evaluate.

        Returns
        =======
        list - A list of length (derivative+1) if successful.  The list elements are as follows:
        list - The 3-D point
        list - The first derivative
        list - The second derivative
        list - etc...
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveEvaluate
        """
        return _base._rsf.curve_evaluate(self._rhino_id, parameter, derivative)

    def frame(self, parameter):
        """
        
        Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.

        Returns
        =======
        list - The plane at the specified parameter if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveFrame
        """
        return _base._rsf.curve_frame(self._rhino_id, parameter)

    def perp_frame(self, parameter):
        """
        
        Returns the perpendicular plane at a parameter of a curve.  The result is relatively parallel (zero-twisting) plane.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.

        Returns
        =======
        list - The plane at the specified parameter if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurvePerpFrame
        """
        return _base._rsf.curve_perp_frame(self._rhino_id, parameter)

    def tangent(self, parameter):
        """
        
        Returns a 3-D vector that is the tangent to a curve at a parameter.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.

        Returns
        =======
        list - A  3-D vector if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveTangent
        """
        return _base._rsf.curve_tangent(self._rhino_id, parameter, pythoncom.Empty)

    def evaluate(self, parameter):
        """
        
        Evaluates a curve at a parameter.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.

        Returns
        =======
        list - A 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EvaluateCurve
        """
        return _base._rsf.evaluate_curve(self._rhino_id, parameter, pythoncom.Empty)
class _CurveRootProp(object):

    def arrows(self, style=pythoncom.Empty):
        """
        
        Enables or disabled a curve object's annotation arrows.

        Parameters
        ==========
        style  (integer, Optional) - The style of annotation arrows to be displayed.  The styles are as follows:
		Value
		Description
		0
		No annotation arrows
		1
		Display an annotation arrow at the starting point of the curve
		2
		Display an annotation arrow at the ending point of the curve
		3

        Returns
        =======
        number - If style is not specified, the current annotation arrow style if successful.
        number - If style is specified, the previous annotation arrow style if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveArrows
        """
        return _base._rsf.curve_arrows(self._rhino_id, style)

    def degree(self):
        """
        
        Returns the degree of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The degree of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDegree
        """
        return _base._rsf.curve_degree(self._rhino_id, pythoncom.Empty)

    def dim(self):
        """
        
        Returns the dimension of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The dimension of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDim
        """
        return _base._rsf.curve_dim(self._rhino_id, pythoncom.Empty)

    def discontinuity(self, style):
        """
        
        Search for a derivatitive, tangent, or curvature discontinuity in a curve object.

        Parameters
        ==========
        style  (integer, Required) - The type of continuity to test for.  The types of continuity are as follows:
		Value
		Description
		1
		C0 - Continuous function
		2
		C1 - Continuous first derivative
		3
		C2 - Continuous first and second derivative
		4
		G1 - Continuous unit tangent
		5

        Returns
        =======
        list - A list of 3-D points where the curve is discontinuous if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDiscontinuity
        """
        return _base._rsf.curve_discontinuity(self._rhino_id, style)

    def domain(self):
        """
        
        Returns the domain of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The domain of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDomain
        """
        return _base._rsf.curve_domain(self._rhino_id, pythoncom.Empty)

    def edit_pnts(self, return_parameters=pythoncom.Empty):
        """
        
        Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.

        Parameters
        ==========
        return_parameters  (boolean, Optional) - Return the edit points as an list of parameter values.  If omitted, the edit points are returned as an list of 3-D points.

        Returns
        =======
        list - If return_parameters is omitted or False, then a list of 3-D edit points if successful.
        list - If return_parameters is True, then a list of parameter values if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveEditPoints
        """
        return _base._rsf.curve_edit_points(self._rhino_id, return_parameters, pythoncom.Empty)

    def end_pnt(self):
        """
        
        Returns the end point of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The 3-D end point of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveEndPoint
        """
        return _base._rsf.curve_end_point(self._rhino_id, pythoncom.Empty)

    def knot_count(self):
        """
        
        Returns the knot count of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of knots if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveKnotCount
        """
        return _base._rsf.curve_knot_count(self._rhino_id, pythoncom.Empty)

    def knots(self):
        """
        
        Returns the knots, or knot vector, of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The knot values of the curve  if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveKnots
        """
        return _base._rsf.curve_knots(self._rhino_id, pythoncom.Empty)

    def length(self, sub_domain=pythoncom.Empty):
        """
        
        Returns the length of a curve object.

        Parameters
        ==========
        sub_domain  (List of integer, Optional) - An list of two numbers identifying the sub-domain of the curve on which the calculation will be performed.  The two parameters (sub-domain) must be non-decreasing.  If omitted, the length of the entire curve is returned.

        Returns
        =======
        number - The length of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveLength
        """
        return _base._rsf.curve_length(self._rhino_id, pythoncom.Empty, sub_domain)

    def mid_pnt(self):
        """
        
        Returns the mid point of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The 3-D mid point of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveMidPoint
        """
        return _base._rsf.curve_mid_point(self._rhino_id)

    def normal(self):
        """
        
        Returns the normal direction of the plane in which a planar curve object lies.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The 3-D normal vector if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveNormal
        """
        return _base._rsf.curve_normal(self._rhino_id)

    def plane(self):
        """
        
        Returns the plane in which a planar curve lies. Note, this function works only on planar curves.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The plane in which the curve lies if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurvePlane
        """
        return _base._rsf.curve_plane(self._rhino_id)

    def control_pnt_count(self):
        """
        
        Returns the control points count of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of control points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurvePointCount
        """
        return _base._rsf.curve_point_count(self._rhino_id, pythoncom.Empty)

    def control_pnts(self):
        """
        
        Returns the control points, or control vertices, of a curve object.  If the curve is a rational NURBS curve, the euclidean control vertices are returned.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The control points of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurvePoints
        """
        return _base._rsf.curve_points(self._rhino_id, pythoncom.Empty)

    def start_pnt(self):
        """
        
        Returns the start point of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The 3-D starting point of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveStartPoint
        """
        return _base._rsf.curve_start_point(self._rhino_id, pythoncom.Empty)

    def weights(self):
        """
        
        Returns an array of weight values that are assigned to the control points of a curve.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The weight values of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveWeights
        """
        return _base._rsf.curve_weights(self._rhino_id, pythoncom.Empty)
class _CylinderDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Cylinder(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Cylinder(_rhino_id)
        else:
            return None
class _EllipseDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.EllipticalArc(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Ellipse(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Ellipse(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.Ellipse(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.EllipticalArc(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.EllipticalArc(_rhino_id)
        else:
            return None
class _EllipticalArcDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.EllipticalArc(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.EllipticalArc(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.EllipticalArc(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.EllipticalArc(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.EllipticalArc(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.EllipticalArc(_rhino_id)
        else:
            return None
class _LineDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.Line(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Line(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Line(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.Line(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Line(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.Line(_rhino_id)
        else:
            return None
class _MeshDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Mesh(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Mesh(_rhino_id)
        else:
            return None

    def copy_by_offset(self, mesh, distance):
        """
        
        Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.

        Parameters
        ==========
        mesh  (mesh object, Required) - The identifier of a mesh object.
        distance  (float, Required) - The distance to offset.

        Returns
        =======
        object - The offset mesh object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshOffset
        """
        _rhino_id = _base._rsf.mesh_offset(mesh._rhino_id, distance)
        if _rhino_id:
            return p2r.obj.Mesh(_rhino_id)
        else:
            return None
class _NurbsCurveDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def copy_by_offset_on_srf(self, surface, distance):
        """
        
        Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.

        Parameters
        ==========
        surface  (surface object, Required) - The surface object's identifier.
        distance  (float, Required) - The distance of the offset.  Based on the curve's direction, a possitive value will offset to the left and a negative value will offset to the right.

        Returns
        =======
        list - A list containing the identifiers of the new curve objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurveOnSurface
        """
        _rhino_id = _base._rsf.offset_curve_on_surface(self._rhino_id, surface._rhino_id, distance)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def copy_by_offset_on_srf_by_param(self, surface, parameter):
        """
        
        Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.

        Parameters
        ==========
        surface  (surface object, Required) - The surface object's identifier.
        parameter  (List of float, Required) - An list containing the surface U,V parameter that the curve will be offset through.

        Returns
        =======
        list - A list containing the identifiers of the new curve objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurveOnSurface2
        """
        _rhino_id = _base._rsf.offset_curve_on_surface_2(self._rhino_id, surface._rhino_id, parameter)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.NurbsCurve(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None
class _NurbsSurfaceDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.NurbsSurface(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.NurbsSurface(_rhino_id)
        else:
            return None

    def copy_by_offset(self, distance):
        """
        
        Offsets a surface by a distance. The offset surface will be added to Rhino.

        Parameters
        ==========
        distance  (float, Required) - The distance to offset.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetSurface
        """
        _rhino_id = _base._rsf.offset_surface(self._rhino_id, distance)
        if _rhino_id:
            return p2r.obj.NurbsSurface(_rhino_id)
        else:
            return None
class _ObjectRoot(object):
    pass
class _ObjectRootDefm(object):

    def box_morph(self, box_points, copy=pythoncom.Empty):
        """
        
        Morphs an object by mapping its eight bounding box points to eight new points. Note, this function only works on non-planar objects.

        Parameters
        ==========
        box_points  (List of float, Required) - An list of eight 3-D points that contain the modified bounding box points.
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        object - The morphed object if successful.
        list - A list of strings identifying the morphed objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BoxMorphObject
        """
        _rhino_id = _base._rsf.box_morph_object(self._rhino_id, box_points, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def shear(self, origin, ref_point, angle, copy=pythoncom.Empty):
        """
        
        Performs a shear transformation on a single object. Transformation is based on the active construction plane.

        Parameters
        ==========
        origin  (List of float, Required) - The origin of the shear transformation.
        ref_point  (List of float, Required) - The reference point of the shear transformation.
        angle  (float, Required) - An angle in degrees of the shear transformation, where -90.0 <= angle <= 90.0.
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        object - The sheared object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ShearObject
        """
        _rhino_id = _base._rsf.shear_object(self._rhino_id, origin, ref_point, angle, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def trfm(self, matrix, copy=pythoncom.Empty):
        """
        
        Moves, scales, or rotates an object given a 4x4 transformation matrix. The matrix acts on the left. The following table demonstrates the transformation matrix configuration:
		1
		0
		0
		dX
		0
		1
		0
		dY
		0
		0
		1
		dZ
		0
		0
		0
		1

        Parameters
        ==========
        matrix  (List of string, Required) - The transformation matrix (4x4 list of numbers).
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        boolean - The transformed object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TransformObject
        """
        _rhino_id = _base._rsf.transform_object(self._rhino_id, matrix, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None
class _ObjectRootFunc(object):
    pass
class _ObjectRootGrps(object):

    def groups(self):
        """
        
        Returns all of the group names that an object is assigned.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of all group names for the object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectGroups
        """
        return _base._rsf.object_groups(self._rhino_id)

    def top_group(self):
        """
        
        Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - The top most group name of the object if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectTopGroup
        """
        return _base._rsf.object_top_group(self._rhino_id)
class _ObjectRootMdfy(object):

    def delete(self):
        """
        
        Deletes one or more objects from the document.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects deleted if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteObjects
        """
        return _base._rsf.delete_objects(self._rhino_id)
class _ObjectRootMtrl(object):

    def index(self):
        """
        
        Returns the material index of an object.
		Rendering materials are stored in Rhino's rendering material table.  This table is conceptually an array.  Render materials associated with objects and layers are specified by zero based indices into this array.
		If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material.  A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The rendering material index if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMaterialIndex
        """
        return _base._rsf.object_material_index(self._rhino_id)

    def source(self, source=pythoncom.Empty):
        """
        
        Returns or modifies the rendering material source of an object.
		Rendering materials are stored in Rhino's rendering material table.  This table is conceptually an array.  Render materials associated with objects and layers are specified by zero based indices into this array.
		The index of the render material used to render an object is specified in one of three ways:
		1. Material from layer.  The rendering material assigned to the layer is used.
		2. Material from object.  The rendering material assigned to the object is used.
		3. Material from parent.  For objects with parents, like objects in block instances, use parent's material. If no parent, treats as material from layer.
		The default rendering material source for new objects is "material by layer."

        Parameters
        ==========
        source  (integer, Optional) - The new rendering material source.  If omitted, the current material source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Material from layer
		1
		Material from object
		2
		<unused>
		3

        Returns
        =======
        number - If a rendering material source is not specified,  the current rendering material source if successful.
        number - If a rendering material source is specified, the previous rendering material source if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMaterialSource
        """
        return _base._rsf.object_material_source(self._rhino_id, source)
class _ObjectRootProp(object):

    def color(self, color=pythoncom.Empty):
        """
        
        Returns or modifies the color of an object.  Object colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters
        ==========
        color  (integer, Optional) - The new color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.

        Returns
        =======
        number - If a color value is not specified,  the current color value if successful.
        number - If a color value is specified, the previous color value if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectColor
        """
        return _base._rsf.object_color(self._rhino_id, color)

    def color_source(self, source=pythoncom.Empty):
        """
        
        Returns or modifies the color source of an object.   The color used to display objects is specified in one of four ways:
		1. Color from layer.  The object's layer determines the object's color.
		2. Color from object.  The object's color is set by the object itself.
		3. Color from material.  The object's diffuse material color determines the object's color.
		4. Color from parent. For objects with parents, like objects in block instances, use parent's color source. If no parent, treats as color from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new color source.  If omitted, the current color source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Color from layer
		1
		Color from object
		2
		Color from material
		3

        Returns
        =======
        number - If a color source is not specified,  the current color source if successful.
        number - If a color source is specified, the previous color source if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectColorSource
        """
        return _base._rsf.object_color_source(self._rhino_id, source)

    def layer(self, layer=pythoncom.Empty):
        """
        
        Returns or modifies the layer of an object.

        Parameters
        ==========
        layer  (Layer, Optional) - The name of an existing layer.  If omitted, the current object layer is returned.  Note, if arrObjects is specified, strLayer is required.

        Returns
        =======
        number - If a layer is not specified,  the object's current layer if successful.
        number - If a layer is specified, the object's previous layer if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectLayer
        """
        return _base._rsf.object_layer(self._rhino_id, layer._rhino_id)

    def linetype(self, layer=pythoncom.Empty):
        """
        
        Returns or modifies the linetype of an object.

        Parameters
        ==========
        layer  (Layer, Optional) - The name of an existing linetype.  If omitted, the current object linetype is returned.  Note, if arrObjects is specified, strLinetype is required.

        Returns
        =======
        number - If a linetype is not specified,  the object's current linetype if successful.
        number - If a linetype is specified, the object's previous linetype if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectLinetype
        """
        return _base._rsf.object_linetype(self._rhino_id, layer._rhino_id)

    def linetype_source(self, source=pythoncom.Empty):
        """
        
        Returns or modifies the linetype source of an object.   The linetype used to display objects is specified in one of three ways:
		1. Linetype from layer.  The object's layer determines the object's linetype.
		2. Linetype from object. The object's linetype is set by the object itself.
		3. Linetype from parent.  For objects with parents, like objects in block instances, use parent's linetype. If no parent, treats as linetype from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new linetype source.  If omitted, the current linetype source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Layer.  Use the object's layer linetype.
		1
		Object.  Use the object's linetype.
		2
		<unused>
		3

        Returns
        =======
        number - If a linetype source is not specified,  the current linetype source if successful.
        number - If a linetype source is specified, the previous linetype source if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectLinetypeSource
        """
        return _base._rsf.object_linetype_source(self._rhino_id, source)

    def name(self, names=pythoncom.Empty):
        """
        
        Returns or modifies the user-definable name of one or more objects.

        Parameters
        ==========
        names  (List of string, Optional) - An list of strings identifying the new user-definable names. This list must have the same upper bounds as arrObjects.  Each element in arrNames will correspond with each element in arrObjects.

        Returns
        =======
        list - If names is not specified,  the current object names if successful. Note, if an object does not have a user-definable name, it's corresponding element will be Null.
        list - If names is specified,  the previous object names if successful.  Note, if an object does not have a user-definable name, it's corresponding element will be Null.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectNames
        """
        return _base._rsf.object_names(self._rhino_id, names)

    def print_color(self, color=pythoncom.Empty):
        """
        
        Returns or modifies the print color of an object.  Object print colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters
        ==========
        color  (integer, Optional) - The new print color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.

        Returns
        =======
        number - If a print color value is not specified,  the current print color value if successful.
        number - If a print color value is specified, the previous print color value if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintColor
        """
        return _base._rsf.object_print_color(self._rhino_id, color)

    def print_color_source(self, source=pythoncom.Empty):
        """
        
        Returns or modifies the print color source of an object.  The color used to print objects is specified in one of four ways:
		1. Print color from layer.  Use the print color assigned to the object's layer.
		2. Print color from object.  Use the print color that is assigned to the object.
		3. Print color from display.  Use the object's display color.
		4. Print color from parent.  For objects with parents, like objects in block instances, use parent's print color.  If no parent, treats as print color from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new print color source.  If omitted, the current print color source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Print color by layer.
		1
		Print color by object.
		2
		Print color by display.
		3

        Returns
        =======
        number - If a print color source is not specified,  the current color source if successful.
        number - If a print color source is specified, the previous color source if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintColorSource
        """
        return _base._rsf.object_print_color_source(self._rhino_id, source)

    def print_width(self, width=pythoncom.Empty):
        """
        
        Returns or modifies the print width of an object.  Object print widths are measured in millimeters (mm).

        Parameters
        ==========
        width  (float, Optional) - The new print width value in millimeters, where dblWidth = 0.0 means use the default width, and dblWidth < 0.0 means do not print (visible for screen display, but does not show on print).  If omitted, the current object print width is returned.  Note, if arrObjects is specified, dblWidth is required.

        Returns
        =======
        number - If a print width value is not specified,  the current print width value if successful.
        number - If a print width value is specified, the previous print width value if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintWidth
        """
        return _base._rsf.object_print_width(self._rhino_id, width)

    def print_width_source(self, source=pythoncom.Empty):
        """
        
        Returns or modifies the print width source of an object.  The width used to print objects is specified in one of three ways:
		1. Print width from layer.  Use the print width assigned to the object's layer.
		2. Print width from object.  Use the print width that is assigned to the object.
		3. Print width from parent.  For objects with parents, like objects in block instances, use parent's print width.  If no parent, treats as print width from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new print width source.  If omitted, the current print width source is returned.  Note, if arrObjects is specified, intSource is required.
		Value
		Description
		0
		Print width by layer.
		1
		Print width by object.
		2
		<unused>
		3

        Returns
        =======
        number - If a print width source is not specified,  the current width source if successful.
        number - If a print width source is specified, the previous width source if successful.
        number - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintWidthSource
        """
        return _base._rsf.object_print_width_source(self._rhino_id, source)
class _ObjectRootRndr(object):

    def add_mesh(self, quality=pythoncom.Empty, enable=pythoncom.Empty):
        """
        
        Adds custom render mesh parameters to a meshable object, such as a surface or a polysurface.  If an object has custom render mesh parameters and they are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        quality  (integer, Optional) - The initial settings of the new custom render mesh parameters. The available options are as follows:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)
        enable  (boolean, Optional) - Enable the custom render mesh parameters.  If omitted, the newly added parameters will be enabled (True).

        Returns
        =======
        boolean - If enable is not specified, then the current enabled/disabled state if successful.
        boolean - If enable is not specified, then the current enabled/disabled state if successful.
        None - If the object does not have custom render mesh parameters, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddObjectMesh
        """
        return _base._rsf.add_object_mesh(self._rhino_id, quality, enable)

    def enable(self, enable=pythoncom.Empty):
        """
        
        Enables or disables an object's custom render mesh parameters. If an object's custom render mesh parameters are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        enable  (boolean, Optional) - Enable the custom render mesh settings.

        Returns
        =======
        boolean - If enable is not specified, then the current enabled/disabled state if successful.
        boolean - If enable is not specified, then the current enabled/disabled state if successful.
        None - If the object does not have custom render mesh parameters, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EnableObjectMesh
        """
        return _base._rsf.enable_object_mesh(self._rhino_id, enable)

    def has_mesh(self):
        """
        
        Verifies that an object has custom render mesh parameters.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True of the object has custom render mesh parameters, False otherwise.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectHasMesh
        """
        return _base._rsf.object_has_mesh(self._rhino_id)

    def density(self, density=pythoncom.Empty):
        """
        
        Returns or modifies an object's custom render mesh parameter's mesh density property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        density  (float, Optional) - The render mesh density, which is a number between 0.0 and 1.0.

        Returns
        =======
        boolean - If density is not specified, the current render mesh density if successful.
        boolean - If density is specified, the previous render mesh density if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshDensity
        """
        return _base._rsf.object_mesh_density(self._rhino_id, density)

    def max_angle(self, angle=pythoncom.Empty):
        """
        
        Returns or modifies an object's custom render mesh parameter's maximum angle property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        angle  (float, Optional) - The render mesh maximum angle in degrees.

        Returns
        =======
        boolean - If angle is not specified, the current render mesh maximum angle if successful.
        boolean - If angle is specified, the previous render mesh maximum angle if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshMaxAngle
        """
        return _base._rsf.object_mesh_max_angle(self._rhino_id, angle)

    def max_aspect_ratio(self, ratio=pythoncom.Empty):
        """
        
        Returns or modifies an object's custom render mesh parameter's maximum aspect ratio property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        ratio  (float, Optional) - The render mesh maximum aspect ratio.  The suggested range, when not zero, is from 1 to 100.

        Returns
        =======
        boolean - If ratio is not specified, the current render mesh maximum aspect ratio if successful.
        boolean - If ratio is specified, the previous render mesh maximum aspect ratio if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshMaxAspectRatio
        """
        return _base._rsf.object_mesh_max_aspect_ratio(self._rhino_id, ratio)

    def max_dist_edge_to_srf(self, distance=pythoncom.Empty):
        """
        
        Returns or modifies an object's custom render mesh parameter's maximum distance, edge to surface property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        distance  (float, Optional) - The render mesh maximum distance, edge to surface.

        Returns
        =======
        boolean - If distance is not specified, the current render mesh maximum distance, edge to surface if successful.
        boolean - If distance is specified, the previous render mesh maximum distance, edge to surface if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshMaxDistEdgeToSrf
        """
        return _base._rsf.object_mesh_max_dist_edge_to_srf(self._rhino_id, distance)

    def max_edge_length(self, length=pythoncom.Empty):
        """
        
        Returns or modifies an object's custom render mesh parameter's maximum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        length  (float, Optional) - The render mesh maximum edge length.

        Returns
        =======
        boolean - If length is not specified, the current render mesh maximum edge length if successful.
        boolean - If length is specified, the previous render mesh maximum edge length if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshMaxEdgeLength
        """
        return _base._rsf.object_mesh_max_edge_length(self._rhino_id, length)

    def min_edge_length(self, length=pythoncom.Empty):
        """
        
        Returns or modifies an object's custom render mesh parameter's minimum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        length  (float, Optional) - The render mesh minimum edge length.

        Returns
        =======
        boolean - If length is not specified, the current render mesh minimum edge length if successful.
        boolean - If length is specified, the previous render mesh minimum edge length if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshMinEdgeLength
        """
        return _base._rsf.object_mesh_min_edge_length(self._rhino_id, length)

    def min_initial_grid_quads(self, quads=pythoncom.Empty):
        """
        
        Returns or modifies an object's custom render mesh parameter's minimum initial grid quads property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        quads  (integer, Optional) - The render mesh minimum initial grid quads.  The suggested range is from 0 to 10000.

        Returns
        =======
        boolean - If quads is not specified, the current render mesh minimum initial grid quads if successful.
        boolean - If quads is specified, the previous render mesh minimum initial grid quads if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshMinInitialGridQuads
        """
        return _base._rsf.object_mesh_min_initial_grid_quads(self._rhino_id, quads)

    def quality(self, quality=pythoncom.Empty):
        """
        
        Returns or sets the render mesh quality of an object's custom render mesh parameters.

        Parameters
        ==========
        quality  (integer, Optional) - The render mesh quality, either:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)

        Returns
        =======
        boolean - If quality is not specified, the current render mesh quality if successful.
        boolean - If quality is specified, the previous render mesh quality if successful.
        None - If the object does not have custom render mesh parameters, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshQuality
        """
        return _base._rsf.object_mesh_quality(self._rhino_id, quality)

    def settings(self, settings=pythoncom.Empty):
        """
        
        Returns or sets the render mesh settings of an object's custom render mesh parameters.

        Parameters
        ==========
        settings  (integer, Optional) - The render mesh settings, which is a bit-coded number that allows or disallows certain features.  The bits can be added together in any combination to form a value between 0 and 15.  The bit values are as follows:
		Value
		Description
		0
		No settings enabled.
		1
		Refine mesh enabled.
		2
		Jagged seams enabled.
		4
		Simple planes enabled.
		8

        Returns
        =======
        boolean - If settings is not specified, the current render mesh settings if successful.
        boolean - If settings is specified, the previous render mesh settings if successful.
        None - If the object does not have custom render mesh parameters, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshSettings
        """
        return _base._rsf.object_mesh_settings(self._rhino_id, settings)
class _ObjectRootStat(object):

    def flash(self, style=pythoncom.Empty):
        """
        
        Causes the selection state of one or more objects to change momentarily so the object appears to flash on the screen.

        Parameters
        ==========
        style  (boolean, Optional) - The flash style.  If True (default), then the objects will flash between their object color and Rhino's selected object color.  If false, then the objects will flash between invisible and visible.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: FlashObject
        """
        return _base._rsf.flash_object()

    def hide(self):
        """
        
        Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects hidden if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: HideObjects
        """
        return _base._rsf.hide_objects(self._rhino_id)

    def lock(self):
        """
        
        Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects locked if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LockObjects
        """
        return _base._rsf.lock_objects(self._rhino_id)

    def match_object_attributes(self, targets):
        """
        
        Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.

        Parameters
        ==========
        targets  (list of array_of _ObjectRoot, Required) - A list of target objects.

        Returns
        =======
        number - The number of objects whose attributes were modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MatchObjectAttributes
        """
        if type(targets) != list and type(targets) != tuple:
            targets = (targets,)
        return _base._rsf.match_object_attributes(map(lambda i: i._rhino_id, targets), self._rhino_id)

    def reset_object_attributes(self):
        """
        
        Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects whose attributes were modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MatchObjectAttributes
        """
        return _base._rsf.match_object_attributes(self._rhino_id, pythoncom.Empty)

    def move_to_layout_space(self, layout=pythoncom.Empty, return_name=pythoncom.Empty):
        """
        
        Returns or changes the layout or model space of an object.

        Parameters
        ==========
        layout  (string, Optional) - To change, or move, an object from model space to page layout space, or from one page layout to another, then specify the title or identifier of an existing page layout view. To move an object from page layout space to model space, just specify Null.
        return_name  (boolean, Optional) - If True (default), then the name, or title, of the page layout view is returned. If False, then the identifier of the page layout view is returned.

        Returns
        =======
        string - If layout is not specified,  the object's current page layout view if successful. Note, if the object is not in page layout space, Null is returned.
        string - If layout  is specified, the object's previous page layout view if successful. Note, if the object was not in page layout space, Null is returned.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectLayout
        """
        return _base._rsf.object_layout(self._rhino_id, layout, return_name)

    def select(self):
        """
        
        Selects one or more objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects selected if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SelectObjects
        """
        return _base._rsf.select_objects(self._rhino_id)

    def show(self):
        """
        
        Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects shown if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ShowObjects
        """
        return _base._rsf.show_objects(self._rhino_id)

    def unlock(self):
        """
        
        Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects unlocked if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnlockObjects
        """
        return _base._rsf.unlock_objects(self._rhino_id)

    def unselect(self):
        """
        
        Unselects one or more selected objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of objects unselected if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnselectObjects
        """
        return _base._rsf.unselect_objects(self._rhino_id)
class _ObjectRootTest(object):

    def is_in_layout_space(self):
        """
        
        Verifies that an object is in either page layout space or model space.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayoutObject
        """
        return _base._rsf.is_layout_object(self._rhino_id)

    def is_hidden(self):
        """
        
        Verifies that an object is hidden.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectHidden
        """
        return _base._rsf.is_object_hidden(self._rhino_id)

    def is_in_box(self, box, mode=pythoncom.Empty):
        """
        
        Verifies an object's bounding box is inside of another bounding box.

        Parameters
        ==========
        box  (List of float, Required) - The bounding box to test against. A bounding box is an list of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
        mode  (boolean, Optional) - The test mode.
		Value
		Description
		True (Default)
		The object's bounding box must be contained by the test bounding box. In other words, test.min <= object.min and object.max <= test.max.
		False

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectInBox
        """
        return _base._rsf.is_object_in_box(self._rhino_id, box, mode)

    def is_in_group(self, group=pythoncom.Empty):
        """
        
        Verifies that an object is a member of a specified group.

        Parameters
        ==========
        group  (string, Optional) - The name of a group.  If omitted, the function verifies that the object is a member of any group.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectInGroup
        """
        return _base._rsf.is_object_in_group(self._rhino_id, group)

    def is_locked(self):
        """
        
        Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectLocked
        """
        return _base._rsf.is_object_locked(self._rhino_id)

    def is_normal(self):
        """
        
        Verifies that an object is normal.  Normal objects are visible, can be snapped to, and can be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectNormal
        """
        return _base._rsf.is_object_normal(self._rhino_id)

    def is_reference(self):
        """
        
        Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectReference
        """
        return _base._rsf.is_object_reference(self._rhino_id)

    def is_selectable(self):
        """
        
        Verifies that an object is selectable.  Objects that are locked, hidden, or on locked or hidden layers cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectSelectable
        """
        return _base._rsf.is_object_selectable(self._rhino_id)

    def is_selected(self):
        """
        
        Verifies that an object is currently selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectSelected
        """
        return _base._rsf.is_object_selected(self._rhino_id)

    def is_solid(self):
        """
        
        Verifies that an object is a closed, solid object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectSolid
        """
        return _base._rsf.is_object_solid(self._rhino_id)

    def is_valid(self):
        """
        
        Verifies that an object's geometry is valid and without error.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectValid
        """
        return _base._rsf.is_object_valid(self._rhino_id)

    def is_visible_in_view(self, view=pythoncom.Empty):
        """
        
        Verifies that an object is visible in a view.

        Parameters
        ==========
        view  (string, Optional) - The title of the view.  If omitted, the current active view is used.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVisibleInView
        """
        return _base._rsf.is_visible_in_view(self._rhino_id, view)
class _ObjectRootTrfm(object):

    def mirror(self, start_point, end_point, copy=pythoncom.Empty):
        """
        
        Mirrors a single object.

        Parameters
        ==========
        start_point  (List of float, Required) - The start of the mirror plane.
        end_point  (List of float, Required) - The end of the mirror plane.
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        string - The mirrored object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MirrorObject
        """
        _rhino_id = _base._rsf.mirror_object(self._rhino_id, start_point, end_point, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move(self, start_point, end_point):
        """
        
        Moves a single object.

        Parameters
        ==========
        start_point  (List of float, Required) - The 3-D starting, or base, point of the move operation.
        end_point  (List of float, Required) - The 3-D ending point of the move operation.

        Returns
        =======
        boolean - The moved object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MoveObject
        """
        _rhino_id = _base._rsf.move_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def move_by_vec(self, translation_vector):
        """
        
        Moves a single object.

        Parameters
        ==========
        translation_vector  (List of float, Required) - The 3-D translation vector.

        Returns
        =======
        boolean - The moved object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MoveObject2
        """
        _rhino_id = _base._rsf.move_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def orient(self, reference, target, flags=pythoncom.Empty):
        """
        
        Orients a single object based on input points.

        Parameters
        ==========
        reference  (List of float, Required) - An list of 3-D reference points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
        target  (List of float, Required) - An list of 3-D target points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
        flags  (integer, Optional) - The orient flags.  Values can be added together to specify multiple options.
		Value
		Description
		1
		Copy object.  The default is not to copy the object.
		2

        Returns
        =======
        string - The oriented object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OrientObject
        """
        _rhino_id = _base._rsf.orient_object(self._rhino_id, reference, target, flags)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def remap(self, src_plane, dst_plane, copy=pythoncom.Empty):
        """
        
        Remqps a single object from one plane, or coordinate system, to another.

        Parameters
        ==========
        src_plane  (List of float, Required) - The source plane to transform from.
        dst_plane  (List of float, Required) - The destination plane to transform to.
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        string - The remapped object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RemapObject
        """
        _rhino_id = _base._rsf.remap_object(self._rhino_id, src_plane, dst_plane, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def rotate(self, point, angle, axis=pythoncom.Empty, copy=pythoncom.Empty):
        """
        
        Rotates a single object. Rotation is based on the active construction plane.

        Parameters
        ==========
        point  (List of float, Required) - The 3-D center point of the rotation.
        angle  (float, Required) - The rotation angle in degrees.
        axis  (List of float, Optional) - A 3-D vector that identifies the axis of rotation. If omitted, the Z axis of the active construction plane is used as the rotation axis.
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        string - The rotated object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RotateObject
        """
        _rhino_id = _base._rsf.rotate_object(self._rhino_id, point, angle, axis, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None

    def scale(self, origin, scale, copy=pythoncom.Empty):
        """
        
        Scales a single object. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.

        Parameters
        ==========
        origin  (List of float, Required) - The origin of the scale transformation.
        scale  (List of float, Required) - An list of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply. Scaling is based on the active construction plane.
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        string - The scaled object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ScaleObject
        """
        _rhino_id = _base._rsf.scale_object(self._rhino_id, origin, scale, copy)
        if _rhino_id:
            return self._class(_rhino_id)
        else:
            return None
class _ObjectRootType(object):

    def object_type(self):
        """
        
        Returns the object type.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The object type if successful.  The valid object types are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectType
        """
        return _base._rsf.object_type(self._rhino_id)
class _ObjectRootUtil(object):

    def description(self):
        """
        
        Returns a short text description of an object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - A short text description of the object is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectDescription
        """
        return _base._rsf.object_description(self._rhino_id)

    def dump(self, type=pythoncom.Empty):
        """
        
        Returns a detailed description of an object.

        Parameters
        ==========
        type  (integer, Optional) - The acceptable values are as follows:
		Value
		Description
		0 (Default)
		Returns both geometry and attribute details. This is equivalent to the results of the What command.
		1
		Returns geometry details.
		2
		Returns attribute details.
		3

        Returns
        =======
        string - A detailed description of the object is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectDump
        """
        return _base._rsf.object_dump(self._rhino_id, type)
class _PlanarMeshDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.PlanarMesh(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.PlanarMesh(_rhino_id)
        else:
            return None

    def copy_by_offset(self, mesh, distance):
        """
        
        Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.

        Parameters
        ==========
        mesh  (mesh object, Required) - The identifier of a mesh object.
        distance  (float, Required) - The distance to offset.

        Returns
        =======
        object - The offset mesh object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshOffset
        """
        _rhino_id = _base._rsf.mesh_offset(mesh._rhino_id, distance)
        if _rhino_id:
            return p2r.obj.PlanarMesh(_rhino_id)
        else:
            return None
class _PlaneSurfaceDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.PlaneSurface(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.PlaneSurface(_rhino_id)
        else:
            return None

    def copy_by_offset(self, distance):
        """
        
        Offsets a surface by a distance. The offset surface will be added to Rhino.

        Parameters
        ==========
        distance  (float, Required) - The distance to offset.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetSurface
        """
        _rhino_id = _base._rsf.offset_surface(self._rhino_id, distance)
        if _rhino_id:
            return _util.cast(_rhino_id)
        else:
            return None
class _PolyCurveDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.PolyCurve(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.PolyCurve(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.PolyCurve(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.PolyCurve(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolyCurve(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.PolyCurve(_rhino_id)
        else:
            return None
class _PolySurfaceDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.PolySurface(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.PolySurface(_rhino_id)
        else:
            return None
class _PolylineDupl(object):

    def copy_by_sub(self, param_0, param_1):
        """
        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters
        ==========
        param_0  (float, Required) - The first parameter on the source curve.
        param_1  (float, Required) - The second parameter on the source curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSubCrv
        """
        _rhino_id = _base._rsf.add_sub_crv(self._rhino_id, param_0, param_1)
        if _rhino_id:
            return p2r.obj.Polyline(_rhino_id)
        else:
            return None

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Polyline(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Polyline(_rhino_id)
        else:
            return None

    def copy_by_offset(self, direction_point, distance, normal=pythoncom.Empty, style=pythoncom.Empty):
        """
        
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
		Value
		Description
		0
		None
		1
		Sharp (Default)
		2
		Round
		3
		Smooth
		4

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve
        """
        _rhino_id = _base._rsf.offset_curve(self._rhino_id, direction_point, distance, normal, style)
        if _rhino_id:
            return p2r.obj.Polyline(_rhino_id)
        else:
            return None

    def copy_by_split(self, parameters, delete=pythoncom.Empty):
        """
        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

        Parameters
        ==========
        parameters  (List of float, Required) - An list of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the two newly created curve objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitCurve
        """
        _rhino_ids = _base._rsf.split_curve(self._rhino_id, parameters, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Polyline(i), _rhino_ids)
        else:
            return None

    def copy_by_trim(self, interval, delete=pythoncom.Empty):
        """
        
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve
        """
        _rhino_id = _base._rsf.trim_curve(self._rhino_id, interval, delete)
        if _rhino_id:
            return p2r.obj.Polyline(_rhino_id)
        else:
            return None
class _SphereDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Sphere(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Sphere(_rhino_id)
        else:
            return None
class _SurfaceRootEval(object):

    def evaluate(self, parameter):
        """
        
        Evaluates a surface at a U,V parameter.

        Parameters
        ==========
        parameter  (List of float, Required) - An list containing the U,V parameter to evaluate.

        Returns
        =======
        list - A 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EvaluateSurface
        """
        return _base._rsf.evaluate_surface(self._rhino_id, parameter)

    def evaluate_derivatives(self, parameter, derivative):
        """
        
        A general purpose surface evaluator.

        Parameters
        ==========
        parameter  (List of float, Required) - An list containing the U,V parameter to evaluate.
        derivative  (integer, Required) - The number of derivatives to evaluate.

        Returns
        =======
        list - A list of length (derivative+1)*(derivative+2)/2 if successful.  The list elements are as follows:
        list - The 3-D point.
        list - The first derivative.
        list - The first derivative.
        list - The second derivative.
        list - The second derivative.
        list - The second derivative.
        list - etc...
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceEvaluate
        """
        return _base._rsf.surface_evaluate(self._rhino_id, parameter, derivative)

    def evaluate_frame(self, parameter):
        """
        
        Returns a plane based on the normal, u, and v directions at a given surface U,V parameter.

        Parameters
        ==========
        parameter  (List of float, Required) - An list containing the U,V parameter to evaluate.

        Returns
        =======
        list - The plane at the specified parameter if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceFrame
        """
        return _base._rsf.surface_frame(self._rhino_id, parameter)
class _TorusDupl(object):

    def copy_move(self, start_point=pythoncom.Empty, end_point=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        start_point  (List of float, Optional) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
        end_point  (List of float, Optional) - The 3-D ending point of the copy operation.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject
        """
        _rhino_id = _base._rsf.copy_object(self._rhino_id, start_point, end_point)
        if _rhino_id:
            return p2r.obj.Torus(_rhino_id)
        else:
            return None

    def copy_move_by_vec(self, translation_vector=pythoncom.Empty):
        """
        
        Copies a single object from one location to another, or in-place.

        Parameters
        ==========
        translation_vector  (List of float, Optional) - The 3-D translation vector.

        Returns
        =======
        object - The copied object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CopyObject2
        """
        _rhino_id = _base._rsf.copy_object_2(self._rhino_id, translation_vector)
        if _rhino_id:
            return p2r.obj.Torus(_rhino_id)
        else:
            return None
class _ArcProp(_CurveRootProp):

    def angle(self):
        """
        
        Returns the angle of an arc curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The angle in degrees if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ArcAngle
        """
        return _base._rsf.arc_angle(self._rhino_id, pythoncom.Empty)

    def center_pnt(self):
        """
        
        Returns the center point of an arc curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ArcCenterPoint
        """
        return _base._rsf.arc_center_point(self._rhino_id, pythoncom.Empty)

    def mid_pnt(self):
        """
        
        Returns the mid point of an arc curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ArcMidPoint
        """
        return _base._rsf.arc_mid_point(self._rhino_id, pythoncom.Empty)

    def radius(self):
        """
        
        Returns the radius of an arc curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The radius of the arc if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ArcRadius
        """
        return _base._rsf.arc_radius(self._rhino_id, pythoncom.Empty)
class _CircleProp(_CurveRootProp):

    def center_pnt(self):
        """
        
        Returns the center point of a circle curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The 3-D center point of the circle if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CircleCenterPoint
        """
        return _base._rsf.circle_center_point(self._rhino_id, pythoncom.Empty)

    def circumference(self):
        """
        
        Returns the circumference of a circle curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The circumference of the circle if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CircleCircumference
        """
        return _base._rsf.circle_circumference(self._rhino_id, pythoncom.Empty)

    def radius(self):
        """
        
        Returns the radius of a circle curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The radius of the circle if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CircleRadius
        """
        return _base._rsf.circle_radius(self._rhino_id, pythoncom.Empty)
class _CurveRoot(_ObjectRoot):
    pass
class _CurveRootFunc(_ObjectRootFunc):

    def crv_arc_length_pnt(self, length, from_start=pythoncom.Empty):
        """
        
        Returns the point on the curve that is a specified arc length from the start of the curve.

        Parameters
        ==========
        length  (float, Required) - The arc length from the start of the curve to evaluate.
        from_start  (boolean, Optional) - If not specified or True, then the arc length point is calculated from the start of the curve. If False, the arc length point is calculated from the end of the curve.

        Returns
        =======
        list - The 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveArcLengthPoint
        """
        return _base._rsf.curve_arc_length_point(self._rhino_id, length, from_start)

    def closest_pnt(self, point):
        """
        
        Returns the parameter of the point on a curve that is closest to a test point.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        number - The parameter of the closest point on the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveClosestPoint
        """
        return _base._rsf.curve_closest_point(self._rhino_id, point, pythoncom.Empty)

    def contour_pnts(self, start_point, end_point, interval=pythoncom.Empty):
        """
        
        Returns the 3-D point locations calculated by contouring a curve object.

        Parameters
        ==========
        start_point  (List of float, Required) - The 3-D starting point of a center line.
        end_point  (List of float, Required) - The 3-D ending point of a center line.
        interval  (float, Optional) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.

        Returns
        =======
        list - A list of 3-D points, one for each contour, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveContourPoints
        """
        return _base._rsf.curve_contour_points(self._rhino_id, start_point, end_point, interval)

    def crv_intersection(self, curve=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        
        Calculates the intersection of two curve objects.

        Parameters
        ==========
        curve  (curve object, Optional) - The identifier of the second curve object.  If omitted, the a self-intersection test will be performed on strObject1.
        tolerance  (float, Optional) - The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.

        Returns
        =======
        list - A two-dimensional list of intersection information if successful.  The list will contain one or more of the following elements:
        number - The intersection event type, either Point (1) or Overlap (2).
        number - If the event type is Point (1), then the first curve parameter.
        number - If the event type is Point (1), then the first curve parameter.
        number - If the event type is Point (1), then the second curve parameter.
        number - If the event type is Point (1), then the second curve parameter.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveCurveIntersection
        """
        return _base._rsf.curve_curve_intersection(self._rhino_id, curve._rhino_id, tolerance)

    def deviation(self, curve):
        """
        
        Returns the minimum and maximum deviation between two curve objects. For more information on curve deviation, see the Rhino help file for the CrvDeviation command.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the second curve object.

        Returns
        =======
        list - A list of numbers identifying the minimum and maximum deviation between the two curves if successful.
        number - Curve A parameter at maximum overlap distance point
        number - Curve A parameter at maximum overlap distance point
        number - Maximum overlap distance
        number - Curve A parameter at minimum distance point
        number - Curve B parameter at minimum distance point
        number - Minimum distance between curves
        None - On error or if no intervals of overlap were found.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDeviation
        """
        return _base._rsf.curve_deviation(self._rhino_id, curve._rhino_id)

    def directions_match(self, curve):
        """
        
        Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the second curve to compare.

        Returns
        =======
        boolean - True if the curve directions match, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDirectionsMatch
        """
        return _base._rsf.curve_directions_match(self._rhino_id, curve._rhino_id)

    def radius(self, point):
        """
        
        Returns the radius of curvature at a point on a curve.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        number - The radius of curvature at the point on the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveRadius
        """
        return _base._rsf.curve_radius(self._rhino_id, point, pythoncom.Empty)

    def srf_intersection(self, surface, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        """
        
        Calculates the intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of a surface object.
        tolerance  (float, Optional) - The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
        angle_tolerance  (float, Optional) - The angle tolerance in degrees.  The angle tolerance is used to determine when the curve is tangent to the surface.  If omitted, the document's current angle tolerance is used.

        Returns
        =======
        list - A two-dimensional list of intersection information if successful.  The list will contain one or more of the following elements:
        number - The intersection event type, either Point (1) or Overlap (2).
        number - If the event type is Point (1), then the curve parameter.
        number - If the event type is Point (1), then the curve parameter.
        number - If the event type is Point (1), then the U surface parameter.
        number - If the event type is Point (1), then the V surface parameter.
        number - If the event type is Point (1), then the U surface parameter.
        number - If the event type is Point (1), then the V surface parameter.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveSurfaceIntersection
        """
        return _base._rsf.curve_surface_intersection(self._rhino_id, surface._rhino_id, tolerance, angle_tolerance)

    def divide_crv(self, segments, create=pythoncom.Empty, points=pythoncom.Empty):
        """
        
        Divides a curve object into a specified number of segments.

        Parameters
        ==========
        segments  (integer, Required) - The number of segments.
        create  (boolean, Optional) - Create the division points. If omitted or False, points are not created.
        points  (boolean, Optional) - Return an list of 3-D points. If omitted or True, points are returned. If False, then an list of curve parameters are returned.

        Returns
        =======
        list - If points is not specified or True, then a list containing 3-D division points if successful.
        list - If points is False, then a list containing division curve parameters if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DivideCurve
        """
        return _base._rsf.divide_curve(self._rhino_id, segments, create, points)

    def divide_crv_equidistant(self, distance, create=pythoncom.Empty, points=pythoncom.Empty):
        """
        
        Divides a curve such that the linear distance between the points is equal.
		Unlike the DivideCurve and DivideCurveLength, which divides a curve based on arc length, or the distance along the curve between two points, this function divides a curve based on the linear distance between points.

        Parameters
        ==========
        distance  (float, Required) - The linear distance between division points.
        create  (boolean, Optional) - Create the division points. If omitted or False, points are not created.
        points  (boolean, Optional) - Return an list of 3-D points. If omitted or True, points are returned. If False, then an list of curve parameters are returned.

        Returns
        =======
        list - If points is not specified or True, then a list containing 3-D division points if successful.
        list - If points is False, then a list containing division curve parameters if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DivideCurveEquidistant
        """
        return _base._rsf.divide_curve_equidistant(self._rhino_id, distance, create, points)

    def divide_crv_length(self, length, create=pythoncom.Empty, points=pythoncom.Empty):
        """
        
        Divides a curve object into segments of a specified length.

        Parameters
        ==========
        length  (float, Required) - The length of each segment.
        create  (boolean, Optional) - Create the division points. If omitted or False, points are not created.
        points  (boolean, Optional) - Return an list of 3-D points. If omitted or True, points are returned. If False, then an list of curve parameters are returned.

        Returns
        =======
        list - If points is not specified or True, then a list containing 3-D division points if successful.
        list - If points is False, then a list containing division curve parameters if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DivideCurveLength
        """
        return _base._rsf.divide_curve_length(self._rhino_id, length, create, points)

    def line_fit_from_pnts(self):
        """
        
        Returns the starting and ending points of a line that was fit through an array of 3-D points.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing the starting and ending points of the fit line if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LineFitFromPoints
        """
        return _base._rsf.line_fit_from_points(self._rhino_id)

    def make_non_periodic(self):
        """
        
        Makes a periodic curve non-periodic.  Non-periodic curves can develop kinks when deformed.

        Parameters
        ==========
        No parameters

        Returns
        =======
        object - If delete is False, the new object if successful.
        object - If delete is True, the modified object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MakeCurveNonPeriodic
        """
        _rhino_id = _base._rsf.make_curve_non_periodic(self._rhino_id, False)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def make_periodic(self):
        """
        
        Makes an existing curve a periodic NURBS curve.  A periodic NURBS curve is a closed curve with a simple knot at the seam.  If a joined curve is made periodic, it becomes a single-span curve and can no longer be exploded.

        Parameters
        ==========
        No parameters

        Returns
        =======
        object - If delete is False, the new object if successful.
        object - If delete is True, the modified object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MakeCurvePeriodic
        """
        _rhino_id = _base._rsf.make_curve_periodic(self._rhino_id, False)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def planar_crv_collision(self, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        
        Determines if two coplanar curves intersect.

        Parameters
        ==========
        curve  (curve object, Required) - The object identifier of the second planar curve.
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are as follows:
		Element
		Type
		Description
		0
		Array
		Required.  The construction plane's origin (3-D point).
		1
		Array
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Array
		Required.  The construction plane's Y axis direction (3-D vector).
		3
		Array
        tolerance  (float, Optional) - The tolerance.  If omitted, the current document absolute tolerance is used.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlanarCurveCollision
        """
        return _base._rsf.planar_curve_collision(self._rhino_id, curve._rhino_id, plane, tolerance)
class _CurveRootFuncClsd(_CurveRootFunc):

    def area(self, objects):
        """
        
        Returns that area of closed planar curves. The results are based on the current drawing units.

        Parameters
        ==========
        objects  (list of array_of _ObjectRoot, Required) - An list of strings containing the identifiers of one or more closed, planar curve objects.

        Returns
        =======
        list - A list of area information if successful.  The list will contain the following information:
        number - The area. If more than one curve was specified, the value will be the cumulative area.
        number - The absolute (+/-) error bound for the area.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveArea
        """
        if type(objects) != list and type(objects) != tuple:
            objects = (objects,)
        return _base._rsf.curve_area(map(lambda i: i._rhino_id, objects))

    def area_centroid(self, objects):
        """
        
        Returns that area centroid of closed, planar curves. The results are based on the current drawing units.

        Parameters
        ==========
        objects  (list of array_of _ObjectRoot, Required) - An list of strings containing the identifiers of one or more closed, planar curve objects.

        Returns
        =======
        list - A list of area centroid information if successful.  The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveAreaCentroid
        """
        if type(objects) != list and type(objects) != tuple:
            objects = (objects,)
        return _base._rsf.curve_area_centroid(map(lambda i: i._rhino_id, objects))

    def boolean_difference(self, curve):
        """
        
        Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the second curve object.

        Returns
        =======
        list of objects - The identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveBooleanDifference
        """
        _rhino_ids = _base._rsf.curve_boolean_difference(self._rhino_id, curve._rhino_id)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolyCurve(i), _rhino_ids)
        else:
            return None

    def boolean_intersection(self, curve):
        """
        
        Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the second curve object.

        Returns
        =======
        list of objects - The identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveBooleanIntersection
        """
        _rhino_ids = _base._rsf.curve_boolean_intersection(self._rhino_id, curve._rhino_id)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolyCurve(i), _rhino_ids)
        else:
            return None

    def boolean_union(self, curves):
        """
        
        Calculates the union of two or more closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters
        ==========
        curves  (list of curve object, Required) - The identifiers of two or more curve objects.

        Returns
        =======
        list of objects - The identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveBooleanUnion
        """
        if type(curves) != list and type(curves) != tuple:
            curves = (curves,)
        _rhino_ids = _base._rsf.curve_boolean_union(map(lambda i: i._rhino_id, curves))
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolyCurve(i), _rhino_ids)
        else:
            return None

    def containment(self, curve, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        
        Determines the relationship between the regions bounded by two coplanar simple closed curves.

        Parameters
        ==========
        curve  (curve object, Required) - The object identifier of the second planar, closed curve.
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are as follows:
		Element
		Type
		Description
		0
		Array
		Required.  The construction plane's origin (3-D point).
		1
		Array
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Array
		Required.  The construction plane's Y axis direction (3-D vector).
		3
		Array
        tolerance  (float, Optional) - The tolerance.  If omitted, the current document absolute tolerance is used.

        Returns
        =======
        number - A number identifying the relationship if successful.  The possible values are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlanarClosedCurveContainment
        """
        return _base._rsf.planar_closed_curve_containment(self._rhino_id, curve._rhino_id, plane, tolerance)

    def pnt_inside(self, point, plane=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        
        Determines if a point is inside of a closed curve, on  a closed curve, or outside of a closed curve.

        Parameters
        ==========
        point  (List of float, Required) - A 3-D point to test.
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are as follows:
		Element
		Type
		Description
		0
		Array
		Required.  The construction plane's origin (3-D point).
		1
		Array
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Array
		Required.  The construction plane's Y axis direction (3-D vector).
		3
		Array
        tolerance  (float, Optional) - The tolerance.  If omitted, the current document absolute tolerance is used.

        Returns
        =======
        number - A number identifying the result if successful.  The possible values are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointInPlanarClosedCurve
        """
        return _base._rsf.point_in_planar_closed_curve(point, self._rhino_id, plane, tolerance)
class _CurveRootFuncOpen(_CurveRootFunc):

    def close(self, tolerance=pythoncom.Empty):
        """
        
        Closes an open curve object by making adjustments to the end points so that they meet at a point.

        Parameters
        ==========
        tolerance  (float, Optional) - The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.

        Returns
        =======
        object - The closed curve object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CloseCurve
        """
        _rhino_id = _base._rsf.close_curve(self._rhino_id, tolerance)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def extend(self, crv_type, side, objects):
        """
        
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension.
		Value
		Description
		0
		Line - Creates an line extension tangent to the original curve.
		1
		Arc - Creates an arc extension tangent to the original curve.
		2
        side  (integer, Required) - The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
        objects  (list of array_of _ObjectRoot, Required) - The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurve
        """
        if type(objects) != list and type(objects) != tuple:
            objects = (objects,)
        _rhino_id = _base._rsf.extend_curve(self._rhino_id, crv_type, side, map(lambda i: i._rhino_id, objects))
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def extend_length(self, crv_type, side, length):
        """
        
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension.
		Value
		Description
		0
		Line - Creates an line extension tangent to the original curve.
		1
		Arc - Creates an arc extension tangent to the original curve.
		2
        side  (integer, Required) - The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
		Extend from the end of the curve.
		2
        length  (float, Required) - The distance to extend the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurveLength
        """
        _rhino_id = _base._rsf.extend_curve_length(self._rhino_id, crv_type, side, length)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None

    def extend_pnt(self, side, point):
        """
        
        Extends a non-closed curve object by smooth extension to a point.

        Parameters
        ==========
        side  (integer, Required) - The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
        point  (List of float, Required) - The 3-D point.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurvePoint
        """
        _rhino_id = _base._rsf.extend_curve_point(self._rhino_id, side, point)
        if _rhino_id:
            return p2r.obj.NurbsCurve(_rhino_id)
        else:
            return None
class _CurveRootMdfy(_ObjectRootMdfy):

    def seam(self, parameter):
        """
        
        Adjusts the seam, or start/end, point of a closed curve.

        Parameters
        ==========
        parameter  (float, Required) - The parameter of the new start/end point. Note, if successful, the resulting curve's domain will start at dblParameter.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveSeam
        """
        return _base._rsf.curve_seam(self._rhino_id, parameter)

    def fair(self, tolerance=pythoncom.Empty):
        """
        
        Fairs a curve object. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvature variations while limiting the geometry changes to be no more than the specified tolerance. Sometimes several applications of this method are necessary to remove nasty curvature problems.

        Parameters
        ==========
        tolerance  (float, Optional) - The fairing tolerance. Of omitted, a default value of 1.0 is used.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: FairCurve
        """
        return _base._rsf.fair_curve(self._rhino_id, tolerance)

    def insert_knot(self, parameter, symmetrical=pythoncom.Empty):
        """
        
        Inserts a knot into a curve object.

        Parameters
        ==========
        parameter  (float, Required) - The parameter on the curve.
        symmetrical  (boolean, Optional) - If blnSymmetrical = True, then knots are added on both sides of the center of the curve. The default value is False.

        Returns
        =======
        boolean - True of False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InsertCurveKnot
        """
        return _base._rsf.insert_curve_knot(self._rhino_id, parameter, symmetrical)

    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):
        """
        
        Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.

        Parameters
        ==========
        degree  (integer, Optional) - The new degree, which must be greater than 1. The default is 3.
        point_count  (integer, Optional) - The new point count, which must be bigger than the intDegree.  With closed curves, the minimum point count is 3.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RebuildCurve
        """
        return _base._rsf.rebuild_curve(self._rhino_id, degree, point_count)

    def remove_knot(self, parameter):
        """
        
        Deletes a knot from a curve object.

        Parameters
        ==========
        parameter  (float, Required) - The parameter on the curve.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.

        Returns
        =======
        boolean - True of False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RemoveCurveKnot
        """
        return _base._rsf.remove_curve_knot(self._rhino_id, parameter)

    def reverse(self):
        """
        
        Reverses the direction of a curve object. This feature can also be found in Rhino's Dir command.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ReverseCurve
        """
        return _base._rsf.reverse_curve(self._rhino_id)

    def simplify(self, flags=pythoncom.Empty):
        """
        
        Simplify curve replaces the curve with a geometrically equivalent polycurve. The polycurve will have the following properties:
		1.  All the polycurve segments are lines, polylines, arcs, or NURBS curves.
		2.  The NURBS curves segments do not have fully multiple interior knots.
		3.  Rational NURBS curves do not have constant weights.
		4.  Any segment for which IsCurveLinear or IsArc is True is a line, polyline segment, or an arc.
		5.  Adjacent co-linear or co-circular segments are combined.
		6.  Segments that meet with G1-continuity have there ends tuned up so that they meet with G1-continuity to within machine precision.

        Parameters
        ==========
        flags  (integer, Optional) - The simplification methods to use. By default, all methods are used (intFlags = 0). The possible options are as follows:
		Value
		Description
		0
		Use all methods.
		1
		Do not split NURBS curves at fully multiple knots.
		2
		Do not replace segments with IsCurveLinear = True with line curves.
		4
		Do not replace segments with IsArc = True with arc curves.
		8
		Do not replace rational NURBS curves with constant denominator with an equivalent non-rational NURBS curve.
		16
		Do not adjust curves at G1-joins.
		32

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SimplifyCurve
        """
        return _base._rsf.simplify_curve(self._rhino_id, flags)
class _CurveRootPropClsd(_CurveRootProp):
    pass
class _CurveRootPropOpen(_CurveRootProp):
    pass
class _CurveRootTest(_ObjectRootTest):

    def is_closable(self, tolerance=pythoncom.Empty):
        """
        
        Decide if it makes sense to close off the curve by moving  the endpoint to the start based on start-end gap size and length of curve as approximated by chord defined by 6 points.

        Parameters
        ==========
        tolerance  (float, Optional) - The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurveClosable
        """
        return _base._rsf.is_curve_closable(self._rhino_id, tolerance)

    def is_closed(self):
        """
        
        Verifies an object is a closed curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurveClosed
        """
        return _base._rsf.is_curve_closed(self._rhino_id, pythoncom.Empty)

    def in_plane(self, plane=pythoncom.Empty):
        """
        
        Test a curve to see if it lies in a specific plane.

        Parameters
        ==========
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are as follows:
		Element
		Type
		Description
		0
		Array
		Required.  The construction plane's origin (3-D point).
		1
		Array
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Array
		Required.  The construction plane's Y axis direction (3-D vector).
		3
		Array

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurveInPlane
        """
        return _base._rsf.is_curve_in_plane(self._rhino_id, plane)

    def is_linear(self):
        """
        
        Verifies an object is a linear curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurveLinear
        """
        return _base._rsf.is_curve_linear(self._rhino_id, pythoncom.Empty)

    def is_periodic(self):
        """
        
        Verifies an object is a periodic curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurvePeriodic
        """
        return _base._rsf.is_curve_periodic(self._rhino_id, pythoncom.Empty)

    def is_planar(self):
        """
        
        Verifies an object is a planar curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurvePlanar
        """
        return _base._rsf.is_curve_planar(self._rhino_id, pythoncom.Empty)

    def is_rational(self):
        """
        
        Verifies an object is a rational NURBS curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurveRational
        """
        return _base._rsf.is_curve_rational(self._rhino_id, pythoncom.Empty)

    def is_pnt_on_crv(self, point):
        """
        
        Verifies that a point is on a curve.

        Parameters
        ==========
        point  (List of integer, Required) - The test, or sampling, point.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPointOnCurve
        """
        return _base._rsf.is_point_on_curve(self._rhino_id, point, pythoncom.Empty)
class _CurveRootType(_ObjectRootType):

    def is_arc(self):
        """
        
        Verifies an object is an arc curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsArc
        """
        return _base._rsf.is_arc(self._rhino_id, pythoncom.Empty)

    def is_circle(self):
        """
        
        Verifies an object is a circle curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCircle
        """
        return _base._rsf.is_circle(self._rhino_id, pythoncom.Empty)

    def is_crv(self):
        """
        
        Verifies an object is a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurve
        """
        return _base._rsf.is_curve(self._rhino_id, pythoncom.Empty)

    def is_ellipse(self):
        """
        
        Verifies an object is an elliptical-shaped curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsEllipse
        """
        return _base._rsf.is_ellipse(self._rhino_id)

    def is_line(self):
        """
        
        Verifies an object is a line curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLine
        """
        return _base._rsf.is_line(self._rhino_id, pythoncom.Empty)

    def is_poly_crv(self):
        """
        
        Verifies an object is a polycurve object.  A polycurve is a curve that is represented by a sequence of contiguous curve segments.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPolyCurve
        """
        return _base._rsf.is_poly_curve(self._rhino_id, pythoncom.Empty)

    def is_polyline(self):
        """
        
        Verifies an object is a polyline curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPolyline
        """
        return _base._rsf.is_polyline(self._rhino_id, pythoncom.Empty)
class _EllipseProp(_CurveRootProp):

    def center_pnt(self):
        """
        
        Returns the center point of an elliptical-shaped curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The 3-D center point of the ellipse if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EllipseCenterPoint
        """
        return _base._rsf.ellipse_center_point(self._rhino_id)

    def quad_pnts(self):
        """
        
        Returns the quadrant points of an elliptical-shaped curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of 3-D points identifying the quadrants of the ellipse if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EllipseQuadPoints
        """
        return _base._rsf.ellipse_quad_points(self._rhino_id)
class _MeshRoot(_ObjectRoot):
    pass
class _MeshRootFunc(_ObjectRootFunc):

    def curve_intersection(self, mesh, return_faces=pythoncom.Empty):
        """
        
        Calculates the intersection of a curve object and a mesh object.

        Parameters
        ==========
        mesh  (mesh object, Required) - The identifier of the mesh to intersect.
        return_faces  (boolean, Optional) - Return both intersection points and face indices.  If omitted or False, then just the intersection points are returned.

        Returns
        =======
        list - If return_faces is either omitted or False, then a list intersection points, if successful.
        list - If return_faces is True, then a one-dimensional list containing information about each intersection if successful.  Each list element is a one-dimensional list that contains the following two elements:
        list - The 3-D intersection point.
        number - The mesh face index on which the intersection point lies.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveMeshIntersection
        """
        return _base._rsf.curve_mesh_intersection(self._rhino_id, mesh._rhino_id, return_faces)

    def explode(self, delete=pythoncom.Empty):
        """
        
        Explodes a mesh object, or mesh objects,  into submeshes.  A submesh is a collection of mesh faces that are contained within a closed loop of unwelded mesh edges.  Unwelded mesh edges are edges where the mesh faces that share the edge have unique mesh vertices (not mesh topology vertices) at both ends of the edge.

        Parameters
        ==========
        delete  (boolean, Optional) - Delete input objects after exploding.  The default is not to delete objects (False).

        Returns
        =======
        list of objects - A list of strings identifying the newly created mesh objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExplodeMeshes
        """
        _rhino_ids = _base._rsf.explode_meshes(self._rhino_id, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Mesh(i), _rhino_ids)
        else:
            return None

    def closest_point(self, point, tolerance=pythoncom.Empty):
        """
        
        Returns the point on a mesh that is closest to a test point.

        Parameters
        ==========
        point  (List of float, Required) - A 3-D point to test.
        tolerance  (float, Optional) - The tolerance. Of omitted, a default tolerance of 0.0 is used.

        Returns
        =======
        list - A list containing the results of the calculation, if successful. The list elements are as follows:
        list - The 3-D point on the mesh object.
        number - The index of the mesh face on which the 3-D point lies.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshClosestPoint
        """
        return _base._rsf.mesh_closest_point(self._rhino_id, point, tolerance)

    def contour_points(self, start_point, end_point, interval=pythoncom.Empty, remove_coincident_points=pythoncom.Empty):
        """
        
        Returns the vertices of the polyline curves generated by contouring a mesh object.

        Parameters
        ==========
        start_point  (List of float, Required) - The 3-D starting point of a center line.
        end_point  (List of float, Required) - The 3-D ending point of a center line.
        interval  (float, Optional) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
        remove_coincident_points  (boolean, Optional) - Remove coincident points.  If True, and the polyline curves from which the contour point are taken are closed, then duplicate starting and ending points of the polyline curve will not be returned. The default is to return duplicate starting and ending points (False).

        Returns
        =======
        list - A list of 3-D point lists, one for each contour, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshContourPoints
        """
        return _base._rsf.mesh_contour_points(self._rhino_id, start_point, end_point, interval, remove_coincident_points)

    def mesh_intersection(self, mesh, tolerance=pythoncom.Empty):
        """
        
        Calculates the intersection of a mesh object with another mesh object.

        Parameters
        ==========
        mesh  (mesh object, Required) - The identifier of the second mesh object.
        tolerance  (float, Optional) - The intersection tolerance. Of omitted, Rhino's internal zero tolerance is used.

        Returns
        =======
        list - A list of 3-D point lists that identify the vertices of the intersection curves (polylines) if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshMeshIntersection
        """
        return _base._rsf.mesh_mesh_intersection(self._rhino_id, mesh._rhino_id, tolerance)

    def naked_edge_points(self):
        """
        
        Identifies the naked edge points of a polygon mesh object. This function shows where polygon mesh vertices are not completely surrounded by faces. Joined meshes, such as are made by Mesh Box, have naked mesh edge points where the sub-meshes are joined.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of boolean values that represent whether or not a mesh vertex is naked or not if successful.  The number of elements in the list will be equal to the value returned by MeshVertexCount. In which case, the list will identify the naked status for each vertex return by MeshVertices.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshNakedEdgePoints
        """
        return _base._rsf.mesh_naked_edge_points(self._rhino_id)

    def split_disjoint_mesh(self, delete=pythoncom.Empty):
        """
        
        Splits up a mesh object into its unconnected pieces.

        Parameters
        ==========
        delete  (boolean, Optional) - Delete the input object. The default is not to delete the input object (False).

        Returns
        =======
        list of objects - A list of strings identifying the newly created mesh objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitDisjointMesh
        """
        _rhino_ids = _base._rsf.split_disjoint_mesh(self._rhino_id, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Mesh(i), _rhino_ids)
        else:
            return None

    def unify_normals(self):
        """
        
        Fixes inconsistencies in the directions of faces of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of faces that were modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnifyMeshNormals
        """
        return _base._rsf.unify_mesh_normals(self._rhino_id)
class _MeshRootFuncClsd(_MeshRootFunc):

    def boolean_difference(self, meshes, delete=pythoncom.Empty):
        """
        
        Performs a Boolean difference operation on two sets of input meshes. For more details, see the MeshBooleanDifference command in the Rhino help file.

        Parameters
        ==========
        meshes  (list of Mesh, Required) - The identifiers of the meshes.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshBooleanDifference
        """
        if type(meshes) != list and type(meshes) != tuple:
            meshes = (meshes,)
        _rhino_ids = _base._rsf.mesh_boolean_difference(self._rhino_id, map(lambda i: i._rhino_id, meshes), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Mesh(i), _rhino_ids)
        else:
            return None

    def boolean_intersection(self, meshes, delete=pythoncom.Empty):
        """
        
        Performs a Boolean intersection operation on two sets of input meshes. For more details, see the MeshBooleanIntersection command in the Rhino help file.

        Parameters
        ==========
        meshes  (list of Mesh, Required) - The identifiers of the meshes.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshBooleanIntersection
        """
        if type(meshes) != list and type(meshes) != tuple:
            meshes = (meshes,)
        _rhino_ids = _base._rsf.mesh_boolean_intersection(self._rhino_id, map(lambda i: i._rhino_id, meshes), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Mesh(i), _rhino_ids)
        else:
            return None

    def boolean_split(self, input_1, delete=pythoncom.Empty):
        """
        
        Performs a Boolean split operation on two sets of input meshes. For more details, see the MeshBooleanSplit command in the Rhino help file.

        Parameters
        ==========
        input_1  (list of Mesh, Required) - The identifiers of the meshes.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshBooleanSplit
        """
        if type(input_1) != list and type(input_1) != tuple:
            input_1 = (input_1,)
        _rhino_ids = _base._rsf.mesh_boolean_split(self._rhino_id, map(lambda i: i._rhino_id, input_1), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Mesh(i), _rhino_ids)
        else:
            return None

    def boolean_union(self, meshes, delete=pythoncom.Empty):
        """
        
        Performs a Boolean union operation on a set of input meshes. For more details, see the MeshBooleanUnion command in the Rhino help file.

        Parameters
        ==========
        meshes  (list of array_of _ObjectRoot, Required) - The identifiers of the meshes to union.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshBooleanUnion
        """
        if type(meshes) != list and type(meshes) != tuple:
            meshes = (meshes,)
        _rhino_ids = _base._rsf.mesh_boolean_union(map(lambda i: i._rhino_id, meshes), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.Mesh(i), _rhino_ids)
        else:
            return None
class _MeshRootFuncOpen(_MeshRootFunc):
    pass
class _MeshRootMdfy(_ObjectRootMdfy):

    def quads_to_triangles(self):
        """
        
        Converts a mesh object's quad faces to triangles.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshQuadsToTriangles
        """
        return _base._rsf.mesh_quads_to_triangles(self._rhino_id)
class _MeshRootProp(_MeshRootFunc):

    def disjoint_mesh_count(self):
        """
        
        Returns the number of meshes that could be created by calling SplitDisjointMesh.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of meshes that could be created if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DisjointMeshCount
        """
        return _base._rsf.disjoint_mesh_count(self._rhino_id)

    def area(self):
        """
        
        Returns the approximate area of one or more mesh objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing three numbers if successful.  The three elements of the list are as follows:
        number - The number of meshes used in the area calculation.
        number - The total area of all meshes.
        number - The error estimate.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshArea
        """
        return _base._rsf.mesh_area(self._rhino_id)

    def area_centroid(self):
        """
        
        Calculates the area centroid of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A 3-D point identifying the area centroid if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshAreaCentroid
        """
        return _base._rsf.mesh_area_centroid(self._rhino_id)

    def face_centers(self):
        """
        
        Returns the center point of each face of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of 3-D points that define the face center points of the mesh if successful.  The number of elements in the list will be equal to the value returned by MeshFaceCount. In which case, the list will identify the center points for each face return by MeshFaces.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshFaceCenters
        """
        return _base._rsf.mesh_face_centers(self._rhino_id)

    def face_count(self):
        """
        
        Returns the total face count of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of mesh faces if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshFaceCount
        """
        return _base._rsf.mesh_face_count(self._rhino_id)

    def face_normals(self):
        """
        
        Returns the face unit normal for each face of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of 3-D vectors that define the face unit normals of the mesh if successful.  The number of elements in the list will be equal to the value returned by MeshFaceCount. In which case, the list will identify the unit normals for each face return by MeshFaces.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshFaceNormals
        """
        return _base._rsf.mesh_face_normals(self._rhino_id)

    def face_vertices(self):
        """
        
        Returns the vertex indices of all faces of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing lists of four numbers that define the vertex indices for each face of the mesh if successful.  Both quad and triangle faces are returned. If the third and forth vertex indices of a face are identical, the face is a triangle. Otherwise the face is a quad.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshFaceVertices
        """
        return _base._rsf.mesh_face_vertices(self._rhino_id)

    def faces(self, face_type=pythoncom.Empty):
        """
        
        Returns the face vertices of a mesh object.

        Parameters
        ==========
        face_type  (boolean, Optional) - The face type to be returned.  If omitted, both triangles and quads are returned (True)
		Value
		Description
		True
		Both triangles and quads.
		False

        Returns
        =======
        list - A list of 3-D points that define the face vertices of the mesh if successful.  If face_type is True, then faces are returned as both quads and triangles (4 3-D points).  For triangles, the third and forth vertex will be identical.  If face_type is False, then faces are returned as only triangles (3 3-D points).  Quads will be converted to triangles.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshFaces
        """
        return _base._rsf.mesh_faces(self._rhino_id, face_type)

    def quad_count(self):
        """
        
        Returns the number of quad faces of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of quad mesh faces if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshQuadCount
        """
        return _base._rsf.mesh_quad_count(self._rhino_id)

    def texture_coordinates(self):
        """
        
        Returns the normalized 2-D texture coordinates of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of 2-D points that define the texture coordinates of the mesh if successful.  Each 2-D point is normalized, that is, each coordinate component ranges in value between 0 and 1.  The number of elements in the list will be equal to the value returned by MeshVertexCount. In which case, the list will identify the texture coordinate for each vertex return by MeshVertices.
        None - If the mesh does not contain texture coordinates, if not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshTextureCoordinates
        """
        return _base._rsf.mesh_texture_coordinates(self._rhino_id)

    def triangle_count(self):
        """
        
        Returns the number of triangular faces of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of triangular mesh faces if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshTriangleCount
        """
        return _base._rsf.mesh_triangle_count(self._rhino_id)

    def vertex_colors(self, vertex_colors=pythoncom.Empty):
        """
        
        Returns or modifies the  vertex colors of a mesh object

        Parameters
        ==========
        vertex_colors  (List of integer, Optional) - An list of RGB color values. Note, for every vertex, there must be a corresponding vertex color.

        Returns
        =======
        list - If vertex_colors  is not specified,  the current vertex color if successful.
        list - If vertex_colors  is specified, the previous vertex colors if successful.
        None - If object does not have vertex colors, if not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshVertexColors
        """
        return _base._rsf.mesh_vertex_colors(self._rhino_id, vertex_colors)

    def vertex_count(self):
        """
        
        Returns the vertex count of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of mesh vertices if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshVertexCount
        """
        return _base._rsf.mesh_vertex_count(self._rhino_id)

    def vertex_normals(self):
        """
        
        Returns the vertex unit normal for each vertex of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of 3-D vectors that define the vertex unit normals of the mesh if successful.  The number of elements in the list will be equal to the value returned by MeshVertexCount. In which case, the list will identify the unit normals for each vertex return by MeshVertices.
        None - If the mesh does not contain vertex normals, if not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshVertexNormals
        """
        return _base._rsf.mesh_vertex_normals(self._rhino_id)

    def vertices(self):
        """
        
        Returns the vertices of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of 3-D points that define the vertices of the mesh if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshVertices
        """
        return _base._rsf.mesh_vertices(self._rhino_id)
class _MeshRootPropClsd(_MeshRootProp):

    def mesh_volume(self, meshes):
        """
        
        Returns the approximate volume of one or more closed mesh objects.

        Parameters
        ==========
        meshes  (list of mesh object, Required) - A list of objects.

        Returns
        =======
        list - A list containing three numbers if successful.  The three elements of the list are as follows:
        number - The number of meshes used in the volume calculation.
        number - The total volume of all meshes.
        number - The error estimate.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshVolume
        """
        if type(meshes) != list and type(meshes) != tuple:
            meshes = (meshes,)
        return _base._rsf.mesh_volume(map(lambda i: i._rhino_id, meshes))

    def mesh_volume_centroid(self):
        """
        
        Calculates the volume centroid of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A 3-D point identifying the volume centroid if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshVolumeCentroid
        """
        return _base._rsf.mesh_volume_centroid(self._rhino_id)
class _MeshRootPropOpen(_MeshRootProp):
    pass
class _MeshRootTest(_ObjectRootTest):

    def is_closed(self):
        """
        
        Verifies a mesh object is closed.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsMeshClosed
        """
        return _base._rsf.is_mesh_closed(self._rhino_id)

    def is_manifold(self):
        """
        
        Verifies a mesh object is manifold.  A mesh for which every edge is shared by at most two faces is called a manifold.  If a mesh has at least one edge that is shared by more than two faces, then that mesh is called non-manifold.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsMeshManifold
        """
        return _base._rsf.is_mesh_manifold(self._rhino_id)

    def has_face_normals(self):
        """
        
        Verifies a mesh object has face normals.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshHasFaceNormals
        """
        return _base._rsf.mesh_has_face_normals(self._rhino_id)

    def has_texture_coordinates(self):
        """
        
        Verifies a mesh object has texture coordinates.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshHasTextureCoordinates
        """
        return _base._rsf.mesh_has_texture_coordinates(self._rhino_id)

    def has_vertex_colors(self):
        """
        
        Verifies a mesh object has vertex colors.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshHasVertexColors
        """
        return _base._rsf.mesh_has_vertex_colors(self._rhino_id)

    def has_vertex_normals(self):
        """
        
        Verifies a mesh object has vertex normals.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshHasVertexNormals
        """
        return _base._rsf.mesh_has_vertex_normals(self._rhino_id)
class _MeshRootType(_ObjectRootTest):

    def is_mesh(self):
        """
        
        Verifies an object is a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsMesh
        """
        return _base._rsf.is_mesh(self._rhino_id)
class _PolylineProp(_CurveRootProp):

    def vertices(self):
        """
        
        Returns the vertices of a polyline curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - An  list of 3-D vertex points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PolylineVertices
        """
        return _base._rsf.polyline_vertices(self._rhino_id, pythoncom.Empty)
class _SurfaceRoot(_ObjectRoot):
    pass
class _SurfaceRootFunc(_ObjectRootFunc):

    def make_non_periodic(self, direction, delete=pythoncom.Empty):
        """
        
        Makes a periodic surface non-periodic. Non-periodic surfaces can develop kinks when deformed.

        Parameters
        ==========
        direction  (integer, Required) - The direction to make non-periodic, either 0 = U, or 1 = V.
        delete  (boolean, Optional) - Delete input surface.  If omitted, the input surface will not be deleted (False).

        Returns
        =======
        object - If delete is False, the new object if successful.
        object - If delete is True, the modified object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MakeSurfaceNonPeriodic
        """
        _rhino_id = _base._rsf.make_surface_non_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.obj.NurbsSurface(_rhino_id)
        else:
            return None

    def make_periodic(self, direction, delete=pythoncom.Empty):
        """
        
        Makes an existing surface a periodic NURBS surface.

        Parameters
        ==========
        direction  (integer, Required) - The direction to make periodic, either 0 = U, or 1 = V.
        delete  (boolean, Optional) - Delete input surface.  If omitted, the input surface will not be deleted (False).

        Returns
        =======
        object - If delete is False, the new object if successful.
        object - If delete is True, the modified object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MakeSurfacePeriodic
        """
        _rhino_id = _base._rsf.make_surface_periodic(self._rhino_id, direction, delete)
        if _rhino_id:
            return p2r.obj.NurbsSurface(_rhino_id)
        else:
            return None

    def closest_pnt(self, point):
        """
        
        Returns the UV parameter of the point on a surface that is closest to a test point.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        list - A list containing the U,V parameters of the closest point on the surface if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceClosestPoint
        """
        return _base._rsf.surface_closest_point(self._rhino_id, point)
class _SurfaceRootFuncClsd(_SurfaceRootFunc):

    def boolean_difference(self, breps, delete=pythoncom.Empty):
        """
        
        Performs a Boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file.

        Parameters
        ==========
        breps  (list of surface object, Required) - The identifiers of the surfaces or polysurfaces to be subtracted.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BooleanDifference
        """
        if type(breps) != list and type(breps) != tuple:
            breps = (breps,)
        _rhino_ids = _base._rsf.boolean_difference(self._rhino_id, map(lambda i: i._rhino_id, breps), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolySurface(i), _rhino_ids)
        else:
            return None

    def boolean_intersection(self, breps, delete=pythoncom.Empty):
        """
        
        Performs a Boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file.

        Parameters
        ==========
        breps  (list of surface object, Required) - The identifiers of the surfaces or polysurfaces.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BooleanIntersection
        """
        if type(breps) != list and type(breps) != tuple:
            breps = (breps,)
        _rhino_ids = _base._rsf.boolean_intersection(self._rhino_id, map(lambda i: i._rhino_id, breps), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolySurface(i), _rhino_ids)
        else:
            return None

    def boolean_union(self, breps, delete=pythoncom.Empty):
        """
        
        Performs a Boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file.

        Parameters
        ==========
        breps  (list of surface object, Required) - The identifiers of the surfaces or polysurfaces to union.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BooleanUnion
        """
        if type(breps) != list and type(breps) != tuple:
            breps = (breps,)
        _rhino_ids = _base._rsf.boolean_union(map(lambda i: i._rhino_id, breps), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolySurface(i), _rhino_ids)
        else:
            return None

    def brep_closest_pnt(self, point):
        """
        
        Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        list - A list of closest point information if successful.  The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BrepClosestPoint
        """
        return _base._rsf.brep_closest_point(self._rhino_id, point)

    def intersect_breps(self, brep_1, tolerance=pythoncom.Empty):
        """
        
        Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.

        Parameters
        ==========
        brep_1  (string, Required) - The second  brep object's identifier.
        tolerance  (float, Optional) - The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..

        Returns
        =======
        list of objects - A list of strings identifying the newly created intersection curve and point objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IntersectBreps
        """
        _rhino_ids = _base._rsf.intersect_breps(self._rhino_id, brep_1, tolerance)
        if _rhino_ids:
            return map(lambda i: self._class(i), _rhino_ids)
        else:
            return None

    def boolean_split(self, cutter, delete=pythoncom.Empty):
        """
        
        Splits a brep.  A brep can be either a surface with a single face or a polysurface.

        Parameters
        ==========
        cutter  (string, Required) - The identifier of the brep object to split with.
        delete  (boolean, Optional) - Delete input brep.  If omitted, the input brep will not be deleted (False).

        Returns
        =======
        list of objects - The identifiers of the new brep objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitBrep
        """
        _rhino_ids = _base._rsf.split_brep(self._rhino_id, cutter, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.PolySurface(i), _rhino_ids)
        else:
            return None
class _SurfaceRootFuncOpen(_SurfaceRootFunc):

    def cap_planar_holes(self):
        """
        
        Caps planar holes in a surface or polysurface. For more details, see the Cap command in the Rhino help file.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CapPlanarHoles
        """
        return _base._rsf.cap_planar_holes(self._rhino_id)
class _SurfaceRootMdfy(_ObjectRootMdfy):

    def flip(self, flip=pythoncom.Empty):
        """
        
        Returns or changes the normal direction of a surface. This feature can also be found in Rhino's Dir command.

        Parameters
        ==========
        flip  (boolean, Optional) - The new normal orientation, either flipped (True) or not flipped (False).  If omitted, the current normal orientation is returned.

        Returns
        =======
        boolean - If flip is not specified, the current normal orientation if successful.
        boolean - If flip is specified, the previous normal orientation if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: FlipSurface
        """
        return _base._rsf.flip_surface(self._rhino_id, flip)

    def insert_knot(self, parameter, direction, symmetrical=pythoncom.Empty):
        """
        
        Inserts a knot into a surface object.

        Parameters
        ==========
        parameter  (float, Required) - An list containing a U,V parameter on the surface.
        direction  (integer, Required) - The direction for knot insertion, either 0 = U, 1 = V, or 2 = both.
        symmetrical  (boolean, Optional) - If blnSymmetrical = True, then knots are added on both sides of the center of the surface.  The default value is False.

        Returns
        =======
        boolean - True of False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InsertSurfaceKnot
        """
        return _base._rsf.insert_surface_knot(self._rhino_id, parameter, direction, symmetrical)

    def rebuild(self, degree=pythoncom.Empty, point_count=pythoncom.Empty):
        """
        
        Rebuilds a surface to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.

        Parameters
        ==========
        degree  (List of integer, Optional) - An list of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3 in each direction.
        point_count  (List of integer, Optional) - An list of two numbers that identify the surface point count in both the U and the V directions.  The point count must be greater than the degree.  The default value is 10 in each direction.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RebuildSurface
        """
        return _base._rsf.rebuild_surface(self._rhino_id, degree, point_count)

    def remove_knot(self, parameter, direction):
        """
        
        Deletes a knot-line from a surface object.

        Parameters
        ==========
        parameter  (float, Required) - An list containing a U,V parameter on the surface.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
        direction  (integer, Required) - The direction for knot insertion, either 0 = U, or 1 = V.

        Returns
        =======
        boolean - True of False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RemoveSurfaceKnot
        """
        return _base._rsf.remove_surface_knot(self._rhino_id, parameter, direction)

    def reverse(self, direction):
        """
        
        Reverses the U and V directions of a surface object. This feature can also be found in Rhino's Dir command.
		To reverse the normal direction of a surface, use the FlipSurface method.

        Parameters
        ==========
        direction  (integer, Required) - The direction to reverse. Values can be added together so as to reverse more than one direction.
		Value
		Description
		1
		Reverse the surface in the U direction.
		2
		Reverse the surface in the V direction.
		4

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ReverseSurface
        """
        return _base._rsf.reverse_surface(self._rhino_id, direction)

    def shrink_trimmed(self):
        """
        
        Shrinks the underlying untrimmed surfaces near to trimming boundaries. For more details, see the ShrinkTrimmedSrf command in the Rhino help file.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ShrinkTrimmedSurface
        """
        return _base._rsf.shrink_trimmed_surface(self._rhino_id)

    def seam(self, direction, parameter):
        """
        
        Changes the seam of a closed surface. For more information, see the Rhino help file for the SrfSeam command.

        Parameters
        ==========
        direction  (integer, Required) - The parameter direction, where 0 = U and 1 = V.
        parameter  (float, Required) - The parameter at which to place the seam.

        Returns
        =======
        boolean - True of False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceSeam
        """
        return _base._rsf.surface_seam(self._rhino_id, direction, parameter)
class _SurfaceRootProp(_ObjectRootProp):

    def area(self):
        """
        
        Calculates the area of a surface or polysurface object. The results are based on the current drawing units.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of area information if successful.  The list will contain the following information:
        number - The area.
        number - The absolute (+/-) error bound for the area.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceArea
        """
        return _base._rsf.surface_area(self._rhino_id)

    def area_centroid(self):
        """
        
        Calculates the area centroid of a surface or polysurface object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of area centroid information if successful.  The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceAreaCentroid
        """
        return _base._rsf.surface_area_centroid(self._rhino_id)

    def area_moments(self):
        """
        
        Calculates the area moments of inertia of a surface or polysurface object.  For more information, see the Rhino help file for "Mass Properties Calculation Details."

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of area moments of inertia information if successful.  The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceAreaMoments
        """
        return _base._rsf.surface_area_moments(self._rhino_id)

    def contour_pnts(self, start_point, end_point, interval=pythoncom.Empty, angle=pythoncom.Empty):
        """
        
        Returns the vertices of the polyline curves generated by contouring a surface or polysurface object.

        Parameters
        ==========
        start_point  (List of float, Required) - The 3-D starting point of a center line.
        end_point  (List of float, Required) - The 3-D ending point of a center line.
        interval  (float, Optional) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
        angle  (float, Optional) - The maximum angle in degrees between unit tangents at adjacent vertices.  If omitted, the maximum angle will be set to 5.0 degrees.

        Returns
        =======
        list - A list of 3-D point lists, one for each contour, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceContourPoints
        """
        return _base._rsf.surface_contour_points(self._rhino_id, start_point, end_point, interval, angle)

    def curvature(self, parameter):
        """
        
        Returns the curvature of a surface at a U,V parameter.  See the Rhino help file for details on surface curvature.

        Parameters
        ==========
        parameter  (List of float, Required) - An list containing the U,V parameter to evaluate.

        Returns
        =======
        list - A list of curvature information if successful.  The list will contain the following information:
        number - Maximum principal curvature.
        number - Minimum principal curvature.
        number - Gaussian curvature.
        number - Mean curvature.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceCurvature
        """
        return _base._rsf.surface_curvature(self._rhino_id, parameter)

    def curvature_analysis(self):
        """
        
        Returns the curvature of a surface.  See the Rhino help file for details on surface curvature analysis.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of curvature information if successful.  The list will contain the following information:
        list - A list containing three values: the min Gaussian curvature, the max Gaussian curvature, and the infinity status.
        list - A list containing three values: the min unsigned mean curvature, the max unsigned mean curvature, and the infinity comparison.
        list - A list containing three values: the min maximum unsigned radius of curvature, the max maximum unsigned radius of curvature, and the infinity comparison.
        list - A list containing three values: the min minimum unsigned radius of curvature, the max minimum unsigned radius of curvature, and the infinity comparison.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceCurvatureAnalysis
        """
        return _base._rsf.surface_curvature_analysis(self._rhino_id)

    def degree(self, direction=pythoncom.Empty):
        """
        
        Returns the degree of a  surface object in the specified direction.

        Parameters
        ==========
        direction  (integer, Optional) - The direction, either 0 = U, or 1 = V, or 2 = Both.  Of omitted, both the degrees in the U and V directions are returned (2 = Both).

        Returns
        =======
        list - If direction is not specified, or direction is set to 2, then the degree in both the U and V directions is returned.
        number - If direction is specified, and direction is set to either 0 or 1, then the degree in either the U or V direction is returned.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceDegree
        """
        return _base._rsf.surface_degree(self._rhino_id, direction)

    def domain(self, direction):
        """
        
        Returns the domain of a  surface object in the specified direction.

        Parameters
        ==========
        direction  (integer, Required) - The direction, either 0 = U, or 1 = V.

        Returns
        =======
        list - A list containing the domain interval in the specified direction if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceDomain
        """
        return _base._rsf.surface_domain(self._rhino_id, direction)

    def edit_pnts(self, return_parameters=pythoncom.Empty, return_all=pythoncom.Empty):
        """
        
        Returns the edit, or Greville, points of a surface object.  For each surface control point, there is a corresponding edit point.

        Parameters
        ==========
        return_parameters  (boolean, Optional) - If False (default), edit points are returned as an list of 3-D points. If True, edit points are returned as an list U,V surface parameters.
        return_all  (boolean, Optional) - If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.

        Returns
        =======
        list - If return_parameters is omitted or False, then a list of 3-D edit points if successful.
        list - If return_parameters is True, then a list of U,V parameter values if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceEditPoints
        """
        return _base._rsf.surface_edit_points(self._rhino_id, return_parameters, return_all)

    def isocurve_density(self, density=pythoncom.Empty):
        """
        
        Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface.

        Parameters
        ==========
        density  (integer, Optional) - The isocurve wireframe density.  The possible values are as follows:
		Value
		Description
		-1
		Hides surface isocurves.
		0
		Display boundary and knot wires.
		1
		Display boundary and knot wires and one interior wire if there are no interior knots.
		>= 2

        Returns
        =======
        number - The density is not specified, then the current isocurve density if successful.
        number - The density is specified, then the previous isocurve density if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceIsocurveDensity
        """
        return _base._rsf.surface_isocurve_density(self._rhino_id, density)

    def knot_count(self):
        """
        
        Returns the knot count of a surface object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The number of knots in the U and V directions if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceKnotCount
        """
        return _base._rsf.surface_knot_count(self._rhino_id)

    def knots(self):
        """
        
        Returns the knots, or knot vector, of a surface object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The knot values of the surface if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceKnots
        """
        return _base._rsf.surface_knots(self._rhino_id)

    def normal(self, parameter):
        """
        
        Returns a 3-D vector that is the normal to a surface at a parameter.

        Parameters
        ==========
        parameter  (List of float, Required) - An list containing the UV parameter to evaluate.

        Returns
        =======
        list - A 3-D vector if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceNormal
        """
        return _base._rsf.surface_normal(self._rhino_id, parameter)

    def pnt_count(self):
        """
        
        Returns the control points count of a surface object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The number of control points in the U and V directions if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfacePointCount
        """
        return _base._rsf.surface_point_count(self._rhino_id)

    def pnts(self, return_all=pythoncom.Empty):
        """
        
        Returns the control points, or control vertices, of a surface object.

        Parameters
        ==========
        return_all  (boolean, Optional) - If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.

        Returns
        =======
        list - The control points of the surface if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfacePoints
        """
        return _base._rsf.surface_points(self._rhino_id, return_all)

    def weights(self):
        """
        
        Returns an array of weight values that are assigned to the control points of a surface.  The number of weights returned will be equal to the number of control points in the U and V directions.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - The weight values of the surface if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceWeights
        """
        return _base._rsf.surface_weights(self._rhino_id)
class _SurfaceRootPropClsd(_SurfaceRootProp):

    def volume(self):
        """
        
        Calculates the volume of closed surface or polysurface objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of volume information if successful.  The list will contain the following information:
        number - The volume.
        number - The absolute (+/-) error bound for the volume.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceVolume
        """
        return _base._rsf.surface_volume(self._rhino_id)

    def volume_centroid(self):
        """
        
        Calculates the volume centroid of closed surface or polysurface objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of volume centroid information if successful.  The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceVolumeCentroid
        """
        return _base._rsf.surface_volume_centroid(self._rhino_id)

    def volume_moments(self):
        """
        
        Calculates the volume moments of inertia of closed surface or polysurface objects.  For more information, see the Rhino help file for "Mass Properties Calculation Details."

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of volume moments of inertia information if successful.  The list will contain the following information:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceVolumeMoments
        """
        return _base._rsf.surface_volume_moments(self._rhino_id)
class _SurfaceRootPropOpen(_SurfaceRootProp):
    pass
class _SurfaceRootTest(_ObjectRootTest):

    def is_brep(self):
        """
        
        Verifies an object is a Brep, or a boundary representation model, object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBrep
        """
        return _base._rsf.is_brep(self._rhino_id)

    def is_brep_manifold(self):
        """
        
        Verifies a polysurface object is manifold.  A polysurface for which every edge is shared by at most two faces is called a manifold.  If a polysurface has at least one edge that is shared by more than two faces, then that polysurface is called non-manifold.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsBrepManifold
        """
        return _base._rsf.is_brep_manifold(self._rhino_id)

    def is_parameter_on_srf(self, parameter):
        """
        
        Verifies that a parameter space point is on a trimmed surface, or not on the trimmed portion of a surface.

        Parameters
        ==========
        parameter  (List of float, Required) - An list containing the U,V parameter to evaluate.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsParameterOnSurface
        """
        return _base._rsf.is_parameter_on_surface(self._rhino_id, parameter)

    def is_plane_surface(self):
        """
        
        Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, a plane surface is not a planar NURBS surface.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPlaneSurface
        """
        return _base._rsf.is_plane_surface(self._rhino_id)

    def is_pnt_in_srf(self, point):
        """
        
        Verifies that a point is inside a closed surface or polysurface.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPointInSurface
        """
        return _base._rsf.is_point_in_surface(self._rhino_id, point)

    def is_pnt_on_srf(self, point):
        """
        
        Verifies that a point lies on a surface.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPointOnSurface
        """
        return _base._rsf.is_point_on_surface(self._rhino_id, point)

    def is_poly_srf(self):
        """
        
        Verifies an object is a polysurface.  Polysurfaces consists of two or more surfaces joined together. If the polysurface fully encloses a volume, it is considered a solid. In some other 3-D programs, this is called a "quilt."

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPolySurface
        """
        return _base._rsf.is_poly_surface(self._rhino_id)

    def is_poly_surface_closed(self):
        """
        
        Verifies a polysurface object is closed.  If the polysurface fully encloses a volume, it is considered a solid.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPolySurfaceClosed
        """
        return _base._rsf.is_poly_surface_closed(self._rhino_id)

    def is_poly_srf_planar(self):
        """
        
        Verifies a polysurface object is planar.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsPolySurfacePlanar
        """
        return _base._rsf.is_poly_surface_planar(self._rhino_id)

    def is_srf_closed(self, direction):
        """
        
        Verifies a surface object is closed in the specified direction.  If the surface fully encloses a volume, it is considered a solid.

        Parameters
        ==========
        direction  (integer, Required) - The direction, either 0 = U, or 1 = V.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSurfaceClosed
        """
        return _base._rsf.is_surface_closed(self._rhino_id, direction)

    def is_srf_periodic(self, direction):
        """
        
        Verifies a surface object is periodic in the specified direction.

        Parameters
        ==========
        direction  (integer, Required) - The direction, either 0 = U, or 1 = V.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSurfacePeriodic
        """
        return _base._rsf.is_surface_periodic(self._rhino_id, direction)

    def is_srf_planar(self, tolerance=pythoncom.Empty):
        """
        
        Verifies a surface object is planar.

        Parameters
        ==========
        tolerance  (float, Optional) - A tolerance to use when checking. The default is to use Rhino's current absolute tolerance.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSurfacePlanar
        """
        return _base._rsf.is_surface_planar(self._rhino_id, tolerance)

    def is_srf_rational(self):
        """
        
        Verifies a surface object is rational.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSurfaceRational
        """
        return _base._rsf.is_surface_rational(self._rhino_id)

    def is_srf_singular(self, direction):
        """
        
        Verifies a surface object is singular in the specified direction.  Surfaces are considered singular if a side collapses to a point.

        Parameters
        ==========
        direction  (integer, Required) - The direction, either 0 = south, 1 = east, 2 = north, or 3 = west.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSurfaceSingular
        """
        return _base._rsf.is_surface_singular(self._rhino_id, direction)

    def is_srf_trimmed(self):
        """
        
        Verifies a surface object has been trimmed.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSurfaceTrimmed
        """
        return _base._rsf.is_surface_trimmed(self._rhino_id)
class _SurfaceRootType(_ObjectRootTest):

    def is_cone(self):
        """
        
        Determines if a surface is a portion of a cone.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCone
        """
        return _base._rsf.is_cone(self._rhino_id)

    def is_cylinder(self):
        """
        
        Determines if a surface is a portion of a cylinder.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCylinder
        """
        return _base._rsf.is_cylinder(self._rhino_id)

    def is_sphere(self):
        """
        
        Determines if a surface is a portion of a sphere.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSphere
        """
        return _base._rsf.is_sphere(self._rhino_id)

    def is_surface(self):
        """
        
        Verifies an object is surface.  Brep objects with only one face are also considered surfaces.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsSurface
        """
        return _base._rsf.is_surface(self._rhino_id)

    def is_torus(self):
        """
        
        Determines if a surface is a portion of a torus.

        Parameters
        ==========
        No parameters

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsTorus
        """
        return _base._rsf.is_torus(self._rhino_id)
class _TorusProp(_SurfaceRootPropClsd):

    def torus_definition(self):
        """
        
        Returns the definition of a torus surface.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing the definition of the torus if successful.  The elements of the list are as follows:
        list - The base plane of the torus.
        number - The major radius of the torus.
        number - The minor radius of the torus.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceTorus
        """
        return _base._rsf.surface_torus(self._rhino_id)
class _CurveRootFuncOorC(_CurveRootFuncOpen,_CurveRootFuncClsd):
    pass
class _CurveRootPropOorC(_CurveRootPropOpen,_CurveRootPropClsd):
    pass
class _MeshRootFuncOorC(_MeshRootFuncOpen,_MeshRootFuncClsd):
    pass
class _MeshRootPropOorc(_MeshRootPropClsd,_MeshRootPropOpen):
    pass
class _PolyCurveFunc(_CurveRootFuncOorC):

    def explode(self, delete=pythoncom.Empty):
        """
        
        Explodes, or un-joins,  one more curve objects.  Polycurves will be exploded into curve segments.  Polylines will be exploded into line segments.  ExplodeCurves will return the curves in
		topological order.

        Parameters
        ==========
        delete  (boolean, Optional) - Delete input objects after exploding.  The default is not to delete objects (False).

        Returns
        =======
        list of objects - A list of strings identifying the newly created curve objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExplodeCurves
        """
        _rhino_ids = _base._rsf.explode_curves(self._rhino_id, delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.NurbsCurve(i), _rhino_ids)
        else:
            return None
class _SphereProp(_SurfaceRootPropClsd):

    def sphere_definition(self):
        """
        
        Returns the definition of a sphere surface.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing the definition of the sphere if successful.  The elements of the list are as follows:
        list - The equatorial plane of the sphere.  The origin of the plane will be the center point of the sphere.
        number - The radius of the sphere.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceSphere
        """
        return _base._rsf.surface_sphere(self._rhino_id)
class _SurfaceRootFuncOorc(_SurfaceRootFuncOpen,_SurfaceRootFuncClsd):
    pass
class _SurfaceRootPropOorc(_SurfaceRootPropOpen,_SurfaceRootPropClsd):
    pass
class _ConeProp(_SurfaceRootPropOorc):

    def cone_def(self):
        """
        
        Returns the definition of a cone surface.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing the definition of the cone if successful.  The elements of the list are as follows:
        list - The plane of the cone.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
        number - The height of the cone.
        number - The radius of the cone.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceCone
        """
        return _base._rsf.surface_cone(self._rhino_id)
class _CylinderProp(_SurfaceRootPropOorc):

    def cylinder_def(self):
        """
        
        Returns the definition of a cylinder surface.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing the definition of the cylinder if successful.  The elements of the list are as follows:
        list - The base plane of the cylinder.
        number - The height of the cylinder.
        number - The radius of the cylinder.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceCylinder
        """
        return _base._rsf.surface_cylinder(self._rhino_id)
class _PolySurfaceFunc(_SurfaceRootFuncOorc):

    def explode(self, objects, delete=pythoncom.Empty):
        """
        
        Explodes, or un-joins,  one more polysurface objects.  Polysurfaces will be exploded into separate surfaces.

        Parameters
        ==========
        objects  (list of array_of _ObjectRoot, Required) - A list of polysurface objects to explode.
        delete  (boolean, Optional) - Delete input objects after exploding.  The default is not to delete objects (False).

        Returns
        =======
        list of objects - A list of strings identifying the newly created surface objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExplodePolysurfaces
        """
        if type(objects) != list and type(objects) != tuple:
            objects = (objects,)
        _rhino_ids = _base._rsf.explode_polysurfaces(map(lambda i: i._rhino_id, objects), delete)
        if _rhino_ids:
            return map(lambda i: p2r.obj.NurbsSurface(i), _rhino_ids)
        else:
            return None
class Arc(_CurveRoot):pass
class Arc(_CurveRoot):
    class wrap(_wrap.WrapBase, Arc):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class dupl(_ArcDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class eval(_CurveRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class func(_CurveRootFuncOpen):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class modf(_CurveRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class prop(_ArcProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class test(_CurveRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Arc
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Arc.defm(_rhino_id)
        self.dupl = Arc.dupl(_rhino_id)
        self.eval = Arc.eval(_rhino_id)
        self.func = Arc.func(_rhino_id)
        self.grps = Arc.grps(_rhino_id)
        self.modf = Arc.modf(_rhino_id)
        self.mtrl = Arc.mtrl(_rhino_id)
        self.prop = Arc.prop(_rhino_id)
        self.rndr = Arc.rndr(_rhino_id)
        self.stat = Arc.stat(_rhino_id)
        self.test = Arc.test(_rhino_id)
        self.trfm = Arc.trfm(_rhino_id)
        self.util = Arc.util(_rhino_id)

    @staticmethod
    def create(plane, radius, angle):
        """
        
        Factory method:
        Adds an arc curve to the document.

        Parameters
        ==========
        plane  (List of float, Required) - The plane on which the arc will lie. The origin of the plane will be the center point of the arc. The X-axis of the plane will define the 0 angle direction.
        radius  (float, Required) - The radius arc.
        angle  (float, Required) - A angle or interval, in degrees, of the arc.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddArc
        """

        _rhino_id = _base._rsf.add_arc(plane, radius, angle)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_3pt(start_point, end_point, point):
        """
        
        Factory method:
        Adds a 3-point arc curve to the document.

        Parameters
        ==========
        start_point  (List of float, Required) - The starting point of the arc.
        end_point  (List of float, Required) - The ending point of the arc.
        point  (List of float, Required) - A point on the arc.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddArc3Pt
        """

        _rhino_id = _base._rsf.add_arc_3_pt(start_point, end_point, point)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_fillet(curve_0, curve_1, radius=pythoncom.Empty, point_0=pythoncom.Empty, point_1=pythoncom.Empty):
        """
        
        Factory method:
        Adds a fillet curve between two curve objects.

        Parameters
        ==========
        curve_0  (NurbsCurve, Required) - The identifier of the first curve object.
        curve_1  (NurbsCurve, Required) - The identifier of the second curve object.
        radius  (float, Optional) - The fillet radius. If omitted, a radius of 1.0 is specified.
        point_0  (List of float, Optional) - The base point on the first curve. If omitted, the starting point of the curve is used.
        point_1  (List of float, Optional) - The base point on the second curve. If omitted, the starting point of the curve is used.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddFilletCurve
        """

        _rhino_id = _base._rsf.add_fillet_curve(curve_0._rhino_id, curve_1._rhino_id, radius, point_0, point_1)

        if _rhino_id:
            return Arc(_rhino_id)
        else:
            return None
class Box(_SurfaceRoot):pass
class Box(_SurfaceRoot):
    class wrap(_wrap.WrapBase, Box):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class dupl(_BoxDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class func(_SurfaceRootFuncOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class prop(_SurfaceRootPropClsd):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Box
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Box.defm(_rhino_id)
        self.dupl = Box.dupl(_rhino_id)
        self.eval = Box.eval(_rhino_id)
        self.func = Box.func(_rhino_id)
        self.grps = Box.grps(_rhino_id)
        self.modf = Box.modf(_rhino_id)
        self.mtrl = Box.mtrl(_rhino_id)
        self.prop = Box.prop(_rhino_id)
        self.rndr = Box.rndr(_rhino_id)
        self.stat = Box.stat(_rhino_id)
        self.test = Box.test(_rhino_id)
        self.trfm = Box.trfm(_rhino_id)
        self.util = Box.util(_rhino_id)

    @staticmethod
    def create(corner_points):
        """
        
        Factory method:
        Adds a new box-shaped polysurface to the document.

        Parameters
        ==========
        corner_points  (List of float, Required) - An list of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddBox
        """

        _rhino_id = _base._rsf.add_box(corner_points)

        if _rhino_id:
            return Box(_rhino_id)
        else:
            return None
class Circle(_CurveRoot):pass
class Circle(_CurveRoot):
    class wrap(_wrap.WrapBase, Circle):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class dupl(_CircleDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class eval(_CurveRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class func(_CurveRootFuncClsd):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class modf(_CurveRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class prop(_CircleProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class test(_CurveRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Circle
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Circle.defm(_rhino_id)
        self.dupl = Circle.dupl(_rhino_id)
        self.eval = Circle.eval(_rhino_id)
        self.func = Circle.func(_rhino_id)
        self.grps = Circle.grps(_rhino_id)
        self.modf = Circle.modf(_rhino_id)
        self.mtrl = Circle.mtrl(_rhino_id)
        self.prop = Circle.prop(_rhino_id)
        self.rndr = Circle.rndr(_rhino_id)
        self.stat = Circle.stat(_rhino_id)
        self.test = Circle.test(_rhino_id)
        self.trfm = Circle.trfm(_rhino_id)
        self.util = Circle.util(_rhino_id)

    @staticmethod
    def create(plane, radius):
        """
        
        Factory method:
        Adds a circle curve to the document.

        Parameters
        ==========
        plane  (List of float, Required) - The plane on which the circle will lie. The origin of the plane will be the center point of the circle.
        radius  (float, Required) - The radius of the circle.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCircle
        """

        _rhino_id = _base._rsf.add_circle(plane, radius)

        if _rhino_id:
            return Circle(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_3pt(first_point, second_point, third_point):
        """
        
        Factory method:
        Adds a 3-point circle curve to the document.

        Parameters
        ==========
        first_point  (List of float, Required) - The first point of the circle.
        second_point  (List of float, Required) - The second point of the circle.
        third_point  (List of float, Required) - The third point of the circle.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCircle3Pt
        """

        _rhino_id = _base._rsf.add_circle_3_pt(first_point, second_point, third_point)

        if _rhino_id:
            return Circle(_rhino_id)
        else:
            return None
class Cone(_SurfaceRoot):pass
class Cone(_SurfaceRoot):
    class wrap(_wrap.WrapBase, Cone):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class dupl(_ConeDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class func(_SurfaceRootFuncOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class prop(_ConeProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cone
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Cone.defm(_rhino_id)
        self.dupl = Cone.dupl(_rhino_id)
        self.eval = Cone.eval(_rhino_id)
        self.func = Cone.func(_rhino_id)
        self.grps = Cone.grps(_rhino_id)
        self.modf = Cone.modf(_rhino_id)
        self.mtrl = Cone.mtrl(_rhino_id)
        self.prop = Cone.prop(_rhino_id)
        self.rndr = Cone.rndr(_rhino_id)
        self.stat = Cone.stat(_rhino_id)
        self.test = Cone.test(_rhino_id)
        self.trfm = Cone.trfm(_rhino_id)
        self.util = Cone.util(_rhino_id)

    @staticmethod
    def create(base_point, height_point, radius, cap=pythoncom.Empty):
        """
        
        Factory method:
        Adds a cone-shaped polysurface to the document.

        Parameters
        ==========
        base_point  (List of float, Required) - The 3-D origin point of the cone.
        height_point  (List of float, Required) - The 3-D height point of the cone.  The height point defines the height and direction of the cone.
        radius  (float, Required) - The radius at the base of the cone.  Note, tan(cone_angle) = dblRadius/ dblHeight.
        cap  (boolean, Optional) - Cap the base of the cone.  The default is to cap the cone (True).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCone
        """

        _rhino_id = _base._rsf.add_cone(base_point, height_point, radius, cap)

        if _rhino_id:
            return Cone(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_plane(base_plane, height, radius, cap=pythoncom.Empty):
        """
        
        Factory method:
        Adds a cone-shaped polysurface to the document.

        Parameters
        ==========
        base_plane  (List of float, Required) - The cone's base plane.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
        height  (float, Required) - The height of the cone.  If arrPlane is specified, then the center of the arrPlane is height * the plane's z-axis.
        radius  (float, Required) - The radius at the base of the cone.  Note, tan(cone_angle) = dblRadius/ dblHeight.
        cap  (boolean, Optional) - Cap the base of the cone.  The default is to cap the cone (True).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCone2
        """

        _rhino_id = _base._rsf.add_cone_2(base_plane, height, radius, cap)

        if _rhino_id:
            return Cone(_rhino_id)
        else:
            return None
class Cylinder(_SurfaceRoot):pass
class Cylinder(_SurfaceRoot):
    class wrap(_wrap.WrapBase, Cylinder):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class dupl(_CylinderDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class func(_SurfaceRootFuncOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class prop(_CylinderProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Cylinder
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Cylinder.defm(_rhino_id)
        self.dupl = Cylinder.dupl(_rhino_id)
        self.eval = Cylinder.eval(_rhino_id)
        self.func = Cylinder.func(_rhino_id)
        self.grps = Cylinder.grps(_rhino_id)
        self.modf = Cylinder.modf(_rhino_id)
        self.mtrl = Cylinder.mtrl(_rhino_id)
        self.prop = Cylinder.prop(_rhino_id)
        self.rndr = Cylinder.rndr(_rhino_id)
        self.stat = Cylinder.stat(_rhino_id)
        self.test = Cylinder.test(_rhino_id)
        self.trfm = Cylinder.trfm(_rhino_id)
        self.util = Cylinder.util(_rhino_id)

    @staticmethod
    def create(base_point, height_point, radius, cap=pythoncom.Empty):
        """
        
        Factory method:
        Adds a cylinder-shaped polysurface to the document.

        Parameters
        ==========
        base_point  (List of float, Required) - The 3-D base point of the cylinder.
        height_point  (List of float, Required) - The 3-D height point of the cylinder.  The height point defines the height and direction of the cylinder.
        radius  (float, Required) - The radius of the cylinder.
        cap  (boolean, Optional) - Cap the ends of the cylinder.  If omitted, the ends of the cylinder will be capped (True).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCylinder
        """

        _rhino_id = _base._rsf.add_cylinder(base_point, height_point, radius, cap)

        if _rhino_id:
            return Cylinder(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_plane(base_plane, height, radius, cap=pythoncom.Empty):
        """
        
        Factory method:
        Adds a cylinder-shaped polysurface to the document.

        Parameters
        ==========
        base_plane  (List of float, Required) - The base plane of the cylinder.
        height  (float, Required) - The height of the cylinder.
        radius  (float, Required) - The radius of the cylinder.
        cap  (boolean, Optional) - Cap the ends of the cylinder.  If omitted, the ends of the cylinder will be capped (True).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCylinder2
        """

        _rhino_id = _base._rsf.add_cylinder_2(base_plane, height, radius, cap)

        if _rhino_id:
            return Cylinder(_rhino_id)
        else:
            return None
class Ellipse(_CurveRoot):pass
class Ellipse(_CurveRoot):
    class wrap(_wrap.WrapBase, Ellipse):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class dupl(_EllipseDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class eval(_CurveRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class func(_CurveRootFuncClsd):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class modf(_CurveRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class prop(_EllipseProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class test(_CurveRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Ellipse
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Ellipse.defm(_rhino_id)
        self.dupl = Ellipse.dupl(_rhino_id)
        self.eval = Ellipse.eval(_rhino_id)
        self.func = Ellipse.func(_rhino_id)
        self.grps = Ellipse.grps(_rhino_id)
        self.modf = Ellipse.modf(_rhino_id)
        self.mtrl = Ellipse.mtrl(_rhino_id)
        self.prop = Ellipse.prop(_rhino_id)
        self.rndr = Ellipse.rndr(_rhino_id)
        self.stat = Ellipse.stat(_rhino_id)
        self.test = Ellipse.test(_rhino_id)
        self.trfm = Ellipse.trfm(_rhino_id)
        self.util = Ellipse.util(_rhino_id)

    @staticmethod
    def create(plane, x_radius, y_radius):
        """
        
        Factory method:
        Adds an elliptical curve to the document.

        Parameters
        ==========
        plane  (List of float, Required) - The plane on which the ellipse will lie. The origin of the plane will be the center point of the ellipse.
        x_radius  (float, Required) - The radius in the X-axis direction.
        y_radius  (float, Required) - The radius in the Y-axis direction.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddEllipse
        """

        _rhino_id = _base._rsf.add_ellipse(plane, x_radius, y_radius)

        if _rhino_id:
            return Ellipse(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_3pt(center, second, third):
        """
        
        Factory method:
        Adds a 3 point elliptical curve to the document.

        Parameters
        ==========
        center  (List of float, Required) - The center point of the ellipse.
        second  (List of float, Required) - The end point of the X-axis.
        third  (List of float, Required) - The end point of the Y-axis.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddEllipse3Pt
        """

        _rhino_id = _base._rsf.add_ellipse_3_pt(center, second, third)

        if _rhino_id:
            return Ellipse(_rhino_id)
        else:
            return None
class EllipticalArc(_CurveRoot):pass
class EllipticalArc(_CurveRoot):
    class wrap(_wrap.WrapBase, EllipticalArc):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class dupl(_EllipticalArcDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class eval(_CurveRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class func(_CurveRootFuncOpen):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class modf(_CurveRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class prop(_CurveRootProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class test(_CurveRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = EllipticalArc
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = EllipticalArc.defm(_rhino_id)
        self.dupl = EllipticalArc.dupl(_rhino_id)
        self.eval = EllipticalArc.eval(_rhino_id)
        self.func = EllipticalArc.func(_rhino_id)
        self.grps = EllipticalArc.grps(_rhino_id)
        self.modf = EllipticalArc.modf(_rhino_id)
        self.mtrl = EllipticalArc.mtrl(_rhino_id)
        self.prop = EllipticalArc.prop(_rhino_id)
        self.rndr = EllipticalArc.rndr(_rhino_id)
        self.stat = EllipticalArc.stat(_rhino_id)
        self.test = EllipticalArc.test(_rhino_id)
        self.trfm = EllipticalArc.trfm(_rhino_id)
        self.util = EllipticalArc.util(_rhino_id)
class GenericObject(_ObjectRoot):pass
class GenericObject(_ObjectRoot):
    class wrap(_wrap.WrapBase, GenericObject):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class prop(_ObjectRootProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class test(_ObjectRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class type(_ObjectRootType):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = GenericObject
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = GenericObject.defm(_rhino_id)
        self.grps = GenericObject.grps(_rhino_id)
        self.mtrl = GenericObject.mtrl(_rhino_id)
        self.prop = GenericObject.prop(_rhino_id)
        self.rndr = GenericObject.rndr(_rhino_id)
        self.stat = GenericObject.stat(_rhino_id)
        self.test = GenericObject.test(_rhino_id)
        self.trfm = GenericObject.trfm(_rhino_id)
        self.type = GenericObject.type(_rhino_id)
        self.util = GenericObject.util(_rhino_id)
class Line(_CurveRoot):pass
class Line(_CurveRoot):
    class wrap(_wrap.WrapBase, Line):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class dupl(_LineDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class eval(_CurveRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class func(_CurveRootFuncOpen):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class modf(_CurveRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class prop(_CurveRootProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class test(_CurveRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Line
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Line.defm(_rhino_id)
        self.dupl = Line.dupl(_rhino_id)
        self.eval = Line.eval(_rhino_id)
        self.func = Line.func(_rhino_id)
        self.grps = Line.grps(_rhino_id)
        self.modf = Line.modf(_rhino_id)
        self.mtrl = Line.mtrl(_rhino_id)
        self.prop = Line.prop(_rhino_id)
        self.rndr = Line.rndr(_rhino_id)
        self.stat = Line.stat(_rhino_id)
        self.test = Line.test(_rhino_id)
        self.trfm = Line.trfm(_rhino_id)
        self.util = Line.util(_rhino_id)

    @staticmethod
    def create(start_point, end_point):
        """
        
        Factory method:
        Adds a line curve to the current model.

        Parameters
        ==========
        start_point  (List of float, Required) - The starting point of the line.
        end_point  (List of float, Required) - The ending point of the line.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddLine
        """

        _rhino_id = _base._rsf.add_line(start_point, end_point)

        if _rhino_id:
            return Line(_rhino_id)
        else:
            return None
class Mesh(_MeshRoot):pass
class Mesh(_MeshRoot):
    class wrap(_wrap.WrapBase, Mesh):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class dupl(_MeshDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class func(_MeshRootFuncOorC):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class modf(_MeshRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class prop(_MeshRootPropOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class test(_MeshRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Mesh
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Mesh.defm(_rhino_id)
        self.dupl = Mesh.dupl(_rhino_id)
        self.func = Mesh.func(_rhino_id)
        self.grps = Mesh.grps(_rhino_id)
        self.modf = Mesh.modf(_rhino_id)
        self.mtrl = Mesh.mtrl(_rhino_id)
        self.prop = Mesh.prop(_rhino_id)
        self.rndr = Mesh.rndr(_rhino_id)
        self.stat = Mesh.stat(_rhino_id)
        self.test = Mesh.test(_rhino_id)
        self.trfm = Mesh.trfm(_rhino_id)
        self.util = Mesh.util(_rhino_id)

    @staticmethod
    def create(vertices, face_vertices, vertex_normals=pythoncom.Empty, texture_coordinates=pythoncom.Empty, vertex_colors=pythoncom.Empty):
        """
        
        Factory method:
        Adds a mesh object to the document.

        Parameters
        ==========
        vertices  (List of float, Required) - An list of 3-D points defining the vertices of the mesh.
        face_vertices  (List of integer, Required) - An list containing lists of four numbers that define the vertex indices for each face of the mesh. If the third and forth vertex indices of a face are identical, a triangular face will be created. Otherwise a quad face will be created.
        vertex_normals  (List of float, Optional) - An list of 3-D vectors defining the vertex normals of the mesh. Note, for every vertex, the must be a corresponding vertex normal.
        texture_coordinates  (List of float, Optional) - An list of 2-D texture coordinates. Note, for every vertex, there must be a corresponding texture coordinate.
        vertex_colors  (List of integer, Optional) - An list of RGB color values. Note, for every vertex, there must be a corresponding vertex color.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddMesh
        """

        _rhino_id = _base._rsf.add_mesh(vertices, face_vertices, vertex_normals, texture_coordinates, vertex_colors)

        if _rhino_id:
            return Mesh(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_polyline(polyline):
        """
        
        Factory method:
        Creates a polygon mesh object based on a closed polyline curve object. The newly created polygon mesh object is added to the document.

        Parameters
        ==========
        polyline  (Polyline, Required) - The identifier of the polyline curve object.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshPolyline
        """

        _rhino_id = _base._rsf.mesh_polyline(polyline._rhino_id)

        if _rhino_id:
            return Mesh(_rhino_id)
        else:
            return None
class NurbsCurve(_CurveRoot):pass
class NurbsCurve(_CurveRoot):
    class wrap(_wrap.WrapBase, NurbsCurve):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class dupl(_NurbsCurveDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class eval(_CurveRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class func(_CurveRootFuncOorC):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class modf(_CurveRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class prop(_CurveRootProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class test(_CurveRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsCurve
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = NurbsCurve.defm(_rhino_id)
        self.dupl = NurbsCurve.dupl(_rhino_id)
        self.eval = NurbsCurve.eval(_rhino_id)
        self.func = NurbsCurve.func(_rhino_id)
        self.grps = NurbsCurve.grps(_rhino_id)
        self.modf = NurbsCurve.modf(_rhino_id)
        self.mtrl = NurbsCurve.mtrl(_rhino_id)
        self.prop = NurbsCurve.prop(_rhino_id)
        self.rndr = NurbsCurve.rndr(_rhino_id)
        self.stat = NurbsCurve.stat(_rhino_id)
        self.test = NurbsCurve.test(_rhino_id)
        self.trfm = NurbsCurve.trfm(_rhino_id)
        self.util = NurbsCurve.util(_rhino_id)

    @staticmethod
    def create_by_pnts(points, degree=pythoncom.Empty):
        """
        
        Factory method:
        Adds a control points curve object to the document.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.
        degree  (integer, Optional) - The degree of the curve.  If omitted, a degree 3 curve is created.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCurve
        """

        _rhino_id = _base._rsf.add_curve(points, degree)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create_interp_crv_on_srf(surface, points):
        """
        
        Factory method:
        Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

        Parameters
        ==========
        surface  (NurbsCurve, Required) - The surface object's identifier.
        points  (List of float, Required) - An list of 3-D points that lie on the specified surface. The list must contain at least two points.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddInterpCrvOnSrf
        """

        _rhino_id = _base._rsf.add_interp_crv_on_srf(surface._rhino_id, points)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create_interp_crv_on_srf_uv(surface, points):
        """
        
        Factory method:
        Adds an interpolated curve object. based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

        Parameters
        ==========
        surface  (NurbsCurve, Required) - The surface object's identifier.
        points  (List of float, Required) - An list of 2-D surface parameters. The list must contain at least two sets of surface parameters.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddInterpCrvOnSrfUV
        """

        _rhino_id = _base._rsf.add_interp_crv_on_srf_u_v(surface._rhino_id, points)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create_interp_crv(points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, start_tan=pythoncom.Empty, end_tan=pythoncom.Empty):
        """
        
        Factory method:
        Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.

        Parameters
        ==========
        points  (List of float, Required) - An list containing 3-D points to interpolate.  For periodic curves, if the final point is a duplicate of the initial point, it is ignored. Note, the number of control points must be >= (intDegree+1).
        degree  (integer, Optional) - The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.  For intKnotStyle = 4 or 5, the degree must be odd.
        knot_style  (integer, Optional) - The knot style to use, and whether the curve should be periodic.  If omitted, uniform knots (0) are created.
		Value
		Description
		0
		Uniform knots.  Parameter spacing between consecutive knots is 1.0.
		1
		Chord length spacing.  Requires dblDegree = 3 with arrCV1 and arrCVn1 specified.
		2
		Sqrt (chord length).  Requires dblDegree = 3 with arrCV1 and arrCVn1 specified.
		3
		Periodic with uniform spacing.
		4
		Periodic with chord length spacing.  Requires an odd degree value.
		5
        start_tan  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the beginning of the curve. If the curve is to periodic, this argument must be omitted.
        end_tan  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the end of the curve. If the curve is to periodic, this argument must be omitted.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddInterpCurve
        """

        _rhino_id = _base._rsf.add_interp_curve(points, degree, knot_style, start_tan, end_tan)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create_interp_crv_ex(points, degree=pythoncom.Empty, knot_style=pythoncom.Empty, sharp=pythoncom.Empty, start_tangent=pythoncom.Empty, end_tangent=pythoncom.Empty):
        """
        
        Factory method:
        Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.

        Parameters
        ==========
        points  (List of float, Required) - An list containing 3-D points to interpolate. Note, the number of control points must be >= (intDegree+1).
        degree  (integer, Optional) - The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.
        knot_style  (integer, Optional) - The knot style to use. If omitted, a knot style = 0 is used. The knot style determines how an interpolated curve will be parameterized.
		Value
		Description
		0
		Uniform.  The knot spacing is always 1 and is not based on the physical spacing of points.
		1
		Chord. The spacing between the points is used for the knot spacing
		2
        sharp  (boolean, Optional) - If True, when you create a closed curve, it will have a kink at the start/end point. If False (default), a smooth closure will be created.
        start_tangent  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the beginning of the curve.
        end_tangent  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the end of the curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddInterpCurveEx
        """

        _rhino_id = _base._rsf.add_interp_curve_ex(points, degree, knot_style, sharp, start_tangent, end_tangent)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create(points, knots, degree, weights=pythoncom.Empty):
        """
        
        Factory method:
        Adds a NURBS curve object to the document.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D control points.
        knots  (List of integer, Required) - The knot values for the curve.  The number of elements in arrKnots must equal the number of elements in arrPoints plus intDegree minus one (1).
        degree  (integer, Required) - The degree of the curve.  The degree must be greater than or equal to one (1).
        weights  (List of integer, Optional) - The weight values for the curve.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddNurbsCurve
        """

        _rhino_id = _base._rsf.add_nurbs_curve(points, knots, degree, weights)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_srf_contour(surface, start_point, end_point, interval=pythoncom.Empty):
        """
        
        Factory method:
        Adds a spaced series of planar curves resulting from the intersection of a defined cutting planes through a surface or a polysurface. For more information, see the Rhino help file for details on the Contour command.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of a surface or polysurface object.
        start_point  (List of float, Required) - The 3-D starting point of a center line.
        end_point  (List of float, Required) - The 3-D ending point of a center line.
        interval  (float, Optional) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSrfContourCrvs
        """

        _rhino_id = _base._rsf.add_srf_contour_crvs(surface._rhino_id, start_point, end_point, interval)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_srf_contour_cut_plane(surface, cut_plane, interval=pythoncom.Empty):
        """
        
        Factory method:
        Adds a spaced series of planar curves resulting from the intersection of a defined cutting planes through a surface or a polysurface. For more information, see the Rhino help file for details on the Contour command.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of a surface or polysurface object.
        cut_plane  (List of float, Required) - A plane that defines the cutting plane.
        interval  (float, Optional) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSrfContourCrvs2
        """

        _rhino_id = _base._rsf.add_srf_contour_crvs_2(surface._rhino_id, cut_plane, interval)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_srf_section(surface, cut_plane):
        """
        
        Factory method:
        Adds planar curves resulting from the intersection of a defined cutting plane through a surface or a polysurface. For more information, see the Rhino help file for details on the Section command.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of a surface or polysurface object.
        cut_plane  (List of float, Required) - A plane that defines the cutting plane.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSrfSectionCrvs
        """

        _rhino_id = _base._rsf.add_srf_section_crvs(surface._rhino_id, cut_plane)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_srf_edge(surface, select=pythoncom.Empty):
        """
        
        Factory method:
        Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of the surface or polysurface object.
        select  (boolean, Optional) - Select the duplicated edge curves.  The default is not to select (False).

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DuplicateEdgeCurves
        """

        _rhino_id = _base._rsf.duplicate_edge_curves(surface._rhino_id, select)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_srf_border(surface):
        """
        
        Factory method:
        Creates a curve that duplicates a surface or polysurface border.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of the surface or polysurface object.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DuplicateSurfaceBorder
        """

        _rhino_id = _base._rsf.duplicate_surface_border(surface._rhino_id)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_srf_iso_curve(surface, parameter, dir):
        """
        
        Factory method:
        Extracts isoparametric curves from a surface.

        Parameters
        ==========
        surface  (surface object, Required) - The object's identifier.
        parameter  (List of float, Required) - An list containing the U,V parameter of the surface to evaluate.
        dir  (integer, Required) - The direction, either 0 = U, 1 = V, or 2 = Both.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtractIsoCurve
        """

        _rhino_id = _base._rsf.extract_iso_curve(surface._rhino_id, parameter, dir)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_fit(curve, degree=pythoncom.Empty, tolerance=pythoncom.Empty, angle_tolerance=pythoncom.Empty):
        """
        
        Factory method:
        Reduces the number of curve control points while maintaining the curve's same general shape.  Use this function for replacing curves with too many control points.  For more information, see the Rhino help file for the FitCrv command.

        Parameters
        ==========
        curve  (curve object, Required) - The object's identifier.
        degree  (integer, Optional) - The curve degree, which must be greater than 1. The default is 3.
        tolerance  (float, Optional) - The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.
        angle_tolerance  (float, Optional) - The kink smoothing tolerance in degrees.  If dblAngleTolerance is 0.0, all kinks are smoothed.  If dblAngleTolerance is > 0.0, kinks smaller than dblAngleTolerance are smoothed.  If dblAngleTolerance is not specified or < 0.0, the document angle tolerance is used for the kink smoothing.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: FitCurve
        """

        _rhino_id = _base._rsf.fit_curve(curve._rhino_id, degree, tolerance, angle_tolerance)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_projection_to_mesh(curves, meshes, direction_vector):
        """
        
        Factory method:
        Projects one or more points onto one or more meshes.

        Parameters
        ==========
        curves  (list of array_of _ObjectRoot, Required) - The identifiers of one or more curve objects to project.
        meshes  (list of surface object, Required) - The identifiers of the mesh objects to project onto.
        direction_vector  (List of float, Required) - The direction (3-D vector) to project the points.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ProjectCurveToMesh
        """
        if type(curves) != list and type(curves) != tuple:
            curves = (curves,)
        if type(meshes) != list and type(meshes) != tuple:
            meshes = (meshes,)

        _rhino_id = _base._rsf.project_curve_to_mesh(map(lambda i: i._rhino_id, curves), map(lambda i: i._rhino_id, meshes), direction_vector)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_projection_to_srf(curve, surfaces, direction_vector):
        """
        
        Factory method:
        Projects one or more points onto one or more surfaces or polysurfaces.

        Parameters
        ==========
        curve  (NurbsCurve, Required) - The identifiers of one or more curve objects to project.
        surfaces  (list of surface object, Required) - The identifiers of the surface or polysurface objects to project onto.
        direction_vector  (List of float, Required) - The direction (3-D vector) to project the points.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ProjectCurveToSurface
        """
        if type(surfaces) != list and type(surfaces) != tuple:
            surfaces = (surfaces,)

        _rhino_id = _base._rsf.project_curve_to_surface(curve._rhino_id, map(lambda i: i._rhino_id, surfaces), direction_vector)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_srf_pull(surface, curve, delete=pythoncom.Empty):
        """
        
        Factory method:
        Pulls a curve object to a surface object. For more information, see the Rhino help file for information on the Pull command.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of the surface object that pulls.
        curve  (curve object, Required) - The identifier of the curve object to pull.
        delete  (boolean, Optional) - Delete input curve.  If omitted, the input curve will not be deleted (False).

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PullCurve
        """

        _rhino_id = _base._rsf.pull_curve(surface._rhino_id, curve._rhino_id, delete)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_srf_short_path(surface, start_point, end_point):
        """
        
        Factory method:
        Creates the shortest possible curve (geodesic) between two points on a surface. For more details, see the ShortPath command in the Rhino help file.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of the surface object that pulls.
        start_point  (List of float, Required) - A 3-D surface point identifying the starting point of the short curve.
        end_point  (List of float, Required) - A 3-D surface point identifying the ending point of the short curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ShortPath
        """

        _rhino_id = _base._rsf.short_path(surface._rhino_id, start_point, end_point)

        if _rhino_id:
            return NurbsCurve(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_srf_principal_curvature(surface, point):
        """
        
        Factory method:
        Adds curvature curves at the evaluated point on a surface. For more information, see the Rhino help file for the Curvature command.

        Parameters
        ==========
        surface  (surface object, Required) - The curve's identifier.
        point  (List of float, Required) - A point on the curve to evaluate.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfacePrincipalCurvature
        """

        _rhino_id = _base._rsf.surface_principal_curvature(surface._rhino_id, point)

        if _rhino_id:

            return map(lambda i: NurbsCurve(i), _rhino_id)

        else:
            return None
class NurbsSurface(_SurfaceRoot):pass
class NurbsSurface(_SurfaceRoot):
    class wrap(_wrap.WrapBase, NurbsSurface):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class dupl(_NurbsSurfaceDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class func(_SurfaceRootFuncOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class prop(_SurfaceRootPropOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = NurbsSurface
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = NurbsSurface.defm(_rhino_id)
        self.dupl = NurbsSurface.dupl(_rhino_id)
        self.eval = NurbsSurface.eval(_rhino_id)
        self.func = NurbsSurface.func(_rhino_id)
        self.grps = NurbsSurface.grps(_rhino_id)
        self.modf = NurbsSurface.modf(_rhino_id)
        self.mtrl = NurbsSurface.mtrl(_rhino_id)
        self.prop = NurbsSurface.prop(_rhino_id)
        self.rndr = NurbsSurface.rndr(_rhino_id)
        self.stat = NurbsSurface.stat(_rhino_id)
        self.test = NurbsSurface.test(_rhino_id)
        self.trfm = NurbsSurface.trfm(_rhino_id)
        self.util = NurbsSurface.util(_rhino_id)

    @staticmethod
    def create_by_cut_plane(objects, start_point, end_point, normal_vector=pythoncom.Empty):
        """
        
        Factory method:
        Adds a planar surface through objects at a designated location.  For more information, see the Rhino help file for the CutPlane command.

        Parameters
        ==========
        objects  (list of array_of _ObjectRoot, Required) - The identifiers of objects that the cutting planes will pass through.
        start_point  (List of float, Required) - The start of the line that defines the cutting plane.
        end_point  (List of float, Required) - The end of the line that defines the cutting plane.
        normal_vector  (List of float, Optional) - In the case of Rhino's CutPlane command, this is the normal to, or Z axis of, the active view's construction plane.  If omitted, the world Z axis is used.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddCutPlane
        """
        if type(objects) != list and type(objects) != tuple:
            objects = (objects,)

        _rhino_id = _base._rsf.add_cut_plane(map(lambda i: i._rhino_id, objects), start_point, end_point, normal_vector)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_edge(edge_curves):
        """
        
        Factory method:
        Creates a surface from 2, 3, or 4 edge curves.

        Parameters
        ==========
        edge_curves  (list of curve object, Required) - An list of 2, 3, or 4 curve object identifiers.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddEdgeSrf
        """
        if type(edge_curves) != list and type(edge_curves) != tuple:
            edge_curves = (edge_curves,)

        _rhino_id = _base._rsf.add_edge_srf(map(lambda i: i._rhino_id, edge_curves))

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_loft(section_curves, start_point=pythoncom.Empty, end_point=pythoncom.Empty, srf_type=pythoncom.Empty, style=pythoncom.Empty, value=pythoncom.Empty, closed=pythoncom.Empty):
        """
        
        Factory method:
        Adds a surface created by lofting curves to the document.
		* This function will not perform any curve sorting. You must pass in curves in the order you want them lofted.
		* This function will not adjust the directions of open curves. Use CurveDirectionsMatch and ReverseCurve to adjust the directions of open curves.
		* This function will not adjust the seams of closed curves. Use CurveSeam to adjust the seam of closed curves.

        Parameters
        ==========
        section_curves  (list of curve object, Required) - An ordered list of strings identifying the curve objects to loft.
        start_point  (List of float, Optional) - The starting point of the loft.
        end_point  (List of float, Optional) - The ending point of the loft.
        srf_type  (integer, Optional) - The type of loft. The default loft type is Normal (0). The possible loft types are as follows:
		Value
		Description
		0
		Normal. Uses chord-length parameterization in the loft direction.
		1
		Loose. The surface is allowed to move away from the original curves to make a smoother surface. The surface control points are created at the same locations as the control points of the loft input curves.
		2
		Straight. The sections between the curves are straight. This is also known as a ruled surface.
		3
		Tight. The surface sticks closely to the original curves. Uses square root of chord-length parameterization in the loft direction.
		4
        style  (integer, Optional) - The simplify method of the loft. The default value is None (0). The possible loft simplify methods are as follows:
		Value
		Description
		0
		None. Does not simplify.
		1
		Rebuild. Rebuilds the shape curves before lofting.
		2
        value  (integer, Optional) - A value based on the specified intStyle. If intStyle=1 (Rebuild), then nValue is the number of control point used to rebuild. If intstyle=1 is specified and this argument is omitted, then curves will be rebuilt using 10 control points. If intStyle=2 (Refit), then nValue is the tolerance used to rebuild. If intstyle=2 is specified and this argument is omitted, then the document's absolute tolerance us used for refitting.
        closed  (boolean, Optional) - Creates a closed surface, continuing the surface past the last curve around to the first curve. Available when you have selected three shape curves. The default value is not to create a closed surface (False).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddLoftSrf
        """
        if type(section_curves) != list and type(section_curves) != tuple:
            section_curves = (section_curves,)

        _rhino_id = _base._rsf.add_loft_srf(map(lambda i: i._rhino_id, section_curves), start_point, end_point, srf_type, style, value, closed)

        if _rhino_id:
            return NurbsSurface(_rhino_id[0])
        else:
            return None

    @staticmethod
    def create(point_count, points, knots_u, knots_v, degree, weights):
        """
        
        Factory method:
        Adds a NURBS surface object to the document.

        Parameters
        ==========
        point_count  (List of integer, Required) - The number of control points in the U and V directions.
        points  (List of float, Required) - An list of 3-D control points.
        knots_u  (List of integer, Required) - The knot values for the surface in the U direction.  The list must contain arrPointCount(0) + arrDegree(0) - 1 elements.
        knots_v  (List of integer, Required) - The knot values for the surface in the V direction.  The list must contain arrPointCount(1) + arrDegree(1) - 1 elements.
        degree  (List of integer, Required) - The degree of the surface in the U and V directions.  The degree in each direction must be greater than or equal to one (1).
        weights  (List of integer, Required) - The weight values for the surface.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddNurbsSurface
        """

        _rhino_id = _base._rsf.add_nurbs_surface(point_count, points, knots_u, knots_v, degree, weights)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_planar_crv(planar_curves):
        """
        
        Factory method:
        Creates one or more surfaces from planar curves.

        Parameters
        ==========
        planar_curves  (list of curve object, Required) - An list of curve object identifiers.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPlanarSrf
        """
        if type(planar_curves) != list and type(planar_curves) != tuple:
            planar_curves = (planar_curves,)

        _rhino_id = _base._rsf.add_planar_srf(map(lambda i: i._rhino_id, planar_curves))

        if _rhino_id:
            return NurbsSurface(_rhino_id[0])
        else:
            return None

    @staticmethod
    def create_by_rail_rev(profile, rail, axis):
        """
        
        Factory method:
        Create a surface by revolving a profile curve along a rail curve.

        Parameters
        ==========
        profile  (curve object, Required) - The identifier of the profile curve.
        rail  (curve object, Required) - The identifier of the rail curve.
        axis  (List of float, Required) - An list of two 3-D points identifying the start point and end point of the rail revolve axis.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddRailRevSrf
        """

        _rhino_id = _base._rsf.add_rail_rev_srf(profile._rhino_id, rail._rhino_id, axis)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_rev(profile, axis, start_angle=pythoncom.Empty, end_angle=pythoncom.Empty):
        """
        
        Factory method:
        Create a surface by revolving a curve around an axis.

        Parameters
        ==========
        profile  (curve object, Required) - The identifier of the curve to revolve.
        axis  (List of float, Required) - An list of two 3-D points identifying the start point and end point of the rail revolve axis.
        start_angle  (float, Optional) - The starting angle. If omitted, an angle of 0.0 is used.
        end_angle  (float, Optional) - The ending angle. If omitted, an angle of 360.0 is used.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddRevSrf
        """

        _rhino_id = _base._rsf.add_rev_srf(profile._rhino_id, axis, start_angle, end_angle)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_control_pnt_grid(count, points, degree=pythoncom.Empty):
        """
        
        Factory method:
        Creates a surface from a grid of control points.

        Parameters
        ==========
        count  (List of integer, Required) - The number of control points in the U and V directions.
        points  (List of float, Required) - An list of 3-D control points.
        degree  (List of float, Optional) - The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSrfControlPtGrid
        """

        _rhino_id = _base._rsf.add_srf_control_pt_grid(count, points, degree)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_corner_pnts(points):
        """
        
        Factory method:
        Creates a new surface from either 3 or 4 corner points.

        Parameters
        ==========
        points  (List of float, Required) - An list of either 3 or 4 corner points.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSrfPt
        """

        _rhino_id = _base._rsf.add_srf_pt(points)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_pnt_grid(count, points, degree=pythoncom.Empty, closed=pythoncom.Empty):
        """
        
        Factory method:
        Creates a surface from a grid of points.

        Parameters
        ==========
        count  (List of integer, Required) - The number of points in the U and V directions.
        points  (List of float, Required) - An list of 3-D points.
        degree  (List of integer, Optional) - The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.
        closed  (List of boolean, Optional) - Whether or not the surface is closed in the U and V directions.  If omitted, the new surface will not be closed in either the U or V directions.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSrfPtGrid
        """

        _rhino_id = _base._rsf.add_srf_pt_grid(count, points, degree, closed)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_sweep_1(rail, shapes, start_point=pythoncom.Empty, end_point=pythoncom.Empty, closed=pythoncom.Empty, style=pythoncom.Empty, style_arg=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):
        """
        
        Factory method:
        Adds a surface created through profile curves that define the surface shape and one curve that defines a surface edge. For more details on this method, see the Rhino help file for the Sweep1 command.
		Note, this method does not perform any curve sorting or direction matching on the input shape curves. This is the responsibility of the script writer.
		For best results:
		* The shape curves should all be oriented in the same direction.
		* The starting point of each shape curve should either intersect with or be close to the rail curve.
		* The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.

        Parameters
        ==========
        rail  (curve object, Required) - The identifier of the rail curve.
        shapes  (list of curve object, Required) - An list of strings identifying one or more shape, or cross section, curves.
        start_point  (List of float, Optional) - The 3-D starting point of the surface.
        end_point  (List of float, Optional) - The 3-D ending point of the surface.
        closed  (boolean, Optional) - If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
        style  (integer, Optional) - The sweep style, where 0 = Freeform and 1 = Roadlike. The default value is 0 = Freeform.
        style_arg  (list, Optional) - If intStyle = 1 (Roadlike), then this argument is a 3-D vector identifying the planar up direction for the sweep.
        simplify  (integer, Optional) - Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
        simplify_arg  (list, Optional) - If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance.  If intSimplify = 2 (Rebuild), then this argument is a number specifying the number of control points to rebuild the shape curves.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSweep1
        """
        if type(shapes) != list and type(shapes) != tuple:
            shapes = (shapes,)

        _rhino_id = _base._rsf.add_sweep_1(rail._rhino_id, map(lambda i: i._rhino_id, shapes), start_point, end_point, closed, style, style_arg, simplify, simplify_arg)

        if _rhino_id:
            return NurbsSurface(_rhino_id[0])
        else:
            return None

    @staticmethod
    def create_by_sweep_2(rails, shapes, start_point=pythoncom.Empty, end_point=pythoncom.Empty, closed=pythoncom.Empty, simple_sweep=pythoncom.Empty, maintain_height=pythoncom.Empty, simplify=pythoncom.Empty, simplify_arg=pythoncom.Empty):
        """
        
        Factory method:
        Adds a surface created through profile curves that define the surface shape and two curves that define the surface edges. For more details on this method, see the Rhino help file for the Sweep2 command.
		Note, this method does not perform any curve sorting or direction matching on the input shape curves. This is the responsibility of the script writer.
		For best results:
		* The shape curves should all be oriented in the same direction.
		* The starting point of each shape curve should either intersect with or be close to the first rail curve.
		* The ending point of each shape curve should either intersect with or be close to the second rail curve.
		* The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.

        Parameters
        ==========
        rails  (list of curve object, Required) - An list of strings identifying two rail curves.
        shapes  (list of curve object, Required) - An list of strings identifying one or more shape, or cross section, curves.
        start_point  (List of float, Optional) - The 3-D starting point of the surface.
        end_point  (List of float, Optional) - The 3-D ending point of the surface.
        closed  (boolean, Optional) - If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
        simple_sweep  (boolean, Optional) - If True, then create surfaces using exact input. This option generates simpler surfaces in cases when the curves are perfectly set up.  The default value is False.
        maintain_height  (boolean, Optional) - By default, shape curves normally scale in both the height and width dimensions. To remove the association between the height scaling from the width scaling, set this value to True.  The default value is False.
        simplify  (integer, Optional) - Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
        simplify_arg  (list, Optional) - If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance.  If intSimplify = 2 (Rebuild), then this argument is a number specifying the number of control points to rebuild the shape curves.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSweep2
        """
        if type(rails) != list and type(rails) != tuple:
            rails = (rails,)
        if type(shapes) != list and type(shapes) != tuple:
            shapes = (shapes,)

        _rhino_id = _base._rsf.add_sweep_2(map(lambda i: i._rhino_id, rails), map(lambda i: i._rhino_id, shapes), start_point, end_point, closed, simple_sweep, maintain_height, simplify, simplify_arg)

        if _rhino_id:
            return NurbsSurface(_rhino_id[0])
        else:
            return None

    @staticmethod
    def create_by_extrude_crv(curve, path):
        """
        
        Factory method:
        Creates a surface by extruding a curve along a path curve.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the curve object to extrude.
        path  (string, Required) - The identifier of the path curve.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtrudeCurve
        """

        _rhino_id = _base._rsf.extrude_curve(curve._rhino_id, path)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_extrude_crv_pnt(curve, point):
        """
        
        Factory method:
        Creates a surface by extruding a curve to a point.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the curve object to extrude.
        point  (List of float, Required) - A 3-D point.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtrudeCurvePoint
        """

        _rhino_id = _base._rsf.extrude_curve_point(curve._rhino_id, point)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_extrude_crv_straight(curve, start_point, end_point):
        """
        
        Factory method:
        Creates a surface by extruding a curve straight along two points that define a line.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the curve object to extrude.
        start_point  (List of float, Required) - A starting point.
        end_point  (List of float, Required) - A ending point.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtrudeCurveStraight
        """

        _rhino_id = _base._rsf.extrude_curve_straight(curve._rhino_id, start_point, end_point)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_extrude_crv_tapered(curve, distance, direction, base_point, angle, corner_type=pythoncom.Empty):
        """
        
        Factory method:
        Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the curve object to extrude.
        distance  (float, Required) - The extrusion distance.
        direction  (List of float, Required) - A 3-D vector that specifies the extrusion direction.
        base_point  (List of float, Required) - A 3-D point that specifies the base point of the extrusion.
        angle  (float, Required) - The angle of the extrusion.
        corner_type  (integer, Optional) - The corner type of the extrusion, where:
		Value
		Description
		0 (Default)
		No corner
		1
		Sharp - Offsets and extends curves with a straight line until they intersect.
		2
		Round - Offsets and fillets curves with an arc of radius equal to the offset distance.
		3
		Smooth - Offsets and connects curves with a smooth (G1 continuity) curve.
		4

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtrudeCurveTapered
        """

        _rhino_id = _base._rsf.extrude_curve_tapered(curve._rhino_id, distance, direction, base_point, angle, corner_type)

        if _rhino_id:

            return map(lambda i: NurbsSurface(i), _rhino_id)

        else:
            return None

    @staticmethod
    def create_by_fit(surface, degree=pythoncom.Empty, tolerance=pythoncom.Empty):
        """
        
        Factory method:
        Reduces the number of surface control points while maintaining the surfaces' same general shape.  Use this function for replacing surface with too many control points.  For more information, see the Rhino help file for the FitSrf command.

        Parameters
        ==========
        surface  (surface object, Required) - The object's identifier.
        degree  (List of integer, Optional) - An list of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3.
        tolerance  (float, Optional) - The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: FitSurface
        """

        _rhino_id = _base._rsf.fit_surface(surface._rhino_id, degree, tolerance)

        if _rhino_id:
            return NurbsSurface(_rhino_id)
        else:
            return None
class PlanarMesh(_MeshRoot):pass
class PlanarMesh(_MeshRoot):
    class wrap(_wrap.WrapBase, PlanarMesh):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class dupl(_PlanarMeshDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class func(_MeshRootFuncOpen):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class modf(_MeshRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class prop(_MeshRootPropOpen):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class test(_MeshRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlanarMesh
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = PlanarMesh.defm(_rhino_id)
        self.dupl = PlanarMesh.dupl(_rhino_id)
        self.func = PlanarMesh.func(_rhino_id)
        self.grps = PlanarMesh.grps(_rhino_id)
        self.modf = PlanarMesh.modf(_rhino_id)
        self.mtrl = PlanarMesh.mtrl(_rhino_id)
        self.prop = PlanarMesh.prop(_rhino_id)
        self.rndr = PlanarMesh.rndr(_rhino_id)
        self.stat = PlanarMesh.stat(_rhino_id)
        self.test = PlanarMesh.test(_rhino_id)
        self.trfm = PlanarMesh.trfm(_rhino_id)
        self.util = PlanarMesh.util(_rhino_id)

    @staticmethod
    def create_by_crv(curve, delete=pythoncom.Empty):
        """
        
        Factory method:
        Creates a planar mesh from a closed, planar curve.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of a closed, planar curve object.
        delete  (boolean, Optional) - If True, then the input curve will be deleted. If not specified or False (default), then the input curve will not be deleted.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPlanarMesh
        """

        _rhino_id = _base._rsf.add_planar_mesh(curve._rhino_id, delete)

        if _rhino_id:
            return PlanarMesh(_rhino_id)
        else:
            return None
class PlaneSurface(_SurfaceRoot):pass
class PlaneSurface(_SurfaceRoot):
    class wrap(_wrap.WrapBase, PlaneSurface):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class dupl(_PlaneSurfaceDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class func(_SurfaceRootFuncOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class prop(_SurfaceRootPropOpen):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PlaneSurface
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = PlaneSurface.defm(_rhino_id)
        self.dupl = PlaneSurface.dupl(_rhino_id)
        self.eval = PlaneSurface.eval(_rhino_id)
        self.func = PlaneSurface.func(_rhino_id)
        self.grps = PlaneSurface.grps(_rhino_id)
        self.modf = PlaneSurface.modf(_rhino_id)
        self.mtrl = PlaneSurface.mtrl(_rhino_id)
        self.prop = PlaneSurface.prop(_rhino_id)
        self.rndr = PlaneSurface.rndr(_rhino_id)
        self.stat = PlaneSurface.stat(_rhino_id)
        self.test = PlaneSurface.test(_rhino_id)
        self.trfm = PlaneSurface.trfm(_rhino_id)
        self.util = PlaneSurface.util(_rhino_id)

    @staticmethod
    def create(base_plane, d_u, d_v):
        """
        
        Factory method:
        Creates a plane surface.

        Parameters
        ==========
        base_plane  (List of float, Required) - The plane.
        d_u  (float, Required) - The magnitude in the U direction.
        d_v  (float, Required) - The magnitude in the V direction.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPlaneSurface
        """

        _rhino_id = _base._rsf.add_plane_surface(base_plane, d_u, d_v)

        if _rhino_id:
            return PlaneSurface(_rhino_id)
        else:
            return None
class PolyCurve(_CurveRoot):pass
class PolyCurve(_CurveRoot):
    class wrap(_wrap.WrapBase, PolyCurve):pass
    class dupl(_PolyCurveDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class func(_PolyCurveFunc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class prop(_ObjectRootProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolyCurve
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.dupl = PolyCurve.dupl(_rhino_id)
        self.func = PolyCurve.func(_rhino_id)
        self.grps = PolyCurve.grps(_rhino_id)
        self.mtrl = PolyCurve.mtrl(_rhino_id)
        self.prop = PolyCurve.prop(_rhino_id)
        self.rndr = PolyCurve.rndr(_rhino_id)
        self.stat = PolyCurve.stat(_rhino_id)
        self.trfm = PolyCurve.trfm(_rhino_id)
        self.util = PolyCurve.util(_rhino_id)

    @staticmethod
    def create(curves, delete=pythoncom.Empty):
        """
        
        Factory method:
        Joins two or more curve object together to form one or more curves or polycurves.

        Parameters
        ==========
        curves  (list of curve object, Required) - A list of curve objects to join.
        delete  (boolean, Optional) - Delete input objects after joining.  The default is not to delete objects (False).

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: JoinCurves
        """
        if type(curves) != list and type(curves) != tuple:
            curves = (curves,)

        _rhino_id = _base._rsf.join_curves(map(lambda i: i._rhino_id, curves), delete)

        if _rhino_id:

            return map(lambda i: PolyCurve(i), _rhino_id)

        else:
            return None
class PolySurface(_SurfaceRoot):pass
class PolySurface(_SurfaceRoot):
    class wrap(_wrap.WrapBase, PolySurface):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class dupl(_PolySurfaceDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class func(_PolySurfaceFunc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = PolySurface
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = PolySurface.defm(_rhino_id)
        self.dupl = PolySurface.dupl(_rhino_id)
        self.eval = PolySurface.eval(_rhino_id)
        self.func = PolySurface.func(_rhino_id)
        self.grps = PolySurface.grps(_rhino_id)
        self.modf = PolySurface.modf(_rhino_id)
        self.mtrl = PolySurface.mtrl(_rhino_id)
        self.rndr = PolySurface.rndr(_rhino_id)
        self.stat = PolySurface.stat(_rhino_id)
        self.test = PolySurface.test(_rhino_id)
        self.trfm = PolySurface.trfm(_rhino_id)
        self.util = PolySurface.util(_rhino_id)

    @staticmethod
    def create_by_srf_extrude(surface, curve, cap=pythoncom.Empty):
        """
        
        Factory method:
        Creates a surface or solid by extruding a straight along a path curve.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of the surface object to extrude.
        curve  (string, Required) - The identifier of the path curve.
        cap  (boolean, Optional) - Extrusion is capped at both ends to make a closed polysurface. The default value is True.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtrudeSurface
        """

        _rhino_id = _base._rsf.extrude_surface(surface._rhino_id, curve, cap)

        if _rhino_id:
            return PolySurface(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_srf_join(surfaces, delete=pythoncom.Empty):
        """
        
        Factory method:
        Joins two or more surface or polysurface object together to form one polysurface object.

        Parameters
        ==========
        surfaces  (list of surface object, Required) - An ordered list of strings identifying the surfaces or polysurfaces objects to join.
        delete  (boolean, Optional) - Delete input objects after joining.  The default is not to delete objects (False).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: JoinSurfaces
        """
        if type(surfaces) != list and type(surfaces) != tuple:
            surfaces = (surfaces,)

        _rhino_id = _base._rsf.join_surfaces(map(lambda i: i._rhino_id, surfaces), delete)

        if _rhino_id:
            return PolySurface(_rhino_id)
        else:
            return None
class Polyline(_CurveRoot):pass
class Polyline(_CurveRoot):
    class wrap(_wrap.WrapBase, Polyline):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class dupl(_PolylineDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class eval(_CurveRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class func(_CurveRootFuncOorC):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class modf(_CurveRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class prop(_PolylineProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class test(_CurveRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Polyline
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Polyline.defm(_rhino_id)
        self.dupl = Polyline.dupl(_rhino_id)
        self.eval = Polyline.eval(_rhino_id)
        self.func = Polyline.func(_rhino_id)
        self.grps = Polyline.grps(_rhino_id)
        self.modf = Polyline.modf(_rhino_id)
        self.mtrl = Polyline.mtrl(_rhino_id)
        self.prop = Polyline.prop(_rhino_id)
        self.rndr = Polyline.rndr(_rhino_id)
        self.stat = Polyline.stat(_rhino_id)
        self.test = Polyline.test(_rhino_id)
        self.trfm = Polyline.trfm(_rhino_id)
        self.util = Polyline.util(_rhino_id)

    @staticmethod
    def create(points):
        """
        
        Factory method:
        Adds a polyline curve object to the current model.

        Parameters
        ==========
        points  (List of float, Required) - An list of 3-D points.  Duplicate, consecutive points found in the list will be removed.  The list must contain at least two 3-D points.  If the list contains less than four points, then the first point and the last point must be different.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddPolyline
        """

        _rhino_id = _base._rsf.add_polyline(points)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_crv(curve, angle_tolerance=pythoncom.Empty, tolerance=pythoncom.Empty, delete_input=pythoncom.Empty):
        """
        
        Factory method:
        Converts a curve to a polyline curve.

        Parameters
        ==========
        curve  (curve object, Required) - The object's identifier.
        angle_tolerance  (float, Optional) - The maximum angle between curve tangents at line endpoints.  If omitted, the angle tolerance is set to 5.0.
        tolerance  (float, Optional) - The distance tolerance at segment midpoints.  If omitted, the tolerance is set to 0.01.
        delete_input  (boolean, Optional) - Delete the curve object specified by strObject.  If omitted, strObject will not be deleted.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ConvertCurveToPolyline
        """

        _rhino_id = _base._rsf.convert_curve_to_polyline(curve._rhino_id, angle_tolerance, tolerance, delete_input)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_mesh_border(mesh):
        """
        
        Factory method:
        Creates a curve that duplicates a mesh border.

        Parameters
        ==========
        mesh  (mesh object, Required) - The identifier of the mesh object.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DuplicateMeshBorder
        """

        _rhino_id = _base._rsf.duplicate_mesh_border(mesh._rhino_id)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_mesh_pull(mesh, curve):
        """
        
        Factory method:
        Pulls a curve object to a mesh object. The function makes a polyline approximation of the input curve and gets the closest point on the mesh for each point on the mesh.  Then it "connects the points" so  that you have a polyline on the mesh.

        Parameters
        ==========
        mesh  (mesh object, Required) - The identifier of the mesh object that pulls.
        curve  (curve object, Required) - The identifier of the curve object to pull.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PullCurveToMesh
        """

        _rhino_id = _base._rsf.pull_curve_to_mesh(mesh._rhino_id, curve._rhino_id)

        if _rhino_id:
            return Polyline(_rhino_id)
        else:
            return None
class Sphere(_SurfaceRoot):pass
class Sphere(_SurfaceRoot):
    class wrap(_wrap.WrapBase, Sphere):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class dupl(_SphereDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class func(_SurfaceRootFuncOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class prop(_SphereProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Sphere
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Sphere.defm(_rhino_id)
        self.dupl = Sphere.dupl(_rhino_id)
        self.eval = Sphere.eval(_rhino_id)
        self.func = Sphere.func(_rhino_id)
        self.grps = Sphere.grps(_rhino_id)
        self.modf = Sphere.modf(_rhino_id)
        self.mtrl = Sphere.mtrl(_rhino_id)
        self.prop = Sphere.prop(_rhino_id)
        self.rndr = Sphere.rndr(_rhino_id)
        self.stat = Sphere.stat(_rhino_id)
        self.test = Sphere.test(_rhino_id)
        self.trfm = Sphere.trfm(_rhino_id)
        self.util = Sphere.util(_rhino_id)

    @staticmethod
    def create(center, radius):
        """
        
        Factory method:
        Adds a spherical surface to the document.

        Parameters
        ==========
        center  (List of float, Required) - The center point of the sphere.
        radius  (float, Required) - The radius of the sphere in current model units.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSphere
        """

        _rhino_id = _base._rsf.add_sphere(center, radius)

        if _rhino_id:
            return Sphere(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_plane(center, radius):
        """
        
        Factory method:
        Adds a spherical surface to the document.

        Parameters
        ==========
        center  (List of float, Required) - An equatorial plane.  The origin of the plane will be the center point of the sphere.
        radius  (float, Required) - The radius of the sphere in current model units.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSphere2
        """

        _rhino_id = _base._rsf.add_sphere_2(center, radius)

        if _rhino_id:
            return Sphere(_rhino_id)
        else:
            return None
class Torus(_SurfaceRoot):pass
class Torus(_SurfaceRoot):
    class wrap(_wrap.WrapBase, Torus):pass
    class defm(_ObjectRootDefm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class dupl(_TorusDupl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class eval(_SurfaceRootEval):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class func(_SurfaceRootFuncOorc):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class grps(_ObjectRootGrps):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class modf(_SurfaceRootMdfy):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class prop(_TorusProp):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class rndr(_ObjectRootRndr):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class stat(_ObjectRootStat):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class test(_SurfaceRootTest):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class trfm(_ObjectRootTrfm):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    class util(_ObjectRootUtil):
        def __init__(self, _rhino_id):
            self._rhino_id = _rhino_id
            self._class = Torus
    # Class constructor
    def __init__(self, _rhino_id):
        if _rhino_id==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._rhino_id = _rhino_id

        self.defm = Torus.defm(_rhino_id)
        self.dupl = Torus.dupl(_rhino_id)
        self.eval = Torus.eval(_rhino_id)
        self.func = Torus.func(_rhino_id)
        self.grps = Torus.grps(_rhino_id)
        self.modf = Torus.modf(_rhino_id)
        self.mtrl = Torus.mtrl(_rhino_id)
        self.prop = Torus.prop(_rhino_id)
        self.rndr = Torus.rndr(_rhino_id)
        self.stat = Torus.stat(_rhino_id)
        self.test = Torus.test(_rhino_id)
        self.trfm = Torus.trfm(_rhino_id)
        self.util = Torus.util(_rhino_id)

    @staticmethod
    def create(base_point, major_radius, minor_radius, direction=pythoncom.Empty):
        """
        
        Factory method:
        Adds a torus-shaped revolved surface to the document.

        Parameters
        ==========
        base_point  (List of float, Required) - The 3-D origin point of the torus.
        major_radius  (float, Required) - The major radius of the torus.  The major radius must be larger than the minor radius.
        minor_radius  (float, Required) - The minor radius of the torus.  The minor radius must be greater than zero.
        direction  (List of float, Optional) - A point that defines the direction of the torus.  If omitted, a torus that is parallel to the world XY plane is created.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddTorus
        """

        _rhino_id = _base._rsf.add_torus(base_point, major_radius, minor_radius, direction)

        if _rhino_id:
            return Torus(_rhino_id)
        else:
            return None

    @staticmethod
    def create_by_plane(base_plane, major_radius, minor_radius):
        """
        
        Factory method:
        Adds a torus-shaped revolved surface to the document.

        Parameters
        ==========
        base_plane  (List of float, Required) - The base plane of the torus.
        major_radius  (float, Required) - The major radius of the torus.  The major radius must be larger than the minor radius.
        minor_radius  (float, Required) - The minor radius of the torus.  The minor radius must be greater than zero.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddTorus2
        """

        _rhino_id = _base._rsf.add_torus_2(base_plane, major_radius, minor_radius)

        if _rhino_id:
            return Torus(_rhino_id)
        else:
            return None
