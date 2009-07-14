# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class ObjectGrip(DispatchBaseClass):



	def ObjectGripLocations(self, strObject, arrPoints):
		"""

		Returns or modifies the location of all grips owned by an object. The locations of the grips are returned in an array of 3-D points with each position in the array corresponding to that grip's index. To modify the locations of grips, you must provide an array of 3-D points that contains the same number of points at grips.

		Parameters

		strObject : Required,   String,   The identifier of the object
		arrPoints : Optional,   Array,   An array of 3-D points identifying the new locations of the grips

		Returns

		Array : If arrPoints is not specified, the current location of all grips if successful.
		Array : If arrPoints is specified, the previous location of all grips if successful.
		Null : If not successful, or on error.

		"""

		pass

	def PrevObjectGrip(self, strObject, intIndex, intDirection, blnEnable):
		"""

		Returns the previous grip index from a specified grip index of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		intIndex : Required,  Number,  The zero-based grip index from which to get the previous grip index
		intDirection : Optional,   Number,   The direction to get the previous grip index, either 0=U or 1=V
		blnEnable : Optional,   Boolean,   If True (default), the previous grip index found will be selected

		Returns

		Number : The index of the next grip from the specified grip index.
		Null : If not successful, or on error.

		"""

		pass

	def SelectObjectGrip(self, strObject, intIndex):
		"""

		Selects a single grip owned by an object. If the object's grips are not turned on, grips will  not be selected.

		Parameters

		strObject : Required,   String,   The identifier of the object
		intIndex : Required,  Number,  The zero-based grip index to select

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def NextObjectGrip(self, strObject, intIndex, intDirection, blnEnable):
		"""

		Returns the next grip index from a specified grip index of an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		intIndex : Required,  Number,  The zero-based grip index from which to get the next grip index
		intDirection : Optional,   Number,   The direction to get the next grip index, either 0=U or 1=V
		blnEnable : Optional,   Boolean,   If True (default), the next grip index found will be selected

		Returns

		Number : The index of the next grip from the specified grip index.
		Null : If not successful, or on error.

		"""

		pass

	def SelectedObjectGrips(self, strObject):
		"""

		Returns an array of grip indices identifying an object's selected grips.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Array : An array of zero-based grip indices identifying the selected grips.
		Null : If not successful, or on error.

		"""

		pass

	def EnableObjectGrips(self, strObject, blnEnable):
		"""

		Enables or disables an object's grips. For curves and surfaces, these are also called control points.

		Parameters

		strObject : Required,   String,   The identifier of the object
		blnEnable : Optional,   Boolean,   If True (default), the specified object's grips will be turned on

		Returns

		Boolean : True of False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def GetObjectGrips(self, strMessage, blnPreSelect, blnSelect):
		"""

		Prompts the user to pick or select one or more object grips from one or more objects.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		blnPreSelect : Optional,   Boolean,   Allow for the selection of a pre-selected object grips
		blnSelect : Optional,   Boolean,   Select the picked object grips

		Returns

		Array : A one-dimensional array containing one or more object grip records if successful. An object grip record itself is a one-dimensional array that contains the following three elements:
		String : The identifier of the object that owns the grip.
		Number : The zero-based index value of the grip.
		Array : A 3-D point identifying the location of the grip.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectGripLocation(self, strObject, intIndex, arrPoint):
		"""

		Returns or modifies the location of an object's grip.

		Parameters

		strObject : Required,   String,   The identifier of the object
		intIndex : Required,  Number,  The zero-based index of the grip to either query or modify
		arrPoint : Optional,   Array,   A 3-D point identifying the new location of the grip

		Returns

		Array : If arrPoint is not specified, the current location of the grip referenced by intIndex if successful.
		Array : If arrPoint is specified, the previous location of the grip referenced by intIndex if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectGripsSelected(self, strObject):
		"""

		Verifies that an object's grips are turned on and at least one grip is selected.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Boolean : True of False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectGripCount(self, strObject):
		"""

		Returns the number of grips owned by an object.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Number : The number of grips if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnselectObjectGrips(self, strObject):
		"""

		Unselects an object's grips. Note, the grips will not be turned off.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Number : The number of grips unselected if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ObjectGripsOn(self, strObject):
		"""

		Verifies that an object's grips are turned on.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Boolean : True of False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def GetObjectGrip(self, strMessage, blnPreSelect, blnSelect):
		"""

		Prompts the user to pick or select a single object grip.

		Parameters

		strMessage : Optional,   String,   A prompt or message
		blnPreSelect : Optional,   Boolean,   Allow for the selection of a pre-selected object grip
		blnSelect : Optional,   Boolean,   Select the picked object grip

		Returns

		Array : A one-dimensional array containing the following three elements if successful:
		String : The identifier of the object that owns the grip.
		Number : The zero-based index value of the grip.
		Array : A 3-D point identifying the location of the grip.
		Null : If not successful, or on error.

		"""

		pass

	def SelectObjectGrips(self, strObject):
		"""

		Selects an object's grips. If the object's grips are not turned on, they will not be selected.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Number : The number of grips selected if successful.
		Null : If not successful, or on error.

		"""

		pass

	def UnselectObjectGrip(self, strObject, intIndex):
		"""

		Unselects a single grip owned by an object.

		Parameters

		strObject : Required,   String,   The identifier of the object
		intIndex : Required,  Number,  The zero-based grip index to unselect

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

