

class application():

        build_date = """
        Returns the build date of Rhino.  The build date is a number in the form of YYYYMMDD.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The build date of Rhino if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: BuildDate

        """
        default_renderer = """
        Returns or changes Rhino's current, or default, render plug-in.  Use the PlugIns method to get a list of available render plug-ins.

        Parameters
        ==========
        renderer  (string, Optional) - The name of a render plug-in to set as default.

        Returns
        =======
        string - If a render plug-in is not specified, the name of the current render plug-in if successful.
        string - If a render plug-in is specified, the name of the previous current render plug-in if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DefaultRenderer

        """
        exit = """
        Closes the Rhino application.

        Parameters
        ==========
        No parameters

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Exit

        """
        help = """
        Displays a topic in Rhino's Help file.

        Parameters
        ==========
        topic  (integer, Optional) - A help topic.

        Returns
        =======
        boolean - True or False indicating success or failure.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Help

        """
        locale_i_d = """
        Returns the language used for the Rhino interface.  The current language is returned as a locale ID, or LCID, value.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - Rhino's current locale ID, or LCID.  The languages currently supported by Rhino are as follows:

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LocaleID

        """
        print_ = """
        Prints a string to Rhino's command window.  Note, this method cannot be called from Visual Basic.  If you are using Visual Basic, use the PrintEx method.

        Parameters
        ==========
        message  (string, Optional) - A prompt, message, or value.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Print

        """
        print_ex = """
        Prints a string to Rhino's command window.  Use this method, instead of the Print method, if you are using Visual Basic.

        Parameters
        ==========
        message  (string, Optional) - A prompt, message, or value.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PrintEx

        """
        prompt = """
        Changes Rhino's command window prompt.

        Parameters
        ==========
        prompt  (string, Optional) - A prompt.

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Prompt

        """
        registry_key = """
        Returns Rhino's Windows Registry key.

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - Rhino's Windows Registry key if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RegistryKey

        """
        screen_size = """
        Returns the current width and height, in pixels, of the screen of the primary display monitor.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A zero-based, one-dimensional list containing two numbers identifying the width and height if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ScreenSize

        """
        sdk_version = """
        Returns the version of the Rhino SDK supported by the running version of Rhino.  Rhino SDK versions are 9 digit numbers in the form of YYYYMMDDn.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The supported Rhino SDK version number if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SdkVersion

        """
        send_keystrokes = """
        Sends a string of printable characters, including spaces, to Rhino's command line.

        Parameters
        ==========
        keys  (string, Optional) - A string to characters to send to the command line.
        add_return  (boolean, Optional) - Append a return character to the end of the string. The default is to append a return character (True).

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SendKeystrokes

        """
        window_handle = """
        Returns the Windows handle of Rhino's main window.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - Rhino's main window handle.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: WindowHandle

        """


class commands():

        add_alias = """
        Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.

        Parameters
        ==========
        alias  (string, Required) - The name of the new command alias. The name cannot match command names or existing aliases.
        macro  (string, Required) - The macro to run when the alias is executed.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddAlias

        """
        alias_count = """
        Returns the number of command alias in Rhino.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - True or False indicating success or failure.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AliasCount

        """
        alias_macro = """
        Returns or modifies the macro of a command alias.

        Parameters
        ==========
        alias  (string, Required) - The name of an existing command alias.
        macro  (string, Optional) - The new macro to run when the alias is executed.

        Returns
        =======
        string - If a new macro is not specified,  the existing macro if successful.
        string - If a new macro is specified, the previous macro if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AliasMacro

        """
        alias_names = """
        Returns a list of command alias names.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of string identifying the command alias names.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AliasNames

        """
        clear_command_history = """
        Clears the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.

        Parameters
        ==========
        No parameters

        Returns
        =======
        No returns

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ClearCommandHistory

        """
        command = """
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
        command  (string, Required) - A Rhino command including any arguments.
        echo  (boolean, Optional) - The command echo mode.  If omitted, command prompts are echoed (True).

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: Command

        """
        command_history = """
        Returns the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - A string containing the contents of Rhino's command history window if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CommandHistory

        """
        delete_alias = """
        Deletes an existing command alias from Rhino.

        Parameters
        ==========
        alias  (string, Required) - The name of an existing command alias.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteAlias

        """
        in_command = """
        Determines if Rhino is currently running a command. Because Rhino allow for transparent commands (commands that can be run from inside of other commands), this method returns the total number of active commands.

        Parameters
        ==========
        ignore_runners  (boolean, Optional) - If true, script running commands, such as LoadScript, RunScript, and ReadCommandFile will not counted. The default is not to count script running command (true).

        Returns
        =======
        number - The number of active commands.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InCommand

        """
        is_alias = """
        Verifies that a command alias exists in Rhino.

        Parameters
        ==========
        alias  (string, Required) - The name of an existing command alias.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsAlias

        """
        is_command = """
        Verifies that a command exists in Rhino. The function is useful when scripting commands found in 3rd party plug-ins.

        Parameters
        ==========
        command_name  (string, Required) - The command name to test.

        Returns
        =======
        boolean - True if successful, otherwise False.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsCommand

        """
        last_command_name = """
        Returns the name of the last executed command.

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - The name of the last executed command.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LastCommandName

        """
        last_command_result = """
        Returns the result code for the last executed command.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The result code successful.  The result codes are as follows:

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LastCommandResult

        """


