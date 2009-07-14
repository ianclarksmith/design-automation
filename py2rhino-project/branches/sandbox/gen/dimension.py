# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Dimension(DispatchBaseClass):



	def IsAlignedDimension(self, strObject):
		"""

		Verifies an object is an aligned dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def DimensionUserText(self, strObject, strUserText):
		"""

		Returns or modifies the user text string of a dimension object. The user text is the string that gets printed when the dimension is drawn. If it contains the token "<>", then the token is replaced with the measured value of the dimension, formatted according to the dimension style settings. Note,  "<>" is the default user text string for linear dimensions.

		Parameters

		strObject : Required,  String,  The object's identifier
		strUserText : Optional,  String,  The new user text string value

		Returns

		String : If strUserText is not specified, then the current user text string if successful.
		String : If strUserText is specified, then the previous user text string if successful.
		Null : On error.

		"""

		pass

	def DimStyleLeaderArrowSize(self, strDimStyle, dblSize):
		"""

		Returns or changes the leader arrow size of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		dblSize : Optional,   Number,   The new leader arrow size

		Returns

		Number : If a size value is not specified, the current leader arrow size if successful.
		Number : If a size value is specified, the previous leader arrow size if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsDiameterDimension(self, strObject):
		"""

		Verifies an object is a diameter dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def DimStyleExtension(self, strDimStyle, dblExtension):
		"""

		Returns or changes the extension line extension of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		dblExtension : Optional,   Number,   The new extension line extension

		Returns

		Number : If an extension is not specified, the current extension line extension if successful.
		Number : If an extension is specified, the previous extension line extension if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsDimStyle(self, strDimStyle):
		"""

		Verifies the existence of a dimension style in the document.

		Parameters

		strDimStyle : Required,   String,   The name of a dimension style to test

		Returns

		Null : On error.

		"""

		pass

	def CurrentDimStyle(self, strDimStyle):
		"""

		Returns or changes the current default dimension style.

		Parameters

		strDimStyle : Optional,   String,   The name of an existing dimension style to make current

		Returns

		String : If a dimension style is not specified, the name of the current dimension style if successful.
		String : If a dimension style is specified, the name of the previous current dimension style if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsLeader(self, strObject):
		"""

		Verifies an object is a dimension leader object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsLinearDimension(self, strObject):
		"""

		Verifies an object is a linear dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsDimension(self, strObject):
		"""

		Verifies an object is a dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def LeaderText(self, strObject, strText):
		"""

		Returns or modifies the text string of a dimension leader object.

		Parameters

		strObject : Required,  String,  The object's identifier
		strText : Optional,  String,  The new text string value

		Returns

		String : If strText is not specified, then the current text string if successful.
		String : If strText is specified, then the previous text string if successful.
		Null : On error.

		"""

		pass

	def DimScale(self, dblScale):
		"""

		Returns or changes the document's global dimension scale.

		Parameters

		dblScale : Optional,   Number,   The new global dimension scale value

		Returns

		Number : If a dimension scale is not specified, the current dimension scale if successful.
		Number : If a dimension scale is specified, the previous dimension scale if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimStyleOffset(self, strDimStyle, dblOffset):
		"""

		Returns or changes the extension line offset of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		dblOffset : Optional,   Number,   The new extension line offset

		Returns

		Number : If an offset is not specified, the current extension line offset if successful.
		Number : If an offset is specified, the previous extension line offset if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsOrdinateDimension(self, strObject):
		"""

		Verifies an object is an ordinate dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def DimStyleTextAlignment(self, strDimStyle, intAlignment):
		"""

		Returns or changes the text alignment mode of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		intAlignment : Optional,   Number,   The new text alignment

		Returns

		Number : If a mode is not specified, the current text alignment mode  if successful.
		Number : If a mode is specified, the previous text alignment mode if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddDimStyle(self, strDimStyle):
		"""

		Adds a new dimension style to the document.  The new dimension style will be initialized with the current default dimension style properties.

		Parameters

		strDimStyle : Optional,   String,   The name of the new dimension style

		Returns

		String : The name of the new dimension style if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimStyleTextHeight(self, strDimStyle, dblHeight):
		"""

		Returns or changes the text height used by a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		dblHeight : Optional,   Number,   The new text height

		Returns

		Number : If a height is not specified, the current text height if successful.
		Number : If a height is specified, the previous text height if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimStyleTextGap(self, strDimStyle, dblGap):
		"""

		Returns or changes the text gap used by a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		dblGap : Optional,   Number,   The new text gap

		Returns

		Number : If a gap is not specified, the current text gap if successful.
		Number : If a gap is specified, the previous text gap if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteDimStyle(self, strDimStyle):
		"""

		Removes an existing dimension style from the document.  The dimension style to be removed cannot be the reference by any dimension objects.

		Parameters

		strDimStyle : Required,   String,   The name of an un-referenced dimension style

		Returns

		String : The name of the deleted dimension style if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddLeader(self, arrPoints, strView, strText):
		"""

		Adds an annotation leader to the document. Leader objects are planar. The array of 3-D points passed to this member should be co-planar.

		Parameters

		arrPoints : Required,   Array,   An array of 3-D points
		strView : Optional,   String,   The title of the view
		strText : Optional,   String,   The leader's text string

		Returns

		String : The identifier of the new object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimStyleNumberFormat(self, strDimStyle, intFormat):
		"""

		Returns or changes the number display format of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		intFormat : Optional,   Number,   The new number display format

		Returns

		Number : If a format is not specified, the current number display format if successful.
		Number : If a format is specified, the previous number display format if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimensionValue(self, strObject):
		"""

		Returns the value of a dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Number : The value of the dimension successful.
		Null : On error.

		"""

		pass

	def IsDimStyleReference(self, strDimStyle):
		"""

		Verifies that an existing dimension style is from a reference file.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style

		Returns

		Null : On error.

		"""

		pass

	def DimStyleAnglePrecision(self, strDimStyle, intPrecision):
		"""

		Returns or changes the angle display precision of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		intPrecision : Optional,   Number,   The new angle precision value

		Returns

		Number : If a precision is not specified, the current angle precision if successful.
		Number : If a precision is specified, the previous angle precision if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsAngularDimension(self, strObject):
		"""

		Verifies an object is an angular dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def DimensionStyle(self, strObject, strStyle):
		"""

		Returns or modifies the dimension style of a dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier
		strStyle : Optional,  String,  The name of an existing dimension style

		Returns

		String : If strStyle is not specified, then the object's current dimension style if successful.
		String : If strStyle is specified, then the object's previous dimension style if successful.
		Null : On error.

		"""

		pass

	def DimStyleArrowSize(self, strDimStyle, dblSize):
		"""

		Returns or changes the arrow size of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		dblSize : Optional,   Number,   The new arrow size

		Returns

		Number : If a size value is not specified, the current arrow size if successful.
		Number : If a size value is specified, the previous arrow size if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsRadialDimension(self, strObject):
		"""

		Verifies an object is a radial dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def RenameDimStyle(self, strOldStyle, strNewStyle):
		"""

		Renames an existing dimension style.

		Parameters

		strOldStyle : Required,   String,   The name of an existing dimension style
		strNewStyle : Required,   String,   The new dimension style name

		Returns

		String : The new dimension style name if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimStyleCount(self):
		"""

		Returns the number of dimension styles in the document.

		No parameters

		Returns

		Number : The number of dimension styles in the document.

		"""

		pass

	def DimensionText(self, strObject):
		"""

		Returns the text displayed by a dimension object.

		Parameters

		strObject : Required,  String,  The object's identifier

		Returns

		String : The dimension text if successful.
		Null : On error.

		"""

		pass

	def DimStyleLinearPrecision(self, strDimStyle, intPrecision):
		"""

		Returns or changes the linear display precision of a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		intPrecision : Optional,   Number,   The new linear precision value

		Returns

		Number : If a precision is not specified, the current linear precision if successful.
		Number : If ar precision is specified, the previous linear precision if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimStyleFont(self, strDimStyle, strFont):
		"""

		Returns or changes the font used by a dimension style.

		Parameters

		strDimStyle : Required,   String,   The name of an existing dimension style
		strFont : Optional,   String,   The new font face name

		Returns

		String : If a font is not specified, the current font if successful.
		String : If a font is specified, the previous font if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DimStyleNames(self, blnSort):
		"""

		Returns the names of all dimension styles in the document.

		Parameters

		blnSort : Optional,   Boolean,   Return a sorted list of dimension style names

		Returns

		Array : An array of dimension style names if successful.
		Null : If not successful, or on error.

		"""

		pass

