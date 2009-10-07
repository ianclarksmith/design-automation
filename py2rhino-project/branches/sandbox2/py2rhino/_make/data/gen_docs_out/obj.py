

class Arc():

        create = """
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
        create_by_3pt = """
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
        create_by_fillet = """
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


class Box():

        create = """
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


class Circle():

        create = """
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
        create_by_3pt = """
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


class Cone():

        create = """
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
        create_by_plane = """
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
        This function calls the Rhinoscript function: AddCone

        """


class Cylinder():

        create = """
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
        create_by_plane = """
        Factory method:
        Adds a cylinder-shaped polysurface to the document.

        Parameters
        ==========
        base_plane  (List of float, Required) - The 3-D base point of the cylinder.
        height  (float, Required) - The 3-D height point of the cylinder.  The height point defines the height and direction of the cylinder.
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


class Ellipse():

        create = """
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
        create_by_3pt = """
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


class EllipticalArc():

    pass


class Line():

        create = """
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


class Mesh():

        create = """
        Factory method:
        Adds a mesh object to the document.

        Parameters
        ==========
        vertices  (List of float, Required) - An list of 3-D points defining the vertices of the mesh.
        faces  (List of integer, Required) - An list containing lists of four numbers that define the vertex indices for each face of the mesh. If the third and forth vertex indices of a face are identical, a triangular face will be created. Otherwise a quad face will be created.
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
        create_by_polyline = """
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


class NurbsCurve():

        create_by_pnts = """
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
        create_interp_crv_on_srf = """
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
        create_interp_crv_on_srf_uv = """
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
        create_interp_crv_ed = True
        create_interp_crv = """
        Factory method:
        Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.

        Parameters
        ==========
        points  (List of float, Required) - An list containing 3-D points to interpolate.  For periodic curves, if the final point is a duplicate of the initial point, it is ignored. Note, the number of control points must be >= (intDegree+1).
        degree  (integer, Optional) - The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.  For intKnotStyle = 4 or 5, the degree must be odd.
        knot_style  (integer, Optional) - The knot style to use, and whether the curve should be periodic.  If omitted, uniform knots (0) are created. The possible knot simplify methods are listed in the table for knot_style.
        start_tan  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the beginning of the curve. If the curve is to periodic, this argument must be omitted.
        end_tan  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the end of the curve. If the curve is to periodic, this argument must be omitted.

        Table: knot_style
        Value, Description
        0, Uniform knots.  Parameter spacing between consecutive knots is 1.0.
        1, Chord length spacing.  Requires dblDegree = 3 with arrCV1 and arrCVn1 specified.
        2, Sqrt (chord length).  Requires dblDegree = 3 with arrCV1 and arrCVn1 specified.
        3, Periodic with uniform spacing.
        4, Periodic with chord length spacing.  Requires an odd degree value.
        5, Periodic with sqrt (chord length) spacing.  Requires an odd degree value.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddInterpCurve

        """
        create_interp_crv_ex_ed = True
        create_interp_crv_ex = """
        Factory method:
        Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.

        Parameters
        ==========
        points  (List of float, Required) - An list containing 3-D points to interpolate. Note, the number of control points must be >= (intDegree+1).
        degree  (integer, Optional) - The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.
        knot_style  (integer, Optional) - The knot style to use. If omitted, a knot style = 0 is used. The knot style determines how an interpolated curve will be parameterized. The possible knot simplify methods are listed in the table for knot_style.
		sharp  (boolean, Optional) - If True, when you create a closed curve, it will have a kink at the start/end point. If False (default), a smooth closure will be created.
        start_tangent  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the beginning of the curve.
        end_tangent  (List of float, Optional) - A 3-D vector that specifies a tangency condition at the end of the curve.
        
        Table: knot_style
        Value, Description
		0, Uniform.  The knot spacing is always 1 and is not based on the physical spacing of points.
		1, Chord. The spacing between the points is used for the knot spacing
		2, Square Root Chord. The square root of the spacing between points is used for the knot spacing.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddInterpCurveEx

        """
        create = """
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
        create_by_srf_contour = """
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
        create_by_srf_section = """
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
        create_by_srf_edge = """
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
        create_by_srf_border = """
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
        create_by_srf_iso_curve = """
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
        create_by_fit = """
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
        create_by_projection_to_mesh = """
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
        create_by_projection_to_srf = """
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
        create_by_srf_pull = """
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
        create_by_srf_short_path = """
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
        create_by_srf_principal_curvature = """
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


class NurbsSurface():

        create_by_cut_plane = """
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
        create_by_edge = """
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
        create_by_loft_ed = True
        create_by_loft = """
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
        srf_type  (integer, Optional) - The type of loft. The default loft type is Normal (0). The possible loft types are listed in the table for srf_type.
		style  (integer, Optional) - The simplify method of the loft. The default value is None (0). The possible loft simplify methods are listed in the table for style.
		value  (integer, Optional) - A value based on the specified intStyle. If intStyle=1 (Rebuild), then nValue is the number of control point used to rebuild. If intstyle=1 is specified and this argument is omitted, then curves will be rebuilt using 10 control points. If intStyle=2 (Refit), then nValue is the tolerance used to rebuild. If intstyle=2 is specified and this argument is omitted, then the document's absolute tolerance us used for refitting.
        closed  (boolean, Optional) - Creates a closed surface, continuing the surface past the last curve around to the first curve. Available when you have selected three shape curves. The default value is not to create a closed surface (False).
        
		Table: srf_type
		Value, Description
		0, Normal. Uses chord-length parameterization in the loft direction.
		1, Loose. The surface is allowed to move away from the original curves to make a smoother surface. The surface control points are created at the same locations as the control points of the loft input curves.
		2, Straight. The sections between the curves are straight. This is also known as a ruled surface.
		3, Tight. The surface sticks closely to the original curves. Uses square root of chord-length parameterization in the loft direction.
		4, Developable. Creates a separate developable surface or polysurface from each pair of curves.
		
		Table: style
		Value, Description
		0, None. Does not simplify.
		1, Rebuild. Rebuilds the shape curves before lofting.
		2, Refit. Refits the shape curves to a specified tolerance.

		

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddLoftSrf

        """
        create = """
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
        create_by_planar_crv = """
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
        create_by_rail_rev = """
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
        create_by_rev = """
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
        create_by_control_pnt_grid = """
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
        create_by_corner_pnts = """
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
        create_by_pnt_grid = """
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
        create_by_sweep_1 = """
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
        create_by_sweep_2 = """
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
        create_by_extrude_crv = """
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
        create_by_extrude_crv_pnt = """
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
        create_by_extrude_crv_straight = """
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
        create_by_extrude_crv_tapered_ed = True
        create_by_extrude_crv_tapered = """
        Factory method:
        Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.

        Parameters
        ==========
        curve  (curve object, Required) - The identifier of the curve object to extrude.
        distance  (float, Required) - The extrusion distance.
        direction  (List of float, Required) - A 3-D vector that specifies the extrusion direction.
        base_point  (List of float, Required) - A 3-D point that specifies the base point of the extrusion.
        angle  (float, Required) - The angle of the extrusion.
        corner_type  (integer, Optional) - The corner type of the extrusion are listed in the table for corner_type.
        
        Table: corner_type
		Value, Description
		0 (Default), No corner
		1, Sharp - Offsets and extends curves with a straight line until they intersect.
		2, Round - Offsets and fillets curves with an arc of radius equal to the offset distance.
		3, Smooth - Offsets and connects curves with a smooth (G1 continuity) curve.
		4, Chamfer - Offsets and connects curves with a straight line between their endpoints.

        Returns
        =======
        list of objects - The new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtrudeCurveTapered

        """
        create_by_fit = """
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


