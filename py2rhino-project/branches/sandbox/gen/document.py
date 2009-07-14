# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Document(DispatchBaseClass):



	def CreatePreviewImage(self, strFile, strView, arrSize, intFlags, blnWireframe):
		"""

		Creates a bitmap preview image of the current model.

		Parameters

		strFile : Required,  String,  The name of the bitmap file to create
		strView : Optional,   String,   The title of the view
		arrSize : Optional,   Array,   An array of two integers that specify the width and height of the bitmap in pixels
		intFlags : Optional,   Integer,   The bitmap creation flags
		blnWireframe : Optional,   Boolean,   If specified and True, then a wireframe preview image, instead of a rendered image, will be created

		Returns

		Boolean : True or False indicating success or failure.

		"""

		pass

	def DocumentModified(self, blnModified):
		"""

		Note, setting the document modified flag to false will prevent the "Do you want to save this file..." from displaying when you close Rhino.

		Parameters

		blnModified : Optional,  Boolean,  The modified state, either True or False

		Returns

		Boolean : If no modified state is specified, the current modified state if successful.
		Boolean : If a modified state is specified, the previous modified state if successful.

		"""

		pass

	def DocumentName(self):
		"""

		Returns the name of the currently loaded Rhino document (3DM file).

		No parameters

		Returns

		String : The current document name if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DocumentPath(self):
		"""

		Returns the path of the currently loaded Rhino document (3DM file).

		No parameters

		Returns

		String : The current document path if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DocumentURL(self, strURL):
		"""

		Returns or sets the uniform resource locator (URL) of the currently loaded Rhino document (3DM file).

		Parameters

		strURL : Optional,   String,   The URL

		Returns

		String : If no URL is specified, the current URL if successful.
		String : If a URL is specified, the previous URL if successful.
		Null : If not successful, or on error.

		"""

		pass

	def EnableRedraw(self, blnSelect):
		"""

		Enables or disables screen redrawing.

		Parameters

		blnSelect : Optional,  Boolean,  The screen redrawing state

		Returns

		Boolean : The previous screen redrawing state.

		"""

		pass

	def ExtractPreviewImage(self, strFileName, strModelName):
		"""

		Extracts the bitmap preview image from the specified model (.3dm).

		Parameters

		strFileName : Required,   String,   The name of the bitmap file to create
		strModelName : Optional,   String,   The model (

		Returns

		Boolean : True or False indicating success or failure.

		"""

		pass

	def IsDocumentModified(self):
		"""

		Verifies that the current document has been modified in some way.

		No parameters

		Returns

		Boolean : True or False indicating either modified or not modified.

		"""

		pass

	def Notes(self, strNotes):
		"""

		Returns or sets the document's notes.  Notes are generally created by using Rhino's Notes command.

		Parameters

		strNotes : Optional,   String,   The notes

		Returns

		String : If strNotes is not specified, the current notes if successful.
		String : If strNotes is specified, the previous notes if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ReadFileVersion(self):
		"""

		Returns the file version of the current document.  Use this function to determine which version of Rhino last saved the document. Note, this function will not return values from referenced or merged files.

		No parameters

		Returns

		Number : The file version of the document if successful.  Note, values less than zero indicate that the current document has not been read (from disk).
		Null : If not successful, or on error.

		"""

		pass

	def Redraw(self):
		"""

		Redraws all views.

		No parameters

		No returns


		"""

		pass

	def RenderAntialias(self, intStyle):
		"""

		pixel.  Increasing the antialiasing level can add considerable time to the overall rendering.  See Rhino's DocumentProperties command (Rhino Render window) for details.

		Parameters

		intStyle : Optional,   Number,   The render antialiasing style

		Returns

		Number : If intStyle is not specified, the current render antialiasing style if successful.
		Number : If intStyle  is not specified, the previous render antialiasing style if successful.
		Number : Is not successful, or on error.

		"""

		pass

	def RenderColor(self, intItem, lngColor):
		"""

		Returns or sets the render ambient light or background color. Render colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed. See Rhino's DocumentProperties command (Rhino Render window) for details.

		Parameters

		intItem : Required,  Number,  The item you wish to either query or change
		lngColor : Optional,  Number,  The new color value

		Returns

		Number : If lngColor is not specified, the current intItem color if successful.
		Number : If lngColor is specified, the previous intItem color if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshDensity(self, dblDensity):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		dblDensity : Optional,   Number,   The render mesh density, which is a number between 0

		Returns

		Number : If dblDensity is not specified, the current render mesh density if successful.
		Number : If dblDensity is specified, the previous render mesh density if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshMaxAngle(self, dblAngle):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		dblAngle : Optional,   Number,   The render mesh maximum angle in degrees

		Returns

		Number : If dblAngle is not specified, the current render maximum angle if successful.
		Number : If dblAngle is specified, the previous render mesh maximum angle if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshMaxAspectRatio(self, dblRatio):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		dblRatio : Optional,   Number,   The render mesh maximum aspect ratio

		Returns

		Number : If dblRatio is not specified, the current render mesh maximum aspect ratio if successful.
		Number : If dblRatio is specified, the previous render mesh maximum aspect ratio if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshMaxDistEdgeToSrf(self, dblDistance):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		dblDistance : Optional,   Number,   The render mesh maximum distance, edge to surface

		Returns

		Number : If dblDistance is not specified, the current render mesh maximum distance, edge to surface if successful.
		Number : If dblDistance is specified, the previous render mesh maximum distance, edge to surface if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshMaxEdgeLength(self, dblLength):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		dblLength : Optional,   Number,   The render mesh maximum edge length

		Returns

		Number : If dblLength is not specified, the current render mesh maximum edge length if successful.
		Number : If dblLength is specified, the previous render mesh maximum edge length if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshMinEdgeLength(self, dblLength):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		dblLength : Optional,   Number,   The render mesh minimum edge length

		Returns

		Number : If dblLength is not specified, the current render mesh minimum edge length if successful.
		Number : If dblLength is specified, the previous render mesh minimum edge length if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshMinInitialGridQuads(self, intQuads):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		intQuads : Optional,   Number,   The render mesh minimum initial grid quads

		Returns

		Number : If intQuads is not specified, the current render mesh minimum initial grid quads if successful.
		Number : If intQuads is specified, the previous render mesh minimum initial grid quads if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshQuality(self, intQuality):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		intQuality : Optional,   Number,   The render mesh quality, either:

		Returns

		Number : If intQuality is not specified, the current render mesh quality if successful.
		Number : If intQuality is specified, the previous render mesh quality if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderMeshSettings(self, intSettings):
		"""

		For more information on render meshes, see the Document Properties: Mesh topic in the Rhino help file.

		Parameters

		intSettings : Optional,   Number,   The render mesh settings, which is a bit-coded number that allows or disallows certain features

		Returns

		Number : If intSettings is not specified, the current render mesh settings if successful.
		Number : If intSettings is specified, the previous render mesh settings if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderResolution(self, arrResolution):
		"""

		Returns or sets the render resolution. Resolution is measured in pixels. See Rhino's DocumentProperties command (Rhino Render window) for details. Note, if the render resolution is set to "viewport", then the size of the active viewt is returned.

		Parameters

		arrResolution : Required,  Array,   An array containing two numbers identifying the resolution width and height in pixels

		Returns

		Array : If arrResolution is not specified, an array containing two numbers identifying the current resolution width and height in pixels if successful.
		Array : If arrResolution is specified, an array containing two numbers identifying the previous resolution width and height in pixels if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenderSettings(self, intSettings):
		"""

		Returns or sets render settings.  See Rhino's DocumentProperties command (Rhino Render window) for details.

		Parameters

		intSettings : Optional,   Number,   The render setting or settings to modify

		Returns

		Number : If intSettings is not specified, the current render settings if successful.
		Number : If intSettings is not specified, the previous render settings if successful.
		Number : Is not successful, or on error.

		"""

		pass

	def UnitAbsoluteTolerance(self, dblAbsTol):
		"""

		Returns or sets the document's absolute tolerance parameter.  Absolute tolerance is measured in drawing units. See Rhino's DocumentProperties command (Units window) for details.

		Parameters

		dblAbsTol : Optional,   Number,   The absolute tolerance in drawing units

		Returns

		Number : If dblAbsTol is not specified, the current absolute tolerance if successful.
		Number : If dblAbsTol is specified, the previous absolute tolerance if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnitAngleTolerance(self, dblAngleTol):
		"""

		Returns or sets the document's angle tolerance parameter.  Angle tolerance is measured degrees.  See Rhino's DocumentProperties command (Units window) for details.

		Parameters

		dblAngleTol : Optional,   Number,   The angle tolerance in degrees

		Returns

		Number : If dblAngleTol is not specified, the current angle tolerance if successful.
		Number : If dblAngleTol is specified, the previous angle tolerance if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnitCustomUnitSystem(self, dblUnits, blnScale, strName):
		"""

		Sets the document's units system to a user-defined system.  This overrides the units system set using the UnitSystem method.  See Rhino's DocumentProperties command (Units window) for details.

		Parameters

		dblUnits : Required,   Number,   The number of units per meter
		blnScale : Optional,   Boolean,   Scale existing geometry based on the new unit system
		strName : Optional,   String,   The name of the new unit system

		Returns

		Number : The previous units system if successful.  See UnitSystem for details.
		Null : If not successful, or on error.

		"""

		pass

	def UnitDistanceDisplayMode(self, intMode):
		"""

		Returns or sets the document's distance display mode parameter.  See Rhino's DocumentProperties command (Units window) for details.

		Parameters

		intMode : Optional,   Number,   The distance display mode

		Returns

		Number : If intMode is not specified, the current distance display mode if successful.
		Number : If intMode is specified, the previous distance display mode if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnitDistanceDisplayPrecision(self, intPrecision):
		"""

		Returns or sets the document's distance display precision parameter.  See Rhino's DocumentProperties command (Units window) for details.

		Parameters

		intPrecision : Optional,   Number,   The distance display precision

		Returns

		Number : If intPrecision is not specified, the current distance display precision if successful.
		Number : If intPrecision is specified, the previous distance display precision if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnitRelativeTolerance(self, dblRelTol):
		"""

		Returns or sets the document's relative tolerance parameter.  Relative tolerance is measured in percent. See Rhino's DocumentProperties command (Units window) for details.

		Parameters

		dblRelTol : Optional,   Number,   The relative tolerance in percent

		Returns

		Number : If dblRelTol is not specified, the current relative tolerance if successful.
		Number : If dblRelTol is specified, the previous relative tolerance if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnitScale(self, intToSystem, intFromSystem):
		"""

		Returns the scale factor for changing between unit systems.

		Parameters

		intToSystem : Required,   Number,   The units system to convert to
		intFromSystem : Optional,   Number,   The units system to convert from (see above)

		Returns

		Number : The scale factor for changing between unit systems if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnitSystem(self, intSystem, blnScale):
		"""

		Returns or sets the document's units system.  See Rhino's DocumentProperties command (Units window) for details.

		Parameters

		intSystem : Optional,   Number,   The units system
		blnScale : Optional,   Boolean,   Scale existing geometry based on the new unit system

		Returns

		Number : The previous units system if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnitSystemName(self, blnCapitalize, blnSingular, blnAbbreviate):
		"""

		Returns the name of the current unit system.

		Parameters

		blnCapitalize : Optional,   Boolean,   Capitalize the first character of the units system name (e
		blnSingular : Optional,   Boolean,  Return the singular form of the units system name (e
		blnAbbreviate : Optional,   Boolean,   Abbreviate the name of the units system (e

		Returns

		String : The name of the current units system if successful.

		"""

		pass

