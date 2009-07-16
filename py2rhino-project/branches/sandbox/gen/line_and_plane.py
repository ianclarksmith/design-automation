# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class LineAndPlane(DispatchBaseClass):



    def distance_to_plane(self, plane, point):
        """

        Returns the distance from a 3-D point to a plane.

        Parameters

        Plane : Required, Array, arr
        Point : Required, Array, arr

        Returns

        Number : The distance if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(628, 1, (12, 0), ((12, 0), (12, 0)), u'DistanceToPlane', None, plane, point)

    def evaluate_plane(self, plane, parameter):
        """

        Evaluates a plane at a U,V parameter.

        Parameters

        Plane : Required, Array, arr
        Parameter : Required, Array, arr

        Returns

        Array : The 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(751, 1, (12, 0), ((12, 0), (12, 0)), u'EvaluatePlane', None, plane, parameter)

    def intersect_planes(self, plane1, plane2, plane3):
        """

        Calculates the intersection of three planes.

        Parameters

        Plane1 : Required, Array, arr
        Plane2 : Required, Array, arr
        Plane3 : Required, Array, arr

        Returns

        Array : The 3-D point of intersection is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(745, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'IntersectPlanes', None, plane1, plane2, plane3)

    def line_closest_point(self, line, point):
        """

        Finds the point on an infinite line that is closest to a test point.

        Parameters

        Line : Required, Array, arr
        Point : Required, Array, arr

        Returns

        Array : The point on the line that is closest to the test point is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(899, 1, (12, 0), ((12, 0), (12, 0)), u'LineClosestPoint', None, line, point)

    def line_is_farther_than(self, line, distance, point, line2):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def line_line_intersection(self, line_a, line_b, planar):
        """

        But, two lines in three dimensions generally do not intersect at a point. They may be parallel (no intersections) or they may be coincident (infinite intersections). But, most often only their projection onto a plane intersects. When they do not exactly intersect at a point they can be connected by a line segment, the shortest line segment is unique and is often considered to be their intersection in 3-D.

        Parameters

        LineA : Required, Array, arr
        LineB : Required, Array, arr
        Planar : Optional, Boolean, bln

        Returns

        Array : If blnPlanar is omitted or True, then a single 3-D intersection point if successful.
        Array : If blnPlanar is False, then an array containing a point on the first line and a point on the second line if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(736, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'LineLineIntersection', None, line_a, line_b, planar)

    def line_max_distance_to(self, line, point, line2):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def line_min_distance_to(self, line, point, line2):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def line_plane(self, line):
        """

        Returns a plane that contains the line.  The origin of the plane is at the start of the line.  If possible, a plane parallel to the world XY, YZ or ZX plane is returned.

        Parameters

        Line : Required, Array, arr

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(898, 1, (12, 0), ((12, 0)), u'LinePlane', None, line)

    def line_plane_intersection(self, line, point):
        """

        Calculates the intersection of a line and a plane.

        Parameters

        Line : Required, Array, arr
        Point : Required, Array, arr

        Returns

        Array : The 3-D point of intersection is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(743, 1, (12, 0), ((12, 0), (12, 0)), u'LinePlaneIntersection', None, line, point)

    def line_transform(self, line, xform):
        """

        Transforms a line.

        Parameters

        Line : Required, Array, arr
        Xform : Required, Array, arr

        Returns

        Array : The resulting line if successful.
        Null : On error.

        """

        return self._ApplyTypes_(897, 1, (12, 0), ((12, 0), (12, 0)), u'LineTransform', None, line, xform)

    def move_plane(self, plane, origin):
        """

        Moves the origin of a plane.

        Parameters

        Plane : Required, Array, arr
        Origin : Required, Array, arr

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(631, 1, (12, 0), ((12, 0), (12, 0)), u'MovePlane', None, plane, origin)

    def plane_closest_point(self, plane, point, return_point):
        """

        Returns the point on a plane that is closest to a test point.

        Parameters

        Plane : Required, Array, arr
        Point : Required, Array, arr
        ReturnPoint : Optional, Boolean, bln

        Returns

        Array : If blnReturnPoint is omitted or True, then the 3-D point if successful. If blnReturnPoint is False, then an array containing the U,V parameters of the point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(629, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'PlaneClosestPoint', None, plane, point, return_point)

    def plane_equation(self, plane):
        """

        Ax + By + Cz + D = 0

        Parameters

        Plane : Required, Array, arr

        Returns

        Array : An array containing four numbers that represent the coefficients of the equation, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(642, 1, (12, 0), ((12, 0)), u'PlaneEquation', None, plane)

    def plane_fit_from_points(self, points):
        """

        Returns a plane that was fit through an array of 3-D points.

        Parameters

        Points : Required, Array, arr

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(725, 1, (12, 0), ((12, 0)), u'PlaneFitFromPoints', None, points)

    def plane_from_frame(self, origin, xaxis, yaxis):
        """

        Construct a plane from a point, and two vectors in the plane.

        Parameters

        Origin : Required, Array, arr
        Xaxis : Required, Array, arr
        Yaxis : Required, Array, arr

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(627, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'PlaneFromFrame', None, origin, xaxis, yaxis)

    def plane_from_normal(self, origin, normal):
        """

        Creates a plane from an origin point and a normal direction vector.

        Parameters

        Origin : Required, Array, arr
        Normal : Required, Array, arr

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(626, 1, (12, 0), ((12, 0), (12, 0)), u'PlaneFromNormal', None, origin, normal)

    def plane_from_points(self, origin, point_x, point_y):
        """

        Creates a plane from three non-colinear points.

        Parameters

        Origin : Required, Array, arr
        PointX : Required, Array, arr
        PointY : Required, Array, arr

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(649, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'PlaneFromPoints', None, origin, point_x, point_y)

    def plane_plane_intersection(self, plane1, point2):
        """

        Calculates the intersection of two planes.

        Parameters

        Plane1 : Required, Array, arr
        Point2 : Required, Array, arr

        Returns

        Array : Two 3-D points identifying the starting and ending points of the intersection line.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(744, 1, (12, 0), ((12, 0), (12, 0)), u'PlanePlaneIntersection', None, plane1, point2)

    def plane_transform(self, plane, xform):
        """

        Transforms a plane.

        Parameters

        Plane : Required, Array, arr
        Xform : Required, Array, arr

        Returns

        Array : The resulting plane if successful.
        Null : On error.

        """

        return self._ApplyTypes_(801, 1, (12, 0), ((12, 0), (12, 0)), u'PlaneTransform', None, plane, xform)

    def rotate_plane(self, plane, angle, axis):
        """

        Rotates a plane.

        Parameters

        Plane : Required, Array, arr
        Angle : Required, Number, dbl
        Axis : Required, Array, arr

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(630, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'RotatePlane', None, plane, angle, axis)

    def world_x_y_plane(self):
        """

        Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(1.0,0.0,0.0), Array(0.0,1.0,0.0)

        No parameters

        Returns

        Array : Rhino's world XY plane.

        """

        return self._ApplyTypes_(652, 1, (12, 0), (), u'WorldXYPlane', None, )

    def world_y_z_plane(self):
        """

        Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,1.0,0.0), Array(0.0,0.0,1.0)

        No parameters

        Returns

        Array : Rhino's world YZ plane.

        """

        return self._ApplyTypes_(653, 1, (12, 0), (), u'WorldYZPlane', None, )

    def world_z_x_plane(self):
        """

        Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,0.0,1.0), Array(1.0,0.0,0.0)

        No parameters

        Returns

        Array : Rhino's world ZX plane.

        """

        return self._ApplyTypes_(654, 1, (12, 0), (), u'WorldZXPlane', None, )