class PlanarMesh():

        create_by_crv = """
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


class PlaneSurface():

        create = """
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


class PolyCurve():

        create = """
        Factory method:
        Joins two or more curve object together to form one or more curves or polycurves.

        Parameters
        ==========
        curves  (list of curve object, Required) - A list of curve objects to join.
        delete  (boolean, Optional) - Delete input objects after joining.  The default is not to delete objects (False).

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: JoinCurves

        """


class PolySurface():

        create_by_srf_extrude = """
        Factory method:
        Creates a surface or solid by extruding a straight along a path curve.

        Parameters
        ==========
        surface  (surface object, Required) - The identifier of the surface object to extrude.
        curve  (curve object, Required) - The identifier of the path curve.
        cap  (boolean, Optional) - Extrusion is capped at both ends to make a closed polysurface. The default value is True.

        Returns
        =======
        object - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtrudeSurface

        """
        create_by_srf_join = """
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


class Polyline():

        create = """
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
        create_by_crv = """
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
        create_by_mesh_border = """
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
        create_by_mesh_pull = """
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


class Sphere():

        create = """
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
        create_by_plane = """
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
        This function calls the Rhinoscript function: AddSphere

        """


class Torus():

        create = """
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
        create_by_plane = """
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
        This function calls the Rhinoscript function: AddTorus

        """


class _ArcDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used. The possible style elements are listed in the table for style.
        
        Table: style
		Value, Description
		0, None
		1, Sharp (Default)
		2, Round
		3, Smooth
		4, Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_split = """
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
        copy_by_trim = """
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


class _ArcModf():

        close = """
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
        extend_ed = True
        extend = """
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible curve types are listed in the table for crv_type.
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side.
        objects  (list of array_of _ObjectRoot, Required) - The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.
        
        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1,  Extend from the end of the curve.
				

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurve

        """
        extend_length_ed = True
        extend_length = """
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible style types are listed in the table for crv_type.
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side.        
        length  (float, Required) - The distance to extend the curve.

        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
		2, Extend from both the start and the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurveLength

        """
        extend_pnt_ed = True
        extend_pnt = """
        Extends a non-closed curve object by smooth extension to a point.

        Parameters
        ==========
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side.  
		point  (List of float, Required) - The 3-D point.
		
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurvePoint

        """


class _ArcProp():

        angle_ed = True
        angle = """
        Returns the angle of an arc curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        float - The angle in degrees if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ArcAngle

        """
        center_pnt = """
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
        mid_pnt = """
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
        radius_ed = True
        radius = """
        Returns the radius of an arc curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        float - The radius of the arc if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ArcRadius

        """


class _BoxDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """


class _CircleDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used. The possible style types are listed in the table for style.
		
		Table: style
		Value, Description
		0, None
		1, Sharp (Default)
		2, Round
		3, Smooth
		4, Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_split = """
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
        copy_by_trim = """
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


class _CircleProp():

        center_pnt = """
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
        circumference_ed = True
        circumference = """
        Returns the circumference of a circle curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        float - The circumference of the circle if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CircleCircumference

        """
        radius_ed = True
        radius = """
        Returns the radius of a circle curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        float - The radius of the circle if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CircleRadius

        """


class _ConeDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """


class _ConeProp():

        cone_def = True
        cone_def = """
        Returns the definition of a cone surface.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing the definition of the cone if successful.  The elements of the list are as follows:
        list - The plane of the cone.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
        float - The height of the cone.
        float - The radius of the cone.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceCone

        """


class _CurveRoot():

    pass


class _CurveRootDefm():

        box_morph = """
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
        shear = """
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
        transform_ed = True
        transform = """
        Moves, scales, or rotates an object given a 4x4 transformation matrix. The matrix acts on the left. The following table demonstrates the transformation matrix configuration:
		1,0,0,dX
		0,1,0,dY
		0,0,1,dZ
		0,0,0,1

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


