# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Selection(DispatchBaseClass):



	def AllObjects(self, blnSelect, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all objects in the document.

		Parameters

		blnSelect : Optional,   Boolean,   Select the objects
		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def FirstObject(self, blnSelect, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifier of the first object in the document.  The first object in the document is the last object created by the user.

		Parameters

		blnSelect : Optional,   Boolean,   Select the object
		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		String : The identifier of the object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def GetCurveObject(self, strMessage, blnPreSelect, blnSelect):
		"""

		Prompts the user to pick, or select, a single curve object.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		blnPreSelect : Optional,   Boolean,   Allow for the selection of pre-selected objects
		blnSelect : Optional,   Boolean,   Select the picked objects

		Returns

		Array : An array of selection information if successful. The array will contain the following information:
		Null : If not successful, or on error.

		"""

		pass

	def GetObject(self, strMessage, intType, blnPreSelect, blnSelect, arrObjects):
		"""

		Prompts the user to pick, or select, a single object.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		intType : Optional,   Number,   The type or types of geometry objects (points, curves, surfaces, meshes, etc
		blnPreSelect : Optional,   Boolean,   Allow for the selection of pre-selected objects
		blnSelect : Optional,   Boolean,   Specifies whether or not the picked objects will remain selected when the function ends
		arrObjects : Optional,   Array,   An array of strings identifying the objects that are allowed to be selected

		Returns

		String : The identifier of the picked object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def GetObjectEx(self, strMessage, intType, blnPreSelect, blnSelect, arrObjects):
		"""

		Prompts the user to pick, or select, a single object.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		intType : Optional,   Number,   The type or types of geometry objects (points, curves, surfaces, meshes, etc
		blnPreSelect : Optional,   Boolean,   Allow for the selection of pre-selected objects
		blnSelect : Optional,   Boolean,   Specifies whether or not the picked objects will remain selected when the function ends
		arrObjects : Optional,   Array,   An array of strings identifying the objects that are allowed to be selected

		Returns

		Array : An array of selection information if successful. The array will contain the following information:
		Null : If not successful, or on error.

		"""

		pass

	def GetObjects(self, strMessage, intType, blnGroup, blnPreSelect, blnSelect, arrObjects):
		"""

		Prompts the user to pick or select one or more objects.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		intType : Optional,   Number,   The type(s) of geometry objects (points, curves, surfaces, meshes, etc
		blnGroup : Optional,   Boolean,   Honor object grouping
		blnPreSelect : Optional,   Boolean,   Allow for the selection of pre-selected objects
		blnSelect : Optional,   Boolean,   Specifies whether or not the picked objects will remain selected when the function ends
		arrObjects : Optional,   Array,   An array of strings identifying the objects that are allowed to be selected

		Returns

		Array : An array of strings identifying the picked objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def GetObjectsEx(self, strMessage, intType, blnGroup, blnPreSelect, blnSelect, arrObjects):
		"""

		Prompts the user to pick or select one or more objects.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		intType : Optional,   Number,   The type(s) of geometry objects (points, curves, surfaces, meshes, etc
		blnGroup : Optional,   Boolean,   Honor object grouping
		blnPreSelect : Optional,   Boolean,   Allow for the selection of pre-selected objects
		blnSelect : Optional,   Boolean,   Specifies whether or not the picked objects will remain selected when the function ends
		arrObjects : Optional,   Array,   An array of strings identifying the objects that are allowed to be selected

		Returns

		Array : An array that contains arrays of selection information if successful. The array of selection information will contain the following:
		Null : If not successful, or on error.

		"""

		pass

	def GetPointCoordinates(self, strMessage, blnPreSelect):
		"""

		Prompts the user to pick or select one or more point objects. Unlike GetObjects, this function does not return an array of point object identifiers. Rather, it returns an array of 3-D point coordinates - one for each selected point object. Note, the array returned is not in any sorted order.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		blnPreSelect : Optional,   Boolean,   Allow for the selection of pre-selected objects

		Returns

		Array : An array of 3-D points, one for each selected point object, if successful.
		Null : If not successful, or on error.

		"""

		pass

	def GetSurfaceObject(self, strMessage, blnPreSelect, blnSelect):
		"""

		Prompts the user to pick, or select, a single surface object.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		blnPreSelect : Optional,   Boolean,   Allow for the selection of pre-selected objects
		blnSelect : Optional,   Boolean,   Select the picked objects

		Returns

		Array : An array of selection information if successful. The array will contain the following information:
		Null : If not successful, or on error.

		"""

		pass

	def HiddenObjects(self, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all hidden objects in the document.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def InvertSelectedObjects(self, blnIncludeLights, blnIncludeGrips):
		"""

		Inverts the current object selection.  The identifiers of the newly selected objects are returned.

		Parameters

		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the newly selected objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LastCreatedObjects(self, blnSelect):
		"""

		Returns the identifiers of the objects that were most recently created or changed by scripting a Rhino command using the Command function.  It is important to call this function immediately after calling the Command function as only the most recently created or changed object identifiers will be returned.

		Parameters

		blnSelect : Optional,   Boolean,   Select the object

		Returns

		Array : An array of strings identifying the most recently created or changed objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LastObject(self, blnSelect, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifier of the last object in the document.  The last object in the document is the first object created by the user.

		Parameters

		blnSelect : Optional,   Boolean,   Select the object
		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		String : The identifier of the object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LockedObjects(self, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all locked objects in the document.  Visible objects are visible and can be snapped to, but they cannot be selected.

		Parameters

		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def NextObject(self, strObject, blnSelect, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifier of the next object in the document.

		Parameters

		strObject : Required,   String,   The identifier of the object from which to get the next object
		blnSelect : Optional,   Boolean,   Select the object
		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		String : The identifier of the object if successful.
		Null : If not successful, or on error.

		"""

		pass

	def NormalObjects(self, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all normal objects in the document.  Normal objects are visible, can be snapped to, and are independent of selection state.

		Parameters

		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectsByColor(self, lngColor, blnSelect, blnIncludeLights):
		"""

		Returns the identifiers of all objects based on the objects' color.  Object colors are represented as RGB colors.   An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

		Parameters

		lngColor : Required,   Number,   An RGB color value
		blnSelect : Optional,   Boolean,   Select the objects
		blnIncludeLights : Optional,   Boolean,   Include light objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectsByGroup(self, strGroup, blnSelect):
		"""

		Returns the identifiers of all objects based on the objects' group name.

		Parameters

		strGroup : Required,   String,   The name of a group of objects
		blnSelect : Optional,   Boolean,   Select the objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectsByLayer(self, strLayer, blnSelect):
		"""

		Returns the identifiers of all objects based on the objects' layer.

		Parameters

		strLayer : Required,   String,   The name of a layer
		blnSelect : Optional,   Boolean,   Select the objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectsByName(self, strName, blnSelect, blnIncludeLights):
		"""

		Returns the identifiers of all objects based on the objects' user-assigned name.

		Parameters

		strName : Required,   String,   The name of an object or objects
		blnSelect : Optional,   Boolean,   Select the objects
		blnIncludeLights : Optional,   Boolean,   Include light objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectsByType(self, intType, blnSelect):
		"""

		Returns the identifiers of all objects based on the objects' geometry type.

		Parameters

		intType : Required,   Number,   The type(s) of geometry objects (points, curves, surfaces, meshes, etc
		blnSelect : Optional,   Boolean,   Select the objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectsByURL(self, strURL, blnSelect, blnIncludeLights):
		"""

		Returns the identifiers of all objects based on the objects' user-assigned URL.

		Parameters

		strURL : Required,   String,   The URL of an object or objects
		blnSelect : Optional,   Boolean,   Select the objects
		blnIncludeLights : Optional,   Boolean,   Include light objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def PrevSelectedObjects(self, blnSelect):
		"""

		Returns the identifiers of the previously selected objects.  The operation of this function is similar to that of Rhino's SelPrev command.

		Parameters

		blnSelect : Optional,   Boolean,   Select the object

		Returns

		Array : An array of strings identifying the previously selected objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ReferenceObjects(self, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all reference objects attached to the document.  An object from a work session reference model is a reference object.  A reference object cannot be modified.  An object is a reference object if, and only if, it is on a reference layer.

		Parameters

		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def SelectedObjects(self, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all objects that are currently selected.

		Parameters

		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnselectAllObjects(self):
		"""

		Unselects all objects in the document.

		No parameters

		Returns

		Number : The number of objects that were unselected.

		"""

		pass

	def UnselectedObjects(self, blnSelect, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all objects that are currently unselected.

		Parameters

		blnSelect : Optional,   Boolean,   Select the objects
		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass

	def VisibleObjects(self, strView, blnSelect, blnIncludeLights, blnIncludeGrips):
		"""

		Returns the identifiers of all objects that are visible in a specified view.

		Parameters

		strView : Optional,   String,   The title of the view
		blnSelect : Optional,   Boolean,   Select the objects
		blnIncludeLights : Optional,   Boolean,   Include light objects
		blnIncludeGrips : Optional,   Boolean,   Include grips objects

		Returns

		Array : An array of strings identifying the objects if successful.
		Null : If not successful, or on error.

		"""

		pass
