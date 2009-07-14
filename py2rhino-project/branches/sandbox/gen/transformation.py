# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Transformation(DispatchBaseClass):



	def XformChangeBasis(self, arrPlane1, arrPlane2, arrX0, arrY0, arrZ0, arrX1, arrY1, arrZ1):
		"""

		Returns a change of basis transformation matrix.

		Parameters

		arrPlane1 : Required,   Array (Plane),   The initial plane
		arrPlane2 : Required,   Array (Plane),   The final plane
		arrX0 : Required,   Array (3-D Vector),   The initial basis X (X0,Y0,Z0 can be any 3-D basis)
		arrY0 : Required,   Array (3-D Vector),  The  initial basis Y
		arrZ0 : Required,   Array (3-D Vector),  The  initial basis Z
		arrX1 : Required,   Array (3-D Vector),   The final basis X (X1,Y1,Z1 can be any 3-D basis)
		arrY1 : Required,   Array (3-D Vector),   The  final basis Y
		arrZ1 : Required,   Array (3-D Vector),   The final basis Z

		Returns

		Array : The 4x4 transformation matrix if successful.
		Null : If not successful, or on error.

		"""

		pass

	def XformCPlaneToWorld(self, arrPoint, arrPlane, 0, 1, 2, 3):
		"""

		Transforms a point from construction plane coordinates to world coordinates.

		Parameters

		arrPoint : Required,   Array,   A 3-D point in construction plane coordinates
		arrPlane : Required,   Array,  The construction plane
		0 : Required,   The construction plane's origin (3-D point), 
		1 : Required,   The construction plane's X axis direction (3-D vector), 
		2 : Required,   The construction plane's Y axis direction (3-D vector), 
		3 : Optional,   The construction plane's Z axis direction (3-D vector), 

		Returns

		Array : A 3-D point in world coordinates if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsXformIdentity(self, arrXform):
		"""

		1

		Parameters

		arrXform : Required,   Array,   A 4x4 transformation matrix

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def XformDiagonal(self, dblValue):
		"""

		1

		Parameters

		dblValue : Required,   number,   The diagonal value

		Returns

		Array : The 4x4 transformation matrix if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsXformZero(self, arrXform):
		"""

		0

		Parameters

		arrXform : Required,   Array,   A 4x4 transformation matrix

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def IsXformIsSimilarity(self, arrXform):
		"""

		Verifies that a matrix is a similarity transformation. A similarity transformation can be broken into a sequence of dialations, translations, rotations, and reflections.

		Parameters

		arrXform : Required,   Array,   A 4x4 transformation matrix

		Returns

		Boolean : True if this transformation is an orientation preserving similarity, otherwise False.
		Null : On error.

		"""

		pass

	def XformIdentity(self):
		"""

		1

		No parameters

		Returns

		Array : The 4x4 transformation matrix.

		"""

		pass

	def XformScreenToWorld(self, arrPoint, strView, blnConvert):
		"""

		Transforms either client-area coordinates of a specified view or screen coordinates to world coordinates. The resulting coordinates are represented as a 3-D point.

		Parameters

		arrPoint : Required,   Array,   A 2-D point in either client-area coordinates of a specified view or screen coordinates
		strView : Optional,   String,   The title of the view
		blnConvert : Optional,  Boolean,  If omitted or False, the function assumes arrPoint represents client-area coordinates

		Returns

		Array : A 3-D point in world coordinates if successful.
		Null : If not successful, or on error.

		"""

		pass

	def XformCompare(self, arrXform1, arrXform2):
		"""

		Compares two transformation matrices.

		Parameters

		arrXform1 : Required,   Array,   The first 4x4 transformation matrix to compare
		arrXform2 : Required,   Array,   The second 4x4 transformation matrix to compare

		Returns

		Null : On error.

		"""

		pass

	def XformZero(self):
		"""

		0

		No parameters

		Returns

		Array : The 4x4 transformation matrix.

		"""

		pass

	def XformTranslation(self, arrVector):
		"""

		Creates a translation transformation matrix.

		Parameters

		arrVector : Required,   Array,   A 3-D translation vector

		Returns

		Array : The 4x4 transformation matrix is successful.
		Null : If not successful, or on error.

		"""

		pass

	def XformMirror(self, arrPoint, arrNormal):
		"""

		Creates a mirror transformation matrix.

		Parameters

		arrPoint : Required,   Array,   A 3-D point on mirror plane
		arrNormal : Required,   Array,   A 3-D vector that is normal to mirror plane

		Returns

		Array : The 4x4 transformation matrix is successful.
		Null : If not successful, or on error.

		"""

		pass

	def XformShear(self, arrPlane, arrX1, arrY1, arrZ1):
		"""

		Returns a scale transformation matrix.

		Parameters

		arrPlane : Required,   Array (Plane),   The plane, where arrPlane(0) is the fixed point
		arrX1 : Required,   Array (3-D Vector),   The x-axis scale factor
		arrY1 : Required,   Array (3-D Vector),   The y-axis scale factor
		arrZ1 : Required,   Array (3-D Vector),   The z-axis scale factor

		Returns

		Array : The 4x4 transformation matrix.
		Null : On error.

		"""

		pass

	def XformPlanarProjection(self, arrPlane):
		"""

		Returns a transformation matrix that projects to a plane.

		Parameters

		arrPlane : Required,   Array,   The plane to project to

		Returns

		Array : The 4x4 transformation matrix.
		Null : On error.

		"""

		pass

	def XformInverse(self, arrXform):
		"""

		Returns the inverse of a non-singular transformation matrix.

		Parameters

		arrXform : Required,   Array,   A 4x4 transformation matrix

		Returns

		Array : The inverted 4x4 transformation matrix if successful.
		Null : If matrix is non-singular, On error.

		"""

		pass

	def XformWorldToCPlane(self, arrPoint, arrPlane, 0, 1, 2, 3):
		"""

		Transforms a point from world coordinates to construction plane coordinates.

		Parameters

		arrPoint : Required,   Array,   A 3-D point in world coordinates
		arrPlane : Required,   Array,  The construction plane
		0 : Required,   The construction plane's origin (3-D point), 
		1 : Required,   The construction plane's X axis direction (3-D vector), 
		2 : Required,   The construction plane's Y axis direction (3-D vector), 
		3 : Optional,   The construction plane's Z axis direction (3-D vector), 

		Returns

		Array : A 3-D point in construction plane coordinates if successful.
		Null : If not successful, or on error.

		"""

		pass

	def XformWorldToScreen(self, arrPoint, strView, blnConvert):
		"""

		Transforms a point from world coordinates to either client-area coordinates of the specified view or screen coordinates. The resulting coordinates are represented as a 2-D point.

		Parameters

		arrPoint : Required,   Array,   A 3-D point in world coordinates
		strView : Optional,   String,   The title of the view
		blnConvert : Optional,  Boolean,  If omitted or False, the function returns the results as client-area coordinates of the specified view

		Returns

		Array : If blnConvert is omitted or False, a 2-D point in client-area coordinates if successful.
		Array : If blnConvert is True, a 2-D point in screen coordinates if successful.
		Null : If not successful, or on error.

		"""

		pass

	def XformDeterminant(self, arrXform):
		"""

		Returns the determinant of a transformation matrix. If the determinant of a transformation matrix is 0, the matrix is said to be singular. Singular matrices do not have inverses.

		Parameters

		arrXform : Required,   Array,   A 4x4 transformation matrix

		Returns

		Number : The determinant if successful.
		Null : On error.

		"""

		pass

	def XformRotation(self, arrPlane1, arrPlane2, dblAngle, arrAxis, arrStartDir, arrEndDir, arrPoint, arrX0, arrY0, arrZ0, arrX1, arrY1, arrZ1):
		"""

		Returns a rotation transformation matrix. The XformRotation provides several ways to compute a rotation transformation.  A positive rotation angle indicates a counter-clockwise (right hand rule) rotation about the axis of rotation.

		Parameters

		arrPlane1 : Required,   Array (Plane),   The starting plane
		arrPlane2 : Required,   Array (Plane),   The ending plane
		dblAngle : Required,   Number,   The rotation angle in degrees
		arrAxis : Required,   Array (3-D Vector),   The rotation axis
		arrStartDir : Required,   Array (3-D Vector),   The starting direction
		arrEndDir : Required,   Array (3-D Vector),   The ending direction
		arrPoint : Required,   Array (3-D Point),   The rotation center point
		arrX0 : Required,   Array (3-D Vector),   The initial frame X
		arrY0 : Required,   Array (3-D Vector),   The initial frame Y
		arrZ0 : Required,   Array (3-D Vector),   The initial frame Z
		arrX1 : Required,   Array (3-D Vector),   The final frame X
		arrY1 : Required,   Array (3-D Vector),   The final frame Y
		arrZ1 : Required,   Array (3-D Vector),   The final frame Z

		Returns

		Array : The 4x4 transformation matrix.
		Null : On error.

		"""

		pass

	def XformScale(self, arrPlane, dblXScale, dblYScale, dblZScale, arrVector, arrPoint, dblScale):
		"""

		Returns a scale transformation matrix.

		Parameters

		arrPlane : Required,   Array (Plane),   The starting plane
		dblXScale : Required,   Number,   The scale factor in the x-axis direction
		dblYScale : Required,   Number,   The scale factor in the y-axis direction
		dblZScale : Required,   Number,   The scale factor in the z-axis direction
		arrVector : Required,   Array (3-D Vector),   The ending direction
		arrPoint : Required,   Array (3-D Point),   The rotation center point
		dblScale : Required,   Array (3-D Vector),   The initial frame X

		Returns

		Array : The 4x4 transformation matrix.
		Null : On error.

		"""

		pass

	def XformMultiply(self, arrXform1, arrXform2):
		"""

		Multiples two transformation matrices, where arrXform = arrXform1 * arrXform2.

		Parameters

		arrXform1 : Required,   Array,   The first 4x4 transformation matrix to multiply
		arrXform2 : Required,   Array,   The second 4x4 transformation matrix to multiply

		Returns

		Array : The 4x4 transformation matrix.
		Null : On error.

		"""

		pass

