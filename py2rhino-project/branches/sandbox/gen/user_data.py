# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import _utils
from _rhinoscript import IRhinoScript

class UserData(IRhinoScript):



    def attribute_data_count(self, object):
        """

        Returns the number of RhinoScript user data items on an object's attributes.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of RhinoScript object user data items if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(685, 1, (12, 0), ((8, 0),), u'AttributeDataCount', None, object)

    def delete_attribute_data(self, object, section, entry):
        """

        Removes RhinoScript user data items from an object's attributes.

        Parameters

        Object : Required, String, str, String
        Section : Optional, String, str, String
        Entry : Optional, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(684, 1, (12, 0), ((8, 0), (8, 0), (8, 0),), u'DeleteAttributeData', None, object, section, entry)

    def delete_document_data(self, section, entry):
        """

        Removes RhinoScript user data items from the current document.

        Parameters

        Section : Optional, String, str, String
        Entry : Optional, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(237, 1, (12, 0), ((8, 0), (8, 0),), u'DeleteDocumentData', None, section, entry)

    def delete_object_data(self, object, section, entry):
        """

        Removes RhinoScript user data items from an object's geometry.

        Parameters

        Object : Required, String, str, String
        Section : Optional, String, str, String
        Entry : Optional, String, str, String

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(238, 1, (12, 0), ((8, 0), (8, 0), (8, 0),), u'DeleteObjectData', None, object, section, entry)

    def document_data_count(self):
        """

        Returns the number of RhinoScript user data items in the current document.

        No parameters

        Returns

        Number : The number of RhinoScript document user data items.

        """

        return self._ApplyTypes_(239, 1, (12, 0), (,), u'DocumentDataCount', None, )

    def get_attribute_data(self, object, section, entry):
        """

        Returns a RhinoScript user data item from an object's attributes.

        Parameters

        Object : Required, String, str, String
        Section : Optional, String, str, String
        Entry : Optional, String, str, String

        Returns

        Array : A zero-based, one-dimensional array of all section names if strSection is not specified.
        Array : A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.
        String : The value of the entry if both strSection and strEntry are specified.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(682, 1, (12, 0), ((8, 0), (8, 0), (8, 0),), u'GetAttributeData', None, object, section, entry)

    def get_document_data(self, section, entry):
        """

        Returns a RhinoScript user data item from the current document.

        Parameters

        Section : Optional, String, str, String
        Entry : Optional, String, str, String

        Returns

        Array : A zero-based, one-dimensional array of all section names if strSection is not specified.
        Array : A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.
        String : The value of the entry if both strSection and strEntry are specified.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(240, 1, (12, 0), ((8, 0), (8, 0),), u'GetDocumentData', None, section, entry)

    def get_object_data(self, object, section, entry):
        """

        Returns a RhinoScript user data item from an object's geometry.

        Parameters

        Object : Required, String, str, String
        Section : Optional, String, str, String
        Entry : Optional, String, str, String

        Returns

        Array : A zero-based, one-dimensional array of all section names if strSection is not specified.
        Array : A zero-based, one-dimensional array of all entry names for strSection if strEntry is not specified.
        String : The value of the entry if both strSection and strEntry are specified.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(241, 1, (12, 0), ((8, 0), (8, 0), (8, 0),), u'GetObjectData', None, object, section, entry)

    def get_user_text(self, object, key, attach_to_geometry):
        """

        Returns User Text that is stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.

        Parameters

        Object : Required, String, str, String
        Key : Optional, String, str, String
        AttachToGeometry : Optional, Boolean, bln, Boolean

        Returns

        String : If strKey is specified, then the associated value if successful.
        Array : If strKey is not specified, then an array of key names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(729, 1, (12, 0), ((8, 0), (8, 0), (11, 0),), u'GetUserText', None, object, key, attach_to_geometry)

    def is_attribute_data(self, object):
        """

        Verifies that an object's attributes contains RhinoScript user data.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True or False indicating whether or not the object's attributes contains any RhinoScript user data if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(686, 1, (12, 0), ((8, 0),), u'IsAttributeData', None, object)

    def is_document_data(self):
        """

        Verifies that the current document contains RhinoScript user data.

        No parameters

        Returns

        Boolean : True or False indicating whether or not the current document contains any RhinoScript document user data.

        """

        return self._ApplyTypes_(278, 1, (12, 0), (,), u'IsDocumentData', None, )

    def is_object_data(self, object):
        """

        Verifies that an object's geometry contains RhinoScript user data.

        Parameters

        Object : Required, String, str, String

        Returns

        Boolean : True or False indicating whether or not the object's geometry contains any RhinoScript user data if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(279, 1, (12, 0), ((8, 0),), u'IsObjectData', None, object)

    def is_user_text(self, object):
        """

        Verifies that an object contains user text. For more details on User Text, see the discussion found in the User Data Methods summary.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : 0 = no user text; 1 = attribute user text; 2 = geometry user text; 3 = both attribute and geometry user text.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(730, 1, (12, 0), ((8, 0),), u'IsUserText', None, object)

    def object_data_count(self, object):
        """

        Returns the number of RhinoScript user data items on an object's geometry.

        Parameters

        Object : Required, String, str, String

        Returns

        Number : The number of RhinoScript object user data items if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(242, 1, (12, 0), ((8, 0),), u'ObjectDataCount', None, object)

    def set_attribute_data(self, object, section, entry, value):
        """

        Adds or sets a RhinoScript user data item to an object's attributes.

        Parameters

        Object : Required, String, str, String
        Section : Required, String, str, String
        Entry : Required, String, str, String
        Value : Required, String, str, String

        Returns

        String : The previous value if successful.
        Null : If no previous value exits, if not successful, or on error.

        """

        return self._ApplyTypes_(683, 1, (12, 0), ((8, 0), (8, 0), (8, 0), (8, 0),), u'SetAttributeData', None, object, section, entry, value)

    def set_document_data(self, section, entry, value):
        """

        Adds or sets a RhinoScript user data item to the current document.

        Parameters

        Section : Required, String, str, String
        Entry : Required, String, str, String
        Value : Required, String, str, String

        Returns

        String : The previous value if successful.
        Null : If no previous value exits, if not successful, or on error.

        """

        return self._ApplyTypes_(243, 1, (12, 0), ((8, 0), (8, 0), (8, 0),), u'SetDocumentData', None, section, entry, value)

    def set_object_data(self, object, section, entry, value):
        """

        Adds or sets a RhinoScript user data item to an object's geometry.

        Parameters

        Object : Required, String, str, String
        Section : Required, String, str, String
        Entry : Required, String, str, String
        Value : Required, String, str, String

        Returns

        String : The previous value if successful.
        Null : If no previous value exits, if not successful, or on error.

        """

        return self._ApplyTypes_(244, 1, (12, 0), ((8, 0), (8, 0), (8, 0), (8, 0),), u'SetObjectData', None, object, section, entry, value)

    def set_user_text(self, object, key, value, attach_to_geometry):
        """

        Sets or removes user text stored on an object. For more details on User Text, see the discussion found in the User Data Methods summary.

        Parameters

        Object : Required, String, str, String
        Key : Required, String, str, String
        Value : Optional, String, str, String
        AttachToGeometry : Optional, Boolean, bln, Boolean

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(728, 1, (12, 0), ((8, 0), (8, 0), (8, 0), (11, 0),), u'SetUserText', None, object, key, value, attach_to_geometry)

