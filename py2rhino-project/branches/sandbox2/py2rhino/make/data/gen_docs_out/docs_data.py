

class Arc():

    create = """
    Factory method:
    Adds an arc curve to the document.
    Parameters
    ==========
    C{plane}(array_of dbl, REQ) - The plane on which the arc will lie. The origin of the plane will be the center point of the arc. The X-axis of the plane will define the 0 angle direction.
    C{radius}(dbl, REQ) - The radius arc.
    C{angle}(dbl, REQ) - A angle or interval, in degrees, of the arc.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_3pt = """
    Factory method:
    Adds a 3-point arc curve to the document.
    Parameters
    ==========
    C{start}(array_of dbl, REQ) - The starting point of the arc.
    C{end}(array_of dbl, REQ) - The ending point of the arc.
    C{point}(array_of dbl, REQ) - A point on the arc.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_fillet = """
    Factory method:
    Adds a fillet curve between two curve objects.
    Parameters
    ==========
    C{curve_0}(_ObjectRoot._CurveRoot.NurbsCurve, REQ) - The identifier of the first curve object.
    C{curve_1}(_ObjectRoot._CurveRoot.NurbsCurve, REQ) - The identifier of the second curve object.
    C{radius}(dbl, OPT) - The fillet radius. If omitted, a radius of 1.0 is specified.
    C{point_0}(array_of dbl, OPT) - The base point on the first curve. If omitted, the starting point of the curve is used.
    C{point_1}(array_of dbl, OPT) - The base point on the second curve. If omitted, the starting point of the curve is used.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Box():

    create = """
    Factory method:
    Adds a new box-shaped polysurface to the document.
    Parameters
    ==========
    C{corners}(array_of dbl, REQ) - An array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Circle():

    create = """
    Factory method:
    Adds a circle curve to the document.
    Parameters
    ==========
    C{plane}(array_of dbl, REQ) - The plane on which the circle will lie. The origin of the plane will be the center point of the circle.
    C{radius}(dbl, REQ) - The radius of the circle.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_3pt = """
    Factory method:
    Adds a 3-point circle curve to the document.
    Parameters
    ==========
    C{first}(array_of dbl, REQ) - The first point of the circle.
    C{second}(array_of dbl, REQ) - The second point of the circle.
    C{third}(array_of dbl, REQ) - The third point of the circle.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Cone():

    create = """
    Factory method:
    Adds a cone-shaped polysurface to the document.
    Parameters
    ==========
    C{base}(array_of dbl, REQ) - The 3-D origin point of the cone.
    C{height}(array_of dbl, REQ) - The cone's base plane.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
    C{radius}(dbl, REQ) - The 3-D height point of the cone.  The height point defines the height and direction of the cone.
    C{cap}(bln, OPT) - The height of the cone.  If arrPlane is specified, then the center of the arrPlane is height * the plane's z-axis.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_plane = """
    Factory method:
    Adds a cone-shaped polysurface to the document.
    Parameters
    ==========
    C{plane}(array_of dbl, REQ) - The 3-D origin point of the cone.
    C{height}(dbl, REQ) - The cone's base plane.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
    C{radius}(dbl, REQ) - The 3-D height point of the cone.  The height point defines the height and direction of the cone.
    C{cap}(bln, OPT) - The height of the cone.  If arrPlane is specified, then the center of the arrPlane is height * the plane's z-axis.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Cylinder():

    create = """
    Factory method:
    Adds a cylinder-shaped polysurface to the document.
    Parameters
    ==========
    C{base}(array_of dbl, REQ) - The 3-D base point of the cylinder.
    C{height}(array_of dbl, REQ) - The base plane of the cylinder.
    C{radius}(dbl, REQ) - The 3-D height point of the cylinder.  The height point defines the height and direction of the cylinder.
    C{cap}(bln, OPT) - The height of the cylinder.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_plane = """
    Factory method:
    Adds a cylinder-shaped polysurface to the document.
    Parameters
    ==========
    C{plane}(array_of dbl, REQ) - The 3-D base point of the cylinder.
    C{height}(dbl, REQ) - The base plane of the cylinder.
    C{radius}(dbl, REQ) - The 3-D height point of the cylinder.  The height point defines the height and direction of the cylinder.
    C{cap}(bln, OPT) - The height of the cylinder.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Ellipse():

    create = """
    Factory method:
    Adds an elliptical curve to the document.
    Parameters
    ==========
    C{plane}(array_of dbl, REQ) - The plane on which the ellipse will lie. The origin of the plane will be the center point of the ellipse.
    C{x_radius}(dbl, REQ) - The radius in the X-axis direction.
    C{y_radius}(dbl, REQ) - The radius in the Y-axis direction.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_3pt = """
    Factory method:
    Adds a 3 point elliptical curve to the document.
    Parameters
    ==========
    C{center}(array_of dbl, REQ) - The center point of the ellipse.
    C{second}(array_of dbl, REQ) - The end point of the X-axis.
    C{third}(array_of dbl, REQ) - The end point of the Y-axis.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class EllipticalArc():

    pass


class GenericObject():

    pass


class Line():

    create = """
    Factory method:
    Adds a line curve to the current model.
    Parameters
    ==========
    C{start}(array_of dbl, REQ) - The starting point of the line.
    C{end}(array_of dbl, REQ) - The ending point of the line.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Mesh():

    create = """
    Factory method:
    Adds a mesh object to the document.
    Parameters
    ==========
    C{vertices}(array_of dbl, REQ) - An array of 3-D points defining the vertices of the mesh.
    C{face_vertices}(array_of int, REQ) - An array containing arrays of four numbers that define the vertex indices for each face of the mesh. If the third and forth vertex indices of a face are identical, a triangular face will be created. Otherwise a quad face will be created.
    C{vertex_normals}(array_of dbl, OPT) - An array of 3-D vectors defining the vertex normals of the mesh. Note, for every vertex, the must be a corresponding vertex normal.
    C{texture_coordinates}(array_of dbl, OPT) - An array of 2-D texture coordinates. Note, for every vertex, there must be a corresponding texture coordinate.
    C{vertex_colors}(array_of int, OPT) - An array of RGB color values. Note, for every vertex, there must be a corresponding vertex color.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_polyline = """
    Factory method:
    Creates a polygon mesh object based on a closed polyline curve object. The newly created polygon mesh object is added to the document.
    Parameters
    ==========
    C{polyline}(_ObjectRoot._CurveRoot.Polyline, REQ) - The identifier of the polyline curve object.
    Returns
    =======
    string - The identifier of the new polygon mesh object if successful.
    null - If not successful, or on error.
    """


