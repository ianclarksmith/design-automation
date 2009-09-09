import py2ecotect as p2e

#=============================================================================
# Functions
#=============================================================================
def draw_arrow_2d(screen_point, size = ""):
    """
    
    Draws a 2D arrow object from the origin point to the specified 2D screen 
    location in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    screen_point 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used. 
    
    [size] 
    This optional parameter sets the size of the object in pixels.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.arrow2d", 
                                                  screen_point[0],
                                                  screen_point[1], 
                                                  size)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_arrow(point, size = ""):
    """
    
    Draws a 3D arrow object from the origin point to the specified 3D world 
    position in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    point
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    [size] 
    This optional parameter sets the size of the object in the current 
    modelling units.
    
    """
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("view.draw.arrowto", 
                                                  point[0],
                                                  point[1],
                                                  point[2], size)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_cross(point):
    """
    
    Draws a 2D cross object at the specified 3D world position in the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    point
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space.  

    """
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("view.draw.cross", 
                                                  point[0],
                                                  point[1],
                                                  point[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_line_2d(screen_point):
    """
    
    Draws a 2D line object from the origin point to the specified 2D screen 
    location in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    screen_point 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.line2d", 
                                                  screen_point[0],
                                                  screen_point[1])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_line(point):
    """
    
    Draws a 3D line object from the origin point to the specified 3D world 
    position in the current view. 

    Parameter(s)
    This command takes the following parameters.
    
    point
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    """
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("view.draw.lineto", 
                                                  point[0],
                                                  point[1],
                                                  point[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_origin_2d(screen_point):
    """
    
    Moves the 2D origin point to the specified 2D screen location in the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    screen_point 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.move2d", 
                                                  screen_point[0],
                                                  screen_point[1])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_origin(point):
    """
    
    Moves the 3D origin point to the specified 3D world position within the 
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    point
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    """
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("view.draw.moveto", 
                                                  point[0],
                                                  point[1],
                                                  point[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_pixel(point):
    """
    
    Draws a pixel at the specified 3D world position within the curent view. 

    Parameter(s)
    This command takes the following parameters.
    
    point
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space.
    
    """
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("view.draw.pixel", 
                                                  point[0],
                                                  point[1],
                                                  point[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_point(point):
    """
    
    Draws a point at the specified 3D world position within the current 
    view. 

    Parameter(s)
    This command takes the following parameters.
    
    point
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space.
    
    """
    point = p2e._base._util.scale_1000(point)
       
    arg_str = p2e._base._util._convert_args_to_string("view.draw.point", 
                                                  point[0],
                                                  point[1],
                                                  point[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_sphere(point, radius):
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
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("view.draw.sphere", 
                                                  point[0],
                                                  point[1],
                                                  point[2], 
                                                  radius)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_text(point, text):
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
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("view.draw.text", 
                                                  point[0],
                                                  point[1],
                                                  point[2], text)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def draw_text_2d(screen_point, string):
    """
    
    Displays a string of text at the specified 2D screen location in the
    current view. 

    Parameter(s)
    This command takes the following parameters.
    
    screen_point 
    A list of two values that represent the position on the screen in the 
    X and Y axis as an offset from the top-left corner in pixels of the 
    display canvas or control being used. 
    
    string 
    The text string to be displayed.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("view.draw.text2d", 
                                                  screen_point[0],
                                                  screen_point[1], 
                                                  string)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
#=============================================================================
# Properties
#=============================================================================
def pen():
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
def screen_point(point):
    """
    
    Returns the 2D screen position of the specified 3D point within the 
    current view. 

    Parameter(s)
    This property takes the following parameters.
    
    point 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y 
    Represents a position on the screen in the X and Y axis as an offset 
    from the top-left corner in pixels. 
    
    """
    point = p2e._base._util.scale_1000(point)
    
    arg_str = p2e._base._util._convert_args_to_string("get.view.point", 
                                                  point[0],
                                                  point[1],
                                                  point[2])
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_list(val, float, float)
#------------------------------------------------------------------------------ 