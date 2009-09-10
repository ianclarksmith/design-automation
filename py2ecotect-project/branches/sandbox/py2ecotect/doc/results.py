import py2ecotect as p2e

#===========================================================================
# Getters and Setters
#===========================================================================
def array(i, j):
    """
    
    The various solar and thermal analysis calculations store their results 
    either directly within the zones they are working on, or in a large 2D 
    data array. This method allows access to this array. The exact format 
    of data within the array depends upon the type of calculation last 
    performed. 

    Parameter(s)
    This property takes the following parameters.
    
    i 
    As defined below. 
    
    j 
    As defined below. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified array value. 
    
    Relevant Data Table(s)
    
    Thermal Analysis
    
    Hourly Temperatures
    Internal temperature values are stored in each zone. Use the following 
    command to access them:
    
    get.zone.temperature zone hour
    
    Hourly Gains 
    The seven different gains are stored in the first seven elements of the 
    array. Thus the i value refers to the table below whereas the j value 
    is the hour index of the day (0 to 23). 
    
    Data Type Value 
    HVAC Load 0 
    Conduction Gain 1 
    Sol-Air Gains 2 
    Direct Solar Gains 3 
    Ventilation Gains 4 
    Internal Gains 5 
    Inter-Zonal Gains 6 
    
    Heat / Cool Load
    Monthly heating and cooling loads are stored directly in the heating 
    and cooling load arrays for each zone. The 'Outside' zone (index = 0) 
    stores the total loads of all zones visible at the time of the last 
    calculation. Use the following commands to access them:
    
    get.zone.heating zone month
    get.zone.cooling zone month  
    
    Temperature Distribution (0 - 48)
    This too is stored within the heating and cooling load arrays for each 
    zone. As there are only 12 indexes in each load array (1 for each 
    month), each index represents a 2-degree range with the heating array 
    representing 0-24 deg Cel and the cooling array 24-48deg Cel.
    
    Solar Exposure
    Single Day
    The data from a single day's solar radiation analysis on a surface is 
    not stored in the results array. Use the get.results.solar command 
    described below.
    
    Average Daily & Total Monthly
    These values are stored in the array by MONTHS and HOURS. The i value 
    refers to the month (0-11) whereas the j value is the hour index of the 
    day (0 to 23). The array only stores the current radiation data value. 
    Thus, if the Radiation Data: Item is set to Absorbed, then only the 
    absorbed value is stored and displayed. 
    
    An annual value is also stored for i=12, but not displayed. For Total 
    Monthly calculations, these are the annual totals for each hour. For 
    Average Daily calculations these are the annual average daily value 
    for eah hour.
    
    Full Hourly
    This calculation stores all 8760 hourly values in the array by DAY and 
    HOUR. The i value refers to the day of the year (0-364) whereas the j 
    value is the hour index of the day (0 to 23). 
    
    Resource Use
    The resource use values are stored in the array by day and type. The i 
    value refers to the day of the year (0-364) whereas the j value is 0 
    for the resource used or 1 for the resource collected.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.array", i, j)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_conduction(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for the total gains conducted through the building fabric. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use. 
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.conduction", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_daily(zone):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    either the Hourly Temperature Profile or Hourly Heat Gains/Losses calculation), 
    this command will directly access the calculated results for the total sum of 
    all gains for the entire day. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.daily", 
                                                  zone.eco_id)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_fabric(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for conduction through fabric, opaque and glazing objects. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.fabric", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_glazing_fabric(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for the conduction gains through only glazing fabric. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.glazingfabric", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_indirect(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for the indirect solar and air temperature effect. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use. 
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.indirect", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_internal(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for internal gains from people and APPLIANCES. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.internal", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_opaque_fabric(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for the conduction gains through only opaque fabric. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.opaquefabric", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_solar(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for the direct solar radiation through glazing. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.solar", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def gains_total(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for the total sum of all gains for the given hour. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value.
    
    """ 
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.total", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)   
 
