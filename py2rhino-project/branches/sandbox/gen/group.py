# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Group(DispatchBaseClass):



    def addgroup(self, strgroup):
        """

        Adds a new empty group to the document.

        Parameters

        strGroup : Optional,   String,   The name of the new group

        Returns

        String : The name of the new group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddGroup', None, strGroup)

    def addobjecttogroup(self, strobject, strgroup):
        """

        Adds a single object to an existing group. Neither the object nor the group can be reference objects.

        Parameters

        strObject : Required,   String,   The identifier of the object to add to the group
        strGroup : Required,   String,   The name of an existing group

        Returns

        Boolean : True or False indicating success or failure
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddObjectToGroup', None, strObject, strGroup)

    def addobjectstogroup(self, arrobjects, strgroup):
        """

        Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.

        Parameters

        arrObjects : Required,   Array,   An array of object identifiers
        strGroup : Required,   String,   The name of an existing group

        Returns

        Number : The number of objects added to the group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'AddObjectsToGroup', None, arrObjects, strGroup)

    def deletegroup(self, strgroup):
        """

        Removes an existing group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects.

        Parameters

        strGroup : Required,   String,   The name of an existing group

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'DeleteGroup', None, strGroup)

    def groupcount(self, ):
        """

        Returns the number of groups in the document.

        No parameters

        Returns

        Number : The number of groups if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GroupCount', None, )

    def groupnames(self, ):
        """

        Returns the name of all the groups in the document.

        No parameters

        Returns

        Array : An array of group names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GroupNames', None, )

    def hidegroup(self, strgroup):
        """

        Hides a group of object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        strGroup : Required,   String,   The name of an existing group

        Returns

        Number : The number of object that were hidden if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'HideGroup', None, strGroup)

    def isgroup(self, strgroup):
        """

        Verifies the existence of a group.

        Parameters

        strGroup : Required,   String,   The name of an existing group

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsGroup', None, strGroup)

    def isgroupempty(self, strgroup):
        """

        Verifies that an existing group is empty, or contains no object members.

        Parameters

        strGroup : Required,   String,   The name of an existing group

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsGroupEmpty', None, strGroup)

    def lockgroup(self, strgroup):
        """

        Locks a group of objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        strGroup : Required,   String,   The name of an existing group

        Returns

        Number : The number of object that were locked if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LockGroup', None, strGroup)

    def removeobjectfromallgroups(self, strobject):
        """

        Removes a single object from any and all groups that it is a member. Neither the object nor the group can be a reference object.

        Parameters

        strObject : Required,   String,   The identifier of the object

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectFromAllGroups', None, strObject)

    def removeobjectfromgroup(self, strobject, strgroup):
        """

        Removes a single object from an existing group.

        Parameters

        strObject : Required,   String,   The identifier of the object
        strGroup : Required,   String,   The name of an existing group

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectFromGroup', None, strObject, strGroup)

    def removeobjectfromtopgroup(self, strobject):
        """

        Removes a single object from it's top-most group.

        Parameters

        strObject : Required,   String,   The identifier of the object

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectFromTopGroup', None, strObject)

    def removeobjectsfromgroup(self, arrobjects, strgroup):
        """

        Removes one or more objects from an existing group.

        Parameters

        arrObjects : Required,   Array,   An array of object identifiers
        strGroup : Required,   String,   The name of an existing group

        Returns

        Number : The number of objects removed from the group if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RemoveObjectsFromGroup', None, arrObjects, strGroup)

    def renamegroup(self, stroldgroup, strnewgroup):
        """

        Renames an existing group.

        Parameters

        strOldGroup : Required,   String,   The name of an existing group
        strNewGroup : Required,   String,   The new group name

        Returns

        String : The new group name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RenameGroup', None, strOldGroup, strNewGroup)

    def showgroup(self, strgroup):
        """

        Shows a group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters

        strGroup : Required,   String,   The name of an existing group

        Returns

        Number : The number of object that were shown if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ShowGroup', None, strGroup)

    def unlockgroup(self, strgroup):
        """

        Unlocks a group of locked objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.

        Parameters

        strGroup : Required,   String,   The name of an existing group

        Returns

        Number : The number of object that were unlocked if successful.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'UnlockGroup', None, strGroup)

