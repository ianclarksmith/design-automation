# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Curve(DispatchBaseClass):



    def add_arc(self, arr_plane, dbl_radius, dbl_angle):
        """

        Adds an arc curve to the document.

        Parameters

        arrPlane : Required, Array, The plane on which the arc will lie
        dblRadius : Required, Number, The radius arc
        dblAngle : Required, Number, A angle or interval, in degrees, of the arc

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddArc', None, arrPlane, dblRadius, dblAngle)

    def add_arc3_pt(self, arr_start, arr_end, arr_point):
        """

        Adds a 3-point arc curve to the document.

        Parameters

        arrStart : Required, Array, The starting point of the arc
        arrEnd : Required, Array, The ending point of the arc
        arrPoint : Required, Array, A point on the arc

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddArc3Pt', None, arrStart, arrEnd, arrPoint)

    def add_circle(self, arr_plane, dbl_radius):
        """

        Adds a circle curve to the document.

        Parameters

        arrPlane : Required, Array, The plane on which the circle will lie
        dblRadius : Required, Number, The radius of the circle

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddCircle', None, arrPlane, dblRadius)

    def add_circle3_pt(self, arr_start, arr_end, arr_point):
        """

        Adds a 3-point circle curve to the document.

        Parameters

        arrStart : Required, Array, The first point of the circle
        arrEnd : Required, Array, The second point of the circle
        arrPoint : Required, Array, The third point of the circle

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddCircle3Pt', None, arrStart, arrEnd, arrPoint)

    def add_curve(self, arr_points, int_degree):
        """

        Adds a control points curve object to the document.

        Parameters

        arrPoints : Required, Array, An array of 3-D points
        intDegree : Optional, Number, The degree of the curve

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddCurve', None, arrPoints, intDegree)

    def add_ellipse(self, arr_plane, dbl_x_radius, dbl_y_radius):
        """

        Adds an elliptical curve to the document.

        Parameters

        arrPlane : Required, Array, The plane on which the ellipse will lie
        dblXRadius : Required, Number, The radius in the X-axis direction
        dblYRadius : Required, Number, The radius in the Y-axis direction

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddEllipse', None, arrPlane, dblXRadius, dblYRadius)

    def add_ellipse3_pt(self, arr_center, arr_second, arr_third):
        """

        Adds a 3 point elliptical curve to the document.

        Parameters

        arrCenter : Required, Array, The center point of the ellipse
        arrSecond : Required, Array, The end point of the X-axis
        arrThird : Required, Array, The end point of the Y-axis

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddEllipse3Pt', None, arrCenter, arrSecond, arrThird)

    def add_fillet_curve(self, str_curve0, str_curve1, dbl_radius, arr_point0, arr_point1):
        """

        Adds a fillet curve between two curve objects.

        Parameters

        strCurve0 : Required, String, The identifier of the first curve object
        strCurve1 : Required, String, The identifier of the second curve object
        dblRadius : Optional, Number, The fillet radius
        arrPoint0 : Optional, Array, The base point on the first curve
        arrPoint1 : Optional, Array, The base point on the second curve

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddFilletCurve', None, strCurve0, strCurve1, dblRadius, arrPoint0, arrPoint1)

    def add_interp_crv_on_srf(self, str_object, arr_points):
        """

        Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

        Parameters

        strObject : Required, String, The surface object's identifier
        arrPoints : Required, Array, An array of 3-D points that lie on the specified surface

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCrvOnSrf', None, strObject, arrPoints)

    def add_interp_crv_on_srf_u_v(self, str_object, arr_points):
        """

        Adds an interpolated curve object. based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

        Parameters

        strObject : Required, String, The surface object's identifier
        arrPoints : Required, Array, An array of 2-D surface parameters

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCrvOnSrfUV', None, strObject, arrPoints)

    def add_interp_curve(self, arr_points, int_degree, int_knot_style, arr_start_tan, arr_end_tan):
        """

        Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.

        Parameters

        arrPoints : Required, Array, An array containing 3-D points to interpolate
        intDegree : Optional, Number, The degree of the curve
        intKnotStyle : Optional, Number, The knot style to use, and whether the curve should be periodic
        arrStartTan : Optional, Array, A 3-D vector that specifies a tangency condition at the beginning of the curve
        arrEndTan : Optional, Array, A 3-D vector that specifies a tangency condition at the end of the curve

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCurve', None, arrPoints, intDegree, intKnotStyle, arrStartTan, arrEndTan)

    def add_interp_curve_ex(self, arr_points, int_degree, int_knot_style, bln_sharp, arr_start_tangent, arr_end_tangent):
        """

        Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.

        Parameters

        arrPoints : Required, Array, An array containing 3-D points to interpolate
        intDegree : Optional, Number, The degree of the curve
        intKnotStyle : Optional, Number, The knot style to use
        blnSharp : Optional, Boolean, If True, when you create a closed curve, it will have a kink at the start/end point
        arrStartTangent : Optional, Array, A 3-D vector that specifies a tangency condition at the beginning of the curve
        arrEndTangent : Optional, Array, A 3-D vector that specifies a tangency condition at the end of the curve

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCurveEx', None, arrPoints, intDegree, intKnotStyle, blnSharp, arrStartTangent, arrEndTangent)

    def add_line(self, arr_start, arr_end):
        """

        Adds a line curve to the current model.

        Parameters

        arrStart : Required, Array, The starting point of the line
        arrEnd : Required, Array, The ending point of the line

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddLine', None, arrStart, arrEnd)

    def add_nurbs_curve(self, arr_points, arr_knots, int_degree, arr_weights):
        """

        Adds a NURBS curve object to the document.

        Parameters

        arrPoints : Required, Array, An array of 3-D control points
        arrKnots : Required, Array, The knot values for the curve
        intDegree : Required, Number, The degree of the curve
        arrWeights : Optional, Array, The weight values for the curve

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddNurbsCurve', None, arrPoints, arrKnots, intDegree, arrWeights)

    def add_polyline(self, arr_points):
        """

        Adds a polyline curve object to the current model.

        Parameters

        arrPoints : Required, Array, An array of 3-D points

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPolyline', None, arrPoints)

    def add_sub_crv(self, str_object, dbl_param0, dbl_param1):
        """

        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters

        strObject : Required, String, The identifier of a closed, planar curve object
        dblParam0 : Required, Number, The first parameter on the source curve
        dblParam1 : Required, Number, The second parameter on the source curve

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddSubCrv', None, strObject, dblParam0, dblParam1)

    def arc_angle(self, str_object, int_index):
        """

        Returns the angle of an arc curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The angle in degrees if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ArcAngle', None, strObject, intIndex)

    def arc_center_point(self, str_object, int_index):
        """

        Returns the center point of an arc curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ArcCenterPoint', None, strObject, intIndex)

    def arc_mid_point(self, str_object, int_index):
        """

        Returns the mid point of an arc curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ArcMidPoint', None, strObject, intIndex)

    def arc_radius(self, str_object, int_index):
        """

        Returns the radius of an arc curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The radius of the arc if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ArcRadius', None, strObject, intIndex)

    def circle_center_point(self, str_object, int_index):
        """

        Returns the center point of a circle curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : The 3-D center point of the circle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CircleCenterPoint', None, strObject, intIndex)

    def circle_circumference(self, str_object, int_index):
        """

        Returns the circumference of a circle curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The circumference of the circle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CircleCircumference', None, strObject, intIndex)

    def circle_radius(self, str_object, int_index):
        """

        Returns the radius of a circle curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The radius of the circle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CircleRadius', None, strObject, intIndex)

    def close_curve(self, str_object, dbl_tolerance):
        """

        Closes an open curve object by making adjustments to the end points so that they meet at a point.

        Parameters

        strObject : Required, String, The object's identifier
        dblTolerance : Optional, Number, The maximum allowable distance between start point and end point of the curve

        Returns

        String : The identifier of the closed curve object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CloseCurve', None, strObject, dblTolerance)

    def convert_curve_to_polyline(self, str_object, dbl_angle_tolerance, dbl_tolerance, bln_delete_input):
        """

        Converts a curve to a polyline curve.

        Parameters

        strObject : Required, String, The object's identifier
        dblAngleTolerance : Optional, Number, The maximum angle between curve tangents at line endpoints
        dblTolerance : Optional, Number, The distance tolerance at segment midpoints
        blnDeleteInput : Optional, Boolean, Delete the curve object specified by strObject

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ConvertCurveToPolyline', None, strObject, dblAngleTolerance, dblTolerance, blnDeleteInput)

    def curve_arc_length_point(self, str_object, dbl_length, bln_from_start):
        """

        Returns the point on the curve that is a specified arc length from the start of the curve.

        Parameters

        strObject : Required, String, The object's identifier
        dblLength : Required, Number, The arc length from the start of the curve to evaluate
        blnFromStart : Optional, Boolean, If not specified or True, then the arc length point is calculated from the start of the curve

        Returns

        Array : The 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveArcLengthPoint', None, strObject, dblLength, blnFromStart)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_arrows(self, str_object, int_style):
        """

        Enables or disabled a curve object's annotation arrows.

        Parameters

        strObject : Required, String, The object's identifier
        intStyle : Optional, Number, The style of annotation arrows to be displayed

        Returns

        Number : If intStyle is not specified, the current annotation arrow style if successful.
        Number : If intStyle is specified, the previous annotation arrow style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveArrows', None, strObject, intStyle)

    def curve_boolean_difference(self, str_curve_a, str_curve_b):
        """

        Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters

        strCurveA : Required, String, The identifier of the first curve object
        strCurveB : Required, String, The identifier of the second curve object

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBooleanDifference', None, strCurveA, strCurveB)

    def curve_boolean_intersection(self, str_curve_a, str_curve_b):
        """

        Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters

        strCurveA : Required, String, The identifier of the first curve object
        strCurveB : Required, String, The identifier of the second curve object

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBooleanIntersection', None, strCurveA, strCurveB)

    def curve_boolean_union(self, arr_curves):
        """

        Calculates the union of two or more closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters

        arrCurves : Required, Array, The identifiers of two or more curve objects

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBooleanUnion', None, arrCurves)

    def curve_brep_intersect(self, str_curve, str_brep, dbl_tolerance):
        """

        Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function, this function works on trimmed surfaces.

        Parameters

        strCurve : Required, String, The curve object's identifier
        strBrep : Required, String, The brep object's identifier
        dblTolerance : Optional, Number, The distance tolerance at segment midpoints

        Returns

        Array : An array of strings identifying the newly created intersection curve and point objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBrepIntersect', None, strCurve, strBrep, dblTolerance)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_closest_point(self, str_object, arr_point, int_index):
        """

        Returns the parameter of the point on a curve that is closest to a test point.

        Parameters

        strObject : Required, String, The object's identifier
        arrPoint : Required, Array, The test, or sampling, point
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The parameter of the closest point on the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveClosestPoint', None, strObject, arrPoint, intIndex)

    def curve_contour_points(self, str_object, arr_start_point, arr_end_point, dbl_interval):
        """

        Returns the 3-D point locations calculated by contouring a curve object.

        Parameters

        strObject : Required, String, The identifier of a curve object
        arrStartPoint : Required, Array, The 3-D starting point of a center line
        arrEndPoint : Required, Array, The 3-D ending point of a center line
        dblInterval : Optional, Number, The distance between contour curves

        Returns

        Array : An array of 3-D points, one for each contour, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveContourPoints', None, strObject, arrStartPoint, arrEndPoint, dblInterval)

    def curve_curvature(self, str_object, dbl_parameter):
        """

        Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.

        Parameters

        strObject : Required, String, The object's identifier
        dblParameter : Required, Number, The parameter to evaluate

        Returns

        Array : An array of curvature information if successful.  The array will contain the following information:
        Number : Radius of curvature
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveCurvature', None, strObject, dblParameter)

    def curve_curve_intersection(self, str_object1, str_object2, dbl_tolerance):
        """

        Calculates the intersection of two curve objects.

        Parameters

        strObject1 : Required, String, The identifier of the first curve object
        strObject2 : Optional, String, The identifier of the second curve object
        dblTolerance : Optional, Number, The absolute tolerance in drawing units

        Returns

        Array : A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:
        Number : The intersection event type, either Point (1) or Overlap (2).
        Number : If the event type is Point (1), then the first curve parameter.
        Number : If the event type is Point (1), then the first curve parameter.
        Number : If the event type is Point (1), then the second curve parameter.
        Number : If the event type is Point (1), then the second curve parameter.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveCurveIntersection', None, strObject1, strObject2, dblTolerance)

    def curve_degree(self, str_object, int_index):
        """

        Returns the degree of a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The degree of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDegree', None, strObject, intIndex)

    def curve_deviation(self, str_curve_a, str_curve_b):
        """

        Returns the minimum and maximum deviation between two curve objects. For more information on curve deviation, see the Rhino help file for the CrvDeviation command.

        Parameters

        strCurveA : Required, String, The identifier of the first curve object
        strCurveB : Required, String, The identifier of the second curve object

        Returns

        Array : An array of numbers identifying the minimum and maximum deviation between the two curves if successful.
        Number : Curve A parameter at maximum overlap distance point
        Number : Curve A parameter at maximum overlap distance point
        Number : Maximum overlap distance
        Number : Curve A parameter at minimum distance point
        Number : Curve B parameter at minimum distance point
        Number : Minimum distance between curves
        Null : On error or if no intervals of overlap were found.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDeviation', None, strCurveA, strCurveB)

    def curve_dim(self, str_object, int_index):
        """

        Returns the dimension of a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The dimension of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDim', None, strObject, intIndex)

    def curve_directions_match(self, str_curve1, str_curve2):
        """

        Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.

        Parameters

        strCurve1 : Required, String, The identifier of the first curve to compare
        strCurve2 : Required, String, The identifier of the second curve to compare

        Returns

        Boolean : True if the curve directions match, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDirectionsMatch', None, strCurve1, strCurve2)

    def curve_discontinuity(self, str_object, int_style):
        """

        Search for a derivatitive, tangent, or curvature discontinuity in a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intStyle : Required, Number, The type of continuity to test for

        Returns

        Array : An array of 3-D points where the curve is discontinuous if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDiscontinuity', None, strObject, intStyle)

    def curve_domain(self, str_object, int_index):
        """

        Returns the domain of a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : The domain of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDomain', None, strObject, intIndex)

    def curve_edit_points(self, str_object, bln_return_parameters, int_index):
        """

        Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.

        Parameters

        strObject : Required, String, The object's identifier
        blnReturnParameters : Optional, Boolean, Return the edit points as an array of parameter values
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.
        Array : If blnReturnParameters is True, then an array of parameter values if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveEditPoints', None, strObject, blnReturnParameters, intIndex)

    def curve_end_point(self, str_object, int_index):
        """

        Returns the end point of a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : The 3-D end point of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveEndPoint', None, strObject, intIndex)

    def curve_evaluate(self, str_object, dbl_parameter, int_derivative):
        """

        A general purpose curve evaluator.

        Parameters

        strObject : Required, String, The object's identifier
        dblParameter : Required, Number, The evaluation parameter
        intDerivative : Required, Number, The number of derivatives to evaluate

        Returns

        Array : An array of length (intDerivative+1) if successful.  The array elements are as follows:
        Array : The 3-D point
        Array : The first derivative
        Array : The second derivative
        Array : etc...
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveEvaluate', None, strObject, dblParameter, intDerivative)

    def curve_fillet_points(self, str_curve0, str_curve1, dbl_radius, arr_base_point0, arr_base_point1):
        """

        Of all possible fillet points, this function returns the one which is the closest to the base point arrBasePoint0, arrBasePoint1.  Distance from the base point is measured by the sum of arc lengths along the two curves.

        Parameters

        strCurve0 : Required, String, The identifier of the first curve object
        strCurve1 : Required, String, The identifier of the second curve object
        dblRadius : Optional, Number, The fillet radius
        arrBasePoint0 : Optional, Array, The base point on the first curve
        arrBasePoint1 : Optional, Array, The base point on the second curve

        Returns

        Array : If blnPoints is True, then an array of point and vector values if successful.  The array elements are as follows:
        String : If blnPoints is False, then the identifier of the fillet curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveFilletPoints', None, strCurve0, strCurve1, dblRadius, arrBasePoint0, arrBasePoint1)

    def curve_frame(self, str_object, dbl_parameter):
        """

        Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.

        Parameters

        strObject : Required, String, The object's identifier
        dblParameter : Required, Number, The parameter to evaluate

        Returns

        Array : The plane at the specified parameter if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveFrame', None, strObject, dblParameter)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_length(self, str_object, int_index, arr_sub_domain):
        """

        Returns the length of a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query
        arrSubDomain : Optional, Array, An array of two numbers identifying the sub-domain of the curve on which the calculation will be performed

        Returns

        Number : The length of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveLength', None, strObject, intIndex, arrSubDomain)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_normal(self, str_object):
        """

        Returns the normal direction of the plane in which a planar curve object lies.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : The 3-D normal vector if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveNormal', None, strObject)

    def curve_perp_frame(self, str_object, dbl_parameter):
        """

        Returns the perpendicular plane at a parameter of a curve.  The result is relatively parallel (zero-twisting) plane.

        Parameters

        strObject : Required, String, The object's identifier
        dblParameter : Required, Number, The parameter to evaluate

        Returns

        Array : The plane at the specified parameter if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePerpFrame', None, strObject, dblParameter)

    def curve_plane(self, str_curve):
        """

        Returns the plane in which a planar curve lies. Note, this function works only on planar curves.

        Parameters

        strCurve : Required, String, The identifier of a planar curve object

        Returns

        Array : The plane in which the curve lies if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePlane', None, strCurve)

    def curve_point_count(self, str_object, int_index):
        """

        Returns the control points count of a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The number of control points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePointCount', None, strObject, intIndex)

    def curve_points(self, str_object, int_index):
        """

        Returns the control points, or control vertices, of a curve object.  If the curve is a rational NURBS curve, the euclidean control vertices are returned.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : The control points of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePoints', None, strObject, intIndex)

    def curve_radius(self, str_object, arr_point, int_index):
        """

        Returns the radius of curvature at a point on a curve.

        Parameters

        strObject : Required, String, The object's identifier
        arrPoint : Required, Array, The test, or sampling, point
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The radius of curvature at the point on the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveRadius', None, strObject, arrPoint, intIndex)

    def curve_seam(self, str_object, dbl_parameter):
        """

        Adjusts the seam, or start/end, point of a closed curve.

        Parameters

        strObject : Required, String, The object's identifier
        dblParameter : Required, Number, The parameter of the new start/end point

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveSeam', None, strObject, dblParameter)

    def curve_start_point(self, str_object, int_index):
        """

        Returns the start point of a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : The 3-D starting point of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveStartPoint', None, strObject, intIndex)

    def curve_surface_intersection(self, str_curve, str_surface, dbl_tolerance, dbl_angle_tolerance):
        """

        Calculates the intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.

        Parameters

        strCurve : Required, String, The identifier of a curve object
        strSurface : Required, String, The identifier of a surface object
        dblTolerance : Optional, Number, The absolute tolerance in drawing units
        dblAngleTolerance : Optional, Number, The angle tolerance in degrees

        Returns

        Array : A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:
        Number : The intersection event type, either Point (1) or Overlap (2).
        Number : If the event type is Point (1), then the curve parameter.
        Number : If the event type is Point (1), then the curve parameter.
        Number : If the event type is Point (1), then the U surface parameter.
        Number : If the event type is Point (1), then the V surface parameter.
        Number : If the event type is Point (1), then the U surface parameter.
        Number : If the event type is Point (1), then the V surface parameter.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveSurfaceIntersection', None, strCurve, strSurface, dblTolerance, dblAngleTolerance)

    def curve_tangent(self, str_object, dbl_parameter, int_index):
        """

        Returns a 3-D vector that is the tangent to a curve at a parameter.

        Parameters

        strObject : Required, String, The object's identifier
        dblParameter : Required, Number, The parameter to evaluate
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : A  3-D vector if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveTangent', None, strObject, dblParameter, intIndex)

    def curve_weights(self, str_object, int_index):
        """

        Returns an array of weight values that are assigned to the control points of a curve.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : The weight values of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurveWeights', None, strObject, intIndex)

    def divide_curve(self, str_object, lng_segments, bln_create, bln_points):
        """

        Divides a curve object into a specified number of segments.

        Parameters

        strObject : Required, String, The object's identifier
        lngSegments : Required, Number, The number of segments
        blnCreate : Optional, Boolean, Create the division points
        blnPoints : Optional, Boolean, Return an array of 3-D points

        Returns

        Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
        Array : If blnPoints is False, then an array containing division curve parameters if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DivideCurve', None, strObject, lngSegments, blnCreate, blnPoints)

    def divide_curve_equidistant(self, str_object, dbl_distance, bln_create, bln_points):
        """

        Unlike the DivideCurve and DivideCurveLength, which divides a curve based on arc length, or the distance along the curve between two points, this function divides a curve based on the linear distance between points.

        Parameters

        strObject : Required, String, The object's identifier
        dblDistance : Required, Number, The linear distance between division points
        blnCreate : Optional, Boolean, Create the division points
        blnPoints : Optional, Boolean, Return an array of 3-D points

        Returns

        Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
        Array : If blnPoints is False, then an array containing division curve parameters if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DivideCurveEquidistant', None, strObject, dblDistance, blnCreate, blnPoints)

    def divide_curve_length(self, str_object, dbl_length, bln_create, bln_points):
        """

        Divides a curve object into segments of a specified length.

        Parameters

        strObject : Required, String, The object's identifier
        dblLength : Required, Number, The length of each segment
        blnCreate : Optional, Boolean, Create the division points
        blnPoints : Optional, Boolean, Return an array of 3-D points

        Returns

        Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
        Array : If blnPoints is False, then an array containing division curve parameters if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DivideCurveLength', None, strObject, dblLength, blnCreate, blnPoints)

    def ellipse_center_point(self, str_object):
        """

        Returns the center point of an elliptical-shaped curve object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : The 3-D center point of the ellipse if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'EllipseCenterPoint', None, strObject)

    def ellipse_quad_points(self, str_object):
        """

        Returns the quadrant points of an elliptical-shaped curve object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of 3-D points identifying the quadrants of the ellipse if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'EllipseQuadPoints', None, strObject)

    def evaluate_curve(self, str_object, dbl_parameter, int_index):
        """

        Evaluates a curve at a parameter.

        Parameters

        strObject : Required, String, The object's identifier
        dblParameter : Required, Number, The parameter to evaluate
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : A 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'EvaluateCurve', None, strObject, dblParameter, intIndex)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def extend_curve(self, str_object, int_type, int_side, arr_objects):
        """

        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters

        strObject : Required, String, The object's identifier
        intType : Required, Number, Type of extension
        intSide : Required, Number, The size to  extent
        arrObjects : Required, Array, The identifiers of curve, surface, and polysurface objects that will be used as boundary objects

        Returns

        String : The identifier of the extended object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtendCurve', None, strObject, intType, intSide, arrObjects)

    def extend_curve_length(self, str_object, int_type, int_side, dbl_length):
        """

        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters

        strObject : Required, String, The object's identifier
        intType : Required, Number, Type of extension
        intSide : Required, Number, The size to  extent
        dblLength : Required, Number, The distance to extend the curve

        Returns

        String : The identifier of the extended object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtendCurveLength', None, strObject, intType, intSide, dblLength)

    def extend_curve_point(self, str_object, int_side, arr_point):
        """

        Extends a non-closed curve object by smooth extension to a point.

        Parameters

        strObject : Required, String, The object's identifier
        intSide : Required, Number, The size to  extent
        arrPoint : Required, Array, The 3-D point

        Returns

        String : The identifier of the extended object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtendCurvePoint', None, strObject, intSide, arrPoint)

    def fair_curve(self, str_object, dbl_tolerance):
        """

        Fairs a curve object. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvature variations while limiting the geometry changes to be no more than the specified tolerance. Sometimes several applications of this method are necessary to remove nasty curvature problems.

        Parameters

        strObject : Required, String, The object's identifier
        dblTolerance : Optional, Number, The fairing tolerance

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'FairCurve', None, strObject, dblTolerance)

    def fit_curve(self, str_object, int_degree, dbl_tolerance, dbl_angle_tolerance):
        """

        Reduces the number of curve control points while maintaining the curve's same general shape.  Use this function for replacing curves with too many control points.  For more information, see the Rhino help file for the FitCrv command.

        Parameters

        strObject : Required, String, The object's identifier
        intDegree : Optional, Number, The curve degree, which must be greater than 1
        dblTolerance : Optional, Number, The fitting tolerance
        dblAngleTolerance : Optional, Number, The kink smoothing tolerance in degrees

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'FitCurve', None, strObject, intDegree, dblTolerance, dblAngleTolerance)

    def insert_curve_knot(self, str_object, dbl_parameter, bln_symmetrical):
        """

        Inserts a knot into a curve object.

        Parameters

        strObject : Required, String, The identifier of the curve object
        dblParameter : Required, Number, The parameter on the curve
        blnSymmetrical : Optional, Boolean, If blnSymmetrical = True, then knots are added on both sides of the center of the curve

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'InsertCurveKnot', None, strObject, dblParameter, blnSymmetrical)

    def is_arc(self, str_object, int_index):
        """

        Verifies an object is an arc curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsArc', None, strObject, intIndex)

    def is_circle(self, str_object, int_index):
        """

        Verifies an object is a circle curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCircle', None, strObject, intIndex)

    def is_curve(self, str_object, int_index):
        """

        Verifies an object is a curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurve', None, strObject, intIndex)

    def is_curve_closable(self, str_object, dbl_tolerance):
        """

        Decide if it makes sense to close off the curve by moving  the endpoint to the start based on start-end gap size and length of curve as approximated by chord defined by 6 points.

        Parameters

        strObject : Required, String, The object's identifier
        dblTolerance : Optional, Number, The maximum allowable distance between start point and end point of the curve

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveClosable', None, strObject, dblTolerance)

    def is_curve_closed(self, str_object, int_index):
        """

        Verifies an object is a closed curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveClosed', None, strObject, intIndex)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def is_curve_linear(self, str_object, int_index):
        """

        Verifies an object is a linear curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveLinear', None, strObject, intIndex)

    def is_curve_periodic(self, str_object, int_index):
        """

        Verifies an object is a periodic curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurvePeriodic', None, strObject, intIndex)

    def is_curve_planar(self, str_object, int_index):
        """

        Verifies an object is a planar curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurvePlanar', None, strObject, intIndex)

    def is_curve_rational(self, str_object, int_index):
        """

        Verifies an object is a rational NURBS curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveRational', None, strObject, intIndex)

    def is_ellipse(self, str_object):
        """

        Verifies an object is an elliptical-shaped curve object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsEllipse', None, strObject)

    def is_line(self, str_object, int_index):
        """

        Verifies an object is a line curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsLine', None, strObject, intIndex)

    def is_point_on_curve(self, str_object, arr_point, arr_point):
        """

        Verifies that a point is on a curve.

        Parameters

        strObject : Required, String, The object's identifier
        arrPoint : Required, Array, The test, or sampling, point
        arrPoint : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPointOnCurve', None, strObject, arrPoint, arrPoint)

    def is_poly_curve(self, str_object, int_index):
        """

        Verifies an object is a polycurve object.  A polycurve is a curve that is represented by a sequence of contiguous curve segments.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPolyCurve', None, strObject, intIndex)

    def is_polyline(self, str_object, int_index):
        """

        Verifies an object is a polyline curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPolyline', None, strObject, intIndex)

    def join_curves(self, str_object, bln_delete):
        """

        Joins two or more curve object together to form one or more curves or polycurves.

        Parameters

        strObject : Required, Array, An array of strings identifying the curve objects to join
        blnDelete : Optional, Boolean, Delete input objects after joining

        Returns

        Array : An array of strings identifying the newly created curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'JoinCurves', None, strObject, blnDelete)

    def line_fit_from_points(self, str_object):
        """

        Returns the starting and ending points of a line that was fit through an array of 3-D points.

        Parameters

        strObject : Required, Array, An array of 3-D points

        Returns

        Array : An array containing the starting and ending points of the fit line if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LineFitFromPoints', None, strObject)

    def make_curve_non_periodic(self, str_object, bln_delete):
        """

        Makes a periodic curve non-periodic.  Non-periodic curves can develop kinks when deformed.

        Parameters

        strObject : Required, String, The object's identifier
        blnDelete : Optional, Boolean, Delete input curve

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MakeCurveNonPeriodic', None, strObject, blnDelete)

    def make_curve_periodic(self, str_object, bln_delete):
        """

        Makes an existing curve a periodic NURBS curve.  A periodic NURBS curve is a closed curve with a simple knot at the seam.  If a joined curve is made periodic, it becomes a single-span curve and can no longer be exploded.

        Parameters

        strObject : Required, String, The object's identifier
        blnDelete : Optional, Boolean, Delete input curve

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MakeCurvePeriodic', None, strObject, blnDelete)

    def mesh_polyline(self, str_polyline):
        """

        Creates a polygon mesh object based on a closed polyline curve object. The newly created polygon mesh object is added to the document.

        Parameters

        strPolyline : Required, String, The identifier of the polyline curve object

        Returns

        String : The identifier of the new polygon mesh object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MeshPolyline', None, strPolyline)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def poly_curve_count(self, str_object, int_index):
        """

        Returns the number of curve segments that make up a polycurve.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Number : The number of curve segments in a polycurve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PolyCurveCount', None, strObject, intIndex)

    def polyline_vertices(self, str_object, int_index):
        """

        Returns the vertices of a polyline curve object.

        Parameters

        strObject : Required, String, The object's identifier
        intIndex : Optional, Number, If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

        Returns

        Array : An  array of 3-D vertex points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PolylineVertices', None, strObject, intIndex)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def rebuild_curve(self, str_object, int_degree, int_point_count):
        """

        Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.

        Parameters

        strObject : Required, String, The object's identifier
        intDegree : Optional, Number, The new degree, which must be greater than 1
        intPointCount : Optional, Number, The new point count, which must be bigger than the intDegree

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RebuildCurve', None, strObject, intDegree, intPointCount)

    def remove_curve_knot(self, str_object, dbl_parameter):
        """

        Deletes a knot from a curve object.

        Parameters

        strObject : Required, String, The identifier of the curve object
        dblParameter : Required, Number, The parameter on the curve

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveCurveKnot', None, strObject, dblParameter)

    def reverse_curve(self, str_object):
        """

        Reverses the direction of a curve object. This feature can also be found in Rhino's Dir command.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ReverseCurve', None, strObject)

    def simplify_curve(self, str_object, int_flags):
        """

        6.  Segments that meet with G1-continuity have there ends tuned up so that they meet with G1-continuity to within machine precision.

        Parameters

        strObject : Required, String, The curve object's identifier
        intFlags : Optional, Number, The simplification methods to use

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SimplifyCurve', None, strObject, intFlags)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def trim_curve(self, str_object, arr_interval, bln_delete):
        """

        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters

        strObject : Required, String, The object's identifier
        arrInterval : Required, Array, An array of two number identifying the interval to keep
        blnDelete : Optional, Boolean, Delete the input curve

        Returns

        String : The identifier of the newly created curve object, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TrimCurve', None, strObject, arrInterval, blnDelete)

