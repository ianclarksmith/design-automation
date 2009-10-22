import py2ecotect as p2e

#===========================================================================
# Functions
#=========================================================================== 

def altitude(point_start, point_end):
    """
    
    Retrieves geometric information from the current ECOTECT model, 
    specifically the vertical angular distance of a line starting at 
    (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
    returned is given in degrees. 

    Parameter(s)
    This property takes the following parameters.

    point_start 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a starting point in 3 dimensional model space.
     
    point_end 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of an end point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).

    alt 
    The altitude angle in degrees. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.model.altitude", 
                                                      point_start[0],
                                                      point_start[1], 
                                                      point_start[2],
                                                      point_end[0],
                                                      point_end[1],
                                                      point_end[2])
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)        
    
def azimuth(point_start, point_end):
    """
    
    Retrieves geometric information from the current ECOTECT model, 
    specifically the horizontal angular distance of a line starting at 
    (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
    returned is given in degrees. 

    Parameter(s)
    This property takes the following parameters.
    
    point_start 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a starting point in 3 dimensional model space.
     
    point_end 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of an end point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    azi 
    The azimuth angle in degrees.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.model.azimuth",
                                                      point_start[0],
                                                      point_start[1], 
                                                      point_start[2],
                                                      point_end[0],
                                                      point_end[1],
                                                      point_end[2])
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)    

#------------------------------------------------------------------------------ 
def angles():    
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
    val = p2e._app.Request("get.model.sunangles")
    return p2e._base._util._convert_str_to_list(val, float)

def position(dist = 0, xyz = (0,0,0)):
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
    A list of three values. If these optional parameters are given, the Sun 
    position will be generated at a location dist away from this position, 
    using the current Sun angles in the model. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    x, y, z 
    Represents the absolute position in the X, Y and Z axis of the Sun in 3 
    dimensional model space. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.model.sunposition", 
                                                          dist, xyz[0], 
                                                          xyz[1], xyz[2])
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_list(val, float) 