# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class Group(IRhinoScript):



    def add_group(self, group):
        """

        Adds a new empty group to the document.

        Parameters

        Group : Optional, String, str, String

        Returns

        String : The name of the new group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(133, 1, (12, 0), ((8, 0),), u'AddGroup', None, group)

    def add_object_to_group(self, object, group):
        """

        Adds a single object to an existing group. Neither the object nor the group can be reference objects.

        Parameters

        Object : Required, String, str, String
        Group : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure
        Null : On error.

        """

        return self._ApplyTypes_(134, 1, (12, 0), ((8, 0), (8, 0),), u'AddObjectToGroup', None, object, group)

    def add_objects_to_group(self, objects, group):
        """

        Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.

        Parameters

        Objects : Required, Array, arrdbl, Array of ?
        Group : Required, String, str, String

        Returns

        Number : The number of objects added to the group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(135, 1, (12, 0), ((8197, 0), (8, 0),), u'AddObjectsToGroup', None, _utils.flatten(objects), group)

    def delete_group(self, group):
        """

        Removes an existing group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects.

        Parameters

        Group : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(136, 1, (12, 0), ((8, 0),), u'DeleteGroup', None, group)

    def group_count(self):
        """

        Returns the number of groups in the document.

        No parameters

        Returns

        Number : The number of groups if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(137, 1, (12, 0), (,), u'GroupCount', None, )

    def group_names(self):
        """

        Returns the name of all the groups in the document.

        No parameters

        Returns

        Array : An array of group names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(138, 1, (12, 0), (,), u'GroupNames', None, )

    def hide_group(self, group):
        """

        Hides a group of object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        Group : Required, String, str, String

        Returns

        Number : The number of object that were hidden if successful.
        Null : On error.

        """

        return self._ApplyTypes_(871, 1, (12, 0), ((8, 0),), u'HideGroup', None, group)

    def is_group(self, group):
        """

        Verifies the existence of a group.

        Parameters

        Group : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(139, 1, (12, 0), ((8, 0),), u'IsGroup', None, group)

    def is_group_empty(self, group):
        """

        Verifies that an existing group is empty, or contains no object members.

        Parameters

        Group : Required, String, str, String

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(140, 1, (12, 0), ((8, 0),), u'IsGroupEmpty', None, group)

    def lock_group(self, group):
        """

        Locks a group of objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        Group : Required, String, str, String

        Returns

        Number : The number of object that were locked if successful.
        Null : On error.

        """

        return self._ApplyTypes_(873, 1, (12, 0), ((8, 0),), u'LockGroup', None, group)

    def remove_object_from_all_groups(self, object):
        """

        Removes a single object from any and all groups that it is a member. Neither the object nor the group can be a reference object.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(141, 1, (12, 0), ((8, 0),), u'RemoveObjectFromAllGroups', None, object)

    def remove_object_from_group(self, object, group):
        """

        Removes a single object from an existing group.

        Parameters

        Object : Required, String, str, String
        Group : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(142, 1, (12, 0), ((8, 0), (8, 0),), u'RemoveObjectFromGroup', None, object, group)

    def remove_object_from_top_group(self, object):
        """

        Removes a single object from it's top-most group.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(143, 1, (12, 0), ((8, 0),), u'RemoveObjectFromTopGroup', None, object)

    def remove_objects_from_group(self, objects, group):
        """

        Removes one or more objects from an existing group.

        Parameters

        Objects : Required, Array, arrdbl, Array of ?
        Group : Required, String, str, String

        Returns

        Number : The number of objects removed from the group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(144, 1, (12, 0), ((8197, 0), (8, 0),), u'RemoveObjectsFromGroup', None, _utils.flatten(objects), group)

    def rename_group(self, old_group, new_group):
        """

        Renames an existing group.

        Parameters

        OldGroup : Required, String, str, String
        NewGroup : Required, String, str, String

        Returns

        String : The new group name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(145, 1, (12, 0), ((8, 0), (8, 0),), u'RenameGroup', None, old_group, new_group)

    def show_group(self, group):
        """

        Shows a group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        Group : Required, String, str, String

        Returns

        Number : The number of object that were shown if successful.
        Null : On error.

        """

        return self._ApplyTypes_(872, 1, (12, 0), ((8, 0),), u'ShowGroup', None, group)

    def unlock_group(self, group):
        """

        Unlocks a group of locked objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        Group : Required, String, str, String

        Returns

        Number : The number of object that were unlocked if successful.
        Null : On error.

        """

        return self._ApplyTypes_(874, 1, (12, 0), ((8, 0),), u'UnlockGroup', None, group)

