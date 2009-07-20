# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Utility(IRhinoScript):



    def all_procedures(self, all):
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

        return self._ApplyTypes_(503, 1, (VT_VARIANT, 0), ((VT_BOOL, 1),), u"AllProcedures", None, all)

    def clipboard_text(self, text):
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

        return self._ApplyTypes_(245, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"ClipboardText", None, text)

    def color_adjust_luma(self, r_g_b, luma, b_scale):
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

        return self._ApplyTypes_(878, 1, (VT_VARIANT, 0), ((VT_I4, 1), (VT_I2, 1), (VT_I2, 1)), u"ColorAdjustLuma", None, r_g_b, luma, b_scale)

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

        return self._ApplyTypes_(882, 1, (VT_VARIANT, 0), ((VT_I4, 1),), u"ColorBlueValue", None, r_g_b)

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

        return self._ApplyTypes_(881, 1, (VT_VARIANT, 0), ((VT_I4, 1),), u"ColorGreenValue", None, r_g_b)

    def color_h_l_s_to_r_g_b(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

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

        return self._ApplyTypes_(876, 1, (VT_VARIANT, 0), ((VT_I4, 1),), u"ColorRGBToHLS", None, r_g_b)

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

        return self._ApplyTypes_(880, 1, (VT_VARIANT, 0), ((VT_I4, 1),), u"ColorRedValue", None, r_g_b)

    def cull_duplicate_numbers(self, numbers, tolerance):
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

        return self._ApplyTypes_(550, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"CullDuplicateNumbers", None, flatten(numbers), tolerance)

    def cull_duplicate_points(self, points, tolerance):
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

        return self._ApplyTypes_(548, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"CullDuplicatePoints", None, flatten(points), tolerance)

    def cull_duplicate_strings(self, strings, case_sensitive):
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

        return self._ApplyTypes_(549, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BOOL, 1)), u"CullDuplicateStrings", None, flatten(strings), case_sensitive)

    def current_printer(self, printer):
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

        return self._ApplyTypes_(358, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"CurrentPrinter", None, printer)

    def get_settings(self, filename, section, entry):
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

        return self._ApplyTypes_(246, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"GetSettings", None, filename, section, entry)

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

        return self._ApplyTypes_(287, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsProcedure", None, sub_name)

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

        return self._ApplyTypes_(547, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1)), u"JoinArrays", None, flatten(1), flatten(2))

    def make_array(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def printer_names(self):
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

        return self._ApplyTypes_(356, 1, (VT_VARIANT, 0), (), u"PrinterNames", None, )

    def pt2_str(self, point, precision, space):
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

        return self._ApplyTypes_(297, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_I2, 1), (VT_BOOL, 1)), u"Pt2Str", None, flatten(point), precision, space)

    def save_settings(self, filename, section, entry, string):
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

        return self._ApplyTypes_(247, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"SaveSettings", None, filename, section, entry, string)

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

        return self._ApplyTypes_(597, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1),), u"SimplifyArray", None, flatten(points))

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

        return self._ApplyTypes_(248, 1, (VT_VARIANT, 0), ((VT_I4, 1),), u"Sleep", None, milliseconds)

    def sort_numbers(self, numbers, ascending):
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

        return self._ApplyTypes_(552, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BOOL, 1)), u"SortNumbers", None, flatten(numbers), ascending)

    def sort_point_list(self, points, tolerance):
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

        return self._ApplyTypes_(644, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1)), u"SortPointList", None, flatten(points), tolerance)

    def sort_points(self, points, ascending, order):
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

        return self._ApplyTypes_(551, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"SortPoints", None, flatten(points), ascending, order)

    def sort_strings(self, strings, ascending, no_case):
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

        return self._ApplyTypes_(640, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"SortStrings", None, flatten(strings), ascending, no_case)

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

        return self._ApplyTypes_(357, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"SpoolToPrinter", None, file, printer)

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

        return self._ApplyTypes_(409, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"Str2Pt", None, point)

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

        return self._ApplyTypes_(410, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"Str2PtArray", None, points)

    def strtok(self, text, delimiters):
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

        return self._ApplyTypes_(250, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"Strtok", None, text, delimiters)

    def text_out(self, text, title):
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

        return self._ApplyTypes_(755, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"TextOut", None, text, title)

    def version(self):
        """        
        Returns the version of RhinoScript.
    
        No parameters

        Returns
        =======

        number
        The version number.

        """

        return self._ApplyTypes_(288, 1, (VT_VARIANT, 0), (), u"Version", None, )

