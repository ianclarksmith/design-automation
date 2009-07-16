# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class LineAndPlane(DispatchBaseClass):



    def distance_to_plane(self, arr_plane, arr_point):
        """

        Returns the distance from a 3-D point to a plane.

        Parameters

        arrPlane : Required, Array, The plane
        arrPoint : Required, Array, The 3-D point

        Returns

        Number : The distance if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DistanceToPlane', None, arrPlane, arrPoint)

    def evaluate_plane(self, arr_plane, arr_parameter):
        """

        Evaluates a plane at a U,V parameter.

        Parameters

        arrPlane : Required, Array, The plane
        arrParameter : Required, Array, An array containing the U,V parameter to evaluate

        Returns

        Array : The 3-D point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'EvaluatePlane', None, arrPlane, arrParameter)

    def intersect_planes(self, arr_plane1, arr_plane2, arr_plane3):
        """

        Calculates the intersection of three planes.

        Parameters

        arrPlane1 : Required, Array, The first plane to intersect
        arrPlane2 : Required, Array, The second plane to intersect
        arrPlane3 : Required, Array, The third plane to intersect

        Returns

        Array : The 3-D point of intersection is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IntersectPlanes', None, arrPlane1, arrPlane2, arrPlane3)

    def line_closest_point(self, arr_line, arr_point):
        """

        Finds the point on an infinite line that is closest to a test point.

        Parameters

        arrLine : Required, Array, Two 3-D points identifying the starting and ending points of the line
        arrPoint : Required, Array, The test point

        Returns

        Array : The point on the line that is closest to the test point is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LineClosestPoint', None, arrLine, arrPoint)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def line_line_intersection(self, arr_line_a, arr_line_b, bln_planar):
        """

        But, two lines in three dimensions generally do not intersect at a point. They may be parallel (no intersections) or they may be coincident (infinite intersections). But, most often only their projection onto a plane intersects. When they do not exactly intersect at a point they can be connected by a line segment, the shortest line segment is unique and is often considered to be their intersection in 3-D.

        Parameters

        arrLineA : Required, Array, Two 3-D points identifying the starting and ending points of the first line
        arrLineB : Required, Array, Two 3-D points identifying the starting and ending points of the second line
        blnPlanar : Optional, Boolean, Assume that the two lines are co-planar

        Returns

        Array : If blnPlanar is omitted or True, then a single 3-D intersection point if successful.
        Array : If blnPlanar is False, then an array containing a point on the first line and a point on the second line if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LineLineIntersection', None, arrLineA, arrLineB, blnPlanar)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def line_plane(self, arr_line):
        """

        Returns a plane that contains the line.  The origin of the plane is at the start of the line.  If possible, a plane parallel to the world XY, YZ or ZX plane is returned.

        Parameters

        arrLine : Required, Array, Two 3-D points identifying the starting and ending points of the line

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LinePlane', None, arrLine)

    def line_plane_intersection(self, arr_line, arr_point):
        """

        Calculates the intersection of a line and a plane.

        Parameters

        arrLine : Required, Array, Two 3-D points identifying the starting and ending points of the line to intersect
        arrPoint : Required, Array, The plane to intersect

        Returns

        Array : The 3-D point of intersection is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LinePlaneIntersection', None, arrLine, arrPoint)

    def line_transform(self, arr_line, arr_xform):
        """

        Transforms a line.

        Parameters

        arrLine : Required, Array, Two 3-D points identifying the starting and ending points of the line
        arrXform : Required, Array, A valid 4x4 transformation matrix

        Returns

        Array : The resulting line if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LineTransform', None, arrLine, arrXform)

    def move_plane(self, arr_plane, arr_origin):
        """

        Moves the origin of a plane.

        Parameters

        arrPlane : Required, Array, The plane
        arrOrigin : Required, Array, A 3-D point identifying the new origin location

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MovePlane', None, arrPlane, arrOrigin)

    def plane_closest_point(self, arr_plane, arr_point, bln_return_point):
        """

        Returns the point on a plane that is closest to a test point.

        Parameters

        arrPlane : Required, Array, The plane
        arrPoint : Required, Array, The 3-D point to test
        blnReturnPoint : Optional, Boolean, If omitted or True, then the point on the plane that is closest to the test point is returned

        Returns

        Array : If blnReturnPoint is omitted or True, then the 3-D point if successful. If blnReturnPoint is False, then an array containing the U,V parameters of the point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlaneClosestPoint', None, arrPlane, arrPoint, blnReturnPoint)

    def plane_equation(self, arr_plane):
        """

        Ax + By + Cz + D = 0

        Parameters

        arrPlane : Required, Array, The plane

        Returns

        Array : An array containing four numbers that represent the coefficients of the equation, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlaneEquation', None, arrPlane)

    def plane_fit_from_points(self, arr_points):
        """

        Returns a plane that was fit through an array of 3-D points.

        Parameters

        arrPoints : Required, Array, An array of 3-D points

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlaneFitFromPoints', None, arrPoints)

    def plane_from_frame(self, arr_origin, arr_xaxis, arr_yaxis):
        """

        Construct a plane from a point, and two vectors in the plane.

        Parameters

        arrOrigin : Required, Array, A 3-D point identifying the origin of the plane
        arrXaxis : Required, Array, A non-zero 3-D vector in the plane that determines the X axis direction
        arrYaxis : Required, Array, A non-zero 3-D vector not parallel to arrXaxis that is used to determine the Y axis direction

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlaneFromFrame', None, arrOrigin, arrXaxis, arrYaxis)

    def plane_from_normal(self, arr_origin, arr_normal):
        """

        Creates a plane from an origin point and a normal direction vector.

        Parameters

        arrOrigin : Required, Array, A 3-D point identifying the origin of the plane
        arrNormal : Required, Array, A non-zero 3-D vector identifying the normal direction of the plane

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlaneFromNormal', None, arrOrigin, arrNormal)

    def plane_from_points(self, arr_origin, arr_point_x, arr_point_y):
        """

        Creates a plane from three non-colinear points.

        Parameters

        arrOrigin : Required, Array, The first point, or origin, of the plane
        arrPointX : Required, Array, A point on the plane's X axis
        arrPointY : Required, Array, A point on the plane's Y axis

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlaneFromPoints', None, arrOrigin, arrPointX, arrPointY)

    def plane_plane_intersection(self, arr_plane1, arr_point2):
        """

        Calculates the intersection of two planes.

        Parameters

        arrPlane1 : Required, Array, The first plane to intersect
        arrPoint2 : Required, Array, The second plane to intersect

        Returns

        Array : Two 3-D points identifying the starting and ending points of the intersection line.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlanePlaneIntersection', None, arrPlane1, arrPoint2)

    def plane_transform(self, arr_plane, arr_xform):
        """

        Transforms a plane.

        Parameters

        arrPlane : Required, Array, The plane to transform
        arrXform : Required, Array, A valid 4x4 transformation matrix

        Returns

        Array : The resulting plane if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PlaneTransform', None, arrPlane, arrXform)

    def rotate_plane(self, arr_plane, dbl_angle, arr_axis):
        """

        Rotates a plane.

        Parameters

        arrPlane : Required, Array, The plane
        dblAngle : Required, Number, The rotation angle in degrees
        arrAxis : Required, Array, A non-zero 3-D vector identifying the axis of rotation

        Returns

        Array : The plane if successful.  The elements of a plane array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RotatePlane', None, arrPlane, dblAngle, arrAxis)

    def world_x_y_plane(self):
        """

        Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(1.0,0.0,0.0), Array(0.0,1.0,0.0)

        No parameters

        Returns

        Array : Rhino's world XY plane.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'WorldXYPlane', None, )

    def world_y_z_plane(self):
        """

        Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,1.0,0.0), Array(0.0,0.0,1.0)

        No parameters

        Returns

        Array : Rhino's world YZ plane.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'WorldYZPlane', None, )

    def world_z_x_plane(self):
        """

        Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,0.0,1.0), Array(1.0,0.0,0.0)

        No parameters

        Returns

        Array : Rhino's world ZX plane.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'WorldZXPlane', None, )

