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

        params = [xform]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(786, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsXformIdentity", None, *params_flattened)

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

        params = [xform]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(787, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsXformSimilarity", None, *params_flattened)

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

        params = [xform]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(785, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsXformZero", None, *params_flattened)

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

        params = [point, plane]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(point), flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(131, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformCPlaneToWorld", None, *params_flattened)

    def xform_change_basis(self, plane1, plane2, x0, y0, z0, x1, y1, z1):
        """        
        Returns a change of basis transformation matrix.
    
        Parameters
        ==========

        plane1, Array of ????, Required        
        The initial plane.
            
        plane2, Array of ????, Required        
        The final plane.
            
        x0, Array of ????, Required        
        The initial basis X (X0,Y0,Z0 can be any 3-D basis)
            
        y0, Array of ????, Required        
        The  initial basis Y
            
        z0, Array of ????, Required        
        The  initial basis Z
            
        x1, Array of ????, Required        
        The final basis X (X1,Y1,Z1 can be any 3-D basis)
            
        y1, Array of ????, Required        
        The  final basis Y
            
        z1, Array of ????, Required        
        The final basis Z
            
        Returns
        =======

        array
        The 4x4 transformation matrix if successful.

        null
        If not successful, or on error.

        """

        params = [plane1, plane2, x0, y0, z0, x1, y1, z1]
        params_opt_or_req = [Required, Required, Required, Required, Required, Required, Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane1), flatten(plane2), flatten(x0), flatten(y0), flatten(z0), flatten(x1), flatten(y1), flatten(z1)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(796, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformChangeBasis", None, *params_flattened)

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

        params = [xform1, xform2]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(xform1), flatten(xform2)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(789, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformCompare", None, *params_flattened)

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

        params = [xform]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(818, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformDeterminant", None, *params_flattened)

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

        params = [value]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [value]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(784, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformDiagonal", None, *params_flattened)

    def xform_identity):
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

        params = []
        params_opt_or_req = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(783, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformIdentity", None, *params_flattened)

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

        params = [xform]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(xform)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(817, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformInverse", None, *params_flattened)

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

        params = [point, normal]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(point), flatten(normal)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(795, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformMirror", None, *params_flattened)

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

        params = [xform1, xform2]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(xform1), flatten(xform2)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(788, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformMultiply", None, *params_flattened)

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

        params = [plane]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(793, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformPlanarProjection", None, *params_flattened)

    def xform_rotation(self, plane1, plane2, angle, axis, start_dir, end_dir, point, x0, y0, z0, x1, y1, z1):
        """        
        Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.
    
        Parameters
        ==========

        plane1, Array of ????, Required        
        The starting plane.
            
        plane2, Array of ????, Required        
        The ending plane.
            
        angle, Double, Required        
        The rotation angle in degrees.
            
        axis, Array of ????, Required        
        The rotation axis.
            
        start_dir, Array of ????, Required        
        The starting direction.
            
        end_dir, Array of ????, Required        
        The ending direction.
            
        point, Array of ????, Required        
        The rotation center point.
            
        x0, Array of ????, Required        
        The initial frame X
            
        y0, Array of ????, Required        
        The initial frame Y.
            
        z0, Array of ????, Required        
        The initial frame Z.
            
        x1, Array of ????, Required        
        The final frame X.
            
        y1, Array of ????, Required        
        The final frame Y.
            
        z1, Array of ????, Required        
        The final frame Z.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [plane1, plane2, angle, axis, start_dir, end_dir, point, x0, y0, z0, x1, y1, z1]
        params_opt_or_req = [Required, Required, Required, Required, Required, Required, Required, Required, Required, Required, Required, Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane1), flatten(plane2), angle, flatten(axis), flatten(start_dir), flatten(end_dir), flatten(point), flatten(x0), flatten(y0), flatten(z0), flatten(x1), flatten(y1), flatten(z1)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformRotation", None, *params_flattened)

    def xform_scale(self, plane, x_scale, y_scale, z_scale, vector, point, scale):
        """        
        Returns a scale transformation matrix.
    
        Parameters
        ==========

        plane, Array of ????, Required        
        The starting plane.
            
        x_scale, Double, Required        
        The scale factor in the x-axis direction.
            
        y_scale, Double, Required        
        The scale factor in the y-axis direction.
            
        z_scale, Double, Required        
        The scale factor in the z-axis direction.
            
        vector, Array of ????, Required        
        The ending direction.
            
        point, Array of ????, Required        
        The rotation center point.
            
        scale, Double, Required        
        The initial frame X
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [plane, x_scale, y_scale, z_scale, vector, point, scale]
        params_opt_or_req = [Required, Required, Required, Required, Required, Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(plane), x_scale, y_scale, z_scale, flatten(vector), flatten(point), scale]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformScale", None, *params_flattened)

    def xform_screen_to_world(self, point, view=None, convert=None):
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

        params = [point, view, convert]
        params_opt_or_req = [Required, Optional, Optional]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(point), view, convert]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(581, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformScreenToWorld", None, *params_flattened)

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

        params = [plane, x1, y1, z1]
        params_opt_or_req = [Required, Required, Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(plane), flatten(x1), flatten(y1), flatten(z1)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(791, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformShear", None, *params_flattened)

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

        params = [vector]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(vector)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(792, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformTranslation", None, *params_flattened)

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

        params = [point, plane]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(point), flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(132, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformWorldToCPlane", None, *params_flattened)

    def xform_world_to_screen(self, point, view=None, convert=None):
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

        params = [point, view, convert]
        params_opt_or_req = [Required, Optional, Optional]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(point), view, convert]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(582, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformWorldToScreen", None, *params_flattened)

    def xform_zero):
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

        params = []
        params_opt_or_req = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(782, 1, (VT_VARIANT, 0), params_magic_numbers, u"XformZero", None, *params_flattened)