class NurbsCurve():

    create_by_pnts = """
    Factory method:
    Adds a control points curve object to the document.
    Parameters
    ==========
    C{points}(array_of dbl, REQ) - An array of 3-D points.
    C{degree}(int, OPT) - The degree of the curve.  If omitted, a degree 3 curve is created.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_interp_crv_on_srf = """
    Factory method:
    Adds an interpolated curve object that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.
    Parameters
    ==========
    C{surface}(_ObjectRoot._CurveRoot.NurbsCurve, REQ) - The surface object's identifier.
    C{points}(array_of dbl, REQ) - An array of 3-D points that lie on the specified surface. The array must contain at least two points.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_interp_crv_on_srf_uv = """
    Factory method:
    Adds an interpolated curve object. based on surface parameters, that lies on a specified surface. Note, this function will not create periodic curves, but it will create closed curves.
    Parameters
    ==========
    C{surface}(_ObjectRoot._CurveRoot.NurbsCurve, REQ) - The surface object's identifier.
    C{points}(array_of dbl, REQ) - An array of 2-D surface parameters. The array must contain at least two sets of surface parameters.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_interp_crv = """
    Factory method:
    Adds an interpolated curve object to  the document.  Options exist to make a periodic curve or to specify the tangent at the endpoints.  The resulting curve is a non-rational NURBS curve of the specified degree.
    Parameters
    ==========
    C{points}(array_of dbl, REQ) - An array containing 3-D points to interpolate.  For periodic curves, if the final point is a duplicate of the initial point, it is ignored. Note, the number of control points must be >= (intDegree+1).
    C{degree}(int, OPT) - The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.  For intKnotStyle = 4 or 5, the degree must be odd.
    C{knot_style}(int, OPT) - The knot style to use, and whether the curve should be periodic.  If omitted, uniform knots (0) are created.
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
    C{start_tan}(array_of dbl, OPT) - A 3-D vector that specifies a tangency condition at the beginning of the curve. If the curve is to periodic, this argument must be omitted.
    C{end_tan}(array_of dbl, OPT) - A 3-D vector that specifies a tangency condition at the end of the curve. If the curve is to periodic, this argument must be omitted.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_interp_crv_ex = """
    Factory method:
    Adds an interpolated curve object to  the document similar to Rhino's InterpCrv command.
    Parameters
    ==========
    C{points}(array_of dbl, REQ) - An array containing 3-D points to interpolate. Note, the number of control points must be >= (intDegree+1).
    C{degree}(int, OPT) - The degree of the curve.  If omitted, degree = 3 is used.  The degree of the curve must be >=1.  Periodic curves must have a degree >= 2.  For intKnotStyle = 1 or 2, the degree must be 3.
    C{knot_style}(int, OPT) - The knot style to use. If omitted, a knot style = 0 is used. The knot style determines how an interpolated curve will be parameterized.
		Value
		Description
		0
		Uniform.  The knot spacing is always 1 and is not based on the physical spacing of points.
		1
		Chord. The spacing between the points is used for the knot spacing
		2
    C{sharp}(bln, OPT) - If True, when you create a closed curve, it will have a kink at the start/end point. If False (default), a smooth closure will be created.
    C{start_tangent}(array_of dbl, OPT) - A 3-D vector that specifies a tangency condition at the beginning of the curve.
    C{end_tangent}(array_of dbl, OPT) - A 3-D vector that specifies a tangency condition at the end of the curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create = """
    Factory method:
    Adds a NURBS curve object to the document.
    Parameters
    ==========
    C{points}(array_of dbl, REQ) - An array of 3-D control points.
    C{knots}(array_of int, REQ) - The knot values for the curve.  The number of elements in arrKnots must equal the number of elements in arrPoints plus intDegree minus one (1).
    C{degree}(int, REQ) - The degree of the curve.  The degree must be greater than or equal to one (1).
    C{weights}(array_of int, OPT) - The weight values for the curve.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_srf_contour = """
    Factory method:
    Adds a spaced series of planar curves resulting from the intersection of a defined cutting planes through a surface or a polysurface. For more information, see the Rhino help file for details on the Contour command.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of a surface or polysurface object.
    C{start_point}(array_of dbl, REQ) - The 3-D starting point of a center line.
    C{end_point}(array_of dbl, REQ) - The 3-D ending point of a center line.
    C{interval}(dbl, OPT) - A plane that defines the cutting plane.
    Returns
    =======
    array - An array of strings identifying the newly created contour curves if successful.
    null - If not successful, or on error.
    """
    create_by_srf_contour_cut_plane = """
    Factory method:
    Adds a spaced series of planar curves resulting from the intersection of a defined cutting planes through a surface or a polysurface. For more information, see the Rhino help file for details on the Contour command.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of a surface or polysurface object.
    C{plane}(array_of dbl, REQ) - The 3-D starting point of a center line.
    C{interval}(dbl, OPT) - The 3-D ending point of a center line.
    Returns
    =======
    array - An array of strings identifying the newly created contour curves if successful.
    null - If not successful, or on error.
    """
    create_by_srf_section = """
    Factory method:
    Adds planar curves resulting from the intersection of a defined cutting plane through a surface or a polysurface. For more information, see the Rhino help file for details on the Section command.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of a surface or polysurface object.
    C{plane}(array_of dbl, REQ) - A plane that defines the cutting plane.
    Returns
    =======
    array - An array of strings identifying the newly created section curves if successful.
    null - If not successful, or on error.
    """
    create_by_srf_edge = """
    Factory method:
    Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of the surface or polysurface object.
    C{select}(bln, OPT) - Select the duplicated edge curves.  The default is not to select (False).
    Returns
    =======
    array - An array of strings identifying the newly created curve objects if successful.
    null - If not successful, or on error.
    """
    create_by_mesh_border = """
    Factory method:
    Creates a curve that duplicates a mesh border.
    Parameters
    ==========
    C{mesh}(_ObjectRoot._MeshRoot, REQ) - The identifier of the mesh object.
    Returns
    =======
    array - An array of strings identifying the new curve objects if successful.
    null - If not successful, or on error.
    """
    create_by_srf_border = """
    Factory method:
    Creates a curve that duplicates a surface or polysurface border.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of the surface or polysurface object.
    Returns
    =======
    array - An array of strings identifying the new curve objects if successful.
    null - If not successful, or on error.
    """
    create_by_srf_iso_curve = """
    Factory method:
    Extracts isoparametric curves from a surface.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The object's identifier.
    C{parameter}(array_of dbl, REQ) - An array containing the U,V parameter of the surface to evaluate.
    C{dir}(int, REQ) - The direction, either 0 = U, 1 = V, or 2 = Both.
    Returns
    =======
    array - An array of strings identifying the newly created curve objects if successful.
    null - If not successful, or on error.
    """
    create_by_fit = """
    Factory method:
    Reduces the number of curve control points while maintaining the curve's same general shape.  Use this function for replacing curves with too many control points.  For more information, see the Rhino help file for the FitCrv command.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The object's identifier.
    C{degree}(int, OPT) - The curve degree, which must be greater than 1. The default is 3.
    C{tolerance}(dbl, OPT) - The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.
    C{angle_tolerance}(dbl, OPT) - The kink smoothing tolerance in degrees.  If dblAngleTolerance is 0.0, all kinks are smoothed.  If dblAngleTolerance is > 0.0, kinks smaller than dblAngleTolerance are smoothed.  If dblAngleTolerance is not specified or < 0.0, the document angle tolerance is used for the kink smoothing.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_projection_to_mesh = """
    Factory method:
    Projects one or more points onto one or more meshes.
    Parameters
    ==========
    C{curves}(array_of _ObjectRoot, REQ) - The identifiers of one or more curve objects to project.
    C{meshes}(array_of str, REQ) - The identifiers of the mesh objects to project onto.
    C{direction}(array_of dbl, REQ) - The direction (3-D vector) to project the points.
    Returns
    =======
    array - The identifiers of the newly created, projected curve objects, if successful.
    null - If not successful, or on error.
    """
    create_by_projection_to_srf = """
    Factory method:
    Projects one or more points onto one or more surfaces or polysurfaces.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot.NurbsCurve, REQ) - The identifiers of one or more curve objects to project.
    C{surfaces}(array_of str, REQ) - The identifiers of the surface or polysurface objects to project onto.
    C{direction}(array_of dbl, REQ) - The direction (3-D vector) to project the points.
    Returns
    =======
    array - The identifiers of the newly created, projected curve objects, if successful.
    null - If not successful, or on error.
    """
    create_by_srf_pull = """
    Factory method:
    Pulls a curve object to a surface object. For more information, see the Rhino help file for information on the Pull command.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of the surface object that pulls.
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The identifier of the curve object to pull.
    C{delete}(bln, OPT) - Delete input curve.  If omitted, the input curve will not be deleted (False).
    Returns
    =======
    array - The identifiers of the new curve objects if successful.
    null - If not successful, or on error.
    """
    create_by_mesh_pull = """
    Factory method:
    Pulls a curve object to a mesh object. The function makes a polyline approximation of the input curve and gets the closest point on the mesh for each point on the mesh.  Then it "connects the points" so  that you have a polyline on the mesh.
    Parameters
    ==========
    C{mesh}(_ObjectRoot._MeshRoot, REQ) - The identifier of the mesh object that pulls.
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The identifier of the curve object to pull.
    Returns
    =======
    string - The identifier of the new curve object if successful.
    null - If not successful, or on error.
    """
    create_by_srf_short_path = """
    Factory method:
    Creates the shortest possible curve (geodesic) between two points on a surface. For more details, see the ShortPath command in the Rhino help file.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of the surface object that pulls.
    C{start}(array_of dbl, REQ) - A 3-D surface point identifying the starting point of the short curve.
    C{end}(array_of dbl, REQ) - A 3-D surface point identifying the ending point of the short curve.
    Returns
    =======
    string - The identifier of the new curve object if successful.
    null - If not successful, or on error.
    """
    create_by_srf_principal_curvature = """
    Factory method:
    Adds curvature curves at the evaluated point on a surface. For more information, see the Rhino help file for the Curvature command.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The curve's identifier.
    C{point}(array_of dbl, REQ) - A point on the curve to evaluate.
    Returns
    =======
    array - An array of two strings that identify the Maximum and Minimum principal curvature curves, respectively, if successful.
    null - If not successful, or on error.
    """


class NurbsSurface():

    create_by_cut_plane = """
    Factory method:
    Adds a planar surface through objects at a designated location.  For more information, see the Rhino help file for the CutPlane command.
    Parameters
    ==========
    C{objects}(array_of _ObjectRoot, REQ) - The identifiers of objects that the cutting planes will pass through.
    C{start_point}(array_of dbl, REQ) - The start of the line that defines the cutting plane.
    C{end_point}(array_of dbl, REQ) - The end of the line that defines the cutting plane.
    C{normal}(array_of dbl, OPT) - In the case of Rhino's CutPlane command, this is the normal to, or Z axis of, the active view's construction plane.  If omitted, the world Z axis is used.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_edge = """
    Factory method:
    Creates a surface from 2, 3, or 4 edge curves.
    Parameters
    ==========
    C{objects}(array_of _ObjectRoot._CurveRoot, REQ) - An array of 2, 3, or 4 curve object identifiers.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_loft = """
    Factory method:
    Adds a surface created by lofting curves to the document.
		* This function will not perform any curve sorting. You must pass in curves in the order you want them lofted.
		* This function will not adjust the directions of open curves. Use CurveDirectionsMatch and ReverseCurve to adjust the directions of open curves.
		* This function will not adjust the seams of closed curves. Use CurveSeam to adjust the seam of closed curves.
    Parameters
    ==========
    C{objects}(array_of _ObjectRoot._CurveRoot, REQ) - An ordered array of strings identifying the curve objects to loft.
    C{start_pt}(array_of dbl, OPT) - The starting point of the loft.
    C{end_pt}(array_of dbl, OPT) - The ending point of the loft.
    C{srf_type}(int, OPT) - The type of loft. The default loft type is Normal (0). The possible loft types are as follows:
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
    C{style}(int, OPT) - The simplify method of the loft. The default value is None (0). The possible loft simplify methods are as follows:
		Value
		Description
		0
		None. Does not simplify.
		1
		Rebuild. Rebuilds the shape curves before lofting.
		2
    C{value}(n, OPT) - A value based on the specified intStyle. If intStyle=1 (Rebuild), then nValue is the number of control point used to rebuild. If intstyle=1 is specified and this argument is omitted, then curves will be rebuilt using 10 control points. If intStyle=2 (Refit), then nValue is the tolerance used to rebuild. If intstyle=2 is specified and this argument is omitted, then the document's absolute tolerance us used for refitting.
    C{closed}(bln, OPT) - Creates a closed surface, continuing the surface past the last curve around to the first curve. Available when you have selected three shape curves. The default value is not to create a closed surface (False).
    Returns
    =======
    array - An array containing the identifiers of the new surface objects if successful.
    null - If not successful, or on error.
    """
    create = """
    Factory method:
    Adds a NURBS surface object to the document.
    Parameters
    ==========
    C{point_count}(array_of int, REQ) - The number of control points in the U and V directions.
    C{points}(array_of dbl, REQ) - An array of 3-D control points.
    C{knots_u}(array_of int, REQ) - The knot values for the surface in the U direction.  The array must contain arrPointCount(0) + arrDegree(0) - 1 elements.
    C{knots_v}(array_of int, REQ) - The knot values for the surface in the V direction.  The array must contain arrPointCount(1) + arrDegree(1) - 1 elements.
    C{degree}(array_of int, REQ) - The degree of the surface in the U and V directions.  The degree in each direction must be greater than or equal to one (1).
    C{weights}(array_of int, REQ) - The weight values for the surface.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_planar_crv = """
    Factory method:
    Creates one or more surfaces from planar curves.
    Parameters
    ==========
    C{objects}(array_of _ObjectRoot._CurveRoot, REQ) - An array of curve object identifiers.
    Returns
    =======
    array - An array of strings identifying the new objects if successful.
    null - If not successful, or on error.
    """
    create_by_rail_rev = """
    Factory method:
    Create a surface by revolving a profile curve along a rail curve.
    Parameters
    ==========
    C{profile}(_ObjectRoot._CurveRoot, REQ) - The identifier of the profile curve.
    C{rail}(_ObjectRoot._CurveRoot, REQ) - The identifier of the rail curve.
    C{axis}(array_of dbl, REQ) - An array of two 3-D points identifying the start point and end point of the rail revolve axis.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_rev = """
    Factory method:
    Create a surface by revolving a curve around an axis.
    Parameters
    ==========
    C{profile}(_ObjectRoot._CurveRoot, REQ) - The identifier of the curve to revolve.
    C{axis}(array_of dbl, REQ) - An array of two 3-D points identifying the start point and end point of the rail revolve axis.
    C{start_angle}(dbl, OPT) - The starting angle. If omitted, an angle of 0.0 is used.
    C{end_angle}(dbl, OPT) - The ending angle. If omitted, an angle of 360.0 is used.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_control_pt_grid = """
    Factory method:
    Creates a surface from a grid of control points.
    Parameters
    ==========
    C{count}(array_of int, REQ) - The number of control points in the U and V directions.
    C{points}(array_of dbl, REQ) - An array of 3-D control points.
    C{degree}(array_of dbl, OPT) - The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_corner_pts = """
    Factory method:
    Creates a new surface from either 3 or 4 corner points.
    Parameters
    ==========
    C{points}(array_of dbl, REQ) - An array of either 3 or 4 corner points.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_pt_grid = """
    Factory method:
    Creates a surface from a grid of points.
    Parameters
    ==========
    C{count}(array_of int, REQ) - The number of points in the U and V directions.
    C{points}(array_of dbl, REQ) - An array of 3-D points.
    C{degree}(array_of int, OPT) - The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.
    C{closed}(array_of bln, OPT) - Whether or not the surface is closed in the U and V directions.  If omitted, the new surface will not be closed in either the U or V directions.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
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
    C{rail}(_ObjectRoot._CurveRoot, REQ) - The identifier of the rail curve.
    C{shapes}(array_of _ObjectRoot._CurveRoot, REQ) - An array of strings identifying one or more shape, or cross section, curves.
    C{start_pt}(array_of dbl, OPT) - The 3-D starting point of the surface.
    C{end_pt}(array_of dbl, OPT) - The 3-D ending point of the surface.
    C{closed}(bln, OPT) - If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
    C{style}(int, OPT) - The sweep style, where 0 = Freeform and 1 = Roadlike. The default value is 0 = Freeform.
    C{style_arg}(va, OPT) - If intStyle = 1 (Roadlike), then this argument is a 3-D vector identifying the planar up direction for the sweep.
    C{simplify}(int, OPT) - Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
    C{simplify_arg}(va, OPT) - If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance.  If intSimplify = 2 (Rebuild), then this argument is a number specifying the number of control points to rebuild the shape curves.
    Returns
    =======
    array - The identifiers of the new surface objects if successful.
    null - If not successful, or on error.
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
    C{rails}(array_of _ObjectRoot._CurveRoot, REQ) - An array of strings identifying two rail curves.
    C{shapes}(array_of _ObjectRoot._CurveRoot, REQ) - An array of strings identifying one or more shape, or cross section, curves.
    C{start_pt}(array_of dbl, OPT) - The 3-D starting point of the surface.
    C{end_pt}(array_of dbl, OPT) - The 3-D ending point of the surface.
    C{closed}(bln, OPT) - If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
    C{simple_sweep}(bln, OPT) - If True, then create surfaces using exact input. This option generates simpler surfaces in cases when the curves are perfectly set up.  The default value is False.
    C{maintain_height}(bln, OPT) - By default, shape curves normally scale in both the height and width dimensions. To remove the association between the height scaling from the width scaling, set this value to True.  The default value is False.
    C{simplify}(int, OPT) - Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
    C{simplify_arg}(va, OPT) - If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance.  If intSimplify = 2 (Rebuild), then this argument is a number specifying the number of control points to rebuild the shape curves.
    Returns
    =======
    array - The identifiers of the new surface objects if successful.
    null - If not successful, or on error.
    """
    create_copy_move = """
    Factory method:
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{object}(_ObjectRoot, REQ) - The identifier of the object to copy.
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    create_copy_move_by_vec = """
    Factory method:
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{object}(_ObjectRoot, REQ) - The identifier of the object to copy.
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    create_by_extrude_crv = """
    Factory method:
    Creates a surface by extruding a curve along a path curve.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The identifier of the curve object to extrude.
    C{path}(str, REQ) - The identifier of the path curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_extrude_crv_pnt = """
    Factory method:
    Creates a surface by extruding a curve to a point.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The identifier of the curve object to extrude.
    C{point}(array_of dbl, REQ) - A 3-D point.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_extrude_crv_straight = """
    Factory method:
    Creates a surface by extruding a curve straight along two points that define a line.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The identifier of the curve object to extrude.
    C{start_point}(array_of dbl, REQ) - A starting point.
    C{end_point}(array_of dbl, REQ) - A ending point.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_extrude_crv_tapered = """
    Factory method:
    Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The identifier of the curve object to extrude.
    C{distance}(dbl, REQ) - The extrusion distance.
    C{direction}(array_of dbl, REQ) - A 3-D vector that specifies the extrusion direction.
    C{base_point}(array_of dbl, REQ) - A 3-D point that specifies the base point of the extrusion.
    C{angle}(dbl, REQ) - The angle of the extrusion.
    C{corner_type}(int, OPT) - The corner type of the extrusion, where:
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
    array - An array of strings identifying the newly created surface objects if successful.
    null - If not successful, or on error.
    """
    create_by_fit = """
    Factory method:
    Reduces the number of surface control points while maintaining the surfaces' same general shape.  Use this function for replacing surface with too many control points.  For more information, see the Rhino help file for the FitSrf command.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The object's identifier.
    C{degree}(array_of int, OPT) - An array of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3.
    C{tolerance}(dbl, OPT) - The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class PlanarMesh():

    create_by_crv = """
    Factory method:
    Creates a planar mesh from a closed, planar curve.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The identifier of a closed, planar curve object.
    C{delete}(bln, OPT) - If True, then the input curve will be deleted. If not specified or False (default), then the input curve will not be deleted.
    Returns
    =======
    string - An string identifying the new object if successful.
    null - If not successful, or on error.
    """


class PlaneSurface():

    create = """
    Factory method:
    Creates a plane surface.
    Parameters
    ==========
    C{plane}(array_of dbl, REQ) - The plane.
    C{d_u}(dbl, REQ) - The magnitude in the U direction.
    C{d_v}(dbl, REQ) - The magnitude in the V direction.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class PolySurface():

    create_by_srf_extrude = """
    Factory method:
    Creates a surface or solid by extruding a straight along a path curve.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The identifier of the surface object to extrude.
    C{curve}(str, REQ) - The identifier of the path curve.
    C{cap}(bln, OPT) - Extrusion is capped at both ends to make a closed polysurface. The default value is True.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_srf_join = """
    Factory method:
    Joins two or more surface or polysurface object together to form one polysurface object.
    Parameters
    ==========
    C{surfaces}(array_of _ObjectRoot._SurfaceRoot, REQ) - An ordered array of strings identifying the surfaces or polysurfaces objects to join.
    C{delete}(bln, OPT) - Delete input objects after joining.  The default is not to delete objects (False).
    Returns
    =======
    string - The identifier of the newly created polysurface object if successful.
    null - If not successful, or on error.
    """


