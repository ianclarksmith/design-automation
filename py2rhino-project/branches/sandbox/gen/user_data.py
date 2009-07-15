# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class UserData(DispatchBaseClass):



	def attributedatacount(self, strobject):
		"""

		Returns the number of RhinoScript user data items on an object's attributes.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Number : The number of RhinoScript object user data items if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AttributeDataCount', None, strObject)

	def deleteattributedata(self, strobject, strsection, strentry):
		"""

		Removes RhinoScript user data items from an object's attributes.

		Parameters

		strObject : Required,   String,   The object's identifier
		strSection : Optional,   String,   The section name
		strEntry : Optional,   String,   The entry name

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteAttributeData', None, strObject, strSection, strEntry)

	def deletedocumentdata(self, strsection, strentry):
		"""

		Removes RhinoScript user data items from the current document.

		Parameters

		strSection : Optional,   String,   The section name
		strEntry : Optional,   String,   The entry name

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteDocumentData', None, strSection, strEntry)

	def deleteobjectdata(self, strobject, strsection, strentry):
		"""

		Removes RhinoScript user data items from an object's geometry.

		Parameters

		strObject : Required,   String,   The object's identifier
		strSection : Optional,   String,   The section name
		strEntry : Optional,   String,   The entry name

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteObjectData', None, strObject, strSection, strEntry)

	def documentdatacount(self, ):
		"""

		Returns the number of RhinoScript user data items in the current document.

		No parameters

		Returns

		Number : The number of RhinoScript document user data items.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DocumentDataCount', None, )

	def getattributedata(self, strobject, strsection, strentry):
		"""

		Returns a RhinoScript user data item from an object's attributes.

		Parameters

		strObject : Required,   String,   The object's identifier
		strSection : Optional,   String,   The section name
		strEntry : Optional,   String,   The entry name

		Returns

		Array : A zero-based, one-dimensional array of all section names if strSection is not specified.
		Array : A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.
		String : The value of the entry if both strSection and strEntry are specified.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'GetAttributeData', None, strObject, strSection, strEntry)

	def getdocumentdata(self, strsection, strentry):
		"""

		Returns a RhinoScript user data item from the current document.

		Parameters

		strSection : Optional,   String,   The section name
		strEntry : Optional,   String,   The entry name

		Returns

		Array : A zero-based, one-dimensional array of all section names if strSection is not specified.
		Array : A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.
		String : The value of the entry if both strSection and strEntry are specified.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'GetDocumentData', None, strSection, strEntry)

	def getobjectdata(self, strobject, strsection, strentry):
		"""

		Returns a RhinoScript user data item from an object's geometry.

		Parameters

		strObject : Required,   String,   The object's identifier
		strSection : Optional,   String,   The section name
		strEntry : Optional,   String,   The entry name

		Returns

		Array : A zero-based, one-dimensional array of all section names if strSection is not specified.
		Array : A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.
		String : The value of the entry if both strSection and strEntry are specified.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'GetObjectData', None, strObject, strSection, strEntry)

	def getusertext(self, strobject, strkey, blnattachtogeometry):
		"""

		Returns User Text that is stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.

		Parameters

		strObject : Required,   String,   The object's identifier
		strKey : Optional,   String,   The key name
		blnAttachToGeometry : Optional,   Boolean,   The location on the object to retrieve the User Text

		Returns

		String : If strKey is specified, then the associated value if successful.
		Array : If strKey is not specified, then an array of key names if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'GetUserText', None, strObject, strKey, blnAttachToGeometry)

	def isattributedata(self, strobject):
		"""

		Verifies that an object's attributes contains RhinoScript user data.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Boolean : True or False indicating whether or not the object's attributes contains any RhinoScript user data if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsAttributeData', None, strObject)

	def isdocumentdata(self, ):
		"""

		Verifies that the current document contains RhinoScript user data.

		No parameters

		Returns

		Boolean : True or False indicating whether or not the current document contains any RhinoScript document user data.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsDocumentData', None, )

	def isobjectdata(self, strobject):
		"""

		Verifies that an object's geometry contains RhinoScript user data.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Boolean : True or False indicating whether or not the object's geometry contains any RhinoScript user data if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsObjectData', None, strObject)

	def isusertext(self, strobject):
		"""

		Verifies that an object contains user text. For more details on User Text, see the discussion found in the User Data Methods summary.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Number : 0 = no user text; 1 = attribute user text; 2 = geometry user text; 3 = both attribute and geometry user text.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsUserText', None, strObject)

	def objectdatacount(self, strobject):
		"""

		Returns the number of RhinoScript user data items on an object's geometry.

		Parameters

		strObject : Required,   String,   The object's identifier

		Returns

		Number : The number of RhinoScript object user data items if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ObjectDataCount', None, strObject)

	def setattributedata(self, strobject, strsection, strentry, strvalue):
		"""

		Adds or sets a RhinoScript user data item to an object's attributes.

		Parameters

		strObject : Required,   String,   The object's identifier
		strSection : Required,   String,   The application name
		strEntry : Required,   String,   The key name
		strValue : Required,   String,   The string value

		Returns

		String : The previous value if successful.
		Null : If no previous value exits, if not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SetAttributeData', None, strObject, strSection, strEntry, strValue)

	def setdocumentdata(self, strsection, strentry, strvalue):
		"""

		Adds or sets a RhinoScript user data item to the current document.

		Parameters

		strSection : Required,   String,   The section name
		strEntry : Required,   String,   The entry name
		strValue : Required,   String,   The string value

		Returns

		String : The previous value if successful.
		Null : If no previous value exits, if not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SetDocumentData', None, strSection, strEntry, strValue)

	def setobjectdata(self, strobject, strsection, strentry, strvalue):
		"""

		Adds or sets a RhinoScript user data item to an object's geometry.

		Parameters

		strObject : Required,   String,   The object's identifier
		strSection : Required,   String,   The application name
		strEntry : Required,   String,   The key name
		strValue : Required,   String,   The string value

		Returns

		String : The previous value if successful.
		Null : If no previous value exits, if not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SetObjectData', None, strObject, strSection, strEntry, strValue)

	def setusertext(self, strobject, strkey, strvalue, blnattachtogeometry):
		"""

		Sets or removes user text stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.

		Parameters

		strObject : Required,   String,   The object's identifier
		strKey : Required,   String,   The key name to set
		strValue : Optional,   String,   The string value to set
		blnAttachToGeometry : Optional,   Boolean,   The location on the object to store the User Text

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SetUserText', None, strObject, strKey, strValue, blnAttachToGeometry)

