# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Linetype(IRhinoScript):



    def is_linetype(self, linetype):
        """        
        Verifies the existence of a linetype in the document.
    
        Parameters
        ==========

        linetype, String, Required        
        The name of an existing linetype.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [linetype]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [linetype]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(607, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLinetype", None, *params_flattened)

    def is_linetype_reference(self, linetype):
        """        
        Verifies that an existing linetype is from a reference file.
    
        Parameters
        ==========

        linetype, String, Required        
        The name of an existing linetype.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [linetype]
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [linetype]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(608, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsLinetypeReference", None, *params_flattened)

    def linetype_count():
        """        
        Returns the number of linetypes in the document.
    
        No parameters

        Returns
        =======

        number
        The number of linetypes in the document.

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

        return self._ApplyTypes_(605, 1, (VT_VARIANT, 0), params_magic_numbers, u"LinetypeCount", None, *params_flattened)

    def linetype_names(self, sort=None):
        """        
        Returns the names of all linetypes in the document.
    
        Parameters
        ==========

        sort, Boolean, Optional        
        Return a sorted list of linetype names. The default is not to return a sorted list (False).
            
        Returns
        =======

        array
        An array of linetype names if successful.

        null
        If not successful, or on error.

        """

        params = [sort]
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [sort]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(606, 1, (VT_VARIANT, 0), params_magic_numbers, u"LinetypeNames", None, *params_flattened)

