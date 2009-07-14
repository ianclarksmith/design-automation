# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Utility(DispatchBaseClass):



	def JoinArrays(self, arr1, arr2):
		"""

		Joins two one-dimensional arrays in to a single one-dimensional array.

		Parameters

		arr1 : Required,  Array,  The first one-dimensional array
		arr2 : Required,  Array,  The second one-dimensional array

		Returns

		Array : A one-dimensional array containing the elements of both input arrays if successful.
		Null : If not successful or on error.

		"""

		pass

	def CullDuplicateStrings(self, arrStrings, blnCaseSensitive):
		"""

		Removes duplicates from an array of strings.

		Parameters

		arrStrings : Required,   Array,   An array of numbers
		blnCaseSensitive : Optional,   Boolean,   Use case sensitivity when culling

		Returns

		Array : An array of strings with duplicates removed if successful.
		Null : If not successful or on error.

		"""

		pass

	def SortPoints(self, arrPoints, blnAscending, blnOrder):
		"""

		Sorts an array of 3-D points.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points
		blnAscending : Optional,   Boolean,   The sorting mode, either ascending or descending
		blnOrder : Optional,   Number,   The component sort order, where:

		Returns

		Array : An array of sorted 3-D points if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ClipboardText(self, strText):
		"""

		Returns or sets a text string to the Windows clipboard.

		Parameters

		strText : Optional,   String,   A text string

		Returns

		String : If strText is not specified, the current text string from the Windows clipboard if successful.
		String : If strText is specified, the previous text string from the Windows clipboard if successful.
		Null : If not successful or on error.

		"""

		pass

	def Version(self):
		"""

		Returns the version of RhinoScript.

		No parameters

		Returns

		Number : The version number.

		"""

		pass

	def Str2Pt(self, arrPoint):
		"""

		Converts a formatted string value into a 3-D point value.

		Parameters

		arrPoint : Required,   String,   A string that contains a delimited point like "1,2,3"

		Returns

		Array : A 3-D point if successful.
		Null : On error.

		"""

		pass

	def Pt2Str(self, arrPoint, nPrecision, blnSpace):
		"""

		Converts a 3-D point value to a string.  Useful for display point values as output, or passing point values to Rhino commands.

		Parameters

		arrPoint : Required,   Array,   A 3-D point
		nPrecision : Optional,   Number,   The display precision of the point coordinates
		blnSpace : Optional,   Boolean,   Append an additional trailing space after the point string

		Returns

		String : The formatted string if successful.
		Null : On error.

		"""

		pass

	def CurrentPrinter(self, strPrinter):
		"""

		Returns or changes the current Windows printer.

		Parameters

		strPrinter : Optional,   String,   The name of a Windows printer as returned by this method or by the PrinterNames method

		Returns

		String : If strPrinter is not specified, the name of the current Windows printer if successful.
		String : If strPrinter is specified, the name of the previously current Windows printer if successful.
		Null : If not successful, or on error.

		"""

		pass

	def SimplifyArray(self, arrPoints):
		"""

		Flattens an array of 3-D points into a one-dimensional array of real number. For example, if you had an array containing three 3-D points, this method would return a one-dimensional array containing nine real numbers.

		Parameters

		arrPoints : Required,  Array,  An array of 3-D points

		Returns

		Array : A one-dimensional array containing real numbers, if successful.
		Null : If not successful or on error.

		"""

		pass

	def Sort(self, arrStrings, blnAscending, blnNoCase):
		"""

		Sorts an array of strings.

		Parameters

		arrStrings : Required,   Array,   An array of string values
		blnAscending : Optional,   Boolean,   The sorting mode, either ascending or descending
		blnNoCase : Optional,   Boolean,   The case sensitivity mode

		Returns

		Array : An array sorted strings if successful.
		Null : If not successful, or on error.

		"""

		pass

	def SortPointList(self, arrPoints, dblTolerance):
		"""

		Sorts an array of 3-D points so they will be connected in "reasonable" polyline order.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points
		dblTolerance : Optional,   Number,   The minimum distance between points

		Returns

		Array : An array of sorted 3-D points  if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ColorRedValue(self, lngRGB):
		"""

		Retrieves an intensity value for the red component of a red-green-blue (RGB) value.

		Parameters

		lngRGB : Required,   Number,   The RGB color value

		Returns

		Number : The red component if successful.
		Null : If not successful or on error.

		"""

		pass

	def ColorRGBToHLS(self, lngRGB):
		"""

		Converts colors from red-green-blue (RGB) to hue-luminance-saturation (HLS) format.

		Parameters

		lngRGB : Required,   Number,   The RGB color value

		Returns

		Array : An array containing the hue, luminance, and saturation values if successful.
		Null : If not successful or on error.

		"""

		pass

	def Strtok(self, strText, strDelimiters):
		"""

		Returns the tokens in a string.  Use this method as an alternative to the VBScript's Split function.

		Parameters

		strText : Required,   String,   A string containing token(s)
		strDelimiters : Optional,   String,   A set of delimiter characters

		Returns

		Array : A zero-based, one-dimensional array containing the string tokens if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ColorHLSToRGB(self, lngRGB):
		"""

		Converts colors from hue-luminance-saturation (HLS) to red-green-blue format.

		Parameters

		lngRGB : Required,   Array,   The HLS color value

		Returns

		Number : The RGB color value if successful.
		Null : If not successful or on error.

		"""

		pass

	def SpoolToPrinter(self, strFile, strPrinter):
		"""

		Spools, or sends, a text file or a print/plot file to a Windows printer.

		Parameters

		strFile : Required,   String,   The full path to the file to spool
		strPrinter : Required,   String,   The name of a Windows printer as returned by either the CurrentPrinter or by the PrinterNames method

		Returns

		String : The name of the spooled file if successful.
		Null : If not successful, or on error.

		"""

		pass

	def TextOut(self, strText, strTitle):
		"""

		Displays a text output window.

		Parameters

		strText : Required,   String,   A text string to display
		strTitle : Optional,   String,   A dialog box title

		Returns

		Null : If successful or on failure.

		"""

		pass

	def CullDuplicatePoints(self, arrPoints, dblTolerance):
		"""

		Removes duplicates from an array of 3-D points.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points
		dblTolerance : Optional,   Number,   The minimum distance between points

		Returns

		Array : An array of 3-D points with duplicates removed if successful.
		Null : If not successful or on error.

		"""

		pass

	def Str2PtArray(self, strPoints):
		"""

		Converts a formatted string value into an array of 3-D point value.

		Parameters

		strPoints : Required,   String,   A string that contains an unknown number of space delimited points like "1,2,3 4,5,6 7,8,9"

		Returns

		Array : An array of 3-D points if successful.
		Null : If not successful, or on error.

		"""

		pass

	def SaveSettings(self, strFilename, strSection, strEntry, strString):
		"""

		...

		Parameters

		strFilename : Required,   String,   The name of the initialization file
		strSection : Optional,   String,   The section to which strString will be copied
		strEntry : Optional,   String,   The name of the entry to be associated with strString
		strString : Optional,   String,   The string to be written to the file

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def MakeArray(self, nUpperBound, vVariant):
		"""

		Creates a new, initialized one-dimensional array of a user-specified bounds.

		Parameters

		nUpperBound : Required,   Number,   The upper bounds of the new array
		vVariant : Optional,   Variant,   The value to initialize every array element

		Returns

		Array : The one-dimensional array if successful.
		Null : If not successful or on error.

		"""

		pass

	def IsProcedure(self, strSubName):
		"""

		Verifies that a user-defined subroutine or function is resident in RhinoScript's VBScript engine.

		Parameters

		strSubName : Required,   String,   The name of a user-defined subroutine of function

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def SortNumbers(self, arrNumbers, blnAscending):
		"""

		Sorts an array of numbers.

		Parameters

		arrNumbers : Required,   Array,   An array of numeric values
		blnAscending : Optional,   Boolean,   The sorting mode, either ascending or descending

		Returns

		Array : An array of sorted numbers if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AllProcedures(self, blnAll):
		"""

		Returns the names of the  user-defined subroutines and functions resident in RhinoScript's VBScript engine.

		Parameters

		blnAll : Optional,   Boolean,   If True (default) the names of all user-defined subroutines and functions are returned

		Returns

		Array : An array of string identifying the names of user-defined procedures.
		Null : If no user-defined procedures are found.

		"""

		pass

	def PrinterNames(self):
		"""

		Returns the name of all installed Windows printer.

		No parameters

		Returns

		Array : An array of Windows printer names if successful.
		Null : If not successful, or on error.

		"""

		pass

	def CullDuplicateNumbers(self, arrNumbers, dblTolerance):
		"""

		Removes duplicates from an array of numbers.

		Parameters

		arrNumbers : Required,   Array,   An array of numbers
		dblTolerance : Optional,   Number,   The minimum distance between numbers

		Returns

		Array : An array of numbers with duplicates removed if successful.
		Null : If not successful or on error.

		"""

		pass

	def ColorAdjustLuma(self, lngRGB, intLuma, bScale):
		"""

		Changes the luminance of a red-green-blue (RGB) value. Hue and saturation are not affected.

		Parameters

		lngRGB : Required,   Number,   The initial RGB color value
		intLuma : Required,   Number,   The luminance in units of 0
		bScale : Optional,   Boolean,   If bScale is set to True, intLuma specifies how much to increment or decrement the current luminance

		Returns

		Number : The modified RGB color value if successful.
		Null : If not successful or on error.

		"""

		pass

	def GetSettings(self, strFilename, strSection, strEntry):
		"""

		...

		Parameters

		strFilename : Required,   String,   The name of the initialization file
		strSection : Optional,   String,   The section containing the entry
		strEntry : Optional,   String,   The entry whose associated string is to be returned

		Returns

		Array : If strSection is not specified, a zero-based, one-dimensional array containing all section names from strFilename if successful.
		Array : If strEntry is not specified, a zero-based, one-dimensional array containing all entry names within strSection if successful.
		String : If strSection and strEntry are returned, the value of strEntry if successful.
		Null : If not successful, or on error.

		"""

		pass

	def Sleep(self, lngMilliseconds):
		"""

		Suspends the execution of a running script for the specified interval.

		Parameters

		lngMilliseconds : Required,   Number,   The duration in milliseconds

		Returns

		Null : If successful, or on error.

		"""

		pass

	def ColorGreenValue(self, lngRGB):
		"""

		Retrieves an intensity value for the green component of a red-green-blue (RGB) value.

		Parameters

		lngRGB : Required,   Number,   The RGB color value

		Returns

		Number : The green component if successful.
		Null : If not successful or on error.

		"""

		pass

	def ColorBlueValue(self, lngRGB):
		"""

		Retrieves an intensity value for the blue component of a red-green-blue (RGB) value.

		Parameters

		lngRGB : Required,   Number,   The RGB color value

		Returns

		Number : The blue component if successful.
		Null : If not successful or on error.

		"""

		pass