class _CurveRootEval():

        curvature = True
        curvature = """
        Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.

        Returns
        =======
        list - A list of curvature information if successful.  The list will contain the following information:
        float - Radius of curvature
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveCurvature

        """
        derivatives = """
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
        frame = """
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
        perp_frame = """
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
        tangent = """
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
        evaluate = """
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


class _CurveRootFunc():

        crv_arc_length_pnt = """
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
        closest_pnt_ed = True
        closest_pnt = """
        Returns the parameter of the point on a curve that is closest to a test point.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        float - The parameter of the closest point on the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveClosestPoint

        """
        contour_pnts = """
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
        crv_intersection = """
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
        deviation = """
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
        directions_match = """
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
        radius_ed = True
        radius = """
        Returns the radius of curvature at a point on a curve.

        Parameters
        ==========
        point  (List of float, Required) - The test, or sampling, point.

        Returns
        =======
        float - The radius of curvature at the point on the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveRadius

        """
        srf_intersection = """
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
        divide_crv = """
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
        divide_crv_equidistant = """
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
        divide_crv_length = """
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
        line_fit_from_pnts = """
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
        make_non_periodic = """
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
        make_periodic = """
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


class _CurveRootFuncClsd():

        area_ed = True
        area = """
        Returns that area of closed planar curves. The results are based on the current drawing units.

        Parameters
        ==========
        objects  (list of array_of _ObjectRoot, Required) - An list of strings containing the identifiers of one or more closed, planar curve objects.

        Returns
        =======
        list - A list of area information if successful.  The list will contain the following information:
        float - The area. If more than one curve was specified, the value will be the cumulative area.
        float - The absolute (+/-) error bound for the area.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveArea

        """
        area_centroid = """
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
        boolean_difference = """
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
        boolean_intersection = """
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
        boolean_union = """
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
        containment_ed=True
        containment = """
        Determines the relationship between the regions bounded by two coplanar simple closed curves.

        Parameters
        ==========
        curve  (curve object, Required) - The object identifier of the second planar, closed curve.
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are listed in the table for plane.
        tolerance  (float, Optional) - The tolerance.  If omitted, the current document absolute tolerance is used.
		
		Table: plane
		Element,Type, Description
		0, Array, Required.  The construction plane's origin (3-D point).
		1, Array, Required.  The construction plane's X axis direction (3-D vector).
		2, Array, Required.  The construction plane's Y axis direction (3-D vector).
		3, Array, Optional.  The construction plane's Z axis direction (3-D vector). 

        Returns
        =======
        number - A number identifying the relationship if successful.  The possible values are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlanarClosedCurveContainment

        """
        pnt_inside_ed = True
        pnt_inside = """
        Determines if a point is inside of a closed curve, on  a closed curve, or outside of a closed curve.

        Parameters
        ==========
        point  (List of float, Required) - A 3-D point to test.
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are for plane.
		tolerance  (float, Optional) - The tolerance.  If omitted, the current document absolute tolerance is used.

		Table: plame
		Element,Type,Description
		0, Array, Required.  The construction plane's origin (3-D point).
		1, Array, Required.  The construction plane's X axis direction (3-D vector).
		2, Array, Required.  The construction plane's Y axis direction (3-D vector).
		3, Array, Optional.  The construction plane's Z axis direction (3-D vector). 

        Returns
        =======
        number - A number identifying the result if successful.  The possible values are as follows:
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PointInPlanarClosedCurve

        """


class _CurveRootModf():

        seam = """
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
        fair = """
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
        insert_knot = """
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
        rebuild = """
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
        remove_knot = """
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
        reverse = """
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
        simplify_ed = True
        simplify = """
        Simplify curve replaces the curve with a geometrically equivalent polycurve. The polycurve will have the following properties:
		1.  All the polycurve segments are lines, polylines, arcs, or NURBS curves.
		2.  The NURBS curves segments do not have fully multiple interior knots.
		3.  Rational NURBS curves do not have constant weights.
		4.  Any segment for which IsCurveLinear or IsArc is True is a line, polyline segment, or an arc.
		5.  Adjacent co-linear or co-circular segments are combined.
		6.  Segments that meet with G1-continuity have there ends tuned up so that they meet with G1-continuity to within machine precision.

        Parameters
        ==========
        flags  (integer, Optional) - The simplification methods to use. By default, all methods are used (intFlags = 0). The possible options are listed in the table for flags.
        
        Table: flags
		Value, Description
		0, Use all methods.
		1, Do not split NURBS curves at fully multiple knots.
		2, Do not replace segments with IsCurveLinear = True with line curves.
		4, Do not replace segments with IsArc = True with arc curves.
		8, Do not replace rational NURBS curves with constant denominator with an equivalent non-rational NURBS curve.
		16, Do not adjust curves at G1-joins.
		32, Do not merge adjacent co-linear lines or co-circular arcs or combine consecutive line segments into a polyline.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SimplifyCurve

        """


class _CurveRootProp():

        degree_ed = True
        degree = """
        Returns the degree of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        float - The degree of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDegree

        """
        dim_ed = True
        dim = """
        Returns the dimension of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        float - The dimension of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDim

        """
        discontinuity_ed = True
        discontinuity = """
        Search for a derivatitive, tangent, or curvature discontinuity in a curve object.

        Parameters
        ==========
        style  (integer, Required) - The type of continuity to test for.  The types of continuity are listed in the table for style.
        
        Table: style
		Value, Description
		1, C0 - Continuous function
		2, C1 - Continuous first derivative
		3, C2 - Continuous first and second derivative
		4, G1 - Continuous unit tangent
		5, G2 - Continuous unit tangent and curvature

        Returns
        =======
        list - A list of 3-D points where the curve is discontinuous if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDiscontinuity

        """
        domain = """
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
        edit_pnts = """
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
        end_pnt = """
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
        knot_count_ed = True
        knot_count = """
        Returns the knot count of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of knots if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveKnotCount

        """
        knots = """
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
        length_ed = True
        length = """
        Returns the length of a curve object.

        Parameters
        ==========
        sub_domain  (List of integer, Optional) - An list of two numbers identifying the sub-domain of the curve on which the calculation will be performed.  The two parameters (sub-domain) must be non-decreasing.  If omitted, the length of the entire curve is returned.

        Returns
        =======
        float - The length of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveLength

        """
        mid_pnt = """
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
        normal = """
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
        plane = """
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
        control_pnt_count_ed = True
        control_pnt_count = """
        Returns the control points count of a curve object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of control points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurvePointCount

        """
        control_pnts = """
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
        start_pnt = """
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
        weights = """
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


class _CurveRootPropClsd():

    pass


class _CurveRootPropOorC():

    pass


class _CurveRootPropOpen():

    pass


class _CurveRootStat():
        
        arrowsPed=True
        arrows = """
        Enables or disabled a curve object's annotation arrows.

        Parameters
        ==========
        style  (integer, Optional) - The style of annotation arrows to be displayed.  The styles are listed in the table for style.
        
        Table: style
		Value, Description
		0, No annotation arrows
		1, Display an annotation arrow at the starting point of the curve
		2, Display an annotation arrow at the ending point of the curve
		3, Display an annotation arrow at both the starting point and the ending point of the curve

        Returns
        =======
        int - If style is not specified, the current annotation arrow style if successful.
        int - If style is specified, the previous annotation arrow style if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveArrows

        """


class _CurveRootTest():

        is_closable = """
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
        is_closed = """
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
        in_plane_ed=True
        in_plane = """
        Test a curve to see if it lies in a specific plane.

        Parameters
        ==========
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are listed on the table plane:

		Table: plane
		Element, Type, Description
		0, Array, Required.  The construction plane's origin (3-D point).
		1, Array, Required.  The construction plane's X axis direction (3-D vector).
		2, Array, Required.  The construction plane's Y axis direction (3-D vector).
		3, Array, Optional.  The construction plane's Z axis direction (3-D vector). 

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCurveInPlane

        """
        is_linear = """
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
        is_periodic = """
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
        is_planar = """
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
        is_rational = """
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
        is_pnt_on_crv = """
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
        planar_crv_collision_ed = True
        planar_crv_collision = """
        Determines if two coplanar curves intersect.

        Parameters
        ==========
        curve  (curve object, Required) - The object identifier of the second planar curve.
        plane  (List of float, Optional) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane list are listed in the table for plane.
        tolerance  (float, Optional) - The tolerance.  If omitted, the current document absolute tolerance is used.
		
		Table: plane
		Element, Type, Description
		0, Array, Required.  The construction plane's origin (3-D point).
		1, Array, Required.  The construction plane's X axis direction (3-D vector).
		2, Array, Required.  The construction plane's Y axis direction (3-D vector).
		3, Array, Optional.  The construction plane's Z axis direction (3-D vector). 

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlanarCurveCollision

        """


