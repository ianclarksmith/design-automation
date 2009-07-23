# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Math(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def angle(self, point1, point2, world=None):
        """        
        Measures the angle between two points.
    
        Parameters
        ==========

        point1, Array of Doubles, Required        
        The first 3-D point.
            
        point2, Array of Doubles, Required        
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
        required = [True, True, False]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(point1), flatten_params(point2), world]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(115, 1, (VT_VARIANT, 0), magic, u"Angle", None, *flattened)

    def angle2(self, point1, point2):
        """        
        Measures the angle between two lines.
    
        Parameters
        ==========

        point1, Array of Doubles, Required        
        An array containing the starting and ending 3-D points of the first line.
            
        point2, Array of Doubles, Required        
        An array containing the starting and ending 3-D points of the second line.
            
        Returns
        =======

        array
        An array containing the following elements if successful.

        null
        If not successful, or on error.

        """

        params = [point1, point2]
        required = [True, True]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(point1), flatten_params(point2)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(116, 1, (VT_VARIANT, 0), magic, u"Angle2", None, *flattened)

    def deviation(self, numbers):
        """        
        Returns the standard deviation from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of Integers, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The standard deviation if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        required = [True]
        magic = [(VT_ARRAY + VT_I2, 1),]
        flattened = [flatten_params(numbers)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(773, 1, (VT_VARIANT, 0), magic, u"Deviation", None, *flattened)

    def distance(self, point1, point2):
        """        
        Measures the distance between two 3-D points, or between a 3-D point and an array of 3-D points.
    
        Parameters
        ==========

        point1, Array of ???, Required        
        The first 3-D point.
            
        point2, Array of ???, Required        
        The second 3-D point.
            
        Returns
        =======

        number
        If arrPoint1 and arrPoint2 are specified, then the distance is successful.

        array
        If arrPoint1 and arrPointArray are specified, then an array of distances if successful.

        null
        If not successful, or on error.

        """

        params = [point1, point2]
        required = [True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(point1), flatten_params(point2)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(118, 1, (VT_VARIANT, 0), magic, u"Distance", None, *flattened)

    def distance_2(self, point1, point_array):
        """        
        Measures the distance between two 3-D points, or between a 3-D point and an array of 3-D points.
    
        Parameters
        ==========

        point1, Array of ???, Required        
        The first 3-D point.
            
        point_array, Array of ???, Required        
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

        params = [point1, point_array]
        required = [True, True]
        magic = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        flattened = [flatten_params(point1), flatten_params(point_array)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(118, 1, (VT_VARIANT, 0), magic, u"Distance", None, *flattened)

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
        required = [True, True]
        magic = [(VT_R8, 1), (VT_R8, 1)]
        flattened = [number_x, number_y]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(765, 1, (VT_VARIANT, 0), magic, u"Hypot", None, *flattened)

    def max(self, numbers):
        """        
        Returns the maximum number from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of Integers, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The maximum number if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        required = [True]
        magic = [(VT_ARRAY + VT_I2, 1),]
        flattened = [flatten_params(numbers)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(768, 1, (VT_VARIANT, 0), magic, u"Max", None, *flattened)

    def mean(self, numbers):
        """        
        Returns the mean number, or average, from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of Integers, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The mean number if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        required = [True]
        magic = [(VT_ARRAY + VT_I2, 1),]
        flattened = [flatten_params(numbers)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(771, 1, (VT_VARIANT, 0), magic, u"Mean", None, *flattened)

    def median(self, numbers):
        """        
        Returns the median value from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of Integers, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The median value if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        required = [True]
        magic = [(VT_ARRAY + VT_I2, 1),]
        flattened = [flatten_params(numbers)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(772, 1, (VT_VARIANT, 0), magic, u"Median", None, *flattened)

    def min(self, numbers):
        """        
        Returns the minimum number from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of Integers, Required        
        An array of numbers to analyze.
            
        Returns
        =======

        number
        The minimum number if successful.

        null
        If not successful, or on error.

        """

        params = [numbers]
        required = [True]
        magic = [(VT_ARRAY + VT_I2, 1),]
        flattened = [flatten_params(numbers)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(769, 1, (VT_VARIANT, 0), magic, u"Min", None, *flattened)

    def polar(self, point, angle, distance, plane=None):
        """        
        Returns the 3-D point that is a specified angle and distance from a 3-D point.
    
        Parameters
        ==========

        point, Array of Doubles, Required        
        The 3-D point to transform.
            
        angle, Double, Required        
        The angle in degrees.
            
        distance, Double, Required        
        The distance.
            
        plane, Array of Doubles, Optional        
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
        required = [True, True, True, False]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_R8, 1), (VT_R8, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [flatten_params(point), angle, distance, flatten_params(plane)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(662, 1, (VT_VARIANT, 0), magic, u"Polar", None, *flattened)

