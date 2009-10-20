import py2ecotect as p2e


#===========================================================================
# Functions
#===========================================================================

def clear_shading_masks():
    """
    
    Deletes the shading masks list and frees allocated memory. If a future 
    calculation requires shading masks, ECOTECT will attempt to re-load them 
    from the cache file on disk. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("masks.clear")
    p2e.doc._masks = []    

def load_shading_masks():
    """
    
    Loads the shading mask list. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("masks.load")

def save_shading_masks():
    """
    
    Saves the current shading mask list. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("masks.save")

def num_shading_masks():

    """
    
    Returns the number of shading masks in the current list. If no masks 
    have been loaded, a value of 0 will be returned. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    count 
    The number of shading masks in the list.
    
    """
    val = p2e._app.Request("get.masks.count")
    return p2e._base._util._convert_str_to_type(val, int)
        
#===============================================================================
# 
#===============================================================================
#------------------------------------------------------------------------------ 
def calc_shading(calc_type="percentage", cumulative=True, start_day=1, stop_day=365, start_time=0.00, stop_time=23.99):
    """
    
    Calculates the shading mask for the currently selected object. The 
    command suffix refers to the shading information to be calculated, as 
    outlined in the following Available Shading Calculations table. The 
    optional parameters only apply to solar stress calculations. If not 
    included, these default to the full year (1-365) and all day (0-24). 

    Parameter(s)
    This command takes the following parameters.
    
    calc_type
    Can be percentage, total, diffuse or direct. Default is 'percentage'.
    
    cumulative 
    A boolean value determining if solar radiation should show cumulative 
    annual results rather than hourly total stress values. Default is True. 
    
    start_day 
    The starting date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 1.
    
    stop_day 
    The end date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 365.
    
    start_time 
    Determines the starting time for the calculation. This is a decimal 
    value between 0.00 and 23.99. Default is 0.00.
    
    stop_time 
    Determines the end time for the calculation. This is a decimal value 
    between 0.00 and 23.99. Default is 23.99.

    """
    p2e.app.view.redraw()
    arg_str = p2e._base._util._convert_args_to_string("calc.shading." + 
                                                  calc_type,cumulative, 
                                                  start_day, stop_day, 
                                                  start_time, stop_time)
    p2e._app.Exec(arg_str)

def calc_shading_percentage(cumulative=True, start_day=1, stop_day=365, start_time=0.00, stop_time=23.99):
    """
    
    Calculates the shading mask for the currently selected object. In this case, 
    the shading information to be calculated is the percentage. The 
    optional parameters only apply to solar stress calculations. If not 
    included, these default to the full year (1-365) and all day (0-24). 

    Parameter(s)
    This command takes the following parameters.
    
    cumulative 
    A boolean value determining if solar radiation should show cumulative 
    annual results rather than hourly total stress values. Default is True. 
    
    start_day 
    The starting date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 1.
    
    stop_day 
    The end date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 365.
    
    start_time 
    Determines the starting time for the calculation. This is a decimal 
    value between 0.00 and 23.99. Default is 0.00.
    
    stop_time 
    Determines the end time for the calculation. This is a decimal value 
    between 0.00 and 23.99. Default is 23.99.

    """    
    calc_shading("percentage", cumulative, start_day, stop_day, start_time, stop_time)

def calc_shading_total(cumulative=True, start_day=1, stop_day=365, start_time=0.00, stop_time=23.99):
    """
    
    Calculates the shading mask for the currently selected object. In this case, 
    the shading information to be calculated is the total shading. The 
    optional parameters only apply to solar stress calculations. If not 
    included, these default to the full year (1-365) and all day (0-24). 

    Parameter(s)
    This command takes the following parameters.
    
    cumulative 
    A boolean value determining if solar radiation should show cumulative 
    annual results rather than hourly total stress values. Default is True. 
    
    start_day 
    The starting date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 1.
    
    stop_day 
    The end date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 365.
    
    start_time 
    Determines the starting time for the calculation. This is a decimal 
    value between 0.00 and 23.99. Default is 0.00.
    
    stop_time 
    Determines the end time for the calculation. This is a decimal value 
    between 0.00 and 23.99. Default is 23.99.

    """     
    calc_shading("total", cumulative, start_day, stop_day, start_time, stop_time)

def calc_shading_diffuse(cumulative=True, start_day=1, stop_day=365, start_time=0.00, stop_time=23.99):
    """
    
    Calculates the shading mask for the currently selected object. In this case, 
    the shading information to be calculated is the diffuse incident solar radiation. The 
    optional parameters only apply to solar stress calculations. If not 
    included, these default to the full year (1-365) and all day (0-24). 

    Parameter(s)
    This command takes the following parameters.
    
    cumulative 
    A boolean value determining if solar radiation should show cumulative 
    annual results rather than hourly total stress values. Default is True. 
    
    start_day 
    The starting date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 1.
    
    stop_day 
    The end date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 365.
    
    start_time 
    Determines the starting time for the calculation. This is a decimal 
    value between 0.00 and 23.99. Default is 0.00.
    
    stop_time 
    Determines the end time for the calculation. This is a decimal value 
    between 0.00 and 23.99. Default is 23.99.

    """     
    calc_shading("diffuse", cumulative, start_day, stop_day, start_time, stop_time)

def calc_shading_direct(cumulative=True, start_day=1, stop_day=365, start_time=0.00, stop_time=23.99):
    """
    
    Calculates the shading mask for the currently selected object. In this case, 
    the shading information to be calculated is the direct incident solar radiation. The 
    optional parameters only apply to solar stress calculations. If not 
    included, these default to the full year (1-365) and all day (0-24). 

    Parameter(s)
    This command takes the following parameters.
    
    cumulative 
    A boolean value determining if solar radiation should show cumulative 
    annual results rather than hourly total stress values. Default is True. 
    
    start_day 
    The starting date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 1.
    
    stop_day 
    The end date for the calculation. This is a julian date, a number 
    between 1 and 365. Default is 365.
    
    start_time 
    Determines the starting time for the calculation. This is a decimal 
    value between 0.00 and 23.99. Default is 0.00.
    
    stop_time 
    Determines the end time for the calculation. This is a decimal value 
    between 0.00 and 23.99. Default is 23.99.

    """ 
    calc_shading("direct", cumulative, start_day, stop_day, start_time, stop_time)
#===============================================================================
# 
#===============================================================================
#------------------------------------------------------------------------------ 
def set_overshadowing_precision(precision):
    """
    
    Sets the accuracy of the overshadowing calculation. This calculation is 
    done by dividing each surface into a grid, generating a random point 
    within each grid square and then checking the in-shade status of each 
    point. 

    Parameter(s)
    This property takes the following parameters.
    
    precision 
    An integer value or token corresponding to the following Shading 
    Accuracy table. 
    
    Relevant Data Table(s)
    
    Shading Precision 
    Token Value Description 
    full 0 Break object into 25x25 grid. 
    high 1 Break object into 10x10 grid. 
    medium 2 Break object into 5x5 grid. 
    low 3 Use single point at object centre. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.shading.accuracy", precision)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def shading_mask_angles():
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
    return p2e._base._util._convert_str_to_list(val, float, float)

