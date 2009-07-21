# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class UserData(IRhinoScript):



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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(685, 1, (VT_VARIANT, 0), params_magic_numbers, u"AttributeDataCount", None, *params_flattened)

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
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, section, entry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(684, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteAttributeData", None, *params_flattened)

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
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [section, entry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(237, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteDocumentData", None, *params_flattened)

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
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, section, entry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(238, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteObjectData", None, *params_flattened)

    def document_data_count():
        """        
        Returns the number of RhinoScript user data items in the current document.
    
        No parameters

        Returns
        =======

        number
        The number of RhinoScript document user data items.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(239, 1, (VT_VARIANT, 0), params_magic_numbers, u"DocumentDataCount", None, *params_flattened)

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
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, section, entry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(682, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetAttributeData", None, *params_flattened)

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
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [section, entry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(240, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetDocumentData", None, *params_flattened)

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
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, section, entry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(241, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetObjectData", None, *params_flattened)

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
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, key, attach_to_geometry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(729, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetUserText", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(686, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsAttributeData", None, *params_flattened)

    def is_document_data():
        """        
        Verifies that the current document contains RhinoScript user data.
    
        No parameters

        Returns
        =======

        boolean
        True or False indicating whether or not the current document contains any RhinoScript document user data.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(278, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsDocumentData", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(279, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsObjectData", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(730, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsUserText", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [object]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(242, 1, (VT_VARIANT, 0), params_magic_numbers, u"ObjectDataCount", None, *params_flattened)

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
        params_required = [True, True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, section, entry, value]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(683, 1, (VT_VARIANT, 0), params_magic_numbers, u"SetAttributeData", None, *params_flattened)

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
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [section, entry, value]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(243, 1, (VT_VARIANT, 0), params_magic_numbers, u"SetDocumentData", None, *params_flattened)

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
        params_required = [True, True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, section, entry, value]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(244, 1, (VT_VARIANT, 0), params_magic_numbers, u"SetObjectData", None, *params_flattened)

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
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [object, key, value, attach_to_geometry]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(728, 1, (VT_VARIANT, 0), params_magic_numbers, u"SetUserText", None, *params_flattened)

