# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class PointAndVector(DispatchBaseClass):



    def is_vector_parallel_to(self, vector1, vector2):
        """

        Compares two vectors to see if they are parallel.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Number : The result of the comparison if successful. The possible results are as follows:
        Null : On error.

        """

        return self._ApplyTypes_(660, 1, (12, 0), ((12, 0), (12, 0)), u'IsVectorParallelTo', None, vector1, vector2)

    def is_vector_perpendicular_to(self, vector1, vector2):
        """

        Compares two vectors to see if they are perpendicular.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Boolean : True if the vectors are perpendicular, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(661, 1, (12, 0), ((12, 0), (12, 0)), u'IsVectorPerpendicularTo', None, vector1, vector2)

    def is_vector_tiny(self, vector):
        """

        Verifies that a vector is very short, or tiny - the x,y,z  elements are less than or equal to 1.0e-12.

        Parameters

        Vector : Required, Array, arr

        Returns

        Boolean : True if the vector is tiny, otherwise False, if successful.
        Null : On error.

        """

        return self._ApplyTypes_(610, 1, (12, 0), ((12, 0)), u'IsVectorTiny', None, vector)

    def is_vector_zero(self, vector):
        """

        Verifies that a vector is zero, or tiny - the  x,y,z elements are equal to 0.0.

        Parameters

        Vector : Required, Array, arr

        Returns

        Boolean : True if the vector is zero, otherwise False, if successful.
        Null : On error.

        """

        return self._ApplyTypes_(611, 1, (12, 0), ((12, 0)), u'IsVectorZero', None, vector)

    def point_add(self, point1, point2):
        """

        Adds a 3-D point or a 3-D vector to a 3-D point.

        Parameters

        Point1 : Required, Array, arr
        Point2 : Required, Array, arr

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(666, 1, (12, 0), ((12, 0), (12, 0)), u'PointAdd', None, point1, point2)

    def point_array_bounding_box(self, points, view, world_coords):
        """

        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an array of 3-D point locations.

        Parameters

        Points : Required, Array, arr
        View : Optional, String, str
        WorldCoords : Optional, Boolean, bln

        Returns

        Array : An array of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(746, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'PointArrayBoundingBox', None, points, view, world_coords)

    def point_array_closest_point(self, points, point):
        """

        Finds the point in an array of 3-D points that is closest to a test point.

        Parameters

        Points : Required, Array, arr
        Point : Required, Array, arr

        Returns

        Number : The index of the element in the point array that is closest to the test point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(742, 1, (12, 0), ((12, 0), (12, 0)), u'PointArrayClosestPoint', None, points, point)

    def point_array_transform(self, points, xform):
        """

        Transforms an array of 3-D points.

        Parameters

        Points : Required, Array, arr
        Xform : Required, Array, arr

        Returns

        Array : The resulting array of 3-D points if successful.
        Null : On error.

        """

        return self._ApplyTypes_(802, 1, (12, 0), ((12, 0), (12, 0)), u'PointArrayTransform', None, points, xform)

    def point_compare(self, point1, point2, tolerance):
        """

        Compares two 3-D points.

        Parameters

        Point1 : Required, Array, arr
        Point2 : Required, Array, arr
        Tolerance : Optional, Number, dbl

        Returns

        Boolean : True or False
        Null : On error.

        """

        return self._ApplyTypes_(667, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'PointCompare', None, point1, point2, tolerance)

    def point_divide(self, point, scale):
        """

        Divides a 3-D point by a value

        Parameters

        Point : Required, Array, arr
        Scale : Required, Number, dbl

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(668, 1, (12, 0), ((12, 0), (12, 0)), u'PointDivide', None, point, scale)

    def point_scale(self, point, scale):
        """

        Scales a 3-D point.

        Parameters

        Point : Required, Array, arr
        Scale : Required, Number, dbl

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(669, 1, (12, 0), ((12, 0), (12, 0)), u'PointScale', None, point, scale)

    def point_subtract(self, point1, point2):
        """

        Subtracts a 3-D point or a 3-D vector from a 3-D point.

        Parameters

        Point1 : Required, Array, arr
        Point2 : Required, Array, arr

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(670, 1, (12, 0), ((12, 0), (12, 0)), u'PointSubtract', None, point1, point2)

    def point_transform(self, point, xform):
        """

        Transforms a 3-D point.

        Parameters

        Point : Required, Array, arr
        Xform : Required, Array, arr

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(671, 1, (12, 0), ((12, 0), (12, 0)), u'PointTransform', None, point, xform)

    def points_are_coplanar(self, points, tolerance):
        """

        Verifies that an array of 3-D points are co-planar.

        Parameters

        Points : Required, Array, arr
        Tolerance : Optional, Number, dbl

        Returns

        Boolean : True or False indicating either coplanar or not coplanar, respectively, if successful.
        Null : On error.

        """

        return self._ApplyTypes_(593, 1, (12, 0), ((12, 0), (12, 0)), u'PointsAreCoplanar', None, points, tolerance)

    def project_point_to_mesh(self, points, points, mesh, meshes, direction):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def project_point_to_surface(self, points, points, surface, surfaces, direction):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def pull_points(self, object, points):
        """

        Pulls an array of points to a surface or mesh object. For more information, see the Rhino help file for information on the Pull command.

        Parameters

        Object : Required, String, str
        Points : Required, String, arr

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(716, 1, (12, 0), ((12, 0), (12, 0)), u'PullPoints', None, object, points)

    def vector_add(self, vector1, vector2):
        """

        Adds two 3-D vectors.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(612, 1, (12, 0), ((12, 0), (12, 0)), u'VectorAdd', None, vector1, vector2)

    def vector_compare(self, vector1, vector2):
        """

        Compares two 3-D vectors.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(613, 1, (12, 0), ((12, 0), (12, 0)), u'VectorCompare', None, vector1, vector2)

    def vector_create(self, point1, point2):
        """

        Creates a vector from two 3-D points.

        Parameters

        Point1 : Required, Array, arr
        Point2 : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(614, 1, (12, 0), ((12, 0), (12, 0)), u'VectorCreate', None, point1, point2)

    def vector_cross_product(self, vector1, vector2):
        """

        Calculates the cross product of two 3-D vectors.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(615, 1, (12, 0), ((12, 0), (12, 0)), u'VectorCrossProduct', None, vector1, vector2)

    def vector_divide(self, vector, divide):
        """

        Divides a 3-D vectors by a value

        Parameters

        Vector : Required, Array, arr
        Divide : Required, Number, dbl

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(625, 1, (12, 0), ((12, 0), (12, 0)), u'VectorDivide', None, vector, divide)

    def vector_dot_product(self, vector1, vector2):
        """

        Calculates the dot product of two 3-D vectors.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(616, 1, (12, 0), ((12, 0), (12, 0)), u'VectorDotProduct', None, vector1, vector2)

    def vector_length(self, vector):
        """

        Returns the length of a 3-D vector.

        Parameters

        Vector : Required, Array, arr

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(617, 1, (12, 0), ((12, 0)), u'VectorLength', None, vector)

    def vector_multiply(self, vector1, vector2):
        """

        Multiplies two 3-D vectors.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Number : The resulting inner (dot) product if successful.
        Null : On error.

        """

        return self._ApplyTypes_(624, 1, (12, 0), ((12, 0), (12, 0)), u'VectorMultiply', None, vector1, vector2)

    def vector_reverse(self, vector):
        """

        Reverses the direction of a 3-D vector.

        Parameters

        Vector : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(618, 1, (12, 0), ((12, 0)), u'VectorReverse', None, vector)

    def vector_rotate(self, vector, angle, axis):
        """

        Rotates a 3-D vector.

        Parameters

        Vector : Required, Array, arr
        Angle : Required, Number, dbl
        Axis : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(678, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'VectorRotate', None, vector, angle, axis)

    def vector_scale(self, vector, scale):
        """

        Scales a 3-D vector.

        Parameters

        Vector : Required, Array, arr
        Scale : Required, Number, dbl

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(619, 1, (12, 0), ((12, 0), (12, 0)), u'VectorScale', None, vector, scale)

    def vector_subtract(self, vector1, vector2):
        """

        Subtracts two 3-D vectors.

        Parameters

        Vector1 : Required, Array, arr
        Vector2 : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(620, 1, (12, 0), ((12, 0), (12, 0)), u'VectorSubtract', None, vector1, vector2)

    def vector_transform(self, vector, xform):
        """

        Transforms a 3-D vector.

        Parameters

        Vector : Required, Array, arr
        Xform : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(800, 1, (12, 0), ((12, 0), (12, 0)), u'VectorTransform', None, vector, xform)

    def vector_unitize(self, vector):
        """

        Unitizes, or normalizes, a 3-D vector. Note, zero vectors cannot be unitized.

        Parameters

        Vector : Required, Array, arr

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(621, 1, (12, 0), ((12, 0)), u'VectorUnitize', None, vector)