class files():

        add_search_path = """
        Adds a new path to Rhino's search path list. Search path items can be added manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.

        Parameters
        ==========
        folder  (string, Required) - A valid folder, or path, to add.
        index  (integer, Optional) - A zero-based position index in the search path list to insert the string. If omitted, the path will be appended to the end of the search path list.

        Returns
        =======
        number - The zero-based index of the new search path item. If the index is less than zero, then the path item was not added to the search path list.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddSearchPath

        """
        autosave_file = """
        Returns or changes the file name used by Rhino's automatic file saving mechanism.

        Parameters
        ==========
        file  (string, Optional) - The name of the new autosave file.

        Returns
        =======
        string - If an autosave file is not specified, the name of the current autosave file if successful.
        string - If an autosave file is specified, the name of the previous autosave file if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AutosaveFile

        """
        autosave_interval = """
        Returns or changes how often the document will be saved when Rhino's automatic file saving mechanism is enabled.

        Parameters
        ==========
        minutes  (integer, Optional) - The number of minutes between saves.

        Returns
        =======
        number - If an interval is not specified, the current interval in minutes if successful.
        number - If an interval is specified, the previous interval in minutes if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AutosaveInterval

        """
        delete_search_path = """
        Removes an existing path from Rhino's search path list. Search path items can be removed manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.

        Parameters
        ==========
        folder  (string, Required) - A valid folder, or path, to remove.

        Returns
        =======
        boolean - True or False indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteSearchPath

        """
        enable_autosave = """
        Enables or disables Rhino's automatic file saving mechanism.

        Parameters
        ==========
        enable  (boolean, Optional) - The autosave state.  If omitted, automatic saving is enabled (True).

        Returns
        =======
        boolean - The previous autosave state.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: EnableAutosave

        """
        exe_folder = """
        Returns the full path to Rhino's executable folder.

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - Rhino's executable folder if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExeFolder

        """
        find_file = """
        Searches for a file using Rhino's search path. Rhino will look for a file in the following locations:
		1. The current document's folder.
		2. Folder's specified in Options dialog, File tab.
		3. Rhino's System folders.

        Parameters
        ==========
        filename  (string, Required) - A valid filename.

        Returns
        =======
        string - A qualified path to the specified filename if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: FindFile

        """
        install_folder = """
        Returns the full path to Rhino's installation folder.

        Parameters
        ==========
        No parameters

        Returns
        =======
        string - Rhino's installation folder if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: InstallFolder

        """
        search_path_count = """
        Returns the number of path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

        Parameters
        ==========
        No parameters

        Returns
        =======
        number - The number of path items in Rhino's search path list.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SearchPathCount

        """
        search_path_list = """
        Returns all of the path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

        Parameters
        ==========
        No parameters

        Returns
        =======
        list - A list of strings containing all of the path items in Rhino's search path list.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: SearchPathList

        """
        template_file = """
        Returns or sets Rhino's default template file. The default template file is the template file used when Rhino starts.

        Parameters
        ==========
        filename  (string, Optional) - The name of the new default template file. Note, the template file must exist.

        Returns
        =======
        string - If filename is not specified, then the current default template file if successful.
        string - If filename is specified, then the previous default template file if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TemplateFile

        """
        template_folder = """
        Returns or sets the location of Rhino's template files.

        Parameters
        ==========
        folder  (string, Optional) - The location of Rhino's template files. Note, the location, or folder, must exist.

        Returns
        =======
        string - If folder is not specified, then the current template file folder if successful.
        string - If folder is specified, then the previous template file folder if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: TemplateFolder

        """
        working_folder = """
        Returns or sets Rhino's working directory, or folder.  The working folder is the default folder for all file operations.

        Parameters
        ==========
        enable  (boolean, Optional) - The new working folder.

        Returns
        =======
        string - If strFolder is not specified, then the current working folder if successful.
        string - If strFolder is specified, then the previous working folder if successful.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: WorkingFolder

        """


class scripts():

        add_startup_script = """
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
        delete_startup_script = """
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
        get_plug_in_object = """
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
        last_loaded_script_file = """
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
        plug_ins = """
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
        startup_script_count = """
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
        startup_script_list = """
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


class settings():

        appearance_color = """
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
        appearance_display = """
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
        display_ole_alerts = """
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
        edge_analysis_color = """
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
        edge_analysis_mode = """
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
        enable_history_recording = """
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
        ortho = """
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
        osnap = """
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
        osnap_dialog = """
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
        osnap_mode = """
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
        planar = """
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
        project_osnaps = """
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
        snap = """
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


class status_bar():

        status_bar_distance = """
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
        status_bar_message = """
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
        status_bar_number = """
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
        status_bar_point = """
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
