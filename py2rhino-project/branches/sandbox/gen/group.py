# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Group(DispatchBaseClass):



	def AddGroup(self, strGroup):
		"""

		Adds a new empty group to the document.

		Parameters

		strGroup : Optional,   String,   The name of the new group

		Returns

		String : The name of the new group if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AddObjectToGroup(self, strObject, strGroup):
		"""

		Adds a single object to an existing group. Neither the object nor the group can be reference objects.

		Parameters

		strObject : Required,   String,   The identifier of the object to add to the group
		strGroup : Required,   String,   The name of an existing group

		Returns

		Boolean : True or False indicating success or failure
		Null : On error.

		"""

		pass

	def AddObjectsToGroup(self, arrObjects, strGroup):
		"""

		Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.

		Parameters

		arrObjects : Required,   Array,   An array of object identifiers
		strGroup : Required,   String,   The name of an existing group

		Returns

		Number : The number of objects added to the group if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteGroup(self, strGroup):
		"""

		Removes an existing group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects.

		Parameters

		strGroup : Required,   String,   The name of an existing group

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def GroupCount(self):
		"""

		Returns the number of groups in the document.

		No parameters

		Returns

		Number : The number of groups if successful.
		Null : If not successful, or on error.

		"""

		pass

	def GroupNames(self):
		"""

		Returns the name of all the groups in the document.

		No parameters

		Returns

		Array : An array of group names if successful.
		Null : If not successful, or on error.

		"""

		pass

	def HideGroup(self, strGroup):
		"""

		Hides a group of object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		strGroup : Required,   String,   The name of an existing group

		Returns

		Number : The number of object that were hidden if successful.
		Null : On error.

		"""

		pass

	def IsGroup(self, strGroup):
		"""

		Verifies the existence of a group.

		Parameters

		strGroup : Required,   String,   The name of an existing group

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def IsGroupEmpty(self, strGroup):
		"""

		Verifies that an existing group is empty, or contains no object members.

		Parameters

		strGroup : Required,   String,   The name of an existing group

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def LockGroup(self, strGroup):
		"""

		Locks a group of objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

		Parameters

		strGroup : Required,   String,   The name of an existing group

		Returns

		Number : The number of object that were locked if successful.
		Null : On error.

		"""

		pass

	def RemoveObjectFromAllGroups(self, strObject):
		"""

		Removes a single object from any and all groups that it is a member. Neither the object nor the group can be a reference object.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def RemoveObjectFromGroup(self, strObject, strGroup):
		"""

		Removes a single object from an existing group.

		Parameters

		strObject : Required,   String,   The identifier of the object
		strGroup : Required,   String,   The name of an existing group

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def RemoveObjectFromTopGroup(self, strObject):
		"""

		Removes a single object from it's top-most group.

		Parameters

		strObject : Required,   String,   The identifier of the object

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def RemoveObjectsFromGroup(self, arrObjects, strGroup):
		"""

		Removes one or more objects from an existing group.

		Parameters

		arrObjects : Required,   Array,   An array of object identifiers
		strGroup : Required,   String,   The name of an existing group

		Returns

		Number : The number of objects removed from the group if successful.
		Null : If not successful, or on error.

		"""

		pass

	def RenameGroup(self, strOldGroup, strNewGroup):
		"""

		Renames an existing group.

		Parameters

		strOldGroup : Required,   String,   The name of an existing group
		strNewGroup : Required,   String,   The new group name

		Returns

		String : The new group name if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ShowGroup(self, strGroup):
		"""

		Shows a group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

		Parameters

		strGroup : Required,   String,   The name of an existing group

		Returns

		Number : The number of object that were shown if successful.
		Null : On error.

		"""

		pass

	def UnlockGroup(self, strGroup):
		"""

		Unlocks a group of locked objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

		Parameters

		strGroup : Required,   String,   The name of an existing group

		Returns

		Number : The number of object that were unlocked if successful.
		Null : On error.

		"""

		pass

