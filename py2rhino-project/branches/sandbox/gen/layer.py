# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Layer(DispatchBaseClass):



	def IsLayerChangeable(self, strLayer):
		"""

		Verifies that the objects on a layer can be changed (normal).

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def LayerColor(self, strLayer, lngColor):
		"""

		Returns or changes the color of a layer.  Layer colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

		Parameters

		strLayer : Required,   String,   The name of an existing layer
		lngColor : Optional,   Number,   The new color value

		Returns

		Number : If a color value  is not specified,  the current color value if successful.
		Number : If a color value is specified, the previous color value if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsLayerReference(self, strLayer):
		"""

		Verifies that an existing layer is from a reference file.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def IsLayerCurrent(self, strLayer):
		"""

		Verifies that a layer is the current layer.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def IsLayerLocked(self, strLayer):
		"""

		Verifies that an existing layer is locked.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def AddLayer(self, strLayer, lngColor, blnVisible, blnLocked, strParent):
		"""

		Adds a new layer to the document.

		Parameters

		strLayer : Optional,   String,   The name of the new layer
		lngColor : Optional,   Number,   A Red-Green-Blue color value
		blnVisible : Optional,   Boolean,   The layer's visibility
		blnLocked : Optional,   Boolean,   The layer's locked state
		strParent : Optional,   String,   The name of the new layer's parent layer

		Returns

		String : The name of the new layer if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LayerOrder(self, strLayer):
		"""

		Returns the current display order index of a layer as displayed in Rhino's Layer dialog box.  A display order index of -1 indicates that the current Layer dialog filter does not allow the layer to appear in the layer list.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Number : A zero-based display order index if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LayerLocked(self, strLayer, blnVisible):
		"""

		Returns or changes the locked mode of a layer. This method should be use instead of LayerMode.

		Parameters

		strLayer : Required,   String,   The name of an existing layer
		blnVisible : Optional,   Boolean,   The new layer locked mode

		Returns

		Boolean : If a layer mode is not specified,  the current layer locked mode if successful.
		Boolean : If a layer mode is specified, the previous layer locked mode if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenameLayer(self, strOldName, strNewName):
		"""

		Renames an existing layer.

		Parameters

		strOldName : Required,   String,   The name of an existing layer
		strNewName : Required,   String,   The new layer name

		Returns

		String : The new layer name if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LayerCount(self):
		"""

		Returns the number of layers in the document.

		No parameters

		Returns

		Number : The number of layers in the document.

		"""

		pass

	def IsLayerParentOf(self, strLayer, strTest):
		"""

		Verifies that a layer is a parent of another layer.

		Parameters

		strLayer : Required,   String,   The name of the layer to test against
		strTest : Required,   String,   The name of the layer to test

		Returns

		Boolean : True if strTest is a parent of strLayer. False otherwise.
		Null : On error.

		"""

		pass

	def PurgeLayer(self, strLayer):
		"""

		Removes an existing layer from the document.  Unlike the DeleteLayer method, PurgeLayer will remove the layer even if contains geometry objects.  The layer to be removed cannot be the current layer.

		Parameters

		strLayer : Required,   String,   The name of the layer to purge

		Returns

		String : The name of the purged layer if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LayerPrintWidth(self, strLayer, dblWidth):
		"""

		Returns or changes the print width of a layer. Print width is specified in millimeters. A print width of 0.0 denotes the "default" print width.

		Parameters

		strLayer : Required,  String,  The name of an existing layer
		dblWidth : Optional,  Number,  The new layer print width in millimeters

		Returns

		Number : If a layer print width is not specified,  the current layer print width if successful.
		Number : If a layer print width is specified, the previous layer print width if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ExpandLayer(self, strLayer, blnExpand):
		"""

		Expands a layer. Expanded layers can be viewed in Rhino's Layer dialog.

		Parameters

		strLayer : Required,   String,   The name of the layer to expand
		blnExpand : Required,   Boolean,   True to expand, False to collapse

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsLayerChildOf(self, strLayer, strTest):
		"""

		Verifies that a layer is a child of another layer.

		Parameters

		strLayer : Required,   String,   The name of the layer to test against
		strTest : Required,   String,   The name of the layer to test

		Returns

		Boolean : True if strTest is a child of strLayer. False otherwise.
		Null : On error.

		"""

		pass

	def LayerVisible(self, strLayer, blnVisible):
		"""

		Returns or changes the visibility property of a layer. This method should be use instead of LayerMode.

		Parameters

		strLayer : Required,   String,   The name of an existing layer
		blnVisible : Optional,   Boolean,   The new layer visibility

		Returns

		Boolean : If a layer mode is not specified,  the current layer visibility if successful.
		Boolean : If a layer mode is specified, the previous layer visibility if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ParentLayer(self, strLayer, strParent):
		"""

		Returns or modifies the parent layer of a layer.

		Parameters

		strLayer : Required,   String,   The name of the layer
		strParent : Optional,   String,   The name of the new parent layer

		Returns

		String : If strParent is not specified, the name of the current parent layer if successful.
		String : If strParent is specified, the name of the previous parent layer if successful.
		Null : If the layer does not have a parent, or on error.

		"""

		pass

	def IsLayerVisible(self, strLayer):
		"""

		Verifies that an existing layer is visible (normal, locked,  and reference).

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def IsLayerEmpty(self, strLayer):
		"""

		Verifies that an existing layer is empty, or contains no objects.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def IsLayerExpanded(self, strLayer):
		"""

		Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's Layer dialog.

		Parameters

		strLayer : Required,   String,   The name of the layer to test

		Returns

		Boolean : True if expanded, False if collapsed.
		Null : On error.

		"""

		pass

	def IsLayerOn(self, strLayer):
		"""

		Verifies that an existing layer is on.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def LayerMaterialIndex(self, strLayer):
		"""

		Returns the material index of a layer.  A material index of -1 indicates that no material has been assigned to the layer.  Thus, the layer will use Rhino's default layer material.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Number : A zero-based material index if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsLayer(self, strLayer):
		"""

		Verifies the existence of a layer in the document.

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def CurrentLayer(self, strLayer):
		"""

		Returns or changes the current layer.

		Parameters

		strLayer : Optional,   String,   The name of an existing layer to make current

		Returns

		String : If a layer name is not specified, the name of the current layer if successful.
		String : If a layer name is specified, the name of the previous current layer if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteLayer(self, strLayer):
		"""

		Removes an existing layer from the document.  The layer to be removed cannot be the current layer.  Unlike the PurgeLayer method,  the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.

		Parameters

		strLayer : Required,   String,   The name of an empty layer

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def LayerLinetype(self, strLayer, strLinetype):
		"""

		Returns or changes the linetype of a layer.

		Parameters

		strLayer : Required,  String,  The name of an existing layer
		strLinetype : Optional,  String,  The name of the new linetype

		Returns

		String : If a linetype is not specified,  the name of the current linetype if successful.
		String : If a linetype is specified, the name of the previous linetype if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LayerChildCount(self, strLayer):
		"""

		Returns the number of immediate child layers of a layer.

		Parameters

		strLayer : Required,   String,   The name of the layer

		Returns

		Number : The number of immediate child layers if successful
		Null : On error.

		"""

		pass

	def LayerNames(self, blnSort):
		"""

		Returns the names of all layers in the document.

		Parameters

		blnSort : Optional,   Boolean,   Return a sorted list of layer names

		Returns

		Array : An array of layer names if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsLayerSelectable(self, strLayer):
		"""

		Verifies that an existing layer is selectable (normal and reference).

		Parameters

		strLayer : Required,   String,   The name of an existing layer

		Returns

		Null : On error.

		"""

		pass

	def LayerPrintColor(self, strLayer, lngColor):
		"""

		Returns or changes the print color of a layer. Layer print colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be printed.

		Parameters

		strLayer : Required,  String,  The name of an existing layer
		lngColor : Optional,  Number,  The new print color value

		Returns

		Number : If a layer print color is not specified,  the current layer print color if successful.
		Number : If a layer print color is specified, the previous layer print color if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LayerChildren(self, strLayer):
		"""

		Returns the immediate child layers of a layer.

		Parameters

		strLayer : Required,   String,   The name of the layer

		Returns

		Array : An array of strings identifying the layer's children if successful
		Null : If the layer has no children, or on error.

		"""

		pass

	def LayerMode(self, strLayer, intMode):
		"""

		Returns or changes the mode of a layer.

		Parameters

		strLayer : Required,   String,   The name of an existing layer
		intMode : Optional,   Number,   The new layer mode

		Returns

		Number : If a layer mode is not specified,  the current layer mode  if successful.
		Number : If a layer mode is specified, the previous layer mode if successful.
		Null : If not successful, or on error.

		"""

		pass