class Polyline():

    create = """
    Factory method:
    Adds a polyline curve object to the current model.
    Parameters
    ==========
    C{points}(array_of dbl, REQ) - An array of 3-D points.  Duplicate, consecutive points found in the array will be removed.  The array must contain at least two 3-D points.  If the array contains less than four points, then the first point and the last point must be different.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_crv = """
    Factory method:
    Converts a curve to a polyline curve.
    Parameters
    ==========
    C{curve}(_ObjectRoot._CurveRoot, REQ) - The object's identifier.
    C{angle_tolerance}(dbl, OPT) - The maximum angle between curve tangents at line endpoints.  If omitted, the angle tolerance is set to 5.0.
    C{tolerance}(dbl, OPT) - The distance tolerance at segment midpoints.  If omitted, the tolerance is set to 0.01.
    C{delete_input}(bln, OPT) - Delete the curve object specified by strObject.  If omitted, strObject will not be deleted.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Sphere():

    create = """
    Factory method:
    Adds a spherical surface to the document.
    Parameters
    ==========
    C{center}(array_of dbl, REQ) - The center point of the sphere.
    C{radius}(dbl, REQ) - An equatorial plane.  The origin of the plane will be the center point of the sphere.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_plane = """
    Factory method:
    Adds a spherical surface to the document.
    Parameters
    ==========
    C{center}(array_of dbl, REQ) - The center point of the sphere.
    C{radius}(dbl, REQ) - An equatorial plane.  The origin of the plane will be the center point of the sphere.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class Torus():

    create = """
    Factory method:
    Adds a torus-shaped revolved surface to the document.
    Parameters
    ==========
    C{base}(array_of dbl, REQ) - The 3-D origin point of the torus.
    C{major_radius}(dbl, REQ) - The base plane of the torus.
    C{minor_radius}(dbl, REQ) - The major radius of the torus.  The major radius must be larger than the minor radius.
    C{direction}(array_of dbl, OPT) - The minor radius of the torus.  The minor radius must be greater than zero.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    create_by_plane = """
    Factory method:
    Adds a torus-shaped revolved surface to the document.
    Parameters
    ==========
    C{plane}(array_of dbl, REQ) - The 3-D origin point of the torus.
    C{major_radius}(dbl, REQ) - The base plane of the torus.
    C{minor_radius}(dbl, REQ) - The major radius of the torus.  The major radius must be larger than the minor radius.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _ArcDupl():

    copy_by_sub = """
    Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    Parameters
    ==========
    C{param_0}(dbl, REQ) - The first parameter on the source curve.
    C{param_1}(dbl, REQ) - The second parameter on the source curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a curve by a distance. The offset curve will be added to Rhino.
    Parameters
    ==========
    C{direction}(array_of dbl, REQ) - The 3-D point that indicates the direction of the offset.
    C{distance}(dbl, REQ) - The distance of the offset.
    C{normal}(array_of dbl, OPT) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
    C{style}(int, OPT) - The corner style.  If omitted, a sharp corner style is used.
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
    array - An array containing the identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    copy_by_split = """
    Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    Parameters
    ==========
    C{parameters}(array_of dbl, REQ) - An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    array - An array containing the identifiers of the two newly created curve objects, if successful.
    null - If not successful, or on error.
    """
    copy_by_trim = """
    Trims a curve by removing portions of the curve outside the specified interval.
    Parameters
    ==========
    C{interval}(array_of int, REQ) - An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    string - The identifier of the newly created curve object, if successful.
    null - If not successful, or on error.
    """


class _ArcProp():

    angle = """
    Returns the angle of an arc curve object.
    Parameters
    ==========
    Returns
    =======
    number - The angle in degrees if successful.
    null - If not successful, or on error.
    """
    center_pnt = """
    Returns the center point of an arc curve object.
    Parameters
    ==========
    Returns
    =======
    null - If not successful, or on error.
    """
    mid_pnt = """
    Returns the mid point of an arc curve object.
    Parameters
    ==========
    Returns
    =======
    null - If not successful, or on error.
    """
    radius = """
    Returns the radius of an arc curve object.
    Parameters
    ==========
    Returns
    =======
    number - The radius of the arc if successful.
    null - If not successful, or on error.
    """


class _BoxDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _CircleDupl():

    copy_by_sub = """
    Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    Parameters
    ==========
    C{param_0}(dbl, REQ) - The first parameter on the source curve.
    C{param_1}(dbl, REQ) - The second parameter on the source curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a curve by a distance. The offset curve will be added to Rhino.
    Parameters
    ==========
    C{direction}(array_of dbl, REQ) - The 3-D point that indicates the direction of the offset.
    C{distance}(dbl, REQ) - The distance of the offset.
    C{normal}(array_of dbl, OPT) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
    C{style}(int, OPT) - The corner style.  If omitted, a sharp corner style is used.
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
    array - An array containing the identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    copy_by_split = """
    Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    Parameters
    ==========
    C{parameters}(array_of dbl, REQ) - An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    array - An array containing the identifiers of the two newly created curve objects, if successful.
    null - If not successful, or on error.
    """
    copy_by_trim = """
    Trims a curve by removing portions of the curve outside the specified interval.
    Parameters
    ==========
    C{interval}(array_of int, REQ) - An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    string - The identifier of the newly created curve object, if successful.
    null - If not successful, or on error.
    """


class _CircleProp():

    center_pnt = """
    Returns the center point of a circle curve object.
    Parameters
    ==========
    Returns
    =======
    array - The 3-D center point of the circle if successful.
    null - If not successful, or on error.
    """
    circumference = """
    Returns the circumference of a circle curve object.
    Parameters
    ==========
    Returns
    =======
    number - The circumference of the circle if successful.
    null - If not successful, or on error.
    """
    radius = """
    Returns the radius of a circle curve object.
    Parameters
    ==========
    Returns
    =======
    number - The radius of the circle if successful.
    null - If not successful, or on error.
    """


class _ConeDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _ConeProp():

    cone_def = """
    Returns the definition of a cone surface.
    Parameters
    ==========
    Returns
    =======
    array - An array containing the definition of the cone if successful.  The elements of the array are as follows:
    array - The plane of the cone.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
    number - The height of the cone.
    number - The radius of the cone.
    null - If not successful, or on error.
    """


class _CurveRoot():

    pass


class _CurveRootEval():

    curvature = """
    Returns the curvature of a curve at a parameter.  See the Rhino help file for details on curve curvature.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter to evaluate.
    Returns
    =======
    array - An array of curvature information if successful.  The array will contain the following information:
    number - Radius of curvature
    null - If not successful, or on error.
    """
    evaluate_derivatives = """
    A general purpose curve evaluator.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The evaluation parameter.
    C{derivative}(int, REQ) - The number of derivatives to evaluate.
    Returns
    =======
    array - An array of length (intDerivative+1) if successful.  The array elements are as follows:
    array - The 3-D point
    array - The first derivative
    array - The second derivative
    array - etc...
    null - If not successful, or on error.
    """
    frame = """
    Returns the plane at a parameter of a curve. The plane is based on the tangent and curvature vectors at a parameter.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter to evaluate.
    Returns
    =======
    array - The plane at the specified parameter if successful.
    null - If not successful, or on error.
    """
    perp_frame = """
    Returns the perpendicular plane at a parameter of a curve.  The result is relatively parallel (zero-twisting) plane.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter to evaluate.
    Returns
    =======
    array - The plane at the specified parameter if successful.
    null - If not successful, or on error.
    """
    tangent = """
    Returns a 3-D vector that is the tangent to a curve at a parameter.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter to evaluate.
    Returns
    =======
    array - A  3-D vector if successful.
    null - If not successful, or on error.
    """
    evaluate = """
    Evaluates a curve at a parameter.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter to evaluate.
    Returns
    =======
    array - A 3-D point if successful.
    null - If not successful, or on error.
    """


class _CurveRootFunc():

    crv_arc_length_pnt = """
    Returns the point on the curve that is a specified arc length from the start of the curve.
    Parameters
    ==========
    C{length}(dbl, REQ) - The arc length from the start of the curve to evaluate.
    C{from_start}(bln, OPT) - If not specified or True, then the arc length point is calculated from the start of the curve. If False, the arc length point is calculated from the end of the curve.
    Returns
    =======
    array - The 3-D point if successful.
    null - If not successful, or on error.
    """
    closest_pnt = """
    Returns the parameter of the point on a curve that is closest to a test point.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - The test, or sampling, point.
    Returns
    =======
    number - The parameter of the closest point on the curve if successful.
    null - If not successful, or on error.
    """
    contour_pnts = """
    Returns the 3-D point locations calculated by contouring a curve object.
    Parameters
    ==========
    C{start_point}(array_of dbl, REQ) - The 3-D starting point of a center line.
    C{end_point}(array_of dbl, REQ) - The 3-D ending point of a center line.
    C{interval}(dbl, OPT) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
    Returns
    =======
    array - An array of 3-D points, one for each contour, if successful.
    null - If not successful, or on error.
    """
    crv_intersection = """
    Calculates the intersection of two curve objects.
    Parameters
    ==========
    C{curve}(str, OPT) - The identifier of the second curve object.  If omitted, the a self-intersection test will be performed on strObject1.
    C{tolerance}(dbl, OPT) - The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
    Returns
    =======
    array - A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:
    number - The intersection event type, either Point (1) or Overlap (2).
    number - If the event type is Point (1), then the first curve parameter.
    number - If the event type is Point (1), then the first curve parameter.
    number - If the event type is Point (1), then the second curve parameter.
    number - If the event type is Point (1), then the second curve parameter.
    null - If not successful, or on error.
    """
    deviation = """
    Returns the minimum and maximum deviation between two curve objects. For more information on curve deviation, see the Rhino help file for the CrvDeviation command.
    Parameters
    ==========
    C{curve_a}(str, REQ) - The identifier of the second curve object.
    Returns
    =======
    array - An array of numbers identifying the minimum and maximum deviation between the two curves if successful.
    number - Curve A parameter at maximum overlap distance point
    number - Curve A parameter at maximum overlap distance point
    number - Maximum overlap distance
    number - Curve A parameter at minimum distance point
    number - Curve B parameter at minimum distance point
    number - Minimum distance between curves
    null - On error or if no intervals of overlap were found.
    """
    directions_match = """
    Tests if two curve objects are generally in the same direction or if they would be more in the same direction if one of them were flipped. When testing curve directions, both curves must be either open or closed - you cannot test one open curve and one closed curve.
    Parameters
    ==========
    C{curve_1}(str, REQ) - The identifier of the second curve to compare.
    Returns
    =======
    boolean - True if the curve directions match, otherwise False.
    null - On error.
    """
    radius = """
    Returns the radius of curvature at a point on a curve.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - The test, or sampling, point.
    Returns
    =======
    number - The radius of curvature at the point on the curve if successful.
    null - If not successful, or on error.
    """
    srf_intersection = """
    Calculates the intersection of a curve object with a surface object. Note, this function works on the untrimmed portion of the surface.
    Parameters
    ==========
    C{surface}(str, REQ) - The identifier of a surface object.
    C{tolerance}(dbl, OPT) - The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
    C{angle_tolerance}(dbl, OPT) - The angle tolerance in degrees.  The angle tolerance is used to determine when the curve is tangent to the surface.  If omitted, the document's current angle tolerance is used.
    Returns
    =======
    array - A two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:
    number - The intersection event type, either Point (1) or Overlap (2).
    number - If the event type is Point (1), then the curve parameter.
    number - If the event type is Point (1), then the curve parameter.
    number - If the event type is Point (1), then the U surface parameter.
    number - If the event type is Point (1), then the V surface parameter.
    number - If the event type is Point (1), then the U surface parameter.
    number - If the event type is Point (1), then the V surface parameter.
    null - If not successful, or on error.
    """
    divide_crv = """
    Divides a curve object into a specified number of segments.
    Parameters
    ==========
    C{segments}(lng, REQ) - The number of segments.
    C{create}(bln, OPT) - Create the division points. If omitted or False, points are not created.
    C{points}(bln, OPT) - Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
    Returns
    =======
    array - If blnPoints is not specified or True, then an array containing 3-D division points if successful.
    array - If blnPoints is False, then an array containing division curve parameters if successful.
    null - If not successful, or on error.
    """
    divide_crv_equidistant = """
    Divides a curve such that the linear distance between the points is equal.
		Unlike the DivideCurve and DivideCurveLength, which divides a curve based on arc length, or the distance along the curve between two points, this function divides a curve based on the linear distance between points.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The linear distance between division points.
    C{create}(bln, OPT) - Create the division points. If omitted or False, points are not created.
    C{points}(bln, OPT) - Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
    Returns
    =======
    array - If blnPoints is not specified or True, then an array containing 3-D division points if successful.
    array - If blnPoints is False, then an array containing division curve parameters if successful.
    null - If not successful, or on error.
    """
    divide_crv_length = """
    Divides a curve object into segments of a specified length.
    Parameters
    ==========
    C{length}(dbl, REQ) - The length of each segment.
    C{create}(bln, OPT) - Create the division points. If omitted or False, points are not created.
    C{points}(bln, OPT) - Return an array of 3-D points. If omitted or True, points are returned. If False, then an array of curve parameters are returned.
    Returns
    =======
    array - If blnPoints is not specified or True, then an array containing 3-D division points if successful.
    array - If blnPoints is False, then an array containing division curve parameters if successful.
    null - If not successful, or on error.
    """
    line_fit_from_pnts = """
    Returns the starting and ending points of a line that was fit through an array of 3-D points.
    Parameters
    ==========
    Returns
    =======
    array - An array containing the starting and ending points of the fit line if successful.
    null - If not successful, or on error.
    """
    make_non_periodic = """
    Makes a periodic curve non-periodic.  Non-periodic curves can develop kinks when deformed.
    Parameters
    ==========
    Returns
    =======
    string - If blnDelete is False, the identifier of the new object if successful.
    string - If blnDelete is True, the identifier of the modified object if successful.
    null - If not successful, or on error.
    """
    make_periodic = """
    Makes an existing curve a periodic NURBS curve.  A periodic NURBS curve is a closed curve with a simple knot at the seam.  If a joined curve is made periodic, it becomes a single-span curve and can no longer be exploded.
    Parameters
    ==========
    Returns
    =======
    string - If blnDelete is False, the identifier of the new object if successful.
    string - If blnDelete is True, the identifier of the modified object if successful.
    null - If not successful, or on error.
    """
    planar_crv_collision = """
    Determines if two coplanar curves intersect.
    Parameters
    ==========
    C{curve}(str, REQ) - The object identifier of the second planar curve.
    C{plane}(array_of dbl, OPT) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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
    C{tolerance}(dbl, OPT) - The tolerance.  If omitted, the current document absolute tolerance is used.
    Returns
    =======
    null - On error.
    """