def set_shading_mask_angles(azi, alt):
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
    arg_str = p2e._base._util._convert_args_to_string("set.shading.angles", azi, alt)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def direct_solar_only_flag():
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
    return p2e._base._util._convert_str_to_type(val, int)
    
def set_direct_solar_only_flag(state):
    """
    
    Sets whether direct sunlight only is to be calclated.. 

    Parameter(s)
    This property takes the following parameters.
    
    state 
    Determines if direct sunlight only is to be calclated. This is a 
    boolean value where 1 or true represents the affirmative and 0 or false 
    the negative. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.shading.directonly", state)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def shading_both_sides_flag():
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
    return p2e._base._util._convert_str_to_type(val, int)

def set_shading_both_sides_flag(state):
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
    arg_str = p2e._base._util._convert_args_to_string("set.shading.bothsides", state)
    p2e._app.Exec(arg_str)



#------------------------------------------------------------------------------ 
def display_shading_rays_flag():
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
    return p2e._base._util._convert_str_to_type(val, int)

def set_display_shading_rays_flag(state):
    """
    
    Sets whether to display shading rays during the shading calculations. 

    Parameter(s)
    This property takes the following parameters.
    
    state 
    Set the display of shading rays. This is a boolean value where 1 or 
    true represents the affirmative and 0 or false the negative. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.shading.rays", state)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def detailed_shading_mask_flag():
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
    val = p2e._app.Request("get.shading.update")#TODO: why 'update' instead of 'state'
    return p2e._base._util._convert_str_to_type(val, int)

def set_detailed_shading_mask_flag(state):
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
    arg_str = p2e._base._util._convert_args_to_string("set.shading.state", state)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
