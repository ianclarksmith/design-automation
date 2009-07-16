# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class UserInterface(DispatchBaseClass):



    def browse_for_folder(self, folder, message, title):
        """

        Displays the Windows browse-for-folder dialog box allowing the user to select a folder.

        Parameters

        Folder : Optional, String, str
        Message : Optional, String, str
        Title : Optional, String, str

        Returns

        String : The selected folder if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(146, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'BrowseForFolder', None, folder, message, title)

    def check_list_box(self, items, values, message, title):
        """

        Displays a list of items in a checkable-style list box dialog.

        Parameters

        Items : Required, Array, arr
        Values : Required, Array, arr
        Message : Optional, String, str
        Title : Optional, String, str

        Returns

        Array : A zero-based, one-dimensional array of boolean values indicating the new checked state of each item in the list.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(52, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'CheckListBox', None, items, values, message, title)

    def combo_list_box(self, items, message, title):
        """

        Displays a list of items in a combo-style list box dialog.

        Parameters

        Items : Required, Array, arr
        Message : Optional, String, str
        Title : Optional, String, str

        Returns

        String : The selected item if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(53, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ComboListBox', None, items, message, title)

    def edit_box(self, string, message, title):
        """

        Displays a dialog box prompting the user to enter a string value.  The string value may span multiple lines.

        Parameters

        String : Optional, String, str
        Message : Optional, String, str
        Title : Optional, String, str

        Returns

        String : Multiple lines that are separated by carriage return-linefeed combinations if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(54, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'EditBox', None, string, message, title)

    def get_angle(self, point, reference, angle, message):
        """

        Pauses for user input of an angle.

        Parameters

        Point : Optional, Array, arr
        Reference : Optional, Array, arr
        Angle : Optional, Number, dbl
        Message : Optional, String, str

        Returns

        Number : The angle in degrees if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(277, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'GetAngle', None, point, reference, angle, message)

    def get_boolean(self, message, items, defaults):
        """

        Pauses for user input of one or more boolean values. Boolean values are displayed as click-able command-line option toggles.

        Parameters

        Message : Required, String, str
        Items : Required, Array, arr
        Defaults : Required, Array, arr

        Returns

        Array : An array of boolean values that represent the boolean items, if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(622, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'GetBoolean', None, message, items, defaults)

    def get_box(self, mode, point, prompt1, prompt2, prompt3):
        """

        Pauses for user input of a box.

        Parameters

        Mode : Optional, Number, int
        Point : Optional, Array, arr
        Prompt1 : Optional, String, str
        Prompt2 : Optional, String, str
        Prompt3 : Optional, String, str

        Returns

        Array : An array of eight 3-D points that define the corners of the box if successful.  Points are returned in counter-clockwise order starting with the bottom rectangle of the box.  See the image below for details.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(342, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'GetBox', None, mode, point, prompt1, prompt2, prompt3)

    def get_color(self, color):
        """

        Displays the Rhino color picker dialog box allowing the user to select an RGB color value.

        Parameters

        Color : Optional, Number, lng

        Returns

        Number : The RGB color value selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(65, 1, (12, 0), ((12, 0)), u'GetColor', None, color)

    def get_distance(self, point, distance, message1, message2):
        """

        Pauses for user input of a distance.

        Parameters

        Point : Optional, Array, arr
        Distance : Optional, Number, dbl
        Message1 : Optional, String, str
        Message2 : Optional, String, str

        Returns

        Number : The distance input by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(66, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'GetDistance', None, point, distance, message1, message2)

    def get_integer(self, message, number, min, max):
        """

        Pauses for user input of a whole number.

        Parameters

        Message : Optional, String, str
        Number : Optional, Number, int
        Min : Optional, Number, int
        Max : Optional, Number, int

        Returns

        Number : The whole number input by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(64, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'GetInteger', None, message, number, min, max)

    def get_layer(self, title, layer, show_new_layer, show_set_current):
        """

        Displays a dialog box prompting the user to select a layer.

        Parameters

        Title : Optional, String, str
        Layer : Optional, String, str
        ShowNewLayer : Optional, Boolean, bln
        ShowSetCurrent : Optional, Boolean, bln

        Returns

        String : The name of the selected layer if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(672, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'GetLayer', None, title, layer, show_new_layer, show_set_current)

    def get_linetype(self, linetype):
        """

        Displays a dialog box prompting the user to select a linetype.

        Parameters

        Linetype : Optional, String, str

        Returns

        String : The name of the selected linetype if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(673, 1, (12, 0), ((12, 0)), u'GetLinetype', None, linetype)

    def get_point(self, message, point, distance, plane):
        """

        Pauses for user input of a point.

        Parameters

        Message : Optional, String, str
        Point : Optional, Array, arr
        Distance : Optional, Number, dbl
        Plane : Optional, Boolean, bln

        Returns

        Array : A zero-based, one-dimensional array containing three numbers identifying the 3-D point input by the user successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(61, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'GetPoint', None, message, point, distance, plane)

    def get_point_on_curve(self, object, message):
        """

        Pauses for user input of a point constrained to a curve object.

        Parameters

        Object : Required, String, str
        Message : Optional, String, str

        Returns

        Array : The 3-D point selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(147, 1, (12, 0), ((12, 0), (12, 0)), u'GetPointOnCurve', None, object, message)

    def get_point_on_line(self, message, start, end, track):
        """

        Pauses for user input of a point constrained to an infinite line.

        Parameters

        Message : Required, String, str
        Start : Required, Array, arr
        End : Required, Array, arr
        Track : Optional, Boolean, bln

        Returns

        Array : The 3-D point selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(798, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'GetPointOnLine', None, message, start, end, track)

    def get_point_on_mesh(self, object, message):
        """

        Pauses for user input of a point constrained to a mesh object.

        Parameters

        Object : Required, String, str
        Message : Optional, String, str

        Returns

        Array : The 3-D point selected by the user successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(401, 1, (12, 0), ((12, 0), (12, 0)), u'GetPointOnMesh', None, object, message)

    def get_point_on_plane(self, message, plane, point):
        """

        Pauses for user input of a point constrained to a plane.

        Parameters

        Message : Optional, String, str
        Plane : Optional, Array, arr
        Point : Optional, Array, arr

        Returns

        Array : The 3-D point selected by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(797, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'GetPointOnPlane', None, message, plane, point)

    def get_point_on_surface(self, object, message):
        """

        Pauses for user input of a point constrained to a surface or polysurface object.

        Parameters

        Object : Required, String, str
        Message : Optional, String, str

        Returns

        Array : The 3-D point selected by the user successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(148, 1, (12, 0), ((12, 0), (12, 0)), u'GetPointOnSurface', None, object, message)

    def get_points(self, draw, plane, message1, message2, max_points, base_point):
        """

        Pauses for user input of one or more points.

        Parameters

        Draw : Optional, Boolean, bln
        Plane : Optional, Boolean, bln
        Message1 : Optional, String, str
        Message2 : Optional, String, str
        MaxPoints : Optional, Number, int
        BasePoint : Optional, Array, arr

        Returns

        Array : An array of 3-D points if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(67, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'GetPoints', None, draw, plane, message1, message2, max_points, base_point)

    def get_print_width(self, print_width):
        """

        Displays a dialog box prompting the user to select a print width.

        Parameters

        PrintWidth : Optional, Number, dbl

        Returns

        Number : The value of the selected print width if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(674, 1, (12, 0), ((12, 0)), u'GetPrintWidth', None, print_width)

    def get_real(self, message, number, min, max):
        """

        Pauses for user input of a number.

        Parameters

        Message : Optional, String, str
        Number : Optional, Number, dbl
        Min : Optional, Number, dbl
        Max : Optional, Number, dbl

        Returns

        Number : The number input by the user if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(63, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'GetReal', None, message, number, min, max)

    def get_rectangle(self, mode, point, prompt1, prompt2, prompt3):
        """


        METHOD NOT IMPLEMENTED DUE TO PARAMETER MISMATCH


        """

        raise exceptions.NotImplementedError

    def get_string(self, message, string, strings):
        """

        Pauses for user input of string value.

        Parameters

        Message : Optional, String, str
        String : Optional, String, str
        Strings : Optional, Array, arr

        Returns

        String : The string either input or selected by the user if successful.  If the user presses the Enter key without typing in a string, an empty string "" is returned.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(62, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'GetString', None, message, string, strings)

    def get_surface_iso_param_point(self, object, message):
        """

        Pauses for user input of a point constrained to a surface object.

        Parameters

        Object : Required, String, str
        Message : Optional, String, str

        Returns

        Array : An array of selection information if successful. The elements of the array are as follows:
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(775, 1, (12, 0), ((12, 0), (12, 0)), u'GetSurfaceIsoParamPoint', None, object, message)

    def html_box(self, file_name, rguments, options, modal):
        """

        Displays a custom, modal HTML dialog page. A modal dialog box retains the input focus while open. The user cannot switch windows until the dialog box is closed.

        Parameters

        FileName : Required, String, str
        rguments : Optional, Variant, vaA
        Options : Optional, String, str
        Modal : Optional, Boolean, bln

        Returns

        Boolean : If blnModal is specified and is True, then True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(276, 1, (12, 0), ((12, 0), vaA, (12, 0), (12, 0)), u'HtmlBox', None, file_name, rguments, options, modal)

    def integer_box(self, message, number, title):
        """

        Displays a dialog box prompting the user to enter a whole number.

        Parameters

        Message : Optional, String, str
        Number : Optional, Number, int
        Title : Optional, String, str

        Returns

        Number : The whole number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(55, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'IntegerBox', None, message, number, title)

    def list_box(self, items, message, title):
        """

        Displays a list of items in a list box dialog.

        Parameters

        Items : Required, Array, arr
        Message : Optional, String, str
        Title : Optional, String, str

        Returns

        String : The selected item if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(56, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'ListBox', None, items, message, title)

    def message_beep(self, beep):
        """

        Plays a system waveform sound.

        Parameters

        Beep : Optional, Number, int

        No returns


        """

        return self._ApplyTypes_(149, 1, (12, 0), ((12, 0)), u'MessageBeep', None, beep)

    def message_box(self, message, buttons, title):
        """

        Displays a Windows message box. A message box contains an application-defined message and title, plus any combination of predefined icons and push buttons.

        Parameters

        Message : Required, String, str
        Buttons : Optional, Number, int
        Title : Optional, String, str

        Returns

        Number : An number indicating which button was clicked:

        """

        return self._ApplyTypes_(150, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'MessageBox', None, message, buttons, title)

    def multi_list_box(self, items, message, title):
        """

        Displays a list of items in a multiple-selection list box dialog.

        Parameters

        Items : Required, Array, arr
        Message : Optional, String, str
        Title : Optional, String, str

        Returns

        Array : A zero-based, one-dimensional array containing the selected item if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(57, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'MultiListBox', None, items, message, title)

    def open_file_name(self, title, filter, folder, filename, extension):
        """

        Displays a Windows file open dialog box allowing the user to select a file name. Note, this function does not open the file.

        Parameters

        Title : Optional, String, str
        Filter : Optional, String, str
        Folder : Optional, String, str
        Filename : Optional, String, str
        Extension : Optional, String, str

        Returns

        String : The file name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(151, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'OpenFileName', None, title, filter, folder, filename, extension)

    def open_file_names(self, title, filter, folder, filename, extension):
        """

        Displays a Windows file open dialog box allowing the user to select one or more file names. Note, this function does not open files.

        Parameters

        Title : Optional, String, str
        Filter : Optional, String, str
        Folder : Optional, String, str
        Filename : Optional, String, str
        Extension : Optional, String, str

        Returns

        Array : An array of file names if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(821, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'OpenFileNames', None, title, filter, folder, filename, extension)

    def popup_menu(self, r_items, modes, point, view):
        """

        Displays a user-defined, context-style popup menu. The popup menu can appear almost anywhere. And, it can be dismissed by either clicking the left or right mouse buttons.

        Parameters

        rItems : Required, Array, arr
        Modes : Optional, Array, arr
        Point : Optional, Array, arr
        View : Optional, String, str

        Returns

        Number : The index of the menu item that was picked.
        Number : -1 if no menu item is picked.
        Null : On error.

        """

        return self._ApplyTypes_(595, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'PopupMenu', None, r_items, modes, point, view)

    def property_list_box(self, items, values, message, title):
        """

        Displays a list of items and their values in a property-style list box dialog.

        Parameters

        Items : Required, Array, arr
        Values : Required, Array, arr
        Message : Optional, String, str
        Title : Optional, String, str

        Returns

        Array : A zero-based, one-dimensional array of strings indicating the new value of each item in the list.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(58, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0)), u'PropertyListBox', None, items, values, message, title)

    def real_box(self, message, number, title):
        """

        Displays a dialog box prompting the user to enter a number.

        Parameters

        Message : Optional, String, str
        Number : Optional, Number, dbl
        Title : Optional, String, str

        Returns

        Number : The number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(59, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'RealBox', None, message, number, title)

    def save_file_name(self, title, filter, folder, filename, extension):
        """

        Displays a Windows file save dialog box allowing the user to enter a file name. Note, this function does not save the file.

        Parameters

        Title : Optional, String, str
        Filter : Optional, String, str
        Folder : Optional, String, str
        Filename : Optional, String, str
        Extension : Optional, String, str

        Returns

        String : The file name if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(152, 1, (12, 0), ((12, 0), (12, 0), (12, 0), (12, 0), (12, 0)), u'SaveFileName', None, title, filter, folder, filename, extension)

    def string_box(self, message, string, title):
        """

        Displays a dialog box prompting the user to enter a string value.

        Parameters

        Message : Optional, String, str
        String : Optional, String, str
        Title : Optional, String, str

        Returns

        String : The string value if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(60, 1, (12, 0), ((12, 0), (12, 0), (12, 0)), u'StringBox', None, message, string, title)

