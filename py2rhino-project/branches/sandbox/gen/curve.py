# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Curve(DispatchBaseClass):



	def addarc(self, arrplane, dblradius, dblangle):
		"""

		Adds an arc curve to the document.

		Parameters

		arrPlane : Required,   Array,   The plane on which the arc will lie
		dblRadius : Required,   Number,   The radius arc
		dblAngle : Required,   Number,   A angle or interval, in degrees, of the arc

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddArc', None, arrPlane, dblRadius, dblAngle)

	def addcircle(self, arrplane, dblradius):
		"""

		Adds a circle curve to the document.

		Parameters

		arrPlane : Required,   Array,   The plane on which the circle will lie
		dblRadius : Required,   Number,   The radius of the circle

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddCircle', None, arrPlane, dblRadius)

	def addcircle3pt(self, arrstart, arrend, arrpoint):
		"""

		Adds a 3-point circle curve to the document.

		Parameters

		arrStart : Required,   Array,  The first point of the circle
		arrEnd : Required,   Array,   The second point of the circle
		arrPoint : Required,   Array,   The third point of the circle

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddCircle3Pt', None, arrStart, arrEnd, arrPoint)

	def addcurve(self, arrpoints, intdegree):
		"""

		Adds a control points curve object to the document.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points
		intDegree : Optional,   Number,   The degree of the curve

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddCurve', None, arrPoints, intDegree)

	def addellipse(self, arrplane, dblxradius, dblyradius):
		"""

		Adds an elliptical curve to the document.

		Parameters

		arrPlane : Required,   Array,   The plane on which the ellipse will lie
		dblXRadius : Required,   Number,   The radius in the X-axis direction
		dblYRadius : Required,   Number,   The radius in the Y-axis direction

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddEllipse', None, arrPlane, dblXRadius, dblYRadius)

	def addellipse3pt(self, arrcenter, arrsecond, arrthird):
		"""

		Adds a 3 point elliptical curve to the document.

		Parameters

		arrCenter : Required,   Array,   The center point of the ellipse
		arrSecond : Required,   Array,   The end point of the X-axis
		arrThird : Required,   Array,   The end point of the Y-axis

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddEllipse3Pt', None, arrCenter, arrSecond, arrThird)

	def addfilletcurve(self, strcurve0, strcurve1, dblradius, arrpoint0, arrpoint1):
		"""

		Adds a fillet curve between two curve objects.

		Parameters

		strCurve0 : Required,   String,   The identifier of the first curve object
		strCurve1 : Required,   String,   The identifier of the second curve object
		dblRadius : Optional,  Number,  The fillet radius
		arrPoint0 : Optional,  Array,  The base point on the first curve
		arrPoint1 : Optional,  Array,  The base point on the second curve

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddFilletCurve', None, strCurve0, strCurve1, dblRadius, arrPoint0, arrPoint1)

	def addinterpcrvonsrf(self, strobject, arrpoints):
		"""

		Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

		Parameters

		strObject : Required,   String,   The surface object's identifier
		arrPoints : Required,   Array,   An array of 3-D points that lie on the specified surface

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCrvOnSrf', None, strObject, arrPoints)

	def addinterpcrvonsrfuv(self, strobject, arrpoints):
		"""

		Adds an interpolated curve object. based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.

		Parameters

		strObject : Required,   String,   The surface object's identifier
		arrPoints : Required,   Array,   An array of 2-D surface parameters

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCrvOnSrfUV', None, strObject, arrPoints)

	def addinterpcurve(self, arrpoints, intdegree, intknotstyle, arrstarttan, arrendtan):
		"""

		Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.

		Parameters

		arrPoints : Required,   Array,   An array containing 3-D points to interpolate
		intDegree : Optional,   Number,   The degree of the curve
		intKnotStyle : Optional,   Number,  The knot style to use, and whether the curve should be periodic
		arrStartTan : Optional,   Array,   A 3-D vector that specifies a tangency condition at the beginning of the curve
		arrEndTan : Optional,   Array,   A 3-D vector that specifies a tangency condition at the end of the curve

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCurve', None, arrPoints, intDegree, intKnotStyle, arrStartTan, arrEndTan)

	def addinterpcurveex(self, arrpoints, intdegree, intknotstyle, blnsharp, arrstarttangent, arrendtangent):
		"""

		Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.

		Parameters

		arrPoints : Required,   Array,   An array containing 3-D points to interpolate
		intDegree : Optional,   Number,   The degree of the curve
		intKnotStyle : Optional,   Number,  The knot style to use
		blnSharp : Optional,   Boolean,   If True, when you create a closed curve, it will have a kink at the start/end point
		arrStartTangent : Optional,   Array,   A 3-D vector that specifies a tangency condition at the beginning of the curve
		arrEndTangent : Optional,   Array,   A 3-D vector that specifies a tangency condition at the end of the curve

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddInterpCurveEx', None, arrPoints, intDegree, intKnotStyle, blnSharp, arrStartTangent, arrEndTangent)

	def addline(self, arrstart, arrend):
		"""

		Adds a line curve to the current model.

		Parameters

		arrStart : Required,   Array,   The starting point of the line
		arrEnd : Required,   Array,   The ending point of the line

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddLine', None, arrStart, arrEnd)

	def addnurbscurve(self, arrpoints, arrknots, intdegree, arrweights):
		"""

		Adds a NURBS curve object to the document.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D control points
		arrKnots : Required,   Array,   The knot values for the curve
		intDegree : Required,   Number,   The degree of the curve
		arrWeights : Optional,   Array,   The weight values for the curve

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddNurbsCurve', None, arrPoints, arrKnots, intDegree, arrWeights)

	def addpolyline(self, arrpoints):
		"""

		Adds a polyline curve object to the current model.

		Parameters

		arrPoints : Required,   Array,    An array of 3-D points

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddPolyline', None, arrPoints)

	def addsubcrv(self, strobject, dblparam0, dblparam1):
		"""

		Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.

		Parameters

		strObject : Required,   String,   The identifier of a closed, planar curve object
		dblParam0 : Required,   Number,   The first parameter on the source curve
		dblParam1 : Required,   Number,   The second parameter on the source curve

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddSubCrv', None, strObject, dblParam0, dblParam1)

	def arcangle(self, strobject, intindex):
		"""

		Returns the angle of an arc curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The angle in degrees if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ArcAngle', None, strObject, intIndex)

	def arccenterpoint(self, strobject, intindex):
		"""

		Returns the center point of an arc curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ArcCenterPoint', None, strObject, intIndex)

	def arcmidpoint(self, strobject, intindex):
		"""

		Returns the mid point of an arc curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ArcMidPoint', None, strObject, intIndex)

	def arcradius(self, strobject, intindex):
		"""

		Returns the radius of an arc curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The radius of the arc if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ArcRadius', None, strObject, intIndex)

	def circlecenterpoint(self, strobject, intindex):
		"""

		Returns the center point of a circle curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : The 3-D center point of the circle if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CircleCenterPoint', None, strObject, intIndex)

	def circlecircumference(self, strobject, intindex):
		"""

		Returns the circumference of a circle curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The circumference of the circle if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CircleCircumference', None, strObject, intIndex)

	def circleradius(self, strobject, intindex):
		"""

		Returns the radius of a circle curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The radius of the circle if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CircleRadius', None, strObject, intIndex)

	def closecurve(self, strobject, dbltolerance):
		"""

		Closes an open curve object by making adjustments to the end points so that they meet at a point.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblTolerance : Optional,  Number,   The maximum allowable distance between start point and end point of the curve

		Returns

		String : The identifier of the closed curve object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CloseCurve', None, strObject, dblTolerance)

	def convertcurvetopolyline(self, strobject, dblangletolerance, dbltolerance, blndeleteinput):
		"""

		Converts a curve to a polyline curve.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblAngleTolerance : Optional,   Number,   The maximum angle between curve tangents at line endpoints
		dblTolerance : Optional,   Number,   The distance tolerance at segment midpoints
		blnDeleteInput : Optional,   Boolean,   Delete the curve object specified by strObject

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ConvertCurveToPolyline', None, strObject, dblAngleTolerance, dblTolerance, blnDeleteInput)

	def curvearclengthpoint(self, strobject, dbllength, blnfromstart):
		"""

		Returns the point on the curve that is a specified arc length from the start of the curve.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblLength : Required,   Number,  The arc length from the start of the curve to evaluate
		blnFromStart : Optional,   Boolean,   If not specified or True, then the arc length point is calculated from the start of the curve

		Returns

		Array : The 3-D point if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveArcLengthPoint', None, strObject, dblLength, blnFromStart)

	def curvearea(self, strobject, arrobjects):
		"""

		Returns that area of closed planar curves. The results are based on the current drawing units.

		Parameters

		strObject : Required,   String,   The identifier of a closed, planar curve object
		arrObjects : Required,   Array,   An array of strings containing the identifiers of one or more closed, planar curve objects

		Returns

		Array : An array of area information if successful.  The array will contain the following information:
		Number : The area. If more than one curve was specified, the value will be the cumulative area.
		Number : The absolute (+/-) error bound for the area.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveArea', None, strObject, arrObjects)

	def curveareacentroid(self, strobject, arrobjects):
		"""

		Returns that area centroid of closed, planar curves. The results are based on the current drawing units.

		Parameters

		strObject : Required,   String,   The identifier of a closed, planar curve object
		arrObjects : Required,   Array,   An array of strings containing the identifiers of one or more closed, planar curve objects

		Returns

		Array : An array of area centroid information if successful.  The array will contain the following information:
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveAreaCentroid', None, strObject, arrObjects)

	def curvearrows(self, strobject, intstyle):
		"""

		Enables or disabled a curve object's annotation arrows.

		Parameters

		strObject : Required,   String,   The object's identifier
		intStyle : Optional,   Number,   The style of annotation arrows to be displayed

		Returns

		Number : If intStyle is not specified, the current annotation arrow style if successful.
		Number : If intStyle is specified, the previous annotation arrow style if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveArrows', None, strObject, intStyle)

	def curvebooleandifference(self, strcurvea, strcurveb):
		"""

		Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

		Parameters

		strCurveA : Required,   String,   The identifier of the first curve object
		strCurveB : Required,   String,   The identifier of the second curve object

		Returns

		Array : The identifiers of the new objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBooleanDifference', None, strCurveA, strCurveB)

	def curvebooleanintersection(self, strcurvea, strcurveb):
		"""

		Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.

		Parameters

		strCurveA : Required,   String,   The identifier of the first curve object
		strCurveB : Required,   String,   The identifier of the second curve object

		Returns

		Array : The identifiers of the new objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBooleanIntersection', None, strCurveA, strCurveB)

	def curvebooleanunion(self, arrcurves):
		"""

		Calculates the union of two or more closed, planar curves and adds the results to the document. Note, curves must be coplanar.

		Parameters

		arrCurves : Required,   Array,   The identifiers of two or more curve objects

		Returns

		Array : The identifiers of the new objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBooleanUnion', None, arrCurves)

	def curvebrepintersect(self, strcurve, strbrep, dbltolerance):
		"""

		Intersects a curve object with a brep object. Note, unlike the CurveSurfaceIntersection function, this function works on trimmed surfaces.

		Parameters

		strCurve : Required,   String,   The curve object's identifier
		strBrep : Required,   String,   The brep object's identifier
		dblTolerance : Optional,   Number,   The distance tolerance at segment midpoints

		Returns

		Array : An array of strings identifying the newly created intersection curve and point objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveBrepIntersect', None, strCurve, strBrep, dblTolerance)

	def curveclosestobject(self, strcurve, strobject, arrobjects):
		"""

		Returns the 3-D point locations on two objects where they are closest to each other.  Note, this function provides similar functionality to that of Rhino's ClosestPt command when used with the Object option.

		Parameters

		strCurve : Required,   String,   The identifier of the curve object to test
		strObject : Required,   String,   The identifier of a point cloud, curve, surface, or polysurface to test against
		arrObjects : Required,   Array,   The identifiers of one or more point cloud, curve, surface, or polysurface to test against

		Returns

		Array : An array containing the results of the closest point calculation if successful.  The elements of the array are as follows:
		String : The identifier of the closest object.
		Array : The 3-D point that is closest to the closest object.
		Array : The 3-D point that is closest to the test curve.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveClosestObject', None, strCurve, strObject, arrObjects)

	def curveclosestpoint(self, strobject, arrpoint, intindex):
		"""

		Returns the parameter of the point on a curve that is closest to a test point.

		Parameters

		strObject : Required,  String,  The object's identifier
		arrPoint : Required,   Array,   The test, or sampling, point
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The parameter of the closest point on the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveClosestPoint', None, strObject, arrPoint, intIndex)

	def curvecontourpoints(self, strobject, arrstartpoint, arrendpoint, dblinterval):
		"""

		Returns the 3-D point locations calculated by contouring a curve object.

		Parameters

		strObject : Required,   String,   The identifier of a curve object
		arrStartPoint : Required,   Array,   The 3-D starting point of a center line
		arrEndPoint : Required,   Array,   The 3-D ending point of a center line
		dblInterval : Optional,   Number,   The distance between contour curves

		Returns

		Array : An array of 3-D points, one for each contour, if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveContourPoints', None, strObject, arrStartPoint, arrEndPoint, dblInterval)

	def curvecurvature(self, strobject, dblparameter):
		"""

		Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblParameter : Required,   Number,   The parameter to evaluate

		Returns

		Array : An array of curvature information if successful.  The array will contain the following information:
		Number : Radius of curvature
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveCurvature', None, strObject, dblParameter)

	def curvecurveintersection(self, strobject1, strobject2, dbltolerance):
		"""

		Calculates the intersection of two curve objects.

		Parameters

		strObject1 : Required,   String,   The identifier of the first curve object
		strObject2 : Optional,   String,   The identifier of the second curve object
		dblTolerance : Optional,   Number,   The absolute tolerance in drawing units

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

	def curvedegree(self, strobject, intindex):
		"""

		Returns the degree of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The degree of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDegree', None, strObject, intIndex)

	def curvedeviation(self, strcurvea, strcurveb):
		"""

		Returns the minimum and maximum deviation between two curve objects. For more information on curve deviation, see the Rhino help file for the CrvDeviation command.

		Parameters

		strCurveA : Required,   String,   The identifier of the first curve object
		strCurveB : Required,   String,   The identifier of the second curve object

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

	def curvedim(self, strobject, intindex):
		"""

		Returns the dimension of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The dimension of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDim', None, strObject, intIndex)

	def curvedirectionsmatch(self, strcurve1, strcurve2):
		"""

		Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.

		Parameters

		strCurve1 : Required,  String,  The identifier of the first curve to compare
		strCurve2 : Required,  String,  The identifier of the second curve to compare

		Returns

		Boolean : True if the curve directions match, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDirectionsMatch', None, strCurve1, strCurve2)

	def curvediscontinuity(self, strobject, intstyle):
		"""

		Search for a derivatitive, tangent, or curvature discontinuity in a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intStyle : Required,   Number,   The type of continuity to test for

		Returns

		Array : An array of 3-D points where the curve is discontinuous if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDiscontinuity', None, strObject, intStyle)

	def curvedomain(self, strobject, intindex):
		"""

		Returns the domain of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : The domain of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveDomain', None, strObject, intIndex)

	def curveeditpoints(self, strobject, blnreturnparameters, intindex):
		"""

		Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.

		Parameters

		strObject : Required,   String,   The object's identifier
		blnReturnParameters : Optional,   Boolean,   Return the edit points as an array of parameter values
		intIndex : Optional,  Number,   If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.
		Array : If blnReturnParameters is True, then an array of parameter values if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveEditPoints', None, strObject, blnReturnParameters, intIndex)

	def curveendpoint(self, strobject, intindex):
		"""

		Returns the end point of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : The 3-D end point of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveEndPoint', None, strObject, intIndex)

	def curveevaluate(self, strobject, dblparameter, intderivative):
		"""

		A general purpose curve evaluator.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblParameter : Required,   Number,   The evaluation parameter
		intDerivative : Required,   Number,   The number of derivatives to evaluate

		Returns

		Array : An array of length (intDerivative+1) if successful.  The array elements are as follows:
		Array : The 3-D point
		Array : The first derivative
		Array : The second derivative
		Array : etc...
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveEvaluate', None, strObject, dblParameter, intDerivative)

	def curvefilletpoints(self, strcurve0, strcurve1, dblradius, arrbasepoint0, arrbasepoint1):
		"""

		Of all possible fillet points, this function returns the one which is the closest to the base point arrBasePoint0, arrBasePoint1.  Distance from the base point is measured by the sum of arc lengths along the two curves.

		Parameters

		strCurve0 : Required,   String,   The identifier of the first curve object
		strCurve1 : Required,   String,   The identifier of the second curve object
		dblRadius : Optional,  Number,  The fillet radius
		arrBasePoint0 : Optional,  Array,  The base point on the first curve
		arrBasePoint1 : Optional,  Array,  The base point on the second curve

		Returns

		Array : If blnPoints is True, then an array of point and vector values if successful.  The array elements are as follows:
		String : If blnPoints is False, then the identifier of the fillet curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveFilletPoints', None, strCurve0, strCurve1, dblRadius, arrBasePoint0, arrBasePoint1)

	def curveframe(self, strobject, dblparameter):
		"""

		Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblParameter : Required,   Number,  The parameter to evaluate

		Returns

		Array : The plane at the specified parameter if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveFrame', None, strObject, dblParameter)

	def curveknotcount(self, strobject, intindex):
		"""

		Returns the knot count of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The number of knots if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveKnotCount', None, strObject, intIndex)

	def curveknots(self, strobject, intindex):
		"""

		Returns the knots, or knot vector, of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : The knot values of the curve  if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveKnots', None, strObject, intIndex)

	def curvelength(self, strobject, intindex, arrsubdomain):
		"""

		Returns the length of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,   Number,   If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query
		arrSubDomain : Optional,   Array,   An array of two numbers identifying the sub-domain of the curve on which the calculation will be performed

		Returns

		Number : The length of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveLength', None, strObject, intIndex, arrSubDomain)

	def curvemidpoint(self, strobject):
		"""

		Returns the mid point of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Array : The 3-D mid point of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveMidPoint', None, strObject)

	def curvenormal(self, strobject):
		"""

		Returns the normal direction of the plane in which a planar curve object lies.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Array : The 3-D normal vector if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveNormal', None, strObject)

	def curveperpframe(self, strobject, dblparameter):
		"""

		Returns the perpendicular plane at a parameter of a curve.  The result is relatively parallel (zero-twisting) plane.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblParameter : Required,   Number,  The parameter to evaluate

		Returns

		Array : The plane at the specified parameter if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePerpFrame', None, strObject, dblParameter)

	def curveplane(self, strcurve):
		"""

		Returns the plane in which a planar curve lies. Note, this function works only on planar curves.

		Parameters

		strCurve : Required,   String,   The identifier of a planar curve object

		Returns

		Array : The plane in which the curve lies if successful.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePlane', None, strCurve)

	def curvepointcount(self, strobject, intindex):
		"""

		Returns the control points count of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The number of control points if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePointCount', None, strObject, intIndex)

	def curvepoints(self, strobject, intindex):
		"""

		Returns the control points, or control vertices, of a curve object.  If the curve is a rational NURBS curve, the euclidean control vertices are returned.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,   If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : The control points of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurvePoints', None, strObject, intIndex)

	def curveradius(self, strobject, arrpoint, intindex):
		"""

		Returns the radius of curvature at a point on a curve.

		Parameters

		strObject : Required,  String,  The object's identifier
		arrPoint : Required,   Array,   The test, or sampling, point
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The radius of curvature at the point on the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveRadius', None, strObject, arrPoint, intIndex)

	def curveseam(self, strobject, dblparameter):
		"""

		Adjusts the seam, or start/end, point of a closed curve.

		Parameters

		strObject : Required,  String,  The object's identifier
		dblParameter : Required,   Number,   The parameter of the new start/end point

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveSeam', None, strObject, dblParameter)

	def curvestartpoint(self, strobject, intindex):
		"""

		Returns the start point of a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : The 3-D starting point of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveStartPoint', None, strObject, intIndex)

	def curvesurfaceintersection(self, strcurve, strsurface, dbltolerance, dblangletolerance):
		"""

		Calculates the intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.

		Parameters

		strCurve : Required,   String,   The identifier of a curve object
		strSurface : Required,   String,   The identifier of a surface object
		dblTolerance : Optional,   Number,   The absolute tolerance in drawing units
		dblAngleTolerance : Optional,   Number,   The angle tolerance in degrees

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

	def curvetangent(self, strobject, dblparameter, intindex):
		"""

		Returns a 3-D vector that is the tangent to a curve at a parameter.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblParameter : Required,   Number,   The parameter to evaluate
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : A  3-D vector if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveTangent', None, strObject, dblParameter, intIndex)

	def curveweights(self, strobject, intindex):
		"""

		Returns an array of weight values that are assigned to the control points of a curve.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : The weight values of the curve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CurveWeights', None, strObject, intIndex)

	def curve_addarc3pt(self, arrstart, arrend, arrpoint):
		"""

		Adds a 3-point arc curve to the document.

		Parameters

		arrStart : Required,   Array,   The starting point of the arc
		arrEnd : Required,   Array,   The ending point of the arc
		arrPoint : Required,   Array,   A point on the arc

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'Curve_AddArc3Pt', None, arrStart, arrEnd, arrPoint)

	def dividecurve(self, strobject, lngsegments, blncreate, blnpoints):
		"""

		Divides a curve object into a specified number of segments.

		Parameters

		strObject : Required,  String,  The object's identifier
		lngSegments : Required,  Number,  The number of segments
		blnCreate : Optional,  Boolean,  Create the division points
		blnPoints : Optional,  Boolean,  Return an array of 3-D points

		Returns

		Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
		Array : If blnPoints is False, then an array containing division curve parameters if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DivideCurve', None, strObject, lngSegments, blnCreate, blnPoints)

	def dividecurveequidistant(self, strobject, dbldistance, blncreate, blnpoints):
		"""

		Unlike the DivideCurve and DivideCurveLength, which divides a curve based on arc length, or the distance along the curve between two points, this function divides a curve based on the linear distance between points.

		Parameters

		strObject : Required,  String,  The object's identifier
		dblDistance : Required,  Number,  The linear distance between division points
		blnCreate : Optional,  Boolean,  Create the division points
		blnPoints : Optional,  Boolean,  Return an array of 3-D points

		Returns

		Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
		Array : If blnPoints is False, then an array containing division curve parameters if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DivideCurveEquidistant', None, strObject, dblDistance, blnCreate, blnPoints)

	def dividecurvelength(self, strobject, dbllength, blncreate, blnpoints):
		"""

		Divides a curve object into segments of a specified length.

		Parameters

		strObject : Required,  String,  The object's identifier
		dblLength : Required,  Number,  The length of each segment
		blnCreate : Optional,  Boolean,  Create the division points
		blnPoints : Optional,  Boolean,  Return an array of 3-D points

		Returns

		Array : If blnPoints is not specified or True, then an array containing 3-D division points if successful.
		Array : If blnPoints is False, then an array containing division curve parameters if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DivideCurveLength', None, strObject, dblLength, blnCreate, blnPoints)

	def ellipsecenterpoint(self, strobject):
		"""

		Returns the center point of an elliptical-shaped curve object.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Array : The 3-D center point of the ellipse if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'EllipseCenterPoint', None, strObject)

	def ellipsequadpoints(self, strobject):
		"""

		Returns the quadrant points of an elliptical-shaped curve object.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Array : An array of 3-D points identifying the quadrants of the ellipse if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'EllipseQuadPoints', None, strObject)

	def evaluatecurve(self, strobject, dblparameter, intindex):
		"""

		Evaluates a curve at a parameter.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblParameter : Required,   Number,   The parameter to evaluate
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : A 3-D point if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'EvaluateCurve', None, strObject, dblParameter, intIndex)

	def explodecurves(self, strobject, arrobjects, blndelete):
		"""

		topological order.

		Parameters

		strObject : Required,   String,   The identifier of the curve object to explode
		arrObjects : Required,   Array,    An array of strings identifying the curve objects to explode
		blnDelete : Optional,   Boolean,   Delete input objects after exploding

		Returns

		Array : An array of strings identifying the newly created curve objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ExplodeCurves', None, strObject, arrObjects, blnDelete)

	def extendcurve(self, strobject, inttype, intside, arrobjects):
		"""

		Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

		Parameters

		strObject : Required,   String,   The object's identifier
		intType : Required,   Number,   Type of extension
		intSide : Required,   Number,   The size to  extent
		arrObjects : Required,   Array,   The identifiers of curve, surface, and polysurface objects that will be used as boundary objects

		Returns

		String : The identifier of the extended object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ExtendCurve', None, strObject, intType, intSide, arrObjects)

	def extendcurvelength(self, strobject, inttype, intside, dbllength):
		"""

		Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

		Parameters

		strObject : Required,   String,   The object's identifier
		intType : Required,   Number,   Type of extension
		intSide : Required,   Number,   The size to  extent
		dblLength : Required,   Number,   The distance to extend the curve

		Returns

		String : The identifier of the extended object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ExtendCurveLength', None, strObject, intType, intSide, dblLength)

	def extendcurvepoint(self, strobject, intside, arrpoint):
		"""

		Extends a non-closed curve object by smooth extension to a point.

		Parameters

		strObject : Required,   String,   The object's identifier
		intSide : Required,   Number,   The size to  extent
		arrPoint : Required,   Array,   The 3-D point

		Returns

		String : The identifier of the extended object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ExtendCurvePoint', None, strObject, intSide, arrPoint)

	def faircurve(self, strobject, dbltolerance):
		"""

		Fairs a curve object. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvature variations while limiting the geometry changes to be no more than the specified tolerance. Sometimes several applications of this method are necessary to remove nasty curvature problems.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblTolerance : Optional,   Number,   The fairing tolerance

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'FairCurve', None, strObject, dblTolerance)

	def fitcurve(self, strobject, intdegree, dbltolerance, dblangletolerance):
		"""

		Reduces the number of curve control points while maintaining the curve's same general shape.  Use this function for replacing curves with too many control points.  For more information, see the Rhino help file for the FitCrv command.

		Parameters

		strObject : Required,   String,   The object's identifier
		intDegree : Optional,   Number,   The curve degree, which must be greater than 1
		dblTolerance : Optional,   Number,   The fitting tolerance
		dblAngleTolerance : Optional,   Number,   The kink smoothing tolerance in degrees

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'FitCurve', None, strObject, intDegree, dblTolerance, dblAngleTolerance)

	def insertcurveknot(self, strobject, dblparameter, blnsymmetrical):
		"""

		Inserts a knot into a curve object.

		Parameters

		strObject : Required,   String,   The identifier of the curve object
		dblParameter : Required,   Number,   The parameter on the curve
		blnSymmetrical : Optional,   Boolean,   If blnSymmetrical = True, then knots are added on both sides of the center of the curve

		Returns

		Boolean : True of False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'InsertCurveKnot', None, strObject, dblParameter, blnSymmetrical)

	def isarc(self, strobject, intindex):
		"""

		Verifies an object is an arc curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsArc', None, strObject, intIndex)

	def iscircle(self, strobject, intindex):
		"""

		Verifies an object is a circle curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCircle', None, strObject, intIndex)

	def iscurve(self, strobject, intindex):
		"""

		Verifies an object is a curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurve', None, strObject, intIndex)

	def iscurveclosable(self, strobject, dbltolerance):
		"""

		Decide if it makes sense to close off the curve by moving  the endpoint to the start based on start-end gap size and length of curve as approximated by chord defined by 6 points.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblTolerance : Optional,  Number,   The maximum allowable distance between start point and end point of the curve

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveClosable', None, strObject, dblTolerance)

	def iscurveclosed(self, strobject, intindex):
		"""

		Verifies an object is a closed curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveClosed', None, strObject, intIndex)

	def iscurveinplane(self, strobject, arrplane, array, array, array, array):
		"""

		Test a curve to see if it lies in a specific plane.

		Parameters

		strObject : Required,   String,   The object's identifier
		arrPlane : Optional,   Array,  The new construction plane
		Array : Required,   The construction plane's origin (3-D point), 
		Array : Required,   The construction plane's X axis direction (3-D vector), 
		Array : Required,   The construction plane's Y axis direction (3-D vector), 
		Array : Optional,   The construction plane's Z axis direction (3-D vector), 

		Returns

		Boolean : True if successful, otherwise False.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveInPlane', None, strObject, arrPlane, Array, Array, Array, Array)

	def iscurvelinear(self, strobject, intindex):
		"""

		Verifies an object is a linear curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveLinear', None, strObject, intIndex)

	def iscurveperiodic(self, strobject, intindex):
		"""

		Verifies an object is a periodic curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurvePeriodic', None, strObject, intIndex)

	def iscurveplanar(self, strobject, intindex):
		"""

		Verifies an object is a planar curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurvePlanar', None, strObject, intIndex)

	def iscurverational(self, strobject, intindex):
		"""

		Verifies an object is a rational NURBS curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsCurveRational', None, strObject, intIndex)

	def isellipse(self, strobject):
		"""

		Verifies an object is an elliptical-shaped curve object.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsEllipse', None, strObject)

	def isline(self, strobject, intindex):
		"""

		Verifies an object is a line curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsLine', None, strObject, intIndex)

	def ispointoncurve(self, strobject, arrpoint, arrpoint):
		"""

		Verifies that a point is on a curve.

		Parameters

		strObject : Required,  String,  The object's identifier
		arrPoint : Required,   Array,   The test, or sampling, point
		arrPoint : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsPointOnCurve', None, strObject, arrPoint, arrPoint)

	def ispolycurve(self, strobject, intindex):
		"""

		Verifies an object is a polycurve object.  A polycurve is a curve that is represented by a sequence of contiguous curve segments.

		Parameters

		strObject : Required,  String,  The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsPolyCurve', None, strObject, intIndex)

	def ispolyline(self, strobject, intindex):
		"""

		Verifies an object is a polyline curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsPolyline', None, strObject, intIndex)

	def joincurves(self, strobject, blndelete):
		"""

		Joins two or more curve object together to form one or more curves or polycurves.

		Parameters

		strObject : Required,   Array,   An array of strings identifying the curve objects to join
		blnDelete : Optional,   Boolean,   Delete input objects after joining

		Returns

		Array : An array of strings identifying the newly created curve objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'JoinCurves', None, strObject, blnDelete)

	def linefitfrompoints(self, strobject):
		"""

		Returns the starting and ending points of a line that was fit through an array of 3-D points.

		Parameters

		strObject : Required,   Array,   An array of 3-D points

		Returns

		Array : An array containing the starting and ending points of the fit line if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'LineFitFromPoints', None, strObject)

	def makecurvenonperiodic(self, strobject, blndelete):
		"""

		Makes a periodic curve non-periodic.  Non-periodic curves can develop kinks when deformed.

		Parameters

		strObject : Required,   String,   The object's identifier
		blnDelete : Optional,   Boolean,   Delete input curve

		Returns

		String : If blnDelete is False, the identifier of the new object if successful.
		String : If blnDelete is True, the identifier of the modified object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'MakeCurveNonPeriodic', None, strObject, blnDelete)

	def makecurveperiodic(self, strobject, blndelete):
		"""

		Makes an existing curve a periodic NURBS curve.  A periodic NURBS curve is a closed curve with a simple knot at the seam.  If a joined curve is made periodic, it becomes a single-span curve and can no longer be exploded.

		Parameters

		strObject : Required,   String,   The object's identifier
		blnDelete : Optional,   Boolean,   Delete input curve

		Returns

		String : If blnDelete is False, the identifier of the new object if successful.
		String : If blnDelete is True, the identifier of the modified object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'MakeCurvePeriodic', None, strObject, blnDelete)

	def meshpolyline(self, strpolyline):
		"""

		Creates a polygon mesh object based on a closed polyline curve object. The newly created polygon mesh object is added to the document.

		Parameters

		strPolyline : Required,   String,   The identifier of the polyline curve object

		Returns

		String : The identifier of the new polygon mesh object if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'MeshPolyline', None, strPolyline)

	def offsetcurve(self, strobject, arrdirection, arrnormal, intstyle):
		"""

		Offsets a curve by a distance. The offset curve will be added to Rhino.

		Parameters

		strObject : Required,   String,   The object's identifier
		arrDirection : Required,   Array,   The 3-D point that indicates the direction of the offset
		arrNormal : Optional,   Array,   A 3-D vector identifying the normal of the plane in which the offset will occur
		intStyle : Optional,   Number,   The corner style

		Returns

		Array : An array containing the identifiers of the new objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'OffsetCurve', None, strObject, arrDirection, arrNormal, intStyle)

	def offsetcurveonsurface(self, strcurve, strsurface):
		"""

		Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.

		Parameters

		strCurve : Required,   String,   The curve object's identifier
		strSurface : Required,   String,   The surface object's identifier

		Returns

		Array : An array containing the identifiers of the new curve objects if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'OffsetCurveOnSurface', None, strCurve, strSurface)

	def planarclosedcurvecontainment(self, strcurve1, strcurve2, arrplane, array, array, array, array, dbltolerance):
		"""

		Determines the relationship between the regions bounded by two coplanar simple closed curves.

		Parameters

		strCurve1 : Required,   String,   The object identifier of the first planar, closed curve
		strCurve2 : Required,   String,   The object identifier of the second planar, closed curve
		arrPlane : Optional,   Array,  The new construction plane
		Array : Required,   The construction plane's origin (3-D point), 
		Array : Required,   The construction plane's X axis direction (3-D vector), 
		Array : Required,   The construction plane's Y axis direction (3-D vector), 
		Array : Optional,   The construction plane's Z axis direction (3-D vector), 
		dblTolerance : Optional,   Number,   The tolerance

		Returns

		Number : A number identifying the relationship if successful.  The possible values are as follows:
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'PlanarClosedCurveContainment', None, strCurve1, strCurve2, arrPlane, Array, Array, Array, Array, dblTolerance)

	def planarcurvecollision(self, strcurve1, strcurve2, arrplane, array, array, array, array, dbltolerance):
		"""

		Determines if two coplanar curves intersect.

		Parameters

		strCurve1 : Required,   String,   The object identifier of the first planar curve
		strCurve2 : Required,   String,   The object identifier of the second planar curve
		arrPlane : Optional,   Array,  The new construction plane
		Array : Required,   The construction plane's origin (3-D point), 
		Array : Required,   The construction plane's X axis direction (3-D vector), 
		Array : Required,   The construction plane's Y axis direction (3-D vector), 
		Array : Optional,   The construction plane's Z axis direction (3-D vector), 
		dblTolerance : Optional,   Number,   The tolerance

		Returns

		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'PlanarCurveCollision', None, strCurve1, strCurve2, arrPlane, Array, Array, Array, Array, dblTolerance)

	def pointinplanarclosedcurve(self, arrpoint, strcurve, arrplane, array, array, array, array, dbltolerance):
		"""

		Determines if a point is inside of a closed curve, on  a closed curve, or outside of a closed curve.

		Parameters

		arrPoint : Required,   Array,   A 3-D point to test
		strCurve : Required,   String,   The object identifier of the planar, closed curve
		arrPlane : Optional,   Array,  The new construction plane
		Array : Required,   The construction plane's origin (3-D point), 
		Array : Required,   The construction plane's X axis direction (3-D vector), 
		Array : Required,   The construction plane's Y axis direction (3-D vector), 
		Array : Optional,   The construction plane's Z axis direction (3-D vector), 
		dblTolerance : Optional,   Number,   The tolerance

		Returns

		Number : A number identifying the result if successful.  The possible values are as follows:
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'PointInPlanarClosedCurve', None, arrPoint, strCurve, arrPlane, Array, Array, Array, Array, dblTolerance)

	def polycurvecount(self, strobject, intindex):
		"""

		Returns the number of curve segments that make up a polycurve.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Number : The number of curve segments in a polycurve if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'PolyCurveCount', None, strObject, intIndex)

	def polylinevertices(self, strobject, intindex):
		"""

		Returns the vertices of a polyline curve object.

		Parameters

		strObject : Required,   String,   The object's identifier
		intIndex : Optional,  Number,  If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query

		Returns

		Array : An  array of 3-D vertex points if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'PolylineVertices', None, strObject, intIndex)

	def projectcurvetomesh(self, strcurve, arrcurves, strmesh, arrmeshes, arrdirection):
		"""

		Projects one or more points onto one or more meshes.

		Parameters

		strCurve : Required,   Array,   The identifier of a curve object to project
		arrCurves : Required,   Array,   The identifiers of one or more curve objects to project
		strMesh : Required,   String,   The identifier of the mesh object to project onto
		arrMeshes : Required,   Array,   The identifiers of the mesh objects to project onto
		arrDirection : Required,   Array,   The direction (3-D vector) to project the points

		Returns

		Array : The identifiers of the newly created, projected curve objects, if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ProjectCurveToMesh', None, strCurve, arrCurves, strMesh, arrMeshes, arrDirection)

	def projectcurvetosurface(self, strcurve, arrcurves, strsurface, arrsurfaces, arrdirection):
		"""

		Projects one or more points onto one or more surfaces or polysurfaces.

		Parameters

		strCurve : Required,   Array,   The identifier of a curve object to project
		arrCurves : Required,   Array,   The identifiers of one or more curve objects to project
		strSurface : Required,   String,   The identifier of the surface or polysurface object to project onto
		arrSurfaces : Required,   Array,   The identifiers of the surface or polysurface objects to project onto
		arrDirection : Required,   Array,   The direction (3-D vector) to project the points

		Returns

		Array : The identifiers of the newly created, projected curve objects, if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ProjectCurveToSurface', None, strCurve, arrCurves, strSurface, arrSurfaces, arrDirection)

	def rebuildcurve(self, strobject, intdegree, intpointcount):
		"""

		Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.

		Parameters

		strObject : Required,   String,   The object's identifier
		intDegree : Optional,   Number,   The new degree, which must be greater than 1
		intPointCount : Optional,   Number,   The new point count, which must be bigger than the intDegree

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'RebuildCurve', None, strObject, intDegree, intPointCount)

	def removecurveknot(self, strobject, dblparameter):
		"""

		Deletes a knot from a curve object.

		Parameters

		strObject : Required,   String,   The identifier of the curve object
		dblParameter : Required,   Number,   The parameter on the curve

		Returns

		Boolean : True of False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveCurveKnot', None, strObject, dblParameter)

	def reversecurve(self, strobject):
		"""

		Reverses the direction of a curve object. This feature can also be found in Rhino's Dir command.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ReverseCurve', None, strObject)

	def simplifycurve(self, strobject, intflags):
		"""

		6.  Segments that meet with G1-continuity have there ends tuned up so that they meet with G1-continuity to within machine precision.

		Parameters

		strObject : Required,   String,   The curve object's identifier
		intFlags : Optional,   Number,   The simplification methods to use

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SimplifyCurve', None, strObject, intFlags)

	def splitcurve(self, strobject, dblparameter, arrparameters, blndelete):
		"""

		Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.

		Parameters

		strObject : Required,   String,   The object's identifier
		dblParameter : Required,   Number,   The parameter, to split the curve at, that is in the interval returned by CurveDomain
		arrParameters : Required,   Array,   An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain
		blnDelete : Optional,   Boolean,   Delete the input curve

		Returns

		Array : An array containing the identifiers of the two newly created curve objects, if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SplitCurve', None, strObject, dblParameter, arrParameters, blnDelete)

	def trimcurve(self, strobject, arrinterval, blndelete):
		"""

		Trims a curve by removing portions of the curve outside the specified interval.

		Parameters

		strObject : Required,   String,   The object's identifier
		arrInterval : Required,   Array,   An array of two number identifying the interval to keep
		blnDelete : Optional,  Boolean,  Delete the input curve

		Returns

		String : The identifier of the newly created curve object, if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'TrimCurve', None, strObject, arrInterval, blnDelete)

