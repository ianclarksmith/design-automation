# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Utility(DispatchBaseClass):



    def all_procedures(self, bln_all):
        """

        Returns the names of the  user-defined subroutines and functions resident in RhinoScript's VBScript engine.

        Parameters

        blnAll : Optional, Boolean, If True (default) the names of all user-defined subroutines and functions are returned

        Returns

        Array : An array of string identifying the names of user-defined procedures.
        Null : If no user-defined procedures are found.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AllProcedures', None, blnAll)

    def clipboard_text(self, str_text):
        """

        Returns or sets a text string to the Windows clipboard.

        Parameters

        strText : Optional, String, A text string

        Returns

        String : If strText is not specified, the current text string from the Windows clipboard if successful.
        String : If strText is specified, the previous text string from the Windows clipboard if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ClipboardText', None, strText)

    def color_adjust_luma(self, lng_r_g_b, int_luma, b_scale):
        """

        Changes the luminance of a red-green-blue (RGB) value. Hue and saturation are not affected.

        Parameters

        lngRGB : Required, Number, The initial RGB color value
        intLuma : Required, Number, The luminance in units of 0
        bScale : Optional, Boolean, If bScale is set to True, intLuma specifies how much to increment or decrement the current luminance

        Returns

        Number : The modified RGB color value if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ColorAdjustLuma', None, lngRGB, intLuma, bScale)

    def color_blue_value(self, lng_r_g_b):
        """

        Retrieves an intensity value for the blue component of a red-green-blue (RGB) value.

        Parameters

        lngRGB : Required, Number, The RGB color value

        Returns

        Number : The blue component if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ColorBlueValue', None, lngRGB)

    def color_green_value(self, lng_r_g_b):
        """

        Retrieves an intensity value for the green component of a red-green-blue (RGB) value.

        Parameters

        lngRGB : Required, Number, The RGB color value

        Returns

        Number : The green component if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ColorGreenValue', None, lngRGB)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def color_r_g_b_to_h_l_s(self, lng_r_g_b):
        """

        Converts colors from red-green-blue (RGB) to hue-luminance-saturation (HLS) format.

        Parameters

        lngRGB : Required, Number, The RGB color value

        Returns

        Array : An array containing the hue, luminance, and saturation values if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ColorRGBToHLS', None, lngRGB)

    def color_red_value(self, lng_r_g_b):
        """

        Retrieves an intensity value for the red component of a red-green-blue (RGB) value.

        Parameters

        lngRGB : Required, Number, The RGB color value

        Returns

        Number : The red component if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ColorRedValue', None, lngRGB)

    def cull_duplicate_numbers(self, arr_numbers, dbl_tolerance):
        """

        Removes duplicates from an array of numbers.

        Parameters

        arrNumbers : Required, Array, An array of numbers
        dblTolerance : Optional, Number, The minimum distance between numbers

        Returns

        Array : An array of numbers with duplicates removed if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CullDuplicateNumbers', None, arrNumbers, dblTolerance)

    def cull_duplicate_points(self, arr_points, dbl_tolerance):
        """

        Removes duplicates from an array of 3-D points.

        Parameters

        arrPoints : Required, Array, An array of 3-D points
        dblTolerance : Optional, Number, The minimum distance between points

        Returns

        Array : An array of 3-D points with duplicates removed if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CullDuplicatePoints', None, arrPoints, dblTolerance)

    def cull_duplicate_strings(self, arr_strings, bln_case_sensitive):
        """

        Removes duplicates from an array of strings.

        Parameters

        arrStrings : Required, Array, An array of numbers
        blnCaseSensitive : Optional, Boolean, Use case sensitivity when culling

        Returns

        Array : An array of strings with duplicates removed if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CullDuplicateStrings', None, arrStrings, blnCaseSensitive)

    def current_printer(self, str_printer):
        """

        Returns or changes the current Windows printer.

        Parameters

        strPrinter : Optional, String, The name of a Windows printer as returned by this method or by the PrinterNames method

        Returns

        String : If strPrinter is not specified, the name of the current Windows printer if successful.
        String : If strPrinter is specified, the name of the previously current Windows printer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CurrentPrinter', None, strPrinter)

    def get_settings(self, str_filename, str_section, str_entry):
        """

        ...

        Parameters

        strFilename : Required, String, The name of the initialization file
        strSection : Optional, String, The section containing the entry
        strEntry : Optional, String, The entry whose associated string is to be returned

        Returns

        Array : If strSection is not specified, a zero-based, one-dimensional array containing all section names from strFilename if successful.
        Array : If strEntry is not specified, a zero-based, one-dimensional array containing all entry names within strSection if successful.
        String : If strSection and strEntry are returned, the value of strEntry if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetSettings', None, strFilename, strSection, strEntry)

    def is_procedure(self, str_sub_name):
        """

        Verifies that a user-defined subroutine or function is resident in RhinoScript's VBScript engine.

        Parameters

        strSubName : Required, String, The name of a user-defined subroutine of function

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsProcedure', None, strSubName)

    def join_arrays(self, arr1, arr2):
        """

        Joins two one-dimensional arrays in to a single one-dimensional array.

        Parameters

        arr1 : Required, Array, The first one-dimensional array
        arr2 : Required, Array, The second one-dimensional array

        Returns

        Array : A one-dimensional array containing the elements of both input arrays if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'JoinArrays', None, arr1, arr2)

        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def printer_names(self):
        """

        Returns the name of all installed Windows printer.

        No parameters

        Returns

        Array : An array of Windows printer names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PrinterNames', None, )

    def pt2_str(self, arr_point, n_precision, bln_space):
        """

        Converts a 3-D point value to a string.  Useful for display point values as output, or passing point values to Rhino commands.

        Parameters

        arrPoint : Required, Array, A 3-D point
        nPrecision : Optional, Number, The display precision of the point coordinates
        blnSpace : Optional, Boolean, Append an additional trailing space after the point string

        Returns

        String : The formatted string if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Pt2Str', None, arrPoint, nPrecision, blnSpace)

    def save_settings(self, str_filename, str_section, str_entry, str_string):
        """

        ...

        Parameters

        strFilename : Required, String, The name of the initialization file
        strSection : Optional, String, The section to which strString will be copied
        strEntry : Optional, String, The name of the entry to be associated with strString
        strString : Optional, String, The string to be written to the file

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SaveSettings', None, strFilename, strSection, strEntry, strString)

    def simplify_array(self, arr_points):
        """

        Flattens an array of 3-D points into a one-dimensional array of real number. For example, if you had an array containing three 3-D points, this method would return a one-dimensional array containing nine real numbers.

        Parameters

        arrPoints : Required, Array, An array of 3-D points

        Returns

        Array : A one-dimensional array containing real numbers, if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SimplifyArray', None, arrPoints)

    def sleep(self, lng_milliseconds):
        """

        Suspends the execution of a running script for the specified interval.

        Parameters

        lngMilliseconds : Required, Number, The duration in milliseconds

        Returns

        Null : If successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Sleep', None, lngMilliseconds)

    def sort(self, arr_strings, bln_ascending, bln_no_case):
        """

        Sorts an array of strings.

        Parameters

        arrStrings : Required, Array, An array of string values
        blnAscending : Optional, Boolean, The sorting mode, either ascending or descending
        blnNoCase : Optional, Boolean, The case sensitivity mode

        Returns

        Array : An array sorted strings if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Sort', None, arrStrings, blnAscending, blnNoCase)

    def sort_numbers(self, arr_numbers, bln_ascending):
        """

        Sorts an array of numbers.

        Parameters

        arrNumbers : Required, Array, An array of numeric values
        blnAscending : Optional, Boolean, The sorting mode, either ascending or descending

        Returns

        Array : An array of sorted numbers if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SortNumbers', None, arrNumbers, blnAscending)

    def sort_point_list(self, arr_points, dbl_tolerance):
        """

        Sorts an array of 3-D points so they will be connected in "reasonable" polyline order.

        Parameters

        arrPoints : Required, Array, An array of 3-D points
        dblTolerance : Optional, Number, The minimum distance between points

        Returns

        Array : An array of sorted 3-D points  if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SortPointList', None, arrPoints, dblTolerance)

    def sort_points(self, arr_points, bln_ascending, bln_order):
        """

        Sorts an array of 3-D points.

        Parameters

        arrPoints : Required, Array, An array of 3-D points
        blnAscending : Optional, Boolean, The sorting mode, either ascending or descending
        blnOrder : Optional, Number, The component sort order, where:

        Returns

        Array : An array of sorted 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SortPoints', None, arrPoints, blnAscending, blnOrder)

    def spool_to_printer(self, str_file, str_printer):
        """

        Spools, or sends, a text file or a print/plot file to a Windows printer.

        Parameters

        strFile : Required, String, The full path to the file to spool
        strPrinter : Required, String, The name of a Windows printer as returned by either the CurrentPrinter or by the PrinterNames method

        Returns

        String : The name of the spooled file if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SpoolToPrinter', None, strFile, strPrinter)

    def str2_pt(self, arr_point):
        """

        Converts a formatted string value into a 3-D point value.

        Parameters

        arrPoint : Required, String, A string that contains a delimited point like "1,2,3"

        Returns

        Array : A 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Str2Pt', None, arrPoint)

    def str2_pt_array(self, str_points):
        """

        Converts a formatted string value into an array of 3-D point value.

        Parameters

        strPoints : Required, String, A string that contains an unknown number of space delimited points like "1,2,3 4,5,6 7,8,9"

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Str2PtArray', None, strPoints)

    def strtok(self, str_text, str_delimiters):
        """

        Returns the tokens in a string.  Use this method as an alternative to the VBScript's Split function.

        Parameters

        strText : Required, String, A string containing token(s)
        strDelimiters : Optional, String, A set of delimiter characters

        Returns

        Array : A zero-based, one-dimensional array containing the string tokens if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Strtok', None, strText, strDelimiters)

    def text_out(self, str_text, str_title):
        """

        Displays a text output window.

        Parameters

        strText : Required, String, A text string to display
        strTitle : Optional, String, A dialog box title

        Returns

        Null : If successful or on failure.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'TextOut', None, strText, strTitle)

    def version(self):
        """

        Returns the version of RhinoScript.

        No parameters

        Returns

        Number : The version number.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'Version', None, )

