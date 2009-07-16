# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Math(DispatchBaseClass):



    def a_cos(self, number):
        """

        Returns the arccosine, or inverse cosine, of a number. The arccosine is the angle whose cosine is number. The returned angle is given in radians in the range 0 (zero) to PI.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : An angle, ?, measured in radians, such that 0 = ? = PI. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(757, 1, (12, 0), ((12, 0)), u'ACos', None, number)

    def a_cos_h(self, number):
        """

        Returns the inverse hyperbolic cosine of a number. Number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is number, so ACosH(CosH(number)) equals the number.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : The inverse hyperbolic cosine of a number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(763, 1, (12, 0), ((12, 0)), u'ACosH', None, number)

    def a_sin(self, number):
        """

        Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is number. The returned angle is given in radians in the range -PI/2 to PI/2.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : An angle, ?, measured in radians, if successful. Note, A positive return value represents a counterclockwise angle from the x-axis; a negative return value represents a clockwise angle. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(756, 1, (12, 0), ((12, 0)), u'ASin', None, number)

    def a_sin_h(self, number):
        """

        Returns the inverse hyperbolic sine of a number. The inverse hyperbolic sine is the value whose hyperbolic sine is number, so ASinH(SinH(number)) equals number.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : The inverse hyperbolic sine of a number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(762, 1, (12, 0), ((12, 0)), u'ASinH', None, number)

    def a_tan2(self, , ):
        """

        Returns the angle whose tangent is the quotient of two specified numbers.

        Parameters

         : Required, Number, y
         : Required, Number, x

        Returns

        Number : An angle, ?, measured in radians, such that -PI = ? = PI, and Tan(?) = y / x, where (x, y) is a point in the Cartesian plane.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(758, 1, (12, 0), (y, x), u'ATan2', None, , )

    def a_tan_h(self, number):
        """

        Returns the inverse hyperbolic tangent of a number. Number must be between -1 and 1 (excluding -1 and 1). The inverse hyperbolic tangent is the value whose hyperbolic tangent is number; ATanH(TanH(number)) equals number.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : The inverse hyperbolic tangent of a number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(764, 1, (12, 0), ((12, 0)), u'ATanH', None, number)

    def angle(self, point1, point2, world):
        """

        Measures the angle between two points.

        Parameters

        Point1 : Required, Array, arr
        Point2 : Required, Array, arr
        World : Optional, Boolean, bln

        Returns

        Array : An array containing the following elements if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(115, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'Angle', None, point1, point2, world)

    def angle2(self, point1, point2):
        """

        Measures the angle between two lines.

        Parameters

        Point1 : Required, Array, arr
        Point2 : Required, Array, arr

        Returns

        Array : An array containing the following elements if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(116, 1, (12, 0), ((12, 0), (12, 0)), u'Angle2', None, point1, point2)

    def ceil(self, number):
        """

        Returns the smallest integer greater than or equal to the specified number.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : The ceiling if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(766, 1, (12, 0), ((12, 0)), u'Ceil', None, number)

    def cos_h(self, angle):
        """

        Returns the hyperbolic cosine of the specified angle.

        Parameters

        Angle : Required, Number, dbl

        Returns

        Number : The hyperbolic cosine of dblAngle if successful. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(760, 1, (12, 0), ((12, 0)), u'CosH', None, angle)

    def deviation(self, numbers):
        """

        Returns the standard deviation from an array of numbers.

        Parameters

        Numbers : Required, Array, arr

        Returns

        Number : The standard deviation if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(773, 1, (12, 0), ((12, 0)), u'Deviation', None, numbers)

    def distance(self, point1, point2, point_array):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def e(self):
        """

        Returns the value of the base of the natural system of logarithms (e).

        No parameters

        Returns

        Number : 2.71828182845904523536028747135

        """

        return self._ApplyTypes_(774, 1, (12, 0), (), u'E', None, )

    def floor(self, number):
        """

        Returns the largest integer less than or equal to the specified number.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : The floor if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(767, 1, (12, 0), ((12, 0)), u'Floor', None, number)

    def hypot(self, , ):
        """

        Calculates the length of the hypotenuse of a right triangle, given the length of the two sides x and y (in other words, the square root of x2 + y2).

        Parameters

         : Required, Number, x
         : Required, Number, y

        Returns

        Number : The length of the hypotenuse if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(765, 1, (12, 0), (x, y), u'Hypot', None, , )

    def log10(self, number):
        """

        Returns the base-10 logarithm of a number.

        Parameters

        Number : Required, Number, dbl

        Returns

        Number : The base-10 logarithm of the number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(777, 1, (12, 0), ((12, 0)), u'Log10', None, number)

    def max(self, numbers):
        """

        Returns the maximum number from an array of numbers.

        Parameters

        Numbers : Required, Array, arr

        Returns

        Number : The maximum number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(768, 1, (12, 0), ((12, 0)), u'Max', None, numbers)

    def mean(self, numbers):
        """

        Returns the mean number, or average, from an array of numbers.

        Parameters

        Numbers : Required, Array, arr

        Returns

        Number : The mean number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(771, 1, (12, 0), ((12, 0)), u'Mean', None, numbers)

    def median(self, numbers):
        """

        Returns the median value from an array of numbers.

        Parameters

        Numbers : Required, Array, arr

        Returns

        Number : The median value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(772, 1, (12, 0), ((12, 0)), u'Median', None, numbers)

    def min(self, numbers):
        """

        Returns the minimum number from an array of numbers.

        Parameters

        Numbers : Required, Array, arr

        Returns

        Number : The minimum number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(769, 1, (12, 0), ((12, 0)), u'Min', None, numbers)

    def p_i(self):
        """

        Returns the ratio of the circumference of a circle to its diameter, approximately 3.141592653589793238462643.

        No parameters

        Returns

        Number : 3.141592653589793238462643

        """

        return self._ApplyTypes_(663, 1, (12, 0), (), u'PI', None, )

    def polar(self, point, angle, distance, plane):
        """

        Returns the 3-D point that is a specified angle and distance from a 3-D point.

        Parameters

        Point : Required, Array, arr
        Angle : Required, Number, dbl
        Distance : Required, Number, dbl
        Plane : Optional, Array, arr

        Returns

        Array : The resulting 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(662, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'Polar', None, point, angle, distance, plane)

    def sin_h(self, angle):
        """

        Returns the hyperbolic sine of the specified angle.

        Parameters

        Angle : Required, Number, dbl

        Returns

        Number : The hyperbolic sine of dblAngle if successful. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(759, 1, (12, 0), ((12, 0)), u'SinH', None, angle)

    def sum(self, numbers):
        """

        Returns the sum of an array of numbers.

        Parameters

        Numbers : Required, Array, arr

        Returns

        Number : The sum of the array if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(770, 1, (12, 0), ((12, 0)), u'Sum', None, numbers)

    def tan_h(self, angle):
        """

        Returns the hyperbolic tangent of the specified angle.

        Parameters

        Angle : Required, Number, dbl

        Returns

        Number : The hyperbolic tangent of dblAngle if successful. Use ToDegrees to convert from radians to degrees.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(761, 1, (12, 0), ((12, 0)), u'TanH', None, angle)

    def to_degrees(self, radians):
        """

        Converts an angle specified in radians to degrees.

        Parameters

        Radians : Required, Number, dbl

        Returns

        Number : The angle in degrees if successful.
        Null : On error.

        """

        return self._ApplyTypes_(664, 1, (12, 0), ((12, 0)), u'ToDegrees', None, radians)

    def to_radians(self, degrees):
        """

        Converts an angle specified in degrees to radians.

        Parameters

        Degrees : Required, Number, dbl

        Returns

        Number : The angle in radians if successful.
        Null : On error.

        """

        return self._ApplyTypes_(665, 1, (12, 0), ((12, 0)), u'ToRadians', None, degrees)

