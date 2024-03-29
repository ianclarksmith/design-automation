import py2ecotect as p2e

#===========================================================================
# Functions
#===========================================================================
def calc_acoustic_response(calc_type, frequency):
    """
    
    Calculates the acoustic response based on acoustic rays already 
    generated using the rays object. 

    Parameter(s)
    This command takes the following parameters.
    
    calc_type 
    This parameter is either 0 for a 'Estimated Reverberation' calculation 
    or 1 for a calculation based on 'Existing Rays/Particles'. 
    
    frequency 
    The frequency parameter refers to the numeric values given in the 
    following 
    
    Available Acoustic Frequencies table. 
    
    Relevant Data Table(s)
    
    Available Acoustic 
    Frequencies 
    Value Frequency 
    0 63 Hz 
    1 125 Hz 
    2 250 Hz 
    3 500 Hz 
    4 1000 Hz 
    5 2000 Hz 
    6 4000 Hz 
    7 8000 Hz 
    8 16000 Hz 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("calc.acousticresponse", 
                                                  calc_type, frequency)
    p2e._app.Exec(arg_str)  
    
def calc_acoustic_response_reverberation(frequency):
    calc_acoustic_response(0, frequency)
def calc_acoustic_response_rays_particles(frequency):
    calc_acoustic_response(1, frequency)   
#------------------------------------------------------------------------------ 
def calc_comfort():
    """
    
    Use this command to (re)calculate mean radiant temperatures and thermal 
    comfort values if you have an a visible analysis grid set up within a 
    valid thermal model. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("calc.comfort")
#------------------------------------------------------------------------------     
def calc_insolation(calc_type, target, select_3d, accumulation, metric = None):
    """
    
    Calculates incident solar radiation levels (insolation) over either the 
    current analysis grid or objects within the model. 

    Parameter(s)
    This command takes the following parameters.
    
    calc_type 
    The type parameter sets the type of calculation to be performed, as 
    shown in the following insolation types table. 
    
    target 
    [grid|objects] This parameter determines whether the insolation 
    calculation is performed over the analysis grid or over objects. It can 
    only have either the value 'grid' or 'objects'. Any other value will be 
    intepreted as 'grid'. 
    
    select3D 
    When calculating over the analysis grid, setting this boolean parameter 
    to 'true' or 1 calculates insolation for the entire 3D volume of the 
    grid. Setting it to 'false' or 0 means just the current 2D slice. When 
    calculating over objects, setting this parameter to 'true' or 1 
    calculates insolation only for selected objects in the model. Setting it 
    to 'false' or 0 means all visible objects. 
    
    accumulation 
    Determines how to tabulate the results of the insolation calculation, 
    based on values in the following solar accumulation table. 
    
    [metric] 
    This parameter must be given if the type parameter has been set to 
    reference. It determines the type of value to store as the 'before' 
    reference, based on the following Insolation Metrics table. 
    
    Relevant Data Table(s)
    
    Available Insolation Calculations 
    Token Value Description 
    incidence 0 Incident Solar Radiation on Points & Surfaces 
    absorption 1 Solar Absorbtion/Transmission of Object Surfaces 
    skyfactor 2 Sky Factor & Photosynthetically Active Radiation 
    shading 3 Shading, Overshadowing and Sunlight Hours 
    reference 4 COMPARE VALUE- Reference (Before) 
    comparison 5 COMPARE VALUE- Comparison (After) 
    
    Available Insolation Accumulations 
    Token Value Description 
    cumulative 0 Cumulative 
    daily 1 Average Daily 
    hourly 2 Average Hourly 
    peak 3 Peak 
    
    Available Insolation Metrics 
    Token Value Description 
    incident 0 Total Incident Radiation 
    absorbed 1 Total Absorbed Radiation 
    transmitted 2 Total Transmitted Radiation 
    photosynthetic 3 Photosynth. Active Radiation 
    shading 4 Avg Shading Percentage 
    sunlight 5 Total Sunlight Hours 
    sky 6 Total Visible Sky  
    
    """
    
    if type == "reference" and  metric is None:
        return
    else:
        arg_str = p2e._base._util._convert_args_to_string("calc.insolation", 
                                                      target, calc_type, select_3d, 
                                                     accumulation, metric)
        p2e._app.Exec(arg_str)
    
def calc_insolation_incidence(target, select_3d, accumulation):
    calc_insolation('incidence', target, select_3d, accumulation, metric = None)
