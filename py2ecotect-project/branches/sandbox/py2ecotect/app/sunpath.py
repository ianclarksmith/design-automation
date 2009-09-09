import py2ecotect as p2e

#===========================================================================
# Functions
#===========================================================================
def copy():
    """
    
    Copies the sunpath view to the clipboard in the default, Windows Bitmap 
    (.bmp), format. 
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("sunpath.copy")

def copy_bmp():
    """
    
    Copies the sunpath view to the clipboard in the Windows Bitmap (.bmp) format. 
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("sunpath.copy.bmp")

def copy_wmf():
    """
    
    Copies the sunpath view to the clipboard in the Windows Metafile (.wmf) format. 
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("sunpath.copy.wmf")
#------------------------------------------------------------------------------ 
def mouse_event():
    """
    
    Simulate mouse events within the sunpath canvas. For more information, 
    see the app.mouseevent command. 
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("sunpath.mouseevent")
#------------------------------------------------------------------------------ 
def pan_down(shift = False):
    """
    
    Pans the current rendered view by 10 deg upward. 
    
    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1 deg will be used for the pan 
    instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.pandown", shift)
    p2e._app.Exec(arg_str)

def pan_left(shift = False):
    """
    
    Pans the current rendered view by 10 deg to the left. 
    
    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1 deg will be used for the pan 
    instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.panleft", shift)
    p2e._app.Exec(arg_str)
 
def pan_right(shift = False):
    """
    
    Pans the current rendered view by 10 deg to the right. 
    
    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1 deg will be used for the pan 
    instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.panright", shift)
    p2e._app.Exec(arg_str)

def pan_up(shift = False):
    """
    
    Pans the current rendered view by 10 deg upward. 
    
    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1 deg will be used for the 
    pan instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.panup", shift)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def redraw():
    """
    
    Redraws the current sunpath view, updating it with any previously made changes. 
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("sunpath.redraw")
#------------------------------------------------------------------------------ 
def save(filename):
    """
    
    Saves the current sunpath view to the specified location in the default, 
    Windows Bitmap (.bmp), format. 
    
    Parameter(s)
    This command takes the following parameters.
    
    filename 
    The full path to the location where the file will be stored.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.save", filename)
    p2e._app.Exec(arg_str)

def save_bmp(filename):
    """
    
    Saves the current sunpath view to the specified location in the Windows 
    Bitmap (.bmp) format. 
    
    Parameter(s)
    This command takes the following parameters.
    
    filename 
    The full path to the location where the file will be stored.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.save.bmp", filename)
    p2e._app.Exec(arg_str)

def save_htb2(filename):
    """
    
    Saves the current sunpath shading percentage data to the specified 
    location as a HTB2 shading mask. 
    
    Parameter(s)
    This command takes the following parameters.
    
    filename 
    The full path to the location where the file will be stored.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.save.htb2", filename)
    p2e._app.Exec(arg_str)

def save_shading(filename):
    """
    
    Saves the current sunpath shading percentage data to the specified 
    location as a text file. 
    
    Parameter(s)
    This command takes the following parameters.
    
    filename 
    The full path to the location where the file will be stored. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.save.shading", filename)
    p2e._app.Exec(arg_str)

def save_wmf(filename):
    """
    
    Saves the current sunpath view to the specified location in the Windows 
    Metafile (.wmf) format. 
    
    Parameter(s)
    This command takes the following parameters.
    
    filename 
    The full path to the location where the file will be stored. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.save.wmf", filename)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def show():
    """
    
    Displays the sun-path window and brings it to the front if it is behind 
    any other windows. 
    
    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("sunpath.show")
#------------------------------------------------------------------------------ 
def zoom_in(shift = False):
    """
    
    Zooms the currently rendered view by 10 deg inward. 
    
    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1 deg will be used for the 
    zoom instead. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.zoomin", shift)
    p2e._app.Exec(arg_str)

def zoom_out(shift = False):
    """
    
    Zooms the currently rendered view by 10 deg outward. 
    
    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1 deg will be used for the 
    zoom instead. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("sunpath.zoomout", shift)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------     
#===========================================================================
# Properties
#===========================================================================
def display():
    """
    
    Retrieves the current display and data overlay settings. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    display 
    An integer taken from the following Sunpath Display Types table. 
    
    overlay 
    An integer taken from the following Sunpath Data Overlay Types table.
    
    """
    val = p2e._app.Request("get.sunpath.display")
    return p2e._base._util._convert_str_to_list(val, int, int)
#------------------------------------------------------------------------------ 
def focus():
    """
    
    Retrieves the position of the current SunPath focus point. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y, z 
    Represents the absolute position in the X, Y and Z axis of the focus 
    point in 3 dimensional model space.
    
    """
    val = p2e._app.Request("get.sunpath.focus")
    return p2e._base._util._convert_str_to_list(val, float, float, float)
#------------------------------------------------------------------------------ 
def screen_point(sunpath_point):
    """
    
    Translates a point within the Sun-Path diagram into an absolute screen 
    position. 
    
    Parameter(s)
    This property takes the following parameters.
    
    sunpath_point 
    A list of two values that represent the X and Y axis position of the 
    point in the Sun-Path diagram. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y 
    The X and Y axis position of the point in absolute screen coordinates.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.sunpath.point", 
                                                  sunpath_point[0],
                                                  sunpath_point[1])
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_list(val, float, float)
#------------------------------------------------------------------------------ 
def pos():
    """
    
    Retrieves the current position of the Sunpath dialog box in your local 
    screen coordinates. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    left 
    The offset of the dialog box from the left of the screen in pixels 
    
    top 
    The offset of the dialog box from the top of the screen in pixels 
    
    """
    val = p2e._app.Request("get.sunpath.pos")
    return p2e._base._util._convert_str_to_list(val, int, int)

def set_pos(left, top):
    """
    
    Sets the current position of the Sunpath dialog box in your local 
    screen coordinates. 
    
    Parameter(s)
    This property takes the following parameters.
    
    left 
    The offset of the dialog box from the left of the screen in pixels 
    
    top 
    The offset of the dialog box from the top of the screen in pixels
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.sunpath.pos", left, 
                                                  top)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def size():
    """
    
    Retrieve the size of the Sunpath dialog box. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    width 
    The width in pixels. 
    
    height 
    The height in pixels.
    
    """
    val = p2e._app.Request("get.sunpath.size")
    return p2e._base._util._convert_str_to_list(val, int, int)

def set_size(width, height):
    """
    
    Resizes the Sunpath dialog box to the specified size. 
    
    Parameter(s)
    This property takes the following parameters.
    
    width 
    The new width in pixels. 
    
    height 
    The new height in pixels. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.sunpath.size", width, height)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def visible():
    """
    
    Displays or hides the SunPath Diagram dialog box. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    shown 
    This is a boolean value where 1 or true means show the dialog and 0 or 
    false means hide it. 
    
    """
    val = p2e._app.Request("get.sunpath.visible")
    return p2e._base._util._convert_str_to_type(val, int)
#------------------------------------------------------------------------------ 
 
