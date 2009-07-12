import py2ecotect
from py2ecotect import StringUtil
         
#===============================================================================
# Private utility functions
#===============================================================================
"""
def _convert_args_to_string(*args):
    arg_str = ""
    for i in args:
        if not isinstance(i, str):
            i = str(i)
        arg_str += (i + " ")
    return arg_str

def _convert_str_to_list(string, typeFunc):
    str_list = string[:-1].split(" ")
    try:
        new_list = []
        for i_str in str_list:
            i = typeFunc(i_str)
            new_list.append(i)
        return new_list
    except:
        print "Error in type conversion: __toTypeList()"
        return None
    
def _convert_str_to_type(string, typeFunc):
    string = string[:-1]
    try:
        return typeFunc(string)
    except:
        print "Error in type conversion: __toType()"            
        return None
"""        
#================================================================================
# Commands
#================================================================================ 
    
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
    arg_str = StringUtil._convert_args_to_string("model.dump", filename)
    py2py2ecotect.conversation.Exec(arg_str)

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
    #TODO: add error checking
    arg_str = StringUtil._convert_args_to_string("model.export" + fileformat, filename)
    py2ecotect.conversation.Exec(arg_str)

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
    
    Here is an example:
    
    
    """
    arg_str = StringUtil._convert_args_to_string("model.import", filename)
    py2ecotect.conversation.Exec(arg_str)

def load(filename):
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
    arg_str = StringUtil.StringUtil._convert_args_to_string("model.load", filename)
    py2ecotect.conversation.Exec(arg_str)

def load_new():
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
    py2ecotect.conversation.Exec("model.new")

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
    py2ecotect.conversation.Exec("model.revert")

def save():
    """
    This command simply saves the current model to disk. If the model does 
    not already have a filename, the command will fail. 

    Parameter(s)
    There are no parameters for this command.
    """
    py2ecotect.conversation.Exec("model.save")

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
    arg_str = StringUtil._convert_args_to_string("model.saveas", filename)        
    py2ecotect.conversation.Exec(arg_str)
    
def update():
    """
    Use the update command to check and refresh inter-object relationships 
    within the model. Complex model with many inter-relationships can take 
    a little time to regenerate so ECOTECT doesn't do this automatically 
    after each script-based manipulation. You can also use object.update to 
    do this specific objects in the model. 
    
    Parameter(s)
    There are no parameters for this command.
    """
    py2ecotect.conversation.Exec("model.update")
#===============================================================================
# Properties
#===============================================================================

def get_altitude(x1, y1, z1, x2, y2, z2):
    """
    Retrieves geometric information from the current ECOTECT model, 
    specifically the vertical angular distance of a line starting at 
    (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
    returned is given in degrees. 

    Parameter(s)
    This property takes the following parameters.

    x1, y1, z1 
    Represents the absolute position in the X, Y and Z axis of a 
    starting point in 3 dimensional model space.
     
    x2, y2, z2 
    Represents the absolute position in the X, Y and Z axis of an end 
    point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).

    alt 
    The altitude angle in degrees. 
    """
    arg_str = StringUtil._convert_args_to_string("get.model.altitude", x1, y1, z1, x2, y2, z2)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, float)        
    
def get_azimuth(x1, y1, z1, x2, y2, z2):
    """
    Retrieves geometric information from the current ECOTECT model, 
    specifically the horizontal angular distance of a line starting at 
    (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
    returned is given in degrees. 

    Parameter(s)
    This property takes the following parameters.
    
    x1, y1, z1 
    Represents the absolute position in the X, Y and Z axis of a 
    starting point in 3 dimensional model space. 
    
    x2, y2, z2 
    Represents the absolute position in the X, Y and Z axis of an end 
    point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    azi 
    The azimuth angle in degrees.
    """
    arg_str = StringUtil._convert_args_to_string("get.model.azimuth", x1, y1, z1, x2, y2, z2)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, float)           

def get_current_node():
    """
    Returns the zero-based index of the last selected node within the 
    currently loaded ECOTECT model. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    node 
    The zero-based index of the current node. 
    """
    val = py2ecotect.conversation.Request("get.model.currentnode")
    return StringUtil._convert_str_to_type(val, int)  

def get_current_object():
    """
    Returns the zero-based index of the last selected object within the 
    currently loaded ECOTECT model. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    object 
    The zero-based index of the current object in the model. 
    """
    val = py2ecotect.conversation.Request("get.model.currentobject")
    return StringUtil._convert_str_to_type(val, int)   

def get_current_zone():
    """
    Returns the zero-based index of the current zone in the currently 
    loaded ECOTECT model. Thus, the Outside zone is always 0. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    model.currentzone 
    The zero-based index of the current zone. 
    """
    val = py2ecotect.conversation.Request("get.model.currentzone")
    return StringUtil._convert_str_to_type(val, int)   

def get_date():
    """
    Retrieves the current date as a formatted string ready for printing 
    or output to a file. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    day 
    An integer value between 1 and 31. 
    
    month 
    An integer value between 0 and 11. 
    """
    val = py2ecotect.conversation.Request("get.model.date")
    return StringUtil._convert_str_to_list(val, int)  

def set_date(day, month, time=None):
    """
    Sets the date in the ECOTECT model. 
    
    Parameter(s)
    This property takes the following parameters.
    
    day 
    An integer value between 1 and 31. 
    
    month 
    An integer value between 0 and 11. 
    
    [time] 
    An optional decimal value between 0.0 and 23.99. 
    """
    if time:
        arg_str = StringUtil._convert_args_to_string("set.model.date", day, month, time)
    else:
        arg_str = StringUtil._convert_args_to_string("set.model.date", day, month)
    py2ecotect.conversation.Exec(arg_str)
    
def get_date_string():
    """
    Retrieves a formated string containing the current model date. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    dateStr 
    A formated date string. 
    """
    val = py2ecotect.conversation.Request("get.model.datestring")
    return StringUtil._convert_str_to_type(val, str)
            
def get_daylight_savings():
    """
    Retrieves the status of the daylight savings flag. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    The daylight savings setting given as a boolean value where 1 
    represents the affirmative and 0 the negative. When true, the 
    current time is offset by one hour. 
    """
    val = py2ecotect.conversation.Request("get.model.daylightsavings")
    return StringUtil._convert_str_to_type(val, bool)          

def get_day_of_the_year():
    """
    Retrieves the current date and displays it in the julian date 
    format, where a single integer value between 1 and 365 represents a 
    day of the year. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    day 
    An integer value between 1 and 365 that represents a day of the 
    year. 
    """
    val = py2ecotect.conversation.Request("get.model.dayoftheyear")
    return StringUtil._convert_str_to_type(val, int)  

def set_day_of_the_year(day, time=None):
    """
    Sets the current date using the julian date format. 

    Parameter(s)
    This property takes the following parameters.
    
    day 
    An integer value between 1 and 365 that represents a day of the year. 
    
    [time] 
    This optional parameter is a decimal hour between 0.0 and 23.99. 
    """
    if time:
        arg_str = StringUtil._convert_args_to_string("set.model.dayoftheyear", day, time)
    else:
        arg_str = StringUtil._convert_args_to_string("set.model.dayoftheyear", day)
    py2ecotect.conversation.Exec(arg_str)

def get_directory():
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
    val = py2ecotect.conversation.Request("get.model.directory")
    return StringUtil._convert_str_to_type(val, str)

def set_directory(path):
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
    args = StringUtil._convert_args_to_string("set.model.directory", path)
    arg_str = StringUtil._convert_args_to_string(args)
    py2ecotect.conversation.Exec(arg_str)

def get_display():
    """
    Retrieves the current information display. When retrieving this 
    value, a single integer value is returned corresponding to items in 
    the Model Display table. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    display 
    What information is displayed in the model. This is given as an 
    integer value from the Model Display table below. 
                
    Token Value Description 
    model 0 Default model only. 
    shadows 1 Shadows and reflections 
    normals 2 Surface normals. 
    sketch 3 Sketched view. 
    winddata 5 Wind distribution data. 
    sprayedrays 7 Sprayed acoustic rays. 
    values 8 Object attribute values. 
    zonetemps 9 Zone temperatures 
    rays 10 Acoustic rays and particles. 
    """
    val = py2ecotect.conversation.Request("get.model.display")
    return StringUtil._convert_str_to_type(val, int)        

def set_display(display):
    """
    This property sets the current information display. 

    Parameter(s)
    This property takes the following parameters.
    
    display 
    Sets what information to display in the model. This can be specified 
    as either a token or value parameter, as outlined in the Model 
    Display table below. 
    
    Token Value Description 
    model 0 Default model only. 
    shadows 1 Shadows and reflections 
    normals 2 Surface normals. 
    sketch 3 Sketched view. 
    winddata 5 Wind distribution data. 
    sprayedrays 7 Sprayed acoustic rays. 
    values 8 Object attribute values. 
    zonetemps 9 Zone temperatures 
    rays 10 Acoustic rays and particles. 
    """
    args = StringUtil._convert_args_to_string("set.model.display", display)
    py2ecotect.conversation.Exec()

def get_distance(x1, y1, z1, x2, y2, z2):
    """
    Retrieves geometric information from the current ECOTECT model, 
    specifically the distance between two points, starting at 
    (x1, y1, z1) and ending at (x2, y2, z2). The value returned is given 
    in the current units. 
    
    Parameter(s)
    This property takes the following parameters.
    
    x1, y1, z1 
    Represents the absolute position in the X, Y and Z axis of a 
    starting point in 3 dimensional model space. 
    
    x2, y2, z2 
    Represents the absolute position in the X, Y and Z axis of an end 
    point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    dist 
    The distance value in the current model units.             
    """
    args = StringUtil._convert_args_to_string("get.model.distance", x1, y1, z1, x2, y2, z2)
    val = py2ecotect.conversation.Request(args)
    return StringUtil._convert_str_to_type(val, float)          


def get_filename():
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
    val = py2ecotect.conversation.Request("get.model.filename")
    return StringUtil._convert_str_to_type(val, str)

def get_last_node():
    """
    Returns the zero-based index of the last added/inserted node within 
    the currently loaded ECOTECT model. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    node 
    The zero-based index of the last created or inserted node. If no 
    such node exists, a value of -1 is returned. 
    """
    val = py2ecotect.conversation.Request("get.model.lastnode")
    return StringUtil._convert_str_to_type(val, int)

def get_materials():
    """
    Returns the number of materials stored in the currently loaded 
    ECOTECT model. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    count 
    The total number of materials defined within the current model's 
    element library. 
    """
    val = py2ecotect.conversation.Request("get.model.materials")
    return StringUtil._convert_str_to_type(val, int)      

def get_month():
    """
    Returns the current month. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    month 
    The current model month given as an integer index between 0 and 11. 
    """
    val = py2ecotect.conversation.Request("get.model.month")
    return StringUtil._convert_str_to_type(val, int)

def get_next_node(object, index):
    """
    Returns the zero-based absolute index of the next node in the specified 
    object, in relation to the current node. 
    
    Parameter(s)
    This property takes the following parameters.
    
    object 
    The zero-based index of the object to use. 
    
    index 
    The zero-based index of the node within the current object to use. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    node 
    The zero-based index of the next node. If no matching node is found, a 
    value of -1 is returned. 
    """
    args = StringUtil._convert_args_to_string("get.model.nextnode", object, index)
    val = py2ecotect.conversation.Request(args)
    return StringUtil._convert_str_to_type(val, int)       

def get_next_object(startat, type, flag, tag, zone):
    """
    
    Use this property to obtain the zero-based index of the next object 
    matching the type, flag and tag values specified. 
    
    Parameter(s)
    This property takes the following parameters.
    
    startat 
    The index value to start searching from. To search from the start, use a 
    value of -1. 
    
    type 
    The element type, as outlined in the Element Types table below. To 
    ignore this parameter, enter it as a negative value, such as -1. 
    
    flag 
    The integer flags from the Object Flags table. To combine multiple flag 
    values, add their numeric values together. To ignore this parameter, 
    enter it as a negative value, such as -1. 
    
    tag 
    The integer tag parameter from the Object Tags table. To combine 
    multiple tag values, add their numeric values together. To ignore this 
    parameter, enter it as a negative value, such as -1. 
    
    zone 
    The zero-based index of the zone to which the object must belong. To 
    ignore this parameter, enter it as a negative value, such as -1. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    object 
    The zero-based index of the next object found. If no matching object is 
    found, a value of -1 is returned. 
    
    Element Types 
    Token Value 
    void 0 
    roof 1 
    floor 2 
    ceiling 3 
    wall 4 
    partition 5 
    window 6 
    panel 7 
    door 8 
    point 9 
    speaker 10 
    light 11 
    appliance 12 
    line 13 
    solarcollector 14 
    camera 15 
    
    Object Flag Codes 
    Value Description 
    1 Object is a single-node point. 
    2 Object is a direction vector. 
    4 Object is a flat surface with an equation. 
    8 Objects is a closed loop. 
    16 Object defines a virtual polyline. 
    32 Object is formed from the extrusion of its parent. 
    64 Object has been extruded. 
    128 Object is linked to another as coplanar. 
    256 Object is linked to another as inside its extents. 
    512 Object is a complex/concave polygon. 
    1024 Object is the parent of another. 
    2048 Object is the child of another. 
    4096 Object defines a model zone. 
    8192 *User has specified particular nodes to generate equation. 
    16384 Object's surface normal is reversed. 
    32768 Object is partially transparent. 
    
    Object Tag Codes 
    Value Description 
    1 *User clicked near one of its lines. 
    2 *Part of the previous selection set. 
    16 Object has valid assigned attribute data. 
    32 Shadows are cast onto this object. 
    256 Object produces solar reflections. 
    512 Object is tagged as an acoustic reflector. 
    4096 Not used. 
    32768 *Generic calculation marker. 

    """
    args = StringUtil._convert_args_to_string("get.model.nextobject", startat, type, flag, tag, zone)
    val = py2ecotect.conversation.Request(args)
    return StringUtil._convert_str_to_type(val, int)          

def get_nodes():
    """
    
    Returns the number of individual object nodes within the currently 
    loaded ECOTECT model. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    count 
    The total number of nodes within the current model. 
    
    """
    val = py2ecotect.conversation.Request("get.model.nodes")
    return StringUtil._convert_str_to_type(val, int)          

def get_objects():
    """
    Returns the number of objects in the currently loaded ECOTECT model. 
    
    Parameter(s)
    This property takes the following parameters.
    
    count 
    The total number of objects in the current model. 
    Return Value(s)
    Getting this property returns the following value(s).
    
    count 
    The total number of objects in the current model. 
    """
    val = py2ecotect.conversation.Request("get.model.objects")
    return StringUtil._convert_str_to_type(val, int)

def get_orientation(x1, y1, z1, x2, y2, z2):
    """
    Retrieves geometric information from the current ECOTECT model, 
    specifically the relative horizontal angle from North of a line starting 
    at (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
    returned is given in a positive clockwise direction. 
    
    Parameter(s)
    This property takes the following parameters.
    
    x1, y1, z1 
    Represents the absolute position in the X, Y and Z axis of a starting 
    point in 3 dimensional model space. 
    
    x2, y2, z2 
    Represents the absolute position in the X, Y and Z axis of an end point 
    in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    ori 
    The orinetation angle in degrees. 
    """
    args = StringUtil._convert_args_to_string("get.model.orientation", x1, y1, z1, x2, y2, z2)
    val = py2ecotect.conversation.Request(args)
    return StringUtil._convert_str_to_type(val, float)        

def get_origin():
    """
    Retrieves the location of the Transformation Origin. This is a dynamic 
    point about which objects are rotated, scaled or mirrored. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y, z 
    Represents the absolute position in the X, Y and Z axis of a point in 3 
    dimensional model space. 
    """
    val = py2ecotect.conversation.Request("get.model.origin")
    return StringUtil._convert_str_to_list(val, float)

def set_origin(x, y, z):
    """
    Sets the location of the Transformation Origin. This is a dynamic point 
    about which objects are rotated, scaled or mirrored. 
    
    Parameter(s)
    This property takes the following parameters.
    
    x, y, z 
    Represents the absolute position in the X, Y and Z axis of a point in 3 
    dimensional model space. 

    """
    args = StringUtil._convert_args_to_string("set.model.origin", x, y, z)
    py2ecotect.conversation.Exec(args)     

def get_path_name():
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
    return py2ecotect.conversation.Request("get.model.pathname")

def get_prev_node(object, index):
    """
    Returns the zero-based absolute index of the previous node in the 
    specified object, in relation to the current node. 

    Parameter(s)
    This property takes the following parameters.
    
    object 
    The zero-based index of the object to use. 
    index 
    
    The zero-based index of the current node in the current object to use. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    node 
    The zero-based index of the previous node. If no matching node is found, 
    a value of -1 is returned. 
    """
    args = StringUtil._convert_args_to_string("get.model.prevnode", object, index)
    val = py2ecotect.conversation.Request(args)
    return StringUtil._convert_str_to_type(val, int)        

def get_prev_object(startat, type, flag, tag, zone):
    """
    Use this property to obtain the zero-based index of the preceding object 
    matching the type, flag and tag values specified. 

    Parameter(s)
    This property takes the following parameters.
    
    startat 
    The index value to start searching from. To search from the start, use 
    a value of -1. 
    
    type 
    This refers to the element type, as outlined in the Element Types table. 
    To ignore this parameter, enter it as a negative value such as -1. 
    
    flag 
    This parameter refers to the items in the Object Flags table. To combine 
    multiple flag values, simply add their numeric values together. To 
    ignore this parameter, enter it as a negative value such as -1. 
    
    tag 
    This parameter refers to the items in the Object Tags table. To combine 
    multiple tag values, simply add their numeric values together. To ignore 
    this parameter, enter it as a negative value such as -1. 
    
    zone 
    The zero-based index of the zone to which the object must belong. To 
    ignore this parameter, enter it as a negative value such as -1. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    object 
    The zero-based index of the next object found. If no matching object is 
    found, a value of -1 is returned. 
    
    Element Types 
    Token Value 
    void 0 
    roof 1 
    floor 2 
    ceiling 3 
    wall 4 
    partition 5 
    window 6 
    panel 7 
    door 8 
    point 9 
    speaker 10 
    light 11 
    appliance 12 
    line 13 
    solarcollector 14 
    camera 15 

    Object Flag Codes 
    Value Description 
    1 Object is a single-node point. 
    2 Object is a direction vector. 
    4 Object is a flat surface with an equation. 
    8 Objects is a closed loop. 
    16 Object defines a virtual polyline. 
    32 Object is formed from the extrusion of its parent. 
    64 Object has been extruded. 
    128 Object is linked to another as coplanar. 
    256 Object is linked to another as inside its extents. 
    512 Object is a complex/concave polygon. 
    1024 Object is the parent of another. 
    2048 Object is the child of another. 
    4096 Object defines a model zone. 
    8192 *User has specified particular nodes to generate equation. 
    16384 Object's surface normal is reversed. 
    32768 Object is partially transparent. 

    Object Tag Codes 
    Value Description 
    1 *User clicked near one of its lines. 
    2 *Part of the previous selection set. 
    16 Object has valid assigned attribute data. 
    32 Shadows are cast onto this object. 
    256 Object produces solar reflections. 
    512 Object is tagged as an acoustic reflector. 
    4096 Not used. 
    32768 *Generic calculation marker. 
    """
    args = StringUtil._convert_args_to_string("get.model.prevobject", startat, type, flag, tag, zone)
    val = py2ecotect.conversation.Request(args)
    return StringUtil._convert_str_to_type(val, int)         

def get_snap():
    """
    No docs
    """
    va = py2ecotect.conversation.Request("get.model.snap")
    return StringUtil._convert_str_to_type(val, bool)         

def set_snap(snap):
    """
    No docs
    """
    args = StringUtil._convert_args_to_string("set.model.snap", snap)
    py2ecotect.conversation.Exec(args)
    
def get_sun_angles():
    """
    Returns two values, being the azimuth and altitude of the Sun for the 
    current date and time, given in decimal degrees. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    azi 
    The current solar azimuth given in degrees. 
    
    alt 
    The current solar altitude given in degrees. 
    """
    val = py2ecotect.conversation.Request("get.model.sunangles")
    return StringUtil._convert_str_to_list(val, float)          
    
def get_sun_position(dist=0, xyz=(0,0,0)):
    """
    Returns a position value that can be used to represent the Sun location 
    relative to the model. This is useful is you wish to locate a Sun 
    position relative to the centre of a WINDOW in order to spray a ray or 
    do a visibility test, for example. 
    
    Parameter(s)
    This property takes the following parameters.
    
    [dist] 
    The optional distance the Sun will be placed from the centre of the 
    model. 
    
    [x, y, z] 
    If these optional parameters are given, the Sun position will be 
    generated at a location dist away from this position, using the current 
    Sun angles in the model. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y, z 
    Represents the absolute position in the X, Y and Z axis of the Sun in 3 
    dimensional model space. 
    """
    arg_str = StringUtil._convert_args_to_string("get.model.sunposition", dist, xyz[0], xyz[1], xyz[2])
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_list(val, float) 
        
def get_sunrise():
    """
    Returns the sunrise time as a 24 hour decimal value. Thus, 6:30am would 
    be returned as 6.5. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    sunrise 
    The time of sunrise given as a decimal hour. 
    """
    val = py2ecotect.conversation.Request("get.model.sunrise")
    return StringUtil._convert_str_to_type(val, float)  
    
def get_sun_set():
    """
    Returns the sunset time as a 24 hour decimal value. Thus, 6:30pm would 
    be returned as 18.5. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    sunset 
    The time of sunset given as a decimal hour. 
    """
    val = py2ecotect.conversation.Request("get.model.sunset")
    return StringUtil._convert_str_to_type(val, float)        

def get_time():
    """
    Retrieves the current time of day. The time value returned is a decimal 
    value between 0.0 and 23.99. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    time 
    A decimal value between 0.0 and 23.99. 
    """
    val = py2ecotect.conversation.Request("get.model.time")
    return StringUtil._convert_str_to_type(val, float)          

def set_time(time):
    """
    Sets the current time of day. 
    
    Parameter(s)
    This property takes the following parameters.
    
    time 
    The time given in decimal hours, between 0.0 and 23.99. 
    """
    args = StringUtil._convert_args_to_string("set.model.time", time)
    py2ecotect.conversation.Exec(args)

def get_time_string():
    """
    Retrieves a formated string containing the current model time. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    timeStr 
    A formated time string. 
    """
    val = py2ecotect.conversation.Request("get.model.timestring")
    return StringUtil._convert_str_to_type(val, str)
    
def get_cap_extrusions():
    """
    Retrieves the capextrusions flag. When capextrusions is set to true or 
    1, extruding an object automatically generates a top or 'lid' to cap off 
    the volume. When set to false or 0, no lid is generated. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    A boolean value where 1 represents the affirmative and 0 the negative. 
    """
    val = py2ecotect.conversation.Request("get.model.xform.capextrusions")
    return StringUtil._convert_str_to_type(val, bool)          
    
def set_cap_extrusions(state = True):
    """
    Sets the capextrusions flag. 
    
    Parameter(s)
    This property takes the following parameters.
    
    [state] 
    When set to true, extruding an object automatically generates a top or 
    'lid' to cap off the volume. When set to false, no lid is generated. 
    """
    args = StringUtil._convert_args_to_string("set.model.xform.capextrusions", state)
    py2ecotect.conversation.Exec(args)

def get_vectors():
    """
    Retrieves the xform.vectors flag. With transform vectors set to true or 
    1, rotating an object with offset-linked children will also rotate the 
    offset vector. When set to false or 0, the offset vector remains the 
    same even though each object rotates individually. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    A boolean value where 1 represents the affirmative and 0 the negative. 
    """
    val = py2ecotect.conversation.Request("get.model.xform.vectors")
    return StringUtil._convert_str_to_type(val, bool)

def set_vectors(state = True):
    """
    Returns the number of zones in the currently loaded ECOTECT model as a 
    single integer. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    count 
    The total number of zones in the current model. 
    """
    args = StringUtil._convert_args_to_string("set.model.xform.vectors", state)
    py2ecotect.conversation.Exec(args)

#===============================================================================
# Main function used for testing
#===============================================================================
def test_doc_test():
    """
    >>> test_doc_test()
    Hi
    """
    print "Hi"
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #dump("C:\Test\mytest1.eco")
    #print get_altitude(11, 10, 15, 9, 16, 13)
    print "Tests completed"     
    