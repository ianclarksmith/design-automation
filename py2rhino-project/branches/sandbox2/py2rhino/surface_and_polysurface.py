# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class SurfaceAndPolysurface(IRhinoScript):



    def add_box(self, corners):
        """        
        Adds a new box-shaped polysurface to the document.
    
        Parameters
        ==========

        corners, Array of ????, Required        
        An array of eight 3-D points that define the corners of the box.  Points need to be  in counter-clockwise order starting with the bottom rectangle of the box.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [corners]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(corners)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(72, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddBox", None, *params_flattened)

    def add_cone(self, base, plane, height, height, radius, cap=None):
        """        
        Adds a cone-shaped polysurface to the document.
    
        Parameters
        ==========

        base, Array of ????, Required        
        The 3-D origin point of the cone.
            
        plane, Array of ????, Required        
        The cone's base plane.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.
            
        height, Array of ????, Required        
        The 3-D height point of the cone.  The height point defines the height and direction of the cone.
            
        height, Double, Required        
        The height of the cone.  If arrPlane is specified, then the center of the arrPlane is height * the plane's z-axis.
            
        radius, Double, Required        
        The radius at the base of the cone.  Note, tan(cone_angle) = dblRadius/ dblHeight.
            
        cap, Boolean, Optional        
        Cap the base of the cone.  The default is to cap the cone (True).
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [base, plane, height, height, radius, cap]
        params_required = [True, True, True, True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(base), flatten(plane), flatten(height), height, radius, cap]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(75, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddCone", None, *params_flattened)

    def add_cut_plane(self, objects, start_point, end_point, normal=None):
        """        
        Adds a planar surface through objects at a designated location.  For more information, see the Rhino help file for the CutPlane command.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        The identifiers of objects that the cutting planes will pass through.
            
        start_point, Array of ????, Required        
        The start of the line that defines the cutting plane.
            
        end_point, Array of ????, Required        
        The end of the line that defines the cutting plane.
            
        normal, Array of ????, Optional        
        In the case of Rhino's CutPlane command, this is the normal to, or Z axis of, the active view's construction plane.  If omitted, the world Z axis is used.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [objects, start_point, end_point, normal]
        params_required = [True, True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(objects), flatten(start_point), flatten(end_point), flatten(normal)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(822, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddCutPlane", None, *params_flattened)

    def add_cylinder(self, base, plane, height, height, radius, cap=None):
        """        
        Adds a cylinder-shaped polysurface to the document.
    
        Parameters
        ==========

        base, Array of ????, Required        
        The 3-D base point of the cylinder.
            
        plane, Array of ????, Required        
        The base plane of the cylinder.
            
        height, Array of ????, Required        
        The 3-D height point of the cylinder.  The height point defines the height and direction of the cylinder.
            
        height, Double, Required        
        The height of the cylinder.
            
        radius, Double, Required        
        The radius of the cylinder.
            
        cap, Boolean, Optional        
        Cap the ends of the cylinder.  If omitted, the ends of the cylinder will be capped (True).
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [base, plane, height, height, radius, cap]
        params_required = [True, True, True, True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(base), flatten(plane), flatten(height), height, radius, cap]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(73, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddCylinder", None, *params_flattened)

    def add_edge_srf(self, objects):
        """        
        Creates a surface from 2, 3, or 4 edge curves.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of 2, 3, or 4 curve object identifiers.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

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

        return self._ApplyTypes_(203, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddEdgeSrf", None, *params_flattened)

    def add_loft_srf(self, objects, start_pt=None, end_pt=None, type=None, style=None, value=None, closed=None):
        """        
        Adds a surface created by lofting curves to the document.
		* This function will not perform any curve sorting. You must pass in curves in the order you want them lofted.
		* This function will not adjust the directions of open curves. Use CurveDirectionsMatch and ReverseCurve to adjust the directions of open curves.
		* This function will not adjust the seams of closed curves. Use CurveSeam to adjust the seam of closed curves.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An ordered array of strings identifying the curve objects to loft.
            
        start_pt, Array of ????, Optional        
        The starting point of the loft.
            
        end_pt, Array of ????, Optional        
        The ending point of the loft.
            
        type, Integer, Optional        
        The type of loft. The default loft type is Normal (0). The possible loft types are as follows:
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
            
        style, Integer, Optional        
        The simplify method of the loft. The default value is None (0). The possible loft simplify methods are as follows:
		Value
		Description
		0
		None. Does not simplify.
		1
		Rebuild. Rebuilds the shape curves before lofting.
		2
            
        value, Integer, Optional        
        A value based on the specified intStyle. If intStyle=1 (Rebuild), then nValue is the number of control point used to rebuild. If intstyle=1 is specified and this argument is omitted, then curves will be rebuilt using 10 control points. If intStyle=2 (Refit), then nValue is the tolerance used to rebuild. If intstyle=2 is specified and this argument is omitted, then the document's absolute tolerance us used for refitting.
            
        closed, Boolean, Optional        
        Creates a closed surface, continuing the surface past the last curve around to the first curve. Available when you have selected three shape curves. The default value is not to create a closed surface (False).
            
        Returns
        =======

        array
        An array containing the identifiers of the new surface objects if successful.

        null
        If not successful, or on error.

        """

        params = [objects, start_pt, end_pt, type, style, value, closed]
        params_required = [True, False, False, False, False, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_I2, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(objects), flatten(start_pt), flatten(end_pt), type, style, value, closed]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(567, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddLoftSrf", None, *params_flattened)

    def add_nurbs_surface(self, point_count, points, knots_u, knots_u, degree, weights):
        """        
        Adds a NURBS surface object to the document.
    
        Parameters
        ==========

        point_count, Array of ????, Required        
        The number of control points in the U and V directions.
            
        points, Array of ????, Required        
        An array of 3-D control points.
            
        knots_u, Array of ????, Required        
        The knot values for the surface in the U direction.  The array must contain arrPointCount(0) + arrDegree(0) - 1 elements.
            
        knots_u, Array of ????, Required        
        The knot values for the surface in the U direction.  The array must contain arrPointCount(1) + arrDegree(1) - 1 elements.
            
        degree, Array of ????, Required        
        The degree of the surface in the U and V directions.  The degree in each direction must be greater than or equal to one (1).
            
        weights, Array of ????, Required        
        The weight values for the surface.  The number of elements in arrWeights equal the number of elements in arrPoints.  Weight values must be greater than zero (0).
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [point_count, points, knots_u, knots_u, degree, weights]
        params_required = [True, True, True, True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(point_count), flatten(points), flatten(knots_u), flatten(knots_u), flatten(degree), flatten(weights)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(435, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddNurbsSurface", None, *params_flattened)

    def add_planar_srf(self, objects):
        """        
        Creates one or more surfaces from planar curves.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of curve object identifiers.
            
        Returns
        =======

        array
        An array of strings identifying the new objects if successful.

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

        return self._ApplyTypes_(371, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddPlanarSrf", None, *params_flattened)

    def add_plane_surface(self, plane, d_u, d_v):
        """        
        Creates a plane surface.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane.
            
        d_u, Double, Required        
        The magnitude in the U direction.
            
        d_v, Double, Required        
        The magnitude in the V direction.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [plane, d_u, d_v]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [flatten(plane), d_u, d_v]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(648, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddPlaneSurface", None, *params_flattened)

    def add_rail_rev_srf(self, profile, rail, axis):
        """        
        Create a surface by revolving a profile curve along a rail curve.
    
        Parameters
        ==========

        profile, String, Required        
        The identifier of the profile curve.
            
        rail, String, Required        
        The identifier of the rail curve.
            
        axis, Array of ????, Required        
        An array of two 3-D points identifying the start point and end point of the rail revolve axis.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [profile, rail, axis]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [profile, rail, flatten(axis)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(536, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddRailRevSrf", None, *params_flattened)

    def add_rev_srf(self, profile, axis, start_angle=None, end_angle=None):
        """        
        Create a surface by revolving a curve around an axis.
    
        Parameters
        ==========

        profile, String, Required        
        The identifier of the curve to revolve.
            
        axis, Array of ????, Required        
        An array of two 3-D points identifying the start point and end point of the rail revolve axis.
            
        start_angle, Double, Optional        
        The starting angle. If omitted, an angle of 0.0 is used.
            
        end_angle, Double, Optional        
        The ending angle. If omitted, an angle of 360.0 is used.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [profile, axis, start_angle, end_angle]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [profile, flatten(axis), start_angle, end_angle]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(535, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddRevSrf", None, *params_flattened)

    def add_sphere(self, center, plane, radius):
        """        
        Adds a spherical surface to the document.
    
        Parameters
        ==========

        center, Array of ????, Required        
        The center point of the sphere.
            
        plane, Array of ????, Required        
        An equatorial plane.  The origin of the plane will be the center point of the sphere.
            
        radius, Double, Required        
        The radius of the sphere in current model units.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [center, plane, radius]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(center), flatten(plane), radius]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(71, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSphere", None, *params_flattened)

    def add_srf_contour_crvs(self, object, start_point, end_point, plane, interval=None):
        """        
        Adds a spaced series of planar curves resulting from the intersection of a defined cutting planes through a surface or a polysurface. For more information, see the Rhino help file for details on the Contour command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a surface or polysurface object.
            
        start_point, Array of ????, Required        
        The 3-D starting point of a center line.
            
        end_point, Array of ????, Required        
        The 3-D ending point of a center line.
            
        plane, Array of ????, Required        
        A plane that defines the cutting plane.
            
        interval, Double, Optional        
        The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
            
        Returns
        =======

        array
        An array of strings identifying the newly created contour curves if successful.

        null
        If not successful, or on error.

        """

        params = [object, start_point, end_point, plane, interval]
        params_required = [True, True, True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [object, flatten(start_point), flatten(end_point), flatten(plane), interval]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(747, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSrfContourCrvs", None, *params_flattened)

    def add_srf_control_pt_grid(self, count, points, degree=None):
        """        
        Creates a surface from a grid of control points.
    
        Parameters
        ==========

        count, Array of ????, Required        
        The number of control points in the U and V directions.
            
        points, Array of ????, Required        
        An array of 3-D control points.
            
        degree, Array of ????, Optional        
        The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [count, points, degree]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(count), flatten(points), flatten(degree)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(294, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSrfControlPtGrid", None, *params_flattened)

    def add_srf_pt(self, points):
        """        
        Creates a new surface from either 3 or 4 corner points.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of either 3 or 4 corner points.
            
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

        return self._ApplyTypes_(204, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSrfPt", None, *params_flattened)

    def add_srf_pt_grid(self, count, points, degree=None, closed=None):
        """        
        Creates a surface from a grid of points.
    
        Parameters
        ==========

        count, Array of ????, Required        
        The number of points in the U and V directions.
            
        points, Array of ????, Required        
        An array of 3-D points.
            
        degree, Array of ????, Optional        
        The degree of the surface in the U and V directions.  If omitted, the degree of the new surface in the U and V directions will be 3.
            
        closed, Array of ????, Optional        
        Whether or not the surface is closed in the U and V directions.  If omitted, the new surface will not be closed in either the U or V directions.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [count, points, degree, closed]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(count), flatten(points), flatten(degree), flatten(closed)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(293, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSrfPtGrid", None, *params_flattened)

    def add_srf_section_crvs(self, object, plane):
        """        
        Adds planar curves resulting from the intersection of a defined cutting plane through a surface or a polysurface. For more information, see the Rhino help file for details on the Section command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a surface or polysurface object.
            
        plane, Array of ????, Required        
        A plane that defines the cutting plane.
            
        Returns
        =======

        array
        An array of strings identifying the newly created section curves if successful.

        null
        If not successful, or on error.

        """

        params = [object, plane]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(803, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSrfSectionCrvs", None, *params_flattened)

    def add_sweep1(self, rail, shapes, start_pt=None, end_pt=None, closed=None, style=None, style_arg=None, simplify=None, simplify_arg=None):
        """        
        Adds a surface created through profile curves that define the surface shape and one curve that defines a surface edge. For more details on this method, see the Rhino help file for the Sweep1 command.
		Note, this method does not perform any curve sorting or direction matching on the input shape curves. This is the responsibility of the script writer.
		For best results:
		* The shape curves should all be oriented in the same direction.
		* The starting point of each shape curve should either intersect with or be close to the rail curve.
		* The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.
    
        Parameters
        ==========

        rail, String, Required        
        The identifier of the rail curve.
            
        shapes, Array of ????, Required        
        An array of strings identifying one or more shape, or cross section, curves.
            
        start_pt, Array of ????, Optional        
        The 3-D starting point of the surface.
            
        end_pt, Array of ????, Optional        
        The 3-D ending point of the surface.
            
        closed, Boolean, Optional        
        If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
            
        style, Integer, Optional        
        The sweep style, where 0 = Freeform and 1 = Roadlike. The default value is 0 = Freeform.
            
        style_arg, Variant, Optional        
        If intStyle = 1 (Roadlike), then this argument is a 3-D vector identifying the planar up direction for the sweep.
            
        simplify, Integer, Optional        
        Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
            
        simplify_arg, Variant, Optional        
        If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance.  If intSimplify = 2 (Rebuild), then this argument is a number specifying the number of control points to rebuild the shape curves.
            
        Returns
        =======

        array
        The identifiers of the new surface objects if successful.

        null
        If not successful, or on error.

        """

        params = [rail, shapes, start_pt, end_pt, closed, style, style_arg, simplify, simplify_arg]
        params_required = [True, True, False, False, False, False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1), (VT_I2, 1), (VT_VARIANT, 1), (VT_I2, 1), (VT_VARIANT, 1)]
        params_flattened = [rail, flatten(shapes), flatten(start_pt), flatten(end_pt), closed, style, style_arg, simplify, simplify_arg]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(893, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSweep1", None, *params_flattened)

    def add_sweep2(self, rails, shapes, start_pt=None, end_pt=None, closed=None, simple_sweep=None, maintain_height=None, simplify=None, simplify_arg=None):
        """        
        Adds a surface created through profile curves that define the surface shape and two curves that define the surface edges. For more details on this method, see the Rhino help file for the Sweep2 command.
		Note, this method does not perform any curve sorting or direction matching on the input shape curves. This is the responsibility of the script writer.
		For best results:
		* The shape curves should all be oriented in the same direction.
		* The starting point of each shape curve should either intersect with or be close to the first rail curve.
		* The ending point of each shape curve should either intersect with or be close to the second rail curve.
		* The shape curves should be passed in order, starting with the curve closest to the starting point of the rail.
    
        Parameters
        ==========

        rails, Array of ????, Required        
        An array of strings identifying two rail curves.
            
        shapes, Array of ????, Required        
        An array of strings identifying one or more shape, or cross section, curves.
            
        start_pt, Array of ????, Optional        
        The 3-D starting point of the surface.
            
        end_pt, Array of ????, Optional        
        The 3-D ending point of the surface.
            
        closed, Boolean, Optional        
        If True, then create a closed surface, continuing the surface past the last curve around to the first curve. This option is only available after you select two cross-section curves.  The default value is False.
            
        simple_sweep, Boolean, Optional        
        If True, then create surfaces using exact input. This option generates simpler surfaces in cases when the curves are perfectly set up.  The default value is False.
            
        maintain_height, Boolean, Optional        
        By default, shape curves normally scale in both the height and width dimensions. To remove the association between the height scaling from the width scaling, set this value to True.  The default value is False.
            
        simplify, Integer, Optional        
        Cross section curve options, where 0 = Do Not Simplify, 1 = Refit, and 2 = Rebuild. The default value is 0 = Do Not Simplify.
            
        simplify_arg, Variant, Optional        
        If intSimplify = 1 (Refit), then this argument is a number specifying the refit tolerance.  If intSimplify = 2 (Rebuild), then this argument is a number specifying the number of control points to rebuild the shape curves.
            
        Returns
        =======

        array
        The identifiers of the new surface objects if successful.

        null
        If not successful, or on error.

        """

        params = [rails, shapes, start_pt, end_pt, closed, simple_sweep, maintain_height, simplify, simplify_arg]
        params_required = [True, True, False, False, False, False, False, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_I2, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(rails), flatten(shapes), flatten(start_pt), flatten(end_pt), closed, simple_sweep, maintain_height, simplify, simplify_arg]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(894, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSweep2", None, *params_flattened)

    def add_torus(self, base, plane, major_radius, minor_radius, direction=None):
        """        
        Adds a torus-shaped revolved surface to the document.
    
        Parameters
        ==========

        base, Array of ????, Required        
        The 3-D origin point of the torus.
            
        plane, Array of ????, Required        
        The base plane of the torus.
            
        major_radius, Double, Required        
        The major radius of the torus.  The major radius must be larger than the minor radius.
            
        minor_radius, Double, Required        
        The minor radius of the torus.  The minor radius must be greater than zero.
            
        direction, Array of ????, Optional        
        A point that defines the direction of the torus.  If omitted, a torus that is parallel to the world XY plane is created.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [base, plane, major_radius, minor_radius, direction]
        params_required = [True, True, True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(base), flatten(plane), major_radius, minor_radius, flatten(direction)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(74, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddTorus", None, *params_flattened)

    def boolean_difference(self, input0, input1, delete=None):
        """        
        Performs a Boolean difference operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanDifference command in the Rhino help file.
    
        Parameters
        ==========

        input0, Array of ????, Required        
        The identifiers of the surfaces or polysurfaces to subtract from.
            
        input1, Array of ????, Required        
        The identifiers of the surfaces or polysurfaces to be subtracted.
            
        delete, Boolean, Optional        
        Delete all input objects. The default is to delete all input objects (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the newly created objects, if successful.

        null
        If not successful, or on error.

        """

        params = [input0, input1, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(input0), flatten(input1), delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(508, 1, (VT_VARIANT, 0), params_magic_numbers, u"BooleanDifference", None, *params_flattened)

    def boolean_intersection(self, input0, input1, delete=None):
        """        
        Performs a Boolean intersection operation on two sets of input surfaces and polysurfaces. For more details, see the BooleanIntersection command in the Rhino help file.
    
        Parameters
        ==========

        input0, Array of ????, Required        
        The identifiers of the surfaces or polysurfaces.
            
        input1, Array of ????, Required        
        The identifiers of the surfaces or polysurfaces.
            
        delete, Boolean, Optional        
        Delete all input objects. The default is to delete all input objects (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the newly created objects, if successful.

        null
        If not successful, or on error.

        """

        params = [input0, input1, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(input0), flatten(input1), delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(507, 1, (VT_VARIANT, 0), params_magic_numbers, u"BooleanIntersection", None, *params_flattened)

    def boolean_union(self, input, delete=None):
        """        
        Performs a Boolean union operation on a set of input surfaces and polysurfaces. For more details, see the BooleanUnion command in the Rhino help file.
    
        Parameters
        ==========

        input, Array of ????, Required        
        The identifiers of the surfaces or polysurfaces to union.
            
        delete, Boolean, Optional        
        Delete all input objects. The default is to delete all input objects (True).
            
        Returns
        =======

        array
        An array containing the identifiers of the newly created objects, if successful.

        null
        If not successful, or on error.

        """

        params = [input, delete]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(input), delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(506, 1, (VT_VARIANT, 0), params_magic_numbers, u"BooleanUnion", None, *params_flattened)

    def brep_closest_point(self, object, point):
        """        
        Returns the point on a surface or polysurface that is closest to a test point. This function works on both untrimmed and trimmed surfaces.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        point, Array of ????, Required        
        The test, or sampling, point.
            
        Returns
        =======

        array
        An array of closest point information if successful.  The array will contain the following information:

        null
        If not successful, or on error.

        """

        params = [object, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(514, 1, (VT_VARIANT, 0), params_magic_numbers, u"BrepClosestPoint", None, *params_flattened)

    def cap_planar_holes(self, surface):
        """        
        Caps planar holes in a surface or polysurface. For more details, see the Cap command in the Rhino help file.
    
        Parameters
        ==========

        surface, String, Required        
        The identifier of the surface or polysurface to cap.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(701, 1, (VT_VARIANT, 0), params_magic_numbers, u"CapPlanarHoles", None, *params_flattened)

    def duplicate_edge_curves(self, object, select=None):
        """        
        Duplicates the edge curves of a surface or polysurface. For more information, see the Rhino help file for information on the DupEdge command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the surface or polysurface object.
            
        select, Boolean, Optional        
        Select the duplicated edge curves.  The default is not to select (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly created curve objects if successful.

        null
        If not successful, or on error.

        """

        params = [object, select]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, select]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(657, 1, (VT_VARIANT, 0), params_magic_numbers, u"DuplicateEdgeCurves", None, *params_flattened)

    def duplicate_surface_border(self, object):
        """        
        Creates a curve that duplicates a surface or polysurface border.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the surface or polysurface object.
            
        Returns
        =======

        array
        An array of strings identifying the new curve objects if successful.

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

        return self._ApplyTypes_(852, 1, (VT_VARIANT, 0), params_magic_numbers, u"DuplicateSurfaceBorder", None, *params_flattened)

    def evaluate_surface(self, object, parameter):
        """        
        Evaluates a surface at a U,V parameter.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Array of ????, Required        
        An array containing the U,V parameter to evaluate.
            
        Returns
        =======

        array
        A 3-D point if successful.

        null
        If not successful, or on error.

        """

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(parameter)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(205, 1, (VT_VARIANT, 0), params_magic_numbers, u"EvaluateSurface", None, *params_flattened)

    def explode_polysurfaces(self, object, objects, delete=None):
        """        
        Explodes, or un-joins,  one more polysurface objects.  Polysurfaces will be exploded into separate surfaces.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the polysurface object to explode.
            
        objects, Array of ????, Required        
        An array of strings identifying the polysurface objects to explode.
            
        delete, Boolean, Optional        
        Delete input objects after exploding.  The default is not to delete objects (False).
            
        Returns
        =======

        array
        An array of strings identifying the newly created surface objects if successful.

        null
        If not successful, or on error.

        """

        params = [object, objects, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [object, flatten(objects), delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(447, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExplodePolysurfaces", None, *params_flattened)

    def extract_iso_curve(self, object, parameter, dir):
        """        
        Extracts isoparametric curves from a surface.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Array of ????, Required        
        An array containing the U,V parameter of the surface to evaluate.
            
        dir, Integer, Required        
        The direction, either 0 = U, 1 = V, or 2 = Both.
            
        Returns
        =======

        array
        An array of strings identifying the newly created curve objects if successful.

        null
        If not successful, or on error.

        """

        params = [object, parameter, dir]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)]
        params_flattened = [object, flatten(parameter), dir]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(488, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtractIsoCurve", None, *params_flattened)

    def extrude_curve(self, curve, path):
        """        
        Creates a surface by extruding a curve along a path curve.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the curve object to extrude.
            
        path, String, Required        
        The identifier of the path curve.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [curve, path]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [curve, path]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(538, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtrudeCurve", None, *params_flattened)

    def extrude_curve_point(self, curve, point):
        """        
        Creates a surface by extruding a curve to a point.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the curve object to extrude.
            
        point, Array of ????, Required        
        A 3-D point.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [curve, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [curve, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(540, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtrudeCurvePoint", None, *params_flattened)

    def extrude_curve_straight(self, curve, start_point, end_point):
        """        
        Creates a surface by extruding a curve straight along two points that define a line.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the curve object to extrude.
            
        start_point, Array of ????, Required        
        A starting point.
            
        end_point, Array of ????, Required        
        A ending point.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [curve, start_point, end_point]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [curve, flatten(start_point), flatten(end_point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(539, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtrudeCurveStraight", None, *params_flattened)

    def extrude_curve_tapered(self, curve, distance, direction, base_point, angle, corner_type=None):
        """        
        Creates a surface by extruding a curve to a taper. Unlike Lofts and Sweeps, the initial orientation of the profile curve is maintained through the extrusion.
    
        Parameters
        ==========

        curve, String, Required        
        The identifier of the curve object to extrude.
            
        distance, Double, Required        
        The extrusion distance.
            
        direction, Array of ????, Required        
        A 3-D vector that specifies the extrusion direction.
            
        base_point, Array of ????, Required        
        A 3-D point that specifies the base point of the extrusion.
            
        angle, Double, Required        
        The angle of the extrusion.
            
        corner_type, Integer, Optional        
        The corner type of the extrusion, where:
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

        array
        An array of strings identifying the newly created surface objects if successful.

        null
        If not successful, or on error.

        """

        params = [curve, distance, direction, base_point, angle, corner_type]
        params_required = [True, True, True, True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_I2, 1)]
        params_flattened = [curve, distance, flatten(direction), flatten(base_point), angle, corner_type]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(914, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtrudeCurveTapered", None, *params_flattened)

    def extrude_surface(self, surface, curve, cap=None):
        """        
        Creates a surface or solid by extruding a straight along a path curve.
    
        Parameters
        ==========

        surface, String, Required        
        The identifier of the surface object to extrude.
            
        curve, String, Required        
        The identifier of the path curve.
            
        cap, Boolean, Optional        
        Extrusion is capped at both ends to make a closed polysurface. The default value is True.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [surface, curve, cap]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [surface, curve, cap]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(541, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExtrudeSurface", None, *params_flattened)

    def fit_surface(self, object, degree=None, tolerance=None):
        """        
        Reduces the number of surface control points while maintaining the surfaces' same general shape.  Use this function for replacing surface with too many control points.  For more information, see the Rhino help file for the FitSrf command.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        degree, Array of ????, Optional        
        An array of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3.
            
        tolerance, Double, Optional        
        The fitting tolerance.  If dblTolerance is not specified or <= 0.0, the document absolute tolerance is used.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [object, degree, tolerance]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [object, flatten(degree), tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(815, 1, (VT_VARIANT, 0), params_magic_numbers, u"FitSurface", None, *params_flattened)

    def flip_surface(self, object, flip=None):
        """        
        Returns or changes the normal direction of a surface. This feature can also be found in Rhino's Dir command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a surface object.
            
        flip, Boolean, Optional        
        The new normal orientation, either flipped (True) or not flipped (False).  If omitted, the current normal orientation is returned.
            
        Returns
        =======

        boolean
        If blnFlip is not specified, the current normal orientation if successful.

        boolean
        If blnFlip is specified, the previous normal orientation if successful.

        null
        If not successful, or on error.

        """

        params = [object, flip]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, flip]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(718, 1, (VT_VARIANT, 0), params_magic_numbers, u"FlipSurface", None, *params_flattened)

    def insert_surface_knot(self, object, parameter, direction, symmetrical=None):
        """        
        Inserts a knot into a surface object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the surface object.
            
        parameter, Double, Required        
        An array containing a U,V parameter on the surface.
            
        direction, Integer, Required        
        The direction for knot insertion, either 0 = U, 1 = V, or 2 = both.
            
        symmetrical, Boolean, Optional        
        If blnSymmetrical = True, then knots are added on both sides of the center of the surface.  The default value is False.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        On error.

        """

        params = [object, parameter, direction, symmetrical]
        params_required = [True, True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [object, parameter, direction, symmetrical]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(516, 1, (VT_VARIANT, 0), params_magic_numbers, u"InsertSurfaceKnot", None, *params_flattened)

    def intersect_breps(self, brep1, brep2, tolerance=None):
        """        
        Intersects a brep object with another  brep object. Note, unlike the SurfaceSurfaceIntersection function this function works on trimmed surfaces.
    
        Parameters
        ==========

        brep1, String, Required        
        The first brep object's identifier.
            
        brep2, String, Required        
        The second  brep object's identifier.
            
        tolerance, Double, Optional        
        The distance tolerance at segment midpoints.  If omitted, the current absolute tolerance is used..
            
        Returns
        =======

        array
        An array of strings identifying the newly created intersection curve and point objects if successful.

        null
        If not successful, or on error.

        """

        params = [brep1, brep2, tolerance]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [brep1, brep2, tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(544, 1, (VT_VARIANT, 0), params_magic_numbers, u"IntersectBreps", None, *params_flattened)

    def is_brep(self, object):
        """        
        Verifies an object is a Brep, or a boundary representation model, object.
    
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

        return self._ApplyTypes_(206, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBrep", None, *params_flattened)

    def is_brep_manifold(self, object):
        """        
        Verifies a polysurface object is manifold.  A polysurface for which every edge is shared by at most two faces is called a manifold.  If a polysurface has at least one edge that is shared by more than two faces, then that polysurface is called non-manifold.
    
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

        return self._ApplyTypes_(854, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsBrepManifold", None, *params_flattened)

    def is_cone(self, surface):
        """        
        Determines if a surface is a portion of a cone.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(885, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCone", None, *params_flattened)

    def is_cylinder(self, surface):
        """        
        Determines if a surface is a portion of a cylinder.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(884, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCylinder", None, *params_flattened)

    def is_parameter_on_surface(self, object, parameter):
        """        
        Verifies that a parameter space point is on a trimmed surface, or not on the trimmed portion of a surface.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Array of ????, Required        
        An array containing the U,V parameter to evaluate.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(parameter)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(879, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsParameterOnSurface", None, *params_flattened)

    def is_plane_surface(self, object):
        """        
        Verifies an object is a plane surface. Plane surfaces can be created by the Plane command. Note, a plane surface is not a planar NURBS surface.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object to verify.
            
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

        return self._ApplyTypes_(638, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPlaneSurface", None, *params_flattened)

    def is_point_in_surface(self, object, point):
        """        
        Verifies that a point is inside a closed surface or polysurface.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        point, Array of ????, Required        
        The test, or sampling, point.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(443, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPointInSurface", None, *params_flattened)

    def is_point_on_surface(self, object, point):
        """        
        Verifies that a point lies on a surface.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        point, Array of ????, Required        
        The test, or sampling, point.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(319, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPointOnSurface", None, *params_flattened)

    def is_poly_surface(self, object):
        """        
        Verifies an object is a polysurface.  Polysurfaces consists of two or more surfaces joined together. If the polysurface fully encloses a volume, it is considered a solid. In some other 3-D programs, this is called a "quilt."
    
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

        return self._ApplyTypes_(207, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPolySurface", None, *params_flattened)

    def is_poly_surface_closed(self, object):
        """        
        Verifies a polysurface object is closed.  If the polysurface fully encloses a volume, it is considered a solid.
    
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

        return self._ApplyTypes_(208, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPolySurfaceClosed", None, *params_flattened)

    def is_poly_surface_planar(self, object):
        """        
        Verifies a polysurface object is planar.
    
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

        return self._ApplyTypes_(209, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsPolySurfacePlanar", None, *params_flattened)

    def is_sphere(self, surface):
        """        
        Determines if a surface is a portion of a sphere.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(883, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSphere", None, *params_flattened)

    def is_surface(self, object):
        """        
        Verifies an object is surface.  Brep objects with only one face are also considered surfaces.
    
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

        return self._ApplyTypes_(210, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSurface", None, *params_flattened)

    def is_surface_closed(self, object, direction):
        """        
        Verifies a surface object is closed in the specified direction.  If the surface fully encloses a volume, it is considered a solid.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The direction, either 0 = U, or 1 = V.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object, direction]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, direction]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(211, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSurfaceClosed", None, *params_flattened)

    def is_surface_periodic(self, object, direction):
        """        
        Verifies a surface object is periodic in the specified direction.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The direction, either 0 = U, or 1 = V.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object, direction]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, direction]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(212, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSurfacePeriodic", None, *params_flattened)

    def is_surface_planar(self, object, tolerance=None):
        """        
        Verifies a surface object is planar.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        tolerance, Double, Optional        
        A tolerance to use when checking. The default is to use Rhino's current absolute tolerance.
            
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

        return self._ApplyTypes_(213, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSurfacePlanar", None, *params_flattened)

    def is_surface_rational(self, object):
        """        
        Verifies a surface object is rational.
    
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

        return self._ApplyTypes_(434, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSurfaceRational", None, *params_flattened)

    def is_surface_singular(self, object, direction):
        """        
        Verifies a surface object is singular in the specified direction.  Surfaces are considered singular if a side collapses to a point.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The direction, either 0 = south, 1 = east, 2 = north, or 3 = west.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [object, direction]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, direction]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(214, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSurfaceSingular", None, *params_flattened)

    def is_surface_trimmed(self, object):
        """        
        Verifies a surface object has been trimmed.
    
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

        return self._ApplyTypes_(269, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsSurfaceTrimmed", None, *params_flattened)

    def is_torus(self, surface):
        """        
        Determines if a surface is a portion of a torus.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(886, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsTorus", None, *params_flattened)

    def join_surfaces(self, object, delete=None):
        """        
        Joins two or more surface or polysurface object together to form one polysurface object.
    
        Parameters
        ==========

        object, String, Required        
        An ordered array of strings identifying the surfaces or polysurfaces objects to join.
            
        delete, Boolean, Optional        
        Delete input objects after joining.  The default is not to delete objects (False).
            
        Returns
        =======

        string
        The identifier of the newly created polysurface object if successful.

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

        return self._ApplyTypes_(487, 1, (VT_VARIANT, 0), params_magic_numbers, u"JoinSurfaces", None, *params_flattened)

    def make_surface_non_periodic(self, object, direction, delete=None):
        """        
        Makes a periodic surface non-periodic. Non-periodic surfaces can develop kinks when deformed.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The direction to make non-periodic, either 0 = U, or 1 = V.
            
        delete, Boolean, Optional        
        Delete input surface.  If omitted, the input surface will not be deleted (False).
            
        Returns
        =======

        string
        If blnDelete is False, the identifier of the new object if successful.

        string
        If blnDelete is True, the identifier of the modified object if successful.

        null
        If not successful, or on error.

        """

        params = [object, direction, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [object, direction, delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(926, 1, (VT_VARIANT, 0), params_magic_numbers, u"MakeSurfaceNonPeriodic", None, *params_flattened)

    def make_surface_periodic(self, object, direction, delete=None):
        """        
        Makes an existing surface a periodic NURBS surface.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The direction to make periodic, either 0 = U, or 1 = V.
            
        delete, Boolean, Optional        
        Delete input surface.  If omitted, the input surface will not be deleted (False).
            
        Returns
        =======

        string
        If blnDelete is False, the identifier of the new object if successful.

        string
        If blnDelete is True, the identifier of the modified object if successful.

        null
        If not successful, or on error.

        """

        params = [object, direction, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [object, direction, delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(445, 1, (VT_VARIANT, 0), params_magic_numbers, u"MakeSurfacePeriodic", None, *params_flattened)

    def offset_surface(self, object, distance):
        """        
        Offsets a surface by a distance. The offset surface will be added to Rhino.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        distance, Double, Required        
        The distance to offset.
            
        Returns
        =======

        string
        The identifier of the new object if successful.

        null
        If not successful, or on error.

        """

        params = [object, distance]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1)]
        params_flattened = [object, distance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(635, 1, (VT_VARIANT, 0), params_magic_numbers, u"OffsetSurface", None, *params_flattened)

    def pull_curve(self, surface, curve, delete=None):
        """        
        Pulls a curve object to a surface object. For more information, see the Rhino help file for information on the Pull command.
    
        Parameters
        ==========

        surface, String, Required        
        The identifier of the surface object that pulls.
            
        curve, String, Required        
        The identifier of the curve object to pull.
            
        delete, Boolean, Optional        
        Delete input curve.  If omitted, the input curve will not be deleted (False).
            
        Returns
        =======

        array
        The identifiers of the new curve objects if successful.

        null
        If not successful, or on error.

        """

        params = [surface, curve, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [surface, curve, delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(493, 1, (VT_VARIANT, 0), params_magic_numbers, u"PullCurve", None, *params_flattened)

    def rebuild_surface(self, object, degree=None, point_count=None):
        """        
        Rebuilds a surface to given degree and control point count.  For more information, see the Rhino help file for the Rebuild command.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        degree, Array of ????, Optional        
        An array of two numbers that identify the surface curve degree in both the U and the V directions. Each degree value must be greater than 1. The default is 3 in each direction.
            
        point_count, Array of ????, Optional        
        An array of two numbers that identify the surface point count in both the U and the V directions.  The point count must be greater than the degree.  The default value is 10 in each direction.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [object, degree, point_count]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(degree), flatten(point_count)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(816, 1, (VT_VARIANT, 0), params_magic_numbers, u"RebuildSurface", None, *params_flattened)

    def remove_surface_knot(self, object, parameter, direction):
        """        
        Deletes a knot-line from a surface object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the surface object.
            
        parameter, Double, Required        
        An array containing a U,V parameter on the surface.  Note, if the parameter is not equal to one of the existing knots, then the knot closest to the specified parameter will be removed.
            
        direction, Integer, Required        
        The direction for knot insertion, either 0 = U, or 1 = V.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        On error.

        """

        params = [object, parameter, direction]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_I2, 1)]
        params_flattened = [object, parameter, direction]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(917, 1, (VT_VARIANT, 0), params_magic_numbers, u"RemoveSurfaceKnot", None, *params_flattened)

    def reverse_surface(self, object, direction):
        """        
        Reverses the U and V directions of a surface object. This feature can also be found in Rhino's Dir command.
		To reverse the normal direction of a surface, use the FlipSurface method.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The direction to reverse. Values can be added together so as to reverse more than one direction.
		Value
		Description
		1
		Reverse the surface in the U direction.
		2
		Reverse the surface in the V direction.
		4
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [object, direction]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, direction]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(927, 1, (VT_VARIANT, 0), params_magic_numbers, u"ReverseSurface", None, *params_flattened)

    def short_path(self, surface, start, end):
        """        
        Creates the shortest possible curve (geodesic) between two points on a surface. For more details, see the ShortPath command in the Rhino help file.
    
        Parameters
        ==========

        surface, String, Required        
        The identifier of the surface object that pulls.
            
        start, Array of ????, Required        
        A 3-D surface point identifying the starting point of the short curve.
            
        end, Array of ????, Required        
        A 3-D surface point identifying the ending point of the short curve.
            
        Returns
        =======

        string
        The identifier of the new curve object if successful.

        null
        If not successful, or on error.

        """

        params = [surface, start, end]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [surface, flatten(start), flatten(end)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(702, 1, (VT_VARIANT, 0), params_magic_numbers, u"ShortPath", None, *params_flattened)

    def shrink_trimmed_surface(self, surface):
        """        
        Shrinks the underlying untrimmed surfaces near to trimming boundaries. For more details, see the ShrinkTrimmedSrf command in the Rhino help file.
    
        Parameters
        ==========

        surface, String, Required        
        The identifier of the surface or polysurface to shrink.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(700, 1, (VT_VARIANT, 0), params_magic_numbers, u"ShrinkTrimmedSurface", None, *params_flattened)

    def split_brep(self, brep, cutter, delete=None):
        """        
        Splits a brep.  A brep can be either a surface with a single face or a polysurface.
    
        Parameters
        ==========

        brep, String, Required        
        The identifier of the brep object to split.
            
        cutter, String, Required        
        The identifier of the brep object to split with.
            
        delete, Boolean, Optional        
        Delete input brep.  If omitted, the input brep will not be deleted (False).
            
        Returns
        =======

        array
        The identifiers of the new brep objects if successful.

        null
        If not successful, or on error.

        """

        params = [brep, cutter, delete]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [brep, cutter, delete]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(637, 1, (VT_VARIANT, 0), params_magic_numbers, u"SplitBrep", None, *params_flattened)

    def surface_area(self, object):
        """        
        Calculates the area of a surface or polysurface object. The results are based on the current drawing units.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of area information if successful.  The array will contain the following information:

        number
        The area.

        number
        The absolute (+/-) error bound for the area.

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

        return self._ApplyTypes_(382, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceArea", None, *params_flattened)

    def surface_area_centroid(self, object):
        """        
        Calculates the area centroid of a surface or polysurface object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of area centroid information if successful.  The array will contain the following information:

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

        return self._ApplyTypes_(384, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceAreaCentroid", None, *params_flattened)

    def surface_area_moments(self, object):
        """        
        Calculates the area moments of inertia of a surface or polysurface object.  For more information, see the Rhino help file for "Mass Properties Calculation Details."
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of area moments of inertia information if successful.  The array will contain the following information:

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

        return self._ApplyTypes_(386, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceAreaMoments", None, *params_flattened)

    def surface_closest_point(self, object, point):
        """        
        Returns the UV parameter of the point on a surface that is closest to a test point.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        point, Array of ????, Required        
        The test, or sampling, point.
            
        Returns
        =======

        array
        An array containing the U,V parameters of the closest point on the surface if successful.

        null
        If not successful, or on error.

        """

        params = [object, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(215, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceClosestPoint", None, *params_flattened)

    def surface_cone(self, surface):
        """        
        Returns the definition of a cone surface.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        array
        An array containing the definition of the cone if successful.  The elements of the array are as follows:

        array
        The plane of the cone.  The apex of cone is at plane's origin and  the axis of the cone is plane's z-axis.

        number
        The height of the cone.

        number
        The radius of the cone.

        null
        If not successful, or on error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(889, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceCone", None, *params_flattened)

    def surface_contour_points(self, object, start_point, end_point, interval=None, angle=None):
        """        
        Returns the vertices of the polyline curves generated by contouring a surface or polysurface object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of a surface or polysurface object.
            
        start_point, Array of ????, Required        
        The 3-D starting point of a center line.
            
        end_point, Array of ????, Required        
        The 3-D ending point of a center line.
            
        interval, Double, Optional        
        The distance between contour curves.  If omitted, the interval will be equal to the diagonal distance of the object's bounding box divided by 50.
            
        angle, Double, Optional        
        The maximum angle in degrees between unit tangents at adjacent vertices.  If omitted, the maximum angle will be set to 5.0 degrees.
            
        Returns
        =======

        array
        An array of 3-D point arrays, one for each contour, if successful.

        null
        If not successful, or on error.

        """

        params = [object, start_point, end_point, interval, angle]
        params_required = [True, True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [object, flatten(start_point), flatten(end_point), interval, angle]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(79, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceContourPoints", None, *params_flattened)

    def surface_curvature(self, object, parameter):
        """        
        Returns the curvature of a surface at a U,V parameter.  See the Rhino help file for details on surface curvature.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Array of ????, Required        
        An array containing the U,V parameter to evaluate.
            
        Returns
        =======

        array
        An array of curvature information if successful.  The array will contain the following information:

        number
        Maximum principal curvature.

        number
        Minimum principal curvature.

        number
        Gaussian curvature.

        number
        Mean curvature.

        null
        If not successful, or on error.

        """

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(parameter)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(378, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceCurvature", None, *params_flattened)

    def surface_curvature_analysis(self, object):
        """        
        Returns the curvature of a surface.  See the Rhino help file for details on surface curvature analysis.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of curvature information if successful.  The array will contain the following information:

        array
        An array containing three values: the min Gaussian curvature, the max Gaussian curvature, and the infinity status.

        array
        An array containing three values: the min unsigned mean curvature, the max unsigned mean curvature, and the infinity comparison.

        array
        An array containing three values: the min maximum unsigned radius of curvature, the max maximum unsigned radius of curvature, and the infinity comparison.

        array
        An array containing three values: the min minimum unsigned radius of curvature, the max minimum unsigned radius of curvature, and the infinity comparison.

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

        return self._ApplyTypes_(632, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceCurvatureAnalysis", None, *params_flattened)

    def surface_cylinder(self, surface):
        """        
        Returns the definition of a cylinder surface.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        array
        An array containing the definition of the cylinder if successful.  The elements of the array are as follows:

        array
        The base plane of the cylinder.

        number
        The height of the cylinder.

        number
        The radius of the cylinder.

        null
        If not successful, or on error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(888, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceCylinder", None, *params_flattened)

    def surface_degree(self, object, direction=None):
        """        
        Returns the degree of a  surface object in the specified direction.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Optional        
        The direction, either 0 = U, or 1 = V, or 2 = Both.  Of omitted, both the degrees in the U and V directions are returned (2 = Both).
            
        Returns
        =======

        array
        If intDirection is not specified, or intDirection is set to 2, then the degree in both the U and V directions is returned.

        number
        If intDirection is specified, and intDirection is set to either 0 or 1, then the degree in either the U or V direction is returned.

        null
        If not successful, or on error.

        """

        params = [object, direction]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, direction]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(216, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceDegree", None, *params_flattened)

    def surface_domain(self, object, direction):
        """        
        Returns the domain of a  surface object in the specified direction.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The direction, either 0 = U, or 1 = V.
            
        Returns
        =======

        array
        An array containing the domain interval in the specified direction if successful.

        null
        If not successful, or on error.

        """

        params = [object, direction]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, direction]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(217, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceDomain", None, *params_flattened)

    def surface_edit_points(self, object, return_parameters=None, return_all=None):
        """        
        Returns the edit, or Greville, points of a surface object.  For each surface control point, there is a corresponding edit point.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        return_parameters, Boolean, Optional        
        If False (default), edit points are returned as an array of 3-D points. If True, edit points are returned as an array U,V surface parameters.
            
        return_all, Boolean, Optional        
        If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.
            
        Returns
        =======

        array
        If blnReturnParameters is omitted or False, then an array of 3-D edit points if successful.

        array
        If blnReturnParameters is True, then an array of U,V parameter values if successful.

        null
        If not successful, or on error.

        """

        params = [object, return_parameters, return_all]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [object, return_parameters, return_all]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(427, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceEditPoints", None, *params_flattened)

    def surface_evaluate(self, object, parameter, derivative):
        """        
        A general purpose surface evaluator.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Array of ????, Required        
        An array containing the U,V parameter to evaluate.
            
        derivative, Integer, Required        
        The number of derivatives to evaluate.
            
        Returns
        =======

        array
        An array of length (intDerivative+1)*(intDerivative+2)/2 if successful.  The array elements are as follows:

        array
        The 3-D point.

        array
        The first derivative.

        array
        The first derivative.

        array
        The second derivative.

        array
        The second derivative.

        array
        The second derivative.

        array
        etc...

        null
        If not successful, or on error.

        """

        params = [object, parameter, derivative]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_I2, 1)]
        params_flattened = [object, flatten(parameter), derivative]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(583, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceEvaluate", None, *params_flattened)

    def surface_frame(self, object, parameter):
        """        
        Returns a plane based on the normal, u, and v directions at a given surface U,V parameter.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Array of ????, Required        
        An array containing the U,V parameter to evaluate.
            
        Returns
        =======

        array
        The plane at the specified parameter if successful.

        null
        If not successful, or on error.

        """

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(parameter)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(623, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceFrame", None, *params_flattened)

    def surface_isocurve_density(self, object, density=None):
        """        
        Returns or sets the isocurve density of a surface or polysurface object. An isoparametric curve is a curve of constant U or V value on a surface. Rhino uses isocurves and surface edge curves to visualize the shape of a NURBS surface.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        density, Integer, Optional        
        The isocurve wireframe density.  The possible values are as follows:
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

        number
        The intDensity is not specified, then the current isocurve density if successful.

        number
        The intDensity is specified, then the previous isocurve density if successful.

        null
        If not successful, or on error.

        """

        params = [object, density]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [object, density]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(361, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceIsocurveDensity", None, *params_flattened)

    def surface_knot_count(self, object):
        """        
        Returns the knot count of a surface object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        The number of knots in the U and V directions if successful.

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

        return self._ApplyTypes_(431, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceKnotCount", None, *params_flattened)

    def surface_knots(self, object):
        """        
        Returns the knots, or knot vector, of a surface object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        The knot values of the surface if successful.

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

        return self._ApplyTypes_(432, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceKnots", None, *params_flattened)

    def surface_normal(self, object, parameter):
        """        
        Returns a 3-D vector that is the normal to a surface at a parameter.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        parameter, Array of ????, Required        
        An array containing the UV parameter to evaluate.
            
        Returns
        =======

        array
        A 3-D vector if successful.

        null
        If not successful, or on error.

        """

        params = [object, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(parameter)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(362, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceNormal", None, *params_flattened)

    def surface_point_count(self, object):
        """        
        Returns the control points count of a surface object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        The number of control points in the U and V directions if successful.

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

        return self._ApplyTypes_(218, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfacePointCount", None, *params_flattened)

    def surface_points(self, object, return_all=None):
        """        
        Returns the control points, or control vertices, of a surface object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        return_all, Boolean, Optional        
        If True (default) all surface edit points are returned. If False, the function will returned surface edit points based on whether or not the surface is closed or periodic.
            
        Returns
        =======

        array
        The control points of the surface if successful.

        null
        If not successful, or on error.

        """

        params = [object, return_all]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, return_all]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(372, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfacePoints", None, *params_flattened)

    def surface_principal_curvature(self, object, point):
        """        
        Adds curvature curves at the evaluated point on a surface. For more information, see the Rhino help file for the Curvature command.
    
        Parameters
        ==========

        object, String, Required        
        The curve's identifier.
            
        point, Array of ????, Required        
        A point on the curve to evaluate.
            
        Returns
        =======

        array
        An array of two strings that identify the Maximum and Minimum principal curvature curves, respectively, if successful.

        null
        If not successful, or on error.

        """

        params = [object, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [object, flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(717, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfacePrincipalCurvature", None, *params_flattened)

    def surface_seam(self, object, direction, parameter):
        """        
        Changes the seam of a closed surface. For more information, see the Rhino help file for the SrfSeam command.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        direction, Integer, Required        
        The parameter direction, where 0 = U and 1 = V.
            
        parameter, Double, Required        
        The parameter at which to place the seam.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        On error.

        """

        params = [object, direction, parameter]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_R8, 1)]
        params_flattened = [object, direction, parameter]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(804, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceSeam", None, *params_flattened)

    def surface_sphere(self, surface):
        """        
        Returns the definition of a sphere surface.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        array
        An array containing the definition of the sphere if successful.  The elements of the array are as follows:

        array
        The equatorial plane of the sphere.  The origin of the plane will be the center point of the sphere.

        number
        The radius of the sphere.

        null
        If not successful, or on error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(887, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceSphere", None, *params_flattened)

    def surface_surface_intersection(self, surface_a, surface_b, tolerance=None, create=None):
        """        
        Calculates the intersection of a surface object with another surface object. Note, this function works on untrimmed surfaces.
    
        Parameters
        ==========

        surface_a, String, Required        
        The identifier of the first surface object.
            
        surface_b, String, Required        
        The identifier of the second surface object.
            
        tolerance, Double, Optional        
        The absolute tolerance in drawing units.  If omitted, the document's current absolute tolerance is used.
            
        create, Boolean, Optional        
        Create the intersection curves and points.  If omitted, intersection geometry will not be created.
            
        Returns
        =======

        array
        If blnCreate is not specified or is equal to False, an array numbers identifying the intersection event type if successful.  The array will contain one or more of the following intersection event types:

        array
        If blnCreate is specified and is equal to True, a two-dimensional array of intersection information if successful.  The array will contain one or more of the following elements:

        number
        The intersection event type.  See the above table for details.

        string
        The identifier of the intersection curve or point object that was created.

        null
        If not successful, or on error.

        """

        params = [surface_a, surface_b, tolerance, create]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_R8, 1), (VT_BOOL, 1)]
        params_flattened = [surface_a, surface_b, tolerance, create]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(484, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceSurfaceIntersection", None, *params_flattened)

    def surface_torus(self, surface):
        """        
        Returns the definition of a torus surface.
    
        Parameters
        ==========

        surface, String, Required        
        The surface object's identifier.
            
        Returns
        =======

        array
        An array containing the definition of the torus if successful.  The elements of the array are as follows:

        array
        The base plane of the torus.

        number
        The major radius of the torus.

        number
        The minor radius of the torus.

        null
        If not successful, or on error.

        """

        params = [surface]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [surface]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(890, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceTorus", None, *params_flattened)

    def surface_volume(self, object):
        """        
        Calculates the volume of closed surface or polysurface objects.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of volume information if successful.  The array will contain the following information:

        number
        The volume.

        number
        The absolute (+/-) error bound for the volume.

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

        return self._ApplyTypes_(383, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceVolume", None, *params_flattened)

    def surface_volume_centroid(self, object):
        """        
        Calculates the volume centroid of closed surface or polysurface objects.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of volume centroid information if successful.  The array will contain the following information:

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

        return self._ApplyTypes_(385, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceVolumeCentroid", None, *params_flattened)

    def surface_volume_moments(self, object):
        """        
        Calculates the volume moments of inertia of closed surface or polysurface objects.  For more information, see the Rhino help file for "Mass Properties Calculation Details."
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        An array of volume moments of inertia information if successful.  The array will contain the following information:

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

        return self._ApplyTypes_(387, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceVolumeMoments", None, *params_flattened)

    def surface_weights(self, object):
        """        
        Returns an array of weight values that are assigned to the control points of a surface.  The number of weights returned will be equal to the number of control points in the U and V directions.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        array
        The weight values of the surface if successful.

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

        return self._ApplyTypes_(433, 1, (VT_VARIANT, 0), params_magic_numbers, u"SurfaceWeights", None, *params_flattened)