class _CurveRootType():

        is_arc = """
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
        is_circle = """
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
        is_crv = """
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
        is_ellipse = """
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
        is_line = """
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
        is_poly_crv = """
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
        is_polyline = """
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


class _CylinderDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """


class _CylinderProp():

        cylinder_def_ed = True 
        cylinder_def = """
        Returns the definition of a cylinder surface.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list containing the definition of the cylinder if successful.  The elements of the list are as follows:
        list - The base plane of the cylinder.
        float - The height of the cylinder.
        float - The radius of the cylinder.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceCylinder

        """


class _EllipseDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used. The possible style types are listed in the table for style.  
		
		Table: style
		Value, Description
		0, None
		1, Sharp (Default)
		2, Round
		3, Smooth
		4, Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_split = """
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
        copy_by_trim = """
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


class _EllipseProp():

        center_pnt = """
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
        quad_pnts = """
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


class _EllipticalArcDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used. The possible style types are listed in the table for style. 
        
		Value, Description
		0, None
		1, Sharp (Default)
		2, Round
		3, Smooth
		4, Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_split = """
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
        copy_by_trim = """
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


class _EllipticalArcModf():

        close = """
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
        extend_ed = True
        extend = """
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side.
        objects  (list of array_of _ObjectRoot, Required) - The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.

        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
        
        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurve

        """
        extend_length_ed = True
        extend_length = """
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to extent. The possible side elements are listed in the table for side.
        length  (float, Required) - The distance to extend the curve.
        
        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
		2, Extend from both the start and the end of the curve.        

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurveLength

        """
        extend_pnt_ed = True
        extend_pnt = """
        Extends a non-closed curve object by smooth extension to a point.

        Parameters
        ==========
        side  (integer, Required) - The size to  extent. The possible size elements are listed in the table for size.
        point  (List of float, Required) - The 3-D point.
        
        Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurvePoint

        """


class _LineDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used. The possible style types are listed in the table for style.  
        
        Table: style
		Value, Description
		0, None
		1, Sharp (Default)
		2, Round
		3, Smooth
		4, Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_split = """
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
        copy_by_trim = """
        Trims a curve by removing portions of the curve outside the specified interval.

        Parameters
        ==========
        interval  (List of integer, Required) - An list of two  identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
        delete  (boolean, Optional) - Delete the input curve. The default is to delete the input curve (True).

        Returns
        =======
        object - The newly created curve object, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TrimCurve

        """


class _LineModf():

        extend_ed = True
        extend = """
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to extent. The possible side elements are listed in the table for side.
        objects  (list of array_of _ObjectRoot, Required) - The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.
        
        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurve

        """
        extend_length_ed = True
        extend_length = """
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to extent. The possible side elements are listed in the table for side.
        
        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value,Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
		2, Extend from both the start and the end of the curve.
		
        length  (float, Required) - The distance to extend the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurveLength

        """
        extend_pnt_ed = True
        extend_pnt = """
        Extends a non-closed curve object by smooth extension to a point.

        Parameters
        ==========
        side  (integer, Required) - The size to extent. The possible side elements are listed in the table for side.
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
		
		point  (List of float, Required) - The 3-D point.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurvePoint

        """


class _MeshDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset = """
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


class _MeshRoot():

    pass


class _MeshRootDefm():

        box_morph = """
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
        shear = """
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
        transform_ed = True
        transform = """
        Moves, scales, or rotates an object given a 4x4 transformation matrix. The matrix acts on the left. The following table demonstrates the transformation matrix configuration:
		1,0,0,dX
		0,1,0,dY
		0,0,1,dZ
		0,0,0,1

        Parameters
        ==========
        matrix  (List of string, Required) - The transformation matrix (4x4 list of s).
        copy  (boolean, Optional) - Copy the object. If omitted, the object will not be copied (False).

        Returns
        =======
        boolean - The transformed object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TransformObject

        """


class _MeshRootFunc():

        curve_intersection_ed = True
        curve_intersection = """
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
        int - The mesh face index on which the intersection point lies.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveMeshIntersection

        """
        explode = """
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
        closest_point_ed = True
        closest_point = """
        Returns the point on a mesh that is closest to a test point.

        Parameters
        ==========
        point  (List of float, Required) - A 3-D point to test.
        tolerance  (float, Optional) - The tolerance. Of omitted, a default tolerance of 0.0 is used.

        Returns
        =======
        list - A list containing the results of the calculation, if successful. The list elements are as follows:
        list - The 3-D point on the mesh object.
        int - The index of the mesh face on which the 3-D point lies.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshClosestPoint

        """
        contour_points = """
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
        mesh_intersection = """
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
        naked_edge_points = """
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
        split_disjoint_mesh = """
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
        unify_normals_ed = True
        unify_normals = """
        Fixes inconsistencies in the directions of faces of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of faces that were modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnifyMeshNormals

        """


class _MeshRootFuncClsd():

        boolean_difference = """
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
        boolean_intersection = """
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
        boolean_split = """
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
        boolean_union = """
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


class _MeshRootFuncOorC():

    pass


class _MeshRootFuncOpen():

    pass


class _MeshRootModf():

        quads_to_triangles = """
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


class _MeshRootProp():

        disjoint_mesh_count_ed = True
        disjoint_mesh_count = """
        Returns the number of meshes that could be created by calling SplitDisjointMesh.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of meshes that could be created if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DisjointMeshCount

        """
        area = """
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
        area_centroid = """
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
        face_centers = """
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
        face_count_ed = True
        face_count = """
        Returns the total face count of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of mesh faces if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshFaceCount

        """
        face_normals = """
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
        face_vertices = """
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
        faces_ed = True
        faces = """
        Returns the face vertices of a mesh object.

        Parameters
        ==========
        face_type  (boolean, Optional) - The face type to be returned.  If omitted, both triangles and quads are returned (True). The face type elements are listed in the table for face_type.
        
        Table: face_type
		Value, Description
		True, Both triangles and quads.
		False, Only triangles

        Returns
        =======
        list - A list of 3-D points that define the face vertices of the mesh if successful.  If face_type is True, then faces are returned as both quads and triangles (4 3-D points).  For triangles, the third and forth vertex will be identical.  If face_type is False, then faces are returned as only triangles (3 3-D points).  Quads will be converted to triangles.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshFaces

        """
        quad_count_ed = True
        quad_count = """
        Returns the number of quad faces of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of quad mesh faces if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshQuadCount

        """
        texture_coordinates = """
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
        triangle_count_ed = True
        triangle_count = """
        Returns the number of triangular faces of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of triangular mesh faces if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshTriangleCount

        """
        vertex_colors = """
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
        vertex_count_ed = True
        vertex_count = """
        Returns the vertex count of a mesh object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of mesh vertices if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshVertexCount

        """
        vertex_normals = """
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
        vertices = """
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


