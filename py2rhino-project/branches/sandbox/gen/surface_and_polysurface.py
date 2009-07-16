# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class SurfaceAndPolysurface(DispatchBaseClass):



    def add_box(self, arr_corners):
        """

        Adds a new box-shaped polysurface to the document.

        Parameters

        arrCorners : Required, Array, An array of eight 3-D points that define the corners of the box

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddBox', None, arrCorners)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_cut_plane(self, arr_objects, arr_start_point, arr_end_point, arr_normal):
        """

        Adds a planar surface through objects at a designated location.  For more information, see the Rhino help file for the CutPlane command.

        Parameters

        arrObjects : Required, Array, The identifiers of objects that the cutting planes will pass through
        arrStartPoint : Required, Array, The start of the line that defines the cutting plane
        arrEndPoint : Required, Number, The end of the line that defines the cutting plane
        arrNormal : Optional, A vector that will be contained in the returned planar surface, In the case of Rhino's CutPlane command, this is the normal to, or Z axis of, the active view's construction plane

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddCutPlane', None, arrObjects, arrStartPoint, arrEndPoint, arrNormal)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_edge_srf(self, arr_objects):
        """

        Creates a surface from 2, 3, or 4 edge curves.

        Parameters

        arrObjects : Required, Array, An array of 2, 3, or 4 curve object identifiers

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddEdgeSrf', None, arrObjects)

    def add_loft_srf(self, arr_objects, arr_start_pt, arr_end_pt, int_type, int_style, n_value, bln_closed):
        """

        * This function will not adjust the seams of closed curves. Use CurveSeam to adjust the seam of closed curves.

        Parameters

        arrObjects : Required, Array, An ordered array of strings identifying the curve objects to loft
        arrStartPt : Optional, Array, The starting point of the loft
        arrEndPt : Optional, Array, The ending point of the loft
        intType : Optional, Number, The type of loft
        intStyle : Optional, Number, The simplify method of the loft
        nValue : Optional, Number, A value based on the specified intStyle
        blnClosed : Optional, Boolean, Creates a closed surface, continuing the surface past the last curve around to the first curve

        Returns

        Array : An array containing the identifiers of the new surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddLoftSrf', None, arrObjects, arrStartPt, arrEndPt, intType, intStyle, nValue, blnClosed)

    def add_nurbs_surface(self, arr_point_count, arr_points, arr_knots_u, arr_knots_u, arr_degree, arr_weights):
        """

        Adds a NURBS surface object to the document.

        Parameters

        arrPointCount : Required, Array, The number of control points in the U and V directions
        arrPoints : Required, Array, An array of 3-D control points
        arrKnotsU : Required, Array, The knot values for the surface in the U direction
        arrKnotsU : Required, Array, The knot values for the surface in the U direction
        arrDegree : Required, Array, The degree of the surface in the U and V directions
        arrWeights : Required, Array, The weight values for the surface

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddNurbsSurface', None, arrPointCount, arrPoints, arrKnotsU, arrKnotsU, arrDegree, arrWeights)

    def add_planar_srf(self, arr_objects):
        """

        Creates one or more surfaces from planar curves.

        Parameters

        arrObjects : Required, Array, An array of curve object identifiers

        Returns

        Array : An array of strings identifying the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPlanarSrf', None, arrObjects)

    def add_plane_surface(self, arr_plane, dbl_d_u, dbl_d_v):
        """

        Creates a plane surface.

        Parameters

        arrPlane : Required, Array, The plane
        dblDU : Required, Number, The magnitude in the U direction
        dblDV : Required, Number, The magnitude in the V direction

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddPlaneSurface', None, arrPlane, dblDU, dblDV)

    def add_rail_rev_srf(self, str_profile, str_rail, arr_axis):
        """

        Create a surface by revolving a profile curve along a rail curve.

        Parameters

        strProfile : Required, String, The identifier of the profile curve
        strRail : Required, String, The identifier of the rail curve
        arrAxis : Required, Array, An array of two 3-D points identifying the start point and end point of the rail revolve axis

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddRailRevSrf', None, strProfile, strRail, arrAxis)

    def add_rev_srf(self, str_profile, arr_axis, dbl_start_angle, dbl_end_angle):
        """

        Create a surface by revolving a curve around an axis.

        Parameters

        strProfile : Required, String, The identifier of the curve to revolve
        arrAxis : Required, Array, An array of two 3-D points identifying the start point and end point of the rail revolve axis
        dblStartAngle : Optional, Number, The starting angle
        dblEndAngle : Optional, Number, The ending angle

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddRevSrf', None, strProfile, arrAxis, dblStartAngle, dblEndAngle)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_srf_control_pt_grid(self, arr_count, arr_points, arr_degree):
        """

        Creates a surface from a grid of control points.

        Parameters

        arrCount : Required, Array, The number of control points in the U and V directions
        arrPoints : Required, Array, An array of 3-D control points
        arrDegree : Optional, Array, The degree of the surface in the U and V directions

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddSrfControlPtGrid', None, arrCount, arrPoints, arrDegree)

    def add_srf_pt(self, arr_points):
        """

        Creates a new surface from either 3 or 4 corner points.

        Parameters

        arrPoints : Required, Array, An array of either 3 or 4 corner points

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddSrfPt', None, arrPoints)

    def add_srf_pt_grid(self, arr_count, arr_points, arr_degree, arr_closed):
        """

        Creates a surface from a grid of points.

        Parameters

        arrCount : Required, Array, The number of points in the U and V directions
        arrPoints : Required, Array, An array of 3-D points
        arrDegree : Optional, Array, The degree of the surface in the U and V directions
        arrClosed : Optional, Array, Whether or not the surface is closed in the U and V directions

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddSrfPtGrid', None, arrCount, arrPoints, arrDegree, arrClosed)

    def add_srf_section_crvs(self, str_object, arr_plane):
        """

        Adds planar curves resulting from the intersection of a defined cutting plane through a surface or a polysurface. For more information, see the Rhino help file for details on the Section command.

        Parameters

        strObject : Required, String, The identifier of a surface or polysurface object
        arrPlane : Required, Array, A plane that defines the cutting plane

        Returns

        Array : An array of strings identifying the newly created section curves if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddSrfSectionCrvs', None, strObject, arrPlane)

    def add_sweep1(self, str_rail, arr_shapes, arr_start_pt, arr_end_pt, bln_closed, int_style, va_style_arg, int_simplify, va_simplify_arg):
        """

        * The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.

        Parameters

        strRail : Required, String, The identifier of the rail curve
        arrShapes : Required, Array, An array of strings identifying one or more shape, or cross section, curves
        arrStartPt : Optional, Array, The 3-D starting point of the surface
        arrEndPt : Optional, Array, The 3-D ending point of the surface
        blnClosed : Optional, Boolean, If True, then create a closed surface, continuing the surface past the last curve around to the first curve
        intStyle : Optional, Integer, The sweep style, where 0 = Freeform and 1 = Roadlike
        vaStyleArg : Optional, Variant, If intStyle = 1 (Roadlike), then this argument is a 3-D vector identifying the planar up direction for the sweep
        intSimplify : Optional, Integer, Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild
        vaSimplifyArg : Optional, Variant, If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance

        Returns

        Array : The identifiers of the new surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddSweep1', None, strRail, arrShapes, arrStartPt, arrEndPt, blnClosed, intStyle, vaStyleArg, intSimplify, vaSimplifyArg)

    def add_sweep2(self, arr_rails, arr_shapes, arr_start_pt, arr_end_pt, bln_closed, bln_simple_sweep, bln_maintain_height, int_simplify, va_simplify_arg):
        """

        * The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.

        Parameters

        arrRails : Required, String, An array of strings identifying two rail curves
        arrShapes : Required, Array, An array of strings identifying one or more shape, or cross section, curves
        arrStartPt : Optional, Array, The 3-D starting point of the surface
        arrEndPt : Optional, Array, The 3-D ending point of the surface
        blnClosed : Optional, Boolean, If True, then create a closed surface, continuing the surface past the last curve around to the first curve
        blnSimpleSweep : Optional, Boolean, If True, then create surfaces using exact input
        blnMaintainHeight : Optional, Boolean, By default, shape curves normally scale in both the height and width dimensions
        intSimplify : Optional, Integer, Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild
        vaSimplifyArg : Optional, Variant, If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance

        Returns

        Array : The identifiers of the new surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddSweep2', None, arrRails, arrShapes, arrStartPt, arrEndPt, blnClosed, blnSimpleSweep, blnMaintainHeight, intSimplify, vaSimplifyArg)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def boolean_difference(self, arr_input0, arr_input1, bln_delete):
        """

        Performs a Boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file.

        Parameters

        arrInput0 : Required, Array, The identifiers of the surfaces or polysurfaces to subtract from
        arrInput1 : Required, Array, The identifiers of the surfaces or polysurfaces to be subtracted
        blnDelete : Optional, Boolean, Delete all input objects

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BooleanDifference', None, arrInput0, arrInput1, blnDelete)

    def boolean_intersection(self, arr_input0, arr_input1, bln_delete):
        """

        Performs a Boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file.

        Parameters

        arrInput0 : Required, Array, The identifiers of the surfaces or polysurfaces
        arrInput1 : Required, Array, The identifiers of the surfaces or polysurfaces
        blnDelete : Optional, Boolean, Delete all input objects

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BooleanIntersection', None, arrInput0, arrInput1, blnDelete)

    def boolean_union(self, arr_input, bln_delete):
        """

        Performs a Boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file.

        Parameters

        arrInput : Required, Array, The identifiers of the surfaces or polysurfaces to union
        blnDelete : Optional, Boolean, Delete all input objects

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BooleanUnion', None, arrInput, blnDelete)

    def brep_closest_point(self, str_object, arr_point):
        """

        Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.

        Parameters

        strObject : Required, String, The object's identifier
        arrPoint : Required, Array, The test, or sampling, point

        Returns

        Array : An array of closest point information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BrepClosestPoint', None, strObject, arrPoint)

    def cap_planar_holes(self, str_surface):
        """

        Caps planar holes in a surface or polysurface. For more details, see the Cap command in the Rhino help file.

        Parameters

        strSurface : Required, String, The identifier of the surface or polysurface to cap

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CapPlanarHoles', None, strSurface)

    def duplicate_edge_curves(self, str_object, bln_select):
        """

        Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.

        Parameters

        strObject : Required, String, The identifier of the surface or polysurface object
        blnSelect : Optional, Boolean, Select the duplicated edge curves

        Returns

        Array : An array of strings identifying the newly created curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DuplicateEdgeCurves', None, strObject, blnSelect)

    def duplicate_surface_border(self, str_object):
        """

        Creates a curve that duplicates a surface or polysurface border.

        Parameters

        strObject : Required, String, The identifier of the surface or polysurface object

        Returns

        Array : An array of strings identifying the new curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DuplicateSurfaceBorder', None, strObject)

    def evaluate_surface(self, str_object, arr_parameter):
        """

        Evaluates a surface at a U,V parameter.

        Parameters

        strObject : Required, String, The object's identifier
        arrParameter : Required, Array, An array containing the U,V parameter to evaluate

        Returns

        Array : A 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'EvaluateSurface', None, strObject, arrParameter)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def extract_iso_curve(self, str_object, arr_parameter, int_dir):
        """

        Extracts isoparametric curves from a surface.

        Parameters

        strObject : Required, String, The object's identifier
        arrParameter : Required, Array, An array containing the U,V parameter of the surface to evaluate
        intDir : Required, Number, The direction, either 0 = U, 1 = V, or 2 = Both

        Returns

        Array : An array of strings identifying the newly created curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtractIsoCurve', None, strObject, arrParameter, intDir)

    def extrude_curve(self, str_curve, str_path):
        """

        Creates a surface by extruding a curve along a path curve.

        Parameters

        strCurve : Required, String, The identifier of the curve object to extrude
        strPath : Required, String, The identifier of the path curve

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtrudeCurve', None, strCurve, strPath)

    def extrude_curve_point(self, str_curve, arr_point):
        """

        Creates a surface by extruding a curve to a point.

        Parameters

        strCurve : Required, String, The identifier of the curve object to extrude
        arrPoint : Required, Array, A 3-D point

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtrudeCurvePoint', None, strCurve, arrPoint)

    def extrude_curve_straight(self, str_curve, arr_start_point, arr_end_point):
        """

        Creates a surface by extruding a curve straight along two points that define a line.

        Parameters

        strCurve : Required, String, The identifier of the curve object to extrude
        arrStartPoint : Required, Array, A starting point
        arrEndPoint : Required, Array, A ending point

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtrudeCurveStraight', None, strCurve, arrStartPoint, arrEndPoint)

    def extrude_curve_tapered(self, str_curve, dbl_distance, arr_direction, arr_base_point, dbl_angle, int_corner_type):
        """

        Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.

        Parameters

        strCurve : Required, String, The identifier of the curve object to extrude
        dblDistance : Required, Number, The extrusion distance
        arrDirection : Required, Array, A 3-D vector that specifies the extrusion direction
        arrBasePoint : Required, Array, A 3-D point that specifies the base point of the extrusion
        dblAngle : Required, Number, The angle of the extrusion
        intCornerType : Optional, Number, The corner type of the extrusion, where:

        Returns

        Array : An array of strings identifying the newly created surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtrudeCurveTapered', None, strCurve, dblDistance, arrDirection, arrBasePoint, dblAngle, intCornerType)

    def extrude_surface(self, str_surface, str_curve, bln_cap):
        """

        Creates a surface or solid by extruding a straight along a path curve.

        Parameters

        strSurface : Required, String, The identifier of the surface object to extrude
        strCurve : Required, String, The identifier of the path curve
        blnCap : Optional, Boolean, Extrusion is capped at both ends to make a closed polysurface

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ExtrudeSurface', None, strSurface, strCurve, blnCap)

    def fit_surface(self, str_object, arr_degree, dbl_tolerance):
        """

        Reduces the number of surface control points while maintaining the surfaces' same general shape.  Use this function for replacing surface with too many control points.  For more information, see the Rhino help file for the FitSrf command.

        Parameters

        strObject : Required, String, The object's identifier
        arrDegree : Optional, Array, An array of two numbers that identify the surface curve degree in both the U and the V directions
        dblTolerance : Optional, Number, The fitting tolerance

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'FitSurface', None, strObject, arrDegree, dblTolerance)

    def flip_surface(self, str_object, bln_flip):
        """

        Returns or changes the normal direction of a surface. This feature can also be found in Rhino's Dir command.

        Parameters

        strObject : Required, String, The identifier of a surface object
        blnFlip : Optional, Boolean, The new normal orientation, either flipped (True) or not flipped (False)

        Returns

        Boolean : If blnFlip is not specified, the current normal orientation if successful.
        Boolean : If blnFlip is specified, the previous normal orientation if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'FlipSurface', None, strObject, blnFlip)

    def insert_surface_knot(self, str_object, dbl_parameter, int_direction, bln_symmetrical):
        """

        Inserts a knot into a surface object.

        Parameters

        strObject : Required, String, The identifier of the surface object
        dblParameter : Required, Array, An array containing a U,V parameter on the surface
        intDirection : Required, Number, The direction for knot insertion, either 0 = U, 1 = V, or 2 = both
        blnSymmetrical : Optional, Boolean, If blnSymmetrical = True, then knots are added on both sides of the center of the surface

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'InsertSurfaceKnot', None, strObject, dblParameter, intDirection, blnSymmetrical)

    def intersect_breps(self, str_brep1, str_brep2, dbl_tolerance):
        """

        Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.

        Parameters

        strBrep1 : Required, String, The first brep object's identifier
        strBrep2 : Required, String, The second  brep object's identifier
        dblTolerance : Optional, Number, The distance tolerance at segment midpoints

        Returns

        Array : An array of strings identifying the newly created intersection curve and point objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IntersectBreps', None, strBrep1, strBrep2, dblTolerance)

    def is_brep(self, str_object):
        """

        Verifies an object is a Brep, or a boundary representation model, object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsBrep', None, strObject)

    def is_brep_manifold(self, str_object):
        """

        Verifies a polysurface object is manifold.  A polysurface for which every edge is shared by at most two faces is called a manifold.  If a polysurface has at least one edge that is shared by more than two faces, then that polysurface is called non-manifold.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsBrepManifold', None, strObject)

    def is_cone(self, str_surface):
        """

        Determines if a surface is a portion of a cone.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCone', None, strSurface)

    def is_cylinder(self, str_surface):
        """

        Determines if a surface is a portion of a cylinder.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsCylinder', None, strSurface)

    def is_parameter_on_surface(self, str_object, arr_parameter):
        """

        Verifies that a parameter space point is on a trimmed surface, or not on the trimmed portion of a surface.

        Parameters

        strObject : Required, String, The object's identifier
        arrParameter : Required, Array, An array containing the U,V parameter to evaluate

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsParameterOnSurface', None, strObject, arrParameter)

    def is_plane_surface(self, str_object):
        """

        Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, a plane surface is not a planar NURBS surface.

        Parameters

        strObject : Required, String, The identifier of the object to verify

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPlaneSurface', None, strObject)

    def is_point_in_surface(self, str_object, arr_point):
        """

        Verifies that a point is inside a closed surface or polysurface.

        Parameters

        strObject : Required, String, The object's identifier
        arrPoint : Required, Array, The test, or sampling, point

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPointInSurface', None, strObject, arrPoint)

    def is_point_on_surface(self, str_object, arr_point):
        """

        Verifies that a point lies on a surface.

        Parameters

        strObject : Required, String, The object's identifier
        arrPoint : Required, Array, The test, or sampling, point

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPointOnSurface', None, strObject, arrPoint)

    def is_poly_surface(self, str_object):
        """

        Verifies an object is a polysurface.  Polysurfaces consists of two or more surfaces joined together. If the polysurface fully encloses a volume, it is considered a solid. In some other 3-D programs, this is called a "quilt."

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPolySurface', None, strObject)

    def is_poly_surface_closed(self, str_object):
        """

        Verifies a polysurface object is closed.  If the polysurface fully encloses a volume, it is considered a solid.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPolySurfaceClosed', None, strObject)

    def is_poly_surface_planar(self, str_object):
        """

        Verifies a polysurface object is planar.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsPolySurfacePlanar', None, strObject)

    def is_sphere(self, str_surface):
        """

        Determines if a surface is a portion of a sphere.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSphere', None, strSurface)

    def is_surface(self, str_object):
        """

        Verifies an object is surface.  Brep objects with only one face are also considered surfaces.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSurface', None, strObject)

    def is_surface_closed(self, str_object, int_direction):
        """

        Verifies a surface object is closed in the specified direction.  If the surface fully encloses a volume, it is considered a solid.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The direction, either 0 = U, or 1 = V

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSurfaceClosed', None, strObject, intDirection)

    def is_surface_periodic(self, str_object, int_direction):
        """

        Verifies a surface object is periodic in the specified direction.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The direction, either 0 = U, or 1 = V

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSurfacePeriodic', None, strObject, intDirection)

    def is_surface_planar(self, str_object, dbl_tolerance):
        """

        Verifies a surface object is planar.

        Parameters

        strObject : Required, String, The object's identifier
        dblTolerance : Optional, Number, A tolerance to use when checking

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSurfacePlanar', None, strObject, dblTolerance)

    def is_surface_rational(self, str_object):
        """

        Verifies a surface object is rational.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSurfaceRational', None, strObject)

    def is_surface_singular(self, str_object, int_direction):
        """

        Verifies a surface object is singular in the specified direction.  Surfaces are considered singular if a side collapses to a point.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The direction, either 0 = south, 1 = east, 2 = north, or 3 = west

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSurfaceSingular', None, strObject, intDirection)

    def is_surface_trimmed(self, str_object):
        """

        Verifies a surface object has been trimmed.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsSurfaceTrimmed', None, strObject)

    def is_torus(self, str_surface):
        """

        Determines if a surface is a portion of a torus.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsTorus', None, strSurface)

    def join_surfaces(self, str_object, bln_delete):
        """

        Joins two or more surface or polysurface object together to form one polysurface object.

        Parameters

        strObject : Required, Array, An ordered array of strings identifying the surfaces or polysurfaces objects to join
        blnDelete : Optional, Boolean, Delete input objects after joining

        Returns

        String : The identifier of the newly created polysurface object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'JoinSurfaces', None, strObject, blnDelete)

    def make_surface_non_periodic(self, str_object, int_direction, bln_delete):
        """

        Makes a periodic surface non-periodic. Non-periodic surfaces can develop kinks when deformed.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The direction to make non-periodic, either 0 = U, or 1 = V
        blnDelete : Optional, Boolean, Delete input surface

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MakeSurfaceNonPeriodic', None, strObject, intDirection, blnDelete)

    def make_surface_periodic(self, str_object, int_direction, bln_delete):
        """

        Makes an existing surface a periodic NURBS surface.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The direction to make periodic, either 0 = U, or 1 = V
        blnDelete : Optional, Boolean, Delete input surface

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MakeSurfacePeriodic', None, strObject, intDirection, blnDelete)

    def offset_surface(self, str_object, dbl_distance):
        """

        Offsets a surface by a distance. The offset surface will be added to Rhino.

        Parameters

        strObject : Required, String, The object's identifier
        dblDistance : Required, Number, The distance to offset

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'OffsetSurface', None, strObject, dblDistance)

    def pull_curve(self, str_surface, str_curve, bln_delete):
        """

        Pulls a curve object to a surface object. For more information, see the Rhino help file for information on the Pull command.

        Parameters

        strSurface : Required, String, The identifier of the surface object that pulls
        strCurve : Required, String, The identifier of the curve object to pull
        blnDelete : Optional, Boolean, Delete input curve

        Returns

        Array : The identifiers of the new curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PullCurve', None, strSurface, strCurve, blnDelete)

    def rebuild_surface(self, str_object, arr_degree, arr_point_count):
        """

        Rebuilds a surface to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.

        Parameters

        strObject : Required, String, The object's identifier
        arrDegree : Optional, Array, An array of two numbers that identify the surface curve degree in both the U and the V directions
        arrPointCount : Optional, Array, An array of two numbers that identify the surface point count in both the U and the V directions

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RebuildSurface', None, strObject, arrDegree, arrPointCount)

    def remove_surface_knot(self, str_object, dbl_parameter, int_direction):
        """

        Deletes a knot-line from a surface object.

        Parameters

        strObject : Required, String, The identifier of the surface object
        dblParameter : Required, Array, An array containing a U,V parameter on the surface
        intDirection : Required, Number, The direction for knot insertion, either 0 = U, or 1 = V

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveSurfaceKnot', None, strObject, dblParameter, intDirection)

    def reverse_surface(self, str_object, int_direction):
        """

        To reverse the normal direction of a surface, use the FlipSurface method.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The direction to reverse

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ReverseSurface', None, strObject, intDirection)

    def short_path(self, str_surface, arr_start, arr_end):
        """

        Creates the shortest possible curve (geodesic) between two points on a surface. For more details, see the ShortPath command in the Rhino help file.

        Parameters

        strSurface : Required, String, The identifier of the surface object that pulls
        arrStart : Required, Array, A 3-D surface point identifying the starting point of the short curve
        arrEnd : Required, Array, A 3-D surface point identifying the ending point of the short curve

        Returns

        String : The identifier of the new curve object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShortPath', None, strSurface, arrStart, arrEnd)

    def shrink_trimmed_surface(self, str_surface):
        """

        Shrinks the underlying untrimmed surfaces near to trimming boundaries. For more details, see the ShrinkTrimmedSrf command in the Rhino help file.

        Parameters

        strSurface : Required, String, The identifier of the surface or polysurface to shrink

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShrinkTrimmedSurface', None, strSurface)

    def split_brep(self, str_brep, str_cutter, bln_delete):
        """

        Splits a brep.  A brep can be either a surface with a single face or a polysurface.

        Parameters

        strBrep : Required, String, The identifier of the brep object to split
        strCutter : Required, String, The identifier of the brep object to split with
        blnDelete : Optional, Boolean, Delete input brep

        Returns

        Array : The identifiers of the new brep objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SplitBrep', None, strBrep, strCutter, blnDelete)

    def surface_area(self, str_object):
        """

        Calculates the area of a surface or polysurface object. The results are based on the current drawing units.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of area information if successful.  The array will contain the following information:
        Number : The area.
        Number : The absolute (+/-) error bound for the area.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceArea', None, strObject)

    def surface_area_centroid(self, str_object):
        """

        Calculates the area centroid of a surface or polysurface object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of area centroid information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceAreaCentroid', None, strObject)

    def surface_area_moments(self, str_object):
        """

        Calculates the area moments of inertia of a surface or polysurface object.  For more information, see the Rhino help file for "Mass Properties Calculation Details."

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of area moments of inertia information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceAreaMoments', None, strObject)

    def surface_closest_point(self, str_object, arr_point):
        """

        Returns the UV parameter of the point on a surface that is closest to a test point.

        Parameters

        strObject : Required, String, The object's identifier
        arrPoint : Required, Array, The test, or sampling, point

        Returns

        Array : An array containing the U,V parameters of the closest point on the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceClosestPoint', None, strObject, arrPoint)

    def surface_cone(self, str_surface):
        """

        Returns the definition of a cone surface.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Array : An array containing the definition of the cone if successful.  The elements of the array are as follows:
        Array : The plane of the cone.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
        Number : The height of the cone.
        Number : The radius of the cone.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceCone', None, strSurface)

    def surface_contour_points(self, str_object, arr_start_point, arr_end_point, dbl_interval, dbl_angle):
        """

        Returns the vertices of the polyline curves generated by contouring a surface or polysurface object.

        Parameters

        strObject : Required, String, The identifier of a surface or polysurface object
        arrStartPoint : Required, Array, The 3-D starting point of a center line
        arrEndPoint : Required, Array, The 3-D ending point of a center line
        dblInterval : Optional, Number, The distance between contour curves
        dblAngle : Optional, Number, The maximum angle in degrees between unit tangents at adjacent vertices

        Returns

        Array : An array of 3-D point arrays, one for each contour, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceContourPoints', None, strObject, arrStartPoint, arrEndPoint, dblInterval, dblAngle)

    def surface_curvature(self, str_object, arr_parameter):
        """

        Returns the curvature of a surface at a U,V parameter.  See the Rhino help file for details on surface curvature.

        Parameters

        strObject : Required, String, The object's identifier
        arrParameter : Required, Array, An array containing the U,V parameter to evaluate

        Returns

        Array : An array of curvature information if successful.  The array will contain the following information:
        Number : Maximum principal curvature.
        Number : Minimum principal curvature.
        Number : Gaussian curvature.
        Number : Mean curvature.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceCurvature', None, strObject, arrParameter)

    def surface_curvature_analysis(self, str_object):
        """

        Returns the curvature of a surface.  See the Rhino help file for details on surface curvature analysis.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of curvature information if successful.  The array will contain the following information:
        Array : An array containing three values: the min Gaussian curvature, the max Gaussian curvature, and the infinity status.
        Array : An array containing three values: the min unsigned mean curvature, the max unsigned mean curvature, and the infinity comparison.
        Array : An array containing three values: the min maximum unsigned radius of curvature, the max maximum unsigned radius of curvature, and the infinity comparison.
        Array : An array containing three values: the min minimum unsigned radius of curvature, the max minimum unsigned radius of curvature, and the infinity comparison.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceCurvatureAnalysis', None, strObject)

    def surface_cylinder(self, str_surface):
        """

        Returns the definition of a cylinder surface.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Array : An array containing the definition of the cylinder if successful.  The elements of the array are as follows:
        Array : The base plane of the cylinder.
        Number : The height of the cylinder.
        Number : The radius of the cylinder.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceCylinder', None, strSurface)

    def surface_degree(self, str_object, int_direction):
        """

        Returns the degree of a  surface object in the specified direction.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Optional, Number, The direction, either 0 = U, or 1 = V, or 2 = Both

        Returns

        Array : If intDirection is not specified, or intDirection is set to 2, then the degree in both the U and V directions is returned.
        Number : If intDirection is specified, and intDirection is set to either 0 or 1, then the degree in either the U or V direction is returned.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceDegree', None, strObject, intDirection)

    def surface_domain(self, str_object, int_direction):
        """

        Returns the domain of a  surface object in the specified direction.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The direction, either 0 = U, or 1 = V

        Returns

        Array : An array containing the domain interval in the specified direction if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceDomain', None, strObject, intDirection)

    def surface_edit_points(self, str_object, bln_return_parameters, bln_return_all):
        """

        Returns the edit, or Greville, points of a surface object.  For each surface control point, there is a corresponding edit point.

        Parameters

        strObject : Required, String, The object's identifier
        blnReturnParameters : Optional, Boolean, If False (default), edit points are returned as an array of 3-D points
        blnReturnAll : Optional, Boolean, If True (default) all surface edit points are returned

        Returns

        Array : If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.
        Array : If blnReturnParameters is True, then an array of U,V parameter values if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceEditPoints', None, strObject, blnReturnParameters, blnReturnAll)

    def surface_evaluate(self, str_object, arr_parameter, int_derivative):
        """

        A general purpose surface evaluator.

        Parameters

        strObject : Required, String, The object's identifier
        arrParameter : Required, Array, An array containing the U,V parameter to evaluate
        intDerivative : Required, Number, The number of derivatives to evaluate

        Returns

        Array : An array of length (intDerivative+1)*(intDerivative+2)/2 if successful.  The array elements are as follows:
        Array : The 3-D point.
        Array : The first derivative.
        Array : The first derivative.
        Array : The second derivative.
        Array : The second derivative.
        Array : The second derivative.
        Array : etc...
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceEvaluate', None, strObject, arrParameter, intDerivative)

    def surface_frame(self, str_object, arr_parameter):
        """

        Returns a plane based on the normal, u, and v directions at a given surface U,V parameter.

        Parameters

        strObject : Required, String, The object's identifier
        arrParameter : Required, Array, An array containing the U,V parameter to evaluate

        Returns

        Array : The plane at the specified parameter if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceFrame', None, strObject, arrParameter)

    def surface_isocurve_density(self, str_object, int_density):
        """

        Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface.

        Parameters

        strObject : Required, String, The object's identifier
        intDensity : Optional, Number, The isocurve wireframe density

        Returns

        Number : The intDensity is not specified, then the current isocurve density if successful.
        Number : The intDensity is specified, then the previous isocurve density if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceIsocurveDensity', None, strObject, intDensity)

    def surface_knot_count(self, str_object):
        """

        Returns the knot count of a surface object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : The number of knots in the U and V directions if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceKnotCount', None, strObject)

    def surface_knots(self, str_object):
        """

        Returns the knots, or knot vector, of a surface object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : The knot values of the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceKnots', None, strObject)

    def surface_normal(self, str_object, arr_parameter):
        """

        Returns a 3-D vector that is the normal to a surface at a parameter.

        Parameters

        strObject : Required, String, The object's identifier
        arrParameter : Required, Array, An array containing the UV parameter to evaluate

        Returns

        Array : A 3-D vector if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceNormal', None, strObject, arrParameter)

    def surface_point_count(self, str_object):
        """

        Returns the control points count of a surface object.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : The number of control points in the U and V directions if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfacePointCount', None, strObject)

    def surface_points(self, str_object, bln_return_all):
        """

        Returns the control points, or control vertices, of a surface object.

        Parameters

        strObject : Required, String, The object's identifier
        blnReturnAll : Optional, Boolean, If True (default) all surface edit points are returned

        Returns

        Array : The control points of the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfacePoints', None, strObject, blnReturnAll)

    def surface_principal_curvature(self, str_object, arr_point):
        """

        Adds curvature curves at the evaluated point on a surface. For more information, see the Rhino help file for the Curvature command.

        Parameters

        strObject : Required, String, The curve's identifier
        arrPoint : Required, Array, A point on the curve to evaluate

        Returns

        Array : An array of two strings that identify the Maximum and Minimum principal curvature curves, respectively, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfacePrincipalCurvature', None, strObject, arrPoint)

    def surface_seam(self, str_object, int_direction, dbl_parameter):
        """

        Changes the seam of a closed surface. For more information, see the Rhino help file for the SrfSeam command.

        Parameters

        strObject : Required, String, The object's identifier
        intDirection : Required, Number, The parameter direction, where 0 = U and 1 = V
        dblParameter : Required, Number, The parameter at which to place the seam

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceSeam', None, strObject, intDirection, dblParameter)

    def surface_sphere(self, str_surface):
        """

        Returns the definition of a sphere surface.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Array : An array containing the definition of the sphere if successful.  The elements of the array are as follows:
        Array : The equatorial plane of the sphere.  The origin of the plane will be the center point of the sphere.
        Number : The radius of the sphere.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceSphere', None, strSurface)

    def surface_surface_intersection(self, str_surface_a, str_surface_b, dbl_tolerance, bln_create):
        """

        Calculates the intersection of a surface object with another surface object. Note, this function works on untrimmed surfaces.

        Parameters

        strSurfaceA : Required, String, The identifier of the first surface object
        strSurfaceB : Required, String, The identifier of the second surface object
        dblTolerance : Optional, Number, The absolute tolerance in drawing units
        blnCreate : Optional, Boolean, Create the intersection curves and points

        Returns

        Array : If blnCreate is not specified or is equal to False, an array numbers identifying the intersection event type if successful.  The array will contain one or more of the following intersection event types:
        Array : If blnCreate is specified and is equal to True, a two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:
        Number : The intersection event type.  See the above table for details.
        String : The identifier of the intersection curve or point object that was created.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceSurfaceIntersection', None, strSurfaceA, strSurfaceB, dblTolerance, blnCreate)

    def surface_torus(self, str_surface):
        """

        Returns the definition of a torus surface.

        Parameters

        strSurface : Required, String, The surface object's identifier

        Returns

        Array : An array containing the definition of the torus if successful.  The elements of the array are as follows:
        Array : The base plane of the torus.
        Number : The major radius of the torus.
        Number : The minor radius of the torus.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceTorus', None, strSurface)

    def surface_volume(self, str_object):
        """

        Calculates the volume of closed surface or polysurface objects.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of volume information if successful.  The array will contain the following information:
        Number : The volume.
        Number : The absolute (+/-) error bound for the volume.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceVolume', None, strObject)

    def surface_volume_centroid(self, str_object):
        """

        Calculates the volume centroid of closed surface or polysurface objects.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of volume centroid information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceVolumeCentroid', None, strObject)

    def surface_volume_moments(self, str_object):
        """

        Calculates the volume moments of inertia of closed surface or polysurface objects.  For more information, see the Rhino help file for "Mass Properties Calculation Details."

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : An array of volume moments of inertia information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceVolumeMoments', None, strObject)

    def surface_weights(self, str_object):
        """

        Returns an array of weight values that are assigned to the control points of a surface.  The number of weights returned will be equal to the number of control points in the U and V directions.

        Parameters

        strObject : Required, String, The object's identifier

        Returns

        Array : The weight values of the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SurfaceWeights', None, strObject)

