import py2ecotect as p2e

#=============================================================================
# Functions
#=============================================================================
def draw_arrow2d(offset, size = ""):
    """
    
    Draws a 2D arrow object from the origin point to the specified 2D screen 
    location in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    offset 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used. 
    
    [size] 
    This optional parameter sets the size of the object in pixels.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.arrow2d", 
                                                  offset[0],
                                                  offset[1], 
                                                  size)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_arrowto(absolute_position, size = ""):
    """
    
    Draws a 3D arrow object from the origin point to the specified 3D world 
    position in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    [size] 
    This optional parameter sets the size of the object in the current 
    modelling units.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.arrowto", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2], size)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_cross(absolute_position):
    """
    
    Draws a 2D cross object at the specified 3D world position in the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space.  

    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.cross", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_line2d(offset):
    """
    
    Draws a 2D line object from the origin point to the specified 2D screen 
    location in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    offset 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.line2d", 
                                                  offset[0],
                                                  offset[1])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_lineto(absolute_position):
    """
    
    Draws a 3D line object from the origin point to the specified 3D world 
    position in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.lineto", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_move2d(offset):
    """
    
    Moves the 2D origin point to the specified 2D screen location in the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    offset 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.move2d", 
                                                  offset[0],
                                                  offset[1])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_moveto(absolute_position):
    """
    
    Moves the 3D origin point to the specified 3D world position within the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.moveto", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_pixel(absolute_position):
    """
    
    Draws a pixel at the specified 3D world position within the curent view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.pixel", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_point(absolute_position):
    """
    
    Draws a point at the specified 3D world position within the current 
    view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.point", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_sphere(absolute_position, radius):
    """
    
    Draws a 3D sphere object at the specified 3D world position in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space.
            
    radius 
    The radius of the sphere in the current modelling units.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.sphere", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2], 
                                                  radius)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_text(absolute_position, text):
    """
    
    Displays a string of text at the specified 3D world position inside the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    absolute_position
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    text 
    The text string to be displayed.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.text", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2], text)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_text2d(offset, string):
    """
    
    Displays a string of text at the specified 3D world position inside the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    offset 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used. 
    
    string 
    The text string to be displayed.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.text2d", 
                                                  offset[0],
                                                  offset[1], 
                                                  string)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
#=============================================================================
# Properties
#=============================================================================
def get_pen():
    """
    
    Retrieves the current pen color and size. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    color 
    The color as a RGB hexidecimal number, given in the form 0xFF8800. 
    
    width 
    The thickness of the pen line in pixels. 
    
    """
    val = p2e._app.Request("get.view.pen")
    return p2e._base._util._convert_str_to_list(val, str, float)

def set_pen(color, width = 0, alpha = 0.0):
    """
    
    Sets the current pen color, size and opacity. 

    Parameter(s)
    This property takes the following parameters.
    
    color 
    The color as a RGB hexidecimal number, given as a string in the form of 
    "0xFF8800" or "FF8800". 
    
    [width] 
    This optional parameter specifies the thickness of the pen line in 
    pixels. 
    
    [alpha] 
    This optional parameter is a decimal value between 0 (transparent) and 
    1(opaque). 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.view.pen", color, 
                                                  width, alpha)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def get_point(absolute_position):
    """
    
    Returns the 2D screen position of the specified 3D point within the 
    current view. 

    Parameter(s)
    This property takes the following parameters.
    
    absolute_position 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y 
    Represents a position on the screen in the X and Y axis as an offset 
    from the top-left corner in pixels. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.view.point", 
                                                  absolute_position[0],
                                                  absolute_position[1],
                                                  absolute_position[2])
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_list(val, float, float)
#------------------------------------------------------------------------------ 