class _MeshRootPropClsd():

        mesh_volume = """
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
        mesh_volume_centroid = """
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


class _MeshRootPropOorc():

    pass


class _MeshRootPropOpen():

    pass


class _MeshRootTest():

        is_closed = """
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
        is_manifold = """
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
        has_face_normals = """
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
        has_texture_coordinates = """
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
        has_vertex_colors = """
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
        has_vertex_normals = """
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


class _MeshRootType():

        is_mesh = """
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


class _NurbsCurveDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used. The possible style types are listed in the table for style.  
        
        Table: style
		Value, Description
		0, None
		1, Sharp (Default)
		2, Round
		3, Smooth
		4, Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_offset_on_srf = """
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
        copy_by_offset_on_srf_by_param = """
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
        This function calls the Rhinoscript function: OffsetCurveOnSurface

        """
        copy_by_split = """
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
        copy_by_trim = """
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


class _NurbsCurveModf():

        close = """
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
        extend_ed = True
        extend = """
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to extent. The possible side elements are listed in the table for side.  
        objects  (list of array_of _ObjectRoot, Required) - The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.
        
        Table: crv_type
		Value,Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
        Table: side
		Value,Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurve

        """
        extend_length_ed = True
        extend_length = """
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side. 
        length  (float, Required) - The distance to extend the curve. 
        
        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
				
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
		2, Extend from both the start and the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurveLength

        """
        extend_pnt_ed = True
        extend_pnt = """
        Extends a non-closed curve object by smooth extension to a point.

        Parameters
        ==========
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side.  
        point  (List of float, Required) - The 3-D point.
        
        Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurvePoint

        """


class _NurbsSurfaceDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset = """
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


class _ObjectRoot():

    pass


class _ObjectRootFunc():

    pass


class _ObjectRootGrps():

        groups = """
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
        top_group = """
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


class _ObjectRootModf():

        delete_ed = True
        delete = """
        Deletes one or more objects from the document.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects deleted if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteObjects

        """


class _ObjectRootMtrl():

        index_ed = True
        index = """
        Returns the material index of an object.
		Rendering materials are stored in Rhino's rendering material table.  This table is conceptually an array.  Render materials associated with objects and layers are specified by zero based indices into this array.
		If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material.  A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The rendering material index if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMaterialIndex

        """
        source_ed = True
        source = """
        Returns or modifies the rendering material source of an object.
		Rendering materials are stored in Rhino's rendering material table.  This table is conceptually an array.  Render materials associated with objects and layers are specified by zero based indices into this array.
		The index of the render material used to render an object is specified in one of three ways:
		1. Material from layer.  The rendering material assigned to the layer is used.
		2. Material from object.  The rendering material assigned to the object is used.
		3. Material from parent.  For objects with parents, like objects in block instances, use parent's material. If no parent, treats as material from layer.
		The default rendering material source for new objects is "material by layer."

        Parameters
        ==========
        source  (integer, Optional) - The new rendering material source.  If omitted, the current material source is returned.  Note, if arrObjects is specified, intSource is required. The possible source elements are listed in the table for source. 
		
		Table: sources
		Value, Description
		0, Material from layer
		1, Material from object
		2, <unused>
		3, Material from parent

        Returns
        =======
        int - If a rendering material source is not specified,  the current rendering material source if successful.
        int - If a rendering material source is specified, the previous rendering material source if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMaterialSource

        """


