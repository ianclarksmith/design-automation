# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class LineAndPlane(IRhinoScript):



    def distance_to_plane(self, plane, point):
        """        
        Returns the distance from a 3-D point to a plane.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            
        point, Array of ????, Required        
        The 3-D point.
            
        Returns
        =======

        number
        The distance if successful.

        null
        If not successful, or on error.

        """

        params = [plane, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane), flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(628, 1, (VT_VARIANT, 0), params_magic_numbers, u"DistanceToPlane", None, *params_flattened)

    def evaluate_plane(self, plane, parameter):
        """        
        Evaluates a plane at a U,V parameter.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            
        parameter, Array of ????, Required        
        An array containing the U,V parameter to evaluate.
            
        Returns
        =======

        array
        The 3-D point if successful.

        null
        If not successful, or on error.

        """

        params = [plane, parameter]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane), flatten(parameter)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(751, 1, (VT_VARIANT, 0), params_magic_numbers, u"EvaluatePlane", None, *params_flattened)

    def intersect_planes(self, plane1, plane2, plane3):
        """        
        Calculates the intersection of three planes.
    
        Parameters
        ==========

        plane1, Array of ????, Required        
        The first plane to intersect.
            
        plane2, Array of ????, Required        
        The second plane to intersect.
            
        plane3, Array of ????, Required        
        The third plane to intersect.
            
        Returns
        =======

        array
        The 3-D point of intersection is successful.

        null
        If not successful, or on error.

        """

        params = [plane1, plane2, plane3]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane1), flatten(plane2), flatten(plane3)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(745, 1, (VT_VARIANT, 0), params_magic_numbers, u"IntersectPlanes", None, *params_flattened)

    def line_closest_point(self, line, point):
        """        
        Finds the point on an infinite line that is closest to a test point.
    
        Parameters
        ==========

        line, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the line.
            
        point, Array of ????, Required        
        The test point.
            
        Returns
        =======

        array
        The point on the line that is closest to the test point is successful.

        null
        If not successful, or on error.

        """

        params = [line, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(line), flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(899, 1, (VT_VARIANT, 0), params_magic_numbers, u"LineClosestPoint", None, *params_flattened)

    def line_is_farther_than(self, line, distance, point, line2):
        """        
        Determines if the shortest distance from a line to a point or another line is greater than a specified distance.
    
        Parameters
        ==========

        line, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the line.
            
        distance, Double, Required        
        The distance.
            
        point, Array of ????, Required        
        The test point.
            
        line2, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the test line.
            
        Returns
        =======

        boolean
        True if the shortest distance from the line to the other object is greater than dblDistance, False otherwise.

        null
        On error.

        """

        params = [line, distance, point, line2]
        params_required = [True, True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(line), distance, flatten(point), flatten(line2)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(902, 1, (VT_VARIANT, 0), params_magic_numbers, u"LineIsFartherThan", None, *params_flattened)

    def line_line_intersection(self, line_a, line_b, planar=None):
        """        
        Calculates the intersection of two non-parallel.  Note, the two lines do not have to intersect for an intersection to be found.
		The default operation of this function assumes that the two lines are co-planar.  Thus, the return value is the intersection point of the two lines.
		But, two lines in three dimensions generally do not intersect at a point. They may be parallel (no intersections) or they may be coincident (infinite intersections). But, most often only their projection onto a plane intersects. When they do not exactly intersect at a point they can be connected by a line segment, the shortest line segment is unique and is often considered to be their intersection in 3-D.
    
        Parameters
        ==========

        line_a, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the first line.
            
        line_b, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the second line.
            
        planar, Boolean, Optional        
        Assume that the two lines are co-planar. The default value is True.
            
        Returns
        =======

        array
        If blnPlanar is omitted or True, then a single 3-D intersection point if successful.

        array
        If blnPlanar is False, then an array containing a point on the first line and a point on the second line if successful.

        null
        If not successful, or on error.

        """

        params = [line_a, line_b, planar]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(line_a), flatten(line_b), planar]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(736, 1, (VT_VARIANT, 0), params_magic_numbers, u"LineLineIntersection", None, *params_flattened)

    def line_max_distance_to(self, line, point, line2):
        """        
        Finds the longest distance between the line, as a finite chord, and a point or another line.
    
        Parameters
        ==========

        line, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the line.
            
        point, Array of ????, Required        
        The test point.
            
        line2, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the test line (another finite chord).
            
        Returns
        =======

        boolean
        A distance (D) such that if Q is any point on the line and P is any point on the other object, then D >= Rhino.Distance(Q, P).

        null
        On error.

        """

        params = [line, point, line2]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(line), flatten(point), flatten(line2)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(901, 1, (VT_VARIANT, 0), params_magic_numbers, u"LineMaxDistanceTo", None, *params_flattened)

    def line_min_distance_to(self, line, point, line2):
        """        
        Finds the shortest distance between the line, as a finite chord, and a point or another line.
    
        Parameters
        ==========

        line, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the line.
            
        point, Array of ????, Required        
        The test point.
            
        line2, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the test line (another finite chord).
            
        Returns
        =======

        boolean
        A distance (D) such that if Q is any point on the line and P is any point on the other object, then D <= Rhino.Distance(Q, P).

        null
        On error.

        """

        params = [line, point, line2]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(line), flatten(point), flatten(line2)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(900, 1, (VT_VARIANT, 0), params_magic_numbers, u"LineMinDistanceTo", None, *params_flattened)

    def line_plane(self, line):
        """        
        Returns a plane that contains the line.  The origin of the plane is at the start of the line.  If possible, a plane parallel to the world XY, YZ or ZX plane is returned.
    
        Parameters
        ==========

        line, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the line.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [line]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(line)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(898, 1, (VT_VARIANT, 0), params_magic_numbers, u"LinePlane", None, *params_flattened)

    def line_plane_intersection(self, line, point):
        """        
        Calculates the intersection of a line and a plane.
    
        Parameters
        ==========

        line, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the line to intersect.
            
        point, Array of ????, Required        
        The plane to intersect.
            
        Returns
        =======

        array
        The 3-D point of intersection is successful.

        null
        If not successful, or on error.

        """

        params = [line, point]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(line), flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(743, 1, (VT_VARIANT, 0), params_magic_numbers, u"LinePlaneIntersection", None, *params_flattened)

    def line_transform(self, line, xform):
        """        
        Transforms a line.
    
        Parameters
        ==========

        line, Array of ????, Required        
        Two 3-D points identifying the starting and ending points of the line.
            
        xform, Array of ????, Required        
        A valid 4x4 transformation matrix.
            
        Returns
        =======

        array
        The resulting line if successful.

        null
        On error.

        """

        params = [line, xform]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(line), flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(897, 1, (VT_VARIANT, 0), params_magic_numbers, u"LineTransform", None, *params_flattened)

    def move_plane(self, plane, origin):
        """        
        Moves the origin of a plane.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            
        origin, Array of ????, Required        
        A 3-D point identifying the new origin location.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [plane, origin]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane), flatten(origin)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(631, 1, (VT_VARIANT, 0), params_magic_numbers, u"MovePlane", None, *params_flattened)

    def plane_closest_point(self, plane, point, return_point=None):
        """        
        Returns the point on a plane that is closest to a test point.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane. The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            
        point, Array of ????, Required        
        The 3-D point to test.
            
        return_point, Boolean, Optional        
        If omitted or True, then the point on the plane that is closest to the test point is returned. If False, then the parameter of the point on the plane that is closest to the test point is returned.
            
        Returns
        =======

        array
        If blnReturnPoint is omitted or True, then the 3-D point if successful. If blnReturnPoint is False, then an array containing the U,V parameters of the point if successful.

        null
        If not successful, or on error.

        """

        params = [plane, point, return_point]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(plane), flatten(point), return_point]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(629, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlaneClosestPoint", None, *params_flattened)

    def plane_equation(self, plane):
        """        
        Returns the equation of  a plane. The standard equation of a plane with a non-zero normal vector is as follows:
		Ax + By + Cz + D = 0
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane. The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            
        Returns
        =======

        array
        An array containing four numbers that represent the coefficients of the equation, if successful.

        null
        If not successful, or on error.

        """

        params = [plane]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(642, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlaneEquation", None, *params_flattened)

    def plane_fit_from_points(self, points):
        """        
        Returns a plane that was fit through an array of 3-D points.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

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

        return self._ApplyTypes_(725, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlaneFitFromPoints", None, *params_flattened)

    def plane_from_frame(self, origin, xaxis, yaxis):
        """        
        Construct a plane from a point, and two vectors in the plane.
    
        Parameters
        ==========

        origin, Array of ????, Required        
        A 3-D point identifying the origin of the plane.
            
        xaxis, Array of ????, Required        
        A non-zero 3-D vector in the plane that determines the X axis direction.
            
        yaxis, Array of ????, Required        
        A non-zero 3-D vector not parallel to arrXaxis that is used to determine the Y axis direction. Note, arrYaxis does not have to be perpendicular to arrXaxis.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [origin, xaxis, yaxis]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(origin), flatten(xaxis), flatten(yaxis)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(627, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlaneFromFrame", None, *params_flattened)

    def plane_from_normal(self, origin, normal):
        """        
        Creates a plane from an origin point and a normal direction vector.
    
        Parameters
        ==========

        origin, Array of ????, Required        
        A 3-D point identifying the origin of the plane.
            
        normal, Array of ????, Required        
        A non-zero 3-D vector identifying the normal direction of the plane.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [origin, normal]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(origin), flatten(normal)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(626, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlaneFromNormal", None, *params_flattened)

    def plane_from_points(self, origin, point_x, point_y):
        """        
        Creates a plane from three non-colinear points.
    
        Parameters
        ==========

        origin, Array of ????, Required        
        The first point, or origin, of the plane.
            
        point_x, Array of ????, Required        
        A point on the plane's X axis.
            
        point_y, Array of ????, Required        
        A point on the plane's Y axis.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [origin, point_x, point_y]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(origin), flatten(point_x), flatten(point_y)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(649, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlaneFromPoints", None, *params_flattened)

    def plane_plane_intersection(self, plane1, point2):
        """        
        Calculates the intersection of two planes.
    
        Parameters
        ==========

        plane1, Array of ????, Required        
        The first plane to intersect.
            
        point2, Array of ????, Required        
        The second plane to intersect.
            
        Returns
        =======

        array
        Two 3-D points identifying the starting and ending points of the intersection line.

        null
        If not successful, or on error.

        """

        params = [plane1, point2]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane1), flatten(point2)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(744, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlanePlaneIntersection", None, *params_flattened)

    def plane_transform(self, plane, xform):
        """        
        Transforms a plane.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane to transform.
            
        xform, Array of ????, Required        
        A valid 4x4 transformation matrix.
            
        Returns
        =======

        array
        The resulting plane if successful.

        null
        On error.

        """

        params = [plane, xform]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane), flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(801, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlaneTransform", None, *params_flattened)

    def rotate_plane(self, plane, angle, axis):
        """        
        Rotates a plane.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            
        angle, Double, Required        
        The rotation angle in degrees.
            
        axis, Array of ????, Required        
        A non-zero 3-D vector identifying the axis of rotation.
            
        Returns
        =======

        array
        The plane if successful.  The elements of a plane array are as follows:

        null
        If not successful, or on error.

        """

        params = [plane, angle, axis]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane), angle, flatten(axis)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(630, 1, (VT_VARIANT, 0), params_magic_numbers, u"RotatePlane", None, *params_flattened)

    def world_x_y_plane():
        """        
        Returns Rhino's world XY plane. This plane could also be created as follows:
		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(1.0,0.0,0.0), Array(0.0,1.0,0.0)
    
        No parameters

        Returns
        =======

        array
        Rhino's world XY plane.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(652, 1, (VT_VARIANT, 0), params_magic_numbers, u"WorldXYPlane", None, *params_flattened)

    def world_y_z_plane():
        """        
        Returns Rhino's world YZ plane. This plane could also be created as follows:
		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,1.0,0.0), Array(0.0,0.0,1.0)
    
        No parameters

        Returns
        =======

        array
        Rhino's world YZ plane.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(653, 1, (VT_VARIANT, 0), params_magic_numbers, u"WorldYZPlane", None, *params_flattened)

    def world_z_x_plane():
        """        
        Returns Rhino's world ZX plane. This plane could also be created as follows:
		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,0.0,1.0), Array(1.0,0.0,0.0)
    
        No parameters

        Returns
        =======

        array
        Rhino's world ZX plane.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(654, 1, (VT_VARIANT, 0), params_magic_numbers, u"WorldZXPlane", None, *params_flattened)