class _CurveRootFuncClsd():

    closed_crv_area = """
    Returns that area of closed planar curves. The results are based on the current drawing units.
    Parameters
    ==========
    C{objects}(array_of _ObjectRoot, REQ) - An array of strings containing the identifiers of one or more closed, planar curve objects.
    Returns
    =======
    array - An array of area information if successful.  The array will contain the following information:
    number - The area. If more than one curve was specified, the value will be the cumulative area.
    number - The absolute (+/-) error bound for the area.
    null - If not successful, or on error.
    """
    closed_crv_area_centroid = """
    Returns that area centroid of closed, planar curves. The results are based on the current drawing units.
    Parameters
    ==========
    C{objects}(array_of _ObjectRoot, REQ) - An array of strings containing the identifiers of one or more closed, planar curve objects.
    Returns
    =======
    array - An array of area centroid information if successful.  The array will contain the following information:
    null - If not successful, or on error.
    """
    boolean_difference = """
    Calculates the difference between two closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    Parameters
    ==========
    C{curve}(str, REQ) - The identifier of the second curve object.
    Returns
    =======
    array - The identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    boolean_intersection = """
    Calculates the intersection of two closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    Parameters
    ==========
    C{curve_a}(str, REQ) - The identifier of the second curve object.
    Returns
    =======
    array - The identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    boolean_union = """
    Calculates the union of two or more closed, planar curves and adds the results to the document. Note, curves must be coplanar.
    Parameters
    ==========
    C{curves}(array_of _ObjectRoot, REQ) - The identifiers of two or more curve objects.
    Returns
    =======
    array - The identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    closed_crv_containment = """
    Determines the relationship between the regions bounded by two coplanar simple closed curves.
    Parameters
    ==========
    C{curve__1}(str, REQ) - The object identifier of the second planar, closed curve.
    C{plane}(array_of dbl, OPT) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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
    C{tolerance}(dbl, OPT) - The tolerance.  If omitted, the current document absolute tolerance is used.
    Returns
    =======
    number - A number identifying the relationship if successful.  The possible values are as follows:
    null - If not successful, or on error.
    """
    closed_crv_pnt_inside = """
    Determines if a point is inside of a closed curve, on  a closed curve, or outside of a closed curve.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - A 3-D point to test.
    C{plane}(array_of dbl, OPT) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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
    C{tolerance}(dbl, OPT) - The tolerance.  If omitted, the current document absolute tolerance is used.
    Returns
    =======
    number - A number identifying the result if successful.  The possible values are as follows:
    null - If not successful, or on error.
    """


class _CurveRootFuncOorc():

    pass


class _CurveRootFuncOpen():

    open_crv_close = """
    Closes an open curve object by making adjustments to the end points so that they meet at a point.
    Parameters
    ==========
    C{tolerance}(dbl, OPT) - The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.
    Returns
    =======
    string - The identifier of the closed curve object if successful.
    null - If not successful, or on error.
    """
    open_crv_extend = """
    Extends a non-closed curve object by a line, arc, or smooth extension until it intersects a collection of objects.
    Parameters
    ==========
    C{crv_type}(int, REQ) - Type of extension.
		Value
		Description
		0
		Line - Creates an line extension tangent to the original curve.
		1
		Arc - Creates an arc extension tangent to the original curve.
		2
    C{side}(int, REQ) - The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
    C{objects}(array_of _ObjectRoot, REQ) - The identifiers of curve, surface, and polysurface objects that will be used as boundary objects.
    Returns
    =======
    string - The identifier of the extended object if successful.
    null - If not successful, or on error.
    """
    open_crv_extend_length = """
    Extends a non-closed curve object by a line, arc, or smooth extension for a specified distance.
    Parameters
    ==========
    C{crv_type}(int, REQ) - Type of extension.
		Value
		Description
		0
		Line - Creates an line extension tangent to the original curve.
		1
		Arc - Creates an arc extension tangent to the original curve.
		2
    C{side}(int, REQ) - The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
		Extend from the end of the curve.
		2
    C{length}(dbl, REQ) - The distance to extend the curve.
    Returns
    =======
    string - The identifier of the extended object if successful.
    null - If not successful, or on error.
    """
    open_crv_extend_pnt = """
    Extends a non-closed curve object by smooth extension to a point.
    Parameters
    ==========
    C{side}(int, REQ) - The size to  extent.
		Value
		Description
		0
		Extend from the start of the curve.
		1
    C{point}(array_of dbl, REQ) - The 3-D point.
    Returns
    =======
    string - The identifier of the extended object if successful.
    null - If not successful, or on error.
    """


class _CurveRootMdfy():

    seam = """
    Adjusts the seam, or start/end, point of a closed curve.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter of the new start/end point. Note, if successful, the resulting curve's domain will start at dblParameter.
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """
    fair = """
    Fairs a curve object. Fair works best on degree 3 (cubic) curves. Fair attempts to remove large curvature variations while limiting the geometry changes to be no more than the specified tolerance. Sometimes several applications of this method are necessary to remove nasty curvature problems.
    Parameters
    ==========
    C{tolerance}(dbl, OPT) - The fairing tolerance. Of omitted, a default value of 1.0 is used.
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """
    insert_knot = """
    Inserts a knot into a curve object.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter on the curve.
    C{symmetrical}(bln, OPT) - If blnSymmetrical = True, then knots are added on both sides of the center of the curve. The default value is False.
    Returns
    =======
    boolean - True of False indicating success or failure.
    null - On error.
    """
    rebuild = """
    Rebuilds a curve to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.
    Parameters
    ==========
    C{degree}(int, OPT) - The new degree, which must be greater than 1. The default is 3.
    C{point_count}(int, OPT) - The new point count, which must be bigger than the intDegree.  With closed curves, the minimum point count is 3.
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """
    remove_knot = """
    Deletes a knot from a curve object.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - The parameter on the curve.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
    Returns
    =======
    boolean - True of False indicating success or failure.
    null - On error.
    """
    reverse = """
    Reverses the direction of a curve object. This feature can also be found in Rhino's Dir command.
    Parameters
    ==========
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """
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
    C{flags}(int, OPT) - The simplification methods to use. By default, all methods are used (intFlags = 0). The possible options are as follows:
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
    null - On error.
    """


class _CurveRootProp():

    arrows = """
    Enables or disabled a curve object's annotation arrows.
    Parameters
    ==========
    C{style}(int, OPT) - The style of annotation arrows to be displayed.  The styles are as follows:
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
    number - If intStyle is not specified, the current annotation arrow style if successful.
    number - If intStyle is specified, the previous annotation arrow style if successful.
    null - If not successful, or on error.
    """
    degree = """
    Returns the degree of a curve object.
    Parameters
    ==========
    Returns
    =======
    number - The degree of the curve if successful.
    null - If not successful, or on error.
    """
    dim = """
    Returns the dimension of a curve object.
    Parameters
    ==========
    Returns
    =======
    number - The dimension of the curve if successful.
    null - If not successful, or on error.
    """
    discontinuity = """
    Search for a derivatitive, tangent, or curvature discontinuity in a curve object.
    Parameters
    ==========
    C{style}(int, REQ) - The type of continuity to test for.  The types of continuity are as follows:
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
    array - An array of 3-D points where the curve is discontinuous if successful.
    null - If not successful, or on error.
    """
    domain = """
    Returns the domain of a curve object.
    Parameters
    ==========
    Returns
    =======
    array - The domain of the curve if successful.
    null - If not successful, or on error.
    """
    edit_pnts = """
    Returns the edit, or Greville, points of a curve object.  For each curve control point, there is a corresponding edit point.
    Parameters
    ==========
    C{return_parameters}(bln, OPT) - Return the edit points as an array of parameter values.  If omitted, the edit points are returned as an array of 3-D points.
    Returns
    =======
    array - If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.
    array - If blnReturnParameters is True, then an array of parameter values if successful.
    null - If not successful, or on error.
    """
    end_pnt = """
    Returns the end point of a curve object.
    Parameters
    ==========
    Returns
    =======
    array - The 3-D end point of the curve if successful.
    null - If not successful, or on error.
    """
    knot_count = """
    Returns the knot count of a curve object.
    Parameters
    ==========
    Returns
    =======
    number - The number of knots if successful.
    null - If not successful, or on error.
    """
    knots = """
    Returns the knots, or knot vector, of a curve object.
    Parameters
    ==========
    Returns
    =======
    array - The knot values of the curve  if successful.
    null - If not successful, or on error.
    """
    length = """
    Returns the length of a curve object.
    Parameters
    ==========
    C{sub_domain}(array_of int, OPT) - An array of two numbers identifying the sub-domain of the curve on which the calculation will be performed.  The two parameters (sub-domain) must be non-decreasing.  If omitted, the length of the entire curve is returned.
    Returns
    =======
    number - The length of the curve if successful.
    null - If not successful, or on error.
    """
    mid_pnt = """
    Returns the mid point of a curve object.
    Parameters
    ==========
    Returns
    =======
    array - The 3-D mid point of the curve if successful.
    null - If not successful, or on error.
    """
    normal = """
    Returns the normal direction of the plane in which a planar curve object lies.
    Parameters
    ==========
    Returns
    =======
    array - The 3-D normal vector if successful.
    null - If not successful, or on error.
    """
    plane = """
    Returns the plane in which a planar curve lies. Note, this function works only on planar curves.
    Parameters
    ==========
    Returns
    =======
    array - The plane in which the curve lies if successful.
    null - On error.
    """
    control_pnt_count = """
    Returns the control points count of a curve object.
    Parameters
    ==========
    Returns
    =======
    number - The number of control points if successful.
    null - If not successful, or on error.
    """
    control_pnts = """
    Returns the control points, or control vertices, of a curve object.  If the curve is a rational NURBS curve, the euclidean control vertices are returned.
    Parameters
    ==========
    Returns
    =======
    array - The control points of the curve if successful.
    null - If not successful, or on error.
    """
    start_pnt = """
    Returns the start point of a curve object.
    Parameters
    ==========
    Returns
    =======
    array - The 3-D starting point of the curve if successful.
    null - If not successful, or on error.
    """
    weights = """
    Returns an array of weight values that are assigned to the control points of a curve.
    Parameters
    ==========
    Returns
    =======
    array - The weight values of the curve if successful.
    null - If not successful, or on error.
    """


class _CurveRootPropClsd():

    pass


class _CurveRootPropOorc():

    pass


class _CurveRootPropOpen():

    pass


class _CurveRootTest():

    is_closable = """
    Decide if it makes sense to close off the curve by moving  the endpoint to the start based on start-end gap size and length of curve as approximated by chord defined by 6 points.
    Parameters
    ==========
    C{tolerance}(dbl, OPT) - The maximum allowable distance between start point and end point of the curve.  If omitted, the document's current absolute tolerance is used.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_closed = """
    Verifies an object is a closed curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    in_plane = """
    Test a curve to see if it lies in a specific plane.
    Parameters
    ==========
    C{plane}(array_of dbl, OPT) - The new construction plane.  If omitted, the currently active construction plane is used.  The elements of a construction plane array are as follows:
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
    null - If not successful, or on error.
    """
    is_linear = """
    Verifies an object is a linear curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_periodic = """
    Verifies an object is a periodic curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_planar = """
    Verifies an object is a planar curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_rational = """
    Verifies an object is a rational NURBS curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_on_crv = """
    Verifies that a point is on a curve.
    Parameters
    ==========
    C{point}(array_of int, REQ) - The test, or sampling, point.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """


class _CurveRootType():

    is_arc = """
    Verifies an object is an arc curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_circle = """
    Verifies an object is a circle curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_crv = """
    Verifies an object is a curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_ellipse = """
    Verifies an object is an elliptical-shaped curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_line = """
    Verifies an object is a line curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_poly_crv = """
    Verifies an object is a polycurve object.  A polycurve is a curve that is represented by a sequence of contiguous curve segments.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_polyline = """
    Verifies an object is a polyline curve object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """


class _CylinderDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _CylinderProp():

    cylinder_def = """
    Returns the definition of a cylinder surface.
    Parameters
    ==========
    Returns
    =======
    array - An array containing the definition of the cylinder if successful.  The elements of the array are as follows:
    array - The base plane of the cylinder.
    number - The height of the cylinder.
    number - The radius of the cylinder.
    null - If not successful, or on error.
    """


class _EllipseDupl():

    copy_by_sub = """
    Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    Parameters
    ==========
    C{param_0}(dbl, REQ) - The first parameter on the source curve.
    C{param_1}(dbl, REQ) - The second parameter on the source curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a curve by a distance. The offset curve will be added to Rhino.
    Parameters
    ==========
    C{direction}(array_of dbl, REQ) - The 3-D point that indicates the direction of the offset.
    C{distance}(dbl, REQ) - The distance of the offset.
    C{normal}(array_of dbl, OPT) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
    C{style}(int, OPT) - The corner style.  If omitted, a sharp corner style is used.
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
    array - An array containing the identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    copy_by_split = """
    Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    Parameters
    ==========
    C{parameters}(array_of dbl, REQ) - An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    array - An array containing the identifiers of the two newly created curve objects, if successful.
    null - If not successful, or on error.
    """
    copy_by_trim = """
    Trims a curve by removing portions of the curve outside the specified interval.
    Parameters
    ==========
    C{interval}(array_of int, REQ) - An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    string - The identifier of the newly created curve object, if successful.
    null - If not successful, or on error.
    """


class _EllipseProp():

    center_pnt = """
    Returns the center point of an elliptical-shaped curve object.
    Parameters
    ==========
    Returns
    =======
    array - The 3-D center point of the ellipse if successful.
    null - If not successful, or on error.
    """
    quad_pnts = """
    Returns the quadrant points of an elliptical-shaped curve object.
    Parameters
    ==========
    Returns
    =======
    array - An array of 3-D points identifying the quadrants of the ellipse if successful.
    null - If not successful, or on error.
    """


class _EllipticalArcDupl():

    copy_by_sub = """
    Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    Parameters
    ==========
    C{param_0}(dbl, REQ) - The first parameter on the source curve.
    C{param_1}(dbl, REQ) - The second parameter on the source curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a curve by a distance. The offset curve will be added to Rhino.
    Parameters
    ==========
    C{direction}(array_of dbl, REQ) - The 3-D point that indicates the direction of the offset.
    C{distance}(dbl, REQ) - The distance of the offset.
    C{normal}(array_of dbl, OPT) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
    C{style}(int, OPT) - The corner style.  If omitted, a sharp corner style is used.
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
    array - An array containing the identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    copy_by_split = """
    Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    Parameters
    ==========
    C{parameters}(array_of dbl, REQ) - An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    array - An array containing the identifiers of the two newly created curve objects, if successful.
    null - If not successful, or on error.
    """
    copy_by_trim = """
    Trims a curve by removing portions of the curve outside the specified interval.
    Parameters
    ==========
    C{interval}(array_of int, REQ) - An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    string - The identifier of the newly created curve object, if successful.
    null - If not successful, or on error.
    """


