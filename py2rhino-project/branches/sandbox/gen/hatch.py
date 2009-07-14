# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Hatch(DispatchBaseClass):



	def AddHatch(self, strCurve, strHatch, dblScale, dblRotation):
		"""

		Creates a new hatch object from a closed planar curve object.

		Parameters

		strCurve : Required,   String,   The identifier of the closed planar curve that defines the boundary of the hatch object
		strHatch : Optional,   String,   The name of the hatch pattern to be used by the hatch object
		dblScale : Optional,   Number,   The hatch pattern scale factor
		dblRotation : Optional,   Number,   The hatch pattern rotation angle in degrees

		Returns

		String : The identifier of the newly created hatch object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddHatchPatterns(self, strFileName, blnReplace):
		"""

		Adds hatch pattens to the document by importing hatch pattern definitions from a pattern file. For more information on hatch pattern files, see the Rhino help file for the Hatch command.

		Parameters

		strFileName : Required,   String,   The name of the hatch pattern file to import
		blnReplace : Optional,   Boolean,   If hatch pattern names already in the document match hatch pattern names in the pattern definition file, then the existing hatch patterns will be redefined

		Returns

		Array : The names of the newly added hatch patterns if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddHatches(self, arrCurves, strHatch, dblScale, dblRotation):
		"""

		Creates one or more new hatch objects from an array of closed planar curve objects.

		Parameters

		arrCurves : Required,   Array,   An array of strings that identify one or more closed planar curves that defines the boundaries of the hatch objects
		strHatch : Optional,   String,   The name of the hatch pattern to be used by the hatch object
		dblScale : Optional,   Number,   The hatch pattern scale factor
		dblRotation : Optional,   Number,   The hatch pattern rotation angle in degrees

		Returns

		Array : The identifiers of the newly created hatch objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def CurrentHatchPattern(self, strHatch):
		"""

		Returns or sets the current hatch pattern file.

		Parameters

		strHatch : Optional,   String,   The name of an existing hatch pattern to make current

		Returns

		String : If a hatch pattern name is not specified, the current hatch pattern if successful.
		String : If a hatch pattern name is specified, the previous current hatch pattern if successful.
		Null : On error.

		"""

		pass

	def ExplodeHatch(self, strHatch, blnDelete):
		"""

		Explodes a hatch object into its component objects. The exploded objects will be added to the document. If the hatch object uses a solid pattern, then planar face Brep objects will be created. Otherwise, line curve objects will be created.

		Parameters

		strHatch : Required,   String,   The identifier of an object
		blnDelete : Optional,   Boolean,   Delete the hatch object

		Returns

		Array : An array of strings identifying the newly created objects if successful.
		Null : On error.

		"""

		pass

	def HatchPattern(self, strObject, strHatch):
		"""

		Returns or changes a hatch object's hatch pattern.

		Parameters

		strObject : Required,   String,   The identifier of a hatch object
		strHatch : Optional,   String,   The name of an existing hatch pattern to replace the current hatch pattern

		Returns

		String : If a hatch pattern name is not specified, the current hatch pattern if successful.
		String : If a hatch pattern name is specified, the previous current hatch pattern if successful.
		Null : On error.

		"""

		pass

	def HatchPatternCount(self):
		"""

		Returns the number of hatch patterns in the document.

		No parameters

		Returns

		Number : The number of hatch patterns in the document.

		"""

		pass

	def HatchPatternDescription(self, strHatch):
		"""

		Returns the description of a hatch pattern. Note, not all hatch patterns have descriptions for descriptions are optional.

		Parameters

		strHatch : Required,   String,   The name of an existing hatch pattern

		Returns

		String : If hatch pattern's description if successful.
		Null : If not successful, or on error.

		"""

		pass

	def HatchPatternFillType(self, strHatch):
		"""

		Gradient, uses fill color definition.

		Parameters

		strHatch : Required,   String,   The name of an existing hatch pattern

		Returns

		Number : If hatch pattern's fill type if successful.
		Null : If not successful, or on error.

		"""

		pass

	def HatchPatternNames(self):
		"""

		Returns the names of all of the hatch pattern in the document.

		No parameters

		Returns

		Array : An array of hatch pattern names if successful.
		Null : If not successful, or on error.

		"""

		pass

	def HatchRotation(self, strObject, dblRotation):
		"""

		Returns or modifies the rotation applied to the hatch pattern when it is mapped to the hatch's plane.

		Parameters

		strObject : Required,   String,   The identifier of a hatch object
		dblRotation : Optional,   Number,   The rotation angle in degrees

		Returns

		Number : If a rotation angle is not specified, the current rotation angle if successful.
		Number : If a rotation angle is specified, the previous rotation angle if successful.
		Null : On error.

		"""

		pass

	def HatchScale(self, strObject, dblScale):
		"""

		Returns or modifies the scale applied to the hatch pattern when it is mapped to the hatch's plane.

		Parameters

		strObject : Required,   String,   The identifier of a hatch object
		dblScale : Optional,   Number,   The scale factor

		Returns

		Number : If a scale factor is not specified, the current scale factor if successful.
		Number : If a scale factor is specified, the previous scale factor if successful.
		Null : On error.

		"""

		pass

	def IsHatch(self, strObject):
		"""

		Verifies the existence of a hatch object in the document.

		Parameters

		strObject : Required,   String,   The identifier of an object

		Returns

		Null : On error.

		"""

		pass

	def IsHatchPattern(self, strHatch):
		"""

		Verifies the existence of a hatch pattern in the document.

		Parameters

		strHatch : Required,   String,   The name of a hatch pattern

		Returns

		Null : On error.

		"""

		pass

	def IsHatchPatternCurrent(self, strHatch):
		"""

		Verifies that a hatch pattern is the current hatch pattern.

		Parameters

		strHatch : Required,   String,   The name of an existing hatch pattern

		Returns

		Null : On error.

		"""

		pass

	def IsHatchPatternReference(self, strHatch):
		"""

		Verifies that a hatch pattern is from a reference file.

		Parameters

		strHatch : Required,   String,   The name of an existing hatch pattern

		Returns

		Null : On error.

		"""

		pass

