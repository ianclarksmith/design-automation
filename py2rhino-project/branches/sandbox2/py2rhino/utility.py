# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Utility(IRhinoScript):



    def all_procedures(self, all=None):
        """        
        Returns the names of the  user-defined subroutines and functions resident in RhinoScript's VBScript engine.
    
        Parameters
        ==========

        all, Boolean, Optional        
        If True (default) the names of all user-defined subroutines and functions are returned. If False, only top-level subroutines are returned. Top level subroutines are subroutines that can be passed to the RunScript command.
            
        Returns
        =======

        array
        An array of string identifying the names of user-defined procedures.

        null
        If no user-defined procedures are found.

        """

        params = [all]
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [all]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(503, 1, (VT_VARIANT, 0), params_magic_numbers, u"AllProcedures", None, *params_flattened)

    def clipboard_text(self, text=None):
        """        
        Returns or sets a text string to the Windows clipboard.
    
        Parameters
        ==========

        text, String, Optional        
        A text string.
            
        Returns
        =======

        string
        If strText is not specified, the current text string from the Windows clipboard if successful.

        string
        If strText is specified, the previous text string from the Windows clipboard if successful.

        null
        If not successful or on error.

        """

        params = [text]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [text]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(245, 1, (VT_VARIANT, 0), params_magic_numbers, u"ClipboardText", None, *params_flattened)

    def color_adjust_luma(self, r_g_b, luma, b_scale=None):
        """        
        Changes the luminance of a red-green-blue (RGB) value. Hue and saturation are not affected.
    
        Parameters
        ==========

        r_g_b, Integer, Required        
        The initial RGB color value.
            
        luma, Integer, Required        
        The luminance in units of 0.1 percent of the total range.  For example, a value of intLuma = 50 corresponds to 5 percent of the maximum luminance.
            
        b_scale, Integer, Optional        
        If bScale is set to True, intLuma specifies how much to increment or decrement the current luminance.  If bScale is set to FALSE, intLuma specifies the absolute luminance.  The default value is False.
		If bScale is set to TRUE, intLuma can range from -1000 to +1000.
            
        Returns
        =======

        number
        The modified RGB color value if successful.

        null
        If not successful or on error.

        """

        params = [r_g_b, luma, b_scale]
        params_required = [True, True, False]
        params_magic_numbers = [(VT_I4, 1), (VT_I2, 1), (VT_I2, 1)]
        params_flattened = [r_g_b, luma, b_scale]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(878, 1, (VT_VARIANT, 0), params_magic_numbers, u"ColorAdjustLuma", None, *params_flattened)

    def color_blue_value(self, r_g_b):
        """        
        Retrieves an intensity value for the blue component of a red-green-blue (RGB) value.
    
        Parameters
        ==========

        r_g_b, Integer, Required        
        The RGB color value.
            
        Returns
        =======

        number
        The blue component if successful.

        null
        If not successful or on error.

        """

        params = [r_g_b]
        params_required = [True]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [r_g_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(882, 1, (VT_VARIANT, 0), params_magic_numbers, u"ColorBlueValue", None, *params_flattened)

    def color_green_value(self, r_g_b):
        """        
        Retrieves an intensity value for the green component of a red-green-blue (RGB) value.
    
        Parameters
        ==========

        r_g_b, Integer, Required        
        The RGB color value.
            
        Returns
        =======

        number
        The green component if successful.

        null
        If not successful or on error.

        """

        params = [r_g_b]
        params_required = [True]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [r_g_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(881, 1, (VT_VARIANT, 0), params_magic_numbers, u"ColorGreenValue", None, *params_flattened)

    def color_h_l_s_to_r_g_b(self, r_g_b):
        """        
        Converts colors from hue-luminance-saturation (HLS) to red-green-blue format.
    
        Parameters
        ==========

        r_g_b, Integer, Required        
        The HLS color value.
            
        Returns
        =======

        number
        The RGB color value if successful.

        null
        If not successful or on error.

        """

        params = [r_g_b]
        params_required = [True]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [r_g_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(877, 1, (VT_VARIANT, 0), params_magic_numbers, u"ColorHLSToRGB", None, *params_flattened)

    def color_r_g_b_to_h_l_s(self, r_g_b):
        """        
        Converts colors from red-green-blue (RGB) to hue-luminance-saturation (HLS) format.
    
        Parameters
        ==========

        r_g_b, Integer, Required        
        The RGB color value.
            
        Returns
        =======

        array
        An array containing the hue, luminance, and saturation values if successful.

        null
        If not successful or on error.

        """

        params = [r_g_b]
        params_required = [True]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [r_g_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(876, 1, (VT_VARIANT, 0), params_magic_numbers, u"ColorRGBToHLS", None, *params_flattened)

    def color_red_value(self, r_g_b):
        """        
        Retrieves an intensity value for the red component of a red-green-blue (RGB) value.
    
        Parameters
        ==========

        r_g_b, Integer, Required        
        The RGB color value.
            
        Returns
        =======

        number
        The red component if successful.

        null
        If not successful or on error.

        """

        params = [r_g_b]
        params_required = [True]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [r_g_b]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(880, 1, (VT_VARIANT, 0), params_magic_numbers, u"ColorRedValue", None, *params_flattened)

    def cull_duplicate_numbers(self, numbers, tolerance=None):
        """        
        Removes duplicates from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numbers.
            
        tolerance, Double, Optional        
        The minimum distance between numbers.  Numbers that fall within this tolerance will be discarded.  If omitted, Rhino's internal zero tolerance is used.
            
        Returns
        =======

        array
        An array of numbers with duplicates removed if successful.

        null
        If not successful or on error.

        """

        params = [numbers, tolerance]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(numbers), tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(550, 1, (VT_VARIANT, 0), params_magic_numbers, u"CullDuplicateNumbers", None, *params_flattened)

    def cull_duplicate_points(self, points, tolerance=None):
        """        
        Removes duplicates from an array of 3-D points.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        tolerance, Double, Optional        
        The minimum distance between points.  Points that fall within this tolerance will be discarded.  If omitted, Rhino's internal zero tolerance is used.
            
        Returns
        =======

        array
        An array of 3-D points with duplicates removed if successful.

        null
        If not successful or on error.

        """

        params = [points, tolerance]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(points), tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(548, 1, (VT_VARIANT, 0), params_magic_numbers, u"CullDuplicatePoints", None, *params_flattened)

    def cull_duplicate_strings(self, strings, case_sensitive=None):
        """        
        Removes duplicates from an array of strings.
    
        Parameters
        ==========

        strings, Array of ????, Required        
        An array of numbers.
            
        case_sensitive, Boolean, Optional        
        Use case sensitivity when culling.  The default is to cull with case sensitivity (True).
            
        Returns
        =======

        array
        An array of strings with duplicates removed if successful.

        null
        If not successful or on error.

        """

        params = [strings, case_sensitive]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(strings), case_sensitive]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(549, 1, (VT_VARIANT, 0), params_magic_numbers, u"CullDuplicateStrings", None, *params_flattened)

    def current_printer(self, printer=None):
        """        
        Returns or changes the current Windows printer.
    
        Parameters
        ==========

        printer, String, Optional        
        The name of a Windows printer as returned by this method or by the PrinterNames method.
            
        Returns
        =======

        string
        If strPrinter is not specified, the name of the current Windows printer if successful.

        string
        If strPrinter is specified, the name of the previously current Windows printer if successful.

        null
        If not successful, or on error.

        """

        params = [printer]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [printer]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(358, 1, (VT_VARIANT, 0), params_magic_numbers, u"CurrentPrinter", None, *params_flattened)

    def get_settings(self, filename, section=None, entry=None):
        """        
        Returns a string from a specified section in a Windows-style initialization file.  The initialization file must have the following form:
		[Section]
		Entry = String
		...
    
        Parameters
        ==========

        filename, String, Required        
        The name of the initialization file.
            
        section, String, Optional        
        The section containing the entry.
            
        entry, String, Optional        
        The entry whose associated string is to be returned.
            
        Returns
        =======

        array
        If strSection is not specified, a zero-based, one-dimensional array containing all section names from strFilename if successful.

        array
        If strEntry is not specified, a zero-based, one-dimensional array containing all entry names within strSection if successful.

        string
        If strSection and strEntry are returned, the value of strEntry if successful.

        null
        If not successful, or on error.

        """

        params = [filename, section, entry]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [filename, section, entry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(246, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetSettings", None, *params_flattened)

    def is_procedure(self, sub_name):
        """        
        Verifies that a user-defined subroutine or function is resident in RhinoScript's VBScript engine.
    
        Parameters
        ==========

        sub_name, String, Required        
        The name of a user-defined subroutine of function.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [sub_name]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [sub_name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(287, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsProcedure", None, *params_flattened)

    def join_arrays(self, 1, 2):
        """        
        Joins two one-dimensional arrays in to a single one-dimensional array.
    
        Parameters
        ==========

        1, Array of ????, Required        
        The first one-dimensional array.
            
        2, Array of ????, Required        
        The second one-dimensional array.
            
        Returns
        =======

        array
        A one-dimensional array containing the elements of both input arrays if successful.

        null
        If not successful or on error.

        """

        params = [1, 2]
        params_required = [True, True]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [flatten(1), flatten(2)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(547, 1, (VT_VARIANT, 0), params_magic_numbers, u"JoinArrays", None, *params_flattened)

    def make_array(self, upper_bound, v_variant=None):
        """        
        Creates a new, initialized one-dimensional array of a user-specified bounds.
    
        Parameters
        ==========

        upper_bound, Integer, Required        
        The upper bounds of the new array.
            
        v_variant, Integer, Optional        
        The value to initialize every array element.  If omitted, every array element will be initialized as Empty.  Note, the Empty VBScript keyword is used to indicate an uninitialized variable value.  This is not the same thing as Null.
            
        Returns
        =======

        array
        The one-dimensional array if successful.

        null
        If not successful or on error.

        """

        params = [upper_bound, v_variant]
        params_required = [True, False]
        params_magic_numbers = [(VT_I2, 1), (VT_I2, 1)]
        params_flattened = [upper_bound, v_variant]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(875, 1, (VT_VARIANT, 0), params_magic_numbers, u"MakeArray", None, *params_flattened)

    def printer_names():
        """        
        Returns the name of all installed Windows printer.
    
        No parameters

        Returns
        =======

        array
        An array of Windows printer names if successful.

        null
        If not successful, or on error.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(356, 1, (VT_VARIANT, 0), params_magic_numbers, u"PrinterNames", None, *params_flattened)

    def pt2_str(self, point, precision=None, space=None):
        """        
        Converts a 3-D point value to a string.  Useful for display point values as output, or passing point values to Rhino commands.
    
        Parameters
        ==========

        point, Array of ????, Required        
        A 3-D point.
            
        precision, Integer, Optional        
        The display precision of the point coordinates.  The default is to display the precision defined by the display precision setting that is found on the Units page of the DocumentProperties command.
            
        space, Boolean, Optional        
        Append an additional trailing space after the point string.  The default value is not to append the additional space (False).
            
        Returns
        =======

        string
        The formatted string if successful.

        null
        On error.

        """

        params = [point, precision, space]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(point), precision, space]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(297, 1, (VT_VARIANT, 0), params_magic_numbers, u"Pt2Str", None, *params_flattened)

    def save_settings(self, filename, section=None, entry=None, string=None):
        """        
        Saves a string to a specified section in a Windows-style initialization file.  The initialization file must have the following form:
		[Section]
		Entry = String
		...
    
        Parameters
        ==========

        filename, String, Required        
        The name of the initialization file.  If strFilename does not exist, the file will be created.  The specified directory must already exist.
            
        section, String, Optional        
        The section to which strString will be copied.  If strSection does not exist, it is created.
            
        entry, String, Optional        
        The name of the entry to be associated with strString.  If strEntry does not exist in the specified section, it is created.  If strEntry is nil, the entire section, including all entries within the section, is deleted.
            
        string, String, Optional        
        The string to be written to the file.  If omitted, the entry pointed to by strEntry is deleted.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [filename, section, entry, string]
        params_required = [True, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [filename, section, entry, string]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(247, 1, (VT_VARIANT, 0), params_magic_numbers, u"SaveSettings", None, *params_flattened)

    def simplify_array(self, points):
        """        
        Flattens an array of 3-D points into a one-dimensional array of real number. For example, if you had an array containing three 3-D points, this method would return a one-dimensional array containing nine real numbers.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        Returns
        =======

        array
        A one-dimensional array containing real numbers, if successful.

        null
        If not successful or on error.

        """

        params = [points]
        params_required = [True]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(points)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(597, 1, (VT_VARIANT, 0), params_magic_numbers, u"SimplifyArray", None, *params_flattened)

    def sleep(self, milliseconds):
        """        
        Suspends the execution of a running script for the specified interval.
    
        Parameters
        ==========

        milliseconds, Integer, Required        
        The duration in milliseconds.
            
        Returns
        =======

        null
        If successful, or on error.

        """

        params = [milliseconds]
        params_required = [True]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [milliseconds]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(248, 1, (VT_VARIANT, 0), params_magic_numbers, u"Sleep", None, *params_flattened)

    def sort_numbers(self, numbers, ascending=None):
        """        
        Sorts an array of numbers.
    
        Parameters
        ==========

        numbers, Array of ????, Required        
        An array of numeric values.
            
        ascending, Boolean, Optional        
        The sorting mode, either ascending or descending.  If omitted, the numbers are sorted ascending.
            
        Returns
        =======

        array
        An array of sorted numbers if successful.

        null
        If not successful, or on error.

        """

        params = [numbers, ascending]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(numbers), ascending]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(552, 1, (VT_VARIANT, 0), params_magic_numbers, u"SortNumbers", None, *params_flattened)

    def sort_point_list(self, points, tolerance=None):
        """        
        Sorts an array of 3-D points so they will be connected in "reasonable" polyline order.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        tolerance, Double, Optional        
        The minimum distance between points.  Points that fall within this tolerance will be discarded.  If omitted, Rhino's internal zero tolerance is used.
            
        Returns
        =======

        array
        An array of sorted 3-D points  if successful.

        null
        If not successful, or on error.

        """

        params = [points, tolerance]
        params_required = [True, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1)]
        params_flattened = [flatten(points), tolerance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(644, 1, (VT_VARIANT, 0), params_magic_numbers, u"SortPointList", None, *params_flattened)

    def sort_points(self, points, ascending=None, order=None):
        """        
        Sorts an array of 3-D points.
    
        Parameters
        ==========

        points, Array of ????, Required        
        An array of 3-D points.
            
        ascending, Boolean, Optional        
        The sorting mode, either ascending or descending.  If omitted, the points are sorted ascending (True).
            
        order, Boolean, Optional        
        The component sort order, where:
		Value
		Component Sort Order
		0 (default)
		X, Y, Z
		1
		X, Z, Y
		2
		Y, X, Z
		3
		Y, Z, X
		4
		Z, X, Y
		5
            
        Returns
        =======

        array
        An array of sorted 3-D points if successful.

        null
        If not successful, or on error.

        """

        params = [points, ascending, order]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(points), ascending, order]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(551, 1, (VT_VARIANT, 0), params_magic_numbers, u"SortPoints", None, *params_flattened)

    def sort_strings(self, strings, ascending=None, no_case=None):
        """        
        Sorts an array of strings.
    
        Parameters
        ==========

        strings, Array of ????, Required        
        An array of string values.
            
        ascending, Boolean, Optional        
        The sorting mode, either ascending or descending.  If omitted or True, the strings are sorted ascending.  If False, the strings are sorted descending.
            
        no_case, Boolean, Optional        
        The case sensitivity mode.  If omitted or True, a case insensitive sorting is performed.  If False, a case sensitive sorting is performed.
            
        Returns
        =======

        array
        An array sorted strings if successful.

        null
        If not successful, or on error.

        """

        params = [strings, ascending, no_case]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [flatten(strings), ascending, no_case]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(640, 1, (VT_VARIANT, 0), params_magic_numbers, u"SortStrings", None, *params_flattened)

    def spool_to_printer(self, file, printer):
        """        
        Spools, or sends, a text file or a print/plot file to a Windows printer.
    
        Parameters
        ==========

        file, String, Required        
        The full path to the file to spool
            
        printer, String, Required        
        The name of a Windows printer as returned by either the CurrentPrinter or by the PrinterNames method.
            
        Returns
        =======

        string
        The name of the spooled file if successful.

        null
        If not successful, or on error.

        """

        params = [file, printer]
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [file, printer]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(357, 1, (VT_VARIANT, 0), params_magic_numbers, u"SpoolToPrinter", None, *params_flattened)

    def str2_pt(self, point):
        """        
        Converts a formatted string value into a 3-D point value.
    
        Parameters
        ==========

        point, String, Required        
        A string that contains a delimited point like "1,2,3".
            
        Returns
        =======

        array
        A 3-D point if successful.

        null
        On error.

        """

        params = [point]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [point]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(409, 1, (VT_VARIANT, 0), params_magic_numbers, u"Str2Pt", None, *params_flattened)

    def str2_pt_array(self, points):
        """        
        Converts a formatted string value into an array of 3-D point value.
    
        Parameters
        ==========

        points, String, Required        
        A string that contains an unknown number of space delimited points like "1,2,3 4,5,6 7,8,9".
            
        Returns
        =======

        array
        An array of 3-D points if successful.

        null
        If not successful, or on error.

        """

        params = [points]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [points]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(410, 1, (VT_VARIANT, 0), params_magic_numbers, u"Str2PtArray", None, *params_flattened)

    def strtok(self, text, delimiters=None):
        """        
        Returns the tokens in a string.  Use this method as an alternative to the VBScript's Split function.
    
        Parameters
        ==========

        text, String, Required        
        A string containing token(s).
            
        delimiters, String, Optional        
        A set of delimiter characters.  If omitted, a space character (" ") is used.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array containing the string tokens if successful.

        null
        If not successful, or on error.

        """

        params = [text, delimiters]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [text, delimiters]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(250, 1, (VT_VARIANT, 0), params_magic_numbers, u"Strtok", None, *params_flattened)

    def text_out(self, text, title=None):
        """        
        Displays a text output window.
    
        Parameters
        ==========

        text, String, Required        
        A text string to display.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        null
        If successful or on failure.

        """

        params = [text, title]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [text, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(755, 1, (VT_VARIANT, 0), params_magic_numbers, u"TextOut", None, *params_flattened)

    def version():
        """        
        Returns the version of RhinoScript.
    
        No parameters

        Returns
        =======

        number
        The version number.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(288, 1, (VT_VARIANT, 0), params_magic_numbers, u"Version", None, *params_flattened)