def calc_insolation_absorption(target, select_3d, accumulation):
    calc_insolation('absorption', target, select_3d, accumulation, metric = None)
def calc_insolation_skyfactor(target, select_3d, accumulation):
    calc_insolation('skyfactor', target, select_3d, accumulation, metric = None)
def calc_insolation_shading(target, select_3d, accumulation):
    calc_insolation('shading', target, select_3d, accumulation, metric = None)
def calc_insolation_reference(target, select_3d, accumulation, metric):
    calc_insolation('reference', target, select_3d, accumulation, metric)
def calc_insolation_comparison(target, select_3d, accumulation):
    calc_insolation('comparison', target, select_3d, accumulation, metric = None)
#------------------------------------------------------------------------------     
def calc_solar_exposure(calc_type, shading, ground, direct):
    """
    
    Calculates solar exposure within the model. 

    Parameter(s)
    This command takes the following parameters.
    
    calc_type 
    The type parameter sets the type of resource calculation to be performed, 
    as shown in the following Types of Solar Calculation Types table. 
    
    shading 
    This parameter sets the type of accuracy of shading calculations to be 
    performed, as shown in the following Solar Shading Accuracy table. 
    
    ground 
    Determines whether ground reflections are considered in the calclation. 
    This is a boolean value where 1 or true represents the affirmative and 0 
    or false the negative. 
    
    direct 
    Determines whether only direct light is included in the solar 
    calculation. This is a boolean value where 1 or true represents the 
    affirmative and 0 or false the negative. 
    
    Relevant Data Table(s)
    
    Available Types of Solar 
    Calculation 
    Token Description 
    day Single day radiation. 
    average Average daily radiation. 
    total Total monthly radiation. 
    full Full hourly radiation. 
    
    
    Accuracy of Solar Calculations 
    Value Description 
    0 Full - break object into 25x25 grid. 
    1 High - break object into 10x10 grid. 
    2 Medium - break object into 5x5 grid. 
    3 Low - use single point at object centre. 

    """
    try:
        arg_str = p2e._base._util._convert_args_to_string("calc.solar", 
                                                      calc_type, shading, 
                                                      ground, direct)
        p2e._app.Exec(arg_str)
    except:
        print "exception occured"

def calc_solar_exposure_one_day(shading, ground, direct):
    calc_solar_exposure("day", shading, ground, direct)
def calc_solar_exposure_average_daily(shading, ground, direct):
    calc_solar_exposure("average", shading, ground, direct)
def calc_solar_exposure_total_monthly(shading, ground, direct):
    calc_solar_exposure("total", shading, ground, direct)
def calc_solar_exposure_full_hourly(shading, ground, direct):
    calc_solar_exposure("full", shading, ground, direct)
