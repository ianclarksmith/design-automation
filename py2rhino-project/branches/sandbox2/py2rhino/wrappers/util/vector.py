# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino.wrappers import base

def is_parallel_to(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: IsVectorParallelTo
    """
    return base._rsf.is_vector_parallel_to(vector_1, vector_2)

def is_perpendicular_to(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: IsVectorPerpendicularTo
    """
    return base._rsf.is_vector_perpendicular_to(vector_1, vector_2)

def is_tiny(vector):

    """
    For help, look up the Rhinoscript function: IsVectorTiny
    """
    return base._rsf.is_vector_tiny(vector)

def is_zero(vector):

    """
    For help, look up the Rhinoscript function: IsVectorZero
    """
    return base._rsf.is_vector_zero(vector)

def add(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: VectorAdd
    """
    return base._rsf.vector_add(vector_1, vector_2)

def compare(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: VectorCompare
    """
    return base._rsf.vector_compare(vector_1, vector_2)

def create(point_1, point_2):

    """
    For help, look up the Rhinoscript function: VectorCreate
    """
    return base._rsf.vector_create(point_1, point_2)

def cross_product(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: VectorCrossProduct
    """
    return base._rsf.vector_cross_product(vector_1, vector_2)

def divide(vector, divide):

    """
    For help, look up the Rhinoscript function: VectorDivide
    """
    return base._rsf.vector_divide(vector, divide)

def dot_product(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: VectorDotProduct
    """
    return base._rsf.vector_dot_product(vector_1, vector_2)

def length(vector):

    """
    For help, look up the Rhinoscript function: VectorLength
    """
    return base._rsf.vector_length(vector)

def multiply(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: VectorMultiply
    """
    return base._rsf.vector_multiply(vector_1, vector_2)

def reverse(vector):

    """
    For help, look up the Rhinoscript function: VectorReverse
    """
    return base._rsf.vector_reverse(vector)

def rotate(vector, angle, axis):

    """
    For help, look up the Rhinoscript function: VectorRotate
    """
    return base._rsf.vector_rotate(vector, angle, axis)

def scale(vector, scale):

    """
    For help, look up the Rhinoscript function: VectorScale
    """
    return base._rsf.vector_scale(vector, scale)

def subtract(vector_1, vector_2):

    """
    For help, look up the Rhinoscript function: VectorSubtract
    """
    return base._rsf.vector_subtract(vector_1, vector_2)

def transform(vector, xform):

    """
    For help, look up the Rhinoscript function: VectorTransform
    """
    return base._rsf.vector_transform(vector, xform)

def unitize(vector):

    """
    For help, look up the Rhinoscript function: VectorUnitize
    """
    return base._rsf.vector_unitize(vector)