class _LineDupl():

    copy_by_sub = """
    Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    Parameters
    ==========
    C{param_0}(dbl, REQ) - The first parameter on the source curve.
    C{param_1}(dbl, REQ) - The second parameter on the source curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a curve by a distance. The offset curve will be added to Rhino.
    Parameters
    ==========
    C{direction}(array_of dbl, REQ) - The 3-D point that indicates the direction of the offset.
    C{distance}(dbl, REQ) - The distance of the offset.
    C{normal}(array_of dbl, OPT) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
    C{style}(int, OPT) - The corner style.  If omitted, a sharp corner style is used.
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
    array - An array containing the identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    copy_by_split = """
    Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    Parameters
    ==========
    C{parameters}(array_of dbl, REQ) - An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    array - An array containing the identifiers of the two newly created curve objects, if successful.
    null - If not successful, or on error.
    """
    copy_by_trim = """
    Trims a curve by removing portions of the curve outside the specified interval.
    Parameters
    ==========
    C{interval}(array_of int, REQ) - An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    string - The identifier of the newly created curve object, if successful.
    null - If not successful, or on error.
    """


class _MeshDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.
    Parameters
    ==========
    C{mesh}(_ObjectRoot._MeshRoot, REQ) - The identifier of a mesh object.
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the offset mesh object if successful.
    null - If not successful, or on error.
    """


class _MeshRoot():

    pass


class _MeshRootFunc():

    curve_intersection = """
    Calculates the intersection of a curve object and a mesh object.
    Parameters
    ==========
    C{mesh}(str, REQ) - The identifier of the mesh to intersect.
    C{return_faces}(bln, OPT) - Return both intersection points and face indices.  If omitted or False, then just the intersection points are returned.
    Returns
    =======
    array - If blnReturnFaces is either omitted or False, then an array intersection points, if successful.
    array - If blnReturnFaces is True, then a one-dimensional array containing information about each intersection if successful.  Each array element is a one-dimensional array that contains the following two elements:
    array - The 3-D intersection point.
    number - The mesh face index on which the intersection point lies.
    null - If not successful, or on error.
    """
    explode = """
    Explodes a mesh object, or mesh objects,  into submeshes.  A submesh is a collection of mesh faces that are contained within a closed loop of unwelded mesh edges.  Unwelded mesh edges are edges where the mesh faces that share the edge have unique mesh vertices (not mesh topology vertices) at both ends of the edge.
    Parameters
    ==========
    C{delete}(bln, OPT) - Delete input objects after exploding.  The default is not to delete objects (False).
    Returns
    =======
    array - An array of strings identifying the newly created mesh objects if successful.
    null - If not successful, or on error.
    """
    closest_point = """
    Returns the point on a mesh that is closest to a test point.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - A 3-D point to test.
    C{tolerance}(dbl, OPT) - The tolerance. Of omitted, a default tolerance of 0.0 is used.
    Returns
    =======
    array - An array containing the results of the calculation, if successful. The array elements are as follows:
    array - The 3-D point on the mesh object.
    number - The index of the mesh face on which the 3-D point lies.
    null - If not successful, or on error.
    """
    contour_points = """
    Returns the vertices of the polyline curves generated by contouring a mesh object.
    Parameters
    ==========
    C{start_point}(array_of dbl, REQ) - The 3-D starting point of a center line.
    C{end_point}(array_of dbl, REQ) - The 3-D ending point of a center line.
    C{interval}(dbl, OPT) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
    C{remove_coincident_points}(bln, OPT) - Remove coincident points.  If True, and the polyline curves from which the contour point are taken are closed, then duplicate starting and ending points of the polyline curve will not be returned. The default is to return duplicate starting and ending points (False).
    Returns
    =======
    array - An array of 3-D point arrays, one for each contour, if successful.
    null - If not successful, or on error.
    """
    mesh_intersection = """
    Calculates the intersection of a mesh object with another mesh object.
    Parameters
    ==========
    C{mesh_1}(str, REQ) - The identifier of the second mesh object.
    C{tolerance}(dbl, OPT) - The intersection tolerance. Of omitted, Rhino's internal zero tolerance is used.
    Returns
    =======
    array - An array of 3-D point arrays that identify the vertices of the intersection curves (polylines) if successful.
    null - If not successful, or on error.
    """
    naked_edge_points = """
    Identifies the naked edge points of a polygon mesh object. This function shows where polygon mesh vertices are not completely surrounded by faces. Joined meshes, such as are made by Mesh Box, have naked mesh edge points where the sub-meshes are joined.
    Parameters
    ==========
    Returns
    =======
    array - An array of boolean values that represent whether or not a mesh vertex is naked or not if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the naked status for each vertex return by MeshVertices.
    null - If not successful, or on error.
    """
    split_disjoint_mesh = """
    Splits up a mesh object into its unconnected pieces.
    Parameters
    ==========
    C{delete}(bln, OPT) - Delete the input object. The default is not to delete the input object (False).
    Returns
    =======
    array - An array of strings identifying the newly created mesh objects if successful.
    null - If not successful, or on error.
    """
    unify_normals = """
    Fixes inconsistencies in the directions of faces of a mesh object.
    Parameters
    ==========
    Returns
    =======
    number - The number of faces that were modified if successful.
    null - If not successful, or on error.
    """


class _MeshRootFuncClsd():

    boolean_difference = """
    Performs a Boolean difference operation on two sets of input meshes. For more details, see the MeshBooleanDifference command in the Rhino help file.
    Parameters
    ==========
    C{meshes}(array_of str, REQ) - The identifiers of the meshes.
    C{delete}(bln, OPT) - Delete all input objects. The default is to delete all input objects (True).
    Returns
    =======
    array - An array containing the identifiers of the newly created objects, if successful.
    null - If not successful, or on error.
    """
    boolean_intersection = """
    Performs a Boolean intersection operation on two sets of input meshes. For more details, see the MeshBooleanIntersection command in the Rhino help file.
    Parameters
    ==========
    C{meshes}(array_of str, REQ) - The identifiers of the meshes.
    C{delete}(bln, OPT) - Delete all input objects. The default is to delete all input objects (True).
    Returns
    =======
    array - An array containing the identifiers of the newly created objects, if successful.
    null - If not successful, or on error.
    """
    boolean_split = """
    Performs a Boolean split operation on two sets of input meshes. For more details, see the MeshBooleanSplit command in the Rhino help file.
    Parameters
    ==========
    C{input_1}(array_of str, REQ) - The identifiers of the meshes.
    C{delete}(bln, OPT) - Delete all input objects. The default is to delete all input objects (True).
    Returns
    =======
    array - An array containing the identifiers of the newly created objects, if successful.
    null - If not successful, or on error.
    """
    boolean_union = """
    Performs a Boolean union operation on a set of input meshes. For more details, see the MeshBooleanUnion command in the Rhino help file.
    Parameters
    ==========
    C{meshes}(array_of _ObjectRoot, REQ) - The identifiers of the meshes to union.
    C{delete}(bln, OPT) - Delete all input objects. The default is to delete all input objects (True).
    Returns
    =======
    array - An array containing the identifiers of the newly created objects, if successful.
    null - If not successful, or on error.
    """


class _MeshRootFuncOorc():

    pass


class _MeshRootFuncOpen():

    pass


class _MeshRootMdfy():

    quads_to_triangles = """
    Converts a mesh object's quad faces to triangles.
    Parameters
    ==========
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """


class _MeshRootProp():

    disjoint_mesh_count = """
    Returns the number of meshes that could be created by calling SplitDisjointMesh.
    Parameters
    ==========
    Returns
    =======
    number - The number of meshes that could be created if successful.
    null - If not successful, or on error.
    """
    area = """
    Returns the approximate area of one or more mesh objects.
    Parameters
    ==========
    Returns
    =======
    array - An array containing three numbers if successful.  The three elements of the array are as follows:
    number - The number of meshes used in the area calculation.
    number - The total area of all meshes.
    number - The error estimate.
    null - If not successful, or on error.
    """
    area_centroid = """
    Calculates the area centroid of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - A 3-D point identifying the area centroid if successful.
    null - If not successful, or on error.
    """
    face_centers = """
    Returns the center point of each face of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - An array of 3-D points that define the face center points of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the center points for each face return by MeshFaces.
    null - If not successful, or on error.
    """
    face_count = """
    Returns the total face count of a mesh object.
    Parameters
    ==========
    Returns
    =======
    number - The number of mesh faces if successful
    null - If not successful, or on error.
    """
    face_normals = """
    Returns the face unit normal for each face of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - An array of 3-D vectors that define the face unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshFaceCount. In which case, the array will identify the unit normals for each face return by MeshFaces.
    null - If not successful, or on error.
    """
    face_vertices = """
    Returns the vertex indices of all faces of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - An array containing arrays of four numbers that define the vertex indices for each face of the mesh if successful.  Both quad and triangle faces are returned. If the third and forth vertex indices of a face are identical, the face is a triangle. Otherwise the face is a quad.
    null - If not successful, or on error.
    """
    faces = """
    Returns the face vertices of a mesh object.
    Parameters
    ==========
    C{face_type}(bln, OPT) - The face type to be returned.  If omitted, both triangles and quads are returned (True)
		Value
		Description
		True
		Both triangles and quads.
		False
    Returns
    =======
    array - An array of 3-D points that define the face vertices of the mesh if successful.  If blnFaceType is True, then faces are returned as both quads and triangles (4 3-D points).  For triangles, the third and forth vertex will be identical.  If blnFaceType is False, then faces are returned as only triangles (3 3-D points).  Quads will be converted to triangles.
    null - If not successful, or on error.
    """
    quad_count = """
    Returns the number of quad faces of a mesh object.
    Parameters
    ==========
    Returns
    =======
    number - The number of quad mesh faces if successful
    null - If not successful, or on error.
    """
    texture_coordinates = """
    Returns the normalized 2-D texture coordinates of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - An array of 2-D points that define the texture coordinates of the mesh if successful.  Each 2-D point is normalized, that is, each coordinate component ranges in value between 0 and 1.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the texture coordinate for each vertex return by MeshVertices.
    null - If the mesh does not contain texture coordinates, if not successful, or on error.
    """
    triangle_count = """
    Returns the number of triangular faces of a mesh object.
    Parameters
    ==========
    Returns
    =======
    number - The number of triangular mesh faces if successful
    null - If not successful, or on error.
    """
    vertex_colors = """
    Returns or modifies the  vertex colors of a mesh object
    Parameters
    ==========
    C{vertex_colors}(array_of int, OPT) - An array of RGB color values. Note, for every vertex, there must be a corresponding vertex color.
    Returns
    =======
    array - If arrVertexColors  is not specified,  the current vertex color if successful.
    array - If arrVertexColors  is specified, the previous vertex colors if successful.
    null - If strObject does not have vertex colors, if not successful, or on error.
    """
    vertex_count = """
    Returns the vertex count of a mesh object.
    Parameters
    ==========
    Returns
    =======
    number - The number of mesh vertices if successful
    null - If not successful, or on error.
    """
    vertex_normals = """
    Returns the vertex unit normal for each vertex of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - An array of 3-D vectors that define the vertex unit normals of the mesh if successful.  The number of elements in the array will be equal to the value returned by MeshVertexCount. In which case, the array will identify the unit normals for each vertex return by MeshVertices.
    null - If the mesh does not contain vertex normals, if not successful, or on error.
    """
    vertices = """
    Returns the vertices of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - An array of 3-D points that define the vertices of the mesh if successful.
    null - If not successful, or on error.
    """


class _MeshRootPropClsd():

    mesh_volume = """
    Returns the approximate volume of one or more closed mesh objects.
    Parameters
    ==========
    C{objects}(array_of str, REQ) - An array of object identifier.
    Returns
    =======
    array - An array containing three numbers if successful.  The three elements of the array are as follows:
    number - The number of meshes used in the volume calculation.
    number - The total volume of all meshes.
    number - The error estimate.
    null - If not successful, or on error.
    """
    mesh_volume_centroid = """
    Calculates the volume centroid of a mesh object.
    Parameters
    ==========
    Returns
    =======
    array - A 3-D point identifying the volume centroid if successful.
    null - If not successful, or on error.
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
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_manifold = """
    Verifies a mesh object is manifold.  A mesh for which every edge is shared by at most two faces is called a manifold.  If a mesh has at least one edge that is shared by more than two faces, then that mesh is called non-manifold.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    has_face_normals = """
    Verifies a mesh object has face normals.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    has_texture_coordinates = """
    Verifies a mesh object has texture coordinates.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    has_vertex_colors = """
    Verifies a mesh object has vertex colors.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    has_vertex_normals = """
    Verifies a mesh object has vertex normals.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """


class _MeshRootType():

    is_mesh = """
    Verifies an object is a mesh object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """


class _NurbsCurveDupl():

    copy_by_sub = """
    Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    Parameters
    ==========
    C{param_0}(dbl, REQ) - The first parameter on the source curve.
    C{param_1}(dbl, REQ) - The second parameter on the source curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a curve by a distance. The offset curve will be added to Rhino.
    Parameters
    ==========
    C{direction}(array_of dbl, REQ) - The 3-D point that indicates the direction of the offset.
    C{distance}(dbl, REQ) - The distance of the offset.
    C{normal}(array_of dbl, OPT) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
    C{style}(int, OPT) - The corner style.  If omitted, a sharp corner style is used.
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
    array - An array containing the identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    copy_by_offset_on_srf = """
    Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The surface object's identifier.
    C{distance}(dbl, REQ) - The distance of the offset.  Based on the curve's direction, a possitive value will offset to the left and a negative value will offset to the right.
    Returns
    =======
    array - An array containing the identifiers of the new curve objects if successful.
    null - If not successful, or on error.
    """
    copy_by_offset_on_srf_param = """
    Offset a curve on a surface.  The source curve must lie on the surface. The offset curve or curves will be added to Rhino.
    Parameters
    ==========
    C{surface}(_ObjectRoot._SurfaceRoot, REQ) - The surface object's identifier.
    C{parameter}(array_of dbl, REQ) - The distance of the offset.  Based on the curve's direction, a possitive value will offset to the left and a negative value will offset to the right.
    Returns
    =======
    array - An array containing the identifiers of the new curve objects if successful.
    null - If not successful, or on error.
    """
    copy_by_split = """
    Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    Parameters
    ==========
    C{parameters}(array_of dbl, REQ) - An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    array - An array containing the identifiers of the two newly created curve objects, if successful.
    null - If not successful, or on error.
    """
    copy_by_trim = """
    Trims a curve by removing portions of the curve outside the specified interval.
    Parameters
    ==========
    C{interval}(array_of int, REQ) - An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    string - The identifier of the newly created curve object, if successful.
    null - If not successful, or on error.
    """


