# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class PointAndVector(DispatchBaseClass):



	def IsVectorParallelTo(self, arrVector1, arrVector2):
		"""

		Compares two vectors to see if they are parallel.

		Parameters

		arrVector1 : Required,   Array,   The 3-D vector
		arrVector2 : Required,   Array,   The 3-D vector to compare to

		Returns

		Number : The result of the comparison if successful. The possible results are as follows:
		Null : On error.

		"""

		pass

	def IsVectorPerpendicularTo(self, arrVector1, arrVector2):
		"""

		Compares two vectors to see if they are perpendicular.

		Parameters

		arrVector1 : Required,   Array,   The 3-D vector
		arrVector2 : Required,   Array,   The 3-D vector to compare to

		Returns

		Boolean : True if the vectors are perpendicular, otherwise False.
		Null : On error.

		"""

		pass

	def IsVectorTiny(self, arrVector):
		"""

		Verifies that a vector is very short, or tiny - the x,y,z  elements are less than or equal to 1.0e-12.

		Parameters

		arrVector : Required,   Array,   The 3-D vector to test

		Returns

		Boolean : True if the vector is tiny, otherwise False, if successful.
		Null : On error.

		"""

		pass

	def IsVectorZero(self, arrVector):
		"""

		Verifies that a vector is zero, or tiny - the  x,y,z elements are equal to 0.0.

		Parameters

		arrVector : Required,   Array,   The 3-D vector to test

		Returns

		Boolean : True if the vector is zero, otherwise False, if successful.
		Null : On error.

		"""

		pass

	def PointAdd(self, arrPoint1, arrPoint2):
		"""

		Adds a 3-D point or a 3-D vector to a 3-D point.

		Parameters

		arrPoint1 : Required,   Array,   The 3-D point to add to
		arrPoint2 : Required,   Array,   The 3-D point or a 3-D vector to add

		Returns

		Array : The resulting 3-D point if successful.
		Null : On error.

		"""

		pass

	def PointArrayBoundingBox(self, arrPoints, strView, blnWorldCoords):
		"""

		Returns either a world axis-aligned or a construction plane axis-aligned bounding box of an array of 3-D point locations.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points
		strView : Optional,   String,   The title of the view that contains the construction plane to which the bounding box should be aligned
		blnWorldCoords : Optional,   Boolean,   Whether or not to return the bounding box as world coordinates or construction plane coordinates

		Returns

		Array : An array of eight 3-D points that define the bounding box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
		Null : If not successful, or on error.

		"""

		pass

	def PointArrayClosestPoint(self, arrPoints, arrPoint):
		"""

		Finds the point in an array of 3-D points that is closest to a test point.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points to test
		arrPoint : Required,   Array,   The 3-D test point

		Returns

		Number : The index of the element in the point array that is closest to the test point if successful.
		Null : If not successful, or on error.

		"""

		pass

	def PointArrayTransform(self, arrPoints, arrXform):
		"""

		Transforms an array of 3-D points.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points to transform
		arrXform : Required,   Array,   A valid 4x4 transformation matrix

		Returns

		Array : The resulting array of 3-D points if successful.
		Null : On error.

		"""

		pass

	def PointCompare(self, arrPoint1, arrPoint2, dblTolerance):
		"""

		Compares two 3-D points.

		Parameters

		arrPoint1 : Required,   Array,   The first 3-D point to compare
		arrPoint2 : Required,   Array,   The second 3-D point to compare
		dblTolerance : Optional,   Number,   The tolerance to use for the comparison

		Returns

		Boolean : True or False
		Null : On error.

		"""

		pass

	def PointDivide(self, arrPoint, dblScale):
		"""

		Divides a 3-D point by a value

		Parameters

		arrPoint : Required,   Array,   The 3-D point to divide
		dblScale : Required,   Number,   The a non-zero value to divide

		Returns

		Array : The resulting 3-D point if successful.
		Null : On error.

		"""

		pass

	def PointScale(self, arrPoint, dblScale):
		"""

		Scales a 3-D point.

		Parameters

		arrPoint : Required,   Array,   The 3-D point to scale
		dblScale : Required,   Number,   The scale factor to apply

		Returns

		Array : The resulting 3-D point if successful.
		Null : On error.

		"""

		pass

	def PointSubtract(self, arrPoint1, arrPoint2):
		"""

		Subtracts a 3-D point or a 3-D vector from a 3-D point.

		Parameters

		arrPoint1 : Required,   Array,   The 3-D point to subtract from
		arrPoint2 : Required,   Array,   The 3-D point or a 3-D vector to subtract

		Returns

		Array : The resulting 3-D point if successful.
		Null : On error.

		"""

		pass

	def PointTransform(self, arrPoint, arrXform):
		"""

		Transforms a 3-D point.

		Parameters

		arrPoint : Required,   Array,   The 3-D point to transform
		arrXform : Required,   Array,   A valid 4x4 transformation matrix

		Returns

		Array : The resulting 3-D point if successful.
		Null : On error.

		"""

		pass

	def PointsAreCoplanar(self, arrPoints, dblTolerance):
		"""

		Verifies that an array of 3-D points are co-planar.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points
		dblTolerance : Optional,  Number,  A tolerance to use when verifying

		Returns

		Boolean : True or False indicating either coplanar or not coplanar, respectively, if successful.
		Null : On error.

		"""

		pass

	def ProjectPointToMesh(self, arrPoints, arrPoints, strMesh, arrMeshes, arrDirection):
		"""

		Projects one or more points onto one or more meshes.

		Parameters

		arrPoints : Required,   Array,   A 3-D point to project
		arrPoints : Required,   Array,   An array of 3-D points to project
		strMesh : Required,   String,   The identifier of the mesh object to project onto
		arrMeshes : Required,   Array,   The identifiers of the mesh objects to project onto
		arrDirection : Required,   Array,   The direction (3-D vector) to project the points

		Returns

		Array : An array of 3-D points if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ProjectPointToSurface(self, arrPoints, arrPoints, strSurface, arrSurfaces, arrDirection):
		"""

		Projects one or more points onto one or more surfaces or polysurfaces.

		Parameters

		arrPoints : Required,   Array,   A 3-D point to project
		arrPoints : Required,   Array,   An array of 3-D points to project
		strSurface : Required,   String,   The identifier of the surface or polysurface object to project onto
		arrSurfaces : Required,   Array,   The identifiers of the surface or polysurface objects to project onto
		arrDirection : Required,   Array,   The direction (3-D vector) to project the points

		Returns

		Array : An array of 3-D points if successful.
		Null : If not successful, or on error.

		"""

		pass

	def PullPoints(self, strObject, arrPoints):
		"""

		Pulls an array of points to a surface or mesh object. For more information, see the Rhino help file for information on the Pull command.

		Parameters

		strObject : Required,   String,   The identifier of the surface or mesh object that pulls
		arrPoints : Required,   String,   An array of 3-D points to pull

		Returns

		Array : An array of 3-D points if successful.
		Null : If not successful, or on error.

		"""

		pass

	def VectorAdd(self, arrVector1, arrVector2):
		"""

		Adds two 3-D vectors.

		Parameters

		arrVector1 : Required,   Array,   The 3-D vector to add to
		arrVector2 : Required,   Array,   The 3-D vector to add

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorCompare(self, arrVector1, arrVector2):
		"""

		Compares two 3-D vectors.

		Parameters

		arrVector1 : Required,   Array,   The first 3-D vector to compare
		arrVector2 : Required,   Array,   The second 3-D vector to compare

		Returns

		Null : On error.

		"""

		pass

	def VectorCreate(self, arrPoint1, arrPoint2):
		"""

		Creates a vector from two 3-D points.

		Parameters

		arrPoint1 : Required,   Array,   The first 3-D point
		arrPoint2 : Required,   Array,   The second 3-D point

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorCrossProduct(self, arrVector1, arrVector2):
		"""

		Calculates the cross product of two 3-D vectors.

		Parameters

		arrVector1 : Required,   Array,   The first 3-D vector
		arrVector2 : Required,   Array,   The second 3-D vector

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorDivide(self, arrVector, dblDivide):
		"""

		Divides a 3-D vectors by a value

		Parameters

		arrVector : Required,   Array,   The 3-D vector to divide
		dblDivide : Required,   Number,   The a non-zero value to divide

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorDotProduct(self, arrVector1, arrVector2):
		"""

		Calculates the dot product of two 3-D vectors.

		Parameters

		arrVector1 : Required,   Array,   The first 3-D vector
		arrVector2 : Required,   Array,   The second 3-D vector

		Returns

		Null : On error.

		"""

		pass

	def VectorLength(self, arrVector):
		"""

		Returns the length of a 3-D vector.

		Parameters

		arrVector : Required,   Array,   The 3-D vector

		Returns

		Null : On error.

		"""

		pass

	def VectorMultiply(self, arrVector1, arrVector2):
		"""

		Multiplies two 3-D vectors.

		Parameters

		arrVector1 : Required,   Array,   The first 3-D vector
		arrVector2 : Required,   Array,   The second 3-D vector

		Returns

		Number : The resulting inner (dot) product if successful.
		Null : On error.

		"""

		pass

	def VectorReverse(self, arrVector):
		"""

		Reverses the direction of a 3-D vector.

		Parameters

		arrVector : Required,   Array,   The 3-D vector

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorRotate(self, arrVector, dblAngle, arrAxis):
		"""

		Rotates a 3-D vector.

		Parameters

		arrVector : Required,   Array,   The 3-D vector
		dblAngle : Required,   Number,   The rotation angle in degrees
		arrAxis : Required,   Array,   A 3-D vector defining the axis of rotation

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorScale(self, arrVector, dblScale):
		"""

		Scales a 3-D vector.

		Parameters

		arrVector : Required,   Array,   The 3-D vector to scale
		dblScale : Required,   Number,   The scale factor to apply

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorSubtract(self, arrVector1, arrVector2):
		"""

		Subtracts two 3-D vectors.

		Parameters

		arrVector1 : Required,   Array,   The 3-D vector to subtract from
		arrVector2 : Required,   Array,   The 3-D vector to subtract

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorTransform(self, arrVector, arrXform):
		"""

		Transforms a 3-D vector.

		Parameters

		arrVector : Required,   Array,   The 3-D vector to transform
		arrXform : Required,   Array,   A valid 4x4 transformation matrix

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

	def VectorUnitize(self, arrVector):
		"""

		Unitizes, or normalizes, a 3-D vector. Note, zero vectors cannot be unitized.

		Parameters

		arrVector : Required,   Array,   The 3-D vector to unitize

		Returns

		Array : The resulting 3-D vector if successful.
		Null : On error.

		"""

		pass