def gains_ventilation(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for infiltration and ventilation. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.ventilation", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)   

def gains_zonal(zone, hour):
    """
    
    Once an hourly thermal analysis has been performed for a single day 
    (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
    calculation), this command will directly access the calculated results 
    for inter-zonal gains. 

    Parameter(s)
    This property takes the following parameters.
    
    zone 
    The zone object to use.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified gains value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.gains.zonal", 
                                                  zone.eco_id, hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)   
#------------------------------------------------------------------------------ 
def solar_absorbed(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    amount of radiation absorbed by the surface (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.absorbed", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)   

def solar_angle(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    angle of incidence (degrees). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.angle", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)   

def solar_area(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    area of collector surface (m^2). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.area", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)   

def solar_available(hour):
    """
    
    Returns the available radiation value after a calc_solar_exposure_day calculation 
    for the amount of available solar radiation from the weather file, 
    given in (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.available", hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)   

def solar_diffuse(hour):
    """
    
    Returns solar radiation value after a calc_solar_exposure_day calculation for 
    the amount of diffuse radiation incident on surface (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.diffuse", hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)
 
def solar_direct(hour):
    """
    
    Returns solar radiation value after a calc_solar_exposure_day calculation for 
    the amount of direct radiation incident on surface (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.direct", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def solar_global(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    total global horizontal radiation from Sun (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.global", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def solar_incident(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    amount of radiation incident on the surface (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.incident", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def solar_reflected(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    amount of reflected incident radiation (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.reflected", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def solar_shading(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    percentage of surface shading (%). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.shading", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)

def solar_transmitted(hour):
    """
    
    Returns the radiation value after a calc_solar_exposure_day calculation for the 
    amount of radiation transmitted through the surface (W). 

    Parameter(s)
    This property takes the following parameters.
    
    hour 
    The hour to retrieve, being from 0 to 23. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified solar value.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.results.solar.transmitted", 
                                                  hour)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
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
    return p2e._base._util._convert_str_to_type(val, float)    
def sky_components():
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
    return p2e._base._util._convert_str_to_list(val, float, float, float)
#------------------------------------------------------------------------------ 
def insolation_diffuse():
    """
    
    Returns the diffuse solar radiation component as a single decimal value 
    in Watts per square metre. This is only valid after a shading 
    calculation has been performed (see the calculation.calc_shading_percentage method 
    and model.set_time for more information). 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the current diffuse solar component.
    
    """
    val = p2e._app.Request("get.shading.diffuse")
    return p2e._base._util._convert_str_to_type(val, float)
 
def insolation_direct():
    """
    
    Returns the current direct solar radiation component as a single 
    decimal value in Watts per square metre. This is only valid after a 
    shading calculation has been performed (see the calculation.calc_shading_percentage method 
    and model.set_time for more information). 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the current direct solar component.
    
    """
    val = p2e._app.Request("get.shading.direct")
    return p2e._base._util._convert_str_to_type(val, float)

def insolation(from_day, to_day):
    """
    
    Returns the total direct and diffuse incident solar radiation on the 
    object for which the current shading mask has been calculated. Both are 
    returned as single decimal values in Watts per square metre. A third 
    value is also returned, being a count of the number of hours over which 
    the direct and diffuse values were generated. 

    Parameter(s)
    This property takes the following parameters.
    
    from_day 
    A value representing the Julian date when the calculation will begin, 
    given as an integer from 1 to 365. 
    
    to_day 
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
    arg_str = p2e._base._util._convert_args_to_string("get.shading.range", from_day, to_day)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_list(val, float, float, float)
#------------------------------------------------------------------------------ 
def shading_percentange():
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
    return p2e._base._util._convert_str_to_type(val, float)

def shading_percentange_at_angle(azi, alt):
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
    arg_str = p2e._base._util._convert_args_to_string("get.shading.percentage.angle", azi, alt)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)
 
def shading_percentange_at_date_time(day, time):
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
    arg_str = p2e._base._util._convert_args_to_string("get.shading.percentage.datetime", day, time)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_list(val, float, float, float, float)
 
def shading_percentange_at_index(x, y):
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
    arg_str = p2e._base._util._convert_args_to_string("get.shading.percentage.index", x, y)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, float)