class _NurbsSurfaceDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _ObjectRoot():

    pass


class _ObjectRootDefm():

    box_morph = """
    Morphs an object by mapping its eight bounding box points to eight new points. Note, this function only works on non-planar objects.
    Parameters
    ==========
    C{box_points}(array_of dbl, REQ) - An array of eight 3-D points that contain the modified bounding box points.
    C{copy}(bln, OPT) - Copy the object. If omitted, the object will not be copied (False).
    Returns
    =======
    string - The identifier of the morphed object if successful.
    array - An array of strings identifying the morphed objects if successful.
    null - If not successful, or on error.
    """
    shear = """
    Performs a shear transformation on a single object. Transformation is based on the active construction plane.
    Parameters
    ==========
    C{origin}(array_of dbl, REQ) - The origin of the shear transformation.
    C{ref_pt}(array_of dbl, REQ) - The reference point of the shear transformation.
    C{angle}(dbl, REQ) - An angle in degrees of the shear transformation, where -90.0 <= angle <= 90.0.
    C{copy}(bln, OPT) - Copy the object. If omitted, the object will not be copied (False).
    Returns
    =======
    string - The identifier of the sheared object if successful.
    null - If not successful, or on error.
    """
    trfm = """
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
    C{matrix}(array_of str, REQ) - The transformation matrix (4x4 array of numbers).
    C{copy}(bln, OPT) - Copy the object. If omitted, the object will not be copied (False).
    Returns
    =======
    boolean - The identifier of the transformed object if successful.
    null - If not successful, or on error.
    """


class _ObjectRootFunc():

    delete = """
    Deletes one or more objects from the document.
    Parameters
    ==========
    Returns
    =======
    number - The number of objects deleted if successful.
    null - If not successful, or on error.
    """


class _ObjectRootGrps():

    groups = """
    Returns all of the group names that an object is assigned.
    Parameters
    ==========
    Returns
    =======
    array - An array of all group names for the object if successful.
    null - If not successful, or on error.
    """
    top_group = """
    Returns the top most group name that an object is assigned.  This function primarily applies to objects that are members of nested groups.
    Parameters
    ==========
    Returns
    =======
    string - The top most group name of the object if successful
    null - If not successful, or on error.
    """


class _ObjectRootMdfy():

    pass


class _ObjectRootMtrl():

    index = """
    Returns the material index of an object.
		Rendering materials are stored in Rhino's rendering material table.  This table is conceptually an array.  Render materials associated with objects and layers are specified by zero based indices into this array.
		If the return value of ObjectMaterialSource is "material by object", then the return value of this function is the index of the object's rendering material.  A material index of -1 indicates no material has been assigned, and that Rhino's internal default material has been assigned to the object.
    Parameters
    ==========
    Returns
    =======
    number - The rendering material index if successful.
    null - If not successful, or on error.
    """
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
    C{source}(int, OPT) - The new rendering material source.  If omitted, the current material source is returned.  Note, if arrObjects is specified, intSource is required.
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
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """


class _ObjectRootProp():

    color = """
    Returns or modifies the color of an object.  Object colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    Parameters
    ==========
    C{color}(lng, OPT) - The new color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.
    Returns
    =======
    number - If a color value is not specified,  the current color value if successful.
    number - If a color value is specified, the previous color value if successful.
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    color_source = """
    Returns or modifies the color source of an object.   The color used to display objects is specified in one of four ways:
		1. Color from layer.  The object's layer determines the object's color.
		2. Color from object.  The object's color is set by the object itself.
		3. Color from material.  The object's diffuse material color determines the object's color.
		4. Color from parent. For objects with parents, like objects in block instances, use parent's color source. If no parent, treats as color from layer.
    Parameters
    ==========
    C{source}(int, OPT) - The new color source.  If omitted, the current color source is returned.  Note, if arrObjects is specified, intSource is required.
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
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    layer = """
    Returns or modifies the layer of an object.
    Parameters
    ==========
    C{layer}(_Entity.Layer, OPT) - The name of an existing layer.  If omitted, the current object layer is returned.  Note, if arrObjects is specified, strLayer is required.
    Returns
    =======
    number - If a layer is not specified,  the object's current layer if successful.
    number - If a layer is specified, the object's previous layer if successful.
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    linetype = """
    Returns or modifies the linetype of an object.
    Parameters
    ==========
    C{layer}(_Entity.Layer, OPT) - The name of an existing linetype.  If omitted, the current object linetype is returned.  Note, if arrObjects is specified, strLinetype is required.
    Returns
    =======
    number - If a linetype is not specified,  the object's current linetype if successful.
    number - If a linetype is specified, the object's previous linetype if successful.
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    linetype_source = """
    Returns or modifies the linetype source of an object.   The linetype used to display objects is specified in one of three ways:
		1. Linetype from layer.  The object's layer determines the object's linetype.
		2. Linetype from object. The object's linetype is set by the object itself.
		3. Linetype from parent.  For objects with parents, like objects in block instances, use parent's linetype. If no parent, treats as linetype from layer.
    Parameters
    ==========
    C{source}(int, OPT) - The new linetype source.  If omitted, the current linetype source is returned.  Note, if arrObjects is specified, intSource is required.
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
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    name = """
    Returns or modifies the user-definable name of one or more objects.
    Parameters
    ==========
    C{names}(array_of str, OPT) - An array of strings identifying the new user-definable names. This array must have the same upper bounds as arrObjects.  Each element in arrNames will correspond with each element in arrObjects.
    Returns
    =======
    array - If arrNames is not specified,  the current object names if successful. Note, if an object does not have a user-definable name, it's corresponding element will be Null.
    array - If arrNames is specified,  the previous object names if successful.  Note, if an object does not have a user-definable name, it's corresponding element will be Null.
    null - If not successful, or on error.
    """
    print_color = """
    Returns or modifies the print color of an object.  Object print colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    Parameters
    ==========
    C{color}(lng, OPT) - The new print color value.  If omitted, the current object color is returned.  Note, if arrObjects is specified, lngColor is required.
    Returns
    =======
    number - If a print color value is not specified,  the current print color value if successful.
    number - If a print color value is specified, the previous print color value if successful.
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    print_color_source = """
    Returns or modifies the print color source of an object.  The color used to print objects is specified in one of four ways:
		1. Print color from layer.  Use the print color assigned to the object's layer.
		2. Print color from object.  Use the print color that is assigned to the object.
		3. Print color from display.  Use the object's display color.
		4. Print color from parent.  For objects with parents, like objects in block instances, use parent's print color.  If no parent, treats as print color from layer.
    Parameters
    ==========
    C{source}(int, OPT) - The new print color source.  If omitted, the current print color source is returned.  Note, if arrObjects is specified, intSource is required.
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
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    print_width = """
    Returns or modifies the print width of an object.  Object print widths are measured in millimeters (mm).
    Parameters
    ==========
    C{width}(dbl, OPT) - The new print width value in millimeters, where dblWidth = 0.0 means use the default width, and dblWidth < 0.0 means do not print (visible for screen display, but does not show on print).  If omitted, the current object print width is returned.  Note, if arrObjects is specified, dblWidth is required.
    Returns
    =======
    number - If a print width value is not specified,  the current print width value if successful.
    number - If a print width value is specified, the previous print width value if successful.
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """
    print_width_source = """
    Returns or modifies the print width source of an object.  The width used to print objects is specified in one of three ways:
		1. Print width from layer.  Use the print width assigned to the object's layer.
		2. Print width from object.  Use the print width that is assigned to the object.
		3. Print width from parent.  For objects with parents, like objects in block instances, use parent's print width.  If no parent, treats as print width from layer.
    Parameters
    ==========
    C{source}(int, OPT) - The new print width source.  If omitted, the current print width source is returned.  Note, if arrObjects is specified, intSource is required.
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
    number - If arrObjects is specified, then the number of objects modified if successful.
    null - If not successful, or on error.
    """


class _ObjectRootRndr():

    add_mesh = """
    Adds custom render mesh parameters to a meshable object, such as a surface or a polysurface.  If an object has custom render mesh parameters and they are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{quality}(int, OPT) - The initial settings of the new custom render mesh parameters. The available options are as follows:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)
    C{enable}(bln, OPT) - Enable the custom render mesh parameters.  If omitted, the newly added parameters will be enabled (True).
    Returns
    =======
    boolean - If blnEnable is not specified, then the current enabled/disabled state if successful.
    boolean - If blnEnable is not specified, then the current enabled/disabled state if successful.
    null - If the object does not have custom render mesh parameters, or on error.
    """
    enable = """
    Enables or disables an object's custom render mesh parameters. If an object's custom render mesh parameters are enabled, then they will be used, instead of the document's render mesh parameters, when a render mesh is generated for the object.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{enable}(bln, OPT) - Enable the custom render mesh settings.
    Returns
    =======
    boolean - If blnEnable is not specified, then the current enabled/disabled state if successful.
    boolean - If blnEnable is not specified, then the current enabled/disabled state if successful.
    null - If the object does not have custom render mesh parameters, or on error.
    """
    has_mesh = """
    Verifies that an object has custom render mesh parameters.
    Parameters
    ==========
    Returns
    =======
    boolean - True of the object has custom render mesh parameters, False otherwise.
    null - On error.
    """
    density = """
    Returns or modifies an object's custom render mesh parameter's mesh density property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{density}(dbl, OPT) - The render mesh density, which is a number between 0.0 and 1.0.
    Returns
    =======
    boolean - If dblDensity is not specified, the current render mesh density if successful.
    boolean - If dblDensity is specified, the previous render mesh density if successful.
    null - If not successful, or on error.
    """
    max_angle = """
    Returns or modifies an object's custom render mesh parameter's maximum angle property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{angle}(dbl, OPT) - The render mesh maximum angle in degrees.
    Returns
    =======
    boolean - If dblAngle is not specified, the current render mesh maximum angle if successful.
    boolean - If dblAngle is specified, the previous render mesh maximum angle if successful.
    null - If not successful, or on error.
    """
    max_aspect_ratio = """
    Returns or modifies an object's custom render mesh parameter's maximum aspect ratio property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{ratio}(dbl, OPT) - The render mesh maximum aspect ratio.  The suggested range, when not zero, is from 1 to 100.
    Returns
    =======
    boolean - If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.
    boolean - If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.
    null - If not successful, or on error.
    """
    max_dist_edge_to_srf = """
    Returns or modifies an object's custom render mesh parameter's maximum distance, edge to surface property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{distance}(dbl, OPT) - The render mesh maximum distance, edge to surface.
    Returns
    =======
    boolean - If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.
    boolean - If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.
    null - If not successful, or on error.
    """
    max_edge_length = """
    Returns or modifies an object's custom render mesh parameter's maximum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{length}(dbl, OPT) - The render mesh maximum edge length.
    Returns
    =======
    boolean - If dblLength is not specified, the current render mesh maximum edge length if successful.
    boolean - If dblLength is specified, the previous render mesh maximum edge length if successful.
    null - If not successful, or on error.
    """
    min_edge_length = """
    Returns or modifies an object's custom render mesh parameter's minimum edge length property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{length}(dbl, OPT) - The render mesh minimum edge length.
    Returns
    =======
    boolean - If dblLength is not specified, the current render mesh minimum edge length if successful.
    boolean - If dblLength is specified, the previous render mesh minimum edge length if successful.
    null - If not successful, or on error.
    """
    min_initial_grid_quads = """
    Returns or modifies an object's custom render mesh parameter's minimum initial grid quads property.
		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.
    Parameters
    ==========
    C{quads}(int, OPT) - The render mesh minimum initial grid quads.  The suggested range is from 0 to 10000.
    Returns
    =======
    boolean - If intQuads is not specified, the current render mesh minimum initial grid quads if successful.
    boolean - If intQuads is specified, the previous render mesh minimum initial grid quads if successful.
    null - If not successful, or on error.
    """
    quality = """
    Returns or sets the render mesh quality of an object's custom render mesh parameters.
    Parameters
    ==========
    C{quality}(int, OPT) - The render mesh quality, either:
		Value
		Description
		0
		Jagged and faster.  Objects may look jagged, but they should shade and render relatively quickly.
		1
		Smooth and slower.  Objects should look smooth, but they may take a very long time to shade and render.
		2 (Default)
    Returns
    =======
    boolean - If intQuality is not specified, the current render mesh quality if successful.
    boolean - If intQuality is specified, the previous render mesh quality if successful.
    null - If the object does not have custom render mesh parameters, or on error.
    """
    settings = """
    Returns or sets the render mesh settings of an object's custom render mesh parameters.
    Parameters
    ==========
    C{settings}(int, OPT) - The render mesh settings, which is a bit-coded number that allows or disallows certain features.  The bits can be added together in any combination to form a value between 0 and 15.  The bit values are as follows:
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
    boolean - If intSettings is not specified, the current render mesh settings if successful.
    boolean - If intSettings is specified, the previous render mesh settings if successful.
    null - If the object does not have custom render mesh parameters, or on error.
    """


