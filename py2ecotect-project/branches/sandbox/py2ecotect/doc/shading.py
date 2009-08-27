import py2ecotect as p2e

#===========================================================================
# Properties
#===========================================================================
def set_accuracy(accuracy):
    """
    
    Sets the accuracy of the overshadowing calculation. This calculation is 
    done by dividing each surface into a grid, generating a random point 
    within each grid square and then checking the in-shade status of each 
    point. 

    Parameter(s)
    This property takes the following parameters.
    
    accuracy 
    An integer value or token corresponding to the following Shading 
    Accuracy table. 
    
    Relevant Data Table(s)
    
    Shading Accuracy 
    Token Value Description 
    full 0 Break object into 25x25 grid. 
    high 1 Break object into 10x10 grid. 
    medium 2 Break object into 5x5 grid. 
    low 3 Use single point at object centre. 
    
    """
    arg_str = p2e._util._convert_args_to_string("set.shading.accuracy", 
                                                 accuracy)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def get_angles():
    """
    
    Retrieves the currently set angles of azimuth and altitude for shading 
    mask calculations, which determines the resolution of the sky dome 
    sections used. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    azi 
    The azimuth angle in degrees. 
    
    alt 
    The altitude angle in degrees. 
    
    """
    val = p2e._app.Request("get.shading.angles")
    return p2e._util._convert_str_to_list(val, float, float)
#------------------------------------------------------------------------------ 
def set_angles(azi, alt):
    """
    
    Sets the angles of azimuth and altitude for shading mask 
    calculations which determine the resolutions of the sky dome 
    sections used. 

    Parameter(s)
    This property takes the following parameters.
    
    azi 
    The azimuth value in degrees. 
    
    alt 
    The altitude value in degrees.
    
    """
    arg_str = p2e._util._convert_args_to_string("set.shading.angles", 
                                                 azi, alt)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def get_both_sides():
    """
    
    Returns a boolean value indicating if shading is calculated for both 
    sides of the selected object 1, or only the direction of the surface 
    normal 0. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    A boolean value determining if shading is calculated for both sides for 
    the selected object. This is a boolean value where 1 is set and 0 means 
    unset.
    
    """
    val = p2e._app.Request("get.shading.bothsides")
    return p2e._util._convert_str_to_type(val, int)

def set_both_sides(state):
    """
    
    Sets whether shading is calculated over both sides of the selected 
    object or only the direction of the surface normal. 

    Parameter(s)
    This property takes the following parameters.
    
    state 
    Determines if shading is calculated for both sides for the selected 
    object. This is a boolean value where 1 or true represents the 
    affirmative and 0 or false the negative. 
    
    """
    arg_str = p2e._util._convert_args_to_string("set.shading.bothsides", 
                                                 state)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def get_sky_components():
    """
    
    Returns the three sky components calculated from the current shading 
    mask. The first two values are the fraction of the sky 
    illuminance/radiation visible to the selected object for which the mask 
    was calculated, under CIE overcast and uniform sky conditions. The 
    third result is only valid for vertical surfaces and is the Vertical 
    Sky Component as defined by the Building Research Establishment. These 
    are the values displayed within the bottom right corner of the SunPath 
    diagram when the shading mask is displayed.

    If the shading calculation has not yet been performed (see the 
    calc.shading.percentage method), this method will carry one out for the 
    current object. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    overcast 
    A decimal value containing the overcast sky component. 
    
    uniform 
    A decimal value containing the uniform sky component. 
    
    vertical 
    A decimal value containing the vertical sky component.
    
    """
    val = p2e._app.Request("get.shading.components")
    return p2e._util._convert_str_to_list(val, float, float, float)
#------------------------------------------------------------------------------ 
def get_diffuse():
    """
    
    Returns the diffuse solar radiation component as a single decimal value 
    in Watts per square metre. This is only valid after a shading 
    calculation has been performed (see the calc.shading.percentage method 
    and set.model.time properties for mroe information). 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the current diffuse solar component.
    
    """
    val = p2e._app.Request("get.shading.diffuse")
    return p2e._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def get_direct():
    """
    
    Returns the current direct solar radiation component as a single 
    decimal value in Watts per square metre. This is only valid after a 
    shading calculation has been performed (see the calc.shading.percentage 
    method and set.model.time properties for more information). 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the current direct solar component.
    
    """
    val = p2e._app.Request("get.shading.direct")
    return p2e._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def get_direct_only():
    """
    
    Returns a boolean value indicating if direct sunlight only is to be 
    calclated. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    A boolean value determining if direct sunlight only is to be calclated. 
    This is a boolean value where 1 is set and 0 means unset. 

    """
    val = p2e._app.Request("get.shading.directonly")
    return p2e._util._convert_str_to_type(val, int)
    
