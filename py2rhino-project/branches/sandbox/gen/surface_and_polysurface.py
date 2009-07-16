# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class SurfaceAndPolysurface(IRhinoScript):



    def add_box(self, corners):
        """

        Adds a new box-shaped polysurface to the document.

        Parameters

        Corners : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(72, 1, (12, 0), ((8197, 0),), u'AddBox', None, _utils.flatten(corners))

    def add_cone(self, base, plane, height1, height2, radius, cap):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_cut_plane(self, objects, start_point, end_point, normal):
        """

        Adds a planar surface through objects at a designated location.  For more information, see the Rhino help file for the CutPlane command.

        Parameters

        Objects : Required, Array, arrdbl, Array of ?
        StartPoint : Required, Array, arrdbl, Array of ?
        EndPoint : Required, Number, arrdbl, Array of ?
        Normal : Optional, A vector that will be contained in the returned planar surface, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(822, 1, (12, 0), ((8197, 0), (8197, 0), (8197, 0), (8197, 0),), u'AddCutPlane', None, _utils.flatten(objects), _utils.flatten(start_point), _utils.flatten(end_point), _utils.flatten(normal))

    def add_cylinder(self, base, plane, height1, height2, radius, cap):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_edge_srf(self, objects):
        """

        Creates a surface from 2, 3, or 4 edge curves.

        Parameters

        Objects : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(203, 1, (12, 0), ((8197, 0),), u'AddEdgeSrf', None, _utils.flatten(objects))

    def add_loft_srf(self, objects, start_pt, end_pt, type, style, value, closed):
        """

        * This function will not adjust the seams of closed curves. Use CurveSeam to adjust the seam of closed curves.

        Parameters

        Objects : Required, Array, arrdbl, Array of ?
        StartPt : Optional, Array, arrdbl, Array of ?
        EndPt : Optional, Array, arrdbl, Array of ?
        Type : Optional, Number, int, Integer
        Style : Optional, Number, int, Integer
        Value : Optional, Number, n, Integer
        Closed : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the new surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(567, 1, (12, 0), ((8200, 0), (8197, 0), (8197, 0), (2, 0), (2, 0), (2, 0), (11, 0),), u'AddLoftSrf', None, _utils.flatten(objects), _utils.flatten(start_pt), _utils.flatten(end_pt), type, style, value, closed)

    def add_nurbs_surface(self, point_count, points, knots_u, knots_v, degree, weights):
        """

        Adds a NURBS surface object to the document.

        Parameters

        PointCount : Required, Array, arrdbl, Array of ?
        Points : Required, Array, arrdbl, Array of ?
        KnotsU : Required, Array, arrdbl, Array of ?
        KnotsU : Required, Array, arrdbl, Array of ?
        Degree : Required, Array, arrdbl, Array of ?
        Weights : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(435, 1, (12, 0), ((8197, 0), (8197, 0), (8197, 0), (8197, 0), (8197, 0), (8197, 0),), u'AddNurbsSurface', None, _utils.flatten(point_count), _utils.flatten(points), _utils.flatten(knots_u), _utils.flatten(knots_v), _utils.flatten(degree), _utils.flatten(weights))

    def add_planar_srf(self, objects):
        """

        Creates one or more surfaces from planar curves.

        Parameters

        Objects : Required, Array, arrdbl, Array of ?

        Returns

        Array : An array of strings identifying the new objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(371, 1, (12, 0), ((8197, 0),), u'AddPlanarSrf', None, _utils.flatten(objects))

    def add_plane_surface(self, plane, d_u, d_v):
        """

        Creates a plane surface.

        Parameters

        Plane : Required, Array, arrdbl, Array of ?
        DU : Required, Number, dbl, Double
        DV : Required, Number, dbl, Double

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(648, 1, (12, 0), ((8197, 0), (5, 0), (5, 0),), u'AddPlaneSurface', None, _utils.flatten(plane), d_u, d_v)

    def add_rail_rev_srf(self, profile, rail, axis):
        """

        Create a surface by revolving a profile curve along a rail curve.

        Parameters

        Profile : Required, String, str, String
        Rail : Required, String, str, String
        Axis : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(536, 1, (12, 0), ((8, 0), (8, 0), (8197, 0),), u'AddRailRevSrf', None, profile, rail, _utils.flatten(axis))

    def add_rev_srf(self, profile, axis, start_angle, end_angle):
        """

        Create a surface by revolving a curve around an axis.

        Parameters

        Profile : Required, String, str, String
        Axis : Required, Array, arrdbl, Array of ?
        StartAngle : Optional, Number, dbl, Double
        EndAngle : Optional, Number, dbl, Double

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(535, 1, (12, 0), ((8, 0), (8197, 0), (5, 0), (5, 0),), u'AddRevSrf', None, profile, _utils.flatten(axis), start_angle, end_angle)

    def add_sphere(self, center, plane, radius):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_srf_contour_crvs(self, object, start_point, end_point, plane, interval):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def add_srf_control_pt_grid(self, count, points, degree):
        """

        Creates a surface from a grid of control points.

        Parameters

        Count : Required, Array, arrdbl, Array of ?
        Points : Required, Array, arrdbl, Array of ?
        Degree : Optional, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(294, 1, (12, 0), ((8197, 0), (8197, 0), (8197, 0),), u'AddSrfControlPtGrid', None, _utils.flatten(count), _utils.flatten(points), _utils.flatten(degree))

    def add_srf_pt(self, points):
        """

        Creates a new surface from either 3 or 4 corner points.

        Parameters

        Points : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(204, 1, (12, 0), ((8197, 0),), u'AddSrfPt', None, _utils.flatten(points))

    def add_srf_pt_grid(self, count, points, degree, closed):
        """

        Creates a surface from a grid of points.

        Parameters

        Count : Required, Array, arrdbl, Array of ?
        Points : Required, Array, arrdbl, Array of ?
        Degree : Optional, Array, arrdbl, Array of ?
        Closed : Optional, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(293, 1, (12, 0), ((8197, 0), (8197, 0), (8197, 0), (8197, 0),), u'AddSrfPtGrid', None, _utils.flatten(count), _utils.flatten(points), _utils.flatten(degree), _utils.flatten(closed))

    def add_srf_section_crvs(self, object, plane):
        """

        Adds planar curves resulting from the intersection of a defined cutting plane through a surface or a polysurface. For more information, see the Rhino help file for details on the Section command.

        Parameters

        Object : Required, String, str, String
        Plane : Required, Array, arrdbl, Array of ?

        Returns

        Array : An array of strings identifying the newly created section curves if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(803, 1, (12, 0), ((8, 0), (8197, 0),), u'AddSrfSectionCrvs', None, object, _utils.flatten(plane))

    def add_sweep1(self, rail, shapes, start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg):
        """

        * The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.

        Parameters

        Rail : Required, String, str, String
        Shapes : Required, Array, arrstr, Array of ?
        StartPt : Optional, Array, arrdbl, Array of ?
        EndPt : Optional, Array, arrdbl, Array of ?
        Closed : Optional, Boolean, bln, Boolean
        Style : Optional, Integer, int, Integer
        StyleArg : Optional, Variant, va, Array of ?
        Simplify : Optional, Integer, int, Integer
        SimplifyArg : Optional, Variant, va, Array of ?

        Returns

        Array : The identifiers of the new surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(893, 1, (12, 0), ((8, 0), (8200, 0), (8197, 0), (8197, 0), (11, 0), (2, 0), (12, 0), (2, 0), (12, 0),), u'AddSweep1', None, rail, _utils.flatten(shapes), _utils.flatten(start_pt), _utils.flatten(end_pt), closed, style, style_arg, simplify, simplify_arg)

    def add_sweep2(self, rails, shapes, start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg):
        """

        * The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.

        Parameters

        Rails : Required, String, arrstr, Array of ?
        Shapes : Required, Array, arrstr, Array of ?
        StartPt : Optional, Array, arrdbl, Array of ?
        EndPt : Optional, Array, arrdbl, Array of ?
        Closed : Optional, Boolean, bln, Boolean
        SimpleSweep : Optional, Boolean, bln, Boolean
        MaintainHeight : Optional, Boolean, bln, Boolean
        Simplify : Optional, Integer, int, Integer
        SimplifyArg : Optional, Variant, va, Array of ?

        Returns

        Array : The identifiers of the new surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(894, 1, (12, 0), ((8200, 0), (8200, 0), (8197, 0), (8197, 0), (11, 0), (11, 0), (11, 0), (2, 0), (12, 0),), u'AddSweep2', None, _utils.flatten(rails), _utils.flatten(shapes), _utils.flatten(start_pt), _utils.flatten(end_pt), closed, simple_sweep, maintain_height, simplify, simplify_arg)

    def add_torus(self, base, plane, major_radius, minor_radius, direction):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def boolean_difference(self, input0, input1, delete):
        """

        Performs a Boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file.

        Parameters

        Input0 : Required, Array, arrdbl, Array of ?
        Input1 : Required, Array, arrdbl, Array of ?
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(508, 1, (12, 0), ((8197, 0), (8197, 0), (11, 0),), u'BooleanDifference', None, _utils.flatten(input0), _utils.flatten(input1), delete)

    def boolean_intersection(self, input0, input1, delete):
        """

        Performs a Boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file.

        Parameters

        Input0 : Required, Array, arrdbl, Array of ?
        Input1 : Required, Array, arrdbl, Array of ?
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(507, 1, (12, 0), ((8197, 0), (8197, 0), (11, 0),), u'BooleanIntersection', None, _utils.flatten(input0), _utils.flatten(input1), delete)

    def boolean_union(self, input, delete):
        """

        Performs a Boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file.

        Parameters

        Input : Required, Array, arrdbl, Array of ?
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : An array containing the identifiers of the newly created objects, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(506, 1, (12, 0), ((8197, 0), (11, 0),), u'BooleanUnion', None, _utils.flatten(input), delete)

    def brep_closest_point(self, object, point):
        """

        Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.

        Parameters

        Object : Required, String, str, String
        Point : Required, Array, arrdbl, Array of ?

        Returns

        Array : An array of closest point information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(514, 1, (12, 0), ((8, 0), (8197, 0),), u'BrepClosestPoint', None, object, _utils.flatten(point))

    def cap_planar_holes(self, surface):
        """

        Caps planar holes in a surface or polysurface. For more details, see the Cap command in the Rhino help file.

        Parameters

        Surface : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(701, 1, (12, 0), ((8, 0),), u'CapPlanarHoles', None, surface)

    def duplicate_edge_curves(self, object, select):
        """

        Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.

        Parameters

        Object : Required, String, str, String
        Select : Optional, Boolean, bln, Boolean

        Returns

        Array : An array of strings identifying the newly created curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(657, 1, (12, 0), ((8, 0), (11, 0),), u'DuplicateEdgeCurves', None, object, select)

    def duplicate_surface_border(self, object):
        """

        Creates a curve that duplicates a surface or polysurface border.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of strings identifying the new curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(852, 1, (12, 0), ((8, 0),), u'DuplicateSurfaceBorder', None, object)

    def evaluate_surface(self, object, parameter):
        """

        Evaluates a surface at a U,V parameter.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, arrdbl, Array of ?

        Returns

        Array : A 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(205, 1, (12, 0), ((8, 0), (8197, 0),), u'EvaluateSurface', None, object, _utils.flatten(parameter))

    def explode_polysurfaces(self, object, objects, delete):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def extract_iso_curve(self, object, parameter, dir):
        """

        Extracts isoparametric curves from a surface.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, arrdbl, Array of ?
        Dir : Required, Number, int, Integer

        Returns

        Array : An array of strings identifying the newly created curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(488, 1, (12, 0), ((8, 0), (8197, 0), (2, 0),), u'ExtractIsoCurve', None, object, _utils.flatten(parameter), dir)

    def extrude_curve(self, curve, path):
        """

        Creates a surface by extruding a curve along a path curve.

        Parameters

        Curve : Required, String, str, String
        Path : Required, String, str, String

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(538, 1, (12, 0), ((8, 0), (8, 0),), u'ExtrudeCurve', None, curve, path)

    def extrude_curve_point(self, curve, point):
        """

        Creates a surface by extruding a curve to a point.

        Parameters

        Curve : Required, String, str, String
        Point : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(540, 1, (12, 0), ((8, 0), (8197, 0),), u'ExtrudeCurvePoint', None, curve, _utils.flatten(point))

    def extrude_curve_straight(self, curve, start_point, end_point):
        """

        Creates a surface by extruding a curve straight along two points that define a line.

        Parameters

        Curve : Required, String, str, String
        StartPoint : Required, Array, arrdbl, Array of ?
        EndPoint : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(539, 1, (12, 0), ((8, 0), (8197, 0), (8197, 0),), u'ExtrudeCurveStraight', None, curve, _utils.flatten(start_point), _utils.flatten(end_point))

    def extrude_curve_tapered(self, curve, distance, direction, base_point, angle, corner_type):
        """

        Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.

        Parameters

        Curve : Required, String, str, String
        Distance : Required, Number, dbl, Double
        Direction : Required, Array, arrdbl, Array of ?
        BasePoint : Required, Array, arrdbl, Array of ?
        Angle : Required, Number, dbl, Double
        CornerType : Optional, Number, int, Integer

        Returns

        Array : An array of strings identifying the newly created surface objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(914, 1, (12, 0), ((8, 0), (5, 0), (8197, 0), (8197, 0), (5, 0), (2, 0),), u'ExtrudeCurveTapered', None, curve, distance, _utils.flatten(direction), _utils.flatten(base_point), angle, corner_type)

    def extrude_surface(self, surface, curve, cap):
        """

        Creates a surface or solid by extruding a straight along a path curve.

        Parameters

        Surface : Required, String, str, String
        Curve : Required, String, str, String
        Cap : Optional, Boolean, bln, Boolean

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(541, 1, (12, 0), ((8, 0), (8, 0), (11, 0),), u'ExtrudeSurface', None, surface, curve, cap)

    def fit_surface(self, object, degree, tolerance):
        """

        Reduces the number of surface control points while maintaining the surfaces' same general shape.  Use this function for replacing surface with too many control points.  For more information, see the Rhino help file for the FitSrf command.

        Parameters

        Object : Required, String, str, String
        Degree : Optional, Array, arrdbl, Array of ?
        Tolerance : Optional, Number, dbl, Double

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(815, 1, (12, 0), ((8, 0), (8197, 0), (5, 0),), u'FitSurface', None, object, _utils.flatten(degree), tolerance)

    def flip_surface(self, object, flip):
        """

        Returns or changes the normal direction of a surface. This feature can also be found in Rhino's Dir command.

        Parameters

        Object : Required, String, str, String
        Flip : Optional, Boolean, bln, Boolean

        Returns

        Boolean : If blnFlip is not specified, the current normal orientation if successful.
        Boolean : If blnFlip is specified, the previous normal orientation if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(718, 1, (12, 0), ((8, 0), (11, 0),), u'FlipSurface', None, object, flip)

    def insert_surface_knot(self, object, parameter, direction, symmetrical):
        """

        Inserts a knot into a surface object.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, dbl, Double
        Direction : Required, Number, int, Integer
        Symmetrical : Optional, Boolean, bln, Boolean

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(516, 1, (12, 0), ((8, 0), (5, 0), (2, 0), (11, 0),), u'InsertSurfaceKnot', None, object, parameter, direction, symmetrical)

    def intersect_breps(self, brep1, brep2, tolerance):
        """

        Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.

        Parameters

        Brep1 : Required, String, str, String
        Brep2 : Required, String, str, String
        Tolerance : Optional, Number, dbl, Double

        Returns

        Array : An array of strings identifying the newly created intersection curve and point objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(544, 1, (12, 0), ((8, 0), (8, 0), (5, 0),), u'IntersectBreps', None, brep1, brep2, tolerance)

    def is_brep(self, object):
        """

        Verifies an object is a Brep, or a boundary representation model, object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(206, 1, (12, 0), ((8, 0),), u'IsBrep', None, object)

    def is_brep_manifold(self, object):
        """

        Verifies a polysurface object is manifold.  A polysurface for which every edge is shared by at most two faces is called a manifold.  If a polysurface has at least one edge that is shared by more than two faces, then that polysurface is called non-manifold.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(854, 1, (12, 0), ((8, 0),), u'IsBrepManifold', None, object)

    def is_cone(self, surface):
        """

        Determines if a surface is a portion of a cone.

        Parameters

        Surface : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(885, 1, (12, 0), ((8, 0),), u'IsCone', None, surface)

    def is_cylinder(self, surface):
        """

        Determines if a surface is a portion of a cylinder.

        Parameters

        Surface : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(884, 1, (12, 0), ((8, 0),), u'IsCylinder', None, surface)

    def is_parameter_on_surface(self, object, parameter):
        """

        Verifies that a parameter space point is on a trimmed surface, or not on the trimmed portion of a surface.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, arrdbl, Array of ?

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(879, 1, (12, 0), ((8, 0), (8197, 0),), u'IsParameterOnSurface', None, object, _utils.flatten(parameter))

    def is_plane_surface(self, object):
        """

        Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, a plane surface is not a planar NURBS surface.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(638, 1, (12, 0), ((8, 0),), u'IsPlaneSurface', None, object)

    def is_point_in_surface(self, object, point):
        """

        Verifies that a point is inside a closed surface or polysurface.

        Parameters

        Object : Required, String, str, String
        Point : Required, Array, arrdbl, Array of ?

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(443, 1, (12, 0), ((8, 0), (8197, 0),), u'IsPointInSurface', None, object, _utils.flatten(point))

    def is_point_on_surface(self, object, point):
        """

        Verifies that a point lies on a surface.

        Parameters

        Object : Required, String, str, String
        Point : Required, Array, arrdbl, Array of ?

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(319, 1, (12, 0), ((8, 0), (8197, 0),), u'IsPointOnSurface', None, object, _utils.flatten(point))

    def is_poly_surface(self, object):
        """

        Verifies an object is a polysurface.  Polysurfaces consists of two or more surfaces joined together. If the polysurface fully encloses a volume, it is considered a solid. In some other 3-D programs, this is called a "quilt."

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(207, 1, (12, 0), ((8, 0),), u'IsPolySurface', None, object)

    def is_poly_surface_closed(self, object):
        """

        Verifies a polysurface object is closed.  If the polysurface fully encloses a volume, it is considered a solid.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(208, 1, (12, 0), ((8, 0),), u'IsPolySurfaceClosed', None, object)

    def is_poly_surface_planar(self, object):
        """

        Verifies a polysurface object is planar.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(209, 1, (12, 0), ((8, 0),), u'IsPolySurfacePlanar', None, object)

    def is_sphere(self, surface):
        """

        Determines if a surface is a portion of a sphere.

        Parameters

        Surface : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(883, 1, (12, 0), ((8, 0),), u'IsSphere', None, surface)

    def is_surface(self, object):
        """

        Verifies an object is surface.  Brep objects with only one face are also considered surfaces.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(210, 1, (12, 0), ((8, 0),), u'IsSurface', None, object)

    def is_surface_closed(self, object, direction):
        """

        Verifies a surface object is closed in the specified direction.  If the surface fully encloses a volume, it is considered a solid.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(211, 1, (12, 0), ((8, 0), (2, 0),), u'IsSurfaceClosed', None, object, direction)

    def is_surface_periodic(self, object, direction):
        """

        Verifies a surface object is periodic in the specified direction.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(212, 1, (12, 0), ((8, 0), (2, 0),), u'IsSurfacePeriodic', None, object, direction)

    def is_surface_planar(self, object, tolerance):
        """

        Verifies a surface object is planar.

        Parameters

        Object : Required, String, str, String
        Tolerance : Optional, Number, dbl, Double

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(213, 1, (12, 0), ((8, 0), (5, 0),), u'IsSurfacePlanar', None, object, tolerance)

    def is_surface_rational(self, object):
        """

        Verifies a surface object is rational.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(434, 1, (12, 0), ((8, 0),), u'IsSurfaceRational', None, object)

    def is_surface_singular(self, object, direction):
        """

        Verifies a surface object is singular in the specified direction.  Surfaces are considered singular if a side collapses to a point.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(214, 1, (12, 0), ((8, 0), (2, 0),), u'IsSurfaceSingular', None, object, direction)

    def is_surface_trimmed(self, object):
        """

        Verifies a surface object has been trimmed.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(269, 1, (12, 0), ((8, 0),), u'IsSurfaceTrimmed', None, object)

    def is_torus(self, surface):
        """

        Determines if a surface is a portion of a torus.

        Parameters

        Surface : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(886, 1, (12, 0), ((8, 0),), u'IsTorus', None, surface)

    def join_surfaces(self, object, delete):
        """

        Joins two or more surface or polysurface object together to form one polysurface object.

        Parameters

        Object : Required, Array, str, String
        Delete : Optional, Boolean, bln, Boolean

        Returns

        String : The identifier of the newly created polysurface object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(487, 1, (12, 0), ((8, 0), (11, 0),), u'JoinSurfaces', None, object, delete)

    def make_surface_non_periodic(self, object, direction, delete):
        """

        Makes a periodic surface non-periodic. Non-periodic surfaces can develop kinks when deformed.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer
        Delete : Optional, Boolean, bln, Boolean

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(926, 1, (12, 0), ((8, 0), (2, 0), (11, 0),), u'MakeSurfaceNonPeriodic', None, object, direction, delete)

    def make_surface_periodic(self, object, direction, delete):
        """

        Makes an existing surface a periodic NURBS surface.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer
        Delete : Optional, Boolean, bln, Boolean

        Returns

        String : If blnDelete is False, the identifier of the new object if successful.
        String : If blnDelete is True, the identifier of the modified object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(445, 1, (12, 0), ((8, 0), (2, 0), (11, 0),), u'MakeSurfacePeriodic', None, object, direction, delete)

    def offset_surface(self, object, distance):
        """

        Offsets a surface by a distance. The offset surface will be added to Rhino.

        Parameters

        Object : Required, String, str, String
        Distance : Required, Number, dbl, Double

        Returns

        String : The identifier of the new object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(635, 1, (12, 0), ((8, 0), (5, 0),), u'OffsetSurface', None, object, distance)

    def pull_curve(self, surface, curve, delete):
        """

        Pulls a curve object to a surface object. For more information, see the Rhino help file for information on the Pull command.

        Parameters

        Surface : Required, String, str, String
        Curve : Required, String, str, String
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : The identifiers of the new curve objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(493, 1, (12, 0), ((8, 0), (8, 0), (11, 0),), u'PullCurve', None, surface, curve, delete)

    def rebuild_surface(self, object, degree, point_count):
        """

        Rebuilds a surface to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.

        Parameters

        Object : Required, String, str, String
        Degree : Optional, Array, arrdbl, Array of ?
        PointCount : Optional, Array, arrdbl, Array of ?

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(816, 1, (12, 0), ((8, 0), (8197, 0), (8197, 0),), u'RebuildSurface', None, object, _utils.flatten(degree), _utils.flatten(point_count))

    def remove_surface_knot(self, object, parameter, direction):
        """

        Deletes a knot-line from a surface object.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, dbl, Double
        Direction : Required, Number, int, Integer

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(917, 1, (12, 0), ((8, 0), (5, 0), (2, 0),), u'RemoveSurfaceKnot', None, object, parameter, direction)

    def reverse_surface(self, object, direction):
        """

        To reverse the normal direction of a surface, use the FlipSurface method.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(927, 1, (12, 0), ((8, 0), (2, 0),), u'ReverseSurface', None, object, direction)

    def short_path(self, surface, start, end):
        """

        Creates the shortest possible curve (geodesic) between two points on a surface. For more details, see the ShortPath command in the Rhino help file.

        Parameters

        Surface : Required, String, str, String
        Start : Required, Array, arrdbl, Array of ?
        End : Required, Array, arrdbl, Array of ?

        Returns

        String : The identifier of the new curve object if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(702, 1, (12, 0), ((8, 0), (8197, 0), (8197, 0),), u'ShortPath', None, surface, _utils.flatten(start), _utils.flatten(end))

    def shrink_trimmed_surface(self, surface):
        """

        Shrinks the underlying untrimmed surfaces near to trimming boundaries. For more details, see the ShrinkTrimmedSrf command in the Rhino help file.

        Parameters

        Surface : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(700, 1, (12, 0), ((8, 0),), u'ShrinkTrimmedSurface', None, surface)

    def split_brep(self, brep, cutter, delete):
        """

        Splits a brep.  A brep can be either a surface with a single face or a polysurface.

        Parameters

        Brep : Required, String, str, String
        Cutter : Required, String, str, String
        Delete : Optional, Boolean, bln, Boolean

        Returns

        Array : The identifiers of the new brep objects if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(637, 1, (12, 0), ((8, 0), (8, 0), (11, 0),), u'SplitBrep', None, brep, cutter, delete)

    def surface_area(self, object):
        """

        Calculates the area of a surface or polysurface object. The results are based on the current drawing units.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of area information if successful.  The array will contain the following information:
        Number : The area.
        Number : The absolute (+/-) error bound for the area.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(382, 1, (12, 0), ((8, 0),), u'SurfaceArea', None, object)

    def surface_area_centroid(self, object):
        """

        Calculates the area centroid of a surface or polysurface object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of area centroid information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(384, 1, (12, 0), ((8, 0),), u'SurfaceAreaCentroid', None, object)

    def surface_area_moments(self, object):
        """

        Calculates the area moments of inertia of a surface or polysurface object.  For more information, see the Rhino help file for "Mass Properties Calculation Details."

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of area moments of inertia information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(386, 1, (12, 0), ((8, 0),), u'SurfaceAreaMoments', None, object)

    def surface_closest_point(self, object, point):
        """

        Returns the UV parameter of the point on a surface that is closest to a test point.

        Parameters

        Object : Required, String, str, String
        Point : Required, Array, arrdbl, Array of ?

        Returns

        Array : An array containing the U,V parameters of the closest point on the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(215, 1, (12, 0), ((8, 0), (8197, 0),), u'SurfaceClosestPoint', None, object, _utils.flatten(point))

    def surface_cone(self, surface):
        """

        Returns the definition of a cone surface.

        Parameters

        Surface : Required, String, str, String

        Returns

        Array : An array containing the definition of the cone if successful.  The elements of the array are as follows:
        Array : The plane of the cone.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
        Number : The height of the cone.
        Number : The radius of the cone.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(889, 1, (12, 0), ((8, 0),), u'SurfaceCone', None, surface)

    def surface_contour_points(self, object, start_point, end_point, interval, angle):
        """

        Returns the vertices of the polyline curves generated by contouring a surface or polysurface object.

        Parameters

        Object : Required, String, str, String
        StartPoint : Required, Array, arrdbl, Array of ?
        EndPoint : Required, Array, arrdbl, Array of ?
        Interval : Optional, Number, dbl, Double
        Angle : Optional, Number, dbl, Double

        Returns

        Array : An array of 3-D point arrays, one for each contour, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(79, 1, (12, 0), ((8, 0), (8197, 0), (8197, 0), (5, 0), (5, 0),), u'SurfaceContourPoints', None, object, _utils.flatten(start_point), _utils.flatten(end_point), interval, angle)

    def surface_curvature(self, object, parameter):
        """

        Returns the curvature of a surface at a U,V parameter.  See the Rhino help file for details on surface curvature.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, arrdbl, Array of ?

        Returns

        Array : An array of curvature information if successful.  The array will contain the following information:
        Number : Maximum principal curvature.
        Number : Minimum principal curvature.
        Number : Gaussian curvature.
        Number : Mean curvature.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(378, 1, (12, 0), ((8, 0), (8197, 0),), u'SurfaceCurvature', None, object, _utils.flatten(parameter))

    def surface_curvature_analysis(self, object):
        """

        Returns the curvature of a surface.  See the Rhino help file for details on surface curvature analysis.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of curvature information if successful.  The array will contain the following information:
        Array : An array containing three values: the min Gaussian curvature, the max Gaussian curvature, and the infinity status.
        Array : An array containing three values: the min unsigned mean curvature, the max unsigned mean curvature, and the infinity comparison.
        Array : An array containing three values: the min maximum unsigned radius of curvature, the max maximum unsigned radius of curvature, and the infinity comparison.
        Array : An array containing three values: the min minimum unsigned radius of curvature, the max minimum unsigned radius of curvature, and the infinity comparison.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(632, 1, (12, 0), ((8, 0),), u'SurfaceCurvatureAnalysis', None, object)

    def surface_cylinder(self, surface):
        """

        Returns the definition of a cylinder surface.

        Parameters

        Surface : Required, String, str, String

        Returns

        Array : An array containing the definition of the cylinder if successful.  The elements of the array are as follows:
        Array : The base plane of the cylinder.
        Number : The height of the cylinder.
        Number : The radius of the cylinder.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(888, 1, (12, 0), ((8, 0),), u'SurfaceCylinder', None, surface)

    def surface_degree(self, object, direction):
        """

        Returns the degree of a  surface object in the specified direction.

        Parameters

        Object : Required, String, str, String
        Direction : Optional, Number, int, Integer

        Returns

        Array : If intDirection is not specified, or intDirection is set to 2, then the degree in both the U and V directions is returned.
        Number : If intDirection is specified, and intDirection is set to either 0 or 1, then the degree in either the U or V direction is returned.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(216, 1, (12, 0), ((8, 0), (2, 0),), u'SurfaceDegree', None, object, direction)

    def surface_domain(self, object, direction):
        """

        Returns the domain of a  surface object in the specified direction.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer

        Returns

        Array : An array containing the domain interval in the specified direction if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(217, 1, (12, 0), ((8, 0), (2, 0),), u'SurfaceDomain', None, object, direction)

    def surface_edit_points(self, object, return_parameters, return_all):
        """

        Returns the edit, or Greville, points of a surface object.  For each surface control point, there is a corresponding edit point.

        Parameters

        Object : Required, String, str, String
        ReturnParameters : Optional, Boolean, bln, Boolean
        ReturnAll : Optional, Boolean, bln, Boolean

        Returns

        Array : If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.
        Array : If blnReturnParameters is True, then an array of U,V parameter values if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(427, 1, (12, 0), ((8, 0), (11, 0), (11, 0),), u'SurfaceEditPoints', None, object, return_parameters, return_all)

    def surface_evaluate(self, object, parameter, derivative):
        """

        A general purpose surface evaluator.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, arrdbl, Array of ?
        Derivative : Required, Number, int, Integer

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

        return self._ApplyTypes_(583, 1, (12, 0), ((8, 0), (8197, 0), (2, 0),), u'SurfaceEvaluate', None, object, _utils.flatten(parameter), derivative)

    def surface_frame(self, object, parameter):
        """

        Returns a plane based on the normal, u, and v directions at a given surface U,V parameter.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, arrdbl, Array of ?

        Returns

        Array : The plane at the specified parameter if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(623, 1, (12, 0), ((8, 0), (8197, 0),), u'SurfaceFrame', None, object, _utils.flatten(parameter))

    def surface_isocurve_density(self, object, density):
        """

        Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface.

        Parameters

        Object : Required, String, str, String
        Density : Optional, Number, int, Integer

        Returns

        Number : The intDensity is not specified, then the current isocurve density if successful.
        Number : The intDensity is specified, then the previous isocurve density if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(361, 1, (12, 0), ((8, 0), (2, 0),), u'SurfaceIsocurveDensity', None, object, density)

    def surface_knot_count(self, object):
        """

        Returns the knot count of a surface object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : The number of knots in the U and V directions if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(431, 1, (12, 0), ((8, 0),), u'SurfaceKnotCount', None, object)

    def surface_knots(self, object):
        """

        Returns the knots, or knot vector, of a surface object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : The knot values of the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(432, 1, (12, 0), ((8, 0),), u'SurfaceKnots', None, object)

    def surface_normal(self, object, parameter):
        """

        Returns a 3-D vector that is the normal to a surface at a parameter.

        Parameters

        Object : Required, String, str, String
        Parameter : Required, Array, arrdbl, Array of ?

        Returns

        Array : A 3-D vector if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(362, 1, (12, 0), ((8, 0), (8197, 0),), u'SurfaceNormal', None, object, _utils.flatten(parameter))

    def surface_point_count(self, object):
        """

        Returns the control points count of a surface object.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : The number of control points in the U and V directions if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(218, 1, (12, 0), ((8, 0),), u'SurfacePointCount', None, object)

    def surface_points(self, object, return_all):
        """

        Returns the control points, or control vertices, of a surface object.

        Parameters

        Object : Required, String, str, String
        ReturnAll : Optional, Boolean, bln, Boolean

        Returns

        Array : The control points of the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(372, 1, (12, 0), ((8, 0), (11, 0),), u'SurfacePoints', None, object, return_all)

    def surface_principal_curvature(self, object, point):
        """

        Adds curvature curves at the evaluated point on a surface. For more information, see the Rhino help file for the Curvature command.

        Parameters

        Object : Required, String, str, String
        Point : Required, Array, arrdbl, Array of ?

        Returns

        Array : An array of two strings that identify the Maximum and Minimum principal curvature curves, respectively, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(717, 1, (12, 0), ((8, 0), (8197, 0),), u'SurfacePrincipalCurvature', None, object, _utils.flatten(point))

    def surface_seam(self, object, direction, parameter):
        """

        Changes the seam of a closed surface. For more information, see the Rhino help file for the SrfSeam command.

        Parameters

        Object : Required, String, str, String
        Direction : Required, Number, int, Integer
        Parameter : Required, Number, dbl, Double

        Returns

        Boolean : True of False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(804, 1, (12, 0), ((8, 0), (2, 0), (5, 0),), u'SurfaceSeam', None, object, direction, parameter)

    def surface_sphere(self, surface):
        """

        Returns the definition of a sphere surface.

        Parameters

        Surface : Required, String, str, String

        Returns

        Array : An array containing the definition of the sphere if successful.  The elements of the array are as follows:
        Array : The equatorial plane of the sphere.  The origin of the plane will be the center point of the sphere.
        Number : The radius of the sphere.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(887, 1, (12, 0), ((8, 0),), u'SurfaceSphere', None, surface)

    def surface_surface_intersection(self, surface_a, surface_b, tolerance, create):
        """

        Calculates the intersection of a surface object with another surface object. Note, this function works on untrimmed surfaces.

        Parameters

        SurfaceA : Required, String, str, String
        SurfaceB : Required, String, str, String
        Tolerance : Optional, Number, dbl, Double
        Create : Optional, Boolean, bln, Boolean

        Returns

        Array : If blnCreate is not specified or is equal to False, an array numbers identifying the intersection event type if successful.  The array will contain one or more of the following intersection event types:
        Array : If blnCreate is specified and is equal to True, a two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:
        Number : The intersection event type.  See the above table for details.
        String : The identifier of the intersection curve or point object that was created.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(484, 1, (12, 0), ((8, 0), (8, 0), (5, 0), (11, 0),), u'SurfaceSurfaceIntersection', None, surface_a, surface_b, tolerance, create)

    def surface_torus(self, surface):
        """

        Returns the definition of a torus surface.

        Parameters

        Surface : Required, String, str, String

        Returns

        Array : An array containing the definition of the torus if successful.  The elements of the array are as follows:
        Array : The base plane of the torus.
        Number : The major radius of the torus.
        Number : The minor radius of the torus.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(890, 1, (12, 0), ((8, 0),), u'SurfaceTorus', None, surface)

    def surface_volume(self, object):
        """

        Calculates the volume of closed surface or polysurface objects.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of volume information if successful.  The array will contain the following information:
        Number : The volume.
        Number : The absolute (+/-) error bound for the volume.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(383, 1, (12, 0), ((8, 0),), u'SurfaceVolume', None, object)

    def surface_volume_centroid(self, object):
        """

        Calculates the volume centroid of closed surface or polysurface objects.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of volume centroid information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(385, 1, (12, 0), ((8, 0),), u'SurfaceVolumeCentroid', None, object)

    def surface_volume_moments(self, object):
        """

        Calculates the volume moments of inertia of closed surface or polysurface objects.  For more information, see the Rhino help file for "Mass Properties Calculation Details."

        Parameters

        Object : Required, String, str, String

        Returns

        Array : An array of volume moments of inertia information if successful.  The array will contain the following information:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(387, 1, (12, 0), ((8, 0),), u'SurfaceVolumeMoments', None, object)

    def surface_weights(self, object):
        """

        Returns an array of weight values that are assigned to the control points of a surface.  The number of weights returned will be equal to the number of control points in the U and V directions.

        Parameters

        Object : Required, String, str, String

        Returns

        Array : The weight values of the surface if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(433, 1, (12, 0), ((8, 0),), u'SurfaceWeights', None, object)

