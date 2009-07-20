# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Transformation(IRhinoScript):



    def is_xform_identity(self, xform):
        """        
        Verifies that a matrix is the identity transformation.
		1
		0
		0
		0
		0
		1
		0
		0
		0
		0
		1
		0
		0
		0
		0
		1
    
        Parameters
        ==========

        xform, Array of ????, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(786, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"IsXformIdentity", None, flatten(xform))

    def is_xform_similarity(self, xform):
        """        
        Verifies that a matrix is a similarity transformation. A similarity transformation can be broken into a sequence of dialations, translations, rotations, and reflections.
    
        Parameters
        ==========

        xform, Array of ????, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        boolean
        True if this transformation is an orientation preserving similarity, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(787, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"IsXformSimilarity", None, flatten(xform))

    def is_xform_zero(self, xform):
        """        
        Verifies that a matrix is the zero transformation.
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
    
        Parameters
        ==========

        xform, Array of ????, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(785, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"IsXformZero", None, flatten(xform))

    def xform_c_plane_to_world(self, point, plane):
        """        
        Transforms a point from construction plane coordinates to world coordinates.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 3-D point in construction plane coordinates.
            
        plane, Array of ????, Required        
        The construction plane.  The elements of a plane array are as follows:
		Elemenet
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3
            
        Returns
        =======

        array
        A 3-D point in world coordinates if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(131, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"XformCPlaneToWorld", None, flatten(point), flatten(plane))

    def xform_change_basis(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_compare(self, xform1, xform2):
        """        
        Compares two transformation matrices.
    
        Parameters
        ==========

        xform1, Array of ????, Required        
        The first 4x4 transformation matrix to compare.
            
        xform2, Array of ????, Required        
        The second 4x4 transformation matrix to compare.
            
        Returns
        =======

        null
        On error.

        """

        return self._ApplyTypes_(789, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"XformCompare", None, flatten(xform1), flatten(xform2))

    def xform_determinant(self, xform):
        """        
        Returns the determinant of a transformation matrix. If the determinant of a transformation matrix is 0, the matrix is said to be singular. Singular matrices do not have inverses.
    
        Parameters
        ==========

        xform, Array of ????, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        number
        The determinant if successful.

        null
        On error.

        """

        return self._ApplyTypes_(818, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"XformDeterminant", None, flatten(xform))

    def xform_diagonal(self, value):
        """        
        Returns a diagonal  transformation matrix. Diagonal matrices are 3x3 with the bottom row = 0,0,0,1.
		d
		0
		0
		0
		0
		d
		0
		0
		0
		0
		d
		0
		0
		0
		0
		1
    
        Parameters
        ==========

        value, Double, Required        
        The diagonal value.
            
        Returns
        =======

        array
        The 4x4 transformation matrix if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(784, 1, (VT_VARIANT, 0), ((VT_R8, 1),), u"XformDiagonal", None, value)

    def xform_identity(self):
        """        
        Returns the identity transformation matrix.
		1
		0
		0
		0
		0
		1
		0
		0
		0
		0
		1
		0
		0
		0
		0
		1
    
        No parameters

        Returns
        =======

        array
        The 4x4 transformation matrix.

        """

        return self._ApplyTypes_(783, 1, (VT_VARIANT, 0), (), u"XformIdentity", None, )

    def xform_inverse(self, xform):
        """        
        Returns the inverse of a non-singular transformation matrix.
    
        Parameters
        ==========

        xform, Array of ????, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        array
        The inverted 4x4 transformation matrix if successful.

        null
        If matrix is non-singular, On error.

        """

        return self._ApplyTypes_(817, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"XformInverse", None, flatten(xform))

    def xform_mirror(self, point, normal):
        """        
        Creates a mirror transformation matrix.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 3-D point on mirror plane.
            
        normal, Array of ????, Required        
        A 3-D vector that is normal to mirror plane.
            
        Returns
        =======

        array
        The 4x4 transformation matrix is successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(795, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"XformMirror", None, flatten(point), flatten(normal))

    def xform_multiply(self, xform1, xform2):
        """        
        Multiples two transformation matrices, where arrXform = arrXform1 * arrXform2.
    
        Parameters
        ==========

        xform1, Array of ????, Required        
        The first 4x4 transformation matrix to multiply.
            
        xform2, Array of ????, Required        
        The second 4x4 transformation matrix to multiply.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        return self._ApplyTypes_(788, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"XformMultiply", None, flatten(xform1), flatten(xform2))

    def xform_planar_projection(self, plane):
        """        
        Returns a transformation matrix that projects to a plane.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane to project to.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        return self._ApplyTypes_(793, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"XformPlanarProjection", None, flatten(plane))

    def xform_rotation(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_scale(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_screen_to_world(self, point, view, convert):
        """        
        Transforms either client-area coordinates of a specified view or screen coordinates to world coordinates. The resulting coordinates are represented as a 3-D point.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 2-D point in either client-area coordinates of a specified view or screen coordinates.
            
        view, String, Optional        
        The title of the view.  If omitted, the active view is used.
            
        convert, Boolean, Optional        
        If omitted or False, the function assumes arrPoint represents client-area coordinates. If True, then the function assumes arrPoint represents screen coordinates.
            
        Returns
        =======

        array
        A 3-D point in world coordinates if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(581, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)), u"XformScreenToWorld", None, flatten(point), view, convert)

    def xform_shear(self, plane, x1, y1, z1):
        """        
        Returns a scale transformation matrix.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The plane, where arrPlane(0) is the fixed point.
            
        x1, Array of ????, Required        
        The x-axis scale factor.
            
        y1, Array of ????, Required        
        The y-axis scale factor.
            
        z1, Array of ????, Required        
        The z-axis scale factor.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        return self._ApplyTypes_(791, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"XformShear", None, flatten(plane), flatten(x1), flatten(y1), flatten(z1))

    def xform_translation(self, vector):
        """        
        Creates a translation transformation matrix.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        A 3-D translation vector.
            
        Returns
        =======

        array
        The 4x4 transformation matrix is successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(792, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"XformTranslation", None, flatten(vector))

    def xform_world_to_c_plane(self, point, plane):
        """        
        Transforms a point from world coordinates to construction plane coordinates.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 3-D point in world coordinates.
            
        plane, Array of ????, Required        
        The construction plane.  The elements of a plane array are as follows:
		Element
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3
            
        Returns
        =======

        array
        A 3-D point in construction plane coordinates if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(132, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"XformWorldToCPlane", None, flatten(point), flatten(plane))

    def xform_world_to_screen(self, point, view, convert):
        """        
        Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2-D point.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 3-D point in world coordinates.
            
        view, String, Optional        
        The title of the view.  If omitted, the active view is used.
            
        convert, Boolean, Optional        
        If omitted or False, the function returns the results as client-area coordinates of the specified view. If True, then the results are returned as screen coordinates.
            
        Returns
        =======

        array
        If blnConvert is omitted or False, a 2-D point in client-area coordinates if successful.

        array
        If blnConvert is True, a 2-D point in screen coordinates if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(582, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)), u"XformWorldToScreen", None, flatten(point), view, convert)

    def xform_zero(self):
        """        
        Returns a zero transformation matrix.
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
		0
    
        No parameters

        Returns
        =======

        array
        The 4x4 transformation matrix.

        """

        return self._ApplyTypes_(782, 1, (VT_VARIANT, 0), (), u"XformZero", None, )

