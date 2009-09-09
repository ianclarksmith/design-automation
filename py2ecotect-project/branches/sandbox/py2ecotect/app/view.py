import py2ecotect as p2e

#=============================================================================
# Functions
#=============================================================================
def view_front():
    """
    
    Sets the current view type to Front. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("view.front")    

def view_side():
    """
    
    Sets the current view type to Side. 

    Parameter(s)
    There are no parameters for this command.
    
    LUA Script Example(s)

    """
    p2e._app.Exec("view.side")

def view_plan():
    """
    
    Sets the current view type to Plan. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("view.plan")
    
def view_axo(azi = 0.0):
    """
    
    Sets the current view to a 3D axonometric view. 

    Parameter(s)
    This command takes the following parameters.
    
    [azi] 
    This optional parameter can be used to specify the azimuth angle in 
    degrees from which the model is viewed.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.axonometric", azi)
    p2e._app.Exec(arg_str)

def view_persp():
    """
    
    Sets the current view type to Perspective. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("view.perspective")
#------------------------------------------------------------------------------ 
def image_copy(format = ""):
    """
    
    Copies the current model view to the clipboard in the Windows Bitmap 
    (.bmp) format. If the .wmf suffix is used, a the Windows Metafile 
    (.wfm) format is created instead. 

    Parameter(s)
    This command takes the following parameters.
    
    [format]
    Can be bmp or wmf. Default is blank.

    """
    if len(format) != 0:
        format = "." + format
    p2e._app.Exec("view.copy" + format)

def image_save(filename, format = ""):
    """
    
    Saves the current model view to the specified location. If no command 
    suffix is given, the default Windows Bitmap (.bmp) format is used, 
    otherwise the suffix is used to select between JPEG (.jpg) and Windows 
    Metafile (.wmf) formats. 

    Parameter(s)
    This command takes the following parameters.
    
    filename 
    The full path of the location where the file will be stored.
    
    format
    Optional parameter thats specifies file format. By default file will be 
    saved in .bmp
    
    """
    if len(format) != 0:
        format = "." + format
    arg_str = p2e._base._util._convert_args_to_string("view.save" + format, 
                                                  filename)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def fit():
    """
    
    Zooms the current model view to fit entirely within the display canvas. 
    This does not change the current ground display grid. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("view.fit")

def fit_grid():
    """
    
    Resizes the ground display grid to encompass all currently visible 
    elements within the model and fits the resulting model view within the 
    display canvas. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("view.fitgrid")
#------------------------------------------------------------------------------ 
def maximise():
    """
    
    Maximises the main ECOTECT application window. 

    Parameter(s)
    This command takes the following parameters.
    
    [state] 
    This optional parameter determines whether the application is maximised 
    (true), or restored to its previous state (false). Defaulting to true 
    if now specified.
    
    """
    p2e._app.Exec("view.maximise")

def minimise():
    """
    
    Minimises the main ECOTECT application window. 

    Parameter(s)
    This command takes the following parameters.
    
    [state] 
    This optional parameter determines whether the application is minimised (true), or restored to its previous state (false). Defaulting to true if now specified.
    
    """
    p2e._app.Exec("view.minimise")
