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

        return self._ApplyTypes_(607, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsLinetype", None, linetype)

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

        return self._ApplyTypes_(608, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"IsLinetypeReference", None, linetype)

    def linetype_count(self):
        """        
        Returns the number of linetypes in the document.
    
        No parameters

        Returns
        =======

        number
        The number of linetypes in the document.

        """

        return self._ApplyTypes_(605, 1, (VT_VARIANT, 0), (), u"LinetypeCount", None, )

    def linetype_names(self, sort):
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

        return self._ApplyTypes_(606, 1, (VT_VARIANT, 0), ((VT_BOOL, 1),), u"LinetypeNames", None, sort)

