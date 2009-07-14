# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Toolbar(DispatchBaseClass):



	def ToolbarCollectionCount(self):
		"""

		Returns the number of currently open toolbar collections.

		No parameters

		Returns

		Number : The number of currently open toolbar collections if successful.
		Null : If not successful, or on error.

		"""

		pass

	def SaveToolbarCollection(self, strName):
		"""

		Saves an open toolbar collection to disk.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def AddToolbarCollection(self, strFile):
		"""

		Create new toolbar collection file with no toolbars.

		Parameters

		strFile : Required,   String,   The filename of the toolbar collection to create

		Returns

		String : The name, or alias, of the newly created toolbar collection if successful.
		Null : On error.

		"""

		pass

	def ToolbarCollectionPath(self, strName):
		"""

		Returns the full path to a currently open toolbar collection file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		String : The full path to the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsToolBar(self, strName, strToolbar):
		"""

		Verifies that a toolbar exists in a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to verify

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def OpenToolbarCollection(self, strFile):
		"""

		Opens an existing toolbar collection file.

		Parameters

		strFile : Required,   String,   The full path to the toolbar collection file to open

		Returns

		String : The Rhino-assigned name of the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsToolbarCollection(self, strFile):
		"""

		Verifies that a toolbar collection is open.

		Parameters

		strFile : Required,   String,   The full path to the toolbar collection file to verify

		Returns

		String : The Rhino-assigned name of the toolbar collection if successful..
		Null : If not successful, or on error.

		"""

		pass

	def CloseToolbarCollection(self, strName, blnPrompt):
		"""

		Closes a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		blnPrompt : Optional,   Boolean,   If True,  then the user will be prompted to save the collection file if it has been modified prior to closing

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def IsToolBarVisible(self, strName, strToolbar):
		"""

		Verifies that a toolbar in a currently open toolbar collection is visible.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to verify

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def AddToolbarButton(self, strName, strToolbar):
		"""

		Add a new button to specified toolbar.  The new button will be completely blank.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to add a button

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def ToolBarNames(self, strName):
		"""

		Returns the names of all toolbars found in a currently open toolbar collection file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		Array : The names of all toolbars in the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsToolbarDocked(self, strName, strToolbar):
		"""

		Verifies that a visible toolbar in a currently open toolbar collection is docked.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to verify

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def HideToolBar(self, strName, strToolbar):
		"""

		Hides a previously visible toolbar in a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to hide

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def DeleteToolbar(self, strName, strToolbar):
		"""

		Deletes a toolbar from an open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to remove

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def ShowToolBar(self, strName, strToolbar):
		"""

		Shows a previously hidden toolbar in a currently open toolbar collection.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to show

		Returns

		Boolean : True or false indicating success or failure.
		Null : On error.

		"""

		pass

	def SaveToolbarCollectionAs(self, strName, strFile):
		"""

		Saves an open toolbar collection to a different disk file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strFile : Required,   String,   The full path to the toolbar collection file to create

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def ToolBarCount(self, strName):
		"""

		Returns the number of toolbars found in a currently open toolbar collection file.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection

		Returns

		Number : The number of toolbars in the toolbar collection if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddToolbar(self, strName, strToolbar):
		"""

		Create new toolbar with one blank button.

		Parameters

		strName : Required,   String,   The name of a currently open toolbar collection
		strToolbar : Required,   String,   The name of a toolbar in the collection to add

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def ToolbarCollectionNames(self):
		"""

		Returns the name of all currently open toolbar collections.

		No parameters

		Returns

		Array : The names of all currently open toolbar collections if successful.
		Null : If not successful, or on error.

		"""

		pass

