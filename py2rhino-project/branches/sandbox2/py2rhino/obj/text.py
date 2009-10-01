# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add_text(text, point, height=pythoncom.Empty, font=pythoncom.Empty, style=pythoncom.Empty):

    """
    
        Adds a text string to the document.

        Parameters
        ==========
        text  (string, Required) - The text to display.
        point  (List of float, Required) - A 3-D point.
        height  (float, Optional) - The text height.  If omitted, a height of 1.0 units is used.
        font  (string, Optional) - The text font.  If omitted, the Arial font is used.
        style  (integer, Optional) - The font style.  If omitted, a normal font style (0) is used.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal
		1
		Bold
		2

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddText

        
    """
    return _base._rsf.add_text(text, point, height, font, style)

def add_text_2(text, plane, height=pythoncom.Empty, font=pythoncom.Empty, style=pythoncom.Empty):

    """
    
        Adds a text string to the document.

        Parameters
        ==========
        text  (string, Required) - The text to display.
        plane  (List of float, Required) - The plane on which the text will lie.  The origin of the plane will be the origin point of the text.
        height  (float, Optional) - The text height.  If omitted, a height of 1.0 units is used.
        font  (string, Optional) - The text font.  If omitted, the Arial font is used.
        style  (integer, Optional) - The font style.  If omitted, a normal font style (0) is used.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal
		1
		Bold
		2

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddText

        
    """
    return _base._rsf.add_text_2(text, plane, height, font, style)

def add_text_dot(test, point):

    """
    
        Adds an annotation text dot to the document.

        Parameters
        ==========
        test  (string, Required) - A character or text string.
        point  (List of float, Required) - A 3-D point identifying the origin point.

        Returns
        =======
        string - The new object if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddTextDot

        
    """
    return _base._rsf.add_text_dot(test, point)

def text_dot_point(object, point=pythoncom.Empty):

    """
    
        Returns or modifies the location, or insertion point, of an annotation text dot object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        point  (List of float, Optional) - A 3-D point identifying the new location point.

        Returns
        =======
        list - If a new location is not specified,  the 3-D point identifying the current location if successful.
        list - If a new location is specified,  the 3-D point identifying the previous location if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextDotPoint

        
    """
    return _base._rsf.text_dot_point(object, point)

def text_dot_text(object, text=pythoncom.Empty):

    """
    
        Returns or modifies the text string of an annotation text dot object.  Annotation dots can be created using Rhino's Dot command.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        text  (string, Optional) - A new character or text string.

        Returns
        =======
        string - If a new text string is not specified,  the current string value if successful.
        string - If a new text string is specified,  the previous string value if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextDotText

        
    """
    return _base._rsf.text_dot_text(object, text)

def text_object_font(object, font=pythoncom.Empty):

    """
    
        Returns or modifies the font used by text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        font  (string, Optional) - The new font face name.  If omitted, the current font is returned.

        Returns
        =======
        string - If a font is not specified,  the current font face name if successful.
        string - If a font is specified,  the previous font face name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectFont

        
    """
    return _base._rsf.text_object_font(object, font)

def text_object_height(object, height=pythoncom.Empty):

    """
    
        Returns or modifies the height of a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        height  (float, Optional) - The new text height.  If omitted, the current text height is returned.

        Returns
        =======
        string - If a height is not specified, the current text height if successful.
        string - If a height is specified, the previous text height if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectHeight

        
    """
    return _base._rsf.text_object_height(object, height)

def text_object_plane(object, plane=pythoncom.Empty):

    """
    
        Returns or modifies the plane used by a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        plane  (List of float, Optional) - The new construction plane.  The elements of a plane list are as follows:
		Value
		Description
		0
		Required.  The construction plane's origin (3-D point).
		1
		Required.  The construction plane's X axis direction (3-D vector).
		2
		Required.  The construction plane's Y axis direction (3-D vector).
		3

        Returns
        =======
        list - If a plane is not specified, the current plane if successful.
        list - If a plane is specified, the previous plane if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectPlane

        
    """
    return _base._rsf.text_object_plane(object, plane)

def text_object_point(object, point=pythoncom.Empty):

    """
    
        Returns or modifies the location of a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        point  (List of float, Optional) - A 3-D point identifying the new location point.

        Returns
        =======
        string - If a new location is not specified,  the 3-D point identifying the current location if successful.
        string - If a new location is specified,  the 3-D point identifying the previous location if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectPoint

        
    """
    return _base._rsf.text_object_point(object, point)

def text_object_style(object, style=pythoncom.Empty):

    """
    
        Returns or modifies the font style of a text object.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        style  (integer, Optional) - The font style.  If omitted, the current font style is returned.  The font style can be any number of the following flags:
		Value
		Description
		0
		Normal.
		1
		Bold.
		2

        Returns
        =======
        number - If a style is not specified,  the current font style if successful.
        number - If a style is specified,  the previous font style if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectStyle

        
    """
    return _base._rsf.text_object_style(object, style)

def text_object_text(object, text=pythoncom.Empty):

    """
    
        Returns or modifies the text string of a text object.  Text objects can be created using Rhino's Text command.

        Parameters
        ==========
        object  (string, Required) - The identifier of the object.
        text  (string, Optional) - A new character or text string.

        Returns
        =======
        string - If a new text string is not specified,  the current string value if successful.
        string - If a new text string is specified,  the previous string value if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TextObjectText

        
    """
    return _base._rsf.text_object_text(object, text)