#------------------------------------------------------------------------------     
def calc_lighting(calc_type, target, select3D, comparison = 0):
    """
    
    Calculates daylight factors and lighting levels over either the current 
    analysis grid or POINT objects within the model. 

    Parameter(s)
    This command takes the following parameters.
    
    calc_type 
    The type parameter sets the type of calculation to be performed, as 
    shown in the following Lighting Types table. 
    
    target 
    [grid|points] This parameter determines whether the lighting calculation 
    is performed over the analysis grid or over POINT objects. It can only 
    have  either the value 'grid' or 'point'. Any other value will be 
    intepreted as grid'. 
    
    select3D 
    When calculating over the analysis grid, setting this boolean parameter 
    to 'true' or 1 calculates lighting for the entire 3D volume of the grid. 
    Setting it to 'false' or 0 means just the current 2D slice. When 
    calculating over objects, setting this parameter to 'true' or 1 
    calculates lighting only for selected POINTs in the model. Setting it to 
    'false' or 0 means all visible POINTs. 
    
    [comparison] 
    The comparison parameter is optional and allows you to compare before 
    and after results, as outlined in the Lighting Comparison following 
    table. 
    
    Relevant Data Table(s)
    
    Available Lighting Calculations 
    Token Value Description 
    daylight 0 Natural Light - Daylight Factors & Levels 
    overall 1 Overall Light - Daylight and Electric Levels 
    compare 2 Comparison against previous calculation 
    
    
    Available Lighting Comparisons 
    Value Description 
    0 Normal: Store Calculated Values 
    1 Compare: After / Before - as a percentage (%) 
    2 Compare: Before / After - as a percentage (%) 
    3 Compare: After - Before 
    4 Compare: Before - After 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("calc.lighting", target, 
                                                  calc_type, select3D, 
                                                  comparison)
    p2e._app.Exec(arg_str)
    
def calc_lighting_daylight(target, select3D):
    calc_lighting('daylight', target, select3D, comparison = 0)
def calc_lighting_overall(target, select3D):
    calc_lighting('overall', target, select3D, comparison = 0)
def calc_lighting_compare(target, select3D, comparison = 0):
    calc_lighting('compare', target, select3D, comparison = 0)
#------------------------------------------------------------------------------   
def calc_resource_consumption(calc_type):
    """
    
    Calculates resource consumption within the model. 

    Parameter(s)
    This command takes the following parameters.
    
    calc_type 
    The type parameter sets the type of resource calculation to be 
    performed, as shown in the following resource calculation types table. 
    
    Relevant Data Table(s)
    
    Available Resource Calculations 
    Token Description 
    energy Daily Energy Use 
    load Daily Load Matching 
    solar Hourly Solar Collection 
    electricity Hourly Electricity Use 
    water Hourly Water Use 
    waste Hourly Waste Water 
    fueloil Hourly Fuel Oil Use 
    kerosene Hourly Kerosene Use 
    natgas Hourly Nat. Gas Use 
    lpgas Hourly LP Gas Use 
    coal Hourly Coal Use 

    """
    arg_str = p2e._base._util._convert_args_to_string("calc.resources", calc_type)
    p2e._app.Exec(arg_str)
def calc_resource_consumption_energy():
    calc_resource_consumption("energy")
def calc_resource_consumption_load():
    calc_resource_consumption("load")    
def calc_resource_consumption_solar():
    calc_resource_consumption("solar")    
def calc_resource_consumption_electricity():
    calc_resource_consumption("electricity")
def calc_resource_consumption_water():
    calc_resource_consumption("water")
def calc_resource_consumption_waste():
    calc_resource_consumption("waste")    
def calc_resource_consumption_fuel_oil():
    calc_resource_consumption("fueloil")    
def calc_resource_consumption_kerosene():
    calc_resource_consumption("kerosene") 
def calc_resource_consumption_nat_gas():
    calc_resource_consumption("natgas")
def calc_resource_consumption_lp_gas():
    calc_resource_consumption("lpgas")  
def calc_resource_consumption_coal():
    calc_resource_consumption("coal")  
#------------------------------------------------------------------------------     
def calc_thermal(calc_type, zone=0):
    """
    
    Use these methods to invoke thermal calculations. The command suffixes 
    refer to the different thermal calculation types as shown in the 
    following Available Thermal Calculations table. Calculation types relate 
    directly to the Thermal Calculation selector in the Thermal Analysis tab 
    of the Graphical Results dialog. 

    Parameter(s)
    This command takes the following parameters.
    
    calc_type
    Refer to  the thermal calculations table below
    
    [zone] 
    This optional parameter can be used to specify the zero-based index of a 
    zone to use for the calculation. This paramater only applies to the 
    .gains and ...gains calculations, and relates directly to the Highlight 
    Zone selector (however the zone index is always given as the absolute 
    index in the entire zone list). 
    
    Relevant Data Table(s)
    
    Available Thermal Calculations 
    Token Description 
    temperatures Hourly temperatures for current day. 
    gains Hourly heat gains for current day. 
    loads Monthly heating and cooling loads. 
    distribution Temperature distribution. 
    fabricgains Average monthly-hourly fabric heat flow. 
    indirectgains Average monthly-hourly indirect solar gains. 
    directgains Average monthly-hourly direct solar gains 
    ventilationgains Average monthly-hourly ventilation gains. 
    internalgains Average monthly-hourly internal gains. 
    zonalgains Average monthly-hourly inter-zonal gains. 
    totalgains Average monthly-hourly total space gains. 
    passivegains Passive gains breakdown. 
    adaptability Passive adaptibility index. 
    comparison Temperature/gains comparison . 
    degreedays Monthly degree days. 

    """
    arg_str = p2e._base._util._convert_args_to_string("calc.thermal." + 
                                                  calc_type, zone)
    p2e._app.Exec(arg_str)
    
def calc_thermal_temperatures(zone=0):
    calc_thermal("temperatures", zone)
def calc_thermal_gains(zone=0):
    calc_thermal("gains", zone)
def calc_thermal_loads(zone=0):
    calc_thermal("loads", zone)
def calc_thermal_distribution(zone=0):
    calc_thermal("distribution", zone)
def calc_thermal_fabric_gains(zone=0):
    calc_thermal("fabricgains", zone)
def calc_thermal_indirect_gains(zone=0):
    calc_thermal("indirectgains", zone)
def calc_thermal_direct_gains(zone=0):
    calc_thermal("directgains", zone)
def calc_thermal_ventilation_gains(zone=0):
    calc_thermal("ventilationgains", zone)   
def calc_thermal_internal_gains(zone=0):
    calc_thermal("internalgains", zone)
def calc_thermal_zonal_gains(zone=0):
    calc_thermal("zonalgains", zone)
def calc_thermal_total_gains(zone=0):
    calc_thermal("totalgains", zone)
def calc_thermal_passive_gains(zone=0):
    calc_thermal("passivegains", zone)
def calc_thermal_adaptability(zone=0):
    calc_thermal("adaptability", zone)
def calc_thermal_comparison(zone=0):
    calc_thermal("comparison", zone)
def calc_thermal_degree_days(zone=0):
    calc_thermal("degreedays", zone)

    
#------------------------------------------------------------------------------
def update_adjacencies(sample_size, shading, ignore = ""):
    """
    
    Calculates inter-zonal adjacencies for all currently visible zones.

    Parameter(s)
    This command takes the following parameters.
    
    [ignore] 
    If this optional string parameter is given instead of any others, the 
    requirement to recalculate inter-zonal adjacencies will be ignored. 
    This may be useful when you perform a zone-related operation that you 
    know will not affect overshadowing or the thermal validity of spaces. 
    
    sample_size 
    To deal with geometry of any level of complexity, ECOTECT samples 
    surfaces using pseudo-random points, each located somewhere within a 
    regular grid. Use this parameter to set the size of this grid for each 
    object in the default dimension units. Smaller sampling grid values will 
    result in more accurate adjacency calculations, but will obviously take 
    much longer to generate. 
    
    shading 
    [true|false] Set this parameter to 'true' to have the calculation 
    generate shading masks for each object. When set to 'false', no masks 
    are calculated and shading is ignored.
    
    """
    if ignore.lower() == "ignore":
        arg_str = p2e._base._util._convert_args_to_string("calc.adjacencies" , 
                                                    ignore)
    else:
        arg_str = p2e._base._util._convert_args_to_string("calc.adjacencies" , 
                                                    sample_size, shading)
    p2e._app.Exec(arg_str)

def update_volumes():
    """
    
    Calculates zone volumes for all currently visible zones. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("calc.volumes")
