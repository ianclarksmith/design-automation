# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def status_bar_distance(distance=pythoncom.Empty):

    """
    
        Sets Rhino's status bar distance pane.

        Parameters
        ==========
        distance  (float, Optional) - The distance to display.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: StatusBarDistance

        
    """
    return _base._rsf.status_bar_distance()

def status_bar_message(message=pythoncom.Empty):

    """
    
        Sets Rhino's status bar message pane.

        Parameters
        ==========
        message  (string, Optional) - A prompt, message, or value.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: StatusBarMessage

        
    """
    return _base._rsf.status_bar_message()

def status_bar_number(number=pythoncom.Empty):

    """
    
        Sets Rhino's status bar number pane.

        Parameters
        ==========
        number  (float, Optional) - The number to display.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: StatusBarNumber

        
    """
    return _base._rsf.status_bar_number()

def status_bar_point(point=pythoncom.Empty):

    """
    
        Sets Rhino's status bar point coordinate panes.

        Parameters
        ==========
        point  (List of float, Optional) - A 3-D point.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: StatusBarPoint

        
    """
    return _base._rsf.status_bar_point()
