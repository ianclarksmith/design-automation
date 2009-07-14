# Auto-generated wrapper for Rhino4 RhinoScript functions
import win32com.client.CLSIDToClass, pythoncom
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from win32com.client import DispatchBaseClass
class Application(DispatchBaseClass):



	def InstallFolder(self):
		"""

		Returns the full path to Rhino's installation folder.

		No parameters

		Returns

		String : Rhino's installation folder if successful.
		Null : If not successful, or on error.

		"""

		pass

	def Osnap(self, blnEnable):
		"""

		Enables or disables Rhino's object snap modeling aid.  Object snaps are tools for specifying points on existing objects.

		Parameters

		blnEnable : Optional,   Boolean,   The new enabled status, either True or False

		Returns

		Boolean : If blnEnable is not specified, then the current object snap status if successful.
		Boolean : If blnEnable is specified, then the previous object snap status if successful.

		"""

		pass

	def LocaleID(self):
		"""

		Returns the language used for the Rhino interface.  The current language is returned as a locale ID, or LCID, value.

		No parameters

		Returns

		Number : Rhino's current locale ID, or LCID.  The languages currently supported by Rhino are as follows:

		"""

		pass

	def StatusBarPoint(self, arrPoint):
		"""

		Sets Rhino's status bar point coordinate panes.

		Parameters

		arrPoint : Optional,   Array,   A 3-D point

		No returns


		"""

		pass

	def OsnapDialog(self, blnVisible):
		"""

		Shows or hides Rhino's dockable object snap bar.

		Parameters

		blnVisible : Optional,   Boolean,   The new visibility state, either True or False

		Returns

		Boolean : If blnVisible is not specified, then the current visibility state if successful.
		Boolean : If blnVisible is specified, then the previous visibility state if successful.

		"""

		pass

	def LastCommandName(self):
		"""

		Returns the name of the last executed command.

		No parameters

		Returns

		String : The name of the last executed command.

		"""

		pass

	def StatusBarDistance(self, dblDistance):
		"""

		Sets Rhino's status bar distance pane.

		Parameters

		dblDistance : Optional,   Number,   The distance to display

		No returns


		"""

		pass

	def AliasCount(self):
		"""

		Returns the number of command alias in Rhino.

		No parameters

		Returns

		Number : True or False indicating success or failure.

		"""

		pass

	def SdkVersion(self):
		"""

		Returns the version of the Rhino SDK supported by the running version of Rhino.  Rhino SDK versions are 9 digit numbers in the form of YYYYMMDDn.

		No parameters

		Returns

		Number : The supported Rhino SDK version number if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AliasNames(self):
		"""

		Returns a list of command alias names.

		No parameters

		Returns

		Array : An array of string identifying the command alias names.

		"""

		pass

	def Snap(self, blnEnable):
		"""

		Enables or disables Rhino's grid snap modeling aid.

		Parameters

		blnEnable : Optional,   Boolean,   The new enabled status, either True or False

		Returns

		Boolean : If blnEnable is not specified, then the current grid snap status if successful.
		Boolean : If blnEnable is specified, then the previous grid snap status if successful.

		"""

		pass

	def Exit(self):
		"""

		Closes the Rhino application.

		No parameters

		No returns


		"""

		pass

	def ScreenSize(self):
		"""

		Returns the current width and height, in pixels, of the screen of the primary display monitor.

		No parameters

		Returns

		Array : A zero-based, one-dimensional array containing two numbers identifying the width and height if successful
		Null : If not successful, or on error.

		"""

		pass

	def Print(self, strMessage):
		"""

		Prints a string to Rhino's command window.  Note, this method cannot be called from Visual Basic.  If you are using Visual Basic, use the PrintEx method.

		Parameters

		strMessage : Optional,   String,   A prompt, message, or value

		No returns


		"""

		pass

	def LastCommandResult(self):
		"""

		Returns the result code for the last executed command.

		No parameters

		Returns

		Number : The result code successful.  The result codes are as follows:

		"""

		pass

	def GetPlugInObject(self, strPlugIn):
		"""

		Returns a scriptable object from a specified plug-in. Note, not all plug-ins contain scriptable objects. Check with the manufacturer of your plug-in to see if they support this capability.

		Parameters

		strPlugIn : Required,   String,   The name of a registered plug-in that supports scripting

		Returns

		Null : If not successful, or on error.

		"""

		pass

	def AutosaveInterval(self, intMinutes):
		"""

		Returns or changes how often the document will be saved when Rhino's automatic file saving mechanism is enabled.

		Parameters

		intMinutes : Optional,   Number,   The number of minutes between saves

		Returns

		Number : If an interval is not specified, the current interval in minutes if successful.
		Number : If an interval is specified, the previous interval in minutes if successful.
		Null : If not successful, or on error.

		"""

		pass

	def EnableHistoryRecording(self, blnEnable):
		"""

		Enables or disables Rhino's command history recording. For more information, see the Rhino help file for the History command.

		Parameters

		blnEnable : Optional,  Boolean,  The history recording state to set

		Returns

		Boolean : If bEnable is not specified, then the current history recording state.
		Boolean : If bEnable is specified, then the previous history recording state.

		"""

		pass

	def FindFile(self, strFilename):
		"""

		3. Rhino's System folders.

		Parameters

		strFilename : Required,   String,   A valid filename

		Returns

		String : A qualified path to the specified filename if successful.
		Null : If not successful, or on error.

		"""

		pass

	def IsCommand(self, strCommandName):
		"""

		Verifies that a command exists in Rhino. The function is useful when scripting commands found in 3rd party plug-ins.

		Parameters

		strCommandName : Required,   String,   The command name to test

		Returns

		Boolean : True if successful, otherwise False.
		Null : On error.

		"""

		pass

	def BuildDate(self):
		"""

		Returns the build date of Rhino.  The build date is a number in the form of YYYYMMDD.

		No parameters

		Returns

		Number : The build date of Rhino if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteAlias(self, strAlias):
		"""

		Deletes an existing command alias from Rhino.

		Parameters

		strAlias : Required,   String,   The name of an existing command alias

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def AutosaveFile(self, strFile):
		"""

		Returns or changes the file name used by Rhino's automatic file saving mechanism.

		Parameters

		strFile : Optional,   String,   The name of the new autosave file

		Returns

		String : If an autosave file is not specified, the name of the current autosave file if successful.
		String : If an autosave file is specified, the name of the previous autosave file if successful.
		Null : If not successful, or on error.

		"""

		pass

	def TemplateFolder(self, strFolder):
		"""

		Returns or sets the location of Rhino's template files.

		Parameters

		strFolder : Optional,   String,   The location of Rhino's template files

		Returns

		String : If strFolder is not specified, then the current template file folder if successful.
		String : If strFolder is specified, then the previous template file folder if successful.

		"""

		pass

	def PrintEx(self, strMessage):
		"""

		Prints a string to Rhino's command window.  Use this method, instead of the Print method, if you are using Visual Basic.

		Parameters

		strMessage : Optional,   String,   A prompt, message, or value

		No returns


		"""

		pass

	def AddSearchPath(self, strFolder, intIndex):
		"""

		Adds a new path to Rhino's search path list. Search path items can be added manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.

		Parameters

		strFolder : Required,   String,   A valid folder, or path, to add
		intIndex : Optional,   Number,   A zero-based position index in the search path list to insert the string

		Returns

		Number : The zero-based index of the new search path item. If the index is less than zero, then the path item was not added to the search path list.
		Null : On error.

		"""

		pass

	def StartupScriptCount(self):
		"""

		Returns the number of startup script items in RhinoScript's startup script list. See "Options RhinoScript" for more details.

		No parameters

		Returns

		Number : The number of path items in Rhino's startup script list.

		"""

		pass

	def StartupScriptList(self):
		"""

		Returns all of the startup script items in Rhino's startup script list. See "Options RhinoScript" for more details.

		No parameters

		Returns

		Array : An array of strings containing all of the startup script items in RhinoScript's startup script list.

		"""

		pass

	def RegistryKey(self):
		"""

		Returns Rhino's Windows Registry key.

		No parameters

		Returns

		String : Rhino's Windows Registry key if successful.
		Null : If not successful, or on error.

		"""

		pass

	def WindowHandle(self):
		"""

		Returns the Windows handle of Rhino's main window.

		No parameters

		Returns

		Number : Rhino's main window handle.

		"""

		pass

	def IsAlias(self, strAlias):
		"""

		Verifies that a command alias exists in Rhino.

		Parameters

		strAlias : Required,   String,   The name of an existing command alias

		Returns

		Boolean : True or False indicating success or failure.
		Null : If not successful, or on error.

		"""

		pass

	def ProjectOsnaps(self, blnEnable):
		"""

		Enables or disables object snap projection.

		Parameters

		blnEnable : Optional,   Boolean,   The new enabled status, either True or False

		Returns

		Boolean : If blnEnable is not specified, then the current object snap projection status if successful.
		Boolean : If blnEnable is specified, then the previous object snap projection status if successful.

		"""

		pass

	def PlugIns(self, intTypes, intStatus):
		"""

		Returns an array of registered Rhino plug-ins.

		Parameters

		intTypes : Optional,   Number,  The type or types of plug-ins to return
		intStatus : Optional,   Number,   The status, either loaded or unloaded, of the plug-ins to return

		Returns

		Array : An array of strings describing the plug-ins if successful.
		Null : If not successful, or on error.

		"""

		pass

	def EdgeAnalysisColor(self, lngColor):
		"""

		Returns or modifies edge analysis color displayed by the ShowEdges command.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

		Parameters

		lngColor : Optional,   Number,   The new color value

		Returns

		Number : If a lngColor is not specified, the current edge analysis color if successful.
		Number : If a lngColor is specified, the previous edge analysis color if successful.
		Null : If not successful, or on error.

		"""

		pass

	def LastLoadedScriptFile(self):
		"""

		Return the full path to the last RhinoScript file that was loaded using the LoadScript command..

		No parameters

		Returns

		String : The last loaded script file if successful.
		Null : If not successful, or on error.

		"""

		pass

	def DeleteSearchPath(self, strFolder):
		"""

		Removes an existing path from Rhino's search path list. Search path items can be removed manually by using Rhino's Options command and modifying the contents of the Files tab. See "Options Files settings" in the Rhino help file for more details.

		Parameters

		strFolder : Required,   String,   A valid folder, or path, to remove

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def Planar(self, blnEnable):
		"""

		Enables or disables Rhino's planar modeling aid.

		Parameters

		blnEnable : Optional,   Boolean,   The new enabled status, either True or False

		Returns

		Boolean : If blnEnable is not specified, then the current planar status if successful.
		Boolean : If blnEnable is specified, then the previous planar status if successful.

		"""

		pass

	def WorkingFolder(self, blnEnable):
		"""

		Returns or sets Rhino's working directory, or folder.  The working folder is the default folder for all file operations.

		Parameters

		blnEnable : Optional,   String,   The new working folder

		Returns

		String : If strFolder is not specified, then the current working folder if successful.
		String : If strFolder is specified, then the previous working folder if successful.

		"""

		pass

	def SearchPathCount(self):
		"""

		Returns the number of path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

		No parameters

		Returns

		Number : The number of path items in Rhino's search path list.

		"""

		pass

	def Ortho(self, blnEnable):
		"""

		Enables or disables Rhino's ortho modeling aid.

		Parameters

		blnEnable : Optional,   Boolean,   The new enabled status, either True or False

		Returns

		Boolean : If blnEnable is not specified, then the current ortho status if successful.
		Boolean : If blnEnable is specified, then the previous ortho status if successful.

		"""

		pass

	def Command(self, strCommand, blnEcho):
		"""

		After the command script has run, you can obtain the identifiers of most recently created or changed object by calling LastCreatedObjects.

		Parameters

		strCommand : Required,   String,   A Rhino command including any arguments
		blnEcho : Optional,   Boolean,  The command echo mode

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def AddStartupScript(self, strScriptFile, intIndex):
		"""

		Adds a new startup script to RhinoScript's startup script list. Startup script  items can be added manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.

		Parameters

		strScriptFile : Required,   String,   A valid path to a RhinoScript 
		intIndex : Optional,   Number,   A zero-based position index in the startup script list to insert the string

		Returns

		Number : The zero-based index of the new startup script item. If the index is less than zero, then the path item was not added to the search path list.
		Null : On error.

		"""

		pass

	def CommandHistory(self):
		"""

		Returns the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.

		No parameters

		Returns

		String : A string containing the contents of Rhino's command history window if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AppearanceDisplay(self, intItem, blnShow):
		"""

		Returns or modifies an application interface item's visibility.

		Parameters

		intItem : Required,   Number,   Item number to either query or modify
		blnShow : Optional,   Boolean,   The new visibility state, either visible (True) or hidden (False)

		Returns

		Number : If a blnShow is not specified, the current visibility state if successful.
		Number : If a blnShow is specified, the visibility state if successful.
		Null : If not successful, or on error.

		"""

		pass

	def OsnapMode(self, intMode):
		"""

		Returns or sets the object snap mode. Object snaps are tools for specifying points on existing objects.

		Parameters

		intMode : Optional,   Number,  The object snap mode or modes to set

		Returns

		Number : If intMode is not specified, then the current object snap mode or modes if successful.
		Number : If intMode is specified, then the previous object snap mode or modes if successful.
		Null : If not successful, or on error.

		"""

		pass

	def AliasMacro(self, strAlias, strMacro):
		"""

		Returns or modifies the macro of a command alias.

		Parameters

		strAlias : Required,   String,   The name of an existing command alias
		strMacro : Optional,   String,   The new macro to run when the alias is executed

		Returns

		String : If a new macro is not specified,  the existing macro if successful.
		String : If a new macro is specified, the previous macro if successful.
		Null : If not successful, or on error.

		"""

		pass

	def InCommand(self, blnIgnoreRunners):
		"""

		Determines if Rhino is currently running a command. Because Rhino allow for transparent commands (commands that can be run from inside of other commands), this method returns the total number of active commands.

		Parameters

		blnIgnoreRunners : Optional,   Boolean,   If true, script running commands, such as LoadScript, RunScript, and ReadCommandFile will not counted

		Returns

		Number : The number of active commands.

		"""

		pass

	def Prompt(self, strPrompt):
		"""

		Changes Rhino's command window prompt.

		Parameters

		strPrompt : Optional,   String,   A prompt

		No returns


		"""

		pass

	def Help(self, intTopic):
		"""

		Displays a topic in Rhino's Help file.

		Parameters

		intTopic : Optional,   Number,   A help topic

		Returns

		Boolean : True or False indicating success or failure.

		"""

		pass

	def AddAlias(self, strAlias, strMacro):
		"""

		Adds a new command alias to Rhino. Command aliases can be added manually by using Rhino's Options command and modifying the contents of the Aliases tab. See "Options Aliases" in the Rhino help file for more details.

		Parameters

		strAlias : Required,   String,   The name of the new command alias
		strMacro : Required,   String,   The macro to run when the alias is executed

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def AppearanceColor(self, intItem, lngColor):
		"""

		Returns or modifies an application interface item's color.  Colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.

		Parameters

		intItem : Required,   Number,   Item number to either query or modify
		lngColor : Optional,   Number,   The new color value

		Returns

		Number : If a lngColor is not specified, the current item color if successful.
		Number : If a lngColor is specified, the previous item color if successful.
		Null : If not successful, or on error.

		"""

		pass

	def StatusBarNumber(self, dblNumber):
		"""

		Sets Rhino's status bar number pane.

		Parameters

		dblNumber : Optional,   Number,   The number to display

		No returns


		"""

		pass

	def DefaultRenderer(self, strRenderer):
		"""

		Returns or changes Rhino's current, or default, render plug-in.  Use the PlugIns method to get a list of available render plug-ins.

		Parameters

		strRenderer : Optional,   String,   The name of a render plug-in to set as default

		Returns

		String : If a render plug-in is not specified, the name of the current render plug-in if successful.
		String : If a render plug-in is specified, the name of the previous current render plug-in if successful.
		Null : If not successful, or on error.

		"""

		pass

	def ExeFolder(self):
		"""

		Returns the full path to Rhino's executable folder.

		No parameters

		Returns

		String : Rhino's executable folder if successful.
		Null : If not successful, or on error.

		"""

		pass

	def EnableAutosave(self, blnEnable):
		"""

		Enables or disables Rhino's automatic file saving mechanism.

		Parameters

		blnEnable : Optional,  Boolean,  The autosave state

		Returns

		Boolean : The previous autosave state.

		"""

		pass

	def SendKeystrokes(self, strKeys, blnAddReturn):
		"""

		Sends a string of printable characters, including spaces, to Rhino's command line.

		Parameters

		strKeys : Optional,   String,   A string to characters to send to the command line
		blnAddReturn : Optional,   String,   Append a return character to the end of the string

		No returns


		"""

		pass

	def EdgeAnalysisMode(self, intMode):
		"""

		Returns or modifies edge analysis mode displayed by the ShowEdges command.

		Parameters

		intMode : Optional,   Number,   The new display mode

		Returns

		Number : If a intMode is not specified, the current edge analysis display mode if successful.
		Number : If a intMode is specified, the previous edge analysis display mode if successful.
		Null : If not successful, or on error.

		"""

		pass

	def StatusBarMessage(self, strMessage):
		"""

		Sets Rhino's status bar message pane.

		Parameters

		strMessage : Optional,   String,   A prompt, message, or value

		No returns


		"""

		pass

	def TemplateFile(self, strFilename):
		"""

		Returns or sets Rhino's default template file. The default template file is the template file used when Rhino starts.

		Parameters

		strFilename : Optional,   String,   The name of the new default template file

		Returns

		String : If strFilename is not specified, then the current default template file if successful.
		String : If strFilename is specified, then the previous default template file if successful.

		"""

		pass

	def SearchPathList(self):
		"""

		Returns all of the path items in Rhino's search path list. See "Options Files settings" in the Rhino help file for more details.

		No parameters

		Returns

		Array : An array of strings containing all of the path items in Rhino's search path list.

		"""

		pass

	def ClearCommandHistory(self):
		"""

		Clears the contents of Rhino's command history window. You can view the command history by using the CommandHistory command.

		No parameters

		No returns


		"""

		pass

	def DeleteStartupScript(self, strScriptFile):
		"""

		Removes an existing startup script from RhinoScript's startup script list. Startup script items can be removed manually by using Rhino's Options command and modifying the contents of the RhinoScript tab.

		Parameters

		strScriptFile : Required,   String,   An existing script file path to remove

		Returns

		Boolean : True or False indicating success or failure.
		Null : On error.

		"""

		pass

	def DisplayOleAlerts(self, blnDisplay):
		"""

		Note, the display of OLE Server Busy/Not Responding dialog boxes will be re-enabled whenever the script engine is reset, either by running the ResetRhinoScript command or by having the Reinitialize option enabled in Tools->Options->RhinoScript.

		Parameters

		blnDisplay : Required,   Boolean,   Enable or disable the display of OLE alert dialog boxes

		Returns

		Null : If successful or on error.

		"""

		pass

