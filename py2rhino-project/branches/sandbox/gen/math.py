# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Math(DispatchBaseClass):



    def acos(self, dblnumber):
        """

        Returns the arccosine, or inverse cosine, of a number. The arccosine is the angle whose cosine is number. The returned angle is given in radians in the range 0 (zero) to PI.

        Parameters

        dblNumber : Required,   Number,   A number representing the cosine of the angle you want and must be from -1 to 1

        Returns

        Number : An angle, ?, measured in radians, such that 0 = ? = PI. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ACos', None, dblNumber)

    def acosh(self, dblnumber):
        """

        Returns the inverse hyperbolic cosine of a number. Number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is number, so ACosH(CosH(number)) equals the number.

        Parameters

        dblNumber : Required,   Number,   A number equal to or greater than 1

        Returns

        Number : The inverse hyperbolic cosine of a number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ACosH', None, dblNumber)

    def asin(self, dblnumber):
        """

        Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is number. The returned angle is given in radians in the range -PI/2 to PI/2.

        Parameters

        dblNumber : Required,   Number,   A number representing the sine of the angle you want and must be from -1 to 1

        Returns

        Number : An angle, ?, measured in radians, if successful. Note, A positive return value represents a counterclockwise angle from the x-axis; a negative return value represents a clockwise angle. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ASin', None, dblNumber)

    def asinh(self, dblnumber):
        """

        Returns the inverse hyperbolic sine of a number. The inverse hyperbolic sine is the value whose hyperbolic sine is number, so ASinH(SinH(number)) equals number.

        Parameters

        dblNumber : Required,   Number,   Any real number

        Returns

        Number : The inverse hyperbolic sine of a number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ASinH', None, dblNumber)

    def atan2(self, y, x):
        """

        Returns the angle whose tangent is the quotient of two specified numbers.

        Parameters

        y : Required,   Number,   The y coordinate of a point
        x : Required,   Number,   The x coordinate of a point

        Returns

        Number : An angle, ?, measured in radians, such that -PI = ? = PI, and Tan(?) = y / x, where (x, y) is a point in the Cartesian plane.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ATan2', None, y, x)

    def atanh(self, dblnumber):
        """

        Returns the inverse hyperbolic tangent of a number. Number must be between -1 and 1 (excluding -1 and 1). The inverse hyperbolic tangent is the value whose hyperbolic tangent is number; ATanH(TanH(number)) equals number.

        Parameters

        dblNumber : Required,   Number,   A number between -1 and 1

        Returns

        Number : The inverse hyperbolic tangent of a number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ATanH', None, dblNumber)

    def angle(self, arrpoint1, arrpoint2, blnworld):
        """

        Measures the angle between two points.

        Parameters

        arrPoint1 : Required,   Array,   The first 3-D point
        arrPoint2 : Required,   Array,   The second 3-D point
        blnWorld : Optional,   Boolean,   If True, the angle calculation is based on the world coordinate system

        Returns

        Array : An array containing the following elements if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Angle', None, arrPoint1, arrPoint2, blnWorld)

    def angle2(self, arrpoint1, arrpoint2):
        """

        Measures the angle between two lines.

        Parameters

        arrPoint1 : Required,   Array,   An array containing the starting and ending 3-D points of the first line
        arrPoint2 : Required,   Array,   An array containing the starting and ending 3-D points of the second line

        Returns

        Array : An array containing the following elements if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Angle2', None, arrPoint1, arrPoint2)

    def ceil(self, dblnumber):
        """

        Returns the smallest integer greater than or equal to the specified number.

        Parameters

        dblNumber : Required,   Number,   A number

        Returns

        Number : The ceiling if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Ceil', None, dblNumber)

    def cosh(self, dblangle):
        """

        Returns the hyperbolic cosine of the specified angle.

        Parameters

        dblAngle : Required,   Number,   An angle, measured in radians

        Returns

        Number : The hyperbolic cosine of dblAngle if successful. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CosH', None, dblAngle)

    def deviation(self, arrnumbers):
        """

        Returns the standard deviation from an array of numbers.

        Parameters

        arrNumbers : Required,   Array,   An array of numbers to analyze

        Returns

        Number : The standard deviation if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Deviation', None, arrNumbers)

    def distance(self, arrpoint1, arrpoint2, arrpointarray):
        """

        Measures the distance between two 3-D points, or between a 3-D point and an array of 3-D points.

        Parameters

        arrPoint1 : Required,   Array,   The first 3-D point
        arrPoint2 : Required,   Array,   The second 3-D point
        arrPointArray : Required,   Array,   An array of 3-D points

        Returns

        Number : If arrPoint1 and arrPoint2 are specified, then the distance is successful.
        Array : If arrPoint1 and arrPointArray are specified, then an array of distances if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Distance', None, arrPoint1, arrPoint2, arrPointArray)

    def e(self, ):
        """

        Returns the value of the base of the natural system of logarithms (e).

        No parameters

        Returns

        Number : 2.71828182845904523536028747135

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'E', None, )

    def floor(self, dblnumber):
        """

        Returns the largest integer less than or equal to the specified number.

        Parameters

        dblNumber : Required,   Number,   A number

        Returns

        Number : The floor if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Floor', None, dblNumber)

    def hypot(self, x, y):
        """

        Calculates the length of the hypotenuse of a right triangle, given the length of the two sides x and y (in other words, the square root of x2 + y2).

        Parameters

        x : Required,   Number,   The x value
        y : Required,   Number,   The y value

        Returns

        Number : The length of the hypotenuse if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Hypot', None, x, y)

    def log10(self, dblnumber):
        """

        Returns the base-10 logarithm of a number.

        Parameters

        dblNumber : Required,   Number,   The positive real number for which you want the base-10 logarithm

        Returns

        Number : The base-10 logarithm of the number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Log10', None, dblNumber)

    def max(self, arrnumbers):
        """

        Returns the maximum number from an array of numbers.

        Parameters

        arrNumbers : Required,   Array,   An array of numbers to analyze

        Returns

        Number : The maximum number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Max', None, arrNumbers)

    def mean(self, arrnumbers):
        """

        Returns the mean number, or average, from an array of numbers.

        Parameters

        arrNumbers : Required,   Array,   An array of numbers to analyze

        Returns

        Number : The mean number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Mean', None, arrNumbers)

    def median(self, arrnumbers):
        """

        Returns the median value from an array of numbers.

        Parameters

        arrNumbers : Required,   Array,   An array of numbers to analyze

        Returns

        Number : The median value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Median', None, arrNumbers)

    def min(self, arrnumbers):
        """

        Returns the minimum number from an array of numbers.

        Parameters

        arrNumbers : Required,   Array,   An array of numbers to analyze

        Returns

        Number : The minimum number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Min', None, arrNumbers)

    def pi(self, ):
        """

        Returns the ratio of the circumference of a circle to its diameter, approximately 3.141592653589793238462643.

        No parameters

        Returns

        Number : 3.141592653589793238462643

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PI', None, )

    def polar(self, arrpoint, dblangle, dbldistance, arrplane, 0, 1, 2, 3):
        """

        Returns the 3-D point that is a specified angle and distance from a 3-D point.

        Parameters

        arrPoint : Required,   Array,   The 3-D point to transform
        dblAngle : Required,   Number,   The angle in degrees
        dblDistance : Required,   Number,   The distance
        arrPlane : Optional,   Array,   The plane to base the transformation
        0 : Required,   The plane's origin (3-D point), 
        1 : Required,   The plane's X axis direction (3-D vector), 
        2 : Required,   The plane's Y axis direction (3-D vector), 
        3 : Optional,   The plane's Z axis direction (3-D vector), 

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Polar', None, arrPoint, dblAngle, dblDistance, arrPlane, 0, 1, 2, 3)

    def sinh(self, dblangle):
        """

        Returns the hyperbolic sine of the specified angle.

        Parameters

        dblAngle : Required,   Number,   An angle, measured in radians

        Returns

        Number : The hyperbolic sine of dblAngle if successful. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SinH', None, dblAngle)

    def sum(self, arrnumbers):
        """

        Returns the sum of an array of numbers.

        Parameters

        arrNumbers : Required,   Array,   An array of numbers to sum

        Returns

        Number : The sum of the array if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Sum', None, arrNumbers)

    def tanh(self, dblangle):
        """

        Returns the hyperbolic tangent of the specified angle.

        Parameters

        dblAngle : Required,   Number,   An angle, measured in radians

        Returns

        Number : The hyperbolic tangent of dblAngle if successful. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TanH', None, dblAngle)

    def todegrees(self, dblradians):
        """

        Converts an angle specified in radians to degrees.

        Parameters

        dblRadians : Required,   Number,   The angle in radians

        Returns

        Number : The angle in degrees if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ToDegrees', None, dblRadians)

    def toradians(self, dbldegrees):
        """

        Converts an angle specified in degrees to radians.

        Parameters

        dblDegrees : Required,   Number,   The angle in degrees

        Returns

        Number : The angle in radians if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ToRadians', None, dblDegrees)

