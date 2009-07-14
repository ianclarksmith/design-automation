# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class LayerState(DispatchBaseClass):



	def IsLayerState(self, strState):
		"""

		Verifies the existence of a layer state in the document.

		Parameters

		strState : Required,   String,   The name of an existing layer state

		Returns

		Null : On error.

		"""

		pass

	def RestoreLayerState(self, strState, intMode):
		"""

		Restores a previously saved layer state.

		Parameters

		strState : Required,   String,   The name of an existing layer state
		intMode : Required,   Number,   The layer properties you want restored

		Returns

		Boolean : True or False indicating success of failure.
		Null : If not successful, or on error.

		"""

		pass

	def LayerStateCount(self):
		"""

		Returns the number of layer states in the document.

		No parameters

		Returns

		Number : The number of layer states in the document.

		"""

		pass

	def ExportLayerStates(self, strFilename):
		"""

		Exports all layer states to an external file.

		Parameters

		strFilename : Required,   String,   The name of an file to create

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def RenameLayerState(self, strOldState, strNewState):
		"""

		Renames an existing layer state.

		Parameters

		strOldState : Required,   String,   The name of an existing layer state
		strNewState : Required,   String,   The new layer name

		Returns

		Boolean : True or False indicating success of failure.
		Null : If not successful, or on error.

		"""

		pass

	def ImportLayerStates(self, strFilename):
		"""

		Imports layer states from a previously exported layer state file.

		Parameters

		strFilename : Required,   String,   The name of an existing layer state file to import

		Returns

		Number : The number of layer states imported if successful.
		Null : On error.

		"""

		pass

	def DeleteLayerState(self, strState):
		"""

		Removes an existing layer state from the document.

		Parameters

		strState : Required,   String,   The name of an existing layer state

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def LayerStateNames(self, blnSort):
		"""

		Returns the names of all layer states in the document.

		Parameters

		blnSort : Optional,   Boolean,   If not specified or True, then the layer state names are sorted in ascending order

		Returns

		Array : An array of layer state names if successful.
		Null : If not successful, or on error.

		"""

		pass

	def SaveLayerState(self, strState):
		"""

		Saves the current state of the layers in the document.

		Parameters

		strState : Optional,   String,   The name of the layer state

		Returns

		String : The name of the new or updated layer state if successful.
		Null : On error.

		"""

		pass

