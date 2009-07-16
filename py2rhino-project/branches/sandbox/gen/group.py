# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Group(DispatchBaseClass):



    def add_group(self, str_group):
        """

        Adds a new empty group to the document.

        Parameters

        strGroup : Optional, String, The name of the new group

        Returns

        String : The name of the new group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddGroup', None, strGroup)

    def add_object_to_group(self, str_object, str_group):
        """

        Adds a single object to an existing group. Neither the object nor the group can be reference objects.

        Parameters

        strObject : Required, String, The identifier of the object to add to the group
        strGroup : Required, String, The name of an existing group

        Returns

        Boolean : True or False indicating success or failure
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddObjectToGroup', None, strObject, strGroup)

    def add_objects_to_group(self, arr_objects, str_group):
        """

        Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.

        Parameters

        arrObjects : Required, Array, An array of object identifiers
        strGroup : Required, String, The name of an existing group

        Returns

        Number : The number of objects added to the group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddObjectsToGroup', None, arrObjects, strGroup)

    def delete_group(self, str_group):
        """

        Removes an existing group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects.

        Parameters

        strGroup : Required, String, The name of an existing group

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteGroup', None, strGroup)

    def group_count(self):
        """

        Returns the number of groups in the document.

        No parameters

        Returns

        Number : The number of groups if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GroupCount', None, )

    def group_names(self):
        """

        Returns the name of all the groups in the document.

        No parameters

        Returns

        Array : An array of group names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GroupNames', None, )

    def hide_group(self, str_group):
        """

        Hides a group of object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        strGroup : Required, String, The name of an existing group

        Returns

        Number : The number of object that were hidden if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'HideGroup', None, strGroup)

    def is_group(self, str_group):
        """

        Verifies the existence of a group.

        Parameters

        strGroup : Required, String, The name of an existing group

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsGroup', None, strGroup)

    def is_group_empty(self, str_group):
        """

        Verifies that an existing group is empty, or contains no object members.

        Parameters

        strGroup : Required, String, The name of an existing group

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsGroupEmpty', None, strGroup)

    def lock_group(self, str_group):
        """

        Locks a group of objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        strGroup : Required, String, The name of an existing group

        Returns

        Number : The number of object that were locked if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LockGroup', None, strGroup)

    def remove_object_from_all_groups(self, str_object):
        """

        Removes a single object from any and all groups that it is a member. Neither the object nor the group can be a reference object.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectFromAllGroups', None, strObject)

    def remove_object_from_group(self, str_object, str_group):
        """

        Removes a single object from an existing group.

        Parameters

        strObject : Required, String, The identifier of the object
        strGroup : Required, String, The name of an existing group

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectFromGroup', None, strObject, strGroup)

    def remove_object_from_top_group(self, str_object):
        """

        Removes a single object from it's top-most group.

        Parameters

        strObject : Required, String, The identifier of the object

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectFromTopGroup', None, strObject)

    def remove_objects_from_group(self, arr_objects, str_group):
        """

        Removes one or more objects from an existing group.

        Parameters

        arrObjects : Required, Array, An array of object identifiers
        strGroup : Required, String, The name of an existing group

        Returns

        Number : The number of objects removed from the group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectsFromGroup', None, arrObjects, strGroup)

    def rename_group(self, str_old_group, str_new_group):
        """

        Renames an existing group.

        Parameters

        strOldGroup : Required, String, The name of an existing group
        strNewGroup : Required, String, The new group name

        Returns

        String : The new group name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RenameGroup', None, strOldGroup, strNewGroup)

    def show_group(self, str_group):
        """

        Shows a group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        strGroup : Required, String, The name of an existing group

        Returns

        Number : The number of object that were shown if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShowGroup', None, strGroup)

    def unlock_group(self, str_group):
        """

        Unlocks a group of locked objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        strGroup : Required, String, The name of an existing group

        Returns

        Number : The number of object that were unlocked if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'UnlockGroup', None, strGroup)

