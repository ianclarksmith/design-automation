# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Application(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def add_alias(self, alias, macro):
        """        
        Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.
    
        Parameters
        ==========

        alias, String, Required        
        The name of the new command alias. The name cannot match command names or existing aliases.
            
        macro, String, Required        
        The macro to run when the alias is executed.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [alias, macro]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [alias, macro]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(709, 1, (VT_VARIANT, 0), magic, u"AddAlias", None, *flattened)

    def add_search_path(self, folder, index=None):
        """        
        Adds a new path to Rhino's search path list. Search path items can be added manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.
    
        Parameters
        ==========

        folder, String, Required        
        A valid folder, or path, to add.
            
        index, Integer, Optional        
        A zero-based position index in the search path list to insert the string. If omitted, the path will be appended to the end of the search path list.
            
        Returns
        =======

        number
        The zero-based index of the new search path item. If the index is less than zero, then the path item was not added to the search path list.

        null
        On error.

        """

        params = [folder, index]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [folder, index]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(511, 1, (VT_VARIANT, 0), magic, u"AddSearchPath", None, *flattened)

    def add_startup_script(self, script_file, index=None):
        """        
        Adds a new startup script to RhinoScript's startup script list. Startup script  items can be added manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.
    
        Parameters
        ==========

        script_file, String, Required        
        A valid path to a RhinoScript .RVB file.
            
        index, Integer, Optional        
        A zero-based position index in the startup script list to insert the string. If omitted, the path will be appended to the end of the startup script list.
            
        Returns
        =======

        number
        The zero-based index of the new startup script item. If the index is less than zero, then the path item was not added to the search path list.

        null
        On error.

        """

        params = [script_file, index]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [script_file, index]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(714, 1, (VT_VARIANT, 0), magic, u"AddStartupScript", None, *flattened)

    def alias_count(self):
        """        
        Returns the number of command alias in Rhino.
    
        No parameters

        Returns
        =======

        number
        True or False indicating success or failure.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(706, 1, (VT_VARIANT, 0), magic, u"AliasCount", None, *flattened)

    def alias_macro(self, alias, macro=None):
        """        
        Returns or modifies the macro of a command alias.
    
        Parameters
        ==========

        alias, String, Required        
        The name of an existing command alias.
            
        macro, String, Optional        
        The new macro to run when the alias is executed.
            
        Returns
        =======

        string
        If a new macro is not specified,  the existing macro if successful.

        string
        If a new macro is specified, the previous macro if successful.

        null
        If not successful, or on error.

        """

        params = [alias, macro]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [alias, macro]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(708, 1, (VT_VARIANT, 0), magic, u"AliasMacro", None, *flattened)

    def alias_names(self):
        """        
        Returns a list of command alias names.
    
        No parameters

        Returns
        =======

        array
        An array of string identifying the command alias names.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(707, 1, (VT_VARIANT, 0), magic, u"AliasNames", None, *flattened)

    def appearance_color(self, item, color=None):
        """        
        Returns or modifies an application interface item's color.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        item, Integer, Required        
        Item number to either query or modify.  The available items are as follows:
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
            
        color, Integer, Optional        
        The new color value.  If omitted, the current item color is returned.
            
        Returns
        =======

        number
        If a lngColor is not specified, the current item color if successful.

        number
        If a lngColor is specified, the previous item color if successful.

        null
        If not successful, or on error.

        """

        params = [item, color]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_I4, 1)]
        flattened = [item, color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(335, 1, (VT_VARIANT, 0), magic, u"AppearanceColor", None, *flattened)

    def appearance_display(self, item, show=None):
        """        
        Returns or modifies an application interface item's visibility.
    
        Parameters
        ==========

        item, Integer, Required        
        Item number to either query or modify.  The available items are as follows:
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
            
        show, Boolean, Optional        
        The new visibility state, either visible (True) or hidden (False).  If omitted, the current visibility state is returned.
            
        Returns
        =======

        number
        If a blnShow is not specified, the current visibility state if successful.

        number
        If a blnShow is specified, the visibility state if successful.

        null
        If not successful, or on error.

        """

        params = [item, show]
        required = [True, False]
        magic = [(VT_I2, 1), (VT_BOOL, 1)]
        flattened = [item, show]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(752, 1, (VT_VARIANT, 0), magic, u"AppearanceDisplay", None, *flattened)

    def autosave_file(self, file=None):
        """        
        Returns or changes the file name used by Rhino's automatic file saving mechanism.
    
        Parameters
        ==========

        file, String, Optional        
        The name of the new autosave file.
            
        Returns
        =======

        string
        If an autosave file is not specified, the name of the current autosave file if successful.

        string
        If an autosave file is specified, the name of the previous autosave file if successful.

        null
        If not successful, or on error.

        """

        params = [file]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [file]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(428, 1, (VT_VARIANT, 0), magic, u"AutosaveFile", None, *flattened)

    def autosave_interval(self, minutes=None):
        """        
        Returns or changes how often the document will be saved when Rhino's automatic file saving mechanism is enabled.
    
        Parameters
        ==========

        minutes, Integer, Optional        
        The number of minutes between saves.
            
        Returns
        =======

        number
        If an interval is not specified, the current interval in minutes if successful.

        number
        If an interval is specified, the previous interval in minutes if successful.

        null
        If not successful, or on error.

        """

        params = [minutes]
        required = [False]
        magic = [(VT_I2, 1),]
        flattened = [minutes]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(429, 1, (VT_VARIANT, 0), magic, u"AutosaveInterval", None, *flattened)

    def build_date(self):
        """        
        Returns the build date of Rhino.  The build date is a number in the form of YYYYMMDD.
    
        No parameters

        Returns
        =======

        number
        The build date of Rhino if successful.

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(360, 1, (VT_VARIANT, 0), magic, u"BuildDate", None, *flattened)

    def clear_command_history(self):
        """        
        Clears the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.
    
        No parameters

        No returns


        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(592, 1, (VT_VARIANT, 0), magic, u"ClearCommandHistory", None, *flattened)

    def command(self, command, echo=None):
        """        
        Runs a Rhino command script.  All Rhino commands can be used in command scripts.  The command can be a build-in Rhino command or a command that is provided by a 3rd party plug-in.
		Write command scripts just as you would type the command sequence at the command line. A space between characters or a new line act like pressing <Enter> at the command line.  For more information on writing command scripts, see "Scripting" in the Rhino help file.
		Note, this method is designed to run one command and one command only.  Do not combine multiple Rhino commands into a single call to this method.  For example:
		WRONG:
		Rhino.Command "_Line _SelLast _Invert"
		CORRECT:
		Rhino.Command "_Line"
		Rhino.Command "_SelLast"
		Rhino.Command "_Invert"
		Also, the exclamation point and space character ( ! ) combination used by button macros and batch-driven scripts to cancel the previous command is not valid.  For example:
		WRONG:
		Rhino.Command "! _Line _Pause _Pause"
		CORRECT:
		Rhino.Command "_Line _Pause _Pause"
		After the command script has run, you can obtain the identifiers of most recently created or changed object by calling LastCreatedObjects.
    
        Parameters
        ==========

        command, String, Required        
        A Rhino command including any arguments.
            
        echo, Boolean, Optional        
        The command echo mode.  If omitted, command prompts are echoed (True).
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [command, echo]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [command, echo]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(1, 1, (VT_VARIANT, 0), magic, u"Command", None, *flattened)

    def command_history(self):
        """        
        Returns the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.
    
        No parameters

        Returns
        =======

        string
        A string containing the contents of Rhino's command history window if successful.

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(591, 1, (VT_VARIANT, 0), magic, u"CommandHistory", None, *flattened)

    def default_renderer(self, renderer=None):
        """        
        Returns or changes Rhino's current, or default, render plug-in.  Use the PlugIns method to get a list of available render plug-ins.
    
        Parameters
        ==========

        renderer, String, Optional        
        The name of a render plug-in to set as default.
            
        Returns
        =======

        string
        If a render plug-in is not specified, the name of the current render plug-in if successful.

        string
        If a render plug-in is specified, the name of the previous current render plug-in if successful.

        null
        If not successful, or on error.

        """

        params = [renderer]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [renderer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(316, 1, (VT_VARIANT, 0), magic, u"DefaultRenderer", None, *flattened)

    def delete_alias(self, alias):
        """        
        Deletes an existing command alias from Rhino.
    
        Parameters
        ==========

        alias, String, Required        
        The name of an existing command alias.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        params = [alias]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [alias]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(710, 1, (VT_VARIANT, 0), magic, u"DeleteAlias", None, *flattened)

    def delete_search_path(self, folder):
        """        
        Removes an existing path from Rhino's search path list. Search path items can be removed manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.
    
        Parameters
        ==========

        folder, String, Required        
        A valid folder, or path, to remove.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [folder]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [folder]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(512, 1, (VT_VARIANT, 0), magic, u"DeleteSearchPath", None, *flattened)

    def delete_startup_script(self, script_file):
        """        
        Removes an existing startup script from RhinoScript's startup script list. Startup script items can be removed manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.
    
        Parameters
        ==========

        script_file, String, Required        
        An existing script file path to remove.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [script_file]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [script_file]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(715, 1, (VT_VARIANT, 0), magic, u"DeleteStartupScript", None, *flattened)

    def display_ole_alerts(self, display):
        """        
        Enables or disables OLE Server Busy/Not Responding dialog boxes from appearing during a lengthy OLE, or COM, operations. In detail, this function does the following:
		* Enables or disables the "Server Busy" dialog box, which is displayed when the message-pending delay expires during an OLE call.
		* Enables or disables the "Not Responding" dialog box, which is displayed if a keyboard or mouse message is pending during an OLE call and the call has timed out.
		Note, the display of OLE Server Busy/Not Responding dialog boxes will be re-enabled whenever the script engine is reset, either by running the ResetRhinoScript command or by having the Reinitialize option enabled in Tools->Options->RhinoScript.
    
        Parameters
        ==========

        display, Boolean, Required        
        Enable or disable the display of OLE alert dialog boxes.
            
        Returns
        =======

        null
        If successful or on error.

        """

        params = [display]
        required = [True]
        magic = [(VT_BOOL, 1),]
        flattened = [display]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(896, 1, (VT_VARIANT, 0), magic, u"DisplayOleAlerts", None, *flattened)

    def edge_analysis_color(self, color=None):
        """        
        Returns or modifies edge analysis color displayed by the ShowEdges command.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        color, Integer, Optional        
        The new color value.  If omitted, the current item color is returned.
            
        Returns
        =======

        number
        If a lngColor is not specified, the current edge analysis color if successful.

        number
        If a lngColor is specified, the previous edge analysis color if successful.

        null
        If not successful, or on error.

        """

        params = [color]
        required = [False]
        magic = [(VT_I4, 1),]
        flattened = [color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(449, 1, (VT_VARIANT, 0), magic, u"EdgeAnalysisColor", None, *flattened)

    def edge_analysis_mode(self, mode=None):
        """        
        Returns or modifies edge analysis mode displayed by the ShowEdges command.
    
        Parameters
        ==========

        mode, Integer, Optional        
        The new display mode.  If omitted, the current display mode is returned.  The available mores are as follows:
		0
		Display all edges.
		1
            
        Returns
        =======

        number
        If a intMode is not specified, the current edge analysis display mode if successful.

        number
        If a intMode is specified, the previous edge analysis display mode if successful.

        null
        If not successful, or on error.

        """

        params = [mode]
        required = [False]
        magic = [(VT_I2, 1),]
        flattened = [mode]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(448, 1, (VT_VARIANT, 0), magic, u"EdgeAnalysisMode", None, *flattened)

    def enable_autosave(self, enable=None):
        """        
        Enables or disables Rhino's automatic file saving mechanism.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The autosave state.  If omitted, automatic saving is enabled (True).
            
        Returns
        =======

        boolean
        The previous autosave state.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(430, 1, (VT_VARIANT, 0), magic, u"EnableAutosave", None, *flattened)

    def enable_history_recording(self, enable=None):
        """        
        Enables or disables Rhino's command history recording. For more information, see the Rhino help file for the History command.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The history recording state to set.
            
        Returns
        =======

        boolean
        If bEnable is not specified, then the current history recording state.

        boolean
        If bEnable is specified, then the previous history recording state.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(735, 1, (VT_VARIANT, 0), magic, u"EnableHistoryRecording", None, *flattened)

    def exe_folder(self):
        """        
        Returns the full path to Rhino's executable folder.
    
        No parameters

        Returns
        =======

        string
        Rhino's executable folder if successful.

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(21, 1, (VT_VARIANT, 0), magic, u"ExeFolder", None, *flattened)

    def exit(self):
        """        
        Closes the Rhino application.
    
        No parameters

        No returns


        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(537, 1, (VT_VARIANT, 0), magic, u"Exit", None, *flattened)

    def find_file(self, filename):
        """        
        Searches for a file using Rhino's search path. Rhino will look for a file in the following locations:
		1. The current document's folder.
		2. Folder's specified in Options dialog, File tab.
		3. Rhino's System folders.
    
        Parameters
        ==========

        filename, String, Required        
        A valid filename.
            
        Returns
        =======

        string
        A qualified path to the specified filename if successful.

        null
        If not successful, or on error.

        """

        params = [filename]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [filename]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(81, 1, (VT_VARIANT, 0), magic, u"FindFile", None, *flattened)

    def get_plug_in_object(self, plug_in):
        """        
        Returns a scriptable object from a specified plug-in. Note, not all plug-ins contain scriptable objects. Check with the manufacturer of your plug-in to see if they support this capability.
    
        Parameters
        ==========

        plug_in, String, Required        
        The name of a registered plug-in that supports scripting.  If the plug-in is registered but not loaded, it will be loaded.
            
        Returns
        =======

        null
        If not successful, or on error.

        """

        params = [plug_in]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [plug_in]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(636, 1, (VT_VARIANT, 0), magic, u"GetPlugInObject", None, *flattened)

    def help(self, topic=None):
        """        
        Displays a topic in Rhino's Help file.
    
        Parameters
        ==========

        topic, Integer, Optional        
        A help topic.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        """

        params = [topic]
        required = [False]
        magic = [(VT_I2, 1),]
        flattened = [topic]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(22, 1, (VT_VARIANT, 0), magic, u"Help", None, *flattened)

    def in_command(self, ignore_runners=None):
        """        
        Determines if Rhino is currently running a command. Because Rhino allow for transparent commands (commands that can be run from inside of other commands), this method returns the total number of active commands.
    
        Parameters
        ==========

        ignore_runners, Boolean, Optional        
        If true, script running commands, such as LoadScript, RunScript, and ReadCommandFile will not counted. The default is not to count script running command (true).
            
        Returns
        =======

        number
        The number of active commands.

        """

        params = [ignore_runners]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [ignore_runners]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(596, 1, (VT_VARIANT, 0), magic, u"InCommand", None, *flattened)

    def install_folder(self):
        """        
        Returns the full path to Rhino's installation folder.
    
        No parameters

        Returns
        =======

        string
        Rhino's installation folder if successful.

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(23, 1, (VT_VARIANT, 0), magic, u"InstallFolder", None, *flattened)

    def is_alias(self, alias):
        """        
        Verifies that a command alias exists in Rhino.
    
        Parameters
        ==========

        alias, String, Required        
        The name of an existing command alias.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        If not successful, or on error.

        """

        params = [alias]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [alias]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(711, 1, (VT_VARIANT, 0), magic, u"IsAlias", None, *flattened)

    def is_command(self, command_name):
        """        
        Verifies that a command exists in Rhino. The function is useful when scripting commands found in 3rd party plug-ins.
    
        Parameters
        ==========

        command_name, String, Required        
        The command name to test.
            
        Returns
        =======

        boolean
        True if successful, otherwise False.

        null
        On error.

        """

        params = [command_name]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [command_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(530, 1, (VT_VARIANT, 0), magic, u"IsCommand", None, *flattened)

    def last_command_name(self):
        """        
        Returns the name of the last executed command.
    
        No parameters

        Returns
        =======

        string
        The name of the last executed command.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(594, 1, (VT_VARIANT, 0), magic, u"LastCommandName", None, *flattened)

    def last_command_result(self):
        """        
        Returns the result code for the last executed command.
    
        No parameters

        Returns
        =======

        number
        The result code successful.  The result codes are as follows:

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(292, 1, (VT_VARIANT, 0), magic, u"LastCommandResult", None, *flattened)

    def last_loaded_script_file(self):
        """        
        Return the full path to the last RhinoScript file that was loaded using the LoadScript command..
    
        No parameters

        Returns
        =======

        string
        The last loaded script file if successful.

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(373, 1, (VT_VARIANT, 0), magic, u"LastLoadedScriptFile", None, *flattened)

    def locale_i_d(self):
        """        
        Returns the language used for the Rhino interface.  The current language is returned as a locale ID, or LCID, value.
    
        No parameters

        Returns
        =======

        number
        Rhino's current locale ID, or LCID.  The languages currently supported by Rhino are as follows:

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(450, 1, (VT_VARIANT, 0), magic, u"LocaleID", None, *flattened)

    def ortho(self, enable=None):
        """        
        Enables or disables Rhino's ortho modeling aid.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The new enabled status, either True or False.
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current ortho status if successful.

        boolean
        If blnEnable is specified, then the previous ortho status if successful.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(345, 1, (VT_VARIANT, 0), magic, u"Ortho", None, *flattened)

    def osnap(self, enable=None):
        """        
        Enables or disables Rhino's object snap modeling aid.  Object snaps are tools for specifying points on existing objects.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The new enabled status, either True or False.
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current object snap status if successful.

        boolean
        If blnEnable is specified, then the previous object snap status if successful.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(347, 1, (VT_VARIANT, 0), magic, u"Osnap", None, *flattened)

    def osnap_dialog(self, visible=None):
        """        
        Shows or hides Rhino's dockable object snap bar.
    
        Parameters
        ==========

        visible, Boolean, Optional        
        The new visibility state, either True or False.
            
        Returns
        =======

        boolean
        If blnVisible is not specified, then the current visibility state if successful.

        boolean
        If blnVisible is specified, then the previous visibility state if successful.

        """

        params = [visible]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [visible]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(349, 1, (VT_VARIANT, 0), magic, u"OsnapDialog", None, *flattened)

    def osnap_mode(self, mode=None):
        """        
        Returns or sets the object snap mode. Object snaps are tools for specifying points on existing objects.
    
        Parameters
        ==========

        mode, Integer, Optional        
        The object snap mode or modes to set.  Object snap modes can be added together to set multiple modes.
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

        number
        If intMode is not specified, then the current object snap mode or modes if successful.

        number
        If intMode is specified, then the previous object snap mode or modes if successful.

        null
        If not successful, or on error.

        """

        params = [mode]
        required = [False]
        magic = [(VT_I2, 1),]
        flattened = [mode]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(343, 1, (VT_VARIANT, 0), magic, u"OsnapMode", None, *flattened)

    def planar(self, enable=None):
        """        
        Enables or disables Rhino's planar modeling aid.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The new enabled status, either True or False
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current planar status if successful.

        boolean
        If blnEnable is specified, then the previous planar status if successful.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(346, 1, (VT_VARIANT, 0), magic, u"Planar", None, *flattened)

    def plug_ins(self, types=None, status=None):
        """        
        Returns an array of registered Rhino plug-ins.
    
        Parameters
        ==========

        types, Integer, Optional        
        The type or types of plug-ins to return.  Plug-in types can be added together to filter several different kinds of plug-ins.  If omitted, all plug-in types are returned.
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
            
        status, Integer, Optional        
        The status, either loaded or unloaded, of the plug-ins to return.  If omitted, both loaded and unloaded plug-ins are returned.
		Value
		Description
		0
		Both loaded or unloaded plug-ins..
		1
		Loaded plug-ins.
		2
            
        Returns
        =======

        array
        An array of strings describing the plug-ins if successful.

        null
        If not successful, or on error.

        """

        params = [types, status]
        required = [False, False]
        magic = [(VT_I2, 1), (VT_I2, 1)]
        flattened = [types, status]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(315, 1, (VT_VARIANT, 0), magic, u"PlugIns", None, *flattened)

    def print_(self, message=None):
        """        
        Prints a string to Rhino's command window.  Note, this method cannot be called from Visual Basic.  If you are using Visual Basic, use the PrintEx method.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt, message, or value.
            
        No returns


        """

        params = [message]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [message]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(2, 1, (VT_VARIANT, 0), magic, u"Print", None, *flattened)

    def print_ex(self, message=None):
        """        
        Prints a string to Rhino's command window.  Use this method, instead of the Print method, if you are using Visual Basic.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt, message, or value.
            
        No returns


        """

        params = [message]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [message]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(370, 1, (VT_VARIANT, 0), magic, u"PrintEx", None, *flattened)

    def project_osnaps(self, enable=None):
        """        
        Enables or disables object snap projection.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The new enabled status, either True or False.
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current object snap projection status if successful.

        boolean
        If blnEnable is specified, then the previous object snap projection status if successful.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(348, 1, (VT_VARIANT, 0), magic, u"ProjectOsnaps", None, *flattened)

    def prompt(self, prompt=None):
        """        
        Changes Rhino's command window prompt.
    
        Parameters
        ==========

        prompt, String, Optional        
        A prompt.
            
        No returns


        """

        params = [prompt]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [prompt]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(24, 1, (VT_VARIANT, 0), magic, u"Prompt", None, *flattened)

    def registry_key(self):
        """        
        Returns Rhino's Windows Registry key.
    
        No parameters

        Returns
        =======

        string
        Rhino's Windows Registry key if successful.

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(25, 1, (VT_VARIANT, 0), magic, u"RegistryKey", None, *flattened)

    def screen_size(self):
        """        
        Returns the current width and height, in pixels, of the screen of the primary display monitor.
    
        No parameters

        Returns
        =======

        array
        A zero-based, one-dimensional array containing two numbers identifying the width and height if successful

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(553, 1, (VT_VARIANT, 0), magic, u"ScreenSize", None, *flattened)

    def sdk_version(self):
        """        
        Returns the version of the Rhino SDK supported by the running version of Rhino.  Rhino SDK versions are 9 digit numbers in the form of YYYYMMDDn.
    
        No parameters

        Returns
        =======

        number
        The supported Rhino SDK version number if successful.

        null
        If not successful, or on error.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(359, 1, (VT_VARIANT, 0), magic, u"SdkVersion", None, *flattened)

    def search_path_count(self):
        """        
        Returns the number of path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.
    
        No parameters

        Returns
        =======

        number
        The number of path items in Rhino's search path list.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(509, 1, (VT_VARIANT, 0), magic, u"SearchPathCount", None, *flattened)

    def search_path_list(self):
        """        
        Returns all of the path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.
    
        No parameters

        Returns
        =======

        array
        An array of strings containing all of the path items in Rhino's search path list.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(510, 1, (VT_VARIANT, 0), magic, u"SearchPathList", None, *flattened)

    def send_keystrokes(self, keys=None, add_return=None):
        """        
        Sends a string of printable characters, including spaces, to Rhino's command line.
    
        Parameters
        ==========

        keys, String, Optional        
        A string to characters to send to the command line.
            
        add_return, Boolean, Optional        
        Append a return character to the end of the string. The default is to append a return character (True).
            
        No returns


        """

        params = [keys, add_return]
        required = [False, False]
        magic = [(VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [keys, add_return]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(496, 1, (VT_VARIANT, 0), magic, u"SendKeystrokes", None, *flattened)

    def snap(self, enable=None):
        """        
        Enables or disables Rhino's grid snap modeling aid.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The new enabled status, either True or False
            
        Returns
        =======

        boolean
        If blnEnable is not specified, then the current grid snap status if successful.

        boolean
        If blnEnable is specified, then the previous grid snap status if successful.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(344, 1, (VT_VARIANT, 0), magic, u"Snap", None, *flattened)

    def startup_script_count(self):
        """        
        Returns the number of startup script items in RhinoScript's startup script list. See "Options RhinoScript" for more details.
    
        No parameters

        Returns
        =======

        number
        The number of path items in Rhino's startup script list.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(712, 1, (VT_VARIANT, 0), magic, u"StartupScriptCount", None, *flattened)

    def startup_script_list(self):
        """        
        Returns all of the startup script items in Rhino's startup script list. See "Options RhinoScript" for more details.
    
        No parameters

        Returns
        =======

        array
        An array of strings containing all of the startup script items in RhinoScript's startup script list.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(713, 1, (VT_VARIANT, 0), magic, u"StartupScriptList", None, *flattened)

    def status_bar_distance(self, distance=None):
        """        
        Sets Rhino's status bar distance pane.
    
        Parameters
        ==========

        distance, Double, Optional        
        The distance to display.
            
        No returns


        """

        params = [distance]
        required = [False]
        magic = [(VT_R8, 1),]
        flattened = [distance]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(26, 1, (VT_VARIANT, 0), magic, u"StatusBarDistance", None, *flattened)

    def status_bar_message(self, message=None):
        """        
        Sets Rhino's status bar message pane.
    
        Parameters
        ==========

        message, String, Optional        
        A prompt, message, or value.
            
        No returns


        """

        params = [message]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [message]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(28, 1, (VT_VARIANT, 0), magic, u"StatusBarMessage", None, *flattened)

    def status_bar_number(self, number=None):
        """        
        Sets Rhino's status bar number pane.
    
        Parameters
        ==========

        number, Double, Optional        
        The number to display.
            
        No returns


        """

        params = [number]
        required = [False]
        magic = [(VT_R8, 1),]
        flattened = [number]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(312, 1, (VT_VARIANT, 0), magic, u"StatusBarNumber", None, *flattened)

    def status_bar_point(self, point=None):
        """        
        Sets Rhino's status bar point coordinate panes.
    
        Parameters
        ==========

        point, Array of Doubles, Optional        
        A 3-D point.
            
        No returns


        """

        params = [point]
        required = [False]
        magic = [(VT_ARRAY + VT_R8, 1),]
        flattened = [flatten_params(point)]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(27, 1, (VT_VARIANT, 0), magic, u"StatusBarPoint", None, *flattened)

    def template_file(self, filename=None):
        """        
        Returns or sets Rhino's default template file. The default template file is the template file used when Rhino starts.
    
        Parameters
        ==========

        filename, String, Optional        
        The name of the new default template file. Note, the template file must exist.
            
        Returns
        =======

        string
        If strFilename is not specified, then the current default template file if successful.

        string
        If strFilename is specified, then the previous default template file if successful.

        """

        params = [filename]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [filename]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(529, 1, (VT_VARIANT, 0), magic, u"TemplateFile", None, *flattened)

    def template_folder(self, folder=None):
        """        
        Returns or sets the location of Rhino's template files.
    
        Parameters
        ==========

        folder, String, Optional        
        The location of Rhino's template files. Note, the location, or folder, must exist.
            
        Returns
        =======

        string
        If strFolder is not specified, then the current template file folder if successful.

        string
        If strFolder is specified, then the previous template file folder if successful.

        """

        params = [folder]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [folder]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(528, 1, (VT_VARIANT, 0), magic, u"TemplateFolder", None, *flattened)

    def window_handle(self):
        """        
        Returns the Windows handle of Rhino's main window.
    
        No parameters

        Returns
        =======

        number
        Rhino's main window handle.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(29, 1, (VT_VARIANT, 0), magic, u"WindowHandle", None, *flattened)

    def working_folder(self, enable=None):
        """        
        Returns or sets Rhino's working directory, or folder.  The working folder is the default folder for all file operations.
    
        Parameters
        ==========

        enable, Boolean, Optional        
        The new working folder.
            
        Returns
        =======

        string
        If strFolder is not specified, then the current working folder if successful.

        string
        If strFolder is specified, then the previous working folder if successful.

        """

        params = [enable]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [enable]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(439, 1, (VT_VARIANT, 0), magic, u"WorkingFolder", None, *flattened)

