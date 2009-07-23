# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Linetype(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [linetype]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(607, 1, (VT_VARIANT, 0), magic, u"IsLinetype", None, *flattened)

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
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [linetype]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(608, 1, (VT_VARIANT, 0), magic, u"IsLinetypeReference", None, *flattened)

    def linetype_count(self):
        """        
        Returns the number of linetypes in the document.
    
        No parameters

        Returns
        =======

        number
        The number of linetypes in the document.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(605, 1, (VT_VARIANT, 0), magic, u"LinetypeCount", None, *flattened)

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
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [sort]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(606, 1, (VT_VARIANT, 0), magic, u"LinetypeNames", None, *flattened)

