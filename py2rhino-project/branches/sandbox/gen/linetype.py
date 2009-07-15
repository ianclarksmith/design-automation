# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Linetype(DispatchBaseClass):



    def islinetype(self, strlinetype):
        """

        Verifies the existence of a linetype in the document.

        Parameters

        strLinetype : Required,   String,   The name of an existing linetype

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsLinetype', None, strLinetype)

    def islinetypereference(self, strlinetype):
        """

        Verifies that an existing linetype is from a reference file.

        Parameters

        strLinetype : Required,   String,   The name of an existing linetype

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IsLinetypeReference', None, strLinetype)

    def linetypecount(self, ):
        """

        Returns the number of linetypes in the document.

        No parameters

        Returns

        Number : The number of linetypes in the document.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LinetypeCount', None, )

    def linetypenames(self, blnsort):
        """

        Returns the names of all linetypes in the document.

        Parameters

        blnSort : Optional,   Boolean,   Return a sorted list of linetype names

        Returns

        Array : An array of linetype names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'LinetypeNames', None, blnSort)

