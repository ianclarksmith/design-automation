# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Toolbar(DispatchBaseClass):



	def addtoolbar(self, strname, strtoolbar):
		"""

		Create new toolbar with one blank button.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to add

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddToolbar', None, strName, strToolbar)

	def addtoolbarbutton(self, strname, strtoolbar):
		"""

		Add a new button to specified toolbar.  The new button will be completely blank.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to add a button

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddToolbarButton', None, strName, strToolbar)

	def addtoolbarcollection(self, strfile):
		"""

		Create new toolbar collection file with no toolbars.

		Parameters

		strFile : Required,   String,   The filename of the toolbar collection to create

		Returns

		String : The name, or alias, of the newly created toolbar collection if successful.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'AddToolbarCollection', None, strFile)

	def closetoolbarcollection(self, strname, blnprompt):
		"""

		Closes a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		blnPrompt : Optional,   Boolean,   If True,  then the user will be prompted to save the collection file if it has been modified prior to closing

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'CloseToolbarCollection', None, strName, blnPrompt)

	def deletetoolbar(self, strname, strtoolbar):
		"""

		Deletes a toolbar from an open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to remove

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteToolbar', None, strName, strToolbar)

	def hidetoolbar(self, strname, strtoolbar):
		"""

		Hides a previously visible toolbar in a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to hide

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'HideToolBar', None, strName, strToolbar)

	def istoolbar(self, strname, strtoolbar):
		"""

		Verifies that a toolbar exists in a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to verify

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsToolBar', None, strName, strToolbar)

	def istoolbarvisible(self, strname, strtoolbar):
		"""

		Verifies that a toolbar in a currently open toolbar collection is visible.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to verify

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsToolBarVisible', None, strName, strToolbar)

	def istoolbarcollection(self, strfile):
		"""

		Verifies that a toolbar collection is open.

		Parameters

		strFile : Required,   String,   The full path to the toolbar collection file to verify

		Returns

		String : The Rhino-assigned name of the toolbar collection if successful..
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsToolbarCollection', None, strFile)

	def istoolbardocked(self, strname, strtoolbar):
		"""

		Verifies that a visible toolbar in a currently open toolbar collection is docked.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to verify

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'IsToolbarDocked', None, strName, strToolbar)

	def opentoolbarcollection(self, strfile):
		"""

		Opens an existing toolbar collection file.

		Parameters

		strFile : Required,   String,   The full path to the toolbar collection file to open

		Returns

		String : The Rhino-assigned name of the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'OpenToolbarCollection', None, strFile)

	def savetoolbarcollection(self, strname):
		"""

		Saves an open toolbar collection to disk.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SaveToolbarCollection', None, strName)

	def savetoolbarcollectionas(self, strname, strfile):
		"""

		Saves an open toolbar collection to a different disk file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strFile : Required,   String,   The full path to the toolbar collection file to create

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'SaveToolbarCollectionAs', None, strName, strFile)

	def showtoolbar(self, strname, strtoolbar):
		"""

		Shows a previously hidden toolbar in a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to show

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ShowToolBar', None, strName, strToolbar)

	def toolbarcount(self, strname):
		"""

		Returns the number of toolbars found in a currently open toolbar collection file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		Number : The number of toolbars in the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ToolBarCount', None, strName)

	def toolbarnames(self, strname):
		"""

		Returns the names of all toolbars found in a currently open toolbar collection file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		Array : The names of all toolbars in the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ToolBarNames', None, strName)

	def toolbarcollectioncount(self, ):
		"""

		Returns the number of currently open toolbar collections.

		No parameters

		Returns

		Number : The number of currently open toolbar collections if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ToolbarCollectionCount', None, )

	def toolbarcollectionnames(self, ):
		"""

		Returns the name of all currently open toolbar collections.

		No parameters

		Returns

		Array : The names of all currently open toolbar collections if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ToolbarCollectionNames', None, )

	def toolbarcollectionpath(self, strname):
		"""

		Returns the full path to a currently open toolbar collection file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		String : The full path to the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		return self._ApplyTypes_(id, 1, (returns), (params), u'ToolbarCollectionPath', None, strName)