class _ObjectRootProp():

        color_ed = True
        color = """
        Returns or modifies the color of an object.  Object colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters
        ==========
        color  (integer, Optional) - The new color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.

        Returns
        =======
        int - If a color value is not specified,  the current color value if successful.
        int - If a color value is specified, the previous color value if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectColor

        """
        color_source_ed = True
        color_source = """
        Returns or modifies the color source of an object.   The color used to display objects is specified in one of four ways:
		1. Color from layer.  The object's layer determines the object's color.
		2. Color from object.  The object's color is set by the object itself.
		3. Color from material.  The object's diffuse material color determines the object's color.
		4. Color from parent. For objects with parents, like objects in block instances, use parent's color source. If no parent, treats as color from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new color source.  If omitted, the current color source is returned.  Note, if arrObjects is specified, intSource is required.  The possible source elements are listed in the table for source.
		
		Table: source
		Value, Description
		0, Color from layer
		1, Color from object
		2, Color from material
		3, Color from parent

        Returns
        =======
        int - If a color source is not specified,  the current color source if successful.
        int - If a color source is specified, the previous color source if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectColorSource

        """
        layer_ed = True
        layer = """
        Returns or modifies the layer of an object.

        Parameters
        ==========
        layer  (Layer, Optional) - The name of an existing layer.  If omitted, the current object layer is returned.  Note, if arrObjects is specified, strLayer is required.

        Returns
        =======
        float - If a layer is not specified,  the object's current layer if successful.
        float - If a layer is specified, the object's previous layer if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectLayer

        """
        linetype_ed = True
        linetype = """
        Returns or modifies the linetype of an object.

        Parameters
        ==========
        layer  (Layer, Optional) - The name of an existing linetype.  If omitted, the current object linetype is returned.  Note, if arrObjects is specified, strLinetype is required.

        Returns
        =======
        float - If a linetype is not specified,  the object's current linetype if successful.
        float - If a linetype is specified, the object's previous linetype if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectLinetype

        """
        linetype_source_ed = True
        linetype_source = """
        Returns or modifies the linetype source of an object.   The linetype used to display objects is specified in one of three ways:
		1. Linetype from layer.  The object's layer determines the object's linetype.
		2. Linetype from object. The object's linetype is set by the object itself.
		3. Linetype from parent.  For objects with parents, like objects in block instances, use parent's linetype. If no parent, treats as linetype from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new linetype source.  If omitted, the current linetype source is returned.  Note, if arrObjects is specified, intSource is required. The possible source elements are listed in the table for source.
		
		Table: source
		Value, Description
		0, Layer.  Use the object's layer linetype.
		1, Object.  Use the object's linetype.
		2, <unused>
		3, Parent.  Use the parent object's linetype.

        Returns
        =======
        int - If a linetype source is not specified,  the current linetype source if successful.
        int - If a linetype source is specified, the previous linetype source if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectLinetypeSource

        """
        name = """
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
        print_color_ed = True
        print_color = """
        Returns or modifies the print color of an object.  Object print colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters
        ==========
        color  (integer, Optional) - The new print color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.

        Returns
        =======
        int - If a print color value is not specified,  the current print color value if successful.
        int - If a print color value is specified, the previous print color value if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintColor

        """
        print_color_source_ed = True
        print_color_source = """
        Returns or modifies the print color source of an object.  The color used to print objects is specified in one of four ways:
		1. Print color from layer.  Use the print color assigned to the object's layer.
		2. Print color from object.  Use the print color that is assigned to the object.
		3. Print color from display.  Use the object's display color.
		4. Print color from parent.  For objects with parents, like objects in block instances, use parent's print color.  If no parent, treats as print color from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new print color source.  If omitted, the current print color source is returned.  Note, if arrObjects is specified, intSource is required. The possible source elements are listed in the table for source.
        
        Table: source
		Value, Description
		0, Print color by layer.
		1, Print color by object.
		2, Print color by display.
		3, Print color by parent.

        Returns
        =======
        int - If a print color source is not specified,  the current color source if successful.
        int - If a print color source is specified, the previous color source if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintColorSource

        """
        print_width_ed = True
        print_width = """
        Returns or modifies the print width of an object.  Object print widths are measured in millimeters (mm).

        Parameters
        ==========
        width  (float, Optional) - The new print width value in millimeters, where dblWidth = 0.0 means use the default width, and dblWidth < 0.0 means do not print (visible for screen display, but does not show on print).  If omitted, the current object print width is returned.  Note, if arrObjects is specified, dblWidth is required.

        Returns
        =======
        float - If a print width value is not specified,  the current print width value if successful.
        float - If a print width value is specified, the previous print width value if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintWidth

        """
        print_width_source_ed = True
        print_width_source = """
        Returns or modifies the print width source of an object.  The width used to print objects is specified in one of three ways:
		1. Print width from layer.  Use the print width assigned to the object's layer.
		2. Print width from object.  Use the print width that is assigned to the object.
		3. Print width from parent.  For objects with parents, like objects in block instances, use parent's print width.  If no parent, treats as print width from layer.

        Parameters
        ==========
        source  (integer, Optional) - The new print width source.  If omitted, the current print width source is returned.  Note, if arrObjects is specified, intSource is required. The possible source elements are listed in the table for source.
        
        Table: source
		Value, Description
		0, Print width by layer.
		1, Print width by object.
		2, <unused>
		3, Print width by parent.

        Returns
        =======
        float - If a print width source is not specified,  the current width source if successful.
        float - If a print width source is specified, the previous width source if successful.
        int - If objects is specified, then the number of objects modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectPrintWidthSource

        """


class _ObjectRootRndr():

        add_mesh_ed = True
        add_mesh = """
        Adds custom render mesh parameters to a meshable object, such as a surface or a polysurface.  If an object has custom render mesh parameters and they are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

        Parameters
        ==========
        quality  (integer, Optional) - The initial settings of the new custom render mesh parameters. The available options are listed in the table for quality.
        enable  (boolean, Optional) - Enable the custom render mesh parameters.  If omitted, the newly added parameters will be enabled (True).
        
        Table: quality
		Value, Description
		0, Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1, Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default), Use the document's current render mesh parameters.

        Returns
        =======
        boolean - If enable is not specified, then the current enabled/disabled state if successful.
        boolean - If enable is not specified, then the current enabled/disabled state if successful.
        None - If the object does not have custom render mesh parameters, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddObjectMesh

        """
        enable = """
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
        has_mesh = """
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
        density = """
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
        max_angle = """
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
        max_aspect_ratio = """
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
        max_dist_edge_to_srf = """
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
        max_edge_length = """
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
        min_edge_length = """
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
        min_initial_grid_quads = """
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
        quality_ed = True
        quality = """
        Returns or sets the render mesh quality of an object's custom render mesh parameters.

        Parameters
        ==========
        quality  (integer, Optional) - The render mesh quality elements are listed in the table for quality.
        
        Table: quality
		Value, Description
		0, Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1, Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default), Use the document's current render mesh parameters.

        Returns
        =======
        boolean - If quality is not specified, the current render mesh quality if successful.
        boolean - If quality is specified, the previous render mesh quality if successful.
        None - If the object does not have custom render mesh parameters, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshQuality

        """
        settings_ed = True;
        settings = """
        Returns or sets the render mesh settings of an object's custom render mesh parameters.

        Parameters
        ==========
        settings  (integer, Optional) - The render mesh settings, which is a bit-coded number that allows or disallows certain features.  The bits can be added together in any combination to form a value between 0 and 15.  The bit values are listed in the table for settings.
		
		Table: settings
		Value,	Description
		0, No settings enabled.
		1, Refine mesh enabled.
		2, Jagged seams enabled.
		4, Simple planes enabled.
		8, Pack textures enabled

        Returns
        =======
        boolean - If settings is not specified, the current render mesh settings if successful.
        boolean - If settings is specified, the previous render mesh settings if successful.
        None - If the object does not have custom render mesh parameters, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectMeshSettings

        """


class _ObjectRootStat():

        flash = """
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
        hide_ed = True
        hide = """
        Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects hidden if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: HideObjects

        """
        lock_ed = True
        lock = """
        Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects locked if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LockObjects

        """
        match_object_attributes_ed = True
        match_object_attributes = """
        Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.

        Parameters
        ==========
        targets  (list of array_of _ObjectRoot, Required) - A list of target objects.

        Returns
        =======
        int - The number of objects whose attributes were modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MatchObjectAttributes

        """
        reset_object_attributes_ed = True
        reset_object_attributes = """
        Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects whose attributes were modified if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MatchObjectAttributes

        """
        move_to_layout_space = """
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
        select_ed = True
        select = """
        Selects one or more objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects selected if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SelectObjects

        """
        show_ed = True
        show = """
        Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects shown if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ShowObjects

        """
        unlock_ed = True
        unlock = """
        Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects unlocked if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnlockObjects

        """
        unselect_ed = True
        unselect = """
        Unselects one or more selected objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        int - The number of objects unselected if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnselectObjects

        """


class _ObjectRootTest():

        is_in_layout_space = """
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
        is_hidden = """
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
        is_in_box_ed = True
        is_in_box = """
        Verifies an object's bounding box is inside of another bounding box.

        Parameters
        ==========
        box  (List of float, Required) - The bounding box to test against. A bounding box is an list of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
        mode  (boolean, Optional) - The test mode. The test values are listed in the table for mode.
        
        Table: mode        
		Value, Description
		True (Default), The object's bounding box must be contained by the test bounding box. In other words, test.min <= object.min and object.max <= test.max.
		False, The object's bounding box must be contained by or intersect with the test bounding box.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsObjectInBox

        """
        is_in_group = """
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
        is_locked = """
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
        is_normal = """
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
        is_reference = """
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
        is_selectable = """
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
        is_selected = """
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
        is_solid = """
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
        is_valid = """
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
        is_visible_in_view = """
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


class _ObjectRootTrfm():

        mirror = """
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
        move = """
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
        move_by_vec = """
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
        This function calls the Rhinoscript function: MoveObject

        """
        orient_ed = True
        orient = """
        Orients a single object based on input points.

        Parameters
        ==========
        reference  (List of float, Required) - An list of 3-D reference points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
        target  (List of float, Required) - An list of 3-D target points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
        flags  (integer, Optional) - The orient flags.  Values can be added together to specify multiple options. The values for the flags are listed in the table for flags.
		
		Table: flags
		Value, Description
		1, Copy object.  The default is not to copy the object.
		2, Scale object.  The default is not to scale the object.  Note, the scale option only applies if both arrReference and arrTarget contain only two 3-D points.

        Returns
        =======
        string - The oriented object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OrientObject

        """
        remap = """
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
        rotate = """
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
        scale = """
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