#------------------------------------------------------------------------------
#===========================================================================
# Getters and Setters
#===========================================================================
def dates():
    """
    
    Retrieves the range of dates used for calculations. Up to three values 
    are returned, being the startDay, the stopDay, and the optional 
    [incDay], which determines if the start and stop days are inclusive of 
    the date range. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    startDay 
    The starting date for the calculation. This is a julian date, being a 
    number between 1 and 365. 
    
    stopDay 
    The end date for the calculation. This is a julian date, being a number 
    between 1 and 365. 
    
    incDay 
    a boolean result (0 or 1) indicating if the start and stop dates are 
    inclusive within the date range. 
    
    """
    val = p2e._app.Request("get.calc.dates")
    return p2e._base._util._convert_str_to_list(val, int, int, bool)

def set_dates(startDay, stopDay, incDay = 1):
    """
    
    Sets the range of dates used for calculations. 

    Parameter(s)
    This property takes the following parameters.
    
    startDay 
    The starting date for the calculation. This is a julian date, a number 
    between 1 and 365. 
    
    stopDay 
    The end date for the calculation. This is a julian date, a number 
    between 1 and 365. 
    
    [incDay] 
    An optional boolean parameter (0 or 1) that determines if the start and 
    stop dates are inclusive of the date range.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.calc.dates", 
                                                  startDay, stopDay, incDay)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def lighting_precision():
    """
    
    Retrieves the level of precision used in lighting calculations for the 
    calc.lighting command. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    precision 
    An integer value corresponding to one of the items in the following 
    Calculation Precision table. 
    
    Relevant Data Table(s)
    
    Available Calculation Precisions 
    Token Value Description 
    full 0 Full Precision 
    veryhigh 1 Very High Precision 
    high 2 High Precision 
    medium 3 Medium Precision 
    low 4 Low Precision 

    """
    val = p2e._app.Request("get.calc.precision")
    return p2e._base._util._convert_str_to_type(val, int)
    
def set_lighting_precision(precision):
    """
    
    Sets the precision of lighting calculations to be used with the calc.
    lighting command. 

    Parameter(s)
    This property takes the following parameters.
    
    precision 
    Determines the calculation accuracy by controlling the number of test 
    rays sprayed from each test point, according to the following table. 
    
    Relevant Data Table(s)
    
    Available Calculation Precisions 
    Token Value Description 
    full 0 Full Precision 
    veryhigh 1 Very High Precision 
    high 2 High Precision 
    medium 3 Medium Precision 
    low 4 Low Precision 

    """
    arg_str = p2e._base._util._convert_args_to_string("set.calc.precision", 
                                                  precision)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def sky():
    """
    
    Retrieves the type of sky illuminance distribution and design sky 
    illuminance level used during daylight calculations. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    sky 
    An integer value or token taken from the following Sky Types table. 
    
    level 
    The design sky illuminance level in Lux. 
    
    Relevant Data Table(s)
    Available Sky Types 
    Token Value Description 
    overcast 0 CIE Overcast Sky 
    uniform 1 CIE Uniform Sky 

    """
    val = p2e._app.Request("get.calc.sky")
    return p2e._base._util._convert_str_to_list(val, int)

def set_sky(sky, level):
    """
    
    Set the type of sky illuminance distribution and design sky 
    illuminance level used during daylight calculations. 

    Parameter(s)
    This property takes the following parameters.
    
    sky 
    An integer value or token taken from the following Sky Types table. 
    
    level 
    The design sky illuminance level in Lux. 
    
    Relevant Data Table(s)
    Available Sky Types 
    Token Value Description 
    overcast 0 CIE Overcast Sky 
    uniform 1 CIE Uniform Sky 

    """
    
    #TODO: check that this works
    arg_str = p2e._base._util._convert_args_to_string("set.material.default", 
                                                  sky, level)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def times():
    """
    
    Retrieves the range of times used for calculations. Up to three values 
    are returned, being the startTime, the stopTime, and the optional 
    [incTime], which determines if the start and stop times are inclusive of 
    the time range. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    startTime 
    The starting time for the calculation. This is a decimal value between 
    0.00 and 23.99. 
    
    stopTime 
    The end time for the calculation. This is a decimal value between 0.00 
    and  23.99. 
    
    [incDay] 
    A boolean value (0 or 1) indicating if the start and stop times are 
    inclusive of the date range.
    
    
    """
    val = p2e._app.Request("get.calc.times")
    return p2e._base._util._convert_str_to_list(val, float, float, bool)

def set_times(startDay, stopDay, incDay = 1):
    """
    
    Sets the range of times used for calculations. 

    Parameter(s)
    This property takes the following parameters.
    
    startTime 
    Determines the starting time for the calculation. This is a decimal 
    value between 0.00 and 23.99. 
    
    stopTime 
    Determines the end time for the calculation. This is a decimal value 
    between 0.00 and 23.99. 
    
    [incDay] 
    An optional boolean parameter (0 or 1) that determines if the start and 
    stop times are inclusive of the date range.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.calc.times", 
                                                  startDay, stopDay, incDay)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def window_condition():
    """
    
    Gets the window conditions for lighting calculations using the 
    calc.lighting command. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    cleanliness 
    An index representing the average cleanliness of windows in the model, 
    as given in the following table. 
    
    Relevant Data Table(s)
    
    Window Cleanliness Values 
    Value Description 
    0 Clean Windows (x 1.00) 
    1 Average Windows (x 0.90) 
    2 Dirty Windows (x 0.75) 

    """
    val = p2e._app.Request("get.calc.windows")
    return p2e._base._util._convert_str_to_type(val, str)

def set_window_condition(cleanliness):
    """
    
    Sets the precision of lighting calculations to be used with the 
    calc.lighting command. 

    Parameter(s)
    This property takes the following parameters.
    
    cleanliness 
    An index representing the average cleanliness of windows in the model, 
    as given in the following table. 
    
    Relevant Data Table(s)
    
    Window Cleanliness Values 
    Value Description 
    0 Clean Windows (x 1.00) 
    1 Average Windows (x 0.90) 
    2 Dirty Windows (x 0.75) 

    """
    arg_str = p2e._base._util._convert_args_to_string("set.calc.windows", 
                                                  cleanliness)
    p2e._app.Exec(arg_str)
    
    return property(**locals())
