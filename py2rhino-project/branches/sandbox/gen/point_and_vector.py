# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class PointAndVector(DispatchBaseClass):



    def is_vector_parallel_to(self, arr_vector1, arr_vector2):
        """

        Compares two vectors to see if they are parallel.

        Parameters

        arrVector1 : Required, Array, The 3-D vector
        arrVector2 : Required, Array, The 3-D vector to compare to

        Returns

        Number : The result of the comparison if successful. The possible results are as follows:
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsVectorParallelTo', None, arrVector1, arrVector2)

    def is_vector_perpendicular_to(self, arr_vector1, arr_vector2):
        """

        Compares two vectors to see if they are perpendicular.

        Parameters

        arrVector1 : Required, Array, The 3-D vector
        arrVector2 : Required, Array, The 3-D vector to compare to

        Returns

        Boolean : True if the vectors are perpendicular, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsVectorPerpendicularTo', None, arrVector1, arrVector2)

    def is_vector_tiny(self, arr_vector):
        """

        Verifies that a vector is very short, or tiny - the x,y,z  elements are less than or equal to 1.0e-12.

        Parameters

        arrVector : Required, Array, The 3-D vector to test

        Returns

        Boolean : True if the vector is tiny, otherwise False, if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsVectorTiny', None, arrVector)

    def is_vector_zero(self, arr_vector):
        """

        Verifies that a vector is zero, or tiny - the  x,y,z elements are equal to 0.0.

        Parameters

        arrVector : Required, Array, The 3-D vector to test

        Returns

        Boolean : True if the vector is zero, otherwise False, if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsVectorZero', None, arrVector)

    def point_add(self, arr_point1, arr_point2):
        """

        Adds a 3-D point or a 3-D vector to a 3-D point.

        Parameters

        arrPoint1 : Required, Array, The 3-D point to add to
        arrPoint2 : Required, Array, The 3-D point or a 3-D vector to add

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointAdd', None, arrPoint1, arrPoint2)

    def point_array_bounding_box(self, arr_points, str_view, bln_world_coords):
        """

        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an array of 3-D point locations.

        Parameters

        arrPoints : Required, Array, An array of 3-D points
        strView : Optional, String, The title of the view that contains the construction plane to which the bounding box should be aligned
        blnWorldCoords : Optional, Boolean, Whether or not to return the bounding box as world coordinates or construction plane coordinates

        Returns

        Array : An array of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointArrayBoundingBox', None, arrPoints, strView, blnWorldCoords)

    def point_array_closest_point(self, arr_points, arr_point):
        """

        Finds the point in an array of 3-D points that is closest to a test point.

        Parameters

        arrPoints : Required, Array, An array of 3-D points to test
        arrPoint : Required, Array, The 3-D test point

        Returns

        Number : The index of the element in the point array that is closest to the test point if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointArrayClosestPoint', None, arrPoints, arrPoint)

    def point_array_transform(self, arr_points, arr_xform):
        """

        Transforms an array of 3-D points.

        Parameters

        arrPoints : Required, Array, An array of 3-D points to transform
        arrXform : Required, Array, A valid 4x4 transformation matrix

        Returns

        Array : The resulting array of 3-D points if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointArrayTransform', None, arrPoints, arrXform)

    def point_compare(self, arr_point1, arr_point2, dbl_tolerance):
        """

        Compares two 3-D points.

        Parameters

        arrPoint1 : Required, Array, The first 3-D point to compare
        arrPoint2 : Required, Array, The second 3-D point to compare
        dblTolerance : Optional, Number, The tolerance to use for the comparison

        Returns

        Boolean : True or False
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointCompare', None, arrPoint1, arrPoint2, dblTolerance)

    def point_divide(self, arr_point, dbl_scale):
        """

        Divides a 3-D point by a value

        Parameters

        arrPoint : Required, Array, The 3-D point to divide
        dblScale : Required, Number, The a non-zero value to divide

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointDivide', None, arrPoint, dblScale)

    def point_scale(self, arr_point, dbl_scale):
        """

        Scales a 3-D point.

        Parameters

        arrPoint : Required, Array, The 3-D point to scale
        dblScale : Required, Number, The scale factor to apply

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointScale', None, arrPoint, dblScale)

    def point_subtract(self, arr_point1, arr_point2):
        """

        Subtracts a 3-D point or a 3-D vector from a 3-D point.

        Parameters

        arrPoint1 : Required, Array, The 3-D point to subtract from
        arrPoint2 : Required, Array, The 3-D point or a 3-D vector to subtract

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointSubtract', None, arrPoint1, arrPoint2)

    def point_transform(self, arr_point, arr_xform):
        """

        Transforms a 3-D point.

        Parameters

        arrPoint : Required, Array, The 3-D point to transform
        arrXform : Required, Array, A valid 4x4 transformation matrix

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointTransform', None, arrPoint, arrXform)

    def points_are_coplanar(self, arr_points, dbl_tolerance):
        """

        Verifies that an array of 3-D points are co-planar.

        Parameters

        arrPoints : Required, Array, An array of 3-D points
        dblTolerance : Optional, Number, A tolerance to use when verifying

        Returns

        Boolean : True or False indicating either coplanar or not coplanar, respectively, if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PointsAreCoplanar', None, arrPoints, dblTolerance)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def pull_points(self, str_object, arr_points):
        """

        Pulls an array of points to a surface or mesh object. For more information, see the Rhino help file for information on the Pull command.

        Parameters

        strObject : Required, String, The identifier of the surface or mesh object that pulls
        arrPoints : Required, String, An array of 3-D points to pull

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PullPoints', None, strObject, arrPoints)

    def vector_add(self, arr_vector1, arr_vector2):
        """

        Adds two 3-D vectors.

        Parameters

        arrVector1 : Required, Array, The 3-D vector to add to
        arrVector2 : Required, Array, The 3-D vector to add

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorAdd', None, arrVector1, arrVector2)

    def vector_compare(self, arr_vector1, arr_vector2):
        """

        Compares two 3-D vectors.

        Parameters

        arrVector1 : Required, Array, The first 3-D vector to compare
        arrVector2 : Required, Array, The second 3-D vector to compare

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorCompare', None, arrVector1, arrVector2)

    def vector_create(self, arr_point1, arr_point2):
        """

        Creates a vector from two 3-D points.

        Parameters

        arrPoint1 : Required, Array, The first 3-D point
        arrPoint2 : Required, Array, The second 3-D point

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorCreate', None, arrPoint1, arrPoint2)

    def vector_cross_product(self, arr_vector1, arr_vector2):
        """

        Calculates the cross product of two 3-D vectors.

        Parameters

        arrVector1 : Required, Array, The first 3-D vector
        arrVector2 : Required, Array, The second 3-D vector

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorCrossProduct', None, arrVector1, arrVector2)

    def vector_divide(self, arr_vector, dbl_divide):
        """

        Divides a 3-D vectors by a value

        Parameters

        arrVector : Required, Array, The 3-D vector to divide
        dblDivide : Required, Number, The a non-zero value to divide

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorDivide', None, arrVector, dblDivide)

    def vector_dot_product(self, arr_vector1, arr_vector2):
        """

        Calculates the dot product of two 3-D vectors.

        Parameters

        arrVector1 : Required, Array, The first 3-D vector
        arrVector2 : Required, Array, The second 3-D vector

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorDotProduct', None, arrVector1, arrVector2)

    def vector_length(self, arr_vector):
        """

        Returns the length of a 3-D vector.

        Parameters

        arrVector : Required, Array, The 3-D vector

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorLength', None, arrVector)

    def vector_multiply(self, arr_vector1, arr_vector2):
        """

        Multiplies two 3-D vectors.

        Parameters

        arrVector1 : Required, Array, The first 3-D vector
        arrVector2 : Required, Array, The second 3-D vector

        Returns

        Number : The resulting inner (dot) product if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorMultiply', None, arrVector1, arrVector2)

    def vector_reverse(self, arr_vector):
        """

        Reverses the direction of a 3-D vector.

        Parameters

        arrVector : Required, Array, The 3-D vector

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorReverse', None, arrVector)

    def vector_rotate(self, arr_vector, dbl_angle, arr_axis):
        """

        Rotates a 3-D vector.

        Parameters

        arrVector : Required, Array, The 3-D vector
        dblAngle : Required, Number, The rotation angle in degrees
        arrAxis : Required, Array, A 3-D vector defining the axis of rotation

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorRotate', None, arrVector, dblAngle, arrAxis)

    def vector_scale(self, arr_vector, dbl_scale):
        """

        Scales a 3-D vector.

        Parameters

        arrVector : Required, Array, The 3-D vector to scale
        dblScale : Required, Number, The scale factor to apply

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorScale', None, arrVector, dblScale)

    def vector_subtract(self, arr_vector1, arr_vector2):
        """

        Subtracts two 3-D vectors.

        Parameters

        arrVector1 : Required, Array, The 3-D vector to subtract from
        arrVector2 : Required, Array, The 3-D vector to subtract

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorSubtract', None, arrVector1, arrVector2)

    def vector_transform(self, arr_vector, arr_xform):
        """

        Transforms a 3-D vector.

        Parameters

        arrVector : Required, Array, The 3-D vector to transform
        arrXform : Required, Array, A valid 4x4 transformation matrix

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorTransform', None, arrVector, arrXform)

    def vector_unitize(self, arr_vector):
        """

        Unitizes, or normalizes, a 3-D vector. Note, zero vectors cannot be unitized.

        Parameters

        arrVector : Required, Array, The 3-D vector to unitize

        Returns

        Array : The resulting 3-D vector if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'VectorUnitize', None, arrVector)