class _ObjectRootType():

        object_type = """
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


class _ObjectRootUtil():

        description = """
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
        dump_ed = True
        dump = """
        Returns a detailed description of an object.

        Parameters
        ==========
        type  (integer, Optional) - The acceptable values are listed in the table for type.
        
        Table: type
		Value, Description
		0 (Default), Returns both geometry and attribute details. This is equivalent to the results of the What command.
		1, Returns geometry details.
		2, Returns attribute details.
		3, Returns detailed technical information about the data structure of the object. This is equivalent to the results of the List command.

        Returns
        =======
        string - A detailed description of the object is successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ObjectDump

        """


class _PlanarMeshDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset = """
        Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.

        Parameters
        ==========
        distance  (float, Required) - The distance to offset.

        Returns
        =======
        object - The offset mesh object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: MeshOffset

        """


class _PlaneSurfaceDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset = """
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


class _PolyCurveDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used. The possible style types are listed in the table for style. 
		
		Table: style
		Value, Description
		0, None
		1, Sharp (Default)
		2, Round
		3, Smooth
		4, Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_split = """
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
        copy_by_trim = """
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


class _PolyCurveEval():

        tangent = """
        Returns a 3-D vector that is the tangent to a curve at a parameter.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - A  3-D vector if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveTangent

        """
        evaluate = """
        Evaluates a curve at a parameter.

        Parameters
        ==========
        parameter  (float, Required) - The parameter to evaluate.
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - A 3-D point if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EvaluateCurve

        """


class _PolyCurveFunc():

        explode = """
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


class _PolyCurveProp():

        degree_ed = True
        degree = """
        Returns the degree of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        float - The degree of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDegree

        """
        dim_ed = True
        dim = """
        Returns the dimension of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        float - The dimension of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDim

        """
        domain = """
        Returns the domain of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - The domain of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveDomain

        """
        edit_pnts = """
        Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.

        Parameters
        ==========
        return_parameters  (boolean, Required) - Return the edit points as an list of parameter values.  If omitted, the edit points are returned as an list of 3-D points.
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - If return_parameters is omitted or False, then a list of 3-D edit points if successful.
        list - If return_parameters is True, then a list of parameter values if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveEditPoints

        """
        end_pnt = """
        Returns the end point of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - The 3-D end point of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveEndPoint

        """
        knot_count_ed = True
        knot_count = """
        Returns the knot count of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        int - The number of knots if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveKnotCount

        """
        knots = """
        Returns the knots, or knot vector, of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - The knot values of the curve  if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveKnots

        """
        length_ed = True
        length = """
        Returns the length of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.
        sub_domain  (List of integer, Optional) - An list of two numbers identifying the sub-domain of the curve on which the calculation will be performed.  The two parameters (sub-domain) must be non-decreasing.  If omitted, the length of the entire curve is returned.

        Returns
        =======
        float - The length of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveLength

        """
        mid_pnt = """
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
        control_pnt_count_ed = True
        control_pnt_count = """
        Returns the control points count of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        int - The number of control points if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurvePointCount

        """
        control_pnts = """
        Returns the control points, or control vertices, of a curve object.  If the curve is a rational NURBS curve, the euclidean control vertices are returned.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - The control points of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurvePoints

        """
        start_pnt = """
        Returns the start point of a curve object.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - The 3-D starting point of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveStartPoint

        """
        weights = """
        Returns an array of weight values that are assigned to the control points of a curve.

        Parameters
        ==========
        index  (integer, Required) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        list - The weight values of the curve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurveWeights

        """
        segment_count_ed = True
        segment_count = """
        Returns the number of curve segments that make up a polycurve.

        Parameters
        ==========
        index  (integer, Optional) - If strObject identifies a polycurve object, then intIndex identifies the curve segment of the polycurve to query.

        Returns
        =======
        int - The number of curve segments in a polycurve if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PolyCurveCount

        """


class _PolySurfaceDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """


class _PolySurfaceFunc():

        explode = """
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


class _PolylineDupl():

        copy_by_sub = """
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
        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """
        copy_by_offset_ed = True
        copy_by_offset = """
        Offsets a curve by a distance. The offset curve will be added to Rhino.

        Parameters
        ==========
        direction_point  (List of float, Required) - The 3-D point that indicates the direction of the offset.
        distance  (float, Required) - The distance of the offset.
        normal  (List of float, Optional) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
        style  (integer, Optional) - The corner style.  If omitted, a sharp corner style is used.
        
        Table : style
		Value,Description
		0,None
		1,Sharp (Default)
		2,Round
		3,Smooth
		4,Chamfer

        Returns
        =======
        list - A list containing the identifiers of the new objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OffsetCurve

        """
        copy_by_split = """
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
        copy_by_trim = """
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


class _PolylineModf():

        close = """
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
        extend_ed = True
        extend = """
        Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to extent. The possible side elements are listed in the table for side.
        objects  (list of array_of _ObjectRoot, Required) - The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.
        
        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurve

        """
        extend_length_ed = True
        extend_length = """
        Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.

        Parameters
        ==========
        crv_type  (integer, Required) - Type of extension. The possible extension types are listed in the table for crv_type.
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side.
        length  (float, Required) - The distance to extend the curve.
        
        Table: crv_type
		Value, Description
		0, Line - Creates an line extension tangent to the original curve.
		1, Arc - Creates an arc extension tangent to the original curve.
		2, Smooth - Creates a smooth curve extension curvature continuous with the original curve.
		
		Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
		2, Extend from both the start and the end of the curve.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurveLength

        """
        extend_pnt_ed = True
        extend_pnt = """
        Extends a non-closed curve object by smooth extension to a point.

        Parameters
        ==========
        side  (integer, Required) - The size to  extent. The possible side elements are listed in the table for side.
        
        Table: side
		Value, Description
		0, Extend from the start of the curve.
		1, Extend from the end of the curve.
		
        point  (List of float, Required) - The 3-D point.

        Returns
        =======
        object - The extended object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExtendCurvePoint

        """


class _PolylineProp():

        vertices = """
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


class _SphereDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """


class _SphereProp():

        sphere_definition = """
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


class _SurfaceRoot():

    pass


class _SurfaceRootDefm():

        box_morph = """
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
        shear = """
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
        transform_ed = True
        transform = """
        Moves, scales, or rotates an object given a 4x4 transformation matrix. The matrix acts on the left. The following table demonstrates the transformation matrix configuration:
		1,0,0,dX
		0,1,0,dY
		0,0,1,dZ
		0,0,0,1

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


class _SurfaceRootEval():

        evaluate = """
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
        derivatives = """
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
        evaluate_frame = """
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


class _SurfaceRootFunc():

        closest_pnt_brep = """
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
        cap_planar_holes = """
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
        intersect_2_breps = """
        Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.

        Parameters
        ==========
        surface  (surface object, Required) - The second  brep object's identifier.
        tolerance  (float, Optional) - The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..

        Returns
        =======
        list of objects - A list of strings identifying the newly created intersection curve and point objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IntersectBreps

        """
        make_non_periodic = """
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
        make_periodic = """
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
        split = """
        Splits a brep.  A brep can be either a surface with a single face or a polysurface.

        Parameters
        ==========
        cutter  (surface object, Required) - The identifier of the brep object to split with.
        delete  (boolean, Optional) - Delete input brep.  If omitted, the input brep will not be deleted (False).

        Returns
        =======
        list of objects - The identifiers of the new brep objects if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SplitBrep

        """
        closest_pnt = """
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
        intersect_2_srfs = """
        Calculates the intersection of a surface object with another surface object. Note, this function works on untrimmed surfaces.

        Parameters
        ==========
        surface_a  (surface object, Required) - The identifier of the second surface object.
        tolerance  (float, Optional) - The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
        create  (boolean, Optional) - Create the intersection curves and points.  If omitted, intersection geometry will not be created.

        Returns
        =======
        list - If create is not specified or is equal to False, a list numbers identifying the intersection event type if successful.  The list will contain one or more of the following intersection event types:
        list - If create is specified and is equal to True, a two-dimensional list of intersection information if successful.  The list will contain one or more of the following elements:
        number - The intersection event type.  See the above table for details.
        string - The intersection curve or point object that was created.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceSurfaceIntersection

        """
        intersect_2_srfs_test = """
        Calculates the intersection of a surface object with another surface object. Note, this function works on untrimmed surfaces.

        Parameters
        ==========
        surface_a  (surface object, Required) - The identifier of the second surface object.
        tolerance  (float, Optional) - The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
        create  (boolean, Optional) - Create the intersection curves and points.  If omitted, intersection geometry will not be created.

        Returns
        =======
        list - If create is not specified or is equal to False, a list numbers identifying the intersection event type if successful.  The list will contain one or more of the following intersection event types:
        list - If create is specified and is equal to True, a two-dimensional list of intersection information if successful.  The list will contain one or more of the following elements:
        number - The intersection event type.  See the above table for details.
        string - The intersection curve or point object that was created.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceSurfaceIntersection

        """


class _SurfaceRootFuncClsd():

        boolean_difference_1 = """
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
        boolean_difference_2 = """
        Performs a Boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file.

        Parameters
        ==========
        breps  (list of surface object, Required) - The identifiers of the surfaces or polysurfaces to subtract from.
        delete  (boolean, Optional) - Delete all input objects. The default is to delete all input objects (True).

        Returns
        =======
        list of objects - A list containing the identifiers of the newly created objects, if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BooleanDifference

        """
        boolean_intersection = """
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
        boolean_union = """
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


class _SurfaceRootModf():

        flip = """
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
        insert_knot = """
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
        rebuild = """
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
        remove_knot = """
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
        reverse_ed = True
        reverse = """
        Reverses the U and V directions of a surface object. This feature can also be found in Rhino's Dir command.
		To reverse the normal direction of a surface, use the FlipSurface method.

        Parameters
        ========== table direction.
        direction  (integer, Required) - The direction to reverse. Values can be added together so as to reverse more than one direction. The possible value are listed in the

        Table: direction
		Value, Description
		1, Reverse the surface in the U direction.
		2, Reverse the surface in the V direction.
		4, Swap, or transpose, the U and V directions of the surface.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ReverseSurface

        """
        shrink_trimmed = """
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
        seam = """
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


class _SurfaceRootProp():

        area = """
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
        area_centroid = """
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
        area_moments = """
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
        contour_pnts = """
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
        curvature = """
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
        curvature_analysis = """
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
        degree_ed = True
        degree = """
        Returns the degree of a  surface object in the specified direction.

        Parameters
        ==========
        direction  (integer, Optional) - The direction, either 0 = U, or 1 = V, or 2 = Both.  Of omitted, both the degrees in the U and V directions are returned (2 = Both).

        Returns
        =======
        list - If direction is not specified, or direction is set to 2, then the degree in both the U and V directions is returned.
        int - If direction is specified, and direction is set to either 0 or 1, then the degree in either the U or V direction is returned.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceDegree

        """
        domain = """
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
        edit_pnts = """
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
        isocurve_density_ed = True
        isocurve_density = """
        Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface.

        Parameters
        ==========
        density  (integer, Optional) - The isocurve wireframe density.  The possible values are listed in the table for density.
        
        Table: density
		Value, Description
		-1, Hides surface isocurves.
		0, Display boundary and knot wires.
		1, Display boundary and knot wires and one interior wire if there are no interior knots.
		>= 2, Display boundary and knot wires and (N+1) interior wires.

        Returns
        =======
        float - The density is not specified, then the current isocurve density if successful.
        float - The density is specified, then the previous isocurve density if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceIsocurveDensity

        """
        knot_count = """
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
        knots = """
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
        normal = """
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
        pnt_count = """
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
        pnts = """
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
        weights = """
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


class _SurfaceRootPropClsd():

        volume_ed = True
        volume = """
        Calculates the volume of closed surface or polysurface objects.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of volume information if successful.  The list will contain the following information:
        float - The volume.
        float - The absolute (+/-) error bound for the volume.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SurfaceVolume

        """
        volume_centroid = """
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
        volume_moments = """
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


class _SurfaceRootTest():

        is_brep = """
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
        is_brep_manifold = """
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
        is_parameter_on_srf = """
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
        is_plane_surface = """
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
        is_pnt_in_srf = """
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
        is_pnt_on_srf = """
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
        is_poly_srf = """
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
        is_poly_surface_closed = """
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
        is_poly_srf_planar = """
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
        is_srf_closed = """
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
        is_srf_periodic = """
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
        is_srf_planar = """
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
        is_srf_rational = """
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
        is_srf_singular = """
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
        is_srf_trimmed = """
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


class _SurfaceRootType():

        is_cone = """
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
        is_cylinder = """
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
        is_sphere = """
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
        is_surface = """
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
        is_torus = """
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


class _TorusDupl():

        copy_move = """
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
        copy_move_by_vec = """
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
        This function calls the Rhinoscript function: CopyObject

        """


class _TorusProp():
        torus_definition = """
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
