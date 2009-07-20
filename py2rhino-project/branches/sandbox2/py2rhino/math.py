# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Math(IRhinoScript):



    def a_cos(self, number):
        """        
        Returns the arccosine, or inverse cosine, of a number. The arccosine is the angle whose cosine is number. The returned angle is given in radians in the range 0 (zero) to PI.
    
        Parameters
        ==========

        number, Double, Required        
        A number representing the cosine of the angle you want and must be from -1 to 1.
            
        Returns
        =======

        number
        An angle, ?, measured in radians, such that 0 = ? = PI. Use ToDegrees to convert from radians to degrees.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(757, 1, (VT_VARIANT, 0), params_magic_numbers, u"ACos", None, *params_flattened)

    def a_cos_h(self, number):
        """        
        Returns the inverse hyperbolic cosine of a number. Number must be greater than or equal to 1. The inverse hyperbolic cosine is the value whose hyperbolic cosine is number, so ACosH(CosH(number)) equals the number.
    
        Parameters
        ==========

        number, Double, Required        
        A number equal to or greater than 1.
            
        Returns
        =======

        number
        The inverse hyperbolic cosine of a number if successful.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(763, 1, (VT_VARIANT, 0), params_magic_numbers, u"ACosH", None, *params_flattened)

    def a_sin(self, number):
        """        
        Returns the arcsine, or inverse sine, of a number. The arcsine is the angle whose sine is number. The returned angle is given in radians in the range -PI/2 to PI/2.
    
        Parameters
        ==========

        number, Double, Required        
        A number representing the sine of the angle you want and must be from -1 to 1.
            
        Returns
        =======

        number
        An angle, ?, measured in radians, if successful. Note, A positive return value represents a counterclockwise angle from the x-axis; a negative return value represents a clockwise angle. Use ToDegrees to convert from radians to degrees.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(756, 1, (VT_VARIANT, 0), params_magic_numbers, u"ASin", None, *params_flattened)

    def a_sin_h(self, number):
        """        
        Returns the inverse hyperbolic sine of a number. The inverse hyperbolic sine is the value whose hyperbolic sine is number, so ASinH(SinH(number)) equals number.
    
        Parameters
        ==========

        number, Double, Required        
        Any real number.
            
        Returns
        =======

        number
        The inverse hyperbolic sine of a number if successful.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(762, 1, (VT_VARIANT, 0), params_magic_numbers, u"ASinH", None, *params_flattened)

    def a_tan2(self, number_y, number_x):
        """        
        Returns the angle whose tangent is the quotient of two specified numbers.
    
        Parameters
        ==========

        number_y, Double, Required        
        The y coordinate of a point.
            
        number_x, Double, Required        
        The x coordinate of a point.
            
        Returns
        =======

        number
        An angle, ?, measured in radians, such that -PI = ? = PI, and Tan(?) = y / x, where (x, y) is a point in the Cartesian plane.

        null
        If not successful, or on error.

        """

        params = [number_y, number_x]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_R8, 1), (VT_R8, 1)]
        params_flattened = [number_y, number_x]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(758, 1, (VT_VARIANT, 0), params_magic_numbers, u"ATan2", None, *params_flattened)

    def a_tan_h(self, number):
        """        
        Returns the inverse hyperbolic tangent of a number. Number must be between -1 and 1 (excluding -1 and 1). The inverse hyperbolic tangent is the value whose hyperbolic tangent is number; ATanH(TanH(number)) equals number.
    
        Parameters
        ==========

        number, Double, Required        
        A number between -1 and 1.
            
        Returns
        =======

        number
        The inverse hyperbolic tangent of a number if successful.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(764, 1, (VT_VARIANT, 0), params_magic_numbers, u"ATanH", None, *params_flattened)

    def angle(self, point1, point2, world=None):
        """        
        Measures the angle between two points.
    
        Parameters
        ==========

        point1, Array of ????, Required        
        The first 3-D point.
            
        point2, Array of ????, Required        
        The second 3-D point.
            
        world, Boolean, Optional        
        If True, the angle calculation is based on the world coordinate system.  If False, the angle calculation is based on the active construction plane.  The default value is True.
            
        Returns
        =======

        array
        An array containing the following elements if successful.

        null
        If not successful, or on error.

        """

        params = [point1, point2, world]
        params_opt_or_req = [Required, Required, Optional]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(point1), flatten(point2), world]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(115, 1, (VT_VARIANT, 0), params_magic_numbers, u"Angle", None, *params_flattened)

    def angle2(self, point1, point2):
        """        
        Measures the angle between two lines.
    
        Parameters
        ==========

        point1, Array of ????, Required        
        An array containing the starting and ending 3-D points of the first line.
            
        point2, Array of ????, Required        
        An array containing the starting and ending 3-D points of the second line.
            
        Returns
        =======

        array
        An array containing the following elements if successful.

        null
        If not successful, or on error.

        """

        params = [point1, point2]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(point1), flatten(point2)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(116, 1, (VT_VARIANT, 0), params_magic_numbers, u"Angle2", None, *params_flattened)

    def ceil(self, number):
        """        
        Returns the smallest integer greater than or equal to the specified number.
    
        Parameters
        ==========

        number, Double, Required        
        A number.
            
        Returns
        =======

        number
        The ceiling if successful.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(766, 1, (VT_VARIANT, 0), params_magic_numbers, u"Ceil", None, *params_flattened)

    def cos_h(self, angle):
        """        
        Returns the hyperbolic cosine of the specified angle.
    
        Parameters
        ==========

        angle, Double, Required        
        An angle, measured in radians.
            
        Returns
        =======

        number
        The hyperbolic cosine of dblAngle if successful. Use ToDegrees to convert from radians to degrees.

        null
        If not successful, or on error.

        """

        params = [angle]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [angle]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(760, 1, (VT_VARIANT, 0), params_magic_numbers, u"CosH", None, *params_flattened)

    def deviation(self, numbers):
        """        
        Returns the standard deviation from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The standard deviation if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(numbers)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(773, 1, (VT_VARIANT, 0), params_magic_numbers, u"Deviation", None, *params_flattened)

    def distance(self, point1, point2, point_array):
        """        
        Measures the distance between two 3-D points, or between a 3-D point and an array of 3-D points.
    
        Parameters
        ==========

        point1, Array of ????, Required        
        The first 3-D point.
            
        point2, Array of ????, Required        
        The second 3-D point.
            
        point_array, Array of ????, Required        
        An array of 3-D points.
            
        Returns
        =======

        number
        If arrPoint1 and arrPoint2 are specified, then the distance is successful.

        array
        If arrPoint1 and arrPointArray are specified, then an array of distances if successful.

        null
        If not successful, or on error.

        """

        params = [point1, point2, point_array]
        params_opt_or_req = [Required, Required, Required]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(point1), flatten(point2), flatten(point_array)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(118, 1, (VT_VARIANT, 0), params_magic_numbers, u"Distance", None, *params_flattened)

    def e):
        """        
        Returns the value of the base of the natural system of logarithms (e).
    
        No parameters

        Returns
        =======

        number
        2.71828182845904523536028747135

        """

        params = []
        params_opt_or_req = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(774, 1, (VT_VARIANT, 0), params_magic_numbers, u"E", None, *params_flattened)

    def floor(self, number):
        """        
        Returns the largest integer less than or equal to the specified number.
    
        Parameters
        ==========

        number, Double, Required        
        A number.
            
        Returns
        =======

        number
        The floor if successful.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(767, 1, (VT_VARIANT, 0), params_magic_numbers, u"Floor", None, *params_flattened)

    def hypot(self, number_x, number_y):
        """        
        Calculates the length of the hypotenuse of a right triangle, given the length of the two sides x and y (in other words, the square root of x2 + y2).
    
        Parameters
        ==========

        number_x, Double, Required        
        The x value.
            
        number_y, Double, Required        
        The y value.
            
        Returns
        =======

        number
        The length of the hypotenuse if successful.

        null
        If not successful, or on error.

        """

        params = [number_x, number_y]
        params_opt_or_req = [Required, Required]
        params_magic_numbers = [(VT_R8, 1), (VT_R8, 1)]
        params_flattened = [number_x, number_y]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(765, 1, (VT_VARIANT, 0), params_magic_numbers, u"Hypot", None, *params_flattened)

    def log10(self, number):
        """        
        Returns the base-10 logarithm of a number.
    
        Parameters
        ==========

        number, Double, Required        
        The positive real number for which you want the base-10 logarithm.
            
        Returns
        =======

        number
        The base-10 logarithm of the number if successful.

        null
        If not successful, or on error.

        """

        params = [number]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(777, 1, (VT_VARIANT, 0), params_magic_numbers, u"Log10", None, *params_flattened)

    def max(self, numbers):
        """        
        Returns the maximum number from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The maximum number if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(numbers)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(768, 1, (VT_VARIANT, 0), params_magic_numbers, u"Max", None, *params_flattened)

    def mean(self, numbers):
        """        
        Returns the mean number, or average, from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The mean number if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(numbers)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(771, 1, (VT_VARIANT, 0), params_magic_numbers, u"Mean", None, *params_flattened)

    def median(self, numbers):
        """        
        Returns the median value from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The median value if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(numbers)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(772, 1, (VT_VARIANT, 0), params_magic_numbers, u"Median", None, *params_flattened)

    def min(self, numbers):
        """        
        Returns the minimum number from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The minimum number if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(numbers)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(769, 1, (VT_VARIANT, 0), params_magic_numbers, u"Min", None, *params_flattened)

    def p_i):
        """        
        Returns the ratio of the circumference of a circle to its diameter, approximately 3.141592653589793238462643.
    
        No parameters

        Returns
        =======

        number
        3.141592653589793238462643

        """

        params = []
        params_opt_or_req = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(663, 1, (VT_VARIANT, 0), params_magic_numbers, u"PI", None, *params_flattened)

    def polar(self, point, angle, distance, plane=None):
        """        
        Returns the 3-D point that is a specified angle and distance from a 3-D point.
    
        Parameters
        ==========

        point, Array of ????, Required        
        The 3-D point to transform.
            
        angle, Double, Required        
        The angle in degrees.
            
        distance, Double, Required        
        The distance.
            
        plane, Array of ????, Optional        
        The plane to base the transformation. Of omitted, the world x-y plane is used. The elements of a plane array are as follows:
		0
		Required.  The plane's origin (3-D point).
		1
		Required.  The plane's X axis direction (3-D vector).
		2
		Required.  The plane's Y axis direction (3-D vector).
		3
            
        Returns
        =======

        array
        The resulting 3-D point if successful.

        null
        On error.

        """

        params = [point, angle, distance, plane]
        params_opt_or_req = [Required, Required, Required, Optional]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_R8, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(point), angle, distance, flatten(plane)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(662, 1, (VT_VARIANT, 0), params_magic_numbers, u"Polar", None, *params_flattened)

    def sin_h(self, angle):
        """        
        Returns the hyperbolic sine of the specified angle.
    
        Parameters
        ==========

        angle, Double, Required        
        An angle, measured in radians.
            
        Returns
        =======

        number
        The hyperbolic sine of dblAngle if successful. Use ToDegrees to convert from radians to degrees.

        null
        If not successful, or on error.

        """

        params = [angle]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [angle]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(759, 1, (VT_VARIANT, 0), params_magic_numbers, u"SinH", None, *params_flattened)

    def sum(self, numbers):
        """        
        Returns the sum of an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numbers to sum.
            
        Returns
        =======

        number
        The sum of the array if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(numbers)]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(770, 1, (VT_VARIANT, 0), params_magic_numbers, u"Sum", None, *params_flattened)

    def tan_h(self, angle):
        """        
        Returns the hyperbolic tangent of the specified angle.
    
        Parameters
        ==========

        angle, Double, Required        
        An angle, measured in radians.
            
        Returns
        =======

        number
        The hyperbolic tangent of dblAngle if successful. Use ToDegrees to convert from radians to degrees.

        null
        If not successful, or on error.

        """

        params = [angle]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [angle]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(761, 1, (VT_VARIANT, 0), params_magic_numbers, u"TanH", None, *params_flattened)

    def to_degrees(self, radians):
        """        
        Converts an angle specified in radians to degrees.
    
        Parameters
        ==========

        radians, Double, Required        
        The angle in radians
            
        Returns
        =======

        number
        The angle in degrees if successful.

        null
        On error.

        """

        params = [radians]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [radians]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(664, 1, (VT_VARIANT, 0), params_magic_numbers, u"ToDegrees", None, *params_flattened)

    def to_radians(self, degrees):
        """        
        Converts an angle specified in degrees to radians.
    
        Parameters
        ==========

        degrees, Double, Required        
        The angle in degrees
            
        Returns
        =======

        number
        The angle in radians if successful.

        null
        On error.

        """

        params = [degrees]
        params_opt_or_req = [Required]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [degrees]

        for i in range(len(params)):
            if (params[i] == None) and (params_opt_or_req[i] = "Optional"):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        return self._ApplyTypes_(665, 1, (VT_VARIANT, 0), params_magic_numbers, u"ToRadians", None, *params_flattened)

