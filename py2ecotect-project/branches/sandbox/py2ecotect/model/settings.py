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


#From project
#------------------------------------------------------------------------------ 
def altitude():
    """
    
    Retrieves the current altitude of the site, relative to sea level. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    alt 
    The altitude as height above sea level.
    
    """
    val = p2e._app.Request("get.project.altitude")
    return p2e._base._util._convert_str_to_type(val, float)

def set_altitude(alt):
    """
    
    Sets the altitude of the site, above sea level. 

    Parameter(s)
    This property takes the following parameters.
    
    alt 
    The altitude as height above sea level.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.altitude", 
                                                 alt)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def client():
    """
    
    Retrieves the text value used to identify the user who worked on the 
    model or the client for whom the model was created. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    result 
    A text string containing the result. 
    
    """
    val = p2e._app.Request("get.project.client")
    return p2e._base._util._convert_str_to_type(val, str)

def set_client(client):
    """
    
    Sets the text value used to identify the user who worked on the model 
    or the client for whom the model was created. 

    Parameter(s)
    This property takes the following parameters.
    
    client 
    A text string containing the new client name.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.client", 
                                                 client)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def description():
    """
    
    Retrieves the job description of the project. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    result 
    A text string containing the result. 
    
    """
    val = p2e._app.Request("get.project.description")
    return p2e._base._util._convert_str_to_type(val, str)
    
def set_description(description):
    """
    
    Sets the job description of the project. 

    Parameter(s)
    This property takes the following parameters.
    
    description 
    A text string containing the new description.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.description", 
                                                 description)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def latitude():    
    """
    
    Retrieves the latitude of the current model. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    lat 
    The latitude in decimal degrees.
    
    """
    val = p2e._app.Request("get.project.latitude")
    return p2e._base._util._convert_str_to_type(val, float)

def set_latitude(lat):
    """
    
    Sets the latitude of the current model. 

    Parameter(s)
    This property takes the following parameters.
    
    lat 
    The latitude in decimal degrees.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.latitude", lat)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def location():
    """
    
    Retrieves the location of the current model as latitude, longitude and 
    timezone. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    latitude 
    The latitude in decimal degrees. 
    
    longitude 
    The longitude in decimal degrees. 
    
    timezone 
    The timezone as a GMT offset in decimal hours.
    
    """ 
    val = p2e._app.Request("get.project.location")
    return p2e._base._util._convert_str_to_list(val, float, float, float)

def set_location(latitude, longitude, timezone, update = True):
    """
    
    Sets the location of the current model. 

    Parameter(s)
    This property takes the following parameters.
    
    latitude 
    The latitude in decimal degrees. 
    
    longitude 
    The longitude in decimal degrees. 
    
    timezone 
    The timezone as a GMT offset in decimal hours. 
    
    [update] 
    If this optional parameter is set, the main window will be updated with
    a redrawn view and sunpath. This is a boolean value where 1 or true
    represents the affirmative and 0 or false the negative.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.location", 
                                                 latitude, longitude, 
                                                 timezone, update)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def location_name():
    """
    
    Retrieves the name of the current model location. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    name 
    A text string representing the name of the location.
    
    """
    val = p2e._app.Request("get.project.locname")
    return p2e._base._util._convert_str_to_type(val, str)

def set_location_name(name):
    """
    
    Sets the name of the current model location. 

    Parameter(s)
    This property takes the following parameters.
    
    name 
    A text string representing the new name of the location.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.locname", 
                                                 name)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def longitude():
    """
    
    Retrieves the longitude of the current model. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    lng 
    The longitude in decimal degrees.
    
    """
    val = p2e._app.Request("get.project.longitude")
    return p2e._base._util._convert_str_to_type(val, float)
      
