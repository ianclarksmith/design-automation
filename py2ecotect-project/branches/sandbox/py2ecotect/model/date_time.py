import py2ecotect as p2e


#===========================================================================
# Functions
#===========================================================================
#------------------------------------------------------------------------------ 
def time():
    """
    
    Retrieves the current time of day. The time value returned is a decimal 
    value between 0.0 and 23.99. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    time 
    A decimal value between 0.0 and 23.99. 
    
    """
    val = p2e._app.Request("get.model.time")
    return p2e._base._util._convert_str_to_type(val, float)          

def set_time(time):
    """
    
    Sets the current time of day. 
    
    Parameter(s)
    This property takes the following parameters.
    
    time 
    The time given in decimal hours, between 0.0 and 23.99. 
    
    """
    args = p2e._base._util._convert_args_to_string("set.model.time", time)
    p2e._app.Exec(args)

def time_string():
    """
    
    Retrieves a formated string containing the current model time. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    timeStr 
    A formated time string. 
    
    """
    val = p2e._app.Request("get.model.timestring")
    return p2e._base._util._convert_str_to_type(val, str)
#------------------------------------------------------------------------------ 
def date():
    """
    
    Retrieves the current date as a formatted string ready for printing 
    or output to a file. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    day 
    An integer value between 1 and 31. 
    
    month 
    An integer value between 0 and 11. 
    
    """
    val = p2e._app.Request("get.model.date")
    return p2e._base._util._convert_str_to_list(val, int)  

def set_date(day, month, time = None):
    """
    
    Sets the date in the ECOTECT model. 
    
    Parameter(s)
    This property takes the following parameters.
    
    day 
    An integer value between 1 and 31. 
    
    month 
    An integer value between 0 and 11. 
    
    [time] 
    An optional decimal value between 0.0 and 23.99. 
    
    """
    if time:
        arg_str = p2e._base._util._convert_args_to_string("set.model.date", day, month, time)
    else:
        arg_str = p2e._base._util._convert_args_to_string("set.model.date", day, month)
    p2e._app.Exec(arg_str)
 
def date_string():    
    """
    
    Retrieves a formated string containing the current model date. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    dateStr 
    A formated date string. 
    
    """
    val = p2e._app.Request("get.model.datestring")
    return p2e._base._util._convert_str_to_type(val, str)
#------------------------------------------------------------------------------ 
def month():
    """
    
    Returns the current month. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    month 
    The current model month given as an integer index between 0 and 11.
     
    """
    val = p2e._app.Request("get.model.month")
    return p2e._base._util._convert_str_to_type(val, int)
#------------------------------------------------------------------------------ 
def daylight_savings_flag():            
    """
    
    Retrieves the status of the daylight savings flag. 
    
    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    The daylight savings setting given as a boolean value where 1 
    represents the affirmative and 0 the negative. When true, the 
    current time is offset by one hour. 
    
    """
    val = p2e._app.Request("get.model.daylightsavings")
    return p2e._base._util._convert_str_to_type(val, bool)          
    
def set_daylight_savings_flag(state):
    """
    
    Sets the status of the daylight savings flag. 

    Parameter(s)
    This property takes the following parameters.
    
    [state] 
    Sets the daylight savings flag. This is a boolean value where 1 or true 
    represents the affirmative and 0 or false the negative. When set to 
    true, the current time is offset by one hour.
    
    """
    args = p2e._base._util._convert_args_to_string("set.model.daylightsavings", state)
    p2e._app.Exec(args)
#------------------------------------------------------------------------------ 
def day_of_the_year():
    """
    
    Retrieves the current date and displays it in the julian date 
    format, where a single integer value between 1 and 365 represents a 
    day of the year. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    day 
    An integer value between 1 and 365 that represents a day of the 
    year. 
    
    """
    val = p2e._app.Request("get.model.dayoftheyear")
    return p2e._base._util._convert_str_to_type(val, int)  

def set_day_of_year(day, time = None):
    """
    
    Sets the current date using the julian date format. 

    Parameter(s)
    This property takes the following parameters.
    
    day 
    An integer value between 1 and 365 that represents a day of the year. 
    
    [time] 
    This optional parameter is a decimal hour between 0.0 and 23.99.
     
    """
    if time:
        arg_str = p2e._base._util._convert_args_to_string("set.model.dayoftheyear", 
                                                      day, time)
    else:
        arg_str = p2e._base._util._convert_args_to_string("set.model.dayoftheyear", 
                                                      day)
    p2e._app.Exec(arg_str)


#------------------------------------------------------------------------------ 
def sunrise():
    """
    
    Returns the sunrise time as a 24 hour decimal value. Thus, 6:30am would 
    be returned as 6.5. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    sunrise 
    The time of sunrise given as a decimal hour. 
    
    """
    val = p2e._app.Request("get.model.sunrise")
    return p2e._base._util._convert_str_to_type(val, float)

def sunset():
    """
    
    Returns the sunset time as a 24 hour decimal value. Thus, 6:30pm would 
    be returned as 18.5. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    sunset 
    The time of sunset given as a decimal hour. 
    
    """
    val = p2e._app.Request("get.model.sunset")
    return p2e._base._util._convert_str_to_type(val, float)