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

        params = [plane, radius, angle]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [flatten(plane), radius, angle]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(651, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddArc", None, *params_flattened)

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

        params = [start, end, point]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(start), flatten(end), flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(82, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddArc3Pt", None, *params_flattened)

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

        params = [plane, radius]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(plane), radius]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(83, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddCircle", None, *params_flattened)

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

        params = [start, end, point]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(start), flatten(end), flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(84, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddCircle3Pt", None, *params_flattened)

    def add_curve(self, points, degree=None):
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

        params = [points, degree]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_I2, 1)]
        params_flattened = [flatten(points), degree]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(77, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddCurve", None, *params_flattened)

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

        params = [plane, x_radius, y_radius]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [flatten(plane), x_radius, y_radius]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(679, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddEllipse", None, *params_flattened)

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

        params = [center, second, third]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(center), flatten(second), flatten(third)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(680, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddEllipse3Pt", None, *params_flattened)

    def add_fillet_curve(self, curve0, curve1, radius=None, point0=None, point1=None):
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

        params = [curve0, curve1, radius, point0, point1]
        params_required = [True, True, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [curve0, curve1, radius, flatten(point0), flatten(point1)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(574, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddFilletCurve", None, *params_flattened)

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

        params = [object, points]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(points)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(513, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddInterpCrvOnSrf", None, *params_flattened)

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

        params = [object, points]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(points)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(641, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddInterpCrvOnSrfUV", None, *params_flattened)

    def add_interp_curve(self, points, degree=None, knot_style=None, start_tan=None, end_tan=None):
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

        params = [points, degree, knot_style, start_tan, end_tan]
        params_required = [True, False, False, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_I2, 1), (VT_I2, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(points), degree, knot_style, flatten(start_tan), flatten(end_tan)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(268, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddInterpCurve", None, *params_flattened)

    def add_interp_curve_ex(self, points, degree=None, knot_style=None, sharp=None, start_tangent=None, end_tangent=None):
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

        params = [points, degree, knot_style, sharp, start_tangent, end_tangent]
        params_required = [True, False, False, False, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(points), degree, knot_style, sharp, flatten(start_tangent), flatten(end_tangent)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(520, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddInterpCurveEx", None, *params_flattened)

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

        params = [start, end]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(start), flatten(end)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(70, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddLine", None, *params_flattened)

    def add_nurbs_curve(self, points, knots, degree, weights=None):
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

        params = [points, knots, degree, weights]
        params_required = [True, True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_I2, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(points), flatten(knots), degree, flatten(weights)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(309, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddNurbsCurve", None, *params_flattened)

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

        params = [points]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(points)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(85, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddPolyline", None, *params_flattened)

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

        params = [object, param0, param1]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [object, param0, param1]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(681, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSubCrv", None, *params_flattened)

    def arc_angle(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(86, 1, (VT_VARIANT, 0), params_magic_numbers, u"ArcAngle", None, *params_flattened)

    def arc_center_point(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(87, 1, (VT_VARIANT, 0), params_magic_numbers, u"ArcCenterPoint", None, *params_flattened)

    def arc_mid_point(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(88, 1, (VT_VARIANT, 0), params_magic_numbers, u"ArcMidPoint", None, *params_flattened)

    def arc_radius(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(89, 1, (VT_VARIANT, 0), params_magic_numbers, u"ArcRadius", None, *params_flattened)

    def circle_center_point(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(90, 1, (VT_VARIANT, 0), params_magic_numbers, u"CircleCenterPoint", None, *params_flattened)

    def circle_circumference(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(91, 1, (VT_VARIANT, 0), params_magic_numbers, u"CircleCircumference", None, *params_flattened)

    def circle_radius(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(92, 1, (VT_VARIANT, 0), params_magic_numbers, u"CircleRadius", None, *params_flattened)

    def close_curve(self, object, tolerance=None):
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

        params = [object, tolerance]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(440, 1, (VT_VARIANT, 0), params_magic_numbers, u"CloseCurve", None, *params_flattened)

    def convert_curve_to_polyline(self, object, angle_tolerance=None, tolerance=None, delete_input=None):
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

        params = [object, angle_tolerance, tolerance, delete_input]
        params_required = [True, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1)]
        params_flattened = [object, angle_tolerance, tolerance, delete_input]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(377, 1, (VT_VARIANT, 0), params_magic_numbers, u"ConvertCurveToPolyline", None, *params_flattened)

    def curve_arc_length_point(self, object, length, from_start=None):
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

        params = [object, length, from_start]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1)]
        params_flattened = [object, length, from_start]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(658, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveArcLengthPoint", None, *params_flattened)

    def curve_area(self, objects):
        """        
        Returns that area of closed planar curves. The results are based on the current drawing units.
    
        Parameters
        ==========

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

        params = [objects]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(objects)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(643, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveArea", None, *params_flattened)

    def curve_area_centroid(self, objects):
        """        
        Returns that area centroid of closed, planar curves. The results are based on the current drawing units.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of strings containing the identifiers of one or more closed, planar curve objects.
            
        Returns
        =======

        array
        An array of area centroid information if successful.  The array will contain the following information:

        null
        If not successful, or on error.

        """

        params = [objects]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(objects)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(677, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveAreaCentroid", None, *params_flattened)

    def curve_arrows(self, object, style=None):
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

        params = [object, style]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(578, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveArrows", None, *params_flattened)

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

        params = [curve_a, curve_b]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [curve_a, curve_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(811, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveBooleanDifference", None, *params_flattened)

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

        params = [curve_a, curve_b]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [curve_a, curve_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(810, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveBooleanIntersection", None, *params_flattened)

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

        params = [curves]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(curves)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(809, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveBooleanUnion", None, *params_flattened)

    def curve_brep_intersect(self, curve, brep, tolerance=None):
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

        params = [curve, brep, tolerance]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [curve, brep, tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(545, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveBrepIntersect", None, *params_flattened)

    def curve_closest_object(self, curve, objects):
        """        
        Returns the 3-D point locations on two objects where they are closest to each other.  Note, this function provides similar functionality to that of Rhino's ClosestPt command when used with the Object option.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the curve object to test.
            
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

        params = [curve, objects]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [curve, flatten(objects)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(870, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveClosestObject", None, *params_flattened)

    def curve_closest_point(self, object, point, index=None):
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

        params = [object, point, index]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)]
        params_flattened = [object, flatten(point), index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(93, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveClosestPoint", None, *params_flattened)

    def curve_contour_points(self, object, start_point, end_point, interval=None):
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

        params = [object, start_point, end_point, interval]
        params_required = [True, True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [object, flatten(start_point), flatten(end_point), interval]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(748, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveContourPoints", None, *params_flattened)

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

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, parameter]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(379, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveCurvature", None, *params_flattened)

    def curve_curve_intersection(self, object1, object2=None, tolerance=None):
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

        params = [object1, object2, tolerance]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object1, object2, tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(423, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveCurveIntersection", None, *params_flattened)

    def curve_degree(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(94, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveDegree", None, *params_flattened)

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

        params = [curve_a, curve_b]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [curve_a, curve_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(687, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveDeviation", None, *params_flattened)

    def curve_dim(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(381, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveDim", None, *params_flattened)

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

        params = [curve1, curve2]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [curve1, curve2]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(543, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveDirectionsMatch", None, *params_flattened)

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

        params = [object, style]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(579, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveDiscontinuity", None, *params_flattened)

    def curve_domain(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(95, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveDomain", None, *params_flattened)

    def curve_edit_points(self, object, return_parameters=None, index=None):
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

        params = [object, return_parameters, index]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1), (VT_I2, 1)]
        params_flattened = [object, return_parameters, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(442, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveEditPoints", None, *params_flattened)

    def curve_end_point(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(96, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveEndPoint", None, *params_flattened)

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

        params = [object, parameter, derivative]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1)]
        params_flattened = [object, parameter, derivative]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(489, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveEvaluate", None, *params_flattened)

    def curve_fillet_points(self, curve0, curve1, radius=None, base_point0=None, base_point1=None):
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

        params = [curve0, curve1, radius, base_point0, base_point1]
        params_required = [True, True, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [curve0, curve1, radius, flatten(base_point0), flatten(base_point1)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(572, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveFilletPoints", None, *params_flattened)

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

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, parameter]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(675, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveFrame", None, *params_flattened)

    def curve_knot_count(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(310, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveKnotCount", None, *params_flattened)

    def curve_knots(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(311, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveKnots", None, *params_flattened)

    def curve_length(self, object, index=None, sub_domain=None):
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

        params = [object, index, sub_domain]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_VARIANT, 1)]
        params_flattened = [object, index, flatten(sub_domain)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(97, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveLength", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(577, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveMidPoint", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(521, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveNormal", None, *params_flattened)

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

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, parameter]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(676, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurvePerpFrame", None, *params_flattened)

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

        params = [curve]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [curve]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(609, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurvePlane", None, *params_flattened)

    def curve_point_count(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(98, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurvePointCount", None, *params_flattened)

    def curve_points(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(308, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurvePoints", None, *params_flattened)

    def curve_radius(self, object, point, index=None):
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

        params = [object, point, index]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)]
        params_flattened = [object, flatten(point), index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(80, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveRadius", None, *params_flattened)

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

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, parameter]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(527, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveSeam", None, *params_flattened)

    def curve_start_point(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(99, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveStartPoint", None, *params_flattened)

    def curve_surface_intersection(self, curve, surface, tolerance=None, angle_tolerance=None):
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

        params = [curve, surface, tolerance, angle_tolerance]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [curve, surface, tolerance, angle_tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(424, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveSurfaceIntersection", None, *params_flattened)

    def curve_tangent(self, object, parameter, index=None):
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

        params = [object, parameter, index]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1)]
        params_flattened = [object, parameter, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(363, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveTangent", None, *params_flattened)

    def curve_weights(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(314, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurveWeights", None, *params_flattened)

    def divide_curve(self, object, segments, create=None, points=None):
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

        params = [object, segments, create, points]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I4, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [object, segments, create, points]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(78, 1, (VT_VARIANT, 0), params_magic_numbers, u"DivideCurve", None, *params_flattened)

    def divide_curve_equidistant(self, object, distance, create=None, points=None):
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

        params = [object, distance, create, points]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [object, distance, create, points]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(913, 1, (VT_VARIANT, 0), params_magic_numbers, u"DivideCurveEquidistant", None, *params_flattened)

    def divide_curve_length(self, object, length, create=None, points=None):
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

        params = [object, length, create, points]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [object, length, create, points]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(374, 1, (VT_VARIANT, 0), params_magic_numbers, u"DivideCurveLength", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(524, 1, (VT_VARIANT, 0), params_magic_numbers, u"EllipseCenterPoint", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(525, 1, (VT_VARIANT, 0), params_magic_numbers, u"EllipseQuadPoints", None, *params_flattened)

    def evaluate_curve(self, object, parameter, index=None):
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

        params = [object, parameter, index]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1)]
        params_flattened = [object, parameter, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(100, 1, (VT_VARIANT, 0), params_magic_numbers, u"EvaluateCurve", None, *params_flattened)

    def explode_curves(self, objects, delete=None):
        """        
        Explodes, or un-joins,  one more curve objects.  Polycurves will be exploded into curve segments.  Polylines will be exploded into line segments.  ExplodeCurves will return the curves in
		topological order.
    
        Parameters
        ==========

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

        params = [objects, delete]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(objects), delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(446, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExplodeCurves", None, *params_flattened)

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

        params = [object, type, side, objects]
        params_required = [True, True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_VARIANT, 1)]
        params_flattened = [object, type, side, flatten(objects)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(438, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtendCurve", None, *params_flattened)

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

        params = [object, type, side, length]
        params_required = [True, True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_R8, 1)]
        params_flattened = [object, type, side, length]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(436, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtendCurveLength", None, *params_flattened)

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

        params = [object, side, point]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_VARIANT, 1)]
        params_flattened = [object, side, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(437, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtendCurvePoint", None, *params_flattened)

    def fair_curve(self, object, tolerance=None):
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

        params = [object, tolerance]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(599, 1, (VT_VARIANT, 0), params_magic_numbers, u"FairCurve", None, *params_flattened)

    def fit_curve(self, object, degree=None, tolerance=None, angle_tolerance=None):
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

        params = [object, degree, tolerance, angle_tolerance]
        params_required = [True, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [object, degree, tolerance, angle_tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(813, 1, (VT_VARIANT, 0), params_magic_numbers, u"FitCurve", None, *params_flattened)

    def insert_curve_knot(self, object, parameter, symmetrical=None):
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

        params = [object, parameter, symmetrical]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1)]
        params_flattened = [object, parameter, symmetrical]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(515, 1, (VT_VARIANT, 0), params_magic_numbers, u"InsertCurveKnot", None, *params_flattened)

    def is_arc(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(101, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsArc", None, *params_flattened)

    def is_circle(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(102, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCircle", None, *params_flattened)

    def is_curve(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(103, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurve", None, *params_flattened)

    def is_curve_closable(self, object, tolerance=None):
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

        params = [object, tolerance]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(441, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurveClosable", None, *params_flattened)

    def is_curve_closed(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(104, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurveClosed", None, *params_flattened)

    def is_curve_in_plane(self, object, plane=None):
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

        params = [object, plane]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(483, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurveInPlane", None, *params_flattened)

    def is_curve_linear(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(105, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurveLinear", None, *params_flattened)

    def is_curve_periodic(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(106, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurvePeriodic", None, *params_flattened)

    def is_curve_planar(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(107, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurvePlanar", None, *params_flattened)

    def is_curve_rational(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(380, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCurveRational", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(523, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsEllipse", None, *params_flattened)

    def is_line(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(108, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLine", None, *params_flattened)

    def is_point_on_curve(self, object, point, index=None):
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

        params = [object, point, index]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)]
        params_flattened = [object, flatten(point), index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(318, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPointOnCurve", None, *params_flattened)

    def is_poly_curve(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(368, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPolyCurve", None, *params_flattened)

    def is_polyline(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(110, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPolyline", None, *params_flattened)

    def join_curves(self, object, delete=None):
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

        params = [object, delete]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(111, 1, (VT_VARIANT, 0), params_magic_numbers, u"JoinCurves", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(726, 1, (VT_VARIANT, 0), params_magic_numbers, u"LineFitFromPoints", None, *params_flattened)

    def make_curve_non_periodic(self, object, delete=None):
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

        params = [object, delete]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(925, 1, (VT_VARIANT, 0), params_magic_numbers, u"MakeCurveNonPeriodic", None, *params_flattened)

    def make_curve_periodic(self, object, delete=None):
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

        params = [object, delete]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(444, 1, (VT_VARIANT, 0), params_magic_numbers, u"MakeCurvePeriodic", None, *params_flattened)

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

        params = [polyline]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [polyline]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(546, 1, (VT_VARIANT, 0), params_magic_numbers, u"MeshPolyline", None, *params_flattened)

    def offset_curve(self, object, direction, distance, normal=None, style=None):
        """        
        Offsets a curve by a distance. The offset curve will be added to Rhino.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Array of ????, Required        
        The 3-D point that indicates the direction of the offset.
            
        distance, Double, Required        
        The distance of the offset.
            
        normal, Array of ????, Optional        
        A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
            
        style, Integer, Optional        
        The corner style.  If omitted, a sharp corner style is used.
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

        params = [object, direction, distance, normal, style]
        params_required = [True, True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_I2, 1)]
        params_flattened = [object, flatten(direction), distance, flatten(normal), style]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(634, 1, (VT_VARIANT, 0), params_magic_numbers, u"OffsetCurve", None, *params_flattened)

    def offset_curve_on_surface(self, curve, surface, distance, parameter):
        """        
        Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.
    
        Parameters
        ==========

        curve, String, Required        
        The curve object's identifier. Note, the curve must lie on the surface.
            
        surface, String, Required        
        The surface object's identifier.
            
        distance, Double, Required        
        The distance of the offset.  Based on the curve's direction, a possitive value will offset to the left and a negative value will offset to the right.
            
        parameter, Array of ????, Required        
        An array containing the surface U,V parameter that the curve will be offset through.
            
        Returns
        =======

        array
        An array containing the identifiers of the new curve objects if successful.

        null
        If not successful, or on error.

        """

        params = [curve, surface, distance, parameter]
        params_required = [True, True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_VARIANT, 1)]
        params_flattened = [curve, surface, distance, flatten(parameter)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(906, 1, (VT_VARIANT, 0), params_magic_numbers, u"OffsetCurveOnSurface", None, *params_flattened)

    def planar_closed_curve_containment(self, curve1, curve2, plane=None, tolerance=None):
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

        params = [curve1, curve2, plane, tolerance]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [curve1, curve2, flatten(plane), tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(480, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlanarClosedCurveContainment", None, *params_flattened)

    def planar_curve_collision(self, curve1, curve2, plane=None, tolerance=None):
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

        params = [curve1, curve2, plane, tolerance]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [curve1, curve2, flatten(plane), tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(481, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlanarCurveCollision", None, *params_flattened)

    def point_in_planar_closed_curve(self, point, curve, plane=None, tolerance=None):
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

        params = [point, curve, plane, tolerance]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(point), curve, flatten(plane), tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(482, 1, (VT_VARIANT, 0), params_magic_numbers, u"PointInPlanarClosedCurve", None, *params_flattened)

    def poly_curve_count(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(369, 1, (VT_VARIANT, 0), params_magic_numbers, u"PolyCurveCount", None, *params_flattened)

    def polyline_vertices(self, object, index=None):
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

        params = [object, index]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(112, 1, (VT_VARIANT, 0), params_magic_numbers, u"PolylineVertices", None, *params_flattened)

    def project_curve_to_mesh(self, curves, mesh, direction):
        """        
        Projects one or more points onto one or more meshes.
    
        Parameters
        ==========

        curves, Array of ????, Required        
        The identifiers of one or more curve objects to project.
            
        mesh, String, Required        
        The identifier of the mesh object to project onto.
            
        direction, Array of ????, Required        
        The direction (3-D vector) to project the points.
            
        Returns
        =======

        array
        The identifiers of the newly created, projected curve objects, if successful.

        null
        If not successful, or on error.

        """

        params = [curves, mesh, direction]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(curves), mesh, flatten(direction)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(911, 1, (VT_VARIANT, 0), params_magic_numbers, u"ProjectCurveToMesh", None, *params_flattened)

    def project_curve_to_surface(self, curves, surface, direction):
        """        
        Projects one or more points onto one or more surfaces or polysurfaces.
    
        Parameters
        ==========

        curves, Array of ????, Required        
        The identifiers of one or more curve objects to project.
            
        surface, String, Required        
        The identifier of the surface or polysurface object to project onto.
            
        direction, Array of ????, Required        
        The direction (3-D vector) to project the points.
            
        Returns
        =======

        array
        The identifiers of the newly created, projected curve objects, if successful.

        null
        If not successful, or on error.

        """

        params = [curves, surface, direction]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(curves), surface, flatten(direction)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(891, 1, (VT_VARIANT, 0), params_magic_numbers, u"ProjectCurveToSurface", None, *params_flattened)

    def rebuild_curve(self, object, degree=None, point_count=None):
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

        params = [object, degree, point_count]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1)]
        params_flattened = [object, degree, point_count]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(814, 1, (VT_VARIANT, 0), params_magic_numbers, u"RebuildCurve", None, *params_flattened)

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

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, parameter]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(916, 1, (VT_VARIANT, 0), params_magic_numbers, u"RemoveCurveKnot", None, *params_flattened)

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

        params = [object]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(542, 1, (VT_VARIANT, 0), params_magic_numbers, u"ReverseCurve", None, *params_flattened)

    def simplify_curve(self, object, flags=None):
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

        params = [object, flags]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, flags]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(573, 1, (VT_VARIANT, 0), params_magic_numbers, u"SimplifyCurve", None, *params_flattened)

    def split_curve(self, object, parameters, delete=None):
        """        
        Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
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

        params = [object, parameters, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [object, flatten(parameters), delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(504, 1, (VT_VARIANT, 0), params_magic_numbers, u"SplitCurve", None, *params_flattened)

    def trim_curve(self, object, interval, delete=None):
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

        params = [object, interval, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [object, flatten(interval), delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(505, 1, (VT_VARIANT, 0), params_magic_numbers, u"TrimCurve", None, *params_flattened)

