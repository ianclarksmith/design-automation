# Auto-generated wrapper for Rhino4 RhinoScript functions

import pythoncom
from py2rhino import _base

def add_search_path(folder, index=pythoncom.Empty):

    """
    
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
    return _base._rsf.add_search_path(folder, index)

def autosave_file(file=pythoncom.Empty):

    """
    
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
    return _base._rsf.autosave_file(file)

def autosave_interval(minutes=pythoncom.Empty):

    """
    
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
    return _base._rsf.autosave_interval(minutes)

def delete_search_path(folder):

    """
    
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
    return _base._rsf.delete_search_path(folder)

def enable_autosave(enable=pythoncom.Empty):

    """
    
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
    return _base._rsf.enable_autosave(enable)

def exe_folder():

    """
    
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
    return _base._rsf.exe_folder()

def find_file(filename):

    """
    
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
    return _base._rsf.find_file(filename)

def install_folder():

    """
    
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
    return _base._rsf.install_folder()

def search_path_count():

    """
    
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
    return _base._rsf.search_path_count()

def search_path_list():

    """
    
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
    return _base._rsf.search_path_list()

def template_file(filename=pythoncom.Empty):

    """
    
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
    return _base._rsf.template_file(filename)

def template_folder(folder=pythoncom.Empty):

    """
    
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
    return _base._rsf.template_folder(folder)

def working_folder(enable=pythoncom.Empty):

    """
    
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
    return _base._rsf.working_folder(enable)
