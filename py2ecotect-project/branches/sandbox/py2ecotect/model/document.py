import py2ecotect as p2e

#===========================================================================
# Functions
#===========================================================================
def dump(filename):
    """
    
    Use the dump command to save a snapshot copy of the current model to the 
    specified filename and location, without changing the stored filename or 
    marking the model as having been recently saved. This command can be 
    useful when performing a large number of parametric calculations and 
    wish to generate several interim results files without all the 
    information usually associated with a model.saveas command. As a 
    comparison, the model.saveas command saves the model with the new 
    filename, copies its adjacency and shading table files, then updates the 
    stored model filename and the main window caption. 

    Parameter(s)

    filename 
    Specifies the filename to use for the dump; however, be aware of the 
    issues with backslashes in filename parameters. It is generally good 
    practice to specify a directory location in addition to the filename, or 
    the export file will be saved to current model directory by default. 
    
    Here is an example:
    
    >>> dump("C:\\Test\\mytest.eco")
    
    """
    arg_str = p2e._base._util._convert_args_to_string("model.dump", filename)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def export_file(filename, fileformat):
    """
    
    Use this command to export the current model data to the a file. A 
    suffix component can be used to specify the file format, as given in the 
    following table. By default, the file(s) will be saved to the disk. 
    However, for some of the formats marked with [run.], if you insert the 
    prefix run. in front of the file type token, ECOTECT will automatically 
    invoke the last action for the export and actually run the associated 
    application to process the exported file. For example, the examples 
    given below show exports to Radiance. With the model.export.run.rad 
    command, Radiance will be involked to actually generate the images 
    defined within the exported Radiance file. 
       
    Parameter(s)

    filename 
    Specifies the filename to use for the export. However, be aware of the 
    issues with backslashes in filename parameters. It is generally good 
    practice to specify a directory location in addition to the filename, 
    or the export file will be saved to current model directory by default.
    
    Extension Read Write Format 
    mod yes yes ASCII Model File 
    rad yes yes RADIANCE Scene File 
    oct no yes RADIANCE Octree 
    pov no yes POV-Ray Scene File 
    wrl yes yes VRML 2.0 FIle 
    dxf yes yes AutoCAD DXF File 
    htb no yes HTB2 Model File 
    nat no yes NatHERS Model File 
    esp no yes ESP-r Model File 
    ray yes yes Binary Acoustic Rays File 
    grd yes yes Binary Analysis Grid File 
    cfd no yes NIST FDS CFD Model File 
    air no yes WinAir 4 CFD Model File 
    wmf no yes Windows Metafile Image File 
    bmp yes yes Windows Bitmap Image File 
    jpg yes yes JPEG Image File 
    gif yes yes GIF Image File 
    scr yes no ECOTECT Script File 
    csv yes yes Comma Separated Value (CSV) File 
    asc yes yes ASCII Text File 
    dat yes yes RADIANCE Point Data File 
    chm no no Microsoft Compiled Help File 
    msk yes yes Shanding Mask File 
    idf yes yes EnergyPlus Input File 
    eio yes no EnergyPlus Summary File 
    eso yes no EnergyPlus Binary Output 
    txt yes yes ASCII Text File 
    
    Here is an example:
    
    >>> export_file("D:\\Temp\\mytest.dxf", ".dxf")
    
    """

    arg_str = p2e._base._util._convert_args_to_string("model.export" + fileformat, filename)
    p2e._app.Exec(arg_str)

