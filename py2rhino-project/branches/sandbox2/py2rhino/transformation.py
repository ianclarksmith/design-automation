# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Transformation(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

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

        xform, Array of Doubles, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        params = [xform]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(xform)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(786, 1, (VT_VARIANT, 0), magic, u"IsXformIdentity", None, *flattened)

    def is_xform_similarity(self, xform):
        """        
        Verifies that a matrix is a similarity transformation. A similarity transformation can be broken into a sequence of dialations, translations, rotations, and reflections.
    
        Parameters
        ==========

        xform, Array of Doubles, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        boolean
        True if this transformation is an orientation preserving similarity, otherwise False.

        null
        On error.

        """

        params = [xform]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(xform)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(787, 1, (VT_VARIANT, 0), magic, u"IsXformSimilarity", None, *flattened)

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

        xform, Array of Doubles, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        params = [xform]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(xform)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(785, 1, (VT_VARIANT, 0), magic, u"IsXformZero", None, *flattened)

    def xform_c_plane_to_world(self, point, plane):
        """        
        Transforms a point from construction plane coordinates to world coordinates.
    
        Parameters
        ==========

        point, Array of Doubles, Required        
        A 3-D point in construction plane coordinates.
            
        plane, Array of Doubles, Required        
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
        required = [True, True]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(point), flatten_params(plane)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(131, 1, (VT_VARIANT, 0), magic, u"XformCPlaneToWorld", None, *flattened)

    def xform_change_basis(self, plane1, plane2):
        """        
        Returns a change of basis transformation matrix.
    
        Parameters
        ==========

        plane1, Array of ????, Required        
        The initial plane.
            
        plane2, Array of ????, Required        
        The final plane.
            
        Returns
        =======

        array
        The 4x4 transformation matrix if successful.

        null
        If not successful, or on error.

        """

        params = [plane1, plane2]
        required = [True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(plane1), flatten_params(plane2)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(796, 1, (VT_VARIANT, 0), magic, u"XformChangeBasis", None, *flattened)

    def xform_change_basis_2(self, x0, y0, z0, x1, y1, z1):
        """        
        Returns a change of basis transformation matrix.
    
        Parameters
        ==========

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

        params = [x0, y0, z0, x1, y1, z1]
        required = [True, True, True, True, True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(x0), flatten_params(y0), flatten_params(z0), flatten_params(x1), flatten_params(y1), flatten_params(z1)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(796, 1, (VT_VARIANT, 0), magic, u"XformChangeBasis", None, *flattened)

    def xform_compare(self, xform1, xform2):
        """        
        Compares two transformation matrices.
    
        Parameters
        ==========

        xform1, Array of Doubles, Required        
        The first 4x4 transformation matrix to compare.
            
        xform2, Array of Doubles, Required        
        The second 4x4 transformation matrix to compare.
            
        Returns
        =======

        null
        On error.

        """

        params = [xform1, xform2]
        required = [True, True]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(xform1), flatten_params(xform2)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(789, 1, (VT_VARIANT, 0), magic, u"XformCompare", None, *flattened)

    def xform_determinant(self, xform):
        """        
        Returns the determinant of a transformation matrix. If the determinant of a transformation matrix is 0, the matrix is said to be singular. Singular matrices do not have inverses.
    
        Parameters
        ==========

        xform, Array of Doubles, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        number
        The determinant if successful.

        null
        On error.

        """

        params = [xform]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(xform)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(818, 1, (VT_VARIANT, 0), magic, u"XformDeterminant", None, *flattened)

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
        required = [True]
        magic = [(VT_R8, 1),]
        flattened = [value]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(784, 1, (VT_VARIANT, 0), magic, u"XformDiagonal", None, *flattened)

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

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(783, 1, (VT_VARIANT, 0), magic, u"XformIdentity", None, *flattened)

    def xform_inverse(self, xform):
        """        
        Returns the inverse of a non-singular transformation matrix.
    
        Parameters
        ==========

        xform, Array of Doubles, Required        
        A 4x4 transformation matrix.
            
        Returns
        =======

        array
        The inverted 4x4 transformation matrix if successful.

        null
        If matrix is non-singular, On error.

        """

        params = [xform]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(xform)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(817, 1, (VT_VARIANT, 0), magic, u"XformInverse", None, *flattened)

    def xform_mirror(self, point, normal):
        """        
        Creates a mirror transformation matrix.
    
        Parameters
        ==========

        point, Array of Doubles, Required        
        A 3-D point on mirror plane.
            
        normal, Array of Doubles, Required        
        A 3-D vector that is normal to mirror plane.
            
        Returns
        =======

        array
        The 4x4 transformation matrix is successful.

        null
        If not successful, or on error.

        """

        params = [point, normal]
        required = [True, True]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(point), flatten_params(normal)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(795, 1, (VT_VARIANT, 0), magic, u"XformMirror", None, *flattened)

    def xform_multiply(self, xform1, xform2):
        """        
        Multiples two transformation matrices, where arrXform = arrXform1 * arrXform2.
    
        Parameters
        ==========

        xform1, Array of Doubles, Required        
        The first 4x4 transformation matrix to multiply.
            
        xform2, Array of Doubles, Required        
        The second 4x4 transformation matrix to multiply.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [xform1, xform2]
        required = [True, True]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(xform1), flatten_params(xform2)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(788, 1, (VT_VARIANT, 0), magic, u"XformMultiply", None, *flattened)

    def xform_planar_projection(self, plane):
        """        
        Returns a transformation matrix that projects to a plane.
    
        Parameters
        ==========

        plane, Array of Doubles, Required        
        The plane to project to.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [plane]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(plane)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(793, 1, (VT_VARIANT, 0), magic, u"XformPlanarProjection", None, *flattened)

    def xform_rotation(self, plane1, plane2):
        """        
        Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.
    
        Parameters
        ==========

        plane1, Array of ????, Required        
        The starting plane.
            
        plane2, Array of ????, Required        
        The ending plane.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [plane1, plane2]
        required = [True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(plane1), flatten_params(plane2)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_rotation_2(self, angle, axis, point):
        """        
        Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.
    
        Parameters
        ==========

        angle, Double, Required        
        The rotation angle in degrees.
            
        axis, Array of ????, Required        
        The rotation axis.
            
        point, Array of ????, Required        
        The rotation center point.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [angle, axis, point]
        required = [True, True, True]
        magic = [(VT_R8, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [angle, flatten_params(axis), flatten_params(point)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_rotation_3(self, start_dir, end_dir, point):
        """        
        Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.
    
        Parameters
        ==========

        start_dir, Array of ????, Required        
        The starting direction.
            
        end_dir, Array of ????, Required        
        The ending direction.
            
        point, Array of ????, Required        
        The rotation center point.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [start_dir, end_dir, point]
        required = [True, True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(start_dir), flatten_params(end_dir), flatten_params(point)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_rotation_4(self, x0, y0, z0, x1, y1, z1):
        """        
        Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.
    
        Parameters
        ==========

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

        params = [x0, y0, z0, x1, y1, z1]
        required = [True, True, True, True, True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(x0), flatten_params(y0), flatten_params(z0), flatten_params(x1), flatten_params(y1), flatten_params(z1)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(794, 1, (VT_VARIANT, 0), magic, u"XformRotation", None, *flattened)

    def xform_scale(self, plane, x_scale, y_scale, z_scale):
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
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [plane, x_scale, y_scale, z_scale]
        required = [True, True, True, True]
        magic = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_R8, 1)]
        flattened = [flatten_params(plane), x_scale, y_scale, z_scale]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_scale_2(self, x_scale, y_scale, z_scale):
        """        
        Returns a scale transformation matrix.
    
        Parameters
        ==========

        x_scale, Double, Required        
        The scale factor in the x-axis direction.
            
        y_scale, Double, Required        
        The scale factor in the y-axis direction.
            
        z_scale, Double, Required        
        The scale factor in the z-axis direction.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [x_scale, y_scale, z_scale]
        required = [True, True, True]
        magic = [(VT_R8, 1), (VT_R8, 1), (VT_R8, 1)]
        flattened = [x_scale, y_scale, z_scale]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_scale_3(self, vector):
        """        
        Returns a scale transformation matrix.
    
        Parameters
        ==========

        vector, Array of ????, Required        
        The ending direction.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [vector]
        required = [True]
        magic = [(VT_VARIANT, 1),]
        flattened = [flatten_params(vector)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_scale_4(self, point, scale):
        """        
        Returns a scale transformation matrix.
    
        Parameters
        ==========

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

        params = [point, scale]
        required = [True, True]
        magic = [(VT_VARIANT, 1), (VT_R8, 1)]
        flattened = [flatten_params(point), scale]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(790, 1, (VT_VARIANT, 0), magic, u"XformScale", None, *flattened)

    def xform_screen_to_world(self, point, view=None, convert=None):
        """        
        Transforms either client-area coordinates of a specified view or screen coordinates to world coordinates. The resulting coordinates are represented as a 3-D point.
    
        Parameters
        ==========

        point, Array of Doubles, Required        
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
        required = [True, False, False]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(point), view, convert]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(581, 1, (VT_VARIANT, 0), magic, u"XformScreenToWorld", None, *flattened)

    def xform_shear(self, plane, x1, y1, z1):
        """        
        Returns a scale transformation matrix.
    
        Parameters
        ==========

        plane, Array of Doubles, Required        
        The plane, where arrPlane(0) is the fixed point.
            
        x1, Array of Doubles, Required        
        The x-axis scale factor.
            
        y1, Array of Doubles, Required        
        The y-axis scale factor.
            
        z1, Array of Doubles, Required        
        The z-axis scale factor.
            
        Returns
        =======

        array
        The 4x4 transformation matrix.

        null
        On error.

        """

        params = [plane, x1, y1, z1]
        required = [True, True, True, True]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(plane), flatten_params(x1), flatten_params(y1), flatten_params(z1)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(791, 1, (VT_VARIANT, 0), magic, u"XformShear", None, *flattened)

    def xform_translation(self, vector):
        """        
        Creates a translation transformation matrix.
    
        Parameters
        ==========

        vector, Array of Doubles, Required        
        A 3-D translation vector.
            
        Returns
        =======

        array
        The 4x4 transformation matrix is successful.

        null
        If not successful, or on error.

        """

        params = [vector]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(vector)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(792, 1, (VT_VARIANT, 0), magic, u"XformTranslation", None, *flattened)

    def xform_world_to_c_plane(self, point, plane):
        """        
        Transforms a point from world coordinates to construction plane coordinates.
    
        Parameters
        ==========

        point, Array of Doubles, Required        
        A 3-D point in world coordinates.
            
        plane, Array of Doubles, Required        
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
        required = [True, True]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(point), flatten_params(plane)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(132, 1, (VT_VARIANT, 0), magic, u"XformWorldToCPlane", None, *flattened)

    def xform_world_to_screen(self, point, view=None, convert=None):
        """        
        Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2-D point.
    
        Parameters
        ==========

        point, Array of Doubles, Required        
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
        required = [True, False, False]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(point), view, convert]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(582, 1, (VT_VARIANT, 0), magic, u"XformWorldToScreen", None, *flattened)

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

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(782, 1, (VT_VARIANT, 0), magic, u"XformZero", None, *flattened)

