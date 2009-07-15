# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class UserInterface(DispatchBaseClass):



    def browseforfolder(self, strfolder, strmessage, strtitle):
        """

        Displays the Windows browse-for-folder dialog box allowing the user to select a folder.

        Parameters

        strFolder : Optional,   String,   A default folder
        strMessage : Optional,   String,   A prompt or message
        strTitle : Optional,   String,   A dialog box title

        Returns

        String : The selected folder if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'BrowseForFolder', None, strFolder, strMessage, strTitle)

    def checklistbox(self, arritems, arrvalues, strmessage, strtitle):
        """

        Displays a list of items in a checkable-style list box dialog.

        Parameters

        arrItems : Required,   Array,   A zero-based, one-dimensional array of string items
        arrValues : Required,   Array,   A zero-based, one-dimensional array of boolean values indicating the checked state of each item in the list
        strMessage : Optional,   String,   A prompt or message
        strTitle : Optional,   String,   A dialog box title

        Returns

        Array : A zero-based, one-dimensional array of boolean values indicating the new checked state of each item in the list.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'CheckListBox', None, arrItems, arrValues, strMessage, strTitle)

    def combolistbox(self, arritems, strmessage, strtitle):
        """

        Displays a list of items in a combo-style list box dialog.

        Parameters

        arrItems : Required,   Array,   A zero-based, one-dimensional array of string items
        strMessage : Optional,   String,   A prompt or message
        strTitle : Optional,   String,   A dialog box title

        Returns

        String : The selected item if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ComboListBox', None, arrItems, strMessage, strTitle)

    def editbox(self, strstring, strmessage, strtitle):
        """

        Displays a dialog box prompting the user to enter a string value.  The string value may span multiple lines.

        Parameters

        strString : Optional,   String,   A default string value
        strMessage : Optional,   String,   A prompt or message
        strTitle : Optional,   String,   A dialog box  title

        Returns

        String : Multiple lines that are separated by carriage return-linefeed combinations if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'EditBox', None, strString, strMessage, strTitle)

    def getangle(self, arrpoint, arrreference, dblangle, strmessage):
        """

        Pauses for user input of an angle.

        Parameters

        arrPoint : Optional,    Array,   A zero-based, one-dimensional array containing three numbers identifying the starting, or base, point
        arrReference : Optional,   Array,   A zero-based, one-dimensional array containing three numbers identifying a reference point
        dblAngle : Optional,   Number,   A default angle value specified in degrees
        strMessage : Optional,   String,   A prompt or message

        Returns

        Number : The angle in degrees if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetAngle', None, arrPoint, arrReference, dblAngle, strMessage)

    def getboolean(self, strmessage, arritems, arrdefaults):
        """

        Pauses for user input of one or more boolean values. Boolean values are displayed as click-able command-line option toggles.

        Parameters

        strMessage : Required,   String,   A prompt or message
        arrItems : Required,   Array,   An array of strings that describe the boolean items that will appear as command-line option toggles
        arrDefaults : Required,   Array,   A array of boolean values to be used as default, or starting values

        Returns

        Array : An array of boolean values that represent the boolean items, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetBoolean', None, strMessage, arrItems, arrDefaults)

    def getbox(self, intmode, arrpoint, strprompt1, strprompt2, strprompt3):
        """

        Pauses for user input of a box.

        Parameters

        intMode : Optional,   Number,   The box selection mode
        arrPoint : Optional,   Array,   A 3-D base point
        strPrompt1 : Optional,   String,   The first prompt or message
        strPrompt2 : Optional,   String,   The second prompt or message
        strPrompt3 : Optional,   String,   The third prompt or message

        Returns

        Array : An array of eight 3-D points that define the corners of the box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetBox', None, intMode, arrPoint, strPrompt1, strPrompt2, strPrompt3)

    def getcolor(self, lngcolor):
        """

        Displays the Rhino color picker dialog box allowing the user to select an RGB color value.

        Parameters

        lngColor : Optional,   Number,   A default RGB color value

        Returns

        Number : The RGB color value selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetColor', None, lngColor)

    def getdistance(self, arrpoint, dbldistance, strmessage1, strmessage2):
        """

        Pauses for user input of a distance.

        Parameters

        arrPoint : Optional,   Array,   A zero-based, one-dimensional array containing three numbers identifying the first distance point
        dblDistance : Optional,   Number,   A default distance value
        strMessage1 : Optional,   String,   A prompt or message for the first distance point
        strMessage2 : Optional,   String,   A prompt or message for the second distance point

        Returns

        Number : The distance input by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetDistance', None, arrPoint, dblDistance, strMessage1, strMessage2)

    def getinteger(self, strmessage, intnumber, intmin, intmax):
        """

        Pauses for user input of a whole number.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        intNumber : Optional,   Number,   A default whole number value
        intMin : Optional,   Number,   A minimum allowable value
        intMax : Optional,   Number,   A maximum allowable value

        Returns

        Number : The whole number input by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetInteger', None, strMessage, intNumber, intMin, intMax)

    def getlayer(self, strtitle, strlayer, blnshownewlayer, blnshowsetcurrent):
        """

        Displays a dialog box prompting the user to select a layer.

        Parameters

        strTitle : Optional,   String,   A dialog box title
        strLayer : Optional,   String,   The name of a layer to pre-select
        blnShowNewLayer : Optional,   Boolean,   Display the "New" layer button
        blnShowSetCurrent : Optional,   Boolean,   Display the "Set layer current" check box

        Returns

        String : The name of the selected layer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetLayer', None, strTitle, strLayer, blnShowNewLayer, blnShowSetCurrent)

    def getlinetype(self, strlinetype):
        """

        Displays a dialog box prompting the user to select a linetype.

        Parameters

        strLinetype : Optional,   String,   The name of the linetype to select

        Returns

        String : The name of the selected linetype if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetLinetype', None, strLinetype)

    def getpoint(self, strmessage, arrpoint, dbldistance, blnplane):
        """

        Pauses for user input of a point.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        arrPoint : Optional,   Array,   A zero-based, one-dimensional array containing three numbers identifying a starting, or base, point
        dblDistance : Optional,   Number,   A constraining distance
        blnPlane : Optional,   Boolean,   Constrain the point selection to the active construction plane

        Returns

        Array : A zero-based, one-dimensional array containing three numbers identifying the 3-D point input by the user successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPoint', None, strMessage, arrPoint, dblDistance, blnPlane)

    def getpointoncurve(self, strobject, strmessage):
        """

        Pauses for user input of a point constrained to a curve object.

        Parameters

        strObject : Required,   String,   The object's identifier
        strMessage : Optional,   String,   A prompt or message

        Returns

        Array : The 3-D point selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPointOnCurve', None, strObject, strMessage)

    def getpointonline(self, strmessage, arrstart, arrend, blntrack):
        """

        Pauses for user input of a point constrained to an infinite line.

        Parameters

        strMessage : Required,   String,   A prompt or message
        arrStart : Required,   Array,   The starting point of the line
        arrEnd : Required,   Array,   The ending point of the line
        blnTrack : Optional,   Boolean,   Draw a tracking line from arrStart

        Returns

        Array : The 3-D point selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPointOnLine', None, strMessage, arrStart, arrEnd, blnTrack)

    def getpointonmesh(self, strobject, strmessage):
        """

        Pauses for user input of a point constrained to a mesh object.

        Parameters

        strObject : Required,   String,   The object's identifier
        strMessage : Optional,   String,   A prompt or message

        Returns

        Array : The 3-D point selected by the user successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPointOnMesh', None, strObject, strMessage)

    def getpointonplane(self, strmessage, arrplane, arrpoint):
        """

        Pauses for user input of a point constrained to a plane.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        arrPlane : Optional,   Array,   The plane to constrain the point to
        arrPoint : Optional,   Array,   A 3-D point from with to draw a tracking line

        Returns

        Array : The 3-D point selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPointOnPlane', None, strMessage, arrPlane, arrPoint)

    def getpointonsurface(self, strobject, strmessage):
        """

        Pauses for user input of a point constrained to a surface or polysurface object.

        Parameters

        strObject : Required,  String,  The object's identifier
        strMessage : Optional,   String,   A prompt or message

        Returns

        Array : The 3-D point selected by the user successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPointOnSurface', None, strObject, strMessage)

    def getpoints(self, blndraw, blnplane, strmessage1, strmessage2, intmaxpoints, arrbasepoint):
        """

        Pauses for user input of one or more points.

        Parameters

        blnDraw : Optional,   Boolean,   Draw lines between points
        blnPlane : Optional,   Boolean,   Constrain the point selection to the active construction plane
        strMessage1 : Optional,   String,   A prompt or message for the first point
        strMessage2 : Optional,   String,   A prompt or message for the next points
        intMaxPoints : Optional,   Number,   The maximum number of points to pick
        arrBasePoint : Optional,   Array,   A starting, or base, point

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPoints', None, blnDraw, blnPlane, strMessage1, strMessage2, intMaxPoints, arrBasePoint)

    def getprintwidth(self, dblprintwidth):
        """

        Displays a dialog box prompting the user to select a print width.

        Parameters

        dblPrintWidth : Optional,   Number,   The print width to select

        Returns

        Number : The value of the selected print width if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetPrintWidth', None, dblPrintWidth)

    def getreal(self, strmessage, dblnumber, dblmin, dblmax):
        """

        Pauses for user input of a number.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        dblNumber : Optional,   Number,   A default number value
        dblMin : Optional,   Number,   A minimum allowable value
        dblMax : Optional,   Number,   A maximum allowable value

        Returns

        Number : The number input by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetReal', None, strMessage, dblNumber, dblMin, dblMax)

    def getrectangle(self, intmode, arrpoint, strprompt1, strprompt2, strprompt3):
        """

        Pauses for user input of a rectangle.

        Parameters

        intMode : Optional,   Number,   The rectangle selection mode
        arrPoint : Optional,   Array,   A 3-D base point
        strPrompt1 : Optional,   String,   The first prompt or message
        strPrompt2 : Optional,   String,   The second prompt or message
        strPrompt3 : Optional,   String,   The third prompt or message

        Returns

        Array : An array of four 3-D points that define the corners of the rectangle if successful.  Points are returned in counter-clockwise order.  See the image below for details.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetRectangle', None, intMode, arrPoint, strPrompt1, strPrompt2, strPrompt3)

    def getstring(self, strmessage, strstring, arrstrings):
        """

        Pauses for user input of string value.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        strString : Optional,   String,   A default value
        arrStrings : Optional,   Array,   A array of strings to be displayed as click-able command options

        Returns

        String : The string either input or selected by the user if successful.  If the user presses the Enter key without typing in a string, an empty string "" is returned.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetString', None, strMessage, strString, arrStrings)

    def getsurfaceisoparampoint(self, strobject, strmessage):
        """

        Pauses for user input of a point constrained to a surface object.

        Parameters

        strObject : Required,  String,  The surface object's identifier
        strMessage : Optional,   String,   A prompt or message

        Returns

        Array : An array of selection information if successful. The elements of the array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'GetSurfaceIsoParamPoint', None, strObject, strMessage)

    def htmlbox(self, strfilename, vaarguments, stroptions, blnmodal):
        """

        Displays a custom, modal HTML dialog page. A modal dialog box retains the input focus while open. The user cannot switch windows until the dialog box is closed.

        Parameters

        strFileName : Required,   String,   The filename the HTML dialog page to display
        vaArguments : Optional,   Variant,   An argument, or a zero-based, one-dimensional array of arguments, to pass to the HTML-dialog page
        strOptions : Optional,   String,   The window ornaments for the dialog box, using one or more of the following semicolon-delimited values:
        blnModal : Optional,   Boolean,   If omitted or True, a modal dialog will be displayed

        Returns

        Boolean : If blnModal is specified and is True, then True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'HtmlBox', None, strFileName, vaArguments, strOptions, blnModal)

    def integerbox(self, strmessage, intnumber, strtitle):
        """

        Displays a dialog box prompting the user to enter a whole number.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        intNumber : Optional,   Number,   A default whole number
        strTitle : Optional,   String,   A dialog box title

        Returns

        Number : The whole number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'IntegerBox', None, strMessage, intNumber, strTitle)

    def listbox(self, arritems, strmessage, strtitle):
        """

        Displays a list of items in a list box dialog.

        Parameters

        arrItems : Required,   Array,   A zero-based, one-dimensional array of string items
        strMessage : Optional,   String,   A prompt or message
        strTitle : Optional,   String,   A dialog box title

        Returns

        String : The selected item if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'ListBox', None, arrItems, strMessage, strTitle)

    def messagebeep(self, intbeep):
        """

        Plays a system waveform sound.

        Parameters

        intBeep : Optional,  Number,    A sound type

        No returns


        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MessageBeep', None, intBeep)

    def messagebox(self, strmessage, intbuttons, strtitle):
        """

        Displays a Windows message box. A message box contains an application-defined message and title, plus any combination of predefined icons and push buttons.

        Parameters

        strMessage : Required,   String,   A prompt or message
        intButtons : Optional,   Number,   The buttons and icon to display
        strTitle : Optional,   String,   A dialog box title

        Returns

        Number : An number indicating which button was clicked:

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MessageBox', None, strMessage, intButtons, strTitle)

    def multilistbox(self, arritems, strmessage, strtitle):
        """

        Displays a list of items in a multiple-selection list box dialog.

        Parameters

        arrItems : Required,   Array,   A zero-based, one-dimensional array of string items
        strMessage : Optional,   String,   A prompt or message
        strTitle : Optional,   String,   A dialog box title

        Returns

        Array : A zero-based, one-dimensional array containing the selected item if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'MultiListBox', None, arrItems, strMessage, strTitle)

    def openfilename(self, strtitle, strfilter, strfolder, strfilename, strextension):
        """

        Displays a Windows file open dialog box allowing the user to select a file name. Note, this function does not open the file.

        Parameters

        strTitle : Optional,   String,   A dialog box title
        strFilter : Optional,   String,   A filter string
        strFolder : Optional,   String,   A default folder
        strFilename : Optional,   String,   A default file name
        strExtension : Optional,   String,   A default file extension

        Returns

        String : The file name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'OpenFileName', None, strTitle, strFilter, strFolder, strFilename, strExtension)

    def openfilenames(self, strtitle, strfilter, strfolder, strfilename, strextension):
        """

        Displays a Windows file open dialog box allowing the user to select one or more file names. Note, this function does not open files.

        Parameters

        strTitle : Optional,   String,   A dialog box title
        strFilter : Optional,   String,   A filter string
        strFolder : Optional,   String,   A default folder
        strFilename : Optional,   String,   A default file name
        strExtension : Optional,   String,   A default file extension

        Returns

        Array : An array of file names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'OpenFileNames', None, strTitle, strFilter, strFolder, strFilename, strExtension)

    def popupmenu(self, arrritems, arrmodes, arrpoint, strview):
        """

        Displays a user-defined, context-style popup menu. The popup menu can appear almost anywhere. And, it can be dismissed by either clicking the left or right mouse buttons.

        Parameters

        arrrItems : Required,   Array,   An array of string representing the menu items
        arrModes : Optional,   Array,   A array if numbers identifying the display mode of the corresponding menu items
        arrPoint : Optional,   Array,   A 3-D point where the menu item is to appear
        strView : Optional,   String,   If arrPoint is specified, the strView is the view in which the menu is to appear

        Returns

        Number : The index of the menu item that was picked.
        Number : -1 if no menu item is picked.
        Null : On error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PopupMenu', None, arrrItems, arrModes, arrPoint, strView)

    def propertylistbox(self, arritems, arrvalues, strmessage, strtitle):
        """

        Displays a list of items and their values in a property-style list box dialog.

        Parameters

        arrItems : Required,   Array,   A zero-based, one-dimensional array of string items
        arrValues : Required,   Array,   A zero-based, one-dimensional array of strings indicating the value of each item in the list
        strMessage : Optional,   String,   A prompt or message
        strTitle : Optional,   String,   A dialog box title

        Returns

        Array : A zero-based, one-dimensional array of strings indicating the new value of each item in the list.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'PropertyListBox', None, arrItems, arrValues, strMessage, strTitle)

    def realbox(self, strmessage, dblnumber, strtitle):
        """

        Displays a dialog box prompting the user to enter a number.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        dblNumber : Optional,   Number,   A default number
        strTitle : Optional,   String,   A dialog box title

        Returns

        Number : The number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'RealBox', None, strMessage, dblNumber, strTitle)

    def savefilename(self, strtitle, strfilter, strfolder, strfilename, strextension):
        """

        Displays a Windows file save dialog box allowing the user to enter a file name. Note, this function does not save the file.

        Parameters

        strTitle : Optional,   String,   A dialog box title
        strFilter : Optional,   String,   A filter string
        strFolder : Optional,   String,   A default folder
        strFilename : Optional,   String,   A default file name
        strExtension : Optional,   String,   A default file extension

        Returns

        String : The file name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'SaveFileName', None, strTitle, strFilter, strFolder, strFilename, strExtension)

    def stringbox(self, strmessage, strstring, strtitle):
        """

        Displays a dialog box prompting the user to enter a string value.

        Parameters

        strMessage : Optional,   String,   A prompt or message
        strString : Optional,   String,   A default string value
        strTitle : Optional,   String,   A dialog box title

        Returns

        String : The string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(id, 1, (returns), (params), u'StringBox', None, strMessage, strString, strTitle)