#------------------------------------------------------------------------------ 
def mouse_event(action, position):
    """
    
    Simulates mouse events within the main model canvas. For more 
    information, see the app.mouseevent command. 

    Parameter(s)
    This command takes the following parameters.
    
    action 
    A token corresponding to the table below. 
    
    position
    A list of two values that represent the position at which to trigger 
    the mouse event on the XY-Axis in pixels.
    
    Relevant Data Table(s)
    
    Available Mouse Actions 
    Token Description 
    move move mouse to new position 
    lclick Left mouse button clicked 
    ldown Left mouse button pressed 
    lup Left mouse button released 
    rclick Right mouse button clicked 
    rdown Right mouse button pressed 
    rup Right mouse button released 
    mclick Middle mouse button clicked 
    mdown Middle mouse button pressed 
    mup Middle mouse button released 
    wdown Mouse wheel pressed 
    wup Mouse wheel released 
    ldblclick Left mouse button double-clicked 
    rdblclick Right mouse button double-clicked 

    """
    arg_str = p2e._base._util._convert_args_to_string("view.mouseevent", 
                                                  action, 
                                                  position[0], position[1])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def move_in(shift = False):
    """
    
    Moves the perspective eye position 10 34653648nward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the move 
    instead. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.movein", shift)
    p2e._app.Exec(arg_str)

def move_out(shift = False):
    """
    
    Moves the perspective eye position 10204142720utward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the move 
    instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.moveout", shift)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def pan_down(shift = False):
    """
    
    Pans the current 2D and 3D view by 10 deg downward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the pan 
    instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.pandown", shift)
    p2e._app.Exec(arg_str)

def pan_left(shift = False):
    """
    
    Pans the current 2D and 3D view by 10 deg to the left. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the pan 
    instead. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.panleft", shift)
    p2e._app.Exec(arg_str)

def pan_right(shift = False):
    """
    
    Pans the current 2D and 3D view by 10 deg to the right. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the pan 
    instead. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.panright", shift)
    p2e._app.Exec(arg_str)

def pan_up(shift = False):
    """
    
    Pans the current 2D and 3D view by 10 deg upward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the pan 
    instead. 

    """
    arg_str = p2e._base._util._convert_args_to_string("view.panup", shift)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def redraw():
    """
    
    Redraws the current model view, updating it with any previously made changes. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("view.redraw")
#------------------------------------------------------------------------------ 
def reset():
    """
    
    Resets the view to fit canvas. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("view.reset")
#------------------------------------------------------------------------------ 
def restore(index):
    """
    
    Restore a previously stored model view. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    An integer value between 1 and 5 specifying the index of the stored view. 
    
    """ 
    arg_str = p2e._base._util._convert_args_to_string("view.restore", index)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def rotate_down(shift = False):
    """
    
    Rotates the current 3D view by 10 deg downward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the 
    rotation instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.rotatedown", shift)
    p2e._app.Exec(arg_str)

def rotate_left(shift = False):
    """
    
    Rotates the current 3D view by 10 deg to the left. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the 
    rotation instead. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.rotateleft", shift)
    p2e._app.Exec(arg_str)

def rotate_right(shift = False):
    """
    
    Rotates the current 3D view by 10 deg to the right. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the 
    rotation instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.rotateright", shift)
    p2e._app.Exec(arg_str)

def rotate_up(shift = False):
    """
    
    Rotates the current 3D view by 10 deg upward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the rotation instead.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.rotateup", shift)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def store(index):
    """
    
    Stores the current model view to the specified index. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    An integer between 1 and 5 indication the index number to which the 
    view will be assigned. 

    """
    arg_str = p2e._base._util._convert_args_to_string("view.store", index)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def zoom(factor):
    """
    
    Zoom the current model view by the specified factor. 

    Parameter(s)
    This command takes the following parameters.
    
    factor 
    A decimal value given as a multiplier.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.store", factor)
    p2e._app.Exec(arg_str)

