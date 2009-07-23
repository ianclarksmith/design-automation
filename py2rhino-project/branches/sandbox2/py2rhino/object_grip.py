# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class ObjectGrip(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def enable_object_grips(self, object, enable=None):
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

        params = [object, enable]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [object, enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(499, 1, (VT_VARIANT, 0), magic, u"EnableObjectGrips", None, *flattened)

    def get_object_grips(self, message=None, pre_select=None, select=None):
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

        params = [message, pre_select, select]
        required = [False, False, False]
        magic = [(VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        flattened = [message, pre_select, select]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(562, 1, (VT_VARIANT, 0), magic, u"GetObjectGrips", None, *flattened)

    def next_object_grip(self, object, index, direction=None, enable=None):
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

        params = [object, index, direction, enable]
        required = [True, True, False, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1)]
        flattened = [object, index, direction, enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(558, 1, (VT_VARIANT, 0), magic, u"NextObjectGrip", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(500, 1, (VT_VARIANT, 0), magic, u"ObjectGripCount", None, *flattened)

    def object_grip_locations(self, object, points=None):
        """        
        Returns or modifies the location of all grips owned by an object. The locations of the grips are returned in an array of 3-D points with each position in the array corresponding to that grip's index. To modify the locations of grips, you must provide an array of 3-D points that contains the same number of points at grips.
    
        Parameters
        ==========

        object, String, Required        
        The identifier of the object.
            
        points, Array of Doubles, Optional        
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

        params = [object, points]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_ARRAY + VT_R8, 1)]
        flattened = [object, flatten_params(points)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(557, 1, (VT_VARIANT, 0), magic, u"ObjectGripLocations", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(497, 1, (VT_VARIANT, 0), magic, u"ObjectGripsOn", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(498, 1, (VT_VARIANT, 0), magic, u"ObjectGripsSelected", None, *flattened)

    def prev_object_grip(self, object, index, direction=None, enable=None):
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

        params = [object, index, direction, enable]
        required = [True, True, False, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_BOOL, 1)]
        flattened = [object, index, direction, enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(559, 1, (VT_VARIANT, 0), magic, u"PrevObjectGrip", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(501, 1, (VT_VARIANT, 0), magic, u"SelectObjectGrips", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(560, 1, (VT_VARIANT, 0), magic, u"SelectedObjectGrips", None, *flattened)

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

        params = [object]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [object]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(502, 1, (VT_VARIANT, 0), magic, u"UnselectObjectGrips", None, *flattened)

