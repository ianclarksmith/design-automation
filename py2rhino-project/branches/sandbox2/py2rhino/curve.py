# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Curve(IRhinoScript):



    def add_arc(self, plane, radius, angle):
        """        
        Adds an arc curve to the document.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane on which the arc will lie. The origin of the plane will be the center point of the arc. The X-axis of the plane will define the 0 angle direction.
            
        radius, Double, Required        
        The radius arc.
            
        angle, Double, Required        
        A angle or interval, in degrees, of the arc.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(651, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1)), u"AddArc", None, flatten(plane), radius, angle)

    def add_arc3_pt(self, start, end, point):
        """        
        Adds a 3-point arc curve to the document.
    
        Parameters
        ==========

        start, Array of ????, Required        
        The starting point of the arc.
            
        end, Array of ????, Required        
        The ending point of the arc.
            
        point, Array of ????, Required        
        A point on the arc.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(82, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddArc3Pt", None, flatten(start), flatten(end), flatten(point))

    def add_circle(self, plane, radius):
        """        
        Adds a circle curve to the document.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane on which the circle will lie. The origin of the plane will be the center point of the circle.
            
        radius, Double, Required        
        The radius of the circle.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(83, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"AddCircle", None, flatten(plane), radius)

    def add_circle3_pt(self, start, end, point):
        """        
        Adds a 3-point circle curve to the document.
    
        Parameters
        ==========

        start, Array of ????, Required        
        The first point of the circle.
            
        end, Array of ????, Required        
        The second point of the circle.
            
        point, Array of ????, Required        
        The third point of the circle.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(84, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddCircle3Pt", None, flatten(start), flatten(end), flatten(point))

    def add_curve(self, points, degree):
        """        
        Adds a control points curve object to the document.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        degree, Integer, Optional        
        The degree of the curve.  If omitted, a degree 3 curve is created.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(77, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_I2, 1)), u"AddCurve", None, flatten(points), degree)

    def add_ellipse(self, plane, x_radius, y_radius):
        """        
        Adds an elliptical curve to the document.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane on which the ellipse will lie. The origin of the plane will be the center point of the ellipse.
            
        x_radius, Double, Required        
        The radius in the X-axis direction.
            
        y_radius, Double, Required        
        The radius in the Y-axis direction.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(679, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1)), u"AddEllipse", None, flatten(plane), x_radius, y_radius)

    def add_ellipse3_pt(self, center, second, third):
        """        
        Adds a 3 point elliptical curve to the document.
    
        Parameters
        ==========

        center, Array of ????, Required        
        The center point of the ellipse.
            
        second, Array of ????, Required        
        The end point of the X-axis.
            
        third, Array of ????, Required        
        The end point of the Y-axis.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(680, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddEllipse3Pt", None, flatten(center), flatten(second), flatten(third))

    def add_fillet_curve(self, curve0, curve1, radius, point0, point1):
        """        
        Adds a fillet curve between two curve objects.
    
        Parameters
        ==========

        curve0, String, Required        
        The identifier of the first curve object.
            
        curve1, String, Required        
        The identifier of the second curve object.
            
        radius, Double, Optional        
        The fillet radius. If omitted, a radius of 1.0 is specified.
            
        point0, Array of ????, Optional        
        The base point on the first curve. If omitted, the starting point of the curve is used.
            
        point1, Array of ????, Optional        
        The base point on the second curve. If omitted, the starting point of the curve is used.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(574, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddFilletCurve", None, curve0, curve1, radius, flatten(point0), flatten(point1))

    def add_interp_crv_on_srf(self, object, points):
        """        
        Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.
    
        Parameters
        ==========

        object, String, Required        
        The surface object's identifier.
            
        points, Array of ????, Required        
        An array of 3-D points that lie on the specified surface. The array must contain at least two points.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(513, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"AddInterpCrvOnSrf", None, object, flatten(points))

    def add_interp_crv_on_srf_u_v(self, object, points):
        """        
        Adds an interpolated curve object. based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.
    
        Parameters
        ==========

        object, String, Required        
        The surface object's identifier.
            
        points, Array of ????, Required        
        An array of 2-D surface parameters. The array must contain at least two sets of surface parameters.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(641, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"AddInterpCrvOnSrfUV", None, object, flatten(points))

    def add_interp_curve(self, points, degree, knot_style, start_tan, end_tan):
        """        
        Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array containing 3-D points to interpolate.  For periodic curves, if the final point is a duplicate of the initial point, it is ignored. Note, the number of control points must be >= (intDegree+1).
            
        degree, Integer, Optional        
        The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.  For intKnotStyle = 4 or 5, the degree must be odd.
            
        knot_style, Integer, Optional        
        The knot style to use, and whether the curve should be periodic.  If omitted, uniform knots (0) are created.
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
            
        start_tan, Array of ????, Optional        
        A 3-D vector that specifies a tangency condition at the beginning of the curve. If the curve is to periodic, this argument must be omitted.
            
        end_tan, Array of ????, Optional        
        A 3-D vector that specifies a tangency condition at the end of the curve. If the curve is to periodic, this argument must be omitted.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(268, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_I2, 1), (VT_I2, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddInterpCurve", None, flatten(points), degree, knot_style, flatten(start_tan), flatten(end_tan))

    def add_interp_curve_ex(self, points, degree, knot_style, sharp, start_tangent, end_tangent):
        """        
        Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array containing 3-D points to interpolate. Note, the number of control points must be >= (intDegree+1).
            
        degree, Integer, Optional        
        The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.
            
        knot_style, Integer, Optional        
        The knot style to use. If omitted, a knot style = 0 is used. The knot style determines how an interpolated curve will be parameterized.
		Value
		Description
		0
		Uniform.  The knot spacing is always 1 and is not based on the physical spacing of points.
		1
		Chord. The spacing between the points is used for the knot spacing
		2
            
        sharp, Boolean, Optional        
        If True, when you create a closed curve, it will have a kink at the start/end point. If False (default), a smooth closure will be created.
            
        start_tangent, Array of ????, Optional        
        A 3-D vector that specifies a tangency condition at the beginning of the curve.
            
        end_tangent, Array of ????, Optional        
        A 3-D vector that specifies a tangency condition at the end of the curve.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(520, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddInterpCurveEx", None, flatten(points), degree, knot_style, sharp, flatten(start_tangent), flatten(end_tangent))

    def add_line(self, start, end):
        """        
        Adds a line curve to the current model.
    
        Parameters
        ==========

        start, Array of ????, Required        
        The starting point of the line.
            
        end, Array of ????, Required        
        The ending point of the line.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(70, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"AddLine", None, flatten(start), flatten(end))

    def add_nurbs_curve(self, points, knots, degree, weights):
        """        
        Adds a NURBS curve object to the document.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D control points.
            
        knots, Array of ????, Required        
        The knot values for the curve.  The number of elements in arrKnots must equal the number of elements in arrPoints plus intDegree minus one (1).
            
        degree, Integer, Required        
        The degree of the curve.  The degree must be greater than or equal to one (1).
            
        weights, Array of ????, Optional        
        The weight values for the curve.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(309, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_I2, 1), (VT_VARIANT, 1)), u"AddNurbsCurve", None, flatten(points), flatten(knots), degree, flatten(weights))

    def add_polyline(self, points):
        """        
        Adds a polyline curve object to the current model.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.  Duplicate, consecutive points found in the array will be removed.  The array must contain at least two 3-D points.  If the array contains less than four points, then the first point and the last point must be different.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(85, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"AddPolyline", None, flatten(points))

    def add_sub_crv(self, object, param0, param1):
        """        
        Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a closed, planar curve object.
            
        param0, Double, Required        
        The first parameter on the source curve.
            
        param1, Double, Required        
        The second parameter on the source curve.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(681, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1)), u"AddSubCrv", None, object, param0, param1)

    def arc_angle(self, object, index):
        """        
        Returns the angle of an arc curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The angle in degrees if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(86, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"ArcAngle", None, object, index)

    def arc_center_point(self, object, index):
        """        
        Returns the center point of an arc curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(87, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"ArcCenterPoint", None, object, index)

    def arc_mid_point(self, object, index):
        """        
        Returns the mid point of an arc curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(88, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"ArcMidPoint", None, object, index)

    def arc_radius(self, object, index):
        """        
        Returns the radius of an arc curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The radius of the arc if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(89, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"ArcRadius", None, object, index)

    def circle_center_point(self, object, index):
        """        
        Returns the center point of a circle curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        The 3-D center point of the circle if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(90, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CircleCenterPoint", None, object, index)

    def circle_circumference(self, object, index):
        """        
        Returns the circumference of a circle curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The circumference of the circle if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(91, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CircleCircumference", None, object, index)

    def circle_radius(self, object, index):
        """        
        Returns the radius of a circle curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The radius of the circle if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(92, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CircleRadius", None, object, index)

    def close_curve(self, object, tolerance):
        """        
        Closes an open curve object by making adjustments to the end points so that they meet at a point.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        tolerance, Double, Optional        
        The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.
            
        Returns
        =======

        string
        The identifier of the closed curve object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(440, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"CloseCurve", None, object, tolerance)

    def convert_curve_to_polyline(self, object, angle_tolerance, tolerance, delete_input):
        """        
        Converts a curve to a polyline curve.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        angle_tolerance, Double, Optional        
        The maximum angle between curve tangents at line endpoints.  If omitted, the angle tolerance is set to 5.0.
            
        tolerance, Double, Optional        
        The distance tolerance at segment midpoints.  If omitted, the tolerance is set to 0.01.
            
        delete_input, Boolean, Optional        
        Delete the curve object specified by strObject.  If omitted, strObject will not be deleted.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(377, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1)), u"ConvertCurveToPolyline", None, object, angle_tolerance, tolerance, delete_input)

    def curve_arc_length_point(self, object, length, from_start):
        """        
        Returns the point on the curve that is a specified arc length from the start of the curve.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        length, Double, Required        
        The arc length from the start of the curve to evaluate.
            
        from_start, Boolean, Optional        
        If not specified or True, then the arc length point is calculated from the start of the curve. If False, the arc length point is calculated from the end of the curve.
            
        Returns
        =======

        array
        The 3-D point if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(658, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1)), u"CurveArcLengthPoint", None, object, length, from_start)

    def curve_area(self, object, objects):
        """        
        Returns that area of closed planar curves. The results are based on the current drawing units.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a closed, planar curve object.
            
        objects, Array of ????, Required        
        An array of strings containing the identifiers of one or more closed, planar curve objects.
            
        Returns
        =======

        array
        An array of area information if successful.  The array will contain the following information:

        number
        The area. If more than one curve was specified, the value will be the cumulative area.

        number
        The absolute (+/-) error bound for the area.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(643, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"CurveArea", None, object, flatten(objects))

    def curve_area_centroid(self, object, objects):
        """        
        Returns that area centroid of closed, planar curves. The results are based on the current drawing units.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a closed, planar curve object.
            
        objects, Array of ????, Required        
        An array of strings containing the identifiers of one or more closed, planar curve objects.
            
        Returns
        =======

        array
        An array of area centroid information if successful.  The array will contain the following information:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(677, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"CurveAreaCentroid", None, object, flatten(objects))

    def curve_arrows(self, object, style):
        """        
        Enables or disabled a curve object's annotation arrows.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        style, Integer, Optional        
        The style of annotation arrows to be displayed.  The styles are as follows:
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

        number
        If intStyle is not specified, the current annotation arrow style if successful.

        number
        If intStyle is specified, the previous annotation arrow style if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(578, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveArrows", None, object, style)

    def curve_boolean_difference(self, curve_a, curve_b):
        """        
        Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    
        Parameters
        ==========

        curve_a, String, Required        
        The identifier of the first curve object.
            
        curve_b, String, Required        
        The identifier of the second curve object.
            
        Returns
        =======

        array
        The identifiers of the new objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(811, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"CurveBooleanDifference", None, curve_a, curve_b)

    def curve_boolean_intersection(self, curve_a, curve_b):
        """        
        Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    
        Parameters
        ==========

        curve_a, String, Required        
        The identifier of the first curve object.
            
        curve_b, String, Required        
        The identifier of the second curve object.
            
        Returns
        =======

        array
        The identifiers of the new objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(810, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"CurveBooleanIntersection", None, curve_a, curve_b)

    def curve_boolean_union(self, curves):
        """        
        Calculates the union of two or more closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    
        Parameters
        ==========

        curves, Array of ????, Required        
        The identifiers of two or more curve objects.
            
        Returns
        =======

        array
        The identifiers of the new objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(809, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"CurveBooleanUnion", None, flatten(curves))

    def curve_brep_intersect(self, curve, brep, tolerance):
        """        
        Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function, this function works on trimmed surfaces.
    
        Parameters
        ==========

        curve, String, Required        
        The curve object's identifier.
            
        brep, String, Required        
        The brep object's identifier.
            
        tolerance, Double, Optional        
        The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..
            
        Returns
        =======

        array
        An array of strings identifying the newly created intersection curve and point objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(545, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1)), u"CurveBrepIntersect", None, curve, brep, tolerance)

    def curve_closest_object(self, curve, object, objects):
        """        
        Returns the 3-D point locations on two objects where they are closest to each other.  Note, this function provides similar functionality to that of Rhino's ClosestPt command when used with the Object option.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the curve object to test.
            
        object, String, Required        
        The identifier of a point cloud, curve, surface, or polysurface to test against.
            
        objects, Array of ????, Required        
        The identifiers of one or more point cloud, curve, surface, or polysurface to test against.
            
        Returns
        =======

        array
        An array containing the results of the closest point calculation if successful.  The elements of the array are as follows:

        string
        The identifier of the closest object.

        array
        The 3-D point that is closest to the closest object.

        array
        The 3-D point that is closest to the test curve.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(870, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1)), u"CurveClosestObject", None, curve, object, flatten(objects))

    def curve_closest_point(self, object, point, index):
        """        
        Returns the parameter of the point on a curve that is closest to a test point.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        point, Array of ????, Required        
        The test, or sampling, point.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The parameter of the closest point on the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(93, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)), u"CurveClosestPoint", None, object, flatten(point), index)

    def curve_contour_points(self, object, start_point, end_point, interval):
        """        
        Returns the 3-D point locations calculated by contouring a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a curve object.
            
        start_point, Array of ????, Required        
        The 3-D starting point of a center line.
            
        end_point, Array of ????, Required        
        The 3-D ending point of a center line.
            
        interval, Double, Optional        
        The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
            
        Returns
        =======

        array
        An array of 3-D points, one for each contour, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(748, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1)), u"CurveContourPoints", None, object, flatten(start_point), flatten(end_point), interval)

    def curve_curvature(self, object, parameter):
        """        
        Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The parameter to evaluate.
            
        Returns
        =======

        array
        An array of curvature information if successful.  The array will contain the following information:

        number
        Radius of curvature

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(379, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"CurveCurvature", None, object, parameter)

    def curve_curve_intersection(self, object1, object2, tolerance):
        """        
        Calculates the intersection of two curve objects.
    
        Parameters
        ==========

        object1, String, Required        
        The identifier of the first curve object.
            
        object2, String, Optional        
        The identifier of the second curve object.  If omitted, the a self-intersection test will be performed on strObject1.
            
        tolerance, Double, Optional        
        The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
            
        Returns
        =======

        array
        A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:

        number
        The intersection event type, either Point (1) or Overlap (2).

        number
        If the event type is Point (1), then the first curve parameter.

        number
        If the event type is Point (1), then the first curve parameter.

        number
        If the event type is Point (1), then the second curve parameter.

        number
        If the event type is Point (1), then the second curve parameter.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(423, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1)), u"CurveCurveIntersection", None, object1, object2, tolerance)

    def curve_degree(self, object, index):
        """        
        Returns the degree of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The degree of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(94, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveDegree", None, object, index)

    def curve_deviation(self, curve_a, curve_b):
        """        
        Returns the minimum and maximum deviation between two curve objects. For more information on curve deviation, see the Rhino help file for the CrvDeviation command.
    
        Parameters
        ==========

        curve_a, String, Required        
        The identifier of the first curve object.
            
        curve_b, String, Required        
        The identifier of the second curve object.
            
        Returns
        =======

        array
        An array of numbers identifying the minimum and maximum deviation between the two curves if successful.

        number
        Curve A parameter at maximum overlap distance point

        number
        Curve A parameter at maximum overlap distance point

        number
        Maximum overlap distance

        number
        Curve A parameter at minimum distance point

        number
        Curve B parameter at minimum distance point

        number
        Minimum distance between curves

        null
        On error or if no intervals of overlap were found.

        """

        return self._ApplyTypes_(687, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"CurveDeviation", None, curve_a, curve_b)

    def curve_dim(self, object, index):
        """        
        Returns the dimension of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The dimension of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(381, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveDim", None, object, index)

    def curve_directions_match(self, curve1, curve2):
        """        
        Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.
    
        Parameters
        ==========

        curve1, String, Required        
        The identifier of the first curve to compare.
            
        curve2, String, Required        
        The identifier of the second curve to compare.
            
        Returns
        =======

        boolean
        True if the curve directions match, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(543, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"CurveDirectionsMatch", None, curve1, curve2)

    def curve_discontinuity(self, object, style):
        """        
        Search for a derivatitive, tangent, or curvature discontinuity in a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        style, Integer, Required        
        The type of continuity to test for.  The types of continuity are as follows:
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

        array
        An array of 3-D points where the curve is discontinuous if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(579, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveDiscontinuity", None, object, style)

    def curve_domain(self, object, index):
        """        
        Returns the domain of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        The domain of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(95, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveDomain", None, object, index)

    def curve_edit_points(self, object, return_parameters, index):
        """        
        Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        return_parameters, Boolean, Optional        
        Return the edit points as an array of parameter values.  If omitted, the edit points are returned as an array of 3-D points.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.

        array
        If blnReturnParameters is True, then an array of parameter values if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(442, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_I2, 1)), u"CurveEditPoints", None, object, return_parameters, index)

    def curve_end_point(self, object, index):
        """        
        Returns the end point of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        The 3-D end point of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(96, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveEndPoint", None, object, index)

    def curve_evaluate(self, object, parameter, derivative):
        """        
        A general purpose curve evaluator.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The evaluation parameter.
            
        derivative, Integer, Required        
        The number of derivatives to evaluate.
            
        Returns
        =======

        array
        An array of length (intDerivative+1) if successful.  The array elements are as follows:

        array
        The 3-D point

        array
        The first derivative

        array
        The second derivative

        array
        etc...

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(489, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1)), u"CurveEvaluate", None, object, parameter, derivative)

    def curve_fillet_points(self, curve0, curve1, radius, base_point0, base_point1):
        """        
        Find points at which to cut a pair of curves so that a fillet of a specified radius fits.  A fillet point is a pair of points (arrPoint0, arrPoint1) such that there is a circle of radius dblRadius tangent to curve strCurve0 at arrPoint0 and tangent to curve strCurve1 at arrPoint1.
		Of all possible fillet points, this function returns the one which is the closest to the base point arrBasePoint0, arrBasePoint1.  Distance from the base point is measured by the sum of arc lengths along the two curves.
    
        Parameters
        ==========

        curve0, String, Required        
        The identifier of the first curve object.
            
        curve1, String, Required        
        The identifier of the second curve object.
            
        radius, Double, Optional        
        The fillet radius. If omitted, a radius of 1.0 is specified.
            
        base_point0, Array of ????, Optional        
        The base point on the first curve. If omitted, the starting point of the curve is used.
            
        base_point1, Array of ????, Optional        
        The base point on the second curve. If omitted, the starting point of the curve is used.
            
        Returns
        =======

        array
        If blnPoints is True, then an array of point and vector values if successful.  The array elements are as follows:

        string
        If blnPoints is False, then the identifier of the fillet curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(572, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"CurveFilletPoints", None, curve0, curve1, radius, flatten(base_point0), flatten(base_point1))

    def curve_frame(self, object, parameter):
        """        
        Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The parameter to evaluate.
            
        Returns
        =======

        array
        The plane at the specified parameter if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(675, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"CurveFrame", None, object, parameter)

    def curve_knot_count(self, object, index):
        """        
        Returns the knot count of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The number of knots if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(310, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveKnotCount", None, object, index)

    def curve_knots(self, object, index):
        """        
        Returns the knots, or knot vector, of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        The knot values of the curve  if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(311, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveKnots", None, object, index)

    def curve_length(self, object, index, sub_domain):
        """        
        Returns the length of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        sub_domain, Array of ????, Optional        
        An array of two numbers identifying the sub-domain of the curve on which the calculation will be performed.  The two parameters (sub-domain) must be non-decreasing.  If omitted, the length of the entire curve is returned.
            
        Returns
        =======

        number
        The length of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(97, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_VARIANT, 1)), u"CurveLength", None, object, index, flatten(sub_domain))

    def curve_mid_point(self, object):
        """        
        Returns the mid point of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        The 3-D mid point of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(577, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"CurveMidPoint", None, object)

    def curve_normal(self, object):
        """        
        Returns the normal direction of the plane in which a planar curve object lies.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        The 3-D normal vector if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(521, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"CurveNormal", None, object)

    def curve_perp_frame(self, object, parameter):
        """        
        Returns the perpendicular plane at a parameter of a curve.  The result is relatively parallel (zero-twisting) plane.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The parameter to evaluate.
            
        Returns
        =======

        array
        The plane at the specified parameter if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(676, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"CurvePerpFrame", None, object, parameter)

    def curve_plane(self, curve):
        """        
        Returns the plane in which a planar curve lies. Note, this function works only on planar curves.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of a planar curve object
            
        Returns
        =======

        array
        The plane in which the curve lies if successful.

        null
        On error.

        """

        return self._ApplyTypes_(609, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"CurvePlane", None, curve)

    def curve_point_count(self, object, index):
        """        
        Returns the control points count of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The number of control points if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(98, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurvePointCount", None, object, index)

    def curve_points(self, object, index):
        """        
        Returns the control points, or control vertices, of a curve object.  If the curve is a rational NURBS curve, the euclidean control vertices are returned.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        The control points of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(308, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurvePoints", None, object, index)

    def curve_radius(self, object, point, index):
        """        
        Returns the radius of curvature at a point on a curve.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        point, Array of ????, Required        
        The test, or sampling, point.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The radius of curvature at the point on the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(80, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)), u"CurveRadius", None, object, flatten(point), index)

    def curve_seam(self, object, parameter):
        """        
        Adjusts the seam, or start/end, point of a closed curve.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The parameter of the new start/end point. Note, if successful, the resulting curve's domain will start at dblParameter.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(527, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"CurveSeam", None, object, parameter)

    def curve_start_point(self, object, index):
        """        
        Returns the start point of a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        The 3-D starting point of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(99, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveStartPoint", None, object, index)

    def curve_surface_intersection(self, curve, surface, tolerance, angle_tolerance):
        """        
        Calculates the intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of a curve object.
            
        surface, String, Required        
        The identifier of a surface object.
            
        tolerance, Double, Optional        
        The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
            
        angle_tolerance, Double, Optional        
        The angle tolerance in degrees.  The angle tolerance is used to determine when the curve is tangent to the surface.  If omitted, the document's current angle tolerance is used.
            
        Returns
        =======

        array
        A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:

        number
        The intersection event type, either Point (1) or Overlap (2).

        number
        If the event type is Point (1), then the curve parameter.

        number
        If the event type is Point (1), then the curve parameter.

        number
        If the event type is Point (1), then the U surface parameter.

        number
        If the event type is Point (1), then the V surface parameter.

        number
        If the event type is Point (1), then the U surface parameter.

        number
        If the event type is Point (1), then the V surface parameter.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(424, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1)), u"CurveSurfaceIntersection", None, curve, surface, tolerance, angle_tolerance)

    def curve_tangent(self, object, parameter, index):
        """        
        Returns a 3-D vector that is the tangent to a curve at a parameter.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The parameter to evaluate.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        A  3-D vector if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(363, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1)), u"CurveTangent", None, object, parameter, index)

    def curve_weights(self, object, index):
        """        
        Returns an array of weight values that are assigned to the control points of a curve.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        The weight values of the curve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(314, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"CurveWeights", None, object, index)

    def divide_curve(self, object, segments, create, points):
        """        
        Divides a curve object into a specified number of segments.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        segments, Integer, Required        
        The number of segments.
            
        create, Boolean, Optional        
        Create the division points. If omitted or False, points are not created.
            
        points, Boolean, Optional        
        Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
            
        Returns
        =======

        array
        If blnPoints is not specified or True, then an array containing 3-D division points if successful.

        array
        If blnPoints is False, then an array containing division curve parameters if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(78, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I4, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"DivideCurve", None, object, segments, create, points)

    def divide_curve_equidistant(self, object, distance, create, points):
        """        
        Divides a curve such that the linear distance between the points is equal.
		Unlike the DivideCurve and DivideCurveLength, which divides a curve based on arc length, or the distance along the curve between two points, this function divides a curve based on the linear distance between points.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        distance, Double, Required        
        The linear distance between division points.
            
        create, Boolean, Optional        
        Create the division points. If omitted or False, points are not created.
            
        points, Boolean, Optional        
        Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
            
        Returns
        =======

        array
        If blnPoints is not specified or True, then an array containing 3-D division points if successful.

        array
        If blnPoints is False, then an array containing division curve parameters if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(913, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"DivideCurveEquidistant", None, object, distance, create, points)

    def divide_curve_length(self, object, length, create, points):
        """        
        Divides a curve object into segments of a specified length.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        length, Double, Required        
        The length of each segment.
            
        create, Boolean, Optional        
        Create the division points. If omitted or False, points are not created.
            
        points, Boolean, Optional        
        Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
            
        Returns
        =======

        array
        If blnPoints is not specified or True, then an array containing 3-D division points if successful.

        array
        If blnPoints is False, then an array containing division curve parameters if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(374, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"DivideCurveLength", None, object, length, create, points)

    def ellipse_center_point(self, object):
        """        
        Returns the center point of an elliptical-shaped curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        The 3-D center point of the ellipse if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(524, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"EllipseCenterPoint", None, object)

    def ellipse_quad_points(self, object):
        """        
        Returns the quadrant points of an elliptical-shaped curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of 3-D points identifying the quadrants of the ellipse if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(525, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"EllipseQuadPoints", None, object)

    def evaluate_curve(self, object, parameter, index):
        """        
        Evaluates a curve at a parameter.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The parameter to evaluate.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        A 3-D point if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(100, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1)), u"EvaluateCurve", None, object, parameter, index)

    def explode_curves(self, object, objects, delete):
        """        
        Explodes, or un-joins,  one more curve objects.  Polycurves will be exploded into curve segments.  Polylines will be exploded into line segments.  ExplodeCurves will return the curves in
		topological order.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the curve object to explode.
            
        objects, Array of ????, Required        
        An array of strings identifying the curve objects to explode.
            
        delete, Boolean, Optional        
        Delete input objects after exploding.  The default is not to delete objects (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly created curve objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(446, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"ExplodeCurves", None, object, flatten(objects), delete)

    def extend_curve(self, object, type, side, objects):
        """        
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        type, Integer, Required        
        Type of extension.
		Value
		Description
		0
		Line - Creates an line extension tangent to the original curve.
		1
		Arc - Creates an arc extension tangent to the original curve.
		2
            
        side, Integer, Required        
        The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
            
        objects, Array of ????, Required        
        The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.
            
        Returns
        =======

        string
        The identifier of the extended object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(438, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_VARIANT, 1)), u"ExtendCurve", None, object, type, side, flatten(objects))

    def extend_curve_length(self, object, type, side, length):
        """        
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        type, Integer, Required        
        Type of extension.
		Value
		Description
		0
		Line - Creates an line extension tangent to the original curve.
		1
		Arc - Creates an arc extension tangent to the original curve.
		2
            
        side, Integer, Required        
        The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
		Extend from the end of the curve.
		2
            
        length, Double, Required        
        The distance to extend the curve.
            
        Returns
        =======

        string
        The identifier of the extended object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(436, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_R8, 1)), u"ExtendCurveLength", None, object, type, side, length)

    def extend_curve_point(self, object, side, point):
        """        
        Extends a non-closed curve object by smooth extension to a point.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        side, Integer, Required        
        The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
            
        point, Array of ????, Required        
        The 3-D point.
            
        Returns
        =======

        string
        The identifier of the extended object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(437, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_VARIANT, 1)), u"ExtendCurvePoint", None, object, side, flatten(point))

    def fair_curve(self, object, tolerance):
        """        
        Fairs a curve object. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvature variations while limiting the geometry changes to be no more than the specified tolerance. Sometimes several applications of this method are necessary to remove nasty curvature problems.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        tolerance, Double, Optional        
        The fairing tolerance. Of omitted, a default value of 1.0 is used.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(599, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"FairCurve", None, object, tolerance)

    def fit_curve(self, object, degree, tolerance, angle_tolerance):
        """        
        Reduces the number of curve control points while maintaining the curve's same general shape.  Use this function for replacing curves with too many control points.  For more information, see the Rhino help file for the FitCrv command.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        degree, Integer, Optional        
        The curve degree, which must be greater than 1. The default is 3.
            
        tolerance, Double, Optional        
        The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.
            
        angle_tolerance, Double, Optional        
        The kink smoothing tolerance in degrees.  If dblAngleTolerance is 0.0, all kinks are smoothed.  If dblAngleTolerance is > 0.0, kinks smaller than dblAngleTolerance are smoothed.  If dblAngleTolerance is not specified or < 0.0, the document angle tolerance is used for the kink smoothing.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(813, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1), (VT_R8, 1)), u"FitCurve", None, object, degree, tolerance, angle_tolerance)

    def insert_curve_knot(self, object, parameter, symmetrical):
        """        
        Inserts a knot into a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the curve object.
            
        parameter, Double, Required        
        The parameter on the curve.
            
        symmetrical, Boolean, Optional        
        If blnSymmetrical = True, then knots are added on both sides of the center of the curve. The default value is False.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(515, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1)), u"InsertCurveKnot", None, object, parameter, symmetrical)

    def is_arc(self, object, index):
        """        
        Verifies an object is an arc curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(101, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsArc", None, object, index)

    def is_circle(self, object, index):
        """        
        Verifies an object is a circle curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(102, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsCircle", None, object, index)

    def is_curve(self, object, index):
        """        
        Verifies an object is a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(103, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsCurve", None, object, index)

    def is_curve_closable(self, object, tolerance):
        """        
        Decide if it makes sense to close off the curve by moving  the endpoint to the start based on start-end gap size and length of curve as approximated by chord defined by 6 points.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        tolerance, Double, Optional        
        The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(441, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"IsCurveClosable", None, object, tolerance)

    def is_curve_closed(self, object, index):
        """        
        Verifies an object is a closed curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(104, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsCurveClosed", None, object, index)

    def is_curve_in_plane(self, object, plane):
        """        
        Test a curve to see if it lies in a specific plane.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        plane, Array of ????, Optional        
        The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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

        boolean
        True if successful, otherwise False.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(483, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"IsCurveInPlane", None, object, flatten(plane))

    def is_curve_linear(self, object, index):
        """        
        Verifies an object is a linear curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(105, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsCurveLinear", None, object, index)

    def is_curve_periodic(self, object, index):
        """        
        Verifies an object is a periodic curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(106, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsCurvePeriodic", None, object, index)

    def is_curve_planar(self, object, index):
        """        
        Verifies an object is a planar curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(107, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsCurvePlanar", None, object, index)

    def is_curve_rational(self, object, index):
        """        
        Verifies an object is a rational NURBS curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(380, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsCurveRational", None, object, index)

    def is_ellipse(self, object):
        """        
        Verifies an object is an elliptical-shaped curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(523, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsEllipse", None, object)

    def is_line(self, object, index):
        """        
        Verifies an object is a line curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(108, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsLine", None, object, index)

    def is_point_on_curve(self, object, point, index):
        """        
        Verifies that a point is on a curve.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        point, Array of ????, Required        
        The test, or sampling, point.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(318, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)), u"IsPointOnCurve", None, object, flatten(point), index)

    def is_poly_curve(self, object, index):
        """        
        Verifies an object is a polycurve object.  A polycurve is a curve that is represented by a sequence of contiguous curve segments.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(368, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsPolyCurve", None, object, index)

    def is_polyline(self, object, index):
        """        
        Verifies an object is a polyline curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(110, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"IsPolyline", None, object, index)

    def join_curves(self, object, delete):
        """        
        Joins two or more curve object together to form one or more curves or polycurves.
    
        Parameters
        ==========

        object, String, Required        
        An array of strings identifying the curve objects to join.
            
        delete, Boolean, Optional        
        Delete input objects after joining.  The default is not to delete objects (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly created curve objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(111, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"JoinCurves", None, object, delete)

    def line_fit_from_points(self, object):
        """        
        Returns the starting and ending points of a line that was fit through an array of 3-D points.
    
        Parameters
        ==========

        object, String, Required        
        An array of 3-D points. The array must contain at least two 3-D points.
            
        Returns
        =======

        array
        An array containing the starting and ending points of the fit line if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(726, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"LineFitFromPoints", None, object)

    def make_curve_non_periodic(self, object, delete):
        """        
        Makes a periodic curve non-periodic.  Non-periodic curves can develop kinks when deformed.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        delete, Boolean, Optional        
        Delete input curve.  If omitted, the input curve will not be deleted (False).
            
        Returns
        =======

        string
        If blnDelete is False, the identifier of the new object if successful.

        string
        If blnDelete is True, the identifier of the modified object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(925, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"MakeCurveNonPeriodic", None, object, delete)

    def make_curve_periodic(self, object, delete):
        """        
        Makes an existing curve a periodic NURBS curve.  A periodic NURBS curve is a closed curve with a simple knot at the seam.  If a joined curve is made periodic, it becomes a single-span curve and can no longer be exploded.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        delete, Boolean, Optional        
        Delete input curve.  If omitted, the input curve will not be deleted (False).
            
        Returns
        =======

        string
        If blnDelete is False, the identifier of the new object if successful.

        string
        If blnDelete is True, the identifier of the modified object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(444, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"MakeCurvePeriodic", None, object, delete)

    def mesh_polyline(self, polyline):
        """        
        Creates a polygon mesh object based on a closed polyline curve object. The newly created polygon mesh object is added to the document.
    
        Parameters
        ==========

        polyline, String, Required        
        The identifier of the polyline curve object.
            
        Returns
        =======

        string
        The identifier of the new polygon mesh object if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(546, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"MeshPolyline", None, polyline)

    def offset_curve(self, object, direction, normal, style):
        """        
        Offsets a curve by a distance. The offset curve will be added to Rhino.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Array of ????, Required        
        The 3-D point that indicates the direction of the offset.
		dblDistance
            
        normal, Array of ????, Optional        
        A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
            
        style, Integer, Optional        
        The corner style.  Of omitted, a sharp corner style is used.
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

        array
        An array containing the identifiers of the new objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(634, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_I2, 1)), u"OffsetCurve", None, object, flatten(direction), flatten(normal), style)

    def offset_curve_on_surface(self, curve, surface):
        """        
        Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.
    
        Parameters
        ==========

        curve, String, Required        
        The curve object's identifier. Note, the curve must lie on the surface.
            
        surface, String, Required        
        The surface object's identifier.
		dblDistance
		Requried.  Number.  The distance of the offset.  Based on the curve's direction, a possitive value will offset to the left and a negative value will offset to the right.
		arrParameter
            
        Returns
        =======

        array
        An array containing the identifiers of the new curve objects if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(906, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"OffsetCurveOnSurface", None, curve, surface)

    def planar_closed_curve_containment(self, curve1, curve2, plane, tolerance):
        """        
        Determines the relationship between the regions bounded by two coplanar simple closed curves.
    
        Parameters
        ==========

        curve1, String, Required        
        The object identifier of the first planar, closed curve.
            
        curve2, String, Required        
        The object identifier of the second planar, closed curve.
            
        plane, Array of ????, Optional        
        The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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
            
        tolerance, Double, Optional        
        The tolerance.  If omitted, the current document absolute tolerance is used.
            
        Returns
        =======

        number
        A number identifying the relationship if successful.  The possible values are as follows:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(480, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)), u"PlanarClosedCurveContainment", None, curve1, curve2, flatten(plane), tolerance)

    def planar_curve_collision(self, curve1, curve2, plane, tolerance):
        """        
        Determines if two coplanar curves intersect.
    
        Parameters
        ==========

        curve1, String, Required        
        The object identifier of the first planar curve.
            
        curve2, String, Required        
        The object identifier of the second planar curve.
            
        plane, Array of ????, Optional        
        The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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
            
        tolerance, Double, Optional        
        The tolerance.  If omitted, the current document absolute tolerance is used.
            
        Returns
        =======

        null
        On error.

        """

        return self._ApplyTypes_(481, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)), u"PlanarCurveCollision", None, curve1, curve2, flatten(plane), tolerance)

    def point_in_planar_closed_curve(self, point, curve, plane, tolerance):
        """        
        Determines if a point is inside of a closed curve, on  a closed curve, or outside of a closed curve.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 3-D point to test.
            
        curve, String, Required        
        The object identifier of the planar, closed curve.
            
        plane, Array of ????, Optional        
        The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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
            
        tolerance, Double, Optional        
        The tolerance.  If omitted, the current document absolute tolerance is used.
            
        Returns
        =======

        number
        A number identifying the result if successful.  The possible values are as follows:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(482, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)), u"PointInPlanarClosedCurve", None, flatten(point), curve, flatten(plane), tolerance)

    def poly_curve_count(self, object, index):
        """        
        Returns the number of curve segments that make up a polycurve.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        number
        The number of curve segments in a polycurve if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(369, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"PolyCurveCount", None, object, index)

    def polyline_vertices(self, object, index):
        """        
        Returns the vertices of a polyline curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        index, Integer, Optional        
        If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
            
        Returns
        =======

        array
        An  array of 3-D vertex points if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(112, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"PolylineVertices", None, object, index)

    def project_curve_to_mesh(self, curve, curves, mesh, meshes, direction):
        """        
        Projects one or more points onto one or more meshes.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of a curve object to project.
            
        curves, Array of ????, Required        
        The identifiers of one or more curve objects to project.
            
        mesh, String, Required        
        The identifier of the mesh object to project onto.
            
        meshes, Array of ????, Required        
        The identifiers of the mesh objects to project onto.
            
        direction, Array of ????, Required        
        The direction (3-D vector) to project the points.
            
        Returns
        =======

        array
        The identifiers of the newly created, projected curve objects, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(911, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"ProjectCurveToMesh", None, curve, flatten(curves), mesh, flatten(meshes), flatten(direction))

    def project_curve_to_surface(self, curve, curves, surface, surfaces, direction):
        """        
        Projects one or more points onto one or more surfaces or polysurfaces.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of a curve object to project.
            
        curves, Array of ????, Required        
        The identifiers of one or more curve objects to project.
            
        surface, String, Required        
        The identifier of the surface or polysurface object to project onto.
            
        surfaces, Array of ????, Required        
        The identifiers of the surface or polysurface objects to project onto.
            
        direction, Array of ????, Required        
        The direction (3-D vector) to project the points.
            
        Returns
        =======

        array
        The identifiers of the newly created, projected curve objects, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(891, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"ProjectCurveToSurface", None, curve, flatten(curves), surface, flatten(surfaces), flatten(direction))

    def rebuild_curve(self, object, degree, point_count):
        """        
        Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        degree, Integer, Optional        
        The new degree, which must be greater than 1. The default is 3.
            
        point_count, Integer, Optional        
        The new point count, which must be bigger than the intDegree.  With closed curves, the minimum point count is 3.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(814, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1)), u"RebuildCurve", None, object, degree, point_count)

    def remove_curve_knot(self, object, parameter):
        """        
        Deletes a knot from a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the curve object.
            
        parameter, Double, Required        
        The parameter on the curve.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(916, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1)), u"RemoveCurveKnot", None, object, parameter)

    def reverse_curve(self, object):
        """        
        Reverses the direction of a curve object. This feature can also be found in Rhino's Dir command.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(542, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"ReverseCurve", None, object)

    def simplify_curve(self, object, flags):
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

        object, String, Required        
        The curve object's identifier.
            
        flags, Integer, Optional        
        The simplification methods to use. By default, all methods are used (intFlags = 0). The possible options are as follows:
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

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(573, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"SimplifyCurve", None, object, flags)

    def split_curve(self, object, parameter, parameters, delete):
        """        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Double, Required        
        The parameter, to split the curve at, that is in the interval returned by CurveDomain.
            
        parameters, Array of ????, Required        
        An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
            
        delete, Boolean, Optional        
        Delete the input curve. The default is to delete the input curve (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the two newly created curve objects, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(504, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"SplitCurve", None, object, parameter, flatten(parameters), delete)

    def trim_curve(self, object, interval, delete):
        """        
        Trims a curve by removing portions of the curve outside the specified interval.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        interval, Array of ????, Required        
        An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
            
        delete, Boolean, Optional        
        Delete the input curve. The default is to delete the input curve (True).
            
        Returns
        =======

        string
        The identifier of the newly created curve object, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(505, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"TrimCurve", None, object, flatten(interval), delete)