def set_direct_only(state):
    """
    
    Sets whether direct sunlight only is to be calclated.. 

    Parameter(s)
    This property takes the following parameters.
    
    state 
    Determines if direct sunlight only is to be calclated. This is a 
    boolean value where 1 or true represents the affirmative and 0 or false 
    the negative. 
    
    """
    arg_str = p2e._util._convert_args_to_string("set.shading.directonly", 
                                                 state)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def get_percentage():
    """
    
    Returns the percentage-in-shade of the selected object as a single 
    decimal percentage value, using the current model date and time 
    settings.

    This is only valid after a shading calculation has been performed (see 
    the calc.shading.percentage method and set.model.time properties for 
    more information). If a negative value is returned, then the 
    set.shading.bothsides option has been used and the point is behind the 
    surface. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the shading value. 
    
    """
    val = p2e._app.Request("get.shading.percentage")
    return p2e._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def get_percentage_angle(azi, alt):
    """
    
    Returns the percentage-in-shade of the selected object as a single 
    decimal percentage value. Note that this is only valid after a shading 
    calculation has been performed (see the calc.shading.percentage method 
    and set.model.time properties for more information).

    If a negative value is returned, then the set.shading.bothsides option 
    has been used and the point is behind the surface. 
    
    Parameter(s)
    This property takes the following parameters.
    
    azi 
    The azimuth (-180 deg to 180 deg) angle representing, together with the 
    altitude angle, a point in the sky from which to retrieve the value.
    
    To retrieve the sun position at any time, use the get.model.sunangles 
    command. 
    
    alt 
    The altitude (0 deg to 90 deg) angle representing, together with the azimuth 
    angle, a point in the sky from which to retrieve the value.
    
    To retrieve the sun position at any time, use the get.model.sunangles 
    command. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the shading value. 
    
    """
    arg_str = p2e._util._convert_args_to_string("get.shading.percentage.angle", 
                                                  azi, alt)
    val = p2e._app.Request(arg_str)
    return p2e._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def get_percentage_date_time(day, time):
    """
    
    Returns the percentage-in-shade of the selected object as a single 
    decimal percentage value. This is only valid after a shading calculation 
    has been performed (see the calc.shading.percentage method and 
    set.model.time properties for more information).

    If a negative value is returned, then the set.shading.bothsides option 
    has been used and the point is behind the surface. 
    
    Parameter(s)
    This property takes the following parameters.
    
    day 
    The day of the year from which to return the percentage (1 to 365). 
    
    time 
    The time of the day from which to return the percentage (0 to 23). 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the shading value
    
    """
    arg_str = p2e._util._convert_args_to_string("get.shading.percentage.datetime", 
                                                  day, time)
    val = p2e._app.Request(arg_str)
    return p2e._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def get_percentage_index(x, y):
    """
    
    Returns the percentage-in-shade of the selected object as a single 
    decimal value. Note that this is only valid after a shading calculation 
    has been performed (see the calc.shading.percentage method and 
    set.model.time properties for more information).

    If a negative value is returned, then the set.shading.bothsides option 
    has been used and the point is behind the surface. 
    
    Parameter(s)
    This property takes the following parameters.
    
    x 
    The X index of the shading table, where X is the azimuth angle 
    increment set in the set.shading.angles property. 
    
    y 
    The Y index of the shading table, where Y is the altitude angle 
    increment set in the set.shading.angles property. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the shading value.
    
    """
    arg_str = p2e._util._convert_args_to_string("get.shading.percentage.index", 
                                                  x, y)
    val = p2e._app.Request(arg_str)
    return p2e._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def get_range(fromDay, toDay):
    """
    
    Returns the total direct and diffuse incident solar radiation on the 
    object for which the current shading mask has been calculated. Both are 
    returned as single decimal values in Watts per square metre. A third 
    value is also returned, being a count of the number of hours over which 
    the direct and diffuse values were generated. 

    Parameter(s)
    This property takes the following parameters.
    
    fromDay 
    A value representing the Julian date when the calculation will begin, 
    given as an integer from 1 to 365. 
    
    toDay 
    A value representing the Julian date when the calculation will end, 
    given as an integer from 1 to 365. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    totalDirect 
    A decimal value containing the totel direct solar component. 
    
    totalDiffuse 
    A decimal value containing the total diffuse solar component. 
    
    totalHours 
    A decimal value containing the total sunlight hours. 

    """
    val = p2e._app.Request("get.shading.range")
    return p2e._util._convert_str_to_list(val, float, float, float)
#------------------------------------------------------------------------------ 
def get_rays():
    """
    
    Retrieves the current setting of whether to display shading rays during 
    the shading calculations. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    A boolean value determining if rays are shown or not. This is a boolean 
    value where 1 is set and 0 means unset. 
    
    """
    val = p2e._app.Request("get.shading.rays")
    return p2e._util._convert_str_to_type(val, int)

def set_rays(state):
    """
    
    Sets whether to display shading rays during the shading calculations. 

    Parameter(s)
    This property takes the following parameters.
    
    state 
    Set the display of shading rays. This is a boolean value where 1 or 
    true represents the affirmative and 0 or false the negative. 
    
    """
    arg_str = p2e._util._convert_args_to_string("set.shading.rays", 
                                                 state)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def sky_component():
    """
    
    Returns the percentage of CIE Overcast Sky illumination visible from 
    the selected surface. This is time-independent and only valid after a 
    shading calculation has been performed (see the calc.shading.percentage 
    method). 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    SC 
    A decimal value containing the sky component.
    
    """
    val = p2e._app.Request("get.shading.skycomponent")
    return p2e._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def get_update():
    """
    
    Returns a boolean value indicating the status of an object's shading 
    mask. A value of 0 indicates the object is using its own mid-accuracy 
    mask. A value of 1 indicates the object is using a detailed shading 
    mask calculated using the calc.shading.percentage command. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    A boolean value determining what mask is used. This is a boolean value 
    where 1 means a detailed mask and 0 it's own mask.
    
    """
    val = p2e._app.Request("get.shading.update")
    return p2e._util._convert_str_to_type(val, int)

def set_update(state):
    """
    
    Sets which shading mask to use for the selected object - it's own 
    mid-accuracy mask, or a detailed shading mask calculated using the 
    calc.shading.percentage command. 

    Parameter(s)
    This property takes the following parameters.
    
    state 
    This is a boolean value where 1 or true represents the affirmative and 
    0 or false the negative. If true, the detailed shading mask overrides 
    the selected object's own shading mask.
    
    """
    arg_str = p2e._util._convert_args_to_string("set.shading.state", 
                                                 state)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 

    
