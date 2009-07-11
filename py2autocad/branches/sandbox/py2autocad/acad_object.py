import exceptions
from util import to_array

class _AcadObject(object):
    """Abstract base class for an AutoCAD object"""
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self, id):
        exceptions.Exception("This class cannot be instantiated")     
    #===========================================================================
    # Methods: Class IAcadObject
    #===========================================================================
    def get_x_data(self, AppName):
        """Gets the extended data (XData) associated with an object"""
        #TODO: what is return type?
        return self._id.GetXData(AppName)
    def set_x_data(self, XDataType, XDataValue):
        """Sets the extended data (XData) associated with an object"""
        self._id.GetXData(XDataType, XDataValue)
    def delete(self):
        """Deletes a specified object"""
        self._id.Delete() 
    def get_extension_dictionary(self):
        """Gets the extension dictionary associated with an object"""
        return self._id.GetExtensionDictionary()
    def erase(self):
        """Erases all the objects in a selection set"""
        return None   
    #===========================================================================
    # Properties:  IAcadObject
    #=========================================================================== 
    def _get_handle(self):
        return None
    handle = property(
                fget=_get_handle, 
                doc="The handle of an object")     
    #---------------------------------------------------------------------------
    def _get_object_name(self):
        return None
    object_name = property(
                fget=_get_object_name, 
                doc="The AutoCAD class name of the object") 
    #---------------------------------------------------------------------------
    def _get_object_id(self):
        return None
    object_id = property(
                fget=_get_object_id, 
                doc="The object ID of the object")              
    #---------------------------------------------------------------------------
    def _get_application(self):
        return None 
    application = property(
                fget=_get_application, 
                doc="The Application object")    
    #---------------------------------------------------------------------------
    def _get_database(self):
        return None 
    database = property(
                fget=_get_database, 
                doc="The database in which the object belongs")   
    #---------------------------------------------------------------------------
    def _get_has_extension_dictionary(self):
        return None
    has_extension_dictionary = property(
                fget=_get_has_extension_dictionary, 
                doc="Determines if the object has an extension dictionary associated with it")         
    #---------------------------------------------------------------------------
    def _get_owner_id(self):
        return None
    owner_id = property(
                fget=_get_owner_id, 
                doc="The object ID of the owner (parent) object")           
    #---------------------------------------------------------------------------    
    def _get_document(self):
        return None  
    document = property(
                fget=_get_document, 
                doc="The document (drawing) in which the object belongs")


