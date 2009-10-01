# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def appearance_color(item, color=pythoncom.Empty):

    """
    
        Returns or modifies an application interface item's color.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters
        ==========
        item  (integer, Required) - Item number to either query or modify.  The available items are as follows:
		Value
		Description
		0
		View background
		1
		Major grid line
		2
		Minor grid line
		3
		X-axis line
		4
		Y-axis line
		5
		Selected objects
		6
		Locked objects
		7
		New layers
		8
		Feedback
		9
		Tracking
		10
		Crosshair
		11
		Text
		12
		Text background
		13
        color  (integer, Optional) - The new color value.  If omitted, the current item color is returned.

        Returns
        =======
        number - If a color is not specified, the current item color if successful.
        number - If a color is specified, the previous item color if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AppearanceColor

        
    """
    return _base._rsf.appearance_color(item, color)

def appearance_display(item, show=pythoncom.Empty):

    """
    
        Returns or modifies an application interface item's visibility.

        Parameters
        ==========
        item  (integer, Required) - Item number to either query or modify.  The available items are as follows:
		Value
		Description
		0
		Application menu
		1
		Command prompt
		2
		Status bar
		3
		View title bars
		4
		Application title bar
		5
		Full path in application title bar
		6
        show  (boolean, Optional) - The new visibility state, either visible (True) or hidden (False).  If omitted, the current visibility state is returned.

        Returns
        =======
        number - If a show is not specified, the current visibility state if successful.
        number - If a show is specified, the visibility state if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AppearanceDisplay

        
    """
    return _base._rsf.appearance_display(item, show)

def display_ole_alerts(display):

    """
    
        Enables or disables OLE Server Busy/Not Responding dialog boxes from appearing during a lengthy OLE, or COM, operations. In detail, this function does the following:
		* Enables or disables the "Server Busy" dialog box, which is displayed when the message-pending delay expires during an OLE call.
		* Enables or disables the "Not Responding" dialog box, which is displayed if a keyboard or mouse message is pending during an OLE call and the call has timed out.
		Note, the display of OLE Server Busy/Not Responding dialog boxes will be re-enabled whenever the script engine is reset, either by running the ResetRhinoScript command or by having the Reinitialize option enabled in Tools->Options->RhinoScript.

        Parameters
        ==========
        display  (boolean, Required) - Enable or disable the display of OLE alert dialog boxes.

        Returns
        =======
        None - If successful or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DisplayOleAlerts

        
    """
    return _base._rsf.display_ole_alerts()

def edge_analysis_color(color=pythoncom.Empty):

    """
    
        Returns or modifies edge analysis color displayed by the ShowEdges command.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters
        ==========
        color  (integer, Optional) - The new color value.  If omitted, the current item color is returned.

        Returns
        =======
        number - If a color is not specified, the current edge analysis color if successful.
        number - If a color is specified, the previous edge analysis color if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EdgeAnalysisColor

        
    """
    return _base._rsf.edge_analysis_color(color)

def edge_analysis_mode(mode=pythoncom.Empty):

    """
    
        Returns or modifies edge analysis mode displayed by the ShowEdges command.

        Parameters
        ==========
        mode  (integer, Optional) - The new display mode.  If omitted, the current display mode is returned.  The available mores are as follows:
		0
		Display all edges.
		1

        Returns
        =======
        number - If a mode is not specified, the current edge analysis display mode if successful.
        number - If a mode is specified, the previous edge analysis display mode if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EdgeAnalysisMode

        
    """
    return _base._rsf.edge_analysis_mode(mode)

def enable_history_recording(enable=pythoncom.Empty):

    """
    
        Enables or disables Rhino's command history recording. For more information, see the Rhino help file for the History command.

        Parameters
        ==========
        enable  (boolean, Optional) - The history recording state to set.

        Returns
        =======
        boolean - If bEnable is not specified, then the current history recording state.
        boolean - If bEnable is specified, then the previous history recording state.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EnableHistoryRecording

        
    """
    return _base._rsf.enable_history_recording(enable)

def ortho(enable=pythoncom.Empty):

    """
    
        Enables or disables Rhino's ortho modeling aid.

        Parameters
        ==========
        enable  (boolean, Optional) - The new enabled status, either True or False.

        Returns
        =======
        boolean - If enable is not specified, then the current ortho status if successful.
        boolean - If enable is specified, then the previous ortho status if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Ortho

        
    """
    return _base._rsf.ortho(enable)

def osnap(enable=pythoncom.Empty):

    """
    
        Enables or disables Rhino's object snap modeling aid.  Object snaps are tools for specifying points on existing objects.

        Parameters
        ==========
        enable  (boolean, Optional) - The new enabled status, either True or False.

        Returns
        =======
        boolean - If enable is not specified, then the current object snap status if successful.
        boolean - If enable is specified, then the previous object snap status if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Osnap

        
    """
    return _base._rsf.osnap(enable)

def osnap_dialog(visible=pythoncom.Empty):

    """
    
        Shows or hides Rhino's dockable object snap bar.

        Parameters
        ==========
        visible  (boolean, Optional) - The new visibility state, either True or False.

        Returns
        =======
        boolean - If visible is not specified, then the current visibility state if successful.
        boolean - If visible is specified, then the previous visibility state if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OsnapDialog

        
    """
    return _base._rsf.osnap_dialog(visible)

def osnap_mode(mode=pythoncom.Empty):

    """
    
        Returns or sets the object snap mode. Object snaps are tools for specifying points on existing objects.

        Parameters
        ==========
        mode  (integer, Optional) - The object snap mode or modes to set.  Object snap modes can be added together to set multiple modes.
		Value
		Description
		0
		None
		1
		Near
		2
		Focus
		4
		Center
		8
		Knot
		16
		Quadrant
		32
		Midpoint
		64
		Intersection
		128
		End
		256
		Perpendicular
		512
		Tangent
		1024

        Returns
        =======
        number - If mode is not specified, then the current object snap mode or modes if successful.
        number - If mode is specified, then the previous object snap mode or modes if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: OsnapMode

        
    """
    return _base._rsf.osnap_mode(mode)

def planar(enable=pythoncom.Empty):

    """
    
        Enables or disables Rhino's planar modeling aid.

        Parameters
        ==========
        enable  (boolean, Optional) - The new enabled status, either True or False

        Returns
        =======
        boolean - If enable is not specified, then the current planar status if successful.
        boolean - If enable is specified, then the previous planar status if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Planar

        
    """
    return _base._rsf.planar(enable)

def project_osnaps(enable=pythoncom.Empty):

    """
    
        Enables or disables object snap projection.

        Parameters
        ==========
        enable  (boolean, Optional) - The new enabled status, either True or False.

        Returns
        =======
        boolean - If enable is not specified, then the current object snap projection status if successful.
        boolean - If enable is specified, then the previous object snap projection status if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ProjectOsnaps

        
    """
    return _base._rsf.project_osnaps(enable)

def snap(enable=pythoncom.Empty):

    """
    
        Enables or disables Rhino's grid snap modeling aid.

        Parameters
        ==========
        enable  (boolean, Optional) - The new enabled status, either True or False

        Returns
        =======
        boolean - If enable is not specified, then the current grid snap status if successful.
        boolean - If enable is specified, then the previous grid snap status if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Snap

        
    """
    return _base._rsf.snap(enable)
