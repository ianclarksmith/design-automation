# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def is_parallel_to(vector_1, vector_2):

    """
    
        Compares two vectors to see if they are parallel.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector.
        vector_2  (List of float, Required) - The 3-D vector to compare to.

        Returns
        =======
        number - The result of the comparison if successful. The possible results are as follows:
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorParallelTo

        
    """
    return _base._rsf.is_vector_parallel_to(vector_1, vector_2)

def is_perpendicular_to(vector_1, vector_2):

    """
    
        Compares two vectors to see if they are perpendicular.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector.
        vector_2  (List of float, Required) - The 3-D vector to compare to.

        Returns
        =======
        boolean - True if the vectors are perpendicular, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorPerpendicularTo

        
    """
    return _base._rsf.is_vector_perpendicular_to(vector_1, vector_2)

def is_tiny(vector):

    """
    
        Verifies that a vector is very short, or tiny - the x,y,z  elements are less than or equal to 1.0e-12.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to test.

        Returns
        =======
        boolean - True if the vector is tiny, otherwise False, if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorTiny

        
    """
    return _base._rsf.is_vector_tiny(vector)

def is_zero(vector):

    """
    
        Verifies that a vector is zero, or tiny - the  x,y,z elements are equal to 0.0.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to test.

        Returns
        =======
        boolean - True if the vector is zero, otherwise False, if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsVectorZero

        
    """
    return _base._rsf.is_vector_zero(vector)

def add(vector_1, vector_2):

    """
    
        Adds two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector to add to.
        vector_2  (List of float, Required) - The 3-D vector to add.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorAdd

        
    """
    return _base._rsf.vector_add(vector_1, vector_2)

def compare(vector_1, vector_2):

    """
    
        Compares two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector to compare.
        vector_2  (List of float, Required) - The second 3-D vector to compare.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorCompare

        
    """
    return _base._rsf.vector_compare(vector_1, vector_2)

def create(point_1, point_2):

    """
    
        Creates a vector from two 3-D points.

        Parameters
        ==========
        point_1  (List of float, Required) - The first 3-D point.
        point_2  (List of float, Required) - The second 3-D point.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorCreate

        
    """
    return _base._rsf.vector_create(point_1, point_2)

def cross_product(vector_1, vector_2):

    """
    
        Calculates the cross product of two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector.
        vector_2  (List of float, Required) - The second 3-D vector.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorCrossProduct

        
    """
    return _base._rsf.vector_cross_product(vector_1, vector_2)

def divide(vector, divide):

    """
    
        Divides a 3-D vectors by a value

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to divide.
        divide  (float, Required) - The a non-zero value to divide.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorDivide

        
    """
    return _base._rsf.vector_divide(vector, divide)

def dot_product(vector_1, vector_2):

    """
    
        Calculates the dot product of two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector.
        vector_2  (List of float, Required) - The second 3-D vector.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorDotProduct

        
    """
    return _base._rsf.vector_dot_product(vector_1, vector_2)

def length(vector):

    """
    
        Returns the length of a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector.

        Returns
        =======
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorLength

        
    """
    return _base._rsf.vector_length(vector)

def multiply(vector_1, vector_2):

    """
    
        Multiplies two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The first 3-D vector.
        vector_2  (List of float, Required) - The second 3-D vector.

        Returns
        =======
        number - The resulting inner (dot) product if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorMultiply

        
    """
    return _base._rsf.vector_multiply(vector_1, vector_2)

def reverse(vector):

    """
    
        Reverses the direction of a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorReverse

        
    """
    return _base._rsf.vector_reverse(vector)

def rotate(vector, angle, axis):

    """
    
        Rotates a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector.
        angle  (float, Required) - The rotation angle in degrees.
        axis  (List of float, Required) - A 3-D vector defining the axis of rotation.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorRotate

        
    """
    return _base._rsf.vector_rotate(vector, angle, axis)

def scale(vector, scale):

    """
    
        Scales a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to scale.
        scale  (float, Required) - The scale factor to apply.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorScale

        
    """
    return _base._rsf.vector_scale(vector, scale)

def subtract(vector_1, vector_2):

    """
    
        Subtracts two 3-D vectors.

        Parameters
        ==========
        vector_1  (List of float, Required) - The 3-D vector to subtract from.
        vector_2  (List of float, Required) - The 3-D vector to subtract.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorSubtract

        
    """
    return _base._rsf.vector_subtract(vector_1, vector_2)

def transform(vector, xform):

    """
    
        Transforms a 3-D vector.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to transform.
        xform  (List of float, Required) - A valid 4x4 transformation matrix.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorTransform

        
    """
    return _base._rsf.vector_transform(vector, xform)

def unitize(vector):

    """
    
        Unitizes, or normalizes, a 3-D vector. Note, zero vectors cannot be unitized.

        Parameters
        ==========
        vector  (List of float, Required) - The 3-D vector to unitize.

        Returns
        =======
        list - The resulting 3-D vector if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: VectorUnitize

        
    """
    return _base._rsf.vector_unitize(vector)
