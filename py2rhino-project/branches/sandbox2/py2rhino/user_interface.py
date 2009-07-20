# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class UserInterface(IRhinoScript):



    def browse_for_folder(self, folder, message, title):
        """        
        Displays the Windows browse-for-folder dialog box allowing the user to select a folder.
    
        Parameters
        ==========

        folder, String, Optional        
        A default folder.
            
        message, String, Optional        
        A prompt or message.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        string
        The selected folder if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(146, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"BrowseForFolder", None, folder, message, title)

    def check_list_box(self, items, values, message, title):
        """        
        Displays a list of items in a checkable-style list box dialog.
    
        Parameters
        ==========

        items, Array of ????, Required        
        A zero-based, one-dimensional array of string items.
            
        values, Array of ????, Required        
        A zero-based, one-dimensional array of boolean values indicating the checked state of each item in the list.
            
        message, String, Optional        
        A prompt or message.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array of boolean values indicating the new checked state of each item in the list.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(52, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"CheckListBox", None, flatten(items), flatten(values), message, title)

    def combo_list_box(self, items, message, title):
        """        
        Displays a list of items in a combo-style list box dialog.
    
        Parameters
        ==========

        items, Array of ????, Required        
        A zero-based, one-dimensional array of string items.
            
        message, String, Optional        
        A prompt or message.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        string
        The selected item if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(53, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"ComboListBox", None, flatten(items), message, title)

    def edit_box(self, string, message, title):
        """        
        Displays a dialog box prompting the user to enter a string value.  The string value may span multiple lines.
    
        Parameters
        ==========

        string, String, Optional        
        A default string value.
            
        message, String, Optional        
        A prompt or message.
            
        title, String, Optional        
        A dialog box  title.
            
        Returns
        =======

        string
        Multiple lines that are separated by carriage return-linefeed combinations if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(54, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"EditBox", None, string, message, title)

    def get_angle(self, point, reference, angle, message):
        """        
        Pauses for user input of an angle.
    
        Parameters
        ==========

        point, Array of ????, Optional        
        A zero-based, one-dimensional array containing three numbers identifying the starting, or base, point.
            
        reference, Array of ????, Optional        
        A zero-based, one-dimensional array containing three numbers identifying a reference point.  If specified, the reference angle is calculated from it and the base point.
            
        angle, Double, Optional        
        A default angle value specified in degrees.
            
        message, String, Optional        
        A prompt or message.
            
        Returns
        =======

        number
        The angle in degrees if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(277, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_BSTR, 1)), u"GetAngle", None, flatten(point), flatten(reference), angle, message)

    def get_boolean(self, message, items, defaults):
        """        
        Pauses for user input of one or more boolean values. Boolean values are displayed as click-able command-line option toggles.
    
        Parameters
        ==========

        message, String, Required        
        A prompt or message.
            
        items, Array of ????, Required        
        An array of strings that describe the boolean items that will appear as command-line option toggles. Each boolean item consists of three strings.
		Element
		Description
		0
		A description of the boolean value.
		1
		A string identifying the False value.
		2
            
        defaults, Array of ????, Required        
        A array of boolean values to be used as default, or starting values.
            
        Returns
        =======

        array
        An array of boolean values that represent the boolean items, if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(622, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"GetBoolean", None, message, flatten(items), flatten(defaults))

    def get_box(self, mode, point, prompt1, prompt2, prompt3):
        """        
        Pauses for user input of a box.
    
        Parameters
        ==========

        mode, Integer, Optional        
        The box selection mode.  If not specified, all modes (0) are available.  The box selection modes are as follows:
		Value
		Description
		0
		All modes.
		1
		Corner.  The base rectangle is created by picking two corner points.
		2
		3-Point.  The base rectangle is created by picking three points
		3
		Vertical.  The base vertical rectangle is created by picking three points.
		4
            
        point, Array of ????, Optional        
        A 3-D base point.
            
        prompt1, String, Optional        
        The first prompt or message.
            
        prompt2, String, Optional        
        The second prompt or message.
            
        prompt3, String, Optional        
        The third prompt or message.  The third prompt used only with 3Point and Vertical modes.
            
        Returns
        =======

        array
        An array of eight 3-D points that define the corners of the box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(342, 1, (VT_VARIANT, 0), ((VT_I2, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"GetBox", None, mode, flatten(point), prompt1, prompt2, prompt3)

    def get_color(self, color):
        """        
        Displays the Rhino color picker dialog box allowing the user to select an RGB color value.
    
        Parameters
        ==========

        color, Integer, Optional        
        A default RGB color value.  If omitted, the default color is black, or RGB(0,0,0).
            
        Returns
        =======

        number
        The RGB color value selected by the user if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(65, 1, (VT_VARIANT, 0), ((VT_I4, 1),), u"GetColor", None, color)

    def get_distance(self, point, distance, message1, message2):
        """        
        Pauses for user input of a distance.
    
        Parameters
        ==========

        point, Array of ????, Optional        
        A zero-based, one-dimensional array containing three numbers identifying the first distance point.
            
        distance, Double, Optional        
        A default distance value.
            
        message1, String, Optional        
        A prompt or message for the first distance point.
            
        message2, String, Optional        
        A prompt or message for the second distance point.
            
        Returns
        =======

        number
        The distance input by the user if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(66, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"GetDistance", None, flatten(point), distance, message1, message2)

    def get_integer(self, message, number, min, max):
        """        
        Pauses for user input of a whole number.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        number, Integer, Optional        
        A default whole number value.
            
        min, Integer, Optional        
        A minimum allowable value.
            
        max, Integer, Optional        
        A maximum allowable value.
            
        Returns
        =======

        number
        The whole number input by the user if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(64, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_I2, 1)), u"GetInteger", None, message, number, min, max)

    def get_layer(self, title, layer, show_new_layer, show_set_current):
        """        
        Displays a dialog box prompting the user to select a layer.
    
        Parameters
        ==========

        title, String, Optional        
        A dialog box title.
            
        layer, String, Optional        
        The name of a layer to pre-select. If omitted, the current layer will be pre-selected.
            
        show_new_layer, Boolean, Optional        
        Display the "New" layer button. If omitted, the button is not displayed.
            
        show_set_current, Boolean, Optional        
        Display the "Set layer current" check box.  If omitted, the check box is not displayed.
            
        Returns
        =======

        string
        The name of the selected layer if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(672, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)), u"GetLayer", None, title, layer, show_new_layer, show_set_current)

    def get_linetype(self, linetype):
        """        
        Displays a dialog box prompting the user to select a linetype.
    
        Parameters
        ==========

        linetype, String, Optional        
        The name of the linetype to select.  If omitted, the current linetype will be selected.
            
        Returns
        =======

        string
        The name of the selected linetype if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(673, 1, (VT_VARIANT, 0), ((VT_BSTR, 1),), u"GetLinetype", None, linetype)

    def get_point(self, message, point, distance, plane):
        """        
        Pauses for user input of a point.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        point, Array of ????, Optional        
        A zero-based, one-dimensional array containing three numbers identifying a starting, or base, point.
            
        distance, Double, Optional        
        A constraining distance.  If a constraining distance is specified, a base point must also be specified.
            
        plane, Boolean, Optional        
        Constrain the point selection to the active construction plane.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array containing three numbers identifying the 3-D point input by the user successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(61, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_BOOL, 1)), u"GetPoint", None, message, flatten(point), distance, plane)

    def get_point_on_curve(self, object, message):
        """        
        Pauses for user input of a point constrained to a curve object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        message, String, Optional        
        A prompt or message.
            
        Returns
        =======

        array
        The 3-D point selected by the user if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(147, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"GetPointOnCurve", None, object, message)

    def get_point_on_line(self, message, start, end, track):
        """        
        Pauses for user input of a point constrained to an infinite line.
    
        Parameters
        ==========

        message, String, Required        
        A prompt or message.
            
        start, Array of ????, Required        
        The starting point of the line.
            
        end, Array of ????, Required        
        The ending point of the line.
            
        track, Boolean, Optional        
        Draw a tracking line from arrStart. If omitted, a tracking line is drawn (True).
            
        Returns
        =======

        array
        The 3-D point selected by the user if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(798, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)), u"GetPointOnLine", None, message, flatten(start), flatten(end), track)

    def get_point_on_mesh(self, object, message):
        """        
        Pauses for user input of a point constrained to a mesh object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        message, String, Optional        
        A prompt or message.
            
        Returns
        =======

        array
        The 3-D point selected by the user successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(401, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"GetPointOnMesh", None, object, message)

    def get_point_on_plane(self, message, plane, point):
        """        
        Pauses for user input of a point constrained to a plane.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        plane, Array of ????, Optional        
        The plane to constrain the point to.
            
        point, Array of ????, Optional        
        A 3-D point from with to draw a tracking line. If omitted, a tracking line will not be drawn.
            
        Returns
        =======

        array
        The 3-D point selected by the user if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(797, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)), u"GetPointOnPlane", None, message, flatten(plane), flatten(point))

    def get_point_on_surface(self, object, message):
        """        
        Pauses for user input of a point constrained to a surface or polysurface object.
    
        Parameters
        ==========

        object, String, Required        
        The object's identifier.
            
        message, String, Optional        
        A prompt or message.
            
        Returns
        =======

        array
        The 3-D point selected by the user successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(148, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"GetPointOnSurface", None, object, message)

    def get_points(self, draw, plane, message1, message2, max_points, base_point):
        """        
        Pauses for user input of one or more points.
    
        Parameters
        ==========

        draw, Boolean, Optional        
        Draw lines between points.  The default is not to draw lines between points (False).
            
        plane, Boolean, Optional        
        Constrain the point selection to the active construction plane.  The default is not to constrain points to the active construction plane (False).
            
        message1, String, Optional        
        A prompt or message for the first point.
            
        message2, String, Optional        
        A prompt or message for the next points.
            
        max_points, Integer, Optional        
        The maximum number of points to pick.  If not specified, an unlimited number of points can be picked.
            
        base_point, Array of ????, Optional        
        A starting, or base, point.
            
        Returns
        =======

        array
        An array of 3-D points if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(67, 1, (VT_VARIANT, 0), ((VT_BOOL, 1), (VT_BOOL, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_I2, 1), (VT_VARIANT, 1)), u"GetPoints", None, draw, plane, message1, message2, max_points, flatten(base_point))

    def get_print_width(self, print_width):
        """        
        Displays a dialog box prompting the user to select a print width.
    
        Parameters
        ==========

        print_width, Double, Optional        
        The print width to select.  If omitted, the default print width will be selected.
            
        Returns
        =======

        number
        The value of the selected print width if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(674, 1, (VT_VARIANT, 0), ((VT_R8, 1),), u"GetPrintWidth", None, print_width)

    def get_real(self, message, number, min, max):
        """        
        Pauses for user input of a number.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        number, Double, Optional        
        A default number value.
            
        min, Double, Optional        
        A minimum allowable value.
            
        max, Double, Optional        
        A maximum allowable value.
            
        Returns
        =======

        number
        The number input by the user if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(63, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1), (VT_R8, 1)), u"GetReal", None, message, number, min, max)

    def get_rectangle(self):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def get_string(self, message, string, strings):
        """        
        Pauses for user input of string value.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        string, String, Optional        
        A default value.
            
        strings, Array of ????, Optional        
        A array of strings to be displayed as click-able command options. Note, strings cannot begin with a numeric character.
            
        Returns
        =======

        string
        The string either input or selected by the user if successful.  If the user presses the Enter key without typing in a string, an empty string  is returned.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(62, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1)), u"GetString", None, message, string, flatten(strings))

    def get_surface_iso_param_point(self, object, message):
        """        
        Pauses for user input of a point constrained to a surface object.
    
        Parameters
        ==========

        object, String, Required        
        The surface object's identifier.
            
        message, String, Optional        
        A prompt or message.
            
        Returns
        =======

        array
        An array of selection information if successful. The elements of the array are as follows:

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(775, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1)), u"GetSurfaceIsoParamPoint", None, object, message)

    def html_box(self, file_name, arguments, options, modal):
        """        
        Displays a custom, modal HTML dialog page. A modal dialog box retains the input focus while open. The user cannot switch windows until the dialog box is closed.
    
        Parameters
        ==========

        file_name, String, Required        
        The filename the HTML dialog page to display.
            
        arguments, Variant, Optional        
        An argument, or a zero-based, one-dimensional array of arguments, to pass to the HTML-dialog page.
            
        options, String, Optional        
        The window ornaments for the dialog box, using one or more of the following semicolon-delimited values:
		Value
		Description
		dialogHeight:sHeight
		Sets the height of the dialog window.
		dialogLeft:sXPos
		Sets the left position of the dialog window relative to the upper-left corner of the desktop.
		dialogTop:sYPos
		Sets the top position of the dialog window relative to the upper-left corner of the desktop.
		dialogWidth:sWidth
		Sets the width of the dialog window.
		center:{ yes | no | 1 | 0 | on | off }
		Specifies whether to center the dialog window within the desktop. The default is yes.
		dialogHide:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window is hidden when printing or using print preview. This feature is only available when a dialog box is opened from a trusted application. The default is no.
		edge:{ sunken | raised }
		Specifies the edge style of the dialog window. The default is raised.
		help:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window displays the context-sensitive Help icon. The default is yes.
		resizable:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window has fixed dimensions. The default is no.
		scroll:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window displays scrollbars. The default is yes.
		status:{ yes | no | 1 | 0 | on | off }
		Specifies whether the dialog window displays a status bar. The default is yes for untrusted dialog windows and no for trusted dialog windows.
		unadorned:{ yes | no | 1 | 0 | on | off }
            
        modal, Boolean, Optional        
        If omitted or True, a modal dialog will be displayed.  If False, a modeless dialog box will be displayed.
            
        Returns
        =======

        boolean
        If blnModal is specified and is True, then True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(276, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)), u"HtmlBox", None, file_name, arguments, options, modal)

    def integer_box(self, message, number, title):
        """        
        Displays a dialog box prompting the user to enter a whole number.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        number, Integer, Optional        
        A default whole number.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        number
        The whole number if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(55, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_BSTR, 1)), u"IntegerBox", None, message, number, title)

    def list_box(self, items, message, title):
        """        
        Displays a list of items in a list box dialog.
    
        Parameters
        ==========

        items, Array of ????, Required        
        A zero-based, one-dimensional array of string items.
            
        message, String, Optional        
        A prompt or message.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        string
        The selected item if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(56, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"ListBox", None, flatten(items), message, title)

    def message_beep(self, beep):
        """        
        Plays a system waveform sound.
    
        Parameters
        ==========

        beep, Integer, Optional        
        A sound type.  If omitted, a simple beep (0) is played:
		Value
		Description
		0
		Simple beep.
		1
		System asterisk.
		2
		System exclamation.
		3
		System hand.
		4
		System question.
		5
            
        No returns


        """

        return self._ApplyTypes_(149, 1, (VT_VARIANT, 0), ((VT_I2, 1),), u"MessageBeep", None, beep)

    def message_box(self, message, buttons, title):
        """        
        Displays a Windows message box. A message box contains an application-defined message and title, plus any combination of predefined icons and push buttons.
    
        Parameters
        ==========

        message, String, Required        
        A prompt or message.
            
        buttons, Integer, Optional        
        The buttons and icon to display.  This parameter can be a combination of the following flags.  If omitted, an OK button and no icon is displayed.
		Value
		Description
		0
		Display OK button only.
		1
		Display OK and Cancel buttons.
		2
		Display Abort, Retry, and Ignore buttons.
		3
		Display Yes, No, and Cancel buttons.
		4
		Display Yes and No buttons.
		5
		Display Retry and Cancel buttons.
		16
		Display Critical Message icon.
		32
		Display Warning Query icon.
		48
		Display Warning Message icon.
		64
		Display Information Message icon.
		0
		First button is the default.
		256
		Second button is the default.
		512
		Third button is the default.
		768
		Fourth button is the default.
		0
		Application modal. The user must respond to the message box before continuing work in the current application.
		4096
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        number
        An number indicating which button was clicked:

        """

        return self._ApplyTypes_(150, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_I2, 1), (VT_BSTR, 1)), u"MessageBox", None, message, buttons, title)

    def multi_list_box(self, items, message, title):
        """        
        Displays a list of items in a multiple-selection list box dialog.
    
        Parameters
        ==========

        items, Array of ????, Required        
        A zero-based, one-dimensional array of string items.
            
        message, String, Optional        
        A prompt or message.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array containing the selected item if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(57, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"MultiListBox", None, flatten(items), message, title)

    def open_file_name(self, title, filter, folder, filename, extension):
        """        
        Displays a Windows file open dialog box allowing the user to select a file name. Note, this function does not open the file.
    
        Parameters
        ==========

        title, String, Optional        
        A dialog box title.
            
        filter, String, Optional        
        A filter string.  The filter string must be in the following form:  "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.  If omitted, the filter (*.*) is used.
            
        folder, String, Optional        
        A default folder.
            
        filename, String, Optional        
        A default file name.
            
        extension, String, Optional        
        A default file extension.
            
        Returns
        =======

        string
        The file name if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(151, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"OpenFileName", None, title, filter, folder, filename, extension)

    def open_file_names(self, title, filter, folder, filename, extension):
        """        
        Displays a Windows file open dialog box allowing the user to select one or more file names. Note, this function does not open files.
    
        Parameters
        ==========

        title, String, Optional        
        A dialog box title.
            
        filter, String, Optional        
        A filter string.  The filter string must be in the following form:  "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.  If omitted, the filter (*.*) is used.
            
        folder, String, Optional        
        A default folder.
            
        filename, String, Optional        
        A default file name.
            
        extension, String, Optional        
        A default file extension.
            
        Returns
        =======

        array
        An array of file names if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(821, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"OpenFileNames", None, title, filter, folder, filename, extension)

    def popup_menu(self, items, modes, point, view):
        """        
        Displays a user-defined, context-style popup menu. The popup menu can appear almost anywhere. And, it can be dismissed by either clicking the left or right mouse buttons.
    
        Parameters
        ==========

        items, Array of ????, Required        
        An array of string representing the menu items. An empty string, or "", will create a menu separator item.
            
        modes, Array of ????, Optional        
        A array if numbers identifying the display mode of the corresponding menu items. If omitted, all menu items are enabled. Note, display modes are ignored for menu separators. The display modes are a follows:
		0
		The menu item is enabled.
		1
		The menu item is disabled.
		2
		The menu item is checked.
		3
            
        point, Array of ????, Optional        
        A 3-D point where the menu item is to appear. If omitted, the menu item will appear at the current cursor position.
            
        view, String, Optional        
        If arrPoint is specified, the strView is the view in which the menu is to appear. If arrPoint is specified but strView is omitted, then the menu will be displayed in the active view.
            
        Returns
        =======

        number
        The index of the menu item that was picked.

        number
        -1 if no menu item is picked.

        null
        On error.

        """

        return self._ApplyTypes_(595, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BSTR, 1)), u"PopupMenu", None, flatten(items), flatten(modes), flatten(point), view)

    def property_list_box(self, items, values, message, title):
        """        
        Displays a list of items and their values in a property-style list box dialog.
    
        Parameters
        ==========

        items, Array of ????, Required        
        A zero-based, one-dimensional array of string items.
            
        values, Array of ????, Required        
        A zero-based, one-dimensional array of strings indicating the value of each item in the list.
            
        message, String, Optional        
        A prompt or message.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        array
        A zero-based, one-dimensional array of strings indicating the new value of each item in the list.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(58, 1, (VT_VARIANT, 0), ((VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"PropertyListBox", None, flatten(items), flatten(values), message, title)

    def real_box(self, message, number, title):
        """        
        Displays a dialog box prompting the user to enter a number.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        number, Double, Optional        
        A default number..
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        number
        The number if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(59, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_R8, 1), (VT_BSTR, 1)), u"RealBox", None, message, number, title)

    def save_file_name(self, title, filter, folder, filename, extension):
        """        
        Displays a Windows file save dialog box allowing the user to enter a file name. Note, this function does not save the file.
    
        Parameters
        ==========

        title, String, Optional        
        A dialog box title.
            
        filter, String, Optional        
        A filter string.  The filter string must be in the following form:  "Description1|Filter1|Description2|Filter2||", where "||" terminates filter string.  If omitted, the filter (*.*) is used.
            
        folder, String, Optional        
        A default folder.
            
        filename, String, Optional        
        A default file name.
            
        extension, String, Optional        
        A default file extension.
            
        Returns
        =======

        string
        The file name if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(152, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"SaveFileName", None, title, filter, folder, filename, extension)

    def string_box(self, message, string, title):
        """        
        Displays a dialog box prompting the user to enter a string value.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt or message.
            
        string, String, Optional        
        A default string value.
            
        title, String, Optional        
        A dialog box title.
            
        Returns
        =======

        string
        The string value if successful.

        null
        If not successful, or on error.

        """

        return self._ApplyTypes_(60, 1, (VT_VARIANT, 0), ((VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)), u"StringBox", None, message, string, title)

