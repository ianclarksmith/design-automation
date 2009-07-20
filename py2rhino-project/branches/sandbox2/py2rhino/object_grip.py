# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class ObjectGrip(IRhinoScript):



    def enable_object_grips(self, object, enable):
        """        
        Enables or disables an object's grips. For curves and surfaces, these are also called control points.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        enable, Boolean, Optional        
        If True (default), the specified object's grips will be turned on. Otherwise, they will be turned off.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(499, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1)), u"EnableObjectGrips", None, object, enable)

    def get_object_grip(self, message, pre_select, select):
        """        
        Prompts the user to pick or select a single object grip.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        pre_select, Boolean, Optional        
        Allow for the selection of a pre-selected object grip.  If omitted, pre-selected object grips are not accepted (False).
            
        select, Boolean, Optional        
        Select the picked object grip.  If omitted, the object grip that is  picked is not selected (False).
            
        Returns
        =======

        array
        A one-dimensional array containing the following three elements if successful:

        string
        The identifier of the object that owns the grip.

        number
        The zero-based index value of the grip.

        array
        A 3-D point identifying the location of the grip.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(561, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"GetObjectGrip", None, message, pre_select, select)

    def get_object_grips(self, message, pre_select, select):
        """        
        Prompts the user to pick or select one or more object grips from one or more objects.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        pre_select, Boolean, Optional        
        Allow for the selection of a pre-selected object grips.  If omitted, pre-selected object grips are not accepted (False).
            
        select, Boolean, Optional        
        Select the picked object grips.  If omitted, the object grips that are picked is not selected (False).
            
        Returns
        =======

        array
        A one-dimensional array containing one or more object grip records if successful. An object grip record itself is a one-dimensional array that contains the following three elements:

        string
        The identifier of the object that owns the grip.

        number
        The zero-based index value of the grip.

        array
        A 3-D point identifying the location of the grip.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(562, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"GetObjectGrips", None, message, pre_select, select)

    def next_object_grip(self, object, index, direction, enable):
        """        
        Returns the next grip index from a specified grip index of an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        index, Integer, Required        
        The zero-based grip index from which to get the next grip index.
            
        direction, Integer, Optional        
        The direction to get the next grip index, either 0=U or 1=V. The default value is 0. Note, this argument only applies when dealing with surfaces.
            
        enable, Boolean, Optional        
        If True (default), the next grip index found will be selected. Otherwise, it will not be selected.
            
        Returns
        =======

        number
        The index of the next grip from the specified grip index.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(558, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1)), u"NextObjectGrip", None, object, index, direction, enable)

    def object_grip_count(self, object):
        """        
        Returns the number of grips owned by an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        number
        The number of grips if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(500, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"ObjectGripCount", None, object)

    def object_grip_location(self, object, index, point):
        """        
        Returns or modifies the location of an object's grip.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        index, Integer, Required        
        The zero-based index of the grip to either query or modify.
            
        point, Array of ????, Optional        
        A 3-D point identifying the new location of the grip.
            
        Returns
        =======

        array
        If arrPoint is not specified, the current location of the grip referenced by intIndex if successful.

        array
        If arrPoint is specified, the previous location of the grip referenced by intIndex if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(556, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_VARIANT, 1)), u"ObjectGripLocation", None, object, index, flatten(point))

    def object_grip_locations(self, object, points):
        """        
        Returns or modifies the location of all grips owned by an object. The locations of the grips are returned in an array of 3-D points with each position in the array corresponding to that grip's index. To modify the locations of grips, you must provide an array of 3-D points that contains the same number of points at grips.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        points, Array of ????, Optional        
        An array of 3-D points identifying the new locations of the grips.
            
        Returns
        =======

        array
        If arrPoints is not specified, the current location of all grips if successful.

        array
        If arrPoints is specified, the previous location of all grips if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(557, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1)), u"ObjectGripLocations", None, object, flatten(points))

    def object_grips_on(self, object):
        """        
        Verifies that an object's grips are turned on.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(497, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"ObjectGripsOn", None, object)

    def object_grips_selected(self, object):
        """        
        Verifies that an object's grips are turned on and at least one grip is selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        boolean
        True of False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(498, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"ObjectGripsSelected", None, object)

    def prev_object_grip(self, object, index, direction, enable):
        """        
        Returns the previous grip index from a specified grip index of an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        index, Integer, Required        
        The zero-based grip index from which to get the previous grip index.
            
        direction, Integer, Optional        
        The direction to get the previous grip index, either 0=U or 1=V. The default value is 0. Note, this argument only applies when dealing with surfaces.
            
        enable, Boolean, Optional        
        If True (default), the previous grip index found will be selected. Otherwise, it will not be selected.
            
        Returns
        =======

        number
        The index of the next grip from the specified grip index.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(559, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1)), u"PrevObjectGrip", None, object, index, direction, enable)

    def select_object_grip(self, object, index):
        """        
        Selects a single grip owned by an object. If the object's grips are not turned on, grips will  not be selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        index, Integer, Required        
        The zero-based grip index to select.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(554, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"SelectObjectGrip", None, object, index)

    def select_object_grips(self, object):
        """        
        Selects an object's grips. If the object's grips are not turned on, they will not be selected.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        number
        The number of grips selected if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(501, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"SelectObjectGrips", None, object)

    def selected_object_grips(self, object):
        """        
        Returns an array of grip indices identifying an object's selected grips.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        array
        An array of zero-based grip indices identifying the selected grips.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(560, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"SelectedObjectGrips", None, object)

    def unselect_object_grip(self, object, index):
        """        
        Unselects a single grip owned by an object.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        index, Integer, Required        
        The zero-based grip index to unselect.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(555, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1)), u"UnselectObjectGrip", None, object, index)

    def unselect_object_grips(self, object):
        """        
        Unselects an object's grips. Note, the grips will not be turned off.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        Returns
        =======

        number
        The number of grips unselected if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(502, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"UnselectObjectGrips", None, object)

