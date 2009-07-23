# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Group(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def add_group(self, group=None):
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

        params = [group]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(133, 1, (VT_VARIANT, 0), magic, u"AddGroup", None, *flattened)

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

        params = [object, group]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(134, 1, (VT_VARIANT, 0), magic, u"AddObjectToGroup", None, *flattened)

    def add_objects_to_group(self, objects, group):
        """        
        Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
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

        params = [objects, group]
        required = [True, True]
        magic = [(VT_VARIANT, 1), (VT_BSTR, 1)]
        flattened = [flatten_params(objects), group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(135, 1, (VT_VARIANT, 0), magic, u"AddObjectsToGroup", None, *flattened)

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

        params = [group]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(136, 1, (VT_VARIANT, 0), magic, u"DeleteGroup", None, *flattened)

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

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(137, 1, (VT_VARIANT, 0), magic, u"GroupCount", None, *flattened)

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

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(138, 1, (VT_VARIANT, 0), magic, u"GroupNames", None, *flattened)

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

        params = [group]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(871, 1, (VT_VARIANT, 0), magic, u"HideGroup", None, *flattened)

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

        params = [group]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(139, 1, (VT_VARIANT, 0), magic, u"IsGroup", None, *flattened)

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

        params = [group]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(140, 1, (VT_VARIANT, 0), magic, u"IsGroupEmpty", None, *flattened)

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

        params = [group]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(873, 1, (VT_VARIANT, 0), magic, u"LockGroup", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(141, 1, (VT_VARIANT, 0), magic, u"RemoveObjectFromAllGroups", None, *flattened)

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

        params = [object, group]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(142, 1, (VT_VARIANT, 0), magic, u"RemoveObjectFromGroup", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(143, 1, (VT_VARIANT, 0), magic, u"RemoveObjectFromTopGroup", None, *flattened)

    def remove_objects_from_group(self, objects, group):
        """        
        Removes one or more objects from an existing group.
    
        Parameters
        ==========

        objects, Array of Strings, Required        
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

        params = [objects, group]
        required = [True, True]
        magic = [(VT_VARIANT, 1), (VT_BSTR, 1)]
        flattened = [flatten_params(objects), group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(144, 1, (VT_VARIANT, 0), magic, u"RemoveObjectsFromGroup", None, *flattened)

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

        params = [old_group, new_group]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [old_group, new_group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(145, 1, (VT_VARIANT, 0), magic, u"RenameGroup", None, *flattened)

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

        params = [group]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(872, 1, (VT_VARIANT, 0), magic, u"ShowGroup", None, *flattened)

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

        params = [group]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [group]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(874, 1, (VT_VARIANT, 0), magic, u"UnlockGroup", None, *flattened)

