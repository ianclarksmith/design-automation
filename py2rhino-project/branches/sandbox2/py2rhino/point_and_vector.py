# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class PointAndVector(IRhinoScript):



    def is_vector_parallel_to(self, vector1, vector2):
        """        
        Compares two vectors to see if they are parallel.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The 3-D vector.
            
        vector2, Array of ????, Required        
        The 3-D vector to compare to.
            
        Returns
        =======

        number
        The result of the comparison if successful. The possible results are as follows:

        null
        On error.

        """

        return self._ApplyTypes_(660, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"IsVectorParallelTo", None, flatten(vector1), flatten(vector2))

    def is_vector_perpendicular_to(self, vector1, vector2):
        """        
        Compares two vectors to see if they are perpendicular.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The 3-D vector.
            
        vector2, Array of ????, Required        
        The 3-D vector to compare to.
            
        Returns
        =======

        boolean
        True if the vectors are perpendicular, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(661, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"IsVectorPerpendicularTo", None, flatten(vector1), flatten(vector2))

    def is_vector_tiny(self, vector):
        """        
        Verifies that a vector is very short, or tiny - the x,y,z  elements are less than or equal to 1.0e-12.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector to test.
            
        Returns
        =======

        boolean
        True if the vector is tiny, otherwise False, if successful.

        null
        On error.

        """

        return self._ApplyTypes_(610, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"IsVectorTiny", None, flatten(vector))

    def is_vector_zero(self, vector):
        """        
        Verifies that a vector is zero, or tiny - the  x,y,z elements are equal to 0.0.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector to test.
            
        Returns
        =======

        boolean
        True if the vector is zero, otherwise False, if successful.

        null
        On error.

        """

        return self._ApplyTypes_(611, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"IsVectorZero", None, flatten(vector))

    def point_add(self, point1, point2):
        """        
        Adds a 3-D point or a 3-D vector to a 3-D point.
    
        Parameters
        ==========

        point1, Array of ????, Required        
        The 3-D point to add to.
            
        point2, Array of ????, Required        
        The 3-D point or a 3-D vector to add.
            
        Returns
        =======

        array
        The resulting 3-D point if successful.

        null
        On error.

        """

        return self._ApplyTypes_(666, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"PointAdd", None, flatten(point1), flatten(point2))

    def point_array_bounding_box(self, points, view, world_coords):
        """        
        Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an array of 3-D point locations.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        view, String, Optional        
        The title of the view that contains the construction plane to which the bounding box should be aligned.  If omitted, a world axis-aligned bounding box will be calculated.
            
        world_coords, Boolean, Optional        
        Whether or not to return the bounding box as world coordinates or construction plane coordinates.  The default is to return world coordinates (True).  Note, this option does not apply to world axis-aligned bounding boxes.
            
        Returns
        =======

        array
        An array of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(746, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)), u"PointArrayBoundingBox", None, flatten(points), view, world_coords)

    def point_array_closest_point(self, points, point):
        """        
        Finds the point in an array of 3-D points that is closest to a test point.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points to test.
            
        point, Array of ????, Required        
        The 3-D test point.
            
        Returns
        =======

        number
        The index of the element in the point array that is closest to the test point if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(742, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"PointArrayClosestPoint", None, flatten(points), flatten(point))

    def point_array_transform(self, points, xform):
        """        
        Transforms an array of 3-D points.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points to transform.
            
        xform, Array of ????, Required        
        A valid 4x4 transformation matrix.
            
        Returns
        =======

        array
        The resulting array of 3-D points if successful.

        null
        On error.

        """

        return self._ApplyTypes_(802, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"PointArrayTransform", None, flatten(points), flatten(xform))

    def point_compare(self, point1, point2, tolerance):
        """        
        Compares two 3-D points.
    
        Parameters
        ==========

        point1, Array of ????, Required        
        The first 3-D point to compare.
            
        point2, Array of ????, Required        
        The second 3-D point to compare.
            
        tolerance, Double, Optional        
        The tolerance to use for the comparison. If omitted, Rhino's internal zero tolerance is used.
            
        Returns
        =======

        boolean
        True or False

        null
        On error.

        """

        return self._ApplyTypes_(667, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1)), u"PointCompare", None, flatten(point1), flatten(point2), tolerance)

    def point_divide(self, point, scale):
        """        
        Divides a 3-D point by a value
    
        Parameters
        ==========

        point, Array of ????, Required        
        The 3-D point to divide.
            
        scale, Double, Required        
        The a non-zero value to divide.
            
        Returns
        =======

        array
        The resulting 3-D point if successful.

        null
        On error.

        """

        return self._ApplyTypes_(668, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"PointDivide", None, flatten(point), scale)

    def point_scale(self, point, scale):
        """        
        Scales a 3-D point.
    
        Parameters
        ==========

        point, Array of ????, Required        
        The 3-D point to scale.
            
        scale, Double, Required        
        The scale factor to apply.
            
        Returns
        =======

        array
        The resulting 3-D point if successful.

        null
        On error.

        """

        return self._ApplyTypes_(669, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"PointScale", None, flatten(point), scale)

    def point_subtract(self, point1, point2):
        """        
        Subtracts a 3-D point or a 3-D vector from a 3-D point.
    
        Parameters
        ==========

        point1, Array of ????, Required        
        The 3-D point to subtract from.
            
        point2, Array of ????, Required        
        The 3-D point or a 3-D vector to subtract.
            
        Returns
        =======

        array
        The resulting 3-D point if successful.

        null
        On error.

        """

        return self._ApplyTypes_(670, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"PointSubtract", None, flatten(point1), flatten(point2))

    def point_transform(self, point, xform):
        """        
        Transforms a 3-D point.
    
        Parameters
        ==========

        point, Array of ????, Required        
        The 3-D point to transform.
            
        xform, Array of ????, Required        
        A valid 4x4 transformation matrix.
            
        Returns
        =======

        array
        The resulting 3-D point if successful.

        null
        On error.

        """

        return self._ApplyTypes_(671, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"PointTransform", None, flatten(point), flatten(xform))

    def points_are_coplanar(self, points, tolerance):
        """        
        Verifies that an array of 3-D points are co-planar.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        tolerance, Double, Optional        
        A tolerance to use when verifying. The default is to use Rhino's internal zero tolerance (1.0e-12).
            
        Returns
        =======

        boolean
        True or False indicating either coplanar or not coplanar, respectively, if successful.

        null
        On error.

        """

        return self._ApplyTypes_(593, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"PointsAreCoplanar", None, flatten(points), tolerance)

    def project_point_to_mesh(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def project_point_to_surface(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def pull_points(self, object, points):
        """        
        Pulls an array of points to a surface or mesh object. For more information, see the Rhino help file for information on the Pull command.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the surface or mesh object that pulls.
            
        points, Array of ????, Required        
        An array of 3-D points to pull.
            
        Returns
        =======

        array
        An array of 3-D points if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(716, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"PullPoints", None, object, flatten(points))

    def vector_add(self, vector1, vector2):
        """        
        Adds two 3-D vectors.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The 3-D vector to add to.
            
        vector2, Array of ????, Required        
        The 3-D vector to add.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(612, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorAdd", None, flatten(vector1), flatten(vector2))

    def vector_compare(self, vector1, vector2):
        """        
        Compares two 3-D vectors.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The first 3-D vector to compare.
            
        vector2, Array of ????, Required        
        The second 3-D vector to compare.
            
        Returns
        =======

        null
        On error.

        """

        return self._ApplyTypes_(613, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorCompare", None, flatten(vector1), flatten(vector2))

    def vector_create(self, point1, point2):
        """        
        Creates a vector from two 3-D points.
    
        Parameters
        ==========

        point1, Array of ????, Required        
        The first 3-D point.
            
        point2, Array of ????, Required        
        The second 3-D point.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(614, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorCreate", None, flatten(point1), flatten(point2))

    def vector_cross_product(self, vector1, vector2):
        """        
        Calculates the cross product of two 3-D vectors.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The first 3-D vector.
            
        vector2, Array of ????, Required        
        The second 3-D vector.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(615, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorCrossProduct", None, flatten(vector1), flatten(vector2))

    def vector_divide(self, vector, divide):
        """        
        Divides a 3-D vectors by a value
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector to divide.
            
        divide, Double, Required        
        The a non-zero value to divide.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(625, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"VectorDivide", None, flatten(vector), divide)

    def vector_dot_product(self, vector1, vector2):
        """        
        Calculates the dot product of two 3-D vectors.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The first 3-D vector.
            
        vector2, Array of ????, Required        
        The second 3-D vector.
            
        Returns
        =======

        null
        On error.

        """

        return self._ApplyTypes_(616, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorDotProduct", None, flatten(vector1), flatten(vector2))

    def vector_length(self, vector):
        """        
        Returns the length of a 3-D vector.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector.
            
        Returns
        =======

        null
        On error.

        """

        return self._ApplyTypes_(617, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"VectorLength", None, flatten(vector))

    def vector_multiply(self, vector1, vector2):
        """        
        Multiplies two 3-D vectors.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The first 3-D vector.
            
        vector2, Array of ????, Required        
        The second 3-D vector.
            
        Returns
        =======

        number
        The resulting inner (dot) product if successful.

        null
        On error.

        """

        return self._ApplyTypes_(624, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorMultiply", None, flatten(vector1), flatten(vector2))

    def vector_reverse(self, vector):
        """        
        Reverses the direction of a 3-D vector.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(618, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"VectorReverse", None, flatten(vector))

    def vector_rotate(self, vector, angle, axis):
        """        
        Rotates a 3-D vector.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector.
            
        angle, Double, Required        
        The rotation angle in degrees.
            
        axis, Array of ????, Required        
        A 3-D vector defining the axis of rotation.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(678, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1), (VT_VARIANT, 1)), u"VectorRotate", None, flatten(vector), angle, flatten(axis))

    def vector_scale(self, vector, scale):
        """        
        Scales a 3-D vector.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector to scale.
            
        scale, Double, Required        
        The scale factor to apply.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(619, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"VectorScale", None, flatten(vector), scale)

    def vector_subtract(self, vector1, vector2):
        """        
        Subtracts two 3-D vectors.
    
        Parameters
        ==========

        vector1, Array of ????, Required        
        The 3-D vector to subtract from.
            
        vector2, Array of ????, Required        
        The 3-D vector to subtract.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(620, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorSubtract", None, flatten(vector1), flatten(vector2))

    def vector_transform(self, vector, xform):
        """        
        Transforms a 3-D vector.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector to transform.
            
        xform, Array of ????, Required        
        A valid 4x4 transformation matrix.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(800, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"VectorTransform", None, flatten(vector), flatten(xform))

    def vector_unitize(self, vector):
        """        
        Unitizes, or normalizes, a 3-D vector. Note, zero vectors cannot be unitized.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The 3-D vector to unitize.
            
        Returns
        =======

        array
        The resulting 3-D vector if successful.

        null
        On error.

        """

        return self._ApplyTypes_(621, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"VectorUnitize", None, flatten(vector))
