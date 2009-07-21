# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Application(IRhinoScript):



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
        params_required = [True, True]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [alias, macro]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(709, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddAlias", None, *params_flattened)

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
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [folder, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(511, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddSearchPath", None, *params_flattened)

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
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_I2, 1)]
        params_flattened = [script_file, index]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(714, 1, (VT_VARIANT, 0), params_magic_numbers, u"AddStartupScript", None, *params_flattened)

    def alias_count():
        """        
        Returns the number of command alias in Rhino.
    
        No parameters

        Returns
        =======

        number
        True or False indicating success or failure.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(706, 1, (VT_VARIANT, 0), params_magic_numbers, u"AliasCount", None, *params_flattened)

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
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BSTR, 1)]
        params_flattened = [alias, macro]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(708, 1, (VT_VARIANT, 0), params_magic_numbers, u"AliasMacro", None, *params_flattened)

    def alias_names():
        """        
        Returns a list of command alias names.
    
        No parameters

        Returns
        =======

        array
        An array of string identifying the command alias names.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(707, 1, (VT_VARIANT, 0), params_magic_numbers, u"AliasNames", None, *params_flattened)

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
        params_required = [True, False]
        params_magic_numbers = [(VT_I2, 1), (VT_I4, 1)]
        params_flattened = [item, color]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(335, 1, (VT_VARIANT, 0), params_magic_numbers, u"AppearanceColor", None, *params_flattened)

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
        params_required = [True, False]
        params_magic_numbers = [(VT_I2, 1), (VT_BOOL, 1)]
        params_flattened = [item, show]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(752, 1, (VT_VARIANT, 0), params_magic_numbers, u"AppearanceDisplay", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [file]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(428, 1, (VT_VARIANT, 0), params_magic_numbers, u"AutosaveFile", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [minutes]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(429, 1, (VT_VARIANT, 0), params_magic_numbers, u"AutosaveInterval", None, *params_flattened)

    def build_date():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(360, 1, (VT_VARIANT, 0), params_magic_numbers, u"BuildDate", None, *params_flattened)

    def clear_command_history():
        """        
        Clears the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.
    
        No parameters

        No returns


        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(592, 1, (VT_VARIANT, 0), params_magic_numbers, u"ClearCommandHistory", None, *params_flattened)

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
        params_required = [True, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [command, echo]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(1, 1, (VT_VARIANT, 0), params_magic_numbers, u"Command", None, *params_flattened)

    def command_history():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(591, 1, (VT_VARIANT, 0), params_magic_numbers, u"CommandHistory", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [renderer]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(316, 1, (VT_VARIANT, 0), params_magic_numbers, u"DefaultRenderer", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [alias]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(710, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteAlias", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [folder]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(512, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteSearchPath", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [script_file]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(715, 1, (VT_VARIANT, 0), params_magic_numbers, u"DeleteStartupScript", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [display]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(896, 1, (VT_VARIANT, 0), params_magic_numbers, u"DisplayOleAlerts", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_I4, 1),]
        params_flattened = [color]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(449, 1, (VT_VARIANT, 0), params_magic_numbers, u"EdgeAnalysisColor", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [mode]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(448, 1, (VT_VARIANT, 0), params_magic_numbers, u"EdgeAnalysisMode", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(430, 1, (VT_VARIANT, 0), params_magic_numbers, u"EnableAutosave", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(735, 1, (VT_VARIANT, 0), params_magic_numbers, u"EnableHistoryRecording", None, *params_flattened)

    def exe_folder():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(21, 1, (VT_VARIANT, 0), params_magic_numbers, u"ExeFolder", None, *params_flattened)

    def exit():
        """        
        Closes the Rhino application.
    
        No parameters

        No returns


        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(537, 1, (VT_VARIANT, 0), params_magic_numbers, u"Exit", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [filename]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(81, 1, (VT_VARIANT, 0), params_magic_numbers, u"FindFile", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [plug_in]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(636, 1, (VT_VARIANT, 0), params_magic_numbers, u"GetPlugInObject", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [topic]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(22, 1, (VT_VARIANT, 0), params_magic_numbers, u"Help", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [ignore_runners]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(596, 1, (VT_VARIANT, 0), params_magic_numbers, u"InCommand", None, *params_flattened)

    def install_folder():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(23, 1, (VT_VARIANT, 0), params_magic_numbers, u"InstallFolder", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [alias]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(711, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsAlias", None, *params_flattened)

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
        params_required = [True]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [command_name]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(530, 1, (VT_VARIANT, 0), params_magic_numbers, u"IsCommand", None, *params_flattened)

    def last_command_name():
        """        
        Returns the name of the last executed command.
    
        No parameters

        Returns
        =======

        string
        The name of the last executed command.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(594, 1, (VT_VARIANT, 0), params_magic_numbers, u"LastCommandName", None, *params_flattened)

    def last_command_result():
        """        
        Returns the result code for the last executed command.
    
        No parameters

        Returns
        =======

        number
        The result code successful.  The result codes are as follows:

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(292, 1, (VT_VARIANT, 0), params_magic_numbers, u"LastCommandResult", None, *params_flattened)

    def last_loaded_script_file():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(373, 1, (VT_VARIANT, 0), params_magic_numbers, u"LastLoadedScriptFile", None, *params_flattened)

    def locale_i_d():
        """        
        Returns the language used for the Rhino interface.  The current language is returned as a locale ID, or LCID, value.
    
        No parameters

        Returns
        =======

        number
        Rhino's current locale ID, or LCID.  The languages currently supported by Rhino are as follows:

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(450, 1, (VT_VARIANT, 0), params_magic_numbers, u"LocaleID", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(345, 1, (VT_VARIANT, 0), params_magic_numbers, u"Ortho", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(347, 1, (VT_VARIANT, 0), params_magic_numbers, u"Osnap", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [visible]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(349, 1, (VT_VARIANT, 0), params_magic_numbers, u"OsnapDialog", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_I2, 1),]
        params_flattened = [mode]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(343, 1, (VT_VARIANT, 0), params_magic_numbers, u"OsnapMode", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(346, 1, (VT_VARIANT, 0), params_magic_numbers, u"Planar", None, *params_flattened)

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
        params_required = [False, False]
        params_magic_numbers = [(VT_I2, 1), (VT_I2, 1)]
        params_flattened = [types, status]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(315, 1, (VT_VARIANT, 0), params_magic_numbers, u"PlugIns", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(2, 1, (VT_VARIANT, 0), params_magic_numbers, u"Print", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(370, 1, (VT_VARIANT, 0), params_magic_numbers, u"PrintEx", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(348, 1, (VT_VARIANT, 0), params_magic_numbers, u"ProjectOsnaps", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [prompt]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(24, 1, (VT_VARIANT, 0), params_magic_numbers, u"Prompt", None, *params_flattened)

    def registry_key():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(25, 1, (VT_VARIANT, 0), params_magic_numbers, u"RegistryKey", None, *params_flattened)

    def screen_size():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(553, 1, (VT_VARIANT, 0), params_magic_numbers, u"ScreenSize", None, *params_flattened)

    def sdk_version():
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
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(359, 1, (VT_VARIANT, 0), params_magic_numbers, u"SdkVersion", None, *params_flattened)

    def search_path_count():
        """        
        Returns the number of path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.
    
        No parameters

        Returns
        =======

        number
        The number of path items in Rhino's search path list.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(509, 1, (VT_VARIANT, 0), params_magic_numbers, u"SearchPathCount", None, *params_flattened)

    def search_path_list():
        """        
        Returns all of the path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.
    
        No parameters

        Returns
        =======

        array
        An array of strings containing all of the path items in Rhino's search path list.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(510, 1, (VT_VARIANT, 0), params_magic_numbers, u"SearchPathList", None, *params_flattened)

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
        params_required = [False, False]
        params_magic_numbers = [(VT_BSTR, 1), (VT_BOOL, 1)]
        params_flattened = [keys, add_return]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(496, 1, (VT_VARIANT, 0), params_magic_numbers, u"SendKeystrokes", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(344, 1, (VT_VARIANT, 0), params_magic_numbers, u"Snap", None, *params_flattened)

    def startup_script_count():
        """        
        Returns the number of startup script items in RhinoScript's startup script list. See "Options RhinoScript" for more details.
    
        No parameters

        Returns
        =======

        number
        The number of path items in Rhino's startup script list.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(712, 1, (VT_VARIANT, 0), params_magic_numbers, u"StartupScriptCount", None, *params_flattened)

    def startup_script_list():
        """        
        Returns all of the startup script items in Rhino's startup script list. See "Options RhinoScript" for more details.
    
        No parameters

        Returns
        =======

        array
        An array of strings containing all of the startup script items in RhinoScript's startup script list.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(713, 1, (VT_VARIANT, 0), params_magic_numbers, u"StartupScriptList", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [distance]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(26, 1, (VT_VARIANT, 0), params_magic_numbers, u"StatusBarDistance", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [message]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(28, 1, (VT_VARIANT, 0), params_magic_numbers, u"StatusBarMessage", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_R8, 1),]
        params_flattened = [number]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(312, 1, (VT_VARIANT, 0), params_magic_numbers, u"StatusBarNumber", None, *params_flattened)

    def status_bar_point(self, point=None):
        """        
        Sets Rhino's status bar point coordinate panes.
    
        Parameters
        ==========

        point, Array of ????, Optional        
        A 3-D point.
            
        No returns


        """

        params = [point]
        params_required = [False]
        params_magic_numbers = [(VT_VARIANT, 1),]
        params_flattened = [flatten(point)]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(27, 1, (VT_VARIANT, 0), params_magic_numbers, u"StatusBarPoint", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [filename]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(529, 1, (VT_VARIANT, 0), params_magic_numbers, u"TemplateFile", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BSTR, 1),]
        params_flattened = [folder]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(528, 1, (VT_VARIANT, 0), params_magic_numbers, u"TemplateFolder", None, *params_flattened)

    def window_handle():
        """        
        Returns the Windows handle of Rhino's main window.
    
        No parameters

        Returns
        =======

        number
        Rhino's main window handle.

        """

        params = []
        params_required = []
        params_magic_numbers = []
        params_flattened = []

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(29, 1, (VT_VARIANT, 0), params_magic_numbers, u"WindowHandle", None, *params_flattened)

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
        params_required = [False]
        params_magic_numbers = [(VT_BOOL, 1),]
        params_flattened = [enable]

        for i in range(len(params)):
            if (params[i] == None) and (not params_required[i]):
                params_magic_numbers.pop(i)
                params_flattened.pop(i)

        params_magic_numbers = tuple(params_magic_numbers)
        params_flattened = tuple(params_flattened)

        return self._ApplyTypes_(439, 1, (VT_VARIANT, 0), params_magic_numbers, u"WorkingFolder", None, *params_flattened)

