# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class LineAndPlane(DispatchBaseClass):



	def DistanceToPlane(self, arrPlane, 0, 1, 2, 3, arrPoint):
		"""

		Returns the distance from a 3-D point to a plane.

		Parameters

		arrPlane : Required,   Array,   The plane
		0 : Required,   The plane's origin (3-D point), 
		1 : Required,   The plane's X axis direction (3-D vector), 
		2 : Required,   The plane's Y axis direction (3-D vector), 
		3 : Optional,   The plane's Z axis direction (3-D vector), 
		arrPoint : Required,   Array,   The 3-D point

		Returns

		Number : The distance if successful.
		Null : If not successful, or on error.

		"""

		pass

	def EvaluatePlane(self, arrPlane, 0, 1, 2, 3, arrParameter):
		"""

		Evaluates a plane at a U,V parameter.

		Parameters

		arrPlane : Required,   Array,   The plane
		0 : Required,   The plane's origin (3-D point), 
		1 : Required,   The plane's X axis direction (3-D vector), 
		2 : Required,   The plane's Y axis direction (3-D vector), 
		3 : Optional,   The plane's Z axis direction (3-D vector), 
		arrParameter : Required,   Array,   An array containing the U,V parameter to evaluate

		Returns

		Array : The 3-D point if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IntersectPlanes(self, arrPlane1, arrPlane2, arrPlane3):
		"""

		Calculates the intersection of three planes.

		Parameters

		arrPlane1 : Required,   Array,   The first plane to intersect
		arrPlane2 : Required,   Array,   The second plane to intersect
		arrPlane3 : Required,   Array,   The third plane to intersect

		Returns

		Array : The 3-D point of intersection is successful.
		Null : If not successful, or on error.

		"""

		pass

	def LineClosestPoint(self, arrLine, arrPoint):
		"""

		Finds the point on an infinite line that is closest to a test point.

		Parameters

		arrLine : Required,   Array,   Two 3-D points identifying the starting and ending points of the line
		arrPoint : Required,   Array,   The test point

		Returns

		Array : The point on the line that is closest to the test point is successful.
		Null : If not successful, or on error.

		"""

		pass

	def LineIsFartherThan(self, arrLine, dblDistance, arrPoint, arrLine2):
		"""

		Determines if the shortest distance from a line to a point or another line is greater than a specified distance.

		Parameters

		arrLine : Required,   Array,   Two 3-D points identifying the starting and ending points of the line
		dblDistance : Required,   Number,   The distance
		arrPoint : Required,   Array,   The test point
		arrLine2 : Required,   Array,   Two 3-D points identifying the starting and ending points of the test line

		Returns

		Boolean : True if the shortest distance from the line to the other object is greater than dblDistance, False otherwise.
		Null : On error.

		"""

		pass

	def LineLineIntersection(self, arrLineA, arrLineB, blnPlanar):
		"""

		But, two lines in three dimensions generally do not intersect at a point. They may be parallel (no intersections) or they may be coincident (infinite intersections). But, most often only their projection onto a plane intersects. When they do not exactly intersect at a point they can be connected by a line segment, the shortest line segment is unique and is often considered to be their intersection in 3-D.

		Parameters

		arrLineA : Required,   Array,   Two 3-D points identifying the starting and ending points of the first line
		arrLineB : Required,   Array,   Two 3-D points identifying the starting and ending points of the second line
		blnPlanar : Optional,   Boolean,   Assume that the two lines are co-planar

		Returns

		Array : If blnPlanar is omitted or True, then a single 3-D intersection point if successful.
		Array : If blnPlanar is False, then an array containing a point on the first line and a point on the second line if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LineMaxDistanceTo(self, arrLine, arrPoint, arrLine2):
		"""

		Finds the longest distance between the line, as a finite chord, and a point or another line.

		Parameters

		arrLine : Required,   Array,   Two 3-D points identifying the starting and ending points of the line
		arrPoint : Required,   Array,   The test point
		arrLine2 : Required,   Array,   Two 3-D points identifying the starting and ending points of the test line (another finite chord)

		Returns

		Boolean : A distance (D) such that if Q is any point on the line and P is any point on the other object, then D >= Rhino.Distance(Q, P).
		Null : On error.

		"""

		pass

	def LineMinDistanceTo(self, arrLine, arrPoint, arrLine2):
		"""

		Finds the shortest distance between the line, as a finite chord, and a point or another line.

		Parameters

		arrLine : Required,   Array,   Two 3-D points identifying the starting and ending points of the line
		arrPoint : Required,   Array,   The test point
		arrLine2 : Required,   Array,   Two 3-D points identifying the starting and ending points of the test line (another finite chord)

		Returns

		Boolean : A distance (D) such that if Q is any point on the line and P is any point on the other object, then D <= Rhino.Distance(Q, P).
		Null : On error.

		"""

		pass

	def LinePlane(self, arrLine):
		"""

		Returns a plane that contains the line.  The origin of the plane is at the start of the line.  If possible, a plane parallel to the world XY, YZ or ZX plane is returned.

		Parameters

		arrLine : Required,   Array,   Two 3-D points identifying the starting and ending points of the line

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def LinePlaneIntersection(self, arrLine, arrPoint):
		"""

		Calculates the intersection of a line and a plane.

		Parameters

		arrLine : Required,   Array,   Two 3-D points identifying the starting and ending points of the line to intersect
		arrPoint : Required,   Array,   The plane to intersect

		Returns

		Array : The 3-D point of intersection is successful.
		Null : If not successful, or on error.

		"""

		pass

	def LineTransform(self, arrLine, arrXform):
		"""

		Transforms a line.

		Parameters

		arrLine : Required,   Array,   Two 3-D points identifying the starting and ending points of the line
		arrXform : Required,   Array,   A valid 4x4 transformation matrix

		Returns

		Array : The resulting line if successful.
		Null : On error.

		"""

		pass

	def MovePlane(self, arrPlane, 0, 1, 2, 3, arrOrigin):
		"""

		Moves the origin of a plane.

		Parameters

		arrPlane : Required,   Array,   The plane
		0 : Required,   The plane's origin (3-D point), 
		1 : Required,   The plane's X axis direction (3-D vector), 
		2 : Required,   The plane's Y axis direction (3-D vector), 
		3 : Optional,   The plane's Z axis direction (3-D vector), 
		arrOrigin : Required,   Array,   A 3-D point identifying the new origin location

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def PlaneClosestPoint(self, arrPlane, 0, 1, 2, 3, arrPoint, blnReturnPoint):
		"""

		Returns the point on a plane that is closest to a test point.

		Parameters

		arrPlane : Required,   Array,   The plane
		0 : Required,   The plane's origin (3-D point), 
		1 : Required,   The plane's X axis direction (3-D vector), 
		2 : Required,   The plane's Y axis direction (3-D vector), 
		3 : Optional,   The plane's Z axis direction (3-D vector), 
		arrPoint : Required,   Array,   The 3-D point to test
		blnReturnPoint : Optional,   Boolean,   If omitted or True, then the point on the plane that is closest to the test point is returned

		Returns

		Array : If blnReturnPoint is omitted or True, then the 3-D point if successful. If blnReturnPoint is False, then an array containing the U,V parameters of the point if successful.
		Null : If not successful, or on error.

		"""

		pass

	def PlaneEquation(self, arrPlane, 0, 1, 2, 3):
		"""

		Ax + By + Cz + D = 0

		Parameters

		arrPlane : Required,   Array,   The plane
		0 : Required,   The plane's origin (3-D point), 
		1 : Required,   The plane's X axis direction (3-D vector), 
		2 : Required,   The plane's Y axis direction (3-D vector), 
		3 : Optional,   The plane's Z axis direction (3-D vector), 

		Returns

		Array : An array containing four numbers that represent the coefficients of the equation, if successful.
		Null : If not successful, or on error.

		"""

		pass

	def PlaneFitFromPoints(self, arrPoints):
		"""

		Returns a plane that was fit through an array of 3-D points.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def PlaneFromFrame(self, arrOrigin, arrXaxis, arrYaxis):
		"""

		Construct a plane from a point, and two vectors in the plane.

		Parameters

		arrOrigin : Required,   Array,   A 3-D point identifying the origin of the plane
		arrXaxis : Required,   Array,   A non-zero 3-D vector in the plane that determines the X axis direction
		arrYaxis : Required,   Array,   A non-zero 3-D vector not parallel to arrXaxis that is used to determine the Y axis direction

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def PlaneFromNormal(self, arrOrigin, arrNormal):
		"""

		Creates a plane from an origin point and a normal direction vector.

		Parameters

		arrOrigin : Required,   Array,   A 3-D point identifying the origin of the plane
		arrNormal : Required,   Array,   A non-zero 3-D vector identifying the normal direction of the plane

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def PlaneFromPoints(self, arrOrigin, arrPointX, arrPointY):
		"""

		Creates a plane from three non-colinear points.

		Parameters

		arrOrigin : Required,   Array,   The first point, or origin, of the plane
		arrPointX : Required,   Array,   A point on the plane's X axis
		arrPointY : Required,   Array,   A point on the plane's Y axis

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def PlanePlaneIntersection(self, arrPlane1, arrPoint2):
		"""

		Calculates the intersection of two planes.

		Parameters

		arrPlane1 : Required,   Array,   The first plane to intersect
		arrPoint2 : Required,   Array,   The second plane to intersect

		Returns

		Array : Two 3-D points identifying the starting and ending points of the intersection line.
		Null : If not successful, or on error.

		"""

		pass

	def PlaneTransform(self, arrPlane, arrXform):
		"""

		Transforms a plane.

		Parameters

		arrPlane : Required,   Array,   The plane to transform
		arrXform : Required,   Array,   A valid 4x4 transformation matrix

		Returns

		Array : The resulting plane if successful.
		Null : On error.

		"""

		pass

	def RotatePlane(self, arrPlane, 0, 1, 2, 3, dblAngle, arrAxis):
		"""

		Rotates a plane.

		Parameters

		arrPlane : Required,   Array,   The plane
		0 : Required,   The plane's origin (3-D point), 
		1 : Required,   The plane's X axis direction (3-D vector), 
		2 : Required,   The plane's Y axis direction (3-D vector), 
		3 : Optional,   The plane's Z axis direction (3-D vector), 
		dblAngle : Required,   Number,   The rotation angle in degrees
		arrAxis : Required,   Array,   A non-zero 3-D vector identifying the axis of rotation

		Returns

		Array : The plane if successful.  The elements of a plane array are as follows:
		Null : If not successful, or on error.

		"""

		pass

	def WorldXYPlane(self):
		"""

		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(1.0,0.0,0.0), Array(0.0,1.0,0.0)

		No parameters

		Returns

		Array : Rhino's world XY plane.

		"""

		pass

	def WorldYZPlane(self):
		"""

		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,1.0,0.0), Array(0.0,0.0,1.0)

		No parameters

		Returns

		Array : Rhino's world YZ plane.

		"""

		pass

	def WorldZXPlane(self):
		"""

		Rhino.PlaneFromFrame Array(0.0,0.0,0.0), Array(0.0,0.0,1.0), Array(1.0,0.0,0.0)

		No parameters

		Returns

		Array : Rhino's world ZX plane.

		"""

		pass