def import_file(filename):
    """
    
    Use this command to import data in into the current model. A suffix 
    component can be used to specify the the file format from the following 
    table.
    
    The Ecotect version of this command is:
    model.import

    Parameter(s)

    filename 
    Specifies the filename to use for the import. However, be aware of the 
    issues with backslashes in filename parameters. It is generally good 
    practice to specify a directory location in addition to the filename, or 
    the import file will be saved to current model directory by default.
    
    Extension Read Write Format 
    mod yes yes ASCII Model File 
    rad yes yes RADIANCE Scene File 
    oct no yes RADIANCE Octree 
    pov no yes POV-Ray Scene File 
    wrl yes yes VRML 2.0 FIle 
    dxf yes yes AutoCAD DXF File 
    htb no yes HTB2 Model File 
    nat no yes NatHERS Model File 
    esp no yes ESP-r Model File 
    ray yes yes Binary Acoustic Rays File 
    grd yes yes Binary Analysis Grid File 
    cfd no yes NIST FDS CFD Model File 
    air no yes WinAir 4 CFD Model File 
    wmf no yes Windows Metafile Image File 
    bmp yes yes Windows Bitmap Image File 
    jpg yes yes JPEG Image File 
    gif yes yes GIF Image File 
    scr yes no ECOTECT Script File 
    csv yes yes Comma Separated Value (CSV) File 
    asc yes yes ASCII Text File 
    dat yes yes RADIANCE Point Data File 
    chm no no Microsoft Compiled Help File 
    msk yes yes Shanding Mask File 
    idf yes yes EnergyPlus Input File 
    eio yes no EnergyPlus Summary File 
    eso yes no EnergyPlus Binary Output 
    txt yes yes ASCII Text File 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("model.import", filename)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def open(filename):
    """
    
    Loads the specified file as the current model. 

    Parameter(s)

    filename 
    Specifies the name of the ECOTECT file to load. In most cases you will 
    need to specify the full pathname of the file to be loaded, as the 
    directory in which the model file resides will become the current
    directory in which the application will work. An example may be:

    filename =  C:\Temp\Test.eco
    
    """
    arg_str = p2e._base._util._convert_args_to_string("model.load", filename)
    p2e._app.Exec(arg_str)
    
    #Clear model lists
    p2e.doc._zones = []
    p2e.doc._objects = []
    p2e.doc._nodes = []
    
    #Update the lists
    p2e.model._populate()     

def new():
    """   
    
    Clears the current model from memory and resets the material library. 
    Note: when used as part of a script, this command will not prompt you to 
    save any changes you have made to the current model. Once called, all 
    changes will be lost. 

    Parameter(s)
    There are no parameters for this command.
    
    Command in ECOTECT:
    model.new
    
    """
    p2e._app.Exec("model.new")
    
    
    #Clear model lists
    p2e.doc._zones = []
    p2e.doc._objects = []
    p2e.doc._nodes = []
    
    #Update the lists
    p2e.model._populate()     

def revert():
    """
    
    Use this command to revert to the last saved version of the current 
    model file. This can be useful where you have been running a long script 
    unattended that has made many changes to the model and do not want them 
    saved. Simply add a model.revert command at the end of the script and it 
    will reload the original. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("model.revert")
     
    #Clear model lists
    p2e.doc._zones = []
    p2e.doc._objects = []
    p2e.doc._nodes = []
    
    #Update the lists
    p2e.model._populate()     
    
def save():
    """
    
    This command simply saves the current model to disk. If the model does 
    not already have a filename, the command will fail. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("model.save")

def save_as(filename):
    """
    
    When invoked, the model.saveas command saves the model with the new 
    filename, copies its adjacency and shading table files, then updates the 
    stored model filename and the main window caption. As a comparison, the 
    model.dump command only saves a snapshot copy of the current model to 
    the specified file, without changing the stored filename or marking the 
    model as having been recently saved. 

    Parameter(s)
    This command takes the following parameters.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("model.saveas", filename)        
    p2e._app.Exec(arg_str)

#------------------------------------------------------------------------------ 
def file_name():
    """
    
    Returns the filename of the currently loaded ECOTECT model. This is 
    the filename only, with no drive or directory components. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    filename 
    A text string containing the filename. 
    
    """
    val = p2e._app.Request("get.model.filename")
    return p2e._base._util._convert_str_to_type(val, str)

def file_path():
    """
    
    Returns the full pathname of the currently loaded ECOTECT model. This 
    includes the full drive, directory and filename specification. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    pathname 
    A text string containing the full pathname.
    
    """
    return p2e._app.Request("get.model.pathname")

def file_directory():
    """
    
    Returns the drive and directory in which the currently loaded 
    ECOTECT model is located. This is essentially the full pathname, but 
    without the filename component. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    path 
    A text string containing the current directory path. 

    """
    val = p2e._app.Request("get.model.directory")
    return p2e._base._util._convert_str_to_type(val, str)

def set_file_directory(path):
    """
    
    Sets the drive and directory to use with the currently loaded 
    ECOTECT model. 

    Parameter(s)
    This property takes the following parameters.
    
    path 
    A string value that defines the directory to use. Include both the 
    drive letter and full directory path. However, be aware of the 
    issues with backslashes in filename parameters as described in the 
    ECOTECT help file.
    
    """
    args = p2e._base._util._convert_args_to_string("set.model.directory", path)
    arg_str = p2e._base._util._convert_args_to_string(args)
    p2e._app.Exec(arg_str)