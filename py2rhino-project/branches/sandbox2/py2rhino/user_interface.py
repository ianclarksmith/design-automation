# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class UserInterface(IRhinoScript):



    def browse_for_folder(self, folder=None, message=None, title=None):
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

        params = [folder, message, title]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [folder, message, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(146, 1, (VT_VARIANT, 0), params_magic_numbers, u"BrowseForFolder", None, *params_flattened)

    def check_list_box(self, items, values, message=None, title=None):
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

        params = [items, values, message, title]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(items), flatten(values), message, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(52, 1, (VT_VARIANT, 0), params_magic_numbers, u"CheckListBox", None, *params_flattened)

    def combo_list_box(self, items, message=None, title=None):
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

        params = [items, message, title]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(items), message, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(53, 1, (VT_VARIANT, 0), params_magic_numbers, u"ComboListBox", None, *params_flattened)

    def edit_box(self, string=None, message=None, title=None):
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

        params = [string, message, title]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [string, message, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(54, 1, (VT_VARIANT, 0), params_magic_numbers, u"EditBox", None, *params_flattened)

    def get_angle(self, point=None, reference=None, angle=None, message=None):
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

        params = [point, reference, angle, message]
        params_required = [False, False, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_R8, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(point), flatten(reference), angle, message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(277, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetAngle", None, *params_flattened)

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

        params = [message, items, defaults]
        params_required = [True, True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [message, flatten(items), flatten(defaults)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(622, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetBoolean", None, *params_flattened)

    def get_box(self, mode=None, point=None, prompt1=None, prompt2=None, prompt3=None):
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

        params = [mode, point, prompt1, prompt2, prompt3]
        params_required = [False, False, False, False, False]
        params_magic_numbers = [(VT_I2, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [mode, flatten(point), prompt1, prompt2, prompt3]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(342, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetBox", None, *params_flattened)

    def get_color(self, color=None):
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

        params = [color]
        params_required = [False]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [color]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(65, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetColor", None, *params_flattened)

    def get_distance(self, point=None, distance=None, message1=None, message2=None):
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

        params = [point, distance, message1, message2]
        params_required = [False, False, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_R8, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(point), distance, message1, message2]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(66, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetDistance", None, *params_flattened)

    def get_integer(self, message=None, number=None, min=None, max=None):
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

        params = [message, number, min, max]
        params_required = [False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_I2, 1), (VT_I2, 1)]
        params_flattened = [message, number, min, max]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(64, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetInteger", None, *params_flattened)

    def get_layer(self, title=None, layer=None, show_new_layer=None, show_set_current=None):
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

        params = [title, layer, show_new_layer, show_set_current]
        params_required = [False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BOOL, 1), (VT_BOOL, 1)]
        params_flattened = [title, layer, show_new_layer, show_set_current]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(672, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetLayer", None, *params_flattened)

    def get_linetype(self, linetype=None):
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

        params = [linetype]
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [linetype]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(673, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetLinetype", None, *params_flattened)

    def get_point_on_curve(self, object, message=None):
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

        params = [object, message]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(147, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPointOnCurve", None, *params_flattened)

    def get_point_on_line(self, message, start, end, track=None):
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

        params = [message, start, end, track]
        params_required = [True, True, True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BOOL, 1)]
        params_flattened = [message, flatten(start), flatten(end), track]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(798, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPointOnLine", None, *params_flattened)

    def get_point_on_mesh(self, object, message=None):
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

        params = [object, message]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(401, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPointOnMesh", None, *params_flattened)

    def get_point_on_plane(self, message=None, plane=None, point=None):
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

        params = [message, plane, point]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_VARIANT, 1)]
        params_flattened = [message, flatten(plane), flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(797, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPointOnPlane", None, *params_flattened)

    def get_point_on_surface(self, object, message=None):
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

        params = [object, message]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(148, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPointOnSurface", None, *params_flattened)

    def get_points(self, draw=None, plane=None, message1=None, message2=None, max_points=None, base_point=None):
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

        params = [draw, plane, message1, message2, max_points, base_point]
        params_required = [False, False, False, False, False, False]
        params_magic_numbers = [(VT_BOOL, 1), (VT_BOOL, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_I2, 1), (VT_VARIANT, 1)]
        params_flattened = [draw, plane, message1, message2, max_points, flatten(base_point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(67, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPoints", None, *params_flattened)

    def get_print_width(self, print_width=None):
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

        params = [print_width]
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [print_width]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(674, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPrintWidth", None, *params_flattened)

    def get_real(self, message=None, number=None, min=None, max=None):
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

        params = [message, number, min, max]
        params_required = [False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_R8, 1), (VT_R8, 1)]
        params_flattened = [message, number, min, max]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(63, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetReal", None, *params_flattened)

    def get_rectangle(self, mode=None, point=None, prompt1=None, prompt2=None, prompt3=None):
        """        
        Pauses for user input of a rectangle.
    
        Parameters
        ==========

        mode, Integer, Optional        
        The rectangle selection mode.  If not specified, all modes (0) are available.  The rectangle selection modes are as follows:
		Value
		Description
		0
		All modes.
		1
		Corner.  A rectangle is created by picking two corner points.
		2
		3-Point.  A rectangle is created by picking three points
		3
		Vertical.  A vertical rectangle is created by picking three points.
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
        An array of four 3-D points that define the corners of the rectangle if successful.  Points are returned in counter-clockwise order.  See the image below for details.

        null
        If not successful, or on error.

        """

        params = [mode, point, prompt1, prompt2, prompt3]
        params_required = [False, False, False, False, False]
        params_magic_numbers = [(VT_I2, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [mode, flatten(point), prompt1, prompt2, prompt3]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(341, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetRectangle", None, *params_flattened)

    def get_string(self, message=None, string=None, strings=None):
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

        params = [message, string, strings]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_VARIANT, 1)]
        params_flattened = [message, string, flatten(strings)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(62, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetString", None, *params_flattened)

    def get_surface_iso_param_point(self, object, message=None):
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

        params = [object, message]
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [object, message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(775, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetSurfaceIsoParamPoint", None, *params_flattened)

    def html_box(self, file_name, arguments=None, options=None, modal=None):
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

        params = [file_name, arguments, options, modal]
        params_required = [True, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [file_name, arguments, options, modal]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(276, 1, (VT_VARIANT, 0), params_magic_numbers, u"HtmlBox", None, *params_flattened)

    def integer_box(self, message=None, number=None, title=None):
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

        params = [message, number, title]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_BSTR, 1)]
        params_flattened = [message, number, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(55, 1, (VT_VARIANT, 0), params_magic_numbers, u"IntegerBox", None, *params_flattened)

    def list_box(self, items, message=None, title=None):
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

        params = [items, message, title]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(items), message, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(56, 1, (VT_VARIANT, 0), params_magic_numbers, u"ListBox", None, *params_flattened)

    def message_beep(self, beep=None):
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

        params = [beep]
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [beep]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(149, 1, (VT_VARIANT, 0), params_magic_numbers, u"MessageBeep", None, *params_flattened)

    def message_box(self, message, buttons=None, title=None):
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

        params = [message, buttons, title]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1), (VT_BSTR, 1)]
        params_flattened = [message, buttons, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(150, 1, (VT_VARIANT, 0), params_magic_numbers, u"MessageBox", None, *params_flattened)

    def multi_list_box(self, items, message=None, title=None):
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

        params = [items, message, title]
        params_required = [True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(items), message, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(57, 1, (VT_VARIANT, 0), params_magic_numbers, u"MultiListBox", None, *params_flattened)

    def open_file_names(self, title=None, filter=None, folder=None, filename=None, extension=None):
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

        params = [title, filter, folder, filename, extension]
        params_required = [False, False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [title, filter, folder, filename, extension]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(821, 1, (VT_VARIANT, 0), params_magic_numbers, u"OpenFileNames", None, *params_flattened)

    def popup_menu(self, items, modes=None, point=None, view=None):
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

        params = [items, modes, point, view]
        params_required = [True, False, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(items), flatten(modes), flatten(point), view]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(595, 1, (VT_VARIANT, 0), params_magic_numbers, u"PopupMenu", None, *params_flattened)

    def property_list_box(self, items, values, message=None, title=None):
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

        params = [items, values, message, title]
        params_required = [True, True, False, False]
        params_magic_numbers = [(VT_VARIANT, 1), (VT_VARIANT, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [flatten(items), flatten(values), message, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(58, 1, (VT_VARIANT, 0), params_magic_numbers, u"PropertyListBox", None, *params_flattened)

    def real_box(self, message=None, number=None, title=None):
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

        params = [message, number, title]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_R8, 1), (VT_BSTR, 1)]
        params_flattened = [message, number, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(59, 1, (VT_VARIANT, 0), params_magic_numbers, u"RealBox", None, *params_flattened)

    def save_file_name(self, title=None, filter=None, folder=None, filename=None, extension=None):
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

        params = [title, filter, folder, filename, extension]
        params_required = [False, False, False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [title, filter, folder, filename, extension]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(152, 1, (VT_VARIANT, 0), params_magic_numbers, u"SaveFileName", None, *params_flattened)

    def string_box(self, message=None, string=None, title=None):
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

        params = [message, string, title]
        params_required = [False, False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [message, string, title]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(60, 1, (VT_VARIANT, 0), params_magic_numbers, u"StringBox", None, *params_flattened)

