import pythoncom
from exceptions import Exception
from py2rhino import _base

#The following functions were not included here:
#GroupCount
#GroupNames
#IsGroup
#RemoveObjectFromAllGroups
#RemoveObjectFromTopGroup

class _GroupModf(object):
    
    def delete(self):
        """
        
        Removes the group from the document. Reference groups cannot be removed. Deleting a group does not delete the member objects.

        Parameters
        ==========
        None

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteGroup

        
        """
        return _base._rsf.delete_group(self._group._name)
 
class _GroupProp(object):
    
    def name(self, name):
        """
        
        Returns the name of the group.
        
        Parameters
        ==========
        None

        Returns
        =======
        string - The group name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        None

        
        """
        return self._group._name 
            
    def rename(self, name):
        """
        
        Renames the group.
        
        Parameters
        ==========
        name (string, Required) - The new name of the group.

        Returns
        =======
        string - The new group name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RenameGroup

        
        """
        name = _base._rsf.rename_group(self._group._name, name)
        if name:
            self._group._name = name
            return name
        else:
            return None    
        
class _GroupObjs(object):        
    def add_object(self, object):
        """
        
        Adds a single object to an existing group. Neither the object nor the group can be reference objects.

        Parameters
        ==========
        object (object, Required) - The object to add to the group.

        Returns
        =======
        boolean - True or False indicating success or failure
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddObjectToGroup

        
        """
        return _base._rsf.add_object_to_group(object._rhino_id, self._group._name)

    def add_objects(self, objects):
        """
        
        Adds one or more objects to an existing group. Neither the objects nor the group can be reference objects.

        Parameters
        ==========
        objects  (List of object, Required) - The list of objects to add to the group.

        Returns
        =======
        integer - The number of objects added to the group if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddObjectsToGroup

        
        """
        object_ids = []
        for object in objects:
            object_ids.append(object._rhino_id)
        return _base._rsf.add_objects_to_group(object_ids, self._group._name)
    
    def remove_object(self, object):
        """
        
        Removes a single object from the group.
        
        Parameters
        ==========
        object - (object, Required) - The object to remove.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RemoveObjectFromGroup

        
        """
        return _base._rsf.remove_object_from_group(object._rhino_id, self._group._name)
    
    def remove_objects(self, objects):
        """
        
        Removes one or more objects from the group.
        
        Parameters
        ==========
        objects (List of object, Required) - The list of objects to remove.

        Returns
        =======
        integer - The number of objects removed from the group if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RemoveObjectsFromGroup

        
        """
        object_ids = []
        for object in objects:
            object_ids.append(object._rhino_id)        
        return _base._rsf.remove_objects_from_group(object_ids, self._group._name)    
    

    
class _GroupTest(object): 
    def is_empty(self):
        """
        
        Verifies that the group is empty, or contains no object members.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsGroupEmpty

        
        """
        return _base._rsf.is_group_empty(self._group._name)
    
class _GroupDspl(object):     
    def hide(self):
        """
        
        Hides all the objects in the group.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.

        Parameters
        ==========
        None

        Returns
        =======
        integer - The number of object that were hidden if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: HideGroup

        
        """
        return _base._rsf.hide_group(self._group._name)
    def show(self, name):
        """
        
        Shows the group of previously hidden objects.  Hidden objects are not visible, cannot be snapped to, and cannot be selected.
        
        Parameters
        ==========
        None

        Returns
        =======
        integer - The number of object that were shown if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ShowGroup

        
        """
        return _base._rsf.show_group(self._group._name)
    def lock  (self):
        """
        
        Locks all the objects in the group.  Locked objects are visible, and they can be snapped to.  But, they cannot be selected.
        
        Parameters
        ==========
        None

        Returns
        =======
        integer - The number of object that were locked if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LockGroup

        
        """
        return _base._rsf.lock_group(self._group._name)
    def unlok(self, name):
        """
        
        Unlocks the group of locked objects.  Locked object are visible, and they can be snapped to.  But, they cannot be selected.
        
        Parameters
        ==========
        None

        Returns
        =======
        integer - The number of object that were unlocked if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: UnlockGroup

        
        """
        return _base._rsf.unlock_group(self._group._name)
    
    
class Group(object):
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    class objs(_GroupObjs):
        def __init__(self, _group):
            self._group = _group
    class modf(_GroupModf):
        def __init__(self, _group):
            self._group = _group
    class test(_GroupTest):
        def __init__(self, _group):
            self._group = _group            
    class dspl(_GroupDspl):
        def __init__(self, _group):
            self._group = _group
    class prop(_GroupProp):
        def __init__(self, _group):
            self._group = _group
    #--------------------------------------------------------------------------
    # Class constructor
    def __init__(self, name):
        if name==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._name = name
        
        #create instances of the nested classes
        self.objs = Group.objs(self)
        self.modf = Group.modf(self)
        self.test = Group.test(self)        
        self.dspl = Group.dspl(self)
        self.prop = Group.prop(self)   
        
    #--------------------------------------------------------------------------
    @staticmethod
    def create(name=pythoncom.Empty):
        """
        
        Factory method:
        Adds a group to the document. Each group must have a unique name.

        Parameters
        ==========
        name (String, Optional) - The name of the new group.  If omitted, Rhino automatically generates the group name.

        Returns
        =======
        String - The name of the new group if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddGroup

        
        """

        name = _base._rsf.add_group(name)

        if name:
            return Group(name)
        else:
            return None


    

    

    

    

    
