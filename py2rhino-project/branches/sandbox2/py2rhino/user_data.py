# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class UserData(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def attribute_data_count(self, object):
        """        
        Returns the number of RhinoScript user data items on an object's attributes.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        number
        The number of RhinoScript object user data items if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(685, 1, (VT_VARIANT, 0), magic, u"AttributeDataCount", None, *flattened)

    def delete_attribute_data(self, object, section=None, entry=None):
        """        
        Removes RhinoScript user data items from an object's attributes.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        section, String, Optional        
        The section name.  If omitted, all sections and their corresponding entries are removed.
            
        entry, String, Optional        
        The entry name.  If omitted, all entries for strSection are removed.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [object, section, entry]
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, section, entry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(684, 1, (VT_VARIANT, 0), magic, u"DeleteAttributeData", None, *flattened)

    def delete_document_data(self, section=None, entry=None):
        """        
        Removes RhinoScript user data items from the current document.
    
        Parameters
        ==========

        section, String, Optional        
        The section name.  If omitted, all sections and their corresponding entries are removed.
            
        entry, String, Optional        
        The entry name.  If omitted, all entries for strSection are removed.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [section, entry]
        required = [False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [section, entry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(237, 1, (VT_VARIANT, 0), magic, u"DeleteDocumentData", None, *flattened)

    def delete_object_data(self, object, section=None, entry=None):
        """        
        Removes RhinoScript user data items from an object's geometry.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        section, String, Optional        
        The section name.  If omitted, all sections and their corresponding entries are removed.
            
        entry, String, Optional        
        The entry name.  If omitted, all entries for strSection are removed.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [object, section, entry]
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, section, entry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(238, 1, (VT_VARIANT, 0), magic, u"DeleteObjectData", None, *flattened)

    def document_data_count(self):
        """        
        Returns the number of RhinoScript user data items in the current document.
    
        No parameters

        Returns
        =======

        number
        The number of RhinoScript document user data items.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(239, 1, (VT_VARIANT, 0), magic, u"DocumentDataCount", None, *flattened)

    def get_attribute_data(self, object, section=None, entry=None):
        """        
        Returns a RhinoScript user data item from an object's attributes.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        section, String, Optional        
        The section name.  If omitted, all section names are returned.
            
        entry, String, Optional        
        The entry name.  If omitted, all entry names for strSection are returned.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array of all section names if strSection is not specified.

        array
        A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.

        string
        The value of the entry if both strSection and strEntry are specified.

        null
        If not successful, or on error.

        """

        params = [object, section, entry]
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, section, entry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(682, 1, (VT_VARIANT, 0), magic, u"GetAttributeData", None, *flattened)

    def get_document_data(self, section=None, entry=None):
        """        
        Returns a RhinoScript user data item from the current document.
    
        Parameters
        ==========

        section, String, Optional        
        The section name.  If omitted, all section names are returned.
            
        entry, String, Optional        
        The entry name.  If omitted, all entry names for strSection are returned.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array of all section names if strSection is not specified.

        array
        A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.

        string
        The value of the entry if both strSection and strEntry are specified.

        null
        If not successful, or on error.

        """

        params = [section, entry]
        required = [False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [section, entry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(240, 1, (VT_VARIANT, 0), magic, u"GetDocumentData", None, *flattened)

    def get_object_data(self, object, section=None, entry=None):
        """        
        Returns a RhinoScript user data item from an object's geometry.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        section, String, Optional        
        The section name.  If omitted, all section names are returned.
            
        entry, String, Optional        
        The entry name.  If omitted, all entry names for strSection are returned.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array of all section names if strSection is not specified.

        array
        A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.

        string
        The value of the entry if both strSection and strEntry are specified.

        null
        If not successful, or on error.

        """

        params = [object, section, entry]
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, section, entry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(241, 1, (VT_VARIANT, 0), magic, u"GetObjectData", None, *flattened)

    def get_user_text(self, object, key=None, attach_to_geometry=None):
        """        
        Returns User Text that is stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        key, String, Optional        
        The key name.  If omitted or an empty string ("") is specified, all key names for the object are returned.
            
        attach_to_geometry, Boolean, Optional        
        The location on the object to retrieve the User Text.
		Value
		Description
		True
		Retrieve text information from the object geometry. If the information is closely associated with the geometry, attach it to the geometry. For example, a circle's radius should be attached to the geometry because the information will be invalid if the circle is control-point edited and changed into a NURBS curve.
		False (Default)
            
        Returns
        =======

        string
        If strKey is specified, then the associated value if successful.

        array
        If strKey is not specified, then an array of key names if successful.

        null
        If not successful, or on error.

        """

        params = [object, key, attach_to_geometry]
        required = [True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [object, key, attach_to_geometry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(729, 1, (VT_VARIANT, 0), magic, u"GetUserText", None, *flattened)

    def is_attribute_data(self, object):
        """        
        Verifies that an object's attributes contains RhinoScript user data.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True or False indicating whether or not the object's attributes contains any RhinoScript user data if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(686, 1, (VT_VARIANT, 0), magic, u"IsAttributeData", None, *flattened)

    def is_document_data(self):
        """        
        Verifies that the current document contains RhinoScript user data.
    
        No parameters

        Returns
        =======

        boolean
        True or False indicating whether or not the current document contains any RhinoScript document user data.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(278, 1, (VT_VARIANT, 0), magic, u"IsDocumentData", None, *flattened)

    def is_object_data(self, object):
        """        
        Verifies that an object's geometry contains RhinoScript user data.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        boolean
        True or False indicating whether or not the object's geometry contains any RhinoScript user data if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(279, 1, (VT_VARIANT, 0), magic, u"IsObjectData", None, *flattened)

    def is_user_text(self, object):
        """        
        Verifies that an object contains user text. For more details on User Text, see the discussion found in the User Data Methods summary.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        number
        0 = no user text; 1 = attribute user text; 2 = geometry user text; 3 = both attribute and geometry user text.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(730, 1, (VT_VARIANT, 0), magic, u"IsUserText", None, *flattened)

    def object_data_count(self, object):
        """        
        Returns the number of RhinoScript user data items on an object's geometry.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        Returns
        =======

        number
        The number of RhinoScript object user data items if successful.

        null
        If not successful, or on error.

        """

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(242, 1, (VT_VARIANT, 0), magic, u"ObjectDataCount", None, *flattened)

    def set_attribute_data(self, object, section, entry, value):
        """        
        Adds or sets a RhinoScript user data item to an object's attributes.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        section, String, Required        
        The application name.
            
        entry, String, Required        
        The key name.
            
        value, String, Required        
        The string value.
            
        Returns
        =======

        string
        The previous value if successful.

        null
        If no previous value exits, if not successful, or on error.

        """

        params = [object, section, entry, value]
        required = [True, True, True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, section, entry, value]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(683, 1, (VT_VARIANT, 0), magic, u"SetAttributeData", None, *flattened)

    def set_document_data(self, section, entry, value):
        """        
        Adds or sets a RhinoScript user data item to the current document.
    
        Parameters
        ==========

        section, String, Required        
        The section name.
            
        entry, String, Required        
        The entry name.
            
        value, String, Required        
        The string value.
            
        Returns
        =======

        string
        The previous value if successful.

        null
        If no previous value exits, if not successful, or on error.

        """

        params = [section, entry, value]
        required = [True, True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [section, entry, value]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(243, 1, (VT_VARIANT, 0), magic, u"SetDocumentData", None, *flattened)

    def set_object_data(self, object, section, entry, value):
        """        
        Adds or sets a RhinoScript user data item to an object's geometry.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        section, String, Required        
        The application name.
            
        entry, String, Required        
        The key name.
            
        value, String, Required        
        The string value.
            
        Returns
        =======

        string
        The previous value if successful.

        null
        If no previous value exits, if not successful, or on error.

        """

        params = [object, section, entry, value]
        required = [True, True, True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [object, section, entry, value]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(244, 1, (VT_VARIANT, 0), magic, u"SetObjectData", None, *flattened)

    def set_user_text(self, object, key, value=None, attach_to_geometry=None):
        """        
        Sets or removes user text stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        key, String, Required        
        The key name to set.
            
        value, String, Optional        
        The string value to set. If omitted the key/value pair specified by strKey will be deleted.
            
        attach_to_geometry, Boolean, Optional        
        The location on the object to store the User Text.
		Value
		Description
		True
		Attaches text information to the object geometry. If the information is closely associated with the geometry, attach it to the geometry. For example, a circle's radius should be attached to the geometry because the information will be invalid if the circle is control-point edited and changed into a NURBS curve.
		False (Default)
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        params = [object, key, value, attach_to_geometry]
        required = [True, True, False, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [object, key, value, attach_to_geometry]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(728, 1, (VT_VARIANT, 0), magic, u"SetUserText", None, *flattened)

