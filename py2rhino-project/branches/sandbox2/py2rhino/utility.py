# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Utility(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

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
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [all]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(503, 1, (VT_VARIANT, 0), magic, u"AllProcedures", None, *flattened)

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
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [text]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(245, 1, (VT_VARIANT, 0), magic, u"ClipboardText", None, *flattened)

    def color_adjust_luma(self, r_g_b, luma, scale=None):
        """        
        Changes the luminance of a red-green-blue (RGB) value. Hue and saturation are not affected.
    
        Parameters
        ==========

        r_g_b, Integer, Required        
        The initial RGB color value.
            
        luma, Integer, Required        
        The luminance in units of 0.1 percent of the total range.  For example, a value of intLuma = 50 corresponds to 5 percent of the maximum luminance.
            
        scale, Boolean, Optional        
        If bScale is set to True, intLuma specifies how much to increment or decrement the current luminance.  If bScale is set to FALSE, intLuma specifies the absolute luminance.  The default value is False.
		If bScale is set to TRUE, intLuma can range from -1000 to +1000.
            
        Returns
        =======

        number
        The modified RGB color value if successful.

        null
        If not successful or on error.

        """

        params = [r_g_b, luma, scale]
        required = [True, True, False]
        magic = [(VT_I4, 1), (VT_I2, 1), (VT_BOOL, 1)]
        flattened = [r_g_b, luma, scale]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(878, 1, (VT_VARIANT, 0), magic, u"ColorAdjustLuma", None, *flattened)

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
        required = [True]
        magic = [(VT_I4, 1),]
        flattened = [r_g_b]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(882, 1, (VT_VARIANT, 0), magic, u"ColorBlueValue", None, *flattened)

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
        required = [True]
        magic = [(VT_I4, 1),]
        flattened = [r_g_b]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(881, 1, (VT_VARIANT, 0), magic, u"ColorGreenValue", None, *flattened)

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
        required = [True]
        magic = [(VT_I4, 1),]
        flattened = [r_g_b]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(877, 1, (VT_VARIANT, 0), magic, u"ColorHLSToRGB", None, *flattened)

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
        required = [True]
        magic = [(VT_I4, 1),]
        flattened = [r_g_b]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(876, 1, (VT_VARIANT, 0), magic, u"ColorRGBToHLS", None, *flattened)

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
        required = [True]
        magic = [(VT_I4, 1),]
        flattened = [r_g_b]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(880, 1, (VT_VARIANT, 0), magic, u"ColorRedValue", None, *flattened)

    def cull_duplicate_numbers(self, numbers, tolerance=None):
        """        
        Removes duplicates from an array of numbers.
    
        Parameters
        ==========

        numbers, Array of Integers, Required        
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
        required = [True, False]
        magic = [(VT_ARRAY + VT_I2, 1), (VT_R8, 1)]
        flattened = [flatten_params(numbers), tolerance]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(550, 1, (VT_VARIANT, 0), magic, u"CullDuplicateNumbers", None, *flattened)

    def cull_duplicate_points(self, points, tolerance=None):
        """        
        Removes duplicates from an array of 3-D points.
    
        Parameters
        ==========

        points, Array of Doubles, Required        
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
        required = [True, False]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_R8, 1)]
        flattened = [flatten_params(points), tolerance]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(548, 1, (VT_VARIANT, 0), magic, u"CullDuplicatePoints", None, *flattened)

    def cull_duplicate_strings(self, strings, case_sensitive=None):
        """        
        Removes duplicates from an array of strings.
    
        Parameters
        ==========

        strings, Array of Integers, Required        
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
        required = [True, False]
        magic = [(VT_ARRAY + VT_I2, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(strings), case_sensitive]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(549, 1, (VT_VARIANT, 0), magic, u"CullDuplicateStrings", None, *flattened)

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
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [printer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(358, 1, (VT_VARIANT, 0), magic, u"CurrentPrinter", None, *flattened)

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
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [filename, section, entry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(246, 1, (VT_VARIANT, 0), magic, u"GetSettings", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [sub_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(287, 1, (VT_VARIANT, 0), magic, u"IsProcedure", None, *flattened)

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

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(356, 1, (VT_VARIANT, 0), magic, u"PrinterNames", None, *flattened)

    def pt2_str(self, point, precision=None, space=None):
        """        
        Converts a 3-D point value to a string.  Useful for display point values as output, or passing point values to Rhino commands.
    
        Parameters
        ==========

        point, Array of Doubles, Required        
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
        required = [True, False, False]
        magic = [(VT_ARRAY + VT_R8, 1), (VT_I2, 1), (VT_BOOL, 1)]
        flattened = [flatten_params(point), precision, space]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(297, 1, (VT_VARIANT, 0), magic, u"Pt2Str", None, *flattened)

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
        required = [True, False, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [filename, section, entry, string]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(247, 1, (VT_VARIANT, 0), magic, u"SaveSettings", None, *flattened)

    def simplify_array(self, points):
        """        
        Flattens an array of 3-D points into a one-dimensional array of real number. For example, if you had an array containing three 3-D points, this method would return a one-dimensional array containing nine real numbers.
    
        Parameters
        ==========

        points, Array of Doubles, Required        
        An array of 3-D points.
            
        Returns
        =======

        array
        A one-dimensional array containing real numbers, if successful.

        null
        If not successful or on error.

        """

        params = [points]
        required = [True]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(points)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(597, 1, (VT_VARIANT, 0), magic, u"SimplifyArray", None, *flattened)

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
        required = [True]
        magic = [(VT_I4, 1),]
        flattened = [milliseconds]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(248, 1, (VT_VARIANT, 0), magic, u"Sleep", None, *flattened)

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
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [file, printer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(357, 1, (VT_VARIANT, 0), magic, u"SpoolToPrinter", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [point]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(409, 1, (VT_VARIANT, 0), magic, u"Str2Pt", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [points]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(410, 1, (VT_VARIANT, 0), magic, u"Str2PtArray", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [text, delimiters]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(250, 1, (VT_VARIANT, 0), magic, u"Strtok", None, *flattened)

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
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [text, title]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(755, 1, (VT_VARIANT, 0), magic, u"TextOut", None, *flattened)

    def version(self):
        """        
        Returns the version of RhinoScript.
    
        No parameters

        Returns
        =======

        number
        The version number.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(288, 1, (VT_VARIANT, 0), magic, u"Version", None, *flattened)