def zoom_in(shift = False):
    """
    
    Zooms the current 2D and 3D view by 10 deg inward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the zoom 
    instead. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.zoomin", shift)
    p2e._app.Exec(arg_str)
    
def zoom_out(shift = False):
    """
    
    Zooms the current 2D and 3D view by 10 deg outward. 

    Parameter(s)
    This command takes the following parameters.
    
    [shift] 
    If this optional parameter is set to true, 1% will be used for the zoom 
    instead. 
            
    """
    arg_str = p2e._base._util._convert_args_to_string("view.zoomout", shift)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
#=============================================================================
# Properties
#=============================================================================
def align():
    """
    
    Retrieves the the alignment of output text by the view.draw.text. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    alignment 
    The alignment parameter is an integer value representing binary bits, as 
    shown in the Text Align table below. Horizontal and vertical alignments 
    are combined by adding the corresponding values. 
    
    Relevant Data Table(s)
    Text Alignment Codes 
    Value Description 
    0 LEFT and TOP 
    2 RIGHT 
    6 CENTER 
    8 BOTTOM 
    24 BASELINE 
    
    """
    val = p2e._app.Request("get.view.align")
    return p2e._base._util._convert_str_to_type(val, int)

def set_align(alignment):
    """
    
    This command allows you to set the alignment of any subsequent output 
    text by the view.draw.text. 

    Parameter(s)
    This property takes the following parameters.
    
    alignment 
    The alignment parameter is an integer value representing binary bits, 
    as shown in the Text Align table below. To combine horizontal and 
    vertical alignments, add the corresponding values together. 
    
    Relevant Data Table(s)
    
    Text Alignment Codes 
    Value Description 
    0 LEFT and TOP 
    2 RIGHT 
    6 CENTER 
    8 BOTTOM 
    24 BASELINE 

    """
    arg_str = p2e._base._util._convert_args_to_string("set.view.align", 
                                                  alignment)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def font():
    """
    
    Retrieves the current font settings for subsequent output text in the 
    current model view (see the view.draw commands above). 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    size 
    This is an integer value describing the size of the font in points. 
    
    name 
    The full name of the font type being used.
    
    """
    val = p2e._app.Request("get.view.font")
    return p2e._base._util._convert_str_to_list(val, int, str)

def set_font(size, name):
    """
    
    Sets the font settings for subsequent output text in the current model 
    view (see the view.draw commands above). 

    Parameter(s)
    This property takes the following parameters.
    
    size 
    The font size to be used. This is usually given as a negative number to 
    tell Windows to use the height of the font. A positive number is used to 
    set the default font cell size. 
    
    name 
    The string identifier of the font to use, for example Arial, Verdana or 
    Courier New. The font name specified should be enclosed in "", as shown 
    in the following example.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.view.font", 
                                                  size, name)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def grid_max():
    """
    
    Retrieves the maximum end position of the current display grid. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y, z 
    Represents the absolute position in the X, Y and Z axis of a maximum 
    point in 3 dimensional model space. 
    
    """
    val = p2e._app.Request("get.view.grid.max")
    return p2e._base._util._convert_str_to_list(val, float, float, float)

def set_grid_max(absolute_position):
    """
    
    This method/property is yet to be documented. 

    Parameter(s)
    This property takes the following parameters.
    
    absolute_position 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a maximum point in 3 dimensional model space.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.view.grid.max", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def grid_min():
    """
    
    Retrieves the minimum starting position of the current display grid. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y, z 
    Represents the absolute position in the X, Y and Z axis of a minimum 
    point in 3 dimensional model space. 

    """
    val = p2e._app.Request("get.view.grid.min")
    return p2e._base._util._convert_str_to_list(val, float, float, float)

def set_grid_min(absolute_position):
    """
    
    Sets the minimum starting position of the current display grid. 

    Parameter(s)
    This property takes the following parameters.
    
    absolute_position 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a minimum point in 3 dimensional model space. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.view.grid.min", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def size():
    """
    
    Retrieves the current view dimensions in pixels. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    width 
    The width of the view canvas. 
    
    height 
    The height of the view canvas.
    
    """
    val = p2e._app.Request("get.view.size")
    return p2e._base._util._convert_str_to_list(val, float, float)

def set_size(width, height):
    """
    
    Sets the current view dimensions in pixels. 

    Parameter(s)
    This property takes the following parameters.
    
    width 
    The new width of the view canvas. 
    
    height 
    The new height of the view canvas.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.view.size", width, height)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def visible():
    """
    
    Returns whether or not the 3D EDITOR view is currently displayed or not. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    visible 
    This is a boolean value where 1 means true and 0 means false.
    
    """
    val = p2e._app.Request("get.view.visible")
    return p2e._base._util._convert_str_to_type(val, int)
#------------------------------------------------------------------------------ 
    