# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
import exceptions
class Application(DispatchBaseClass):



    def add_alias(self, alias, macro):
        """

        Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.

        Parameters

        Alias : Required, String, str
        Macro : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(709, 1, (12, 0), ((12, 0), (12, 0)), u'AddAlias', None, alias, macro)

    def add_search_path(self, folder, index):
        """

        Adds a new path to Rhino's search path list. Search path items can be added manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.

        Parameters

        Folder : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The zero-based index of the new search path item. If the index is less than zero, then the path item was not added to the search path list.
        Null : On error.

        """

        return self._ApplyTypes_(511, 1, (12, 0), ((12, 0), (12, 0)), u'AddSearchPath', None, folder, index)

    def add_startup_script(self, script_file, index):
        """

        Adds a new startup script to RhinoScript's startup script list. Startup script  items can be added manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.

        Parameters

        ScriptFile : Required, String, str
        Index : Optional, Number, int

        Returns

        Number : The zero-based index of the new startup script item. If the index is less than zero, then the path item was not added to the search path list.
        Null : On error.

        """

        return self._ApplyTypes_(714, 1, (12, 0), ((12, 0), (12, 0)), u'AddStartupScript', None, script_file, index)

    def alias_count(self):
        """

        Returns the number of command alias in Rhino.

        No parameters

        Returns

        Number : True or False indicating success or failure.

        """

        return self._ApplyTypes_(706, 1, (12, 0), (), u'AliasCount', None, )

    def alias_macro(self, alias, macro):
        """

        Returns or modifies the macro of a command alias.

        Parameters

        Alias : Required, String, str
        Macro : Optional, String, str

        Returns

        String : If a new macro is not specified,  the existing macro if successful.
        String : If a new macro is specified, the previous macro if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(708, 1, (12, 0), ((12, 0), (12, 0)), u'AliasMacro', None, alias, macro)

    def alias_names(self):
        """

        Returns a list of command alias names.

        No parameters

        Returns

        Array : An array of string identifying the command alias names.

        """

        return self._ApplyTypes_(707, 1, (12, 0), (), u'AliasNames', None, )

    def appearance_color(self, item, color):
        """

        Returns or modifies an application interface item's color.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        Item : Required, Number, int
        Color : Optional, Number, lng

        Returns

        Number : If a lngColor is not specified, the current item color if successful.
        Number : If a lngColor is specified, the previous item color if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(335, 1, (12, 0), ((12, 0), (12, 0)), u'AppearanceColor', None, item, color)

    def appearance_display(self, item, show):
        """

        Returns or modifies an application interface item's visibility.

        Parameters

        Item : Required, Number, int
        Show : Optional, Boolean, bln

        Returns

        Number : If a blnShow is not specified, the current visibility state if successful.
        Number : If a blnShow is specified, the visibility state if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(752, 1, (12, 0), ((12, 0), (12, 0)), u'AppearanceDisplay', None, item, show)

    def autosave_file(self, file):
        """

        Returns or changes the file name used by Rhino's automatic file saving mechanism.

        Parameters

        File : Optional, String, str

        Returns

        String : If an autosave file is not specified, the name of the current autosave file if successful.
        String : If an autosave file is specified, the name of the previous autosave file if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(428, 1, (12, 0), ((12, 0)), u'AutosaveFile', None, file)

    def autosave_interval(self, minutes):
        """

        Returns or changes how often the document will be saved when Rhino's automatic file saving mechanism is enabled.

        Parameters

        Minutes : Optional, Number, int

        Returns

        Number : If an interval is not specified, the current interval in minutes if successful.
        Number : If an interval is specified, the previous interval in minutes if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(429, 1, (12, 0), ((12, 0)), u'AutosaveInterval', None, minutes)

    def build_date(self):
        """

        Returns the build date of Rhino.  The build date is a number in the form of YYYYMMDD.

        No parameters

        Returns

        Number : The build date of Rhino if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(360, 1, (12, 0), (), u'BuildDate', None, )

    def clear_command_history(self):
        """

        Clears the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.

        No parameters

        No returns


        """

        return self._ApplyTypes_(592, 1, (12, 0), (), u'ClearCommandHistory', None, )

    def command(self, command, echo):
        """

        After the command script has run, you can obtain the identifiers of most recently created or changed object by calling LastCreatedObjects.

        Parameters

        Command : Required, String, str
        Echo : Optional, Boolean, bln

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(1, 1, (12, 0), ((12, 0), (12, 0)), u'Command', None, command, echo)

    def command_history(self):
        """

        Returns the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.

        No parameters

        Returns

        String : A string containing the contents of Rhino's command history window if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(591, 1, (12, 0), (), u'CommandHistory', None, )

    def default_renderer(self, renderer):
        """

        Returns or changes Rhino's current, or default, render plug-in.  Use the PlugIns method to get a list of available render plug-ins.

        Parameters

        Renderer : Optional, String, str

        Returns

        String : If a render plug-in is not specified, the name of the current render plug-in if successful.
        String : If a render plug-in is specified, the name of the previous current render plug-in if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(316, 1, (12, 0), ((12, 0)), u'DefaultRenderer', None, renderer)

    def delete_alias(self, alias):
        """

        Deletes an existing command alias from Rhino.

        Parameters

        Alias : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(710, 1, (12, 0), ((12, 0)), u'DeleteAlias', None, alias)

    def delete_search_path(self, folder):
        """

        Removes an existing path from Rhino's search path list. Search path items can be removed manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.

        Parameters

        Folder : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(512, 1, (12, 0), ((12, 0)), u'DeleteSearchPath', None, folder)

    def delete_startup_script(self, script_file):
        """

        Removes an existing startup script from RhinoScript's startup script list. Startup script items can be removed manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.

        Parameters

        ScriptFile : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : On error.

        """

        return self._ApplyTypes_(715, 1, (12, 0), ((12, 0)), u'DeleteStartupScript', None, script_file)

    def display_ole_alerts(self, display):
        """

        Note, the display of OLE Server Busy/Not Responding dialog boxes will be re-enabled whenever the script engine is reset, either by running the ResetRhinoScript command or by having the Reinitialize option enabled in Tools->Options->RhinoScript.

        Parameters

        Display : Required, Boolean, bln

        Returns

        Null : If successful or on error.

        """

        return self._ApplyTypes_(896, 1, (12, 0), ((12, 0)), u'DisplayOleAlerts', None, display)

    def edge_analysis_color(self, color):
        """

        Returns or modifies edge analysis color displayed by the ShowEdges command.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

        Parameters

        Color : Optional, Number, lng

        Returns

        Number : If a lngColor is not specified, the current edge analysis color if successful.
        Number : If a lngColor is specified, the previous edge analysis color if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(449, 1, (12, 0), ((12, 0)), u'EdgeAnalysisColor', None, color)

    def edge_analysis_mode(self, mode):
        """

        Returns or modifies edge analysis mode displayed by the ShowEdges command.

        Parameters

        Mode : Optional, Number, int

        Returns

        Number : If a intMode is not specified, the current edge analysis display mode if successful.
        Number : If a intMode is specified, the previous edge analysis display mode if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(448, 1, (12, 0), ((12, 0)), u'EdgeAnalysisMode', None, mode)

    def enable_autosave(self, enable):
        """

        Enables or disables Rhino's automatic file saving mechanism.

        Parameters

        Enable : Optional, Boolean, bln

        Returns

        Boolean : The previous autosave state.

        """

        return self._ApplyTypes_(430, 1, (12, 0), ((12, 0)), u'EnableAutosave', None, enable)

    def enable_history_recording(self, enable):
        """

        Enables or disables Rhino's command history recording. For more information, see the Rhino help file for the History command.

        Parameters

        Enable : Optional, Boolean, bln

        Returns

        Boolean : If bEnable is not specified, then the current history recording state.
        Boolean : If bEnable is specified, then the previous history recording state.

        """

        return self._ApplyTypes_(735, 1, (12, 0), ((12, 0)), u'EnableHistoryRecording', None, enable)

    def exe_folder(self):
        """

        Returns the full path to Rhino's executable folder.

        No parameters

        Returns

        String : Rhino's executable folder if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(21, 1, (12, 0), (), u'ExeFolder', None, )

    def exit(self):
        """

        Closes the Rhino application.

        No parameters

        No returns


        """

        return self._ApplyTypes_(537, 1, (12, 0), (), u'Exit', None, )

    def find_file(self, filename):
        """

        3. Rhino's System folders.

        Parameters

        Filename : Required, String, str

        Returns

        String : A qualified path to the specified filename if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(81, 1, (12, 0), ((12, 0)), u'FindFile', None, filename)

    def get_plug_in_object(self, plug_in):
        """

        Returns a scriptable object from a specified plug-in. Note, not all plug-ins contain scriptable objects. Check with the manufacturer of your plug-in to see if they support this capability.

        Parameters

        PlugIn : Required, String, str

        Returns

        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(636, 1, (12, 0), ((12, 0)), u'GetPlugInObject', None, plug_in)

    def help(self, topic):
        """

        Displays a topic in Rhino's Help file.

        Parameters

        Topic : Optional, Number, int

        Returns

        Boolean : True or False indicating success or failure.

        """

        return self._ApplyTypes_(22, 1, (12, 0), ((12, 0)), u'Help', None, topic)

    def in_command(self, ignore_runners):
        """

        Determines if Rhino is currently running a command. Because Rhino allow for transparent commands (commands that can be run from inside of other commands), this method returns the total number of active commands.

        Parameters

        IgnoreRunners : Optional, Boolean, bln

        Returns

        Number : The number of active commands.

        """

        return self._ApplyTypes_(596, 1, (12, 0), ((12, 0)), u'InCommand', None, ignore_runners)

    def install_folder(self):
        """

        Returns the full path to Rhino's installation folder.

        No parameters

        Returns

        String : Rhino's installation folder if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(23, 1, (12, 0), (), u'InstallFolder', None, )

    def is_alias(self, alias):
        """

        Verifies that a command alias exists in Rhino.

        Parameters

        Alias : Required, String, str

        Returns

        Boolean : True or False indicating success or failure.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(711, 1, (12, 0), ((12, 0)), u'IsAlias', None, alias)

    def is_command(self, command_name):
        """

        Verifies that a command exists in Rhino. The function is useful when scripting commands found in 3rd party plug-ins.

        Parameters

        CommandName : Required, String, str

        Returns

        Boolean : True if successful, otherwise False.
        Null : On error.

        """

        return self._ApplyTypes_(530, 1, (12, 0), ((12, 0)), u'IsCommand', None, command_name)

    def last_command_name(self):
        """

        Returns the name of the last executed command.

        No parameters

        Returns

        String : The name of the last executed command.

        """

        return self._ApplyTypes_(594, 1, (12, 0), (), u'LastCommandName', None, )

    def last_command_result(self):
        """

        Returns the result code for the last executed command.

        No parameters

        Returns

        Number : The result code successful.  The result codes are as follows:

        """

        return self._ApplyTypes_(292, 1, (12, 0), (), u'LastCommandResult', None, )

    def last_loaded_script_file(self):
        """

        Return the full path to the last RhinoScript file that was loaded using the LoadScript command..

        No parameters

        Returns

        String : The last loaded script file if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(373, 1, (12, 0), (), u'LastLoadedScriptFile', None, )

    def locale_i_d(self):
        """

        Returns the language used for the Rhino interface.  The current language is returned as a locale ID, or LCID, value.

        No parameters

        Returns

        Number : Rhino's current locale ID, or LCID.  The languages currently supported by Rhino are as follows:

        """

        return self._ApplyTypes_(450, 1, (12, 0), (), u'LocaleID', None, )

    def ortho(self, enable):
        """

        Enables or disables Rhino's ortho modeling aid.

        Parameters

        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current ortho status if successful.
        Boolean : If blnEnable is specified, then the previous ortho status if successful.

        """

        return self._ApplyTypes_(345, 1, (12, 0), ((12, 0)), u'Ortho', None, enable)

    def osnap(self, enable):
        """

        Enables or disables Rhino's object snap modeling aid.  Object snaps are tools for specifying points on existing objects.

        Parameters

        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current object snap status if successful.
        Boolean : If blnEnable is specified, then the previous object snap status if successful.

        """

        return self._ApplyTypes_(347, 1, (12, 0), ((12, 0)), u'Osnap', None, enable)

    def osnap_dialog(self, visible):
        """

        Shows or hides Rhino's dockable object snap bar.

        Parameters

        Visible : Optional, Boolean, bln

        Returns

        Boolean : If blnVisible is not specified, then the current visibility state if successful.
        Boolean : If blnVisible is specified, then the previous visibility state if successful.

        """

        return self._ApplyTypes_(349, 1, (12, 0), ((12, 0)), u'OsnapDialog', None, visible)

    def osnap_mode(self, mode):
        """

        Returns or sets the object snap mode. Object snaps are tools for specifying points on existing objects.

        Parameters

        Mode : Optional, Number, int

        Returns

        Number : If intMode is not specified, then the current object snap mode or modes if successful.
        Number : If intMode is specified, then the previous object snap mode or modes if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(343, 1, (12, 0), ((12, 0)), u'OsnapMode', None, mode)

    def planar(self, enable):
        """

        Enables or disables Rhino's planar modeling aid.

        Parameters

        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current planar status if successful.
        Boolean : If blnEnable is specified, then the previous planar status if successful.

        """

        return self._ApplyTypes_(346, 1, (12, 0), ((12, 0)), u'Planar', None, enable)

    def plug_ins(self, types, status):
        """

        Returns an array of registered Rhino plug-ins.

        Parameters

        Types : Optional, Number, int
        Status : Optional, Number, int

        Returns

        Array : An array of strings describing the plug-ins if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(315, 1, (12, 0), ((12, 0), (12, 0)), u'PlugIns', None, types, status)

    def print_rh(self, message):
        """

        Prints a string to Rhino's command window.  Note, this method cannot be called from Visual Basic.  If you are using Visual Basic, use the PrintEx method.

        Parameters

        Message : Optional, String, str

        No returns


        """

        return self._ApplyTypes_(2, 1, (12, 0), ((12, 0)), u'Print', None, message)

    def print_ex(self, message):
        """

        Prints a string to Rhino's command window.  Use this method, instead of the Print method, if you are using Visual Basic.

        Parameters

        Message : Optional, String, str

        No returns


        """

        return self._ApplyTypes_(370, 1, (12, 0), ((12, 0)), u'PrintEx', None, message)

    def project_osnaps(self, enable):
        """

        Enables or disables object snap projection.

        Parameters

        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current object snap projection status if successful.
        Boolean : If blnEnable is specified, then the previous object snap projection status if successful.

        """

        return self._ApplyTypes_(348, 1, (12, 0), ((12, 0)), u'ProjectOsnaps', None, enable)

    def prompt(self, prompt):
        """

        Changes Rhino's command window prompt.

        Parameters

        Prompt : Optional, String, str

        No returns


        """

        return self._ApplyTypes_(24, 1, (12, 0), ((12, 0)), u'Prompt', None, prompt)

    def registry_key(self):
        """

        Returns Rhino's Windows Registry key.

        No parameters

        Returns

        String : Rhino's Windows Registry key if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(25, 1, (12, 0), (), u'RegistryKey', None, )

    def screen_size(self):
        """

        Returns the current width and height, in pixels, of the screen of the primary display monitor.

        No parameters

        Returns

        Array : A zero-based, one-dimensional array containing two numbers identifying the width and height if successful
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(553, 1, (12, 0), (), u'ScreenSize', None, )

    def sdk_version(self):
        """

        Returns the version of the Rhino SDK supported by the running version of Rhino.  Rhino SDK versions are 9 digit numbers in the form of YYYYMMDDn.

        No parameters

        Returns

        Number : The supported Rhino SDK version number if successful.
        Null : If not successful, or on error.

        """

        return self._ApplyTypes_(359, 1, (12, 0), (), u'SdkVersion', None, )

    def search_path_count(self):
        """

        Returns the number of path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

        No parameters

        Returns

        Number : The number of path items in Rhino's search path list.

        """

        return self._ApplyTypes_(509, 1, (12, 0), (), u'SearchPathCount', None, )

    def search_path_list(self):
        """

        Returns all of the path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

        No parameters

        Returns

        Array : An array of strings containing all of the path items in Rhino's search path list.

        """

        return self._ApplyTypes_(510, 1, (12, 0), (), u'SearchPathList', None, )

    def send_keystrokes(self, keys, add_return):
        """

        Sends a string of printable characters, including spaces, to Rhino's command line.

        Parameters

        Keys : Optional, String, str
        AddReturn : Optional, String, bln

        No returns


        """

        return self._ApplyTypes_(496, 1, (12, 0), ((12, 0), (12, 0)), u'SendKeystrokes', None, keys, add_return)

    def snap(self, enable):
        """

        Enables or disables Rhino's grid snap modeling aid.

        Parameters

        Enable : Optional, Boolean, bln

        Returns

        Boolean : If blnEnable is not specified, then the current grid snap status if successful.
        Boolean : If blnEnable is specified, then the previous grid snap status if successful.

        """

        return self._ApplyTypes_(344, 1, (12, 0), ((12, 0)), u'Snap', None, enable)

    def startup_script_count(self):
        """

        Returns the number of startup script items in RhinoScript's startup script list. See "Options RhinoScript" for more details.

        No parameters

        Returns

        Number : The number of path items in Rhino's startup script list.

        """

        return self._ApplyTypes_(712, 1, (12, 0), (), u'StartupScriptCount', None, )

    def startup_script_list(self):
        """

        Returns all of the startup script items in Rhino's startup script list. See "Options RhinoScript" for more details.

        No parameters

        Returns

        Array : An array of strings containing all of the startup script items in RhinoScript's startup script list.

        """

        return self._ApplyTypes_(713, 1, (12, 0), (), u'StartupScriptList', None, )

    def status_bar_distance(self, distance):
        """

        Sets Rhino's status bar distance pane.

        Parameters

        Distance : Optional, Number, dbl

        No returns


        """

        return self._ApplyTypes_(26, 1, (12, 0), ((12, 0)), u'StatusBarDistance', None, distance)

    def status_bar_message(self, message):
        """

        Sets Rhino's status bar message pane.

        Parameters

        Message : Optional, String, str

        No returns


        """

        return self._ApplyTypes_(28, 1, (12, 0), ((12, 0)), u'StatusBarMessage', None, message)

    def status_bar_number(self, number):
        """

        Sets Rhino's status bar number pane.

        Parameters

        Number : Optional, Number, dbl

        No returns


        """

        return self._ApplyTypes_(312, 1, (12, 0), ((12, 0)), u'StatusBarNumber', None, number)

    def status_bar_point(self, point):
        """

        Sets Rhino's status bar point coordinate panes.

        Parameters

        Point : Optional, Array, arr

        No returns


        """

        return self._ApplyTypes_(27, 1, (12, 0), ((12, 0)), u'StatusBarPoint', None, point)

    def template_file(self, filename):
        """

        Returns or sets Rhino's default template file. The default template file is the template file used when Rhino starts.

        Parameters

        Filename : Optional, String, str

        Returns

        String : If strFilename is not specified, then the current default template file if successful.
        String : If strFilename is specified, then the previous default template file if successful.

        """

        return self._ApplyTypes_(529, 1, (12, 0), ((12, 0)), u'TemplateFile', None, filename)

    def template_folder(self, folder):
        """

        Returns or sets the location of Rhino's template files.

        Parameters

        Folder : Optional, String, str

        Returns

        String : If strFolder is not specified, then the current template file folder if successful.
        String : If strFolder is specified, then the previous template file folder if successful.

        """

        return self._ApplyTypes_(528, 1, (12, 0), ((12, 0)), u'TemplateFolder', None, folder)

    def window_handle(self):
        """

        Returns the Windows handle of Rhino's main window.

        No parameters

        Returns

        Number : Rhino's main window handle.

        """

        return self._ApplyTypes_(29, 1, (12, 0), (), u'WindowHandle', None, )

    def working_folder(self, enable):
        """

        Returns or sets Rhino's working directory, or folder.  The working folder is the default folder for all file operations.

        Parameters

        Enable : Optional, String, bln

        Returns

        String : If strFolder is not specified, then the current working folder if successful.
        String : If strFolder is specified, then the previous working folder if successful.

        """

        return self._ApplyTypes_(439, 1, (12, 0), ((12, 0)), u'WorkingFolder', None, enable)

