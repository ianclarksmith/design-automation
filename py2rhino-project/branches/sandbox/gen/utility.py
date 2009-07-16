# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Utility(DispatchBaseClass):



    def all_procedures(self, all):
        """

        Returns the names of the  user-defined subroutines and functions resident in RhinoScript's VBScript engine.

        Parameters

        All : Optional, Boolean, bln

        Returns

        Array : An array of string identifying the names of user-defined procedures.
        Null : If no user-defined procedures are found.

        """

        return self._ApplyTypes_(503, 1, (12, 0), ((12, 0)), u'AllProcedures', None, all)

    def clipboard_text(self, text):
        """

        Returns or sets a text string to the Windows clipboard.

        Parameters

        Text : Optional, String, str

        Returns

        String : If strText is not specified, the current text string from the Windows clipboard if successful.
        String : If strText is specified, the previous text string from the Windows clipboard if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(245, 1, (12, 0), ((12, 0)), u'ClipboardText', None, text)

    def color_adjust_luma(self, r_g_b, luma, ale):
        """

        Changes the luminance of a red-green-blue (RGB) value. Hue and saturation are not affected.

        Parameters

        RGB : Required, Number, lng
        Luma : Required, Number, int
        ale : Optional, Boolean, bSc

        Returns

        Number : The modified RGB color value if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(878, 1, (12, 0), ((12, 0), (12, 0), bSc), u'ColorAdjustLuma', None, r_g_b, luma, ale)

    def color_blue_value(self, r_g_b):
        """

        Retrieves an intensity value for the blue component of a red-green-blue (RGB) value.

        Parameters

        RGB : Required, Number, lng

        Returns

        Number : The blue component if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(882, 1, (12, 0), ((12, 0)), u'ColorBlueValue', None, r_g_b)

    def color_green_value(self, r_g_b):
        """

        Retrieves an intensity value for the green component of a red-green-blue (RGB) value.

        Parameters

        RGB : Required, Number, lng

        Returns

        Number : The green component if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(881, 1, (12, 0), ((12, 0)), u'ColorGreenValue', None, r_g_b)

    def color_h_l_s_to_r_g_b(self, r_g_b):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def color_r_g_b_to_h_l_s(self, r_g_b):
        """

        Converts colors from red-green-blue (RGB) to hue-luminance-saturation (HLS) format.

        Parameters

        RGB : Required, Number, lng

        Returns

        Array : An array containing the hue, luminance, and saturation values if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(876, 1, (12, 0), ((12, 0)), u'ColorRGBToHLS', None, r_g_b)

    def color_red_value(self, r_g_b):
        """

        Retrieves an intensity value for the red component of a red-green-blue (RGB) value.

        Parameters

        RGB : Required, Number, lng

        Returns

        Number : The red component if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(880, 1, (12, 0), ((12, 0)), u'ColorRedValue', None, r_g_b)

    def cull_duplicate_numbers(self, numbers, tolerance):
        """

        Removes duplicates from an array of numbers.

        Parameters

        Numbers : Required, Array, arr
        Tolerance : Optional, Number, dbl

        Returns

        Array : An array of numbers with duplicates removed if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(550, 1, (12, 0), ((12, 0), (12, 0)), u'CullDuplicateNumbers', None, numbers, tolerance)

    def cull_duplicate_points(self, points, tolerance):
        """

        Removes duplicates from an array of 3-D points.

        Parameters

        Points : Required, Array, arr
        Tolerance : Optional, Number, dbl

        Returns

        Array : An array of 3-D points with duplicates removed if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(548, 1, (12, 0), ((12, 0), (12, 0)), u'CullDuplicatePoints', None, points, tolerance)

    def cull_duplicate_strings(self, strings, case_sensitive):
        """

        Removes duplicates from an array of strings.

        Parameters

        Strings : Required, Array, arr
        CaseSensitive : Optional, Boolean, bln

        Returns

        Array : An array of strings with duplicates removed if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(549, 1, (12, 0), ((12, 0), (12, 0)), u'CullDuplicateStrings', None, strings, case_sensitive)

    def current_printer(self, printer):
        """

        Returns or changes the current Windows printer.

        Parameters

        Printer : Optional, String, str

        Returns

        String : If strPrinter is not specified, the name of the current Windows printer if successful.
        String : If strPrinter is specified, the name of the previously current Windows printer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(358, 1, (12, 0), ((12, 0)), u'CurrentPrinter', None, printer)

    def get_settings(self, filename, section, entry):
        """

        ...

        Parameters

        Filename : Required, String, str
        Section : Optional, String, str
        Entry : Optional, String, str

        Returns

        Array : If strSection is not specified, a zero-based, one-dimensional array containing all section names from strFilename if successful.
        Array : If strEntry is not specified, a zero-based, one-dimensional array containing all entry names within strSection if successful.
        String : If strSection and strEntry are returned, the value of strEntry if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(246, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'GetSettings', None, filename, section, entry)

    def is_procedure(self, sub_name):
        """

        Verifies that a user-defined subroutine or function is resident in RhinoScript's VBScript engine.

        Parameters

        SubName : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(287, 1, (12, 0), ((12, 0)), u'IsProcedure', None, sub_name)

    def join_arrays(self, 1, 2):
        """

        Joins two one-dimensional arrays in to a single one-dimensional array.

        Parameters

        1 : Required, Array, arr
        2 : Required, Array, arr

        Returns

        Array : A one-dimensional array containing the elements of both input arrays if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(547, 1, (12, 0), ((12, 0), (12, 0)), u'JoinArrays', None, 1, 2)

    def make_array(self, per_bound, riant):
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

        return self._ApplyTypes_(356, 1, (12, 0), (), u'PrinterNames', None, )

    def pt2_str(self, point, ecision, space):
        """

        Converts a 3-D point value to a string.  Useful for display point values as output, or passing point values to Rhino commands.

        Parameters

        Point : Required, Array, arr
        ecision : Optional, Number, nPr
        Space : Optional, Boolean, bln

        Returns

        String : The formatted string if successful.
        Null : On error.

        """

        return self._ApplyTypes_(297, 1, (12, 0), ((12, 0), nPr, (12, 0)), u'Pt2Str', None, point, ecision, space)

    def save_settings(self, filename, section, entry, string):
        """

        ...

        Parameters

        Filename : Required, String, str
        Section : Optional, String, str
        Entry : Optional, String, str
        String : Optional, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(247, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'SaveSettings', None, filename, section, entry, string)

    def simplify_array(self, points):
        """

        Flattens an array of 3-D points into a one-dimensional array of real number. For example, if you had an array containing three 3-D points, this method would return a one-dimensional array containing nine real numbers.

        Parameters

        Points : Required, Array, arr

        Returns

        Array : A one-dimensional array containing real numbers, if successful.
        Null : If not successful or on error.

        """

        return self._ApplyTypes_(597, 1, (12, 0), ((12, 0)), u'SimplifyArray', None, points)

    def sleep(self, milliseconds):
        """

        Suspends the execution of a running script for the specified interval.

        Parameters

        Milliseconds : Required, Number, lng

        Returns

        Null : If successful, or on error.

        """

        return self._ApplyTypes_(248, 1, (12, 0), ((12, 0)), u'Sleep', None, milliseconds)

    def sort(self, strings, ascending, no_case):
        """

        Sorts an array of strings.

        Parameters

        Strings : Required, Array, arr
        Ascending : Optional, Boolean, bln
        NoCase : Optional, Boolean, bln

        Returns

        Array : An array sorted strings if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(249, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'Sort', None, strings, ascending, no_case)

    def sort_numbers(self, numbers, ascending):
        """

        Sorts an array of numbers.

        Parameters

        Numbers : Required, Array, arr
        Ascending : Optional, Boolean, bln

        Returns

        Array : An array of sorted numbers if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(552, 1, (12, 0), ((12, 0), (12, 0)), u'SortNumbers', None, numbers, ascending)

    def sort_point_list(self, points, tolerance):
        """

        Sorts an array of 3-D points so they will be connected in "reasonable" polyline order.

        Parameters

        Points : Required, Array, arr
        Tolerance : Optional, Number, dbl

        Returns

        Array : An array of sorted 3-D points  if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(644, 1, (12, 0), ((12, 0), (12, 0)), u'SortPointList', None, points, tolerance)

    def sort_points(self, points, ascending, order):
        """

        Sorts an array of 3-D points.

        Parameters

        Points : Required, Array, arr
        Ascending : Optional, Boolean, bln
        Order : Optional, Number, bln

        Returns

        Array : An array of sorted 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(551, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'SortPoints', None, points, ascending, order)

    def spool_to_printer(self, file, printer):
        """

        Spools, or sends, a text file or a print/plot file to a Windows printer.

        Parameters

        File : Required, String, str
        Printer : Required, String, str

        Returns

        String : The name of the spooled file if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(357, 1, (12, 0), ((12, 0), (12, 0)), u'SpoolToPrinter', None, file, printer)

    def str2_pt(self, point):
        """

        Converts a formatted string value into a 3-D point value.

        Parameters

        Point : Required, String, arr

        Returns

        Array : A 3-D point if successful.
        Null : On error.

        """

        return self._ApplyTypes_(409, 1, (12, 0), ((12, 0)), u'Str2Pt', None, point)

    def str2_pt_array(self, points):
        """

        Converts a formatted string value into an array of 3-D point value.

        Parameters

        Points : Required, String, str

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(410, 1, (12, 0), ((12, 0)), u'Str2PtArray', None, points)

    def strtok(self, text, delimiters):
        """

        Returns the tokens in a string.  Use this method as an alternative to the VBScript's Split function.

        Parameters

        Text : Required, String, str
        Delimiters : Optional, String, str

        Returns

        Array : A zero-based, one-dimensional array containing the string tokens if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(250, 1, (12, 0), ((12, 0), (12, 0)), u'Strtok', None, text, delimiters)

    def text_out(self, text, title):
        """

        Displays a text output window.

        Parameters

        Text : Required, String, str
        Title : Optional, String, str

        Returns

        Null : If successful or on failure.

        """

        return self._ApplyTypes_(755, 1, (12, 0), ((12, 0), (12, 0)), u'TextOut', None, text, title)

    def version(self):
        """

        Returns the version of RhinoScript.

        No parameters

        Returns

        Number : The version number.

        """

        return self._ApplyTypes_(288, 1, (12, 0), (), u'Version', None, )

