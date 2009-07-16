# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Linetype(DispatchBaseClass):



    def is_linetype(self, linetype):
        """

        Verifies the existence of a linetype in the document.

        Parameters

        Linetype : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(607, 1, (12, 0), ((12, 0)), u'IsLinetype', None, linetype)

    def is_linetype_reference(self, linetype):
        """

        Verifies that an existing linetype is from a reference file.

        Parameters

        Linetype : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(608, 1, (12, 0), ((12, 0)), u'IsLinetypeReference', None, linetype)

    def linetype_count(self):
        """

        Returns the number of linetypes in the document.

        No parameters

        Returns

        Number : The number of linetypes in the document.

        """

        return self._ApplyTypes_(605, 1, (12, 0), (), u'LinetypeCount', None, )

    def linetype_names(self, sort):
        """

        Returns the names of all linetypes in the document.

        Parameters

        Sort : Optional, Boolean, bln

        Returns

        Array : An array of linetype names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(606, 1, (12, 0), ((12, 0)), u'LinetypeNames', None, sort)