class _ObjectRootStat():

    flash = """
    Causes the selection state of one or more objects to change momentarily so the object appears to flash on the screen.
    Parameters
    ==========
    C{style}(bln, OPT) - The flash style.  If True (default), then the objects will flash between their object color and Rhino's selected object color.  If false, then the objects will flash between invisible and visible.
    Returns
    =======
    """
    hide = """
    Hides one or more objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    Parameters
    ==========
    Returns
    =======
    number - The number of objects hidden if successful.
    null - If not successful, or on error.
    """
    lock = """
    Locks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    Parameters
    ==========
    Returns
    =======
    number - The number of objects locked if successful.
    null - If not successful, or on error.
    """
    match_object_attributes = """
    Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
    Parameters
    ==========
    C{targets}(array_of _ObjectRoot, REQ) - An array of strings identifying the target objects.
    Returns
    =======
    number - The number of objects whose attributes were modified if successful.
    null - If not successful, or on error.
    """
    reset_object_attributes = """
    Matches, or copies, the attributes of a source object to a target object or an array of target objects. If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
    Parameters
    ==========
    C{source}(_ObjectRoot, OMIT) - The identifier of the source object.  If the source object is not specified, the attributes of the target object(s) will be reset to Rhino's default object attributes.
    Returns
    =======
    number - The number of objects whose attributes were modified if successful.
    null - If not successful, or on error.
    """
    move_to_layout_space = """
    Returns or changes the layout or model space of an object.
    Parameters
    ==========
    C{layout}(str, OPT) - To change, or move, an object from model space to page layout space, or from one page layout to another, then specify the title or identifier of an existing page layout view. To move an object from page layout space to model space, just specify Null.
    C{return_name}(bln, OPT) - If True (default), then the name, or title, of the page layout view is returned. If False, then the identifier of the page layout view is returned.
    Returns
    =======
    string - If strLayout is not specified,  the object's current page layout view if successful. Note, if the object is not in page layout space, Null is returned.
    string - If strLayout  is specified, the object's previous page layout view if successful. Note, if the object was not in page layout space, Null is returned.
    null - If not successful, or on error.
    """
    select = """
    Selects one or more objects.
    Parameters
    ==========
    Returns
    =======
    number - The number of objects selected if successful.
    null - If not successful, or on error.
    """
    show = """
    Shows one or more hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    Parameters
    ==========
    Returns
    =======
    number - The number of objects shown if successful.
    null - If not successful, or on error.
    """
    unlock = """
    Unlocks one or more objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    Parameters
    ==========
    Returns
    =======
    number - The number of objects unlocked if successful.
    null - If not successful, or on error.
    """
    unselect = """
    Unselects one or more selected objects.
    Parameters
    ==========
    Returns
    =======
    number - The number of objects unselected if successful.
    null - If not successful, or on error.
    """


class _ObjectRootTest():

    is_in_layout_space = """
    Verifies that an object is in either page layout space or model space.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_hidden = """
    Verifies that an object is hidden.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_in_box = """
    Verifies an object's bounding box is inside of another bounding box.
    Parameters
    ==========
    C{box}(array_of dbl, REQ) - The bounding box to test against. A bounding box is an array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
    C{mode}(bln, OPT) - The test mode.
		Value
		Description
		True (Default)
		The object's bounding box must be contained by the test bounding box. In other words, test.min <= object.min and object.max <= test.max.
		False
    Returns
    =======
    null - On error.
    """
    is_in_group = """
    Verifies that an object is a member of a specified group.
    Parameters
    ==========
    C{group}(str, OPT) - The name of a group.  If omitted, the function verifies that the object is a member of any group.
    Returns
    =======
    null - On error.
    """
    is_locked = """
    Verifies that an object is locked.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_normal = """
    Verifies that an object is normal.  Normal objects are visible, can be snapped to, and can be selected.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_reference = """
    Verifies that an object is a reference object.  Reference objects are object that are not part of the current document.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_selectable = """
    Verifies that an object is selectable.  Objects that are locked, hidden, or on locked or hidden layers cannot be selected.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_selected = """
    Verifies that an object is currently selected.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_solid = """
    Verifies that an object is a closed, solid object.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_valid = """
    Verifies that an object's geometry is valid and without error.
    Parameters
    ==========
    Returns
    =======
    null - On error.
    """
    is_visible_in_view = """
    Verifies that an object is visible in a view.
    Parameters
    ==========
    C{view}(str, OPT) - The title of the view.  If omitted, the current active view is used.
    Returns
    =======
    null - On error.
    """


class _ObjectRootTrfm():

    mirror = """
    Mirrors a single object.
    Parameters
    ==========
    C{start_pt}(array_of dbl, REQ) - The start of the mirror plane.
    C{end_pt}(array_of dbl, REQ) - The end of the mirror plane.
    C{copy}(bln, OPT) - Copy the object. If omitted, the object will not be copied (False).
    Returns
    =======
    string - The identifier of the mirrored object if successful.
    null - If not successful, or on error.
    """
    move = """
    Moves a single object.
    Parameters
    ==========
    C{start}(array_of dbl, REQ) - The 3-D starting, or base, point of the move operation.
    C{end}(array_of dbl, REQ) - The 3-D ending point of the move operation.
    Returns
    =======
    boolean - The identifier of the moved object if successful.
    null - If not successful, or on error.
    """
    move_by_vec = """
    Moves a single object.
    Parameters
    ==========
    C{translation}(array_of dbl, REQ) - The 3-D starting, or base, point of the move operation.
    Returns
    =======
    boolean - The identifier of the moved object if successful.
    null - If not successful, or on error.
    """
    orient = """
    Orients a single object based on input points.
    Parameters
    ==========
    C{reference}(array_of dbl, REQ) - An array of 3-D reference points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
    C{target}(array_of dbl, REQ) - An array of 3-D target points.  If two 3-D points are specified, then this method will function similar to Rhino's Orient command.  If more than two 3-D points are specified, then the function will orient similar to Rhino's Orient3Pt command.
    C{flags}(int, OPT) - The orient flags.  Values can be added together to specify multiple options.
		Value
		Description
		1
		Copy object.  The default is not to copy the object.
		2
    Returns
    =======
    string - The identifier of the oriented object if successful.
    null - If not successful, or on error.
    """
    remap = """
    Remqps a single object from one plane, or coordinate system, to another.
    Parameters
    ==========
    C{src_plane}(array_of dbl, REQ) - The source plane to transform from.
    C{dst_plane}(array_of dbl, REQ) - The destination plane to transform to.
    C{copy}(bln, OPT) - Copy the object. If omitted, the object will not be copied (False).
    Returns
    =======
    string - The identifier of the remapped object if successful.
    null - If not successful, or on error.
    """
    rotate = """
    Rotates a single object. Rotation is based on the active construction plane.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - The 3-D center point of the rotation.
    C{angle}(dbl, REQ) - The rotation angle in degrees.
    C{axis}(array_of dbl, OPT) - A 3-D vector that identifies the axis of rotation. If omitted, the Z axis of the active construction plane is used as the rotation axis.
    C{copy}(bln, OPT) - Copy the object. If omitted, the object will not be copied (False).
    Returns
    =======
    string - The identifier of the rotated object if successful.
    null - If not successful, or on error.
    """
    scale = """
    Scales a single object. This function can be used to perform uniform or non-uniform scale transformations. Scaling is based on the active construction plane.
    Parameters
    ==========
    C{origin}(array_of dbl, REQ) - The origin of the scale transformation.
    C{scale}(array_of dbl, REQ) - An array of three numbers that identify the X axis, Y axis, and Z axis scale factors to apply. Scaling is based on the active construction plane.
    C{copy}(bln, OPT) - Copy the object. If omitted, the object will not be copied (False).
    Returns
    =======
    string - The identifier of the scaled object if successful.
    null - If not successful, or on error.
    """


class _ObjectRootType():

    object_type = """
    Returns the object type.
    Parameters
    ==========
    Returns
    =======
    number - The object type if successful.  The valid object types are as follows:
    null - If not successful, or on error.
    """


class _ObjectRootUtil():

    description = """
    Returns a short text description of an object.
    Parameters
    ==========
    Returns
    =======
    string - A short text description of the object is successful.
    null - If not successful, or on error.
    """
    dump = """
    Returns a detailed description of an object.
    Parameters
    ==========
    C{type}(int, OPT) - The acceptable values are as follows:
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
    null - If not successful, or on error.
    """


class _PlanarMeshDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Makes a new mesh with vertices offset at a distance in the opposite direction of the existing vertex normals.
    Parameters
    ==========
    C{mesh}(_ObjectRoot._MeshRoot, REQ) - The identifier of a mesh object.
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the offset mesh object if successful.
    null - If not successful, or on error.
    """


class _PlaneSurfaceDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _PolySurfaceDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _PolySurfaceFunc():

    explode = """
    Explodes, or un-joins,  one more polysurface objects.  Polysurfaces will be exploded into separate surfaces.
    Parameters
    ==========
    C{objects}(array_of _Object, REQ) - An array of strings identifying the polysurface objects to explode.
    C{delete}(bln, OPT) - Delete input objects after exploding.  The default is not to delete objects (False).
    Returns
    =======
    array - An array of strings identifying the newly created surface objects if successful.
    null - If not successful, or on error.
    """


class _PolylineDupl():

    copy_by_sub = """
    Adds a new curve object based on a portion, or interval, of an existing curve object. This function is similar in operation to Rhino's SubCrv command.
    Parameters
    ==========
    C{param_0}(dbl, REQ) - The first parameter on the source curve.
    C{param_1}(dbl, REQ) - The second parameter on the source curve.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """
    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a curve by a distance. The offset curve will be added to Rhino.
    Parameters
    ==========
    C{direction}(array_of dbl, REQ) - The 3-D point that indicates the direction of the offset.
    C{distance}(dbl, REQ) - The distance of the offset.
    C{normal}(array_of dbl, OPT) - A 3-D vector identifying the normal of the plane in which the offset will occur. If omitted, the normal of the active construction plane will be used.
    C{style}(int, OPT) - The corner style.  If omitted, a sharp corner style is used.
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
    array - An array containing the identifiers of the new objects if successful.
    null - If not successful, or on error.
    """
    copy_by_split = """
    Splits, or divides, a curve at a specified parameter. The parameter must be in the interior of the curve's domain.
    Parameters
    ==========
    C{parameters}(array_of dbl, REQ) - An array of one or more parameters, to split the curve at, that are in the interval returned by CurveDomain.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    array - An array containing the identifiers of the two newly created curve objects, if successful.
    null - If not successful, or on error.
    """
    copy_by_trim = """
    Trims a curve by removing portions of the curve outside the specified interval.
    Parameters
    ==========
    C{interval}(array_of int, REQ) - An array of two number identifying the interval to keep. Portions of the curve before domain(0) and after domain(1) will be removed. If the input curve is open, the interval must be increasing. If the input curve is closed and the interval is decreasing, then the portion of the curve across the start and end of the curve is returned.
    C{delete}(bln, OPT) - Delete the input curve. The default is to delete the input curve (True).
    Returns
    =======
    string - The identifier of the newly created curve object, if successful.
    null - If not successful, or on error.
    """


class _PolylineProp():

    vertices = """
    Returns the vertices of a polyline curve object.
    Parameters
    ==========
    Returns
    =======
    array - An  array of 3-D vertex points if successful.
    null - If not successful, or on error.
    """


class _SphereDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _SphereProp():

    sphere_definition = """
    Returns the definition of a sphere surface.
    Parameters
    ==========
    Returns
    =======
    array - An array containing the definition of the sphere if successful.  The elements of the array are as follows:
    array - The equatorial plane of the sphere.  The origin of the plane will be the center point of the sphere.
    number - The radius of the sphere.
    null - If not successful, or on error.
    """


class _SurfaceRoot():

    pass


class _SurfaceRootEval():

    evaluate = """
    Evaluates a surface at a U,V parameter.
    Parameters
    ==========
    C{parameter}(array_of dbl, REQ) - An array containing the U,V parameter to evaluate.
    Returns
    =======
    array - A 3-D point if successful.
    null - If not successful, or on error.
    """
    evaluate_derivatives = """
    A general purpose surface evaluator.
    Parameters
    ==========
    C{parameter}(array_of dbl, REQ) - An array containing the U,V parameter to evaluate.
    C{derivative}(int, REQ) - The number of derivatives to evaluate.
    Returns
    =======
    array - An array of length (intDerivative+1)*(intDerivative+2)/2 if successful.  The array elements are as follows:
    array - The 3-D point.
    array - The first derivative.
    array - The first derivative.
    array - The second derivative.
    array - The second derivative.
    array - The second derivative.
    array - etc...
    null - If not successful, or on error.
    """
    evaluate_frame = """
    Returns a plane based on the normal, u, and v directions at a given surface U,V parameter.
    Parameters
    ==========
    C{parameter}(array_of dbl, REQ) - An array containing the U,V parameter to evaluate.
    Returns
    =======
    array - The plane at the specified parameter if successful.
    null - If not successful, or on error.
    """


class _SurfaceRootFunc():

    make_non_periodic = """
    Makes a periodic surface non-periodic. Non-periodic surfaces can develop kinks when deformed.
    Parameters
    ==========
    C{direction}(int, REQ) - The direction to make non-periodic, either 0 = U, or 1 = V.
    C{delete}(bln, OPT) - Delete input surface.  If omitted, the input surface will not be deleted (False).
    Returns
    =======
    string - If blnDelete is False, the identifier of the new object if successful.
    string - If blnDelete is True, the identifier of the modified object if successful.
    null - If not successful, or on error.
    """
    make_periodic = """
    Makes an existing surface a periodic NURBS surface.
    Parameters
    ==========
    C{direction}(int, REQ) - The direction to make periodic, either 0 = U, or 1 = V.
    C{delete}(bln, OPT) - Delete input surface.  If omitted, the input surface will not be deleted (False).
    Returns
    =======
    string - If blnDelete is False, the identifier of the new object if successful.
    string - If blnDelete is True, the identifier of the modified object if successful.
    null - If not successful, or on error.
    """
    closest_pnt = """
    Returns the UV parameter of the point on a surface that is closest to a test point.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - The test, or sampling, point.
    Returns
    =======
    array - An array containing the U,V parameters of the closest point on the surface if successful.
    null - If not successful, or on error.
    """


class _SurfaceRootFuncClsd():

    boolean_difference = """
    Performs a Boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file.
    Parameters
    ==========
    C{breps}(array_of _ObjectRoot._SurfaceRoot, REQ) - The identifiers of the surfaces or polysurfaces to be subtracted.
    C{delete}(bln, OPT) - Delete all input objects. The default is to delete all input objects (True).
    Returns
    =======
    array - An array containing the identifiers of the newly created objects, if successful.
    null - If not successful, or on error.
    """
    boolean_intersection = """
    Performs a Boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file.
    Parameters
    ==========
    C{breps}(array_of _ObjectRoot._SurfaceRoot, REQ) - The identifiers of the surfaces or polysurfaces.
    C{delete}(bln, OPT) - Delete all input objects. The default is to delete all input objects (True).
    Returns
    =======
    array - An array containing the identifiers of the newly created objects, if successful.
    null - If not successful, or on error.
    """
    boolean_union = """
    Performs a Boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file.
    Parameters
    ==========
    C{breps}(array_of _ObjectRoot._SurfaceRoot, REQ) - The identifiers of the surfaces or polysurfaces to union.
    C{delete}(bln, OPT) - Delete all input objects. The default is to delete all input objects (True).
    Returns
    =======
    array - An array containing the identifiers of the newly created objects, if successful.
    null - If not successful, or on error.
    """
    brep_closest_pnt = """
    Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - The test, or sampling, point.
    Returns
    =======
    array - An array of closest point information if successful.  The array will contain the following information:
    null - If not successful, or on error.
    """
    intersect_breps = """
    Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.
    Parameters
    ==========
    C{brep_1}(str, REQ) - The second  brep object's identifier.
    C{tolerance}(dbl, OPT) - The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..
    Returns
    =======
    array - An array of strings identifying the newly created intersection curve and point objects if successful.
    null - If not successful, or on error.
    """
    boolean_split = """
    Splits a brep.  A brep can be either a surface with a single face or a polysurface.
    Parameters
    ==========
    C{cutter}(str, REQ) - The identifier of the brep object to split with.
    C{delete}(bln, OPT) - Delete input brep.  If omitted, the input brep will not be deleted (False).
    Returns
    =======
    array - The identifiers of the new brep objects if successful.
    null - If not successful, or on error.
    """


