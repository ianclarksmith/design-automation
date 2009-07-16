# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Transformation(DispatchBaseClass):



    def is_xform_identity(self, arr_xform):
        """

        1

        Parameters

        arrXform : Required, Array, A 4x4 transformation matrix

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsXformIdentity', None, arrXform)

    def is_xform_similarity(self, arr_xform):
        """

        Verifies that a matrix is a similarity transformation. A similarity transformation can be broken into a sequence of dialations, translations, rotations, and reflections.

        Parameters

        arrXform : Required, Array, A 4x4 transformation matrix

        Returns

        Boolean : True if this transformation is an orientation preserving similarity, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsXformSimilarity', None, arrXform)

    def is_xform_zero(self, arr_xform):
        """

        0

        Parameters

        arrXform : Required, Array, A 4x4 transformation matrix

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsXformZero', None, arrXform)

    def xform_c_plane_to_world(self, arr_point, arr_plane):
        """

        Transforms a point from construction plane coordinates to world coordinates.

        Parameters

        arrPoint : Required, Array, A 3-D point in construction plane coordinates
        arrPlane : Required, Array, The construction plane

        Returns

        Array : A 3-D point in world coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformCPlaneToWorld', None, arrPoint, arrPlane)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_compare(self, arr_xform1, arr_xform2):
        """

        Compares two transformation matrices.

        Parameters

        arrXform1 : Required, Array, The first 4x4 transformation matrix to compare
        arrXform2 : Required, Array, The second 4x4 transformation matrix to compare

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformCompare', None, arrXform1, arrXform2)

    def xform_determinant(self, arr_xform):
        """

        Returns the determinant of a transformation matrix. If the determinant of a transformation matrix is 0, the matrix is said to be singular. Singular matrices do not have inverses.

        Parameters

        arrXform : Required, Array, A 4x4 transformation matrix

        Returns

        Number : The determinant if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformDeterminant', None, arrXform)

    def xform_diagonal(self, dbl_value):
        """

        1

        Parameters

        dblValue : Required, number, The diagonal value

        Returns

        Array : The 4x4 transformation matrix if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformDiagonal', None, dblValue)

    def xform_identity(self):
        """

        1

        No parameters

        Returns

        Array : The 4x4 transformation matrix.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformIdentity', None, )

    def xform_inverse(self, arr_xform):
        """

        Returns the inverse of a non-singular transformation matrix.

        Parameters

        arrXform : Required, Array, A 4x4 transformation matrix

        Returns

        Array : The inverted 4x4 transformation matrix if successful.
        Null : If matrix is non-singular, On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformInverse', None, arrXform)

    def xform_mirror(self, arr_point, arr_normal):
        """

        Creates a mirror transformation matrix.

        Parameters

        arrPoint : Required, Array, A 3-D point on mirror plane
        arrNormal : Required, Array, A 3-D vector that is normal to mirror plane

        Returns

        Array : The 4x4 transformation matrix is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformMirror', None, arrPoint, arrNormal)

    def xform_multiply(self, arr_xform1, arr_xform2):
        """

        Multiples two transformation matrices, where arrXform = arrXform1 * arrXform2.

        Parameters

        arrXform1 : Required, Array, The first 4x4 transformation matrix to multiply
        arrXform2 : Required, Array, The second 4x4 transformation matrix to multiply

        Returns

        Array : The 4x4 transformation matrix.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformMultiply', None, arrXform1, arrXform2)

    def xform_planar_projection(self, arr_plane):
        """

        Returns a transformation matrix that projects to a plane.

        Parameters

        arrPlane : Required, Array, The plane to project to

        Returns

        Array : The 4x4 transformation matrix.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformPlanarProjection', None, arrPlane)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_screen_to_world(self, arr_point, str_view, bln_convert):
        """

        Transforms either client-area coordinates of a specified view or screen coordinates to world coordinates. The resulting coordinates are represented as a 3-D point.

        Parameters

        arrPoint : Required, Array, A 2-D point in either client-area coordinates of a specified view or screen coordinates
        strView : Optional, String, The title of the view
        blnConvert : Optional, Boolean, If omitted or False, the function assumes arrPoint represents client-area coordinates

        Returns

        Array : A 3-D point in world coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformScreenToWorld', None, arrPoint, strView, blnConvert)

    def xform_shear(self, arr_plane, arr_x1, arr_y1, arr_z1):
        """

        Returns a scale transformation matrix.

        Parameters

        arrPlane : Required, Array (Plane), The plane, where arrPlane(0) is the fixed point
        arrX1 : Required, Array (3-D Vector), The x-axis scale factor
        arrY1 : Required, Array (3-D Vector), The y-axis scale factor
        arrZ1 : Required, Array (3-D Vector), The z-axis scale factor

        Returns

        Array : The 4x4 transformation matrix.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformShear', None, arrPlane, arrX1, arrY1, arrZ1)

    def xform_translation(self, arr_vector):
        """

        Creates a translation transformation matrix.

        Parameters

        arrVector : Required, Array, A 3-D translation vector

        Returns

        Array : The 4x4 transformation matrix is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformTranslation', None, arrVector)

    def xform_world_to_c_plane(self, arr_point, arr_plane):
        """

        Transforms a point from world coordinates to construction plane coordinates.

        Parameters

        arrPoint : Required, Array, A 3-D point in world coordinates
        arrPlane : Required, Array, The construction plane

        Returns

        Array : A 3-D point in construction plane coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformWorldToCPlane', None, arrPoint, arrPlane)

    def xform_world_to_screen(self, arr_point, str_view, bln_convert):
        """

        Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2-D point.

        Parameters

        arrPoint : Required, Array, A 3-D point in world coordinates
        strView : Optional, String, The title of the view
        blnConvert : Optional, Boolean, If omitted or False, the function returns the results as client-area coordinates of the specified view

        Returns

        Array : If blnConvert is omitted or False, a 2-D point in client-area coordinates if successful.
        Array : If blnConvert is True, a 2-D point in screen coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformWorldToScreen', None, arrPoint, strView, blnConvert)

    def xform_zero(self):
        """

        0

        No parameters

        Returns

        Array : The 4x4 transformation matrix.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'XformZero', None, )

