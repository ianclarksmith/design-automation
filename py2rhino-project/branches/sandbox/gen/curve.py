# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Curve(DispatchBaseClass):



    def add_arc(self, plane, radius, angle):
        """

        Adds an arc curve to the document.

        Parameters

        Plane : Required, Array, arr
        Radius : Required, Number, dbl
        Angle : Required, Number, dbl

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(651, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddArc', None, plane, radius, angle)

    def add_arc3_pt(self, start, end, point):
        """

        Adds a 3-point arc curve to the document.

        Parameters

        Start : Required, Array, arr
        End : Required, Array, arr
        Point : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(82, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddArc3Pt', None, start, end, point)

    def add_circle(self, plane, radius):
        """

        Adds a circle curve to the document.

        Parameters

        Plane : Required, Array, arr
        Radius : Required, Number, dbl

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(83, 1, (12, 0), ((12, 0), (12, 0)), u'AddCircle', None, plane, radius)

    def add_circle3_pt(self, start, end, point):
        """

        Adds a 3-point circle curve to the document.

        Parameters

        Start : Required, Array, arr
        End : Required, Array, arr
        Point : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(84, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddCircle3Pt', None, start, end, point)

    def add_curve(self, points, degree):
        """

        Adds a control points curve object to the document.

        Parameters

        Points : Required, Array, arr
        Degree : Optional, Number, int

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(77, 1, (12, 0), ((12, 0), (12, 0)), u'AddCurve', None, points, degree)

    def add_ellipse(self, plane, x_radius, y_radius):
        """

        Adds an elliptical curve to the document.

        Parameters

        Plane : Required, Array, arr
        XRadius : Required, Number, dbl
        YRadius : Required, Number, dbl

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(679, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddEllipse', None, plane, x_radius, y_radius)

    def add_ellipse3_pt(self, center, second, third):
        """

        Adds a 3 point elliptical curve to the document.

        Parameters

        Center : Required, Array, arr
        Second : Required, Array, arr
        Third : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(680, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddEllipse3Pt', None, center, second, third)

    def add_fillet_curve(self, curve0, curve1, radius, point0, point1):
        """

        Adds a fillet curve between two curve objects.

        Parameters

        Curve0 : Required, String, str
        Curve1 : Required, String, str
        Radius : Optional, Number, dbl
        Point0 : Optional, Array, arr
        Point1 : Optional, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(574, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'AddFilletCurve', None, curve0, curve1, radius, point0, point1)

    def add_interp_crv_on_srf(self, object, points):
        """

        Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

        Parameters

        Object : Required, String, str
        Points : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(513, 1, (12, 0), ((12, 0), (12, 0)), u'AddInterpCrvOnSrf', None, object, points)

    def add_interp_crv_on_srf_u_v(self, object, points):
        """

        Adds an interpolated curve object. based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

        Parameters

        Object : Required, String, str
        Points : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(641, 1, (12, 0), ((12, 0), (12, 0)), u'AddInterpCrvOnSrfUV', None, object, points)

    def add_interp_curve(self, points, degree, knot_style, start_tan, end_tan):
        """

        Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.

        Parameters

        Points : Required, Array, arr
        Degree : Optional, Number, int
        KnotStyle : Optional, Number, int
        StartTan : Optional, Array, arr
        EndTan : Optional, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(268, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'AddInterpCurve', None, points, degree, knot_style, start_tan, end_tan)

    def add_interp_curve_ex(self, points, degree, knot_style, sharp, start_tangent, end_tangent):
        """

        Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.

        Parameters

        Points : Required, Array, arr
        Degree : Optional, Number, int
        KnotStyle : Optional, Number, int
        Sharp : Optional, Boolean, bln
        StartTangent : Optional, Array, arr
        EndTangent : Optional, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(520, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'AddInterpCurveEx', None, points, degree, knot_style, sharp, start_tangent, end_tangent)

    def add_line(self, start, end):
        """

        Adds a line curve to the current model.

        Parameters

        Start : Required, Array, arr
        End : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(70, 1, (12, 0), ((12, 0), (12, 0)), u'AddLine', None, start, end)

    def add_nurbs_curve(self, points, knots, degree, weights):
        """

        Adds a NURBS curve object to the document.

        Parameters

        Points : Required, Array, arr
        Knots : Required, Array, arr
        Degree : Required, Number, int
        Weights : Optional, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(309, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'AddNurbsCurve', None, points, knots, degree, weights)

    def add_polyline(self, points):
        """

        Adds a polyline curve object to the current model.

        Parameters

        Points : Required, Array, arr

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(85, 1, (12, 0), ((12, 0)), u'AddPolyline', None, points)

    def add_sub_crv(self, object, param0, param1):
        """

        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

        Parameters

        Object : Required, String, str
        Param0 : Required, Number, dbl
        Param1 : Required, Number, dbl

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(681, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'AddSubCrv', None, object, param0, param1)

    def arc_angle(self, object, index):
        """

        Returns the angle of an arc curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The angle in degrees if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(86, 1, (12, 0), ((12, 0), (12, 0)), u'ArcAngle', None, object, index)

    def arc_center_point(self, object, index):
        """

        Returns the center point of an arc curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(87, 1, (12, 0), ((12, 0), (12, 0)), u'ArcCenterPoint', None, object, index)

    def arc_mid_point(self, object, index):
        """

        Returns the mid point of an arc curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(88, 1, (12, 0), ((12, 0), (12, 0)), u'ArcMidPoint', None, object, index)

    def arc_radius(self, object, index):
        """

        Returns the radius of an arc curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The radius of the arc if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(89, 1, (12, 0), ((12, 0), (12, 0)), u'ArcRadius', None, object, index)

    def circle_center_point(self, object, index):
        """

        Returns the center point of a circle curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Array : The 3-D center point of the circle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(90, 1, (12, 0), ((12, 0), (12, 0)), u'CircleCenterPoint', None, object, index)

    def circle_circumference(self, object, index):
        """

        Returns the circumference of a circle curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The circumference of the circle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(91, 1, (12, 0), ((12, 0), (12, 0)), u'CircleCircumference', None, object, index)

    def circle_radius(self, object, index):
        """

        Returns the radius of a circle curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The radius of the circle if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(92, 1, (12, 0), ((12, 0), (12, 0)), u'CircleRadius', None, object, index)

    def close_curve(self, object, tolerance):
        """

        Closes an open curve object by making adjustments to the end points so that they meet at a point.

        Parameters

        Object : Required, String, str
        Tolerance : Optional, Number, dbl

        Returns

        String : The identifier of the closed curve object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(440, 1, (12, 0), ((12, 0), (12, 0)), u'CloseCurve', None, object, tolerance)

    def convert_curve_to_polyline(self, object, angle_tolerance, tolerance, delete_input):
        """

        Converts a curve to a polyline curve.

        Parameters

        Object : Required, String, str
        AngleTolerance : Optional, Number, dbl
        Tolerance : Optional, Number, dbl
        DeleteInput : Optional, Boolean, bln

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(377, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'ConvertCurveToPolyline', None, object, angle_tolerance, tolerance, delete_input)

    def curve_arc_length_point(self, object, length, from_start):
        """

        Returns the point on the curve that is a specified arc length from the start of the curve.

        Parameters

        Object : Required, String, str
        Length : Required, Number, dbl
        FromStart : Optional, Boolean, bln

        Returns

        Array : The 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(658, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveArcLengthPoint', None, object, length, from_start)

    def curve_area(self, object, objects):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_area_centroid(self, object, objects):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_arrows(self, object, style):
        """

        Enables or disabled a curve object's annotation arrows.

        Parameters

        Object : Required, String, str
        Style : Optional, Number, int

        Returns

        Number : If intStyle is not specified, the current annotation arrow style if successful.
        Number : If intStyle is specified, the previous annotation arrow style if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(578, 1, (12, 0), ((12, 0), (12, 0)), u'CurveArrows', None, object, style)

    def curve_boolean_difference(self, curve_a, curve_b):
        """

        Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters

        CurveA : Required, String, str
        CurveB : Required, String, str

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(811, 1, (12, 0), ((12, 0), (12, 0)), u'CurveBooleanDifference', None, curve_a, curve_b)

    def curve_boolean_intersection(self, curve_a, curve_b):
        """

        Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters

        CurveA : Required, String, str
        CurveB : Required, String, str

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(810, 1, (12, 0), ((12, 0), (12, 0)), u'CurveBooleanIntersection', None, curve_a, curve_b)

    def curve_boolean_union(self, curves):
        """

        Calculates the union of two or more closed, planar curves and adds the results to the document. Note, curves must be coplanar.

        Parameters

        Curves : Required, Array, arr

        Returns

        Array : The identifiers of the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(809, 1, (12, 0), ((12, 0)), u'CurveBooleanUnion', None, curves)

    def curve_brep_intersect(self, curve, brep, tolerance):
        """

        Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function, this function works on trimmed surfaces.

        Parameters

        Curve : Required, String, str
        Brep : Required, String, str
        Tolerance : Optional, Number, dbl

        Returns

        Array : An array of strings identifying the newly created intersection curve and point objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(545, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveBrepIntersect', None, curve, brep, tolerance)

    def curve_closest_object(self, curve, object, objects):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_closest_point(self, object, point, index):
        """

        Returns the parameter of the point on a curve that is closest to a test point.

        Parameters

        Object : Required, String, str
        Point : Required, Array, arr
        Index : Optional, Number, int

        Returns

        Number : The parameter of the closest point on the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(93, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveClosestPoint', None, object, point, index)

    def curve_contour_points(self, object, start_point, end_point, interval):
        """

        Returns the 3-D point locations calculated by contouring a curve object.

        Parameters

        Object : Required, String, str
        StartPoint : Required, Array, arr
        EndPoint : Required, Array, arr
        Interval : Optional, Number, dbl

        Returns

        Array : An array of 3-D points, one for each contour, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(748, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'CurveContourPoints', None, object, start_point, end_point, interval)

    def curve_curvature(self, object, parameter):
        """

        Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl

        Returns

        Array : An array of curvature information if successful.  The array will contain the following information:
        Number : Radius of curvature
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(379, 1, (12, 0), ((12, 0), (12, 0)), u'CurveCurvature', None, object, parameter)

    def curve_curve_intersection(self, object1, object2, tolerance):
        """

        Calculates the intersection of two curve objects.

        Parameters

        Object1 : Required, String, str
        Object2 : Optional, String, str
        Tolerance : Optional, Number, dbl

        Returns

        Array : A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:
        Number : The intersection event type, either Point (1) or Overlap (2).
        Number : If the event type is Point (1), then the first curve parameter.
        Number : If the event type is Point (1), then the first curve parameter.
        Number : If the event type is Point (1), then the second curve parameter.
        Number : If the event type is Point (1), then the second curve parameter.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(423, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveCurveIntersection', None, object1, object2, tolerance)

    def curve_degree(self, object, index):
        """

        Returns the degree of a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The degree of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(94, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDegree', None, object, index)

    def curve_deviation(self, curve_a, curve_b):
        """

        Returns the minimum and maximum deviation between two curve objects. For more information on curve deviation, see the Rhino help file for the CrvDeviation command.

        Parameters

        CurveA : Required, String, str
        CurveB : Required, String, str

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

        return self._ApplyTypes_(687, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDeviation', None, curve_a, curve_b)

    def curve_dim(self, object, index):
        """

        Returns the dimension of a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The dimension of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(381, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDim', None, object, index)

    def curve_directions_match(self, curve1, curve2):
        """

        Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.

        Parameters

        Curve1 : Required, String, str
        Curve2 : Required, String, str

        Returns

        Boolean : True if the curve directions match, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(543, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDirectionsMatch', None, curve1, curve2)

    def curve_discontinuity(self, object, style):
        """

        Search for a derivatitive, tangent, or curvature discontinuity in a curve object.

        Parameters

        Object : Required, String, str
        Style : Required, Number, int

        Returns

        Array : An array of 3-D points where the curve is discontinuous if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(579, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDiscontinuity', None, object, style)

    def curve_domain(self, object, index):
        """

        Returns the domain of a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Array : The domain of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(95, 1, (12, 0), ((12, 0), (12, 0)), u'CurveDomain', None, object, index)

    def curve_edit_points(self, object, return_parameters, index):
        """

        Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.

        Parameters

        Object : Required, String, str
        ReturnParameters : Optional, Boolean, bln
        Index : Optional, Number, int

        Returns

        Array : If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.
        Array : If blnReturnParameters is True, then an array of parameter values if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(442, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveEditPoints', None, object, return_parameters, index)

    def curve_end_point(self, object, index):
        """

        Returns the end point of a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Array : The 3-D end point of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(96, 1, (12, 0), ((12, 0), (12, 0)), u'CurveEndPoint', None, object, index)

    def curve_evaluate(self, object, parameter, derivative):
        """

        A general purpose curve evaluator.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl
        Derivative : Required, Number, int

        Returns

        Array : An array of length (intDerivative+1) if successful.  The array elements are as follows:
        Array : The 3-D point
        Array : The first derivative
        Array : The second derivative
        Array : etc...
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(489, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveEvaluate', None, object, parameter, derivative)

    def curve_fillet_points(self, curve0, curve1, radius, base_point0, base_point1):
        """

        Of all possible fillet points, this function returns the one which is the closest to the base point arrBasePoint0, arrBasePoint1.  Distance from the base point is measured by the sum of arc lengths along the two curves.

        Parameters

        Curve0 : Required, String, str
        Curve1 : Required, String, str
        Radius : Optional, Number, dbl
        BasePoint0 : Optional, Array, arr
        BasePoint1 : Optional, Array, arr

        Returns

        Array : If blnPoints is True, then an array of point and vector values if successful.  The array elements are as follows:
        String : If blnPoints is False, then the identifier of the fillet curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(572, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'CurveFilletPoints', None, curve0, curve1, radius, base_point0, base_point1)

    def curve_frame(self, object, parameter):
        """

        Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl

        Returns

        Array : The plane at the specified parameter if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(675, 1, (12, 0), ((12, 0), (12, 0)), u'CurveFrame', None, object, parameter)

    def curve_knot_count(self, object, index):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_knots(self, object, index):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_length(self, object, index, sub_domain):
        """

        Returns the length of a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int
        SubDomain : Optional, Array, arr

        Returns

        Number : The length of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(97, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveLength', None, object, index, sub_domain)

    def curve_mid_point(self, object):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def curve_normal(self, object):
        """

        Returns the normal direction of the plane in which a planar curve object lies.

        Parameters

        Object : Required, String, str

        Returns

        Array : The 3-D normal vector if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(521, 1, (12, 0), ((12, 0)), u'CurveNormal', None, object)

    def curve_perp_frame(self, object, parameter):
        """

        Returns the perpendicular plane at a parameter of a curve.  The result is relatively parallel (zero-twisting) plane.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl

        Returns

        Array : The plane at the specified parameter if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(676, 1, (12, 0), ((12, 0), (12, 0)), u'CurvePerpFrame', None, object, parameter)

    def curve_plane(self, curve):
        """

        Returns the plane in which a planar curve lies. Note, this function works only on planar curves.

        Parameters

        Curve : Required, String, str

        Returns

        Array : The plane in which the curve lies if successful.
        Null : On error.

        """

        return self._ApplyTypes_(609, 1, (12, 0), ((12, 0)), u'CurvePlane', None, curve)

    def curve_point_count(self, object, index):
        """

        Returns the control points count of a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The number of control points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(98, 1, (12, 0), ((12, 0), (12, 0)), u'CurvePointCount', None, object, index)

    def curve_points(self, object, index):
        """

        Returns the control points, or control vertices, of a curve object.  If the curve is a rational NURBS curve, the euclidean control vertices are returned.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Array : The control points of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(308, 1, (12, 0), ((12, 0), (12, 0)), u'CurvePoints', None, object, index)

    def curve_radius(self, object, point, index):
        """

        Returns the radius of curvature at a point on a curve.

        Parameters

        Object : Required, String, str
        Point : Required, Array, arr
        Index : Optional, Number, int

        Returns

        Number : The radius of curvature at the point on the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(80, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveRadius', None, object, point, index)

    def curve_seam(self, object, parameter):
        """

        Adjusts the seam, or start/end, point of a closed curve.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(527, 1, (12, 0), ((12, 0), (12, 0)), u'CurveSeam', None, object, parameter)

    def curve_start_point(self, object, index):
        """

        Returns the start point of a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Array : The 3-D starting point of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(99, 1, (12, 0), ((12, 0), (12, 0)), u'CurveStartPoint', None, object, index)

    def curve_surface_intersection(self, curve, surface, tolerance, angle_tolerance):
        """

        Calculates the intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.

        Parameters

        Curve : Required, String, str
        Surface : Required, String, str
        Tolerance : Optional, Number, dbl
        AngleTolerance : Optional, Number, dbl

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

        return self._ApplyTypes_(424, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'CurveSurfaceIntersection', None, curve, surface, tolerance, angle_tolerance)

    def curve_tangent(self, object, parameter, index):
        """

        Returns a 3-D vector that is the tangent to a curve at a parameter.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl
        Index : Optional, Number, int

        Returns

        Array : A  3-D vector if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(363, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'CurveTangent', None, object, parameter, index)

    def curve_weights(self, object, index):
        """

        Returns an array of weight values that are assigned to the control points of a curve.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Array : The weight values of the curve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(314, 1, (12, 0), ((12, 0), (12, 0)), u'CurveWeights', None, object, index)

    def divide_curve(self, object, segments, create, points):
        """

        Divides a curve object into a specified number of segments.

        Parameters

        Object : Required, String, str
        Segments : Required, Number, lng
        Create : Optional, Boolean, bln
        Points : Optional, Boolean, bln

        Returns

        Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
        Array : If blnPoints is False, then an array containing division curve parameters if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(78, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'DivideCurve', None, object, segments, create, points)

    def divide_curve_equidistant(self, object, distance, create, points):
        """

        Unlike the DivideCurve and DivideCurveLength, which divides a curve based on arc length, or the distance along the curve between two points, this function divides a curve based on the linear distance between points.

        Parameters

        Object : Required, String, str
        Distance : Required, Number, dbl
        Create : Optional, Boolean, bln
        Points : Optional, Boolean, bln

        Returns

        Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
        Array : If blnPoints is False, then an array containing division curve parameters if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(913, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'DivideCurveEquidistant', None, object, distance, create, points)

    def divide_curve_length(self, object, length, create, points):
        """

        Divides a curve object into segments of a specified length.

        Parameters

        Object : Required, String, str
        Length : Required, Number, dbl
        Create : Optional, Boolean, bln
        Points : Optional, Boolean, bln

        Returns

        Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
        Array : If blnPoints is False, then an array containing division curve parameters if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(374, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'DivideCurveLength', None, object, length, create, points)

    def ellipse_center_point(self, object):
        """

        Returns the center point of an elliptical-shaped curve object.

        Parameters

        Object : Required, String, str

        Returns

        Array : The 3-D center point of the ellipse if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(524, 1, (12, 0), ((12, 0)), u'EllipseCenterPoint', None, object)

    def ellipse_quad_points(self, object):
        """

        Returns the quadrant points of an elliptical-shaped curve object.

        Parameters

        Object : Required, String, str

        Returns

        Array : An array of 3-D points identifying the quadrants of the ellipse if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(525, 1, (12, 0), ((12, 0)), u'EllipseQuadPoints', None, object)

    def evaluate_curve(self, object, parameter, index):
        """

        Evaluates a curve at a parameter.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl
        Index : Optional, Number, int

        Returns

        Array : A 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(100, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'EvaluateCurve', None, object, parameter, index)

    def explode_curves(self, object, objects, delete):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def extend_curve(self, object, type, side, objects):
        """

        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters

        Object : Required, String, str
        Type : Required, Number, int
        Side : Required, Number, int
        Objects : Required, Array, arr

        Returns

        String : The identifier of the extended object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(438, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'ExtendCurve', None, object, type, side, objects)

    def extend_curve_length(self, object, type, side, length):
        """

        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters

        Object : Required, String, str
        Type : Required, Number, int
        Side : Required, Number, int
        Length : Required, Number, dbl

        Returns

        String : The identifier of the extended object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(436, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'ExtendCurveLength', None, object, type, side, length)

    def extend_curve_point(self, object, side, point):
        """

        Extends a non-closed curve object by smooth extension to a point.

        Parameters

        Object : Required, String, str
        Side : Required, Number, int
        Point : Required, Array, arr

        Returns

        String : The identifier of the extended object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(437, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ExtendCurvePoint', None, object, side, point)

    def fair_curve(self, object, tolerance):
        """

        Fairs a curve object. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvature variations while limiting the geometry changes to be no more than the specified tolerance. Sometimes several applications of this method are necessary to remove nasty curvature problems.

        Parameters

        Object : Required, String, str
        Tolerance : Optional, Number, dbl

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(599, 1, (12, 0), ((12, 0), (12, 0)), u'FairCurve', None, object, tolerance)

    def fit_curve(self, object, degree, tolerance, angle_tolerance):
        """

        Reduces the number of curve control points while maintaining the curve's same general shape.  Use this function for replacing curves with too many control points.  For more information, see the Rhino help file for the FitCrv command.

        Parameters

        Object : Required, String, str
        Degree : Optional, Number, int
        Tolerance : Optional, Number, dbl
        AngleTolerance : Optional, Number, dbl

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(813, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'FitCurve', None, object, degree, tolerance, angle_tolerance)

    def insert_curve_knot(self, object, parameter, symmetrical):
        """

        Inserts a knot into a curve object.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl
        Symmetrical : Optional, Boolean, bln

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(515, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'InsertCurveKnot', None, object, parameter, symmetrical)

    def is_arc(self, object, index):
        """

        Verifies an object is an arc curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(101, 1, (12, 0), ((12, 0), (12, 0)), u'IsArc', None, object, index)

    def is_circle(self, object, index):
        """

        Verifies an object is a circle curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(102, 1, (12, 0), ((12, 0), (12, 0)), u'IsCircle', None, object, index)

    def is_curve(self, object, index):
        """

        Verifies an object is a curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(103, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurve', None, object, index)

    def is_curve_closable(self, object, tolerance):
        """

        Decide if it makes sense to close off the curve by moving  the endpoint to the start based on start-end gap size and length of curve as approximated by chord defined by 6 points.

        Parameters

        Object : Required, String, str
        Tolerance : Optional, Number, dbl

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(441, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurveClosable', None, object, tolerance)

    def is_curve_closed(self, object, index):
        """

        Verifies an object is a closed curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(104, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurveClosed', None, object, index)

    def is_curve_in_plane(self, object, plane, ay, ay, ay, ay):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def is_curve_linear(self, object, index):
        """

        Verifies an object is a linear curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(105, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurveLinear', None, object, index)

    def is_curve_periodic(self, object, index):
        """

        Verifies an object is a periodic curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(106, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurvePeriodic', None, object, index)

    def is_curve_planar(self, object, index):
        """

        Verifies an object is a planar curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(107, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurvePlanar', None, object, index)

    def is_curve_rational(self, object, index):
        """

        Verifies an object is a rational NURBS curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(380, 1, (12, 0), ((12, 0), (12, 0)), u'IsCurveRational', None, object, index)

    def is_ellipse(self, object):
        """

        Verifies an object is an elliptical-shaped curve object.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(523, 1, (12, 0), ((12, 0)), u'IsEllipse', None, object)

    def is_line(self, object, index):
        """

        Verifies an object is a line curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(108, 1, (12, 0), ((12, 0), (12, 0)), u'IsLine', None, object, index)

    def is_point_on_curve(self, object, point, point):
        """

        Verifies that a point is on a curve.

        Parameters

        Object : Required, String, str
        Point : Required, Array, arr
        Point : Optional, Number, arr

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(318, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'IsPointOnCurve', None, object, point, point)

    def is_poly_curve(self, object, index):
        """

        Verifies an object is a polycurve object.  A polycurve is a curve that is represented by a sequence of contiguous curve segments.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(368, 1, (12, 0), ((12, 0), (12, 0)), u'IsPolyCurve', None, object, index)

    def is_polyline(self, object, index):
        """

        Verifies an object is a polyline curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(110, 1, (12, 0), ((12, 0), (12, 0)), u'IsPolyline', None, object, index)

    def join_curves(self, object, delete):
        """

        Joins two or more curve object together to form one or more curves or polycurves.

        Parameters

        Object : Required, Array, str
        Delete : Optional, Boolean, bln

        Returns

        Array : An array of strings identifying the newly created curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(111, 1, (12, 0), ((12, 0), (12, 0)), u'JoinCurves', None, object, delete)

    def line_fit_from_points(self, object):
        """

        Returns the starting and ending points of a line that was fit through an array of 3-D points.

        Parameters

        Object : Required, Array, str

        Returns

        Array : An array containing the starting and ending points of the fit line if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(726, 1, (12, 0), ((12, 0)), u'LineFitFromPoints', None, object)

    def make_curve_non_periodic(self, object, delete):
        """

        Makes a periodic curve non-periodic.  Non-periodic curves can develop kinks when deformed.

        Parameters

        Object : Required, String, str
        Delete : Optional, Boolean, bln

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(925, 1, (12, 0), ((12, 0), (12, 0)), u'MakeCurveNonPeriodic', None, object, delete)

    def make_curve_periodic(self, object, delete):
        """

        Makes an existing curve a periodic NURBS curve.  A periodic NURBS curve is a closed curve with a simple knot at the seam.  If a joined curve is made periodic, it becomes a single-span curve and can no longer be exploded.

        Parameters

        Object : Required, String, str
        Delete : Optional, Boolean, bln

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(444, 1, (12, 0), ((12, 0), (12, 0)), u'MakeCurvePeriodic', None, object, delete)

    def mesh_polyline(self, polyline):
        """

        Creates a polygon mesh object based on a closed polyline curve object. The newly created polygon mesh object is added to the document.

        Parameters

        Polyline : Required, String, str

        Returns

        String : The identifier of the new polygon mesh object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(546, 1, (12, 0), ((12, 0)), u'MeshPolyline', None, polyline)

    def offset_curve(self, object, direction, normal, style):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def offset_curve_on_surface(self, curve, surface):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def planar_closed_curve_containment(self, curve1, curve2, plane, ay, ay, ay, ay, tolerance):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def planar_curve_collision(self, curve1, curve2, plane, ay, ay, ay, ay, tolerance):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def point_in_planar_closed_curve(self, point, curve, plane, ay, ay, ay, ay, tolerance):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def poly_curve_count(self, object, index):
        """

        Returns the number of curve segments that make up a polycurve.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The number of curve segments in a polycurve if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(369, 1, (12, 0), ((12, 0), (12, 0)), u'PolyCurveCount', None, object, index)

    def polyline_vertices(self, object, index):
        """

        Returns the vertices of a polyline curve object.

        Parameters

        Object : Required, String, str
        Index : Optional, Number, int

        Returns

        Array : An  array of 3-D vertex points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(112, 1, (12, 0), ((12, 0), (12, 0)), u'PolylineVertices', None, object, index)

    def project_curve_to_mesh(self, curve, curves, mesh, meshes, direction):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def project_curve_to_surface(self, curve, curves, surface, surfaces, direction):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def rebuild_curve(self, object, degree, point_count):
        """

        Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.

        Parameters

        Object : Required, String, str
        Degree : Optional, Number, int
        PointCount : Optional, Number, int

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(814, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'RebuildCurve', None, object, degree, point_count)

    def remove_curve_knot(self, object, parameter):
        """

        Deletes a knot from a curve object.

        Parameters

        Object : Required, String, str
        Parameter : Required, Number, dbl

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(916, 1, (12, 0), ((12, 0), (12, 0)), u'RemoveCurveKnot', None, object, parameter)

    def reverse_curve(self, object):
        """

        Reverses the direction of a curve object. This feature can also be found in Rhino's Dir command.

        Parameters

        Object : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(542, 1, (12, 0), ((12, 0)), u'ReverseCurve', None, object)

    def simplify_curve(self, object, flags):
        """

        6.  Segments that meet with G1-continuity have there ends tuned up so that they meet with G1-continuity to within machine precision.

        Parameters

        Object : Required, String, str
        Flags : Optional, Number, int

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(573, 1, (12, 0), ((12, 0), (12, 0)), u'SimplifyCurve', None, object, flags)

    def split_curve(self, object, parameter, parameters, delete):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def trim_curve(self, object, interval, delete):
        """

        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters

        Object : Required, String, str
        Interval : Required, Array, arr
        Delete : Optional, Boolean, bln

        Returns

        String : The identifier of the newly created curve object, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(505, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'TrimCurve', None, object, interval, delete)