class _SurfaceRootFuncOorc():

    pass


class _SurfaceRootFuncOpen():

    cap_planar_holes = """
    Caps planar holes in a surface or polysurface. For more details, see the Cap command in the Rhino help file.
    Parameters
    ==========
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """


class _SurfaceRootMdfy():

    flip = """
    Returns or changes the normal direction of a surface. This feature can also be found in Rhino's Dir command.
    Parameters
    ==========
    C{flip}(bln, OPT) - The new normal orientation, either flipped (True) or not flipped (False).  If omitted, the current normal orientation is returned.
    Returns
    =======
    boolean - If blnFlip is not specified, the current normal orientation if successful.
    boolean - If blnFlip is specified, the previous normal orientation if successful.
    null - If not successful, or on error.
    """
    insert_knot = """
    Inserts a knot into a surface object.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - An array containing a U,V parameter on the surface.
    C{direction}(int, REQ) - The direction for knot insertion, either 0 = U, 1 = V, or 2 = both.
    C{symmetrical}(bln, OPT) - If blnSymmetrical = True, then knots are added on both sides of the center of the surface.  The default value is False.
    Returns
    =======
    boolean - True of False indicating success or failure.
    null - On error.
    """
    rebuild = """
    Rebuilds a surface to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.
    Parameters
    ==========
    C{degree}(array_of int, OPT) - An array of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3 in each direction.
    C{point_count}(array_of int, OPT) - An array of two numbers that identify the surface point count in both the U and the V directions.  The point count must be greater than the degree.  The default value is 10 in each direction.
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """
    remove_knot = """
    Deletes a knot-line from a surface object.
    Parameters
    ==========
    C{parameter}(dbl, REQ) - An array containing a U,V parameter on the surface.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
    C{direction}(int, REQ) - The direction for knot insertion, either 0 = U, or 1 = V.
    Returns
    =======
    boolean - True of False indicating success or failure.
    null - On error.
    """
    reverse = """
    Reverses the U and V directions of a surface object. This feature can also be found in Rhino's Dir command.
		To reverse the normal direction of a surface, use the FlipSurface method.
    Parameters
    ==========
    C{direction}(int, REQ) - The direction to reverse. Values can be added together so as to reverse more than one direction.
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
    null - On error.
    """
    shrink_trimmed = """
    Shrinks the underlying untrimmed surfaces near to trimming boundaries. For more details, see the ShrinkTrimmedSrf command in the Rhino help file.
    Parameters
    ==========
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """
    seam = """
    Changes the seam of a closed surface. For more information, see the Rhino help file for the SrfSeam command.
    Parameters
    ==========
    C{direction}(int, REQ) - The parameter direction, where 0 = U and 1 = V.
    C{parameter}(dbl, REQ) - The parameter at which to place the seam.
    Returns
    =======
    boolean - True of False indicating success or failure.
    null - On error.
    """


class _SurfaceRootProp():

    area = """
    Calculates the area of a surface or polysurface object. The results are based on the current drawing units.
    Parameters
    ==========
    Returns
    =======
    array - An array of area information if successful.  The array will contain the following information:
    number - The area.
    number - The absolute (+/-) error bound for the area.
    null - If not successful, or on error.
    """
    area_centroid = """
    Calculates the area centroid of a surface or polysurface object.
    Parameters
    ==========
    Returns
    =======
    array - An array of area centroid information if successful.  The array will contain the following information:
    null - If not successful, or on error.
    """
    area_moments = """
    Calculates the area moments of inertia of a surface or polysurface object.  For more information, see the Rhino help file for "Mass Properties Calculation Details."
    Parameters
    ==========
    Returns
    =======
    array - An array of area moments of inertia information if successful.  The array will contain the following information:
    null - If not successful, or on error.
    """
    contour_pnts = """
    Returns the vertices of the polyline curves generated by contouring a surface or polysurface object.
    Parameters
    ==========
    C{start_point}(array_of dbl, REQ) - The 3-D starting point of a center line.
    C{end_point}(array_of dbl, REQ) - The 3-D ending point of a center line.
    C{interval}(dbl, OPT) - The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
    C{angle}(dbl, OPT) - The maximum angle in degrees between unit tangents at adjacent vertices.  If omitted, the maximum angle will be set to 5.0 degrees.
    Returns
    =======
    array - An array of 3-D point arrays, one for each contour, if successful.
    null - If not successful, or on error.
    """
    curvature = """
    Returns the curvature of a surface at a U,V parameter.  See the Rhino help file for details on surface curvature.
    Parameters
    ==========
    C{parameter}(array_of dbl, REQ) - An array containing the U,V parameter to evaluate.
    Returns
    =======
    array - An array of curvature information if successful.  The array will contain the following information:
    number - Maximum principal curvature.
    number - Minimum principal curvature.
    number - Gaussian curvature.
    number - Mean curvature.
    null - If not successful, or on error.
    """
    curvature_analysis = """
    Returns the curvature of a surface.  See the Rhino help file for details on surface curvature analysis.
    Parameters
    ==========
    Returns
    =======
    array - An array of curvature information if successful.  The array will contain the following information:
    array - An array containing three values: the min Gaussian curvature, the max Gaussian curvature, and the infinity status.
    array - An array containing three values: the min unsigned mean curvature, the max unsigned mean curvature, and the infinity comparison.
    array - An array containing three values: the min maximum unsigned radius of curvature, the max maximum unsigned radius of curvature, and the infinity comparison.
    array - An array containing three values: the min minimum unsigned radius of curvature, the max minimum unsigned radius of curvature, and the infinity comparison.
    null - If not successful, or on error.
    """
    degree = """
    Returns the degree of a  surface object in the specified direction.
    Parameters
    ==========
    C{direction}(int, OPT) - The direction, either 0 = U, or 1 = V, or 2 = Both.  Of omitted, both the degrees in the U and V directions are returned (2 = Both).
    Returns
    =======
    array - If intDirection is not specified, or intDirection is set to 2, then the degree in both the U and V directions is returned.
    number - If intDirection is specified, and intDirection is set to either 0 or 1, then the degree in either the U or V direction is returned.
    null - If not successful, or on error.
    """
    domain = """
    Returns the domain of a  surface object in the specified direction.
    Parameters
    ==========
    C{direction}(int, REQ) - The direction, either 0 = U, or 1 = V.
    Returns
    =======
    array - An array containing the domain interval in the specified direction if successful.
    null - If not successful, or on error.
    """
    edit_pnts = """
    Returns the edit, or Greville, points of a surface object.  For each surface control point, there is a corresponding edit point.
    Parameters
    ==========
    C{return_parameters}(bln, OPT) - If False (default), edit points are returned as an array of 3-D points. If True, edit points are returned as an array U,V surface parameters.
    C{return_all}(bln, OPT) - If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.
    Returns
    =======
    array - If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.
    array - If blnReturnParameters is True, then an array of U,V parameter values if successful.
    null - If not successful, or on error.
    """
    isocurve_density = """
    Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface.
    Parameters
    ==========
    C{density}(int, OPT) - The isocurve wireframe density.  The possible values are as follows:
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
    number - The intDensity is not specified, then the current isocurve density if successful.
    number - The intDensity is specified, then the previous isocurve density if successful.
    null - If not successful, or on error.
    """
    knot_count = """
    Returns the knot count of a surface object.
    Parameters
    ==========
    Returns
    =======
    array - The number of knots in the U and V directions if successful.
    null - If not successful, or on error.
    """
    knots = """
    Returns the knots, or knot vector, of a surface object.
    Parameters
    ==========
    Returns
    =======
    array - The knot values of the surface if successful.
    null - If not successful, or on error.
    """
    normal = """
    Returns a 3-D vector that is the normal to a surface at a parameter.
    Parameters
    ==========
    C{parameter}(array_of dbl, REQ) - An array containing the UV parameter to evaluate.
    Returns
    =======
    array - A 3-D vector if successful.
    null - If not successful, or on error.
    """
    pnt_count = """
    Returns the control points count of a surface object.
    Parameters
    ==========
    Returns
    =======
    array - The number of control points in the U and V directions if successful.
    null - If not successful, or on error.
    """
    pnts = """
    Returns the control points, or control vertices, of a surface object.
    Parameters
    ==========
    C{return_all}(bln, OPT) - If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.
    Returns
    =======
    array - The control points of the surface if successful.
    null - If not successful, or on error.
    """
    weights = """
    Returns an array of weight values that are assigned to the control points of a surface.  The number of weights returned will be equal to the number of control points in the U and V directions.
    Parameters
    ==========
    Returns
    =======
    array - The weight values of the surface if successful.
    null - If not successful, or on error.
    """


class _SurfaceRootPropClsd():

    volume = """
    Calculates the volume of closed surface or polysurface objects.
    Parameters
    ==========
    Returns
    =======
    array - An array of volume information if successful.  The array will contain the following information:
    number - The volume.
    number - The absolute (+/-) error bound for the volume.
    null - If not successful, or on error.
    """
    volume_centroid = """
    Calculates the volume centroid of closed surface or polysurface objects.
    Parameters
    ==========
    Returns
    =======
    array - An array of volume centroid information if successful.  The array will contain the following information:
    null - If not successful, or on error.
    """
    volume_moments = """
    Calculates the volume moments of inertia of closed surface or polysurface objects.  For more information, see the Rhino help file for "Mass Properties Calculation Details."
    Parameters
    ==========
    Returns
    =======
    array - An array of volume moments of inertia information if successful.  The array will contain the following information:
    null - If not successful, or on error.
    """


class _SurfaceRootPropOorc():

    pass


class _SurfaceRootPropOpen():

    pass


class _SurfaceRootTest():

    is_brep = """
    Verifies an object is a Brep, or a boundary representation model, object.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_brep_manifold = """
    Verifies a polysurface object is manifold.  A polysurface for which every edge is shared by at most two faces is called a manifold.  If a polysurface has at least one edge that is shared by more than two faces, then that polysurface is called non-manifold.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_parameter_on_srf = """
    Verifies that a parameter space point is on a trimmed surface, or not on the trimmed portion of a surface.
    Parameters
    ==========
    C{parameter}(array_of dbl, REQ) - An array containing the U,V parameter to evaluate.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_plane_surface = """
    Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, a plane surface is not a planar NURBS surface.
    Parameters
    ==========
    Returns
    =======
    boolean - True or False indicating success or failure.
    null - On error.
    """
    is_pnt_in_srf = """
    Verifies that a point is inside a closed surface or polysurface.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - The test, or sampling, point.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_pnt_on_srf = """
    Verifies that a point lies on a surface.
    Parameters
    ==========
    C{point}(array_of dbl, REQ) - The test, or sampling, point.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_poly_srf = """
    Verifies an object is a polysurface.  Polysurfaces consists of two or more surfaces joined together. If the polysurface fully encloses a volume, it is considered a solid. In some other 3-D programs, this is called a "quilt."
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_poly_surface_closed = """
    Verifies a polysurface object is closed.  If the polysurface fully encloses a volume, it is considered a solid.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_poly_srf_planar = """
    Verifies a polysurface object is planar.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_srf_closed = """
    Verifies a surface object is closed in the specified direction.  If the surface fully encloses a volume, it is considered a solid.
    Parameters
    ==========
    C{direction}(int, REQ) - The direction, either 0 = U, or 1 = V.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_srf_periodic = """
    Verifies a surface object is periodic in the specified direction.
    Parameters
    ==========
    C{direction}(int, REQ) - The direction, either 0 = U, or 1 = V.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_srf_planar = """
    Verifies a surface object is planar.
    Parameters
    ==========
    C{tolerance}(dbl, OPT) - A tolerance to use when checking. The default is to use Rhino's current absolute tolerance.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_srf_rational = """
    Verifies a surface object is rational.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_srf_singular = """
    Verifies a surface object is singular in the specified direction.  Surfaces are considered singular if a side collapses to a point.
    Parameters
    ==========
    C{direction}(int, REQ) - The direction, either 0 = south, 1 = east, 2 = north, or 3 = west.
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_srf_trimmed = """
    Verifies a surface object has been trimmed.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """


class _SurfaceRootType():

    is_cone = """
    Determines if a surface is a portion of a cone.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_cylinder = """
    Determines if a surface is a portion of a cylinder.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_sphere = """
    Determines if a surface is a portion of a sphere.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_surface = """
    Verifies an object is surface.  Brep objects with only one face are also considered surfaces.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """
    is_torus = """
    Determines if a surface is a portion of a torus.
    Parameters
    ==========
    Returns
    =======
    boolean - True if successful, otherwise False.
    null - On error.
    """


class _TorusDupl():

    copy_move = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{start}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    C{end}(array_of dbl, OPT) - The 3-D ending point of the copy operation.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_move_by_vec = """
    Copies a single object from one location to another, or in-place.
    Parameters
    ==========
    C{translation}(array_of dbl, OPT) - The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place.
    Returns
    =======
    string - The identifier of the copied object if successful.
    null - If not successful, or on error.
    """
    copy_by_offset = """
    Offsets a surface by a distance. The offset surface will be added to Rhino.
    Parameters
    ==========
    C{distance}(dbl, REQ) - The distance to offset.
    Returns
    =======
    string - The identifier of the new object if successful.
    null - If not successful, or on error.
    """


class _TorusProp():

    torus_definition = """
    Returns the definition of a torus surface.
    Parameters
    ==========
    Returns
    =======
    array - An array containing the definition of the torus if successful.  The elements of the array are as follows:
    array - The base plane of the torus.
    number - The major radius of the torus.
    number - The minor radius of the torus.
    null - If not successful, or on error.
    """
