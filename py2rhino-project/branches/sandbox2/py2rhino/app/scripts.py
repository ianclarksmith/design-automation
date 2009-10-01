# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add_startup_script(script_file, index=pythoncom.Empty):

    """
    
        Adds a new startup script to RhinoScript's startup script list. Startup script  items can be added manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.

        Parameters
        ==========
        script_file  (string, Required) - A valid path to a RhinoScript .RVB file.
        index  (integer, Optional) - A zero-based position index in the startup script list to insert the string. If omitted, the path will be appended to the end of the startup script list.

        Returns
        =======
        number - The zero-based index of the new startup script item. If the index is less than zero, then the path item was not added to the search path list.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddStartupScript

        
    """
    return _base._rsf.add_startup_script(script_file, index)

def delete_startup_script(script_file):

    """
    
        Removes an existing startup script from RhinoScript's startup script list. Startup script items can be removed manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.

        Parameters
        ==========
        script_file  (string, Required) - An existing script file path to remove.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteStartupScript

        
    """
    return _base._rsf.delete_startup_script(script_file)

def get_plug_in_object(plug_in):

    """
    
        Returns a scriptable object from a specified plug-in. Note, not all plug-ins contain scriptable objects. Check with the manufacturer of your plug-in to see if they support this capability.

        Parameters
        ==========
        plug_in  (string, Required) - The name of a registered plug-in that supports scripting.  If the plug-in is registered but not loaded, it will be loaded.

        Returns
        =======
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: GetPlugInObject

        
    """
    return _base._rsf.get_plug_in_object(plug_in)

def last_loaded_script_file():

    """
    
        Return the full path to the last RhinoScript file that was loaded using the LoadScript command..

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - The last loaded script file if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LastLoadedScriptFile

        
    """
    return _base._rsf.last_loaded_script_file()

def plug_ins(types=pythoncom.Empty, status=pythoncom.Empty):

    """
    
        Returns an array of registered Rhino plug-ins.

        Parameters
        ==========
        types  (integer, Optional) - The type or types of plug-ins to return.  Plug-in types can be added together to filter several different kinds of plug-ins.  If omitted, all plug-in types are returned.
		Value
		Description
		0
		All plug-ins
		1
		Render plug-ins
		2
		File export plug-ins
		4
		File import plug-ins
		8
		Digitizer plug-ins
		16
        status  (integer, Optional) - The status, either loaded or unloaded, of the plug-ins to return.  If omitted, both loaded and unloaded plug-ins are returned.
		Value
		Description
		0
		Both loaded or unloaded plug-ins..
		1
		Loaded plug-ins.
		2

        Returns
        =======
        list - A list of strings describing the plug-ins if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PlugIns

        
    """
    return _base._rsf.plug_ins(types, status)

def startup_script_count():

    """
    
        Returns the number of startup script items in RhinoScript's startup script list. See "Options RhinoScript" for more details.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of path items in Rhino's startup script list.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: StartupScriptCount

        
    """
    return _base._rsf.startup_script_count()

def startup_script_list():

    """
    
        Returns all of the startup script items in Rhino's startup script list. See "Options RhinoScript" for more details.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of strings containing all of the startup script items in RhinoScript's startup script list.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: StartupScriptList

        
    """
    return _base._rsf.startup_script_list()
