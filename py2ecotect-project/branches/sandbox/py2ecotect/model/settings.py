import py2ecotect as p2e

#TODO: merge this with project

#===========================================================================
# Functions
#===========================================================================
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
    p2e._app.Exec("model.update")

#------------------------------------------------------------------------------ 
def transformation_origin():
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
    val = p2e._app.Request("get.model.origin")
    return p2e._base._util._convert_str_to_list(val, float)

def set_transformation_origin(absolute_position):
    """
    
    Sets the location of the Transformation Origin. This is a dynamic point 
    about which objects are rotated, scaled or mirrored. 
    
    Parameter(s)
    This property takes the following parameters.
    
    absolute_position 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a point in 3 dimensional model space. 

    """
    args = p2e._base._util._convert_args_to_string("set.model.origin", 
                                                       absolute_position[0],
                                                       absolute_position[1],
                                                       absolute_position[2])
    p2e._app.Exec(args)
#------------------------------------------------------------------------------ 
def snap():
    """
    
    Retrieves the current information display

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    display 
    What information is displayed in the model. This is given as an integer 
    value from the Model Display table below. 
    
    Relevant Data Table(s)
    
    Model Display Options 
    Token Value Description 
    model 0 Default model only. 
    shadows 1 Shadows and reflections 
    normals 2 Surface normals. 
    sketch 3 Sketched view. 
    winddata 5 Wind distribution data. 
    sprayedrays 7 Sprayed acoustic rays. 
    values 8 Object attribute values. 
    zonetemps 9 Zone temperatures 
    rays 10 Acoustic rays and particles 

    """
    #TODO: check docs - sounds all wrong
    val = p2e._app.Request("get.model.snap")
    return p2e._base._util._convert_str_to_type(val, bool)         

def set_snap(snap):
    """
    
    This property sets the current information display. 

    Parameter(s)
    This property takes the following parameters.
    
    display 
    Sets what information to display in the model. This can be specified as
     either a token or value parameter, as outlined in the Model Display
      table below. 
    
    Relevant Data Table(s)
    
    Model Display Options
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
    args = p2e._base._util._convert_args_to_string("set.model.snap", snap)
    p2e._app.Exec(args)
#------------------------------------------------------------------------------ 
def flag_cap_extrusions():
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
    val = p2e._app.Request("get.model.xform.capextrusions")
    return p2e._base._util._convert_str_to_type(val, bool)          

def set_flag_cap_extrusions(state = True):
    """
    
    Sets the capextrusions flag. 
    
    Parameter(s)
    This property takes the following parameters.
    
    [state] 
    When set to true, extruding an object automatically generates a top or 
    'lid' to cap off the volume. When set to false, no lid is generated. 
    
    """
    args = p2e._base._util._convert_args_to_string("set.model.xform.capextrusions", state)
    p2e._app.Exec(args)
#------------------------------------------------------------------------------ 
def flag_vectors():
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
    val = p2e._app.Request("get.model.xform.vectors")
    return p2e._base._util._convert_str_to_type(val, bool)

def set_flag_vectors(state = True):
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
    args = p2e._base._util._convert_args_to_string("set.model.xform.vectors", state)
    p2e._app.Exec(args)

#------------------------------------------------------------------------------ 
#===============================================================================
# Main function used for testing
#===============================================================================
def distance(absolute_position_start, absolute_position_end):
    """
    
    Retrieves geometric information from the current ECOTECT model, 
    specifically the distance between two points, starting at 
    (x1, y1, z1) and ending at (x2, y2, z2). The value returned is given 
    in the current units. 
    
    Parameter(s)
    This property takes the following parameters.
    
    absolute_position_start 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a starting point in 3 dimensional model space.
     
    absolute_position_end 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of an end point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    dist 
    The distance value in the current model units.    
    
    """
    args = p2e._base._util._convert_args_to_string("get.model.distance", 
                                                   absolute_position_start[0],
                                                   absolute_position_start[1], 
                                                   absolute_position_start[2],
                                                   absolute_position_end[0],
                                                   absolute_position_end[1],
                                                   absolute_position_end[2])
    val = p2e._app.Request(args)
    return p2e._base._util._convert_str_to_type(val, float) 

def orientation(absolute_position_start, absolute_position_end):
    """
    
    Retrieves geometric information from the current ECOTECT model, 
    specifically the relative horizontal angle from North of a line starting 
    at (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
    returned is given in a positive clockwise direction. 
    
    Parameter(s)
    This property takes the following parameters.
    
    absolute_position_start 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of a starting point in 3 dimensional model space.
     
    absolute_position_end 
    A list of three values that represent the absolute position in the 
    X, Y and Z axis of an end point in 3 dimensional model space. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    ori 
    The orinetation angle in degrees. 
    
    """
    args = p2e._base._util._convert_args_to_string("get.model.orientation",
                                                       absolute_position_start[0],
                                                       absolute_position_start[1], 
                                                       absolute_position_start[2],
                                                       absolute_position_end[0],
                                                       absolute_position_end[1],
                                                       absolute_position_end[2])
    val = p2e._app.Request(args)
    return p2e._base._util._convert_str_to_type(val, float)  
#===============================================================================
# Main function used for testing
#===============================================================================
      
if __name__ == "__main__":
    pass
    
    print "Tests completed"     
    