# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add_alias(alias, macro):

    """
    
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
    return _base._rsf.add_alias(alias, macro)

def alias_count():

    """
    
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
    return _base._rsf.alias_count()

def alias_macro(alias, macro=pythoncom.Empty):

    """
    
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
    return _base._rsf.alias_macro(alias, macro)

def alias_names():

    """
    
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
    return _base._rsf.alias_names()

def clear_command_history():

    """
    
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
    return _base._rsf.clear_command_history()

def command(command, echo=pythoncom.Empty):

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
    return _base._rsf.command(command, echo)

def command_history():

    """
    
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
    return _base._rsf.command_history()

def delete_alias(alias):

    """
    
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
    return _base._rsf.delete_alias(alias)

def in_command(ignore_runners=pythoncom.Empty):

    """
    
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
    return _base._rsf.in_command(ignore_runners)

def is_alias(alias):

    """
    
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
    return _base._rsf.is_alias(alias)

def is_command(command_name):

    """
    
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
    return _base._rsf.is_command(command_name)

def last_command_name():

    """
    
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
    return _base._rsf.last_command_name()

def last_command_result():

    """
    
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
    return _base._rsf.last_command_result()
