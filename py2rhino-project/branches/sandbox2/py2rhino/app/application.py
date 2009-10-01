# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def build_date():

    """
    
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
    return _base._rsf.build_date()

def default_renderer(renderer=pythoncom.Empty):

    """
    
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
    return _base._rsf.default_renderer(renderer)

def exit():

    """
    
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
    return _base._rsf.exit()

def help(topic=pythoncom.Empty):

    """
    
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
    return _base._rsf.help(topic)

def locale_i_d():

    """
    
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
    return _base._rsf.locale_i_d()

def print_(message=pythoncom.Empty):

    """
    
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
    return _base._rsf.print_()

def print_ex(message=pythoncom.Empty):

    """
    
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
    return _base._rsf.print_ex()

def prompt(prompt=pythoncom.Empty):

    """
    
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
    return _base._rsf.prompt()

def registry_key():

    """
    
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
    return _base._rsf.registry_key()

def screen_size():

    """
    
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
    return _base._rsf.screen_size()

def sdk_version():

    """
    
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
    return _base._rsf.sdk_version()

def send_keystrokes(keys=pythoncom.Empty, add_return=pythoncom.Empty):

    """
    
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
    return _base._rsf.send_keystrokes()

def window_handle():

    """
    
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
    return _base._rsf.window_handle()
