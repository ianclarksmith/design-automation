# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Transformation(IRhinoScript):



    def is_xform_identity(self, xform):
        """

        1

        Parameters

        Xform : Required, Array, arrdbl, Array of ?

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(786, 1, (12, 0), ((8197, 0),), u'IsXformIdentity', None, _utils.flatten(xform))

    def is_xform_similarity(self, xform):
        """

        Verifies that a matrix is a similarity transformation. A similarity transformation can be broken into a sequence of dialations, translations, rotations, and reflections.

        Parameters

        Xform : Required, Array, arrdbl, Array of ?

        Returns

        Boolean : True if this transformation is an orientation preserving similarity, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(787, 1, (12, 0), ((8197, 0),), u'IsXformSimilarity', None, _utils.flatten(xform))

    def is_xform_zero(self, xform):
        """

        0

        Parameters

        Xform : Required, Array, arrdbl, Array of ?

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(785, 1, (12, 0), ((8197, 0),), u'IsXformZero', None, _utils.flatten(xform))

    def xform_c_plane_to_world(self, point, plane):
        """

        Transforms a point from construction plane coordinates to world coordinates.

        Parameters

        Point : Required, Array, arrdbl, Array of ?
        Plane : Required, Array, arrdbl, Array of ?

        Returns

        Array : A 3-D point in world coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(131, 1, (12, 0), ((8197, 0), (8197, 0),), u'XformCPlaneToWorld', None, _utils.flatten(point), _utils.flatten(plane))

    def xform_change_basis(self, plane1, plane2, x0, y0, z0, x1, y1, z1):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_compare(self, xform1, xform2):
        """

        Compares two transformation matrices.

        Parameters

        Xform1 : Required, Array, arrdbl, Array of ?
        Xform2 : Required, Array, arrdbl, Array of ?

        Returns

        Null : On error.

        """

        return self._ApplyTypes_(789, 1, (12, 0), ((8197, 0), (8197, 0),), u'XformCompare', None, _utils.flatten(xform1), _utils.flatten(xform2))

    def xform_determinant(self, xform):
        """

        Returns the determinant of a transformation matrix. If the determinant of a transformation matrix is 0, the matrix is said to be singular. Singular matrices do not have inverses.

        Parameters

        Xform : Required, Array, arrdbl, Array of ?

        Returns

        Number : The determinant if successful.
        Null : On error.

        """

        return self._ApplyTypes_(818, 1, (12, 0), ((8197, 0),), u'XformDeterminant', None, _utils.flatten(xform))

    def xform_diagonal(self, value):
        """

        1

        Parameters

        Value : Required, number, dbl, Double

        Returns

        Array : The 4x4 transformation matrix if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(784, 1, (12, 0), ((5, 0),), u'XformDiagonal', None, value)

    def xform_identity(self):
        """

        1

        No parameters

        Returns

        Array : The 4x4 transformation matrix.

        """

        return self._ApplyTypes_(783, 1, (12, 0), (,), u'XformIdentity', None, )

    def xform_inverse(self, xform):
        """

        Returns the inverse of a non-singular transformation matrix.

        Parameters

        Xform : Required, Array, arrdbl, Array of ?

        Returns

        Array : The inverted 4x4 transformation matrix if successful.
        Null : If matrix is non-singular, On error.

        """

        return self._ApplyTypes_(817, 1, (12, 0), ((8197, 0),), u'XformInverse', None, _utils.flatten(xform))

    def xform_mirror(self, point, normal):
        """

        Creates a mirror transformation matrix.

        Parameters

        Point : Required, Array, arrdbl, Array of ?
        Normal : Required, Array, arrdbl, Array of ?

        Returns

        Array : The 4x4 transformation matrix is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(795, 1, (12, 0), ((8197, 0), (8197, 0),), u'XformMirror', None, _utils.flatten(point), _utils.flatten(normal))

    def xform_multiply(self, xform1, xform2):
        """

        Multiples two transformation matrices, where arrXform = arrXform1 * arrXform2.

        Parameters

        Xform1 : Required, Array, arrdbl, Array of ?
        Xform2 : Required, Array, arrdbl, Array of ?

        Returns

        Array : The 4x4 transformation matrix.
        Null : On error.

        """

        return self._ApplyTypes_(788, 1, (12, 0), ((8197, 0), (8197, 0),), u'XformMultiply', None, _utils.flatten(xform1), _utils.flatten(xform2))

    def xform_planar_projection(self, plane):
        """

        Returns a transformation matrix that projects to a plane.

        Parameters

        Plane : Required, Array, arrdbl, Array of ?

        Returns

        Array : The 4x4 transformation matrix.
        Null : On error.

        """

        return self._ApplyTypes_(793, 1, (12, 0), ((8197, 0),), u'XformPlanarProjection', None, _utils.flatten(plane))

    def xform_rotation(self, plane1, plane2, angle, axis, start_dir, end_dir, point, x0, y0, z0, x1, y1, z1):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_scale(self, plane, x_scale, y_scale, z_scale, vector, point, scale):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def xform_screen_to_world(self, point, view, convert):
        """

        Transforms either client-area coordinates of a specified view or screen coordinates to world coordinates. The resulting coordinates are represented as a 3-D point.

        Parameters

        Point : Required, Array, arrdbl, Array of ?
        View : Optional, String, str, String
        Convert : Optional, Boolean, bln, Boolean

        Returns

        Array : A 3-D point in world coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(581, 1, (12, 0), ((8197, 0), (8, 0), (11, 0),), u'XformScreenToWorld', None, _utils.flatten(point), view, convert)

    def xform_shear(self, plane, x1, y1, z1):
        """

        Returns a scale transformation matrix.

        Parameters

        Plane : Required, Array (Plane), arrdbl, Array of ?
        X1 : Required, Array (3-D Vector), arrdbl, Array of ?
        Y1 : Required, Array (3-D Vector), arrdbl, Array of ?
        Z1 : Required, Array (3-D Vector), arrdbl, Array of ?

        Returns

        Array : The 4x4 transformation matrix.
        Null : On error.

        """

        return self._ApplyTypes_(791, 1, (12, 0), ((8197, 0), (8197, 0), (8197, 0), (8197, 0),), u'XformShear', None, _utils.flatten(plane), _utils.flatten(x1), _utils.flatten(y1), _utils.flatten(z1))

    def xform_translation(self, vector):
        """

        Creates a translation transformation matrix.

        Parameters

        Vector : Required, Array, arrdbl, Array of ?

        Returns

        Array : The 4x4 transformation matrix is successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(792, 1, (12, 0), ((8197, 0),), u'XformTranslation', None, _utils.flatten(vector))

    def xform_world_to_c_plane(self, point, plane):
        """

        Transforms a point from world coordinates to construction plane coordinates.

        Parameters

        Point : Required, Array, arrdbl, Array of ?
        Plane : Required, Array, arrdbl, Array of ?

        Returns

        Array : A 3-D point in construction plane coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(132, 1, (12, 0), ((8197, 0), (8197, 0),), u'XformWorldToCPlane', None, _utils.flatten(point), _utils.flatten(plane))

    def xform_world_to_screen(self, point, view, convert):
        """

        Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2-D point.

        Parameters

        Point : Required, Array, arrdbl, Array of ?
        View : Optional, String, str, String
        Convert : Optional, Boolean, bln, Boolean

        Returns

        Array : If blnConvert is omitted or False, a 2-D point in client-area coordinates if successful.
        Array : If blnConvert is True, a 2-D point in screen coordinates if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(582, 1, (12, 0), ((8197, 0), (8, 0), (11, 0),), u'XformWorldToScreen', None, _utils.flatten(point), view, convert)

    def xform_zero(self):
        """

        0

        No parameters

        Returns

        Array : The 4x4 transformation matrix.

        """

        return self._ApplyTypes_(782, 1, (12, 0), (,), u'XformZero', None, )