def set_longitude(lng):
    """
    
    Sets the longitude of the current model. 

    Parameter(s)
    This property takes the following parameters.
    
    lng 
    The longitude in decimal degrees.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.longitude", 
                                                 lng)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def north():
    """
    
    Retrieves the North angle offset. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    angle 
    The angle in degrees between true north and the positive Y axis.
    
    """
    val = p2e._app.Request("get.project.north")
    return p2e._base._util._convert_str_to_type(val, float)

def set_north(north):
    """
    
    Sets the North angle offset. 

    Parameter(s)
    This property takes the following parameters.
    
    north 
    The angle in degrees between true north and the positive Y axis.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.north", 
                                                 north)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def job_reference(): 
    """
    
    Retrieves the job reference number for the project. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    result 
    A text string containing the result.
    
    """
    val = p2e._app.Request("get.project.reference")
    return p2e._base._util._convert_str_to_type(val, str)

def set_job_reference(description):
    """
    
    Sets the job reference number of the project. 

    Parameter(s)
    This property takes the following parameters.
    
    description 
    A text string containing the new reference number. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.reference", 
                                                 description)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def terrain():
    """
    
    Retrieves the type of terrain the project site is located on. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    terrain 
    An integer value from following Terrain Types table. 
    
    Relevant Data Table(s)
    
    Terrain Types 
    Token Value Description 
    exposed 0 In a location exposed to the wind  
    rural 1 In a rural setting (reasonably open)  
    suburban 2 In a suburban setting (reasoanbly protected)  
    urban 3 In a dense urban setting (very protected)  

    """
    val = p2e._app.Request("get.project.terrain")
    return p2e._base._util._convert_str_to_type(val, int)

def set_terrain(terrain):
    """
    
    Sets the type of terrain the project site is located on. 

    Parameter(s)
    This property takes the following parameters.
    
    terrain 
    The terrain type according to the following Terrain Types table. This 
    can be set as a token or a value. 
    
    Relevant Data Table(s)
    
    Terrain Types 
    Token Value Description 
    exposed 0 In a location exposed to the wind  
    rural 1 In a rural setting (reasonably open)  
    suburban 2 In a suburban setting (reasoanbly protected)  
    urban 3 In a dense urban setting (very protected)  
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.terrain", 
                                                 terrain)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def timezone():
    """
    
    Retrieves the timezone for the model location. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    tz 
    The time zone as an offset from GMT in decimal hours. 
    
    """
    val = p2e._app.Request("get.project.timezone")
    return p2e._base._util._convert_str_to_type(val, float)
    
def set_timezone(tz):
    """
    
    Sets the timezone of the model's location. 

    Parameter(s)
    This property takes the following parameters.
    
    tz 
    A GMT offset value in +/- decimal hours.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.timezone", 
                                                  tz)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def project_title():
    """
    
    Retrieves the title for the project. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    result 
    A text string containing the result. 
    
    """
    val = p2e._app.Request("get.project.title")
    return p2e._base._util._convert_str_to_type(val, str)

def set_project_title(description):
    """
    
    Sets the title of the project. 

    Parameter(s)
    This property takes the following parameters.
    
    description 
    A text string containing the new title.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.title", 
                                                 description)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def building_type():
    """
    
    Retrieves the building type. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    type 
    An integer value corresponding to the following Project Types table. 
    
    Relevant Data Table(s)
    
    Project Types 
    Value Description 
    0 Domestic Dwelling 
    1 Commercial Residential 
    2 Office/Shop/Assembly 
    3 Industrial or Storage 
    5 Other 
    
    """
    val = p2e._app.Request("get.project.type")
    return p2e._base._util._convert_str_to_type(val, int)

def set_building_type(type):
    """
    
    Sets the building type. 

    Parameter(s)
    This property takes the following parameters.
    
    type 
    An integer value corresponding to the following Project Types table. 
    
    Relevant Data Table(s)
    
    Project Types 
    Value Description 
    0 Domestic Dwelling 
    1 Commercial Residential 
    2 Office/Shop/Assembly 
    3 Industrial or Storage 
    5 Other 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.type", type)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 



    