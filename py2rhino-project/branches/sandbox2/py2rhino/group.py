# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Group(IRhinoScript):



    def add_group(self, group):
        """        
        Adds a new empty group to the document.
    
        Parameters
        ==========

        group, String, Optional        
        The name of the new group.  If omitted, Rhino automatically generates the group name.
            
        Returns
        =======

        string
        The name of the new group if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(133, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"AddGroup", None, group)

    def add_object_to_group(self, object, group):
        """        
        Adds a single object to an existing group. Neither the object nor the group can be reference objects.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object to add to the group.
            
        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        boolean
        True or False indicating success or failure

        null
        On error.

        """

        return self._ApplyTypes_(134, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"AddObjectToGroup", None, object, group)

    def add_objects_to_group(self, objects, group):
        """        
        Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of object identifiers.
            
        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        number
        The number of objects added to the group if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(135, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1)), u"AddObjectsToGroup", None, flatten(objects), group)

    def delete_group(self, group):
        """        
        Removes an existing group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects.
    
        Parameters
        ==========

        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(136, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"DeleteGroup", None, group)

    def group_count(self):
        """        
        Returns the number of groups in the document.
    
        No parameters

        Returns
        =======

        number
        The number of groups if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(137, 1, (VT_VARIANT, 0), (), u"GroupCount", None, )

    def group_names(self):
        """        
        Returns the name of all the groups in the document.
    
        No parameters

        Returns
        =======

        array
        An array of group names if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(138, 1, (VT_VARIANT, 0), (), u"GroupNames", None, )

    def hide_group(self, group):
        """        
        Hides a group of object.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    
        Parameters
        ==========

        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        number
        The number of object that were hidden if successful.

        null
        On error.

        """

        return self._ApplyTypes_(871, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"HideGroup", None, group)

    def is_group(self, group):
        """        
        Verifies the existence of a group.
    
        Parameters
        ==========

        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(139, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsGroup", None, group)

    def is_group_empty(self, group):
        """        
        Verifies that an existing group is empty, or contains no object members.
    
        Parameters
        ==========

        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        return self._ApplyTypes_(140, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsGroupEmpty", None, group)

    def lock_group(self, group):
        """        
        Locks a group of objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    
        Parameters
        ==========

        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        number
        The number of object that were locked if successful.

        null
        On error.

        """

        return self._ApplyTypes_(873, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"LockGroup", None, group)

    def remove_object_from_all_groups(self, object):
        """        
        Removes a single object from any and all groups that it is a member. Neither the object nor the group can be a reference object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(141, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"RemoveObjectFromAllGroups", None, object)

    def remove_object_from_group(self, object, group):
        """        
        Removes a single object from an existing group.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(142, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"RemoveObjectFromGroup", None, object, group)

    def remove_object_from_top_group(self, object):
        """        
        Removes a single object from it's top-most group.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        return self._ApplyTypes_(143, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"RemoveObjectFromTopGroup", None, object)

    def remove_objects_from_group(self, objects, group):
        """        
        Removes one or more objects from an existing group.
    
        Parameters
        ==========

        objects, Array of ????, Required        
        An array of object identifiers.
            
        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        number
        The number of objects removed from the group if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(144, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1)), u"RemoveObjectsFromGroup", None, flatten(objects), group)

    def rename_group(self, old_group, new_group):
        """        
        Renames an existing group.
    
        Parameters
        ==========

        old_group, String, Required        
        The name of an existing group.
            
        new_group, String, Required        
        The new group name.
            
        Returns
        =======

        string
        The new group name if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(145, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"RenameGroup", None, old_group, new_group)

    def show_group(self, group):
        """        
        Shows a group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
    
        Parameters
        ==========

        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        number
        The number of object that were shown if successful.

        null
        On error.

        """

        return self._ApplyTypes_(872, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"ShowGroup", None, group)

    def unlock_group(self, group):
        """        
        Unlocks a group of locked objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
    
        Parameters
        ==========

        group, String, Required        
        The name of an existing group.
            
        Returns
        =======

        number
        The number of object that were unlocked if successful.

        null
        On error.

        """

        return self._ApplyTypes_(874, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"UnlockGroup", None, group)

