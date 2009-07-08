import py2ecotect
from py2ecotect import StringUtil

def get_flag(flag):
    """
    
    Gets the state of individual flags that control the display of attribute 
    values. 

    Parameter(s)
    This property takes the following parameters.
    
    flag 
    This parameter specifies the bitwise flag.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    state 
    The boolean state of the selected bitwise flag. If set, the value is 1, if 
    not it is 0. The table below gives the bitwise values of each available 
    attribute flag. 
    
    Relevant Data Table(s)
    
    Available Attribute Flags 
    Token Value Description 
    text 1 Display object attribute as a text value 
    vectors 2 Display object attribute as a vector. 
    colours 4 Display object attribute as a fill colous. 

    """
    arg_str = StringUtil._convert_args_to_string("get.attribute.flag", flag)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, int)

def set_flag(flag, state = True):
    """
    
    Sets individual flags that control the display of attribute values. 

    Parameter(s)
    This property takes the following parameters.
    
    flag 
    This parameter specifies the bitwise flag to be set or cleared. 
    
    [state] 
    This parameter determines whether the flag is to be set or cleared. This is 
    a boolean value where 1 or true represents the affirmative and 0 or false 
    the negative. If not included, it defaults to true. 
    
    Relevant Data Table(s)
    
    Available Attribute Flags 
    Token Value Description 
    text 1 Display object attribute as a text value 
    vectors 2 Display object attribute as a vector. 
    colours 4 Display object attribute as a fill colous.
    
    Here is an example:
    
    >>> set_flag("text", False)
    
    """
    arg_str = StringUtil._convert_args_to_string("set.attribute.flag", flag, 
                                                 state)
    py2ecotect.conversation.Exec(arg_str)

def get_flags():
    """
    
    Retrieves a value representing the total of all the attribute flags that 
    control the display of attribute values. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    flags 
    The bitwise total of all the flags currently set. The table below gives the 
    bitwise values of each available attribute flag. 
    
    Relevant Data Table(s)
    
    Available Attribute Flags 
    Token Value Description 
    text 1 Display object attribute as a text value 
    vectors 2 Display object attribute as a vector. 
    colours 4 Display object attribute as a fill colous. 

    """
    val = py2ecotect.conversation.Request("get.attribute.flags")
    return StringUtil._convert_str_to_type(val, int)

def get_name(index):
    """
    
    Gets the name of the specified object attribute as a string value. 

    Parameter(s)
    This property takes the following parameters.
    
    index 
    An number from 0 to 2 representing the index of the three available object 
    attributes. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    name 
    A text string containing the name name of the attribute.
    
    """
    arg_str = StringUtil._convert_args_to_string("get.attribute.name", index)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, str)

def set_name(index, name):
    """
    
    Sets the name of the specified object attribute as a string value. The index 
    parameter is an from 0 to 2 representing the index of the object attribute. 

    Parameter(s)
    This property takes the following parameters.
    
    index 
    An number from 0 to 2 representing the index of the 3 available object 
    attributes.
    
    """
    arg_str = StringUtil._convert_args_to_string("set.attribute.name", index, 
                                                 name)
    py2ecotect.conversation.Exec(arg_str)

def get_scale():
    """
    
    Gets the minimum and maximum extents of the colour scale used to display the 
    object attributes. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    min 
    The minimum scale value. 
    
    max 
    The maximum scale value.
    
    """
    val = py2ecotect.conversation.Request("get.attribute.scale")
    return StringUtil._convert_str_to_list(val, float)

def set_scale(min, max):
    """
    
    Sets the minimum and maximum extents of the colour scale used to display the 
    object attributes. 

    Parameter(s)
    This property takes the following parameters.
    
    min 
    Sets the minimum scale value to be used. 
    
    max 
    Sets the maximum scale value to be used.
    
    """
    arg_str = StringUtil._convert_args_to_string("set.attribute.scale", min, max)
    py2ecotect.conversation.Exec(arg_str)

def set_type(index, type):
    """
    
    Sets the type of the specified object attribute. The index parameter is an 
    from 0 to 2 representing the index of the object attribute, whilst type must 
    be a value from the following table.

    Parameter(s)
    This property takes the following parameters.
    
    index 
    An value ranging 0 and 2, representing the index of the object attribute to 
    be set. 
    
    type 
    A value representing a standard data type, taken from the following 
    Attribute Types table. 
    
    Relevant Data Table(s)
    
    Available Attribute Types Value Description 
    1 Number Rays Hit 
    10 Avg Daily Total (Wh/m^2) 
    11 Avg Daily Direct (Wh/m^2) 
    12 Avg Daily Diffuse (Wh/m^2) 
    20 Daylight Factor (%) 
    21 Daylight Level (Lux) 
    22 Daylight Autonomy (%) 
    23 Electric Light (Lux) 
    24 Sky Component (%) 
    30 Percentage Rays Hit (%) 
    31 Weighted Level 
    40 Temperature 
    41 Heat Gains 
    42 Flow Rate 

    """
    arg_str = StringUtil._convert_args_to_string("set.attribute.type", index, 
                                                 type)
    py2ecotect.conversation.Exec(arg_str)

def get_units(type):
    """
    
    Gets the name of the specified object attribute as a string value. The index 
    parameter is an from 0 to 2 representing the index of the object attribute. 

    Parameter(s)
    This property takes the following parameters.
    
    type 
    An nmber from 0 to 2 representing the index of the object attribute. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    units 
    The units of measurement used, for example Lux.
    
    """
    arg_str = StringUtil._convert_args_to_string("get.attribute.units", type)
    val = py2ecotect.conversation.Request(arg_str)
    return StringUtil._convert_str_to_type(val, str)

def set_units(type, units):
    """
    
    Sets the name of the specified object attribute as a string value. The index 
    parameter is an from 0 to 2 representing the index of the object attribute, 
    while the units parameter specifies the units of measurement to be used. 

    Parameter(s)
    This property takes the following parameters.
    
    type 
    An number from 0 to 2 representing the index of the object attribute. 
    
    units 
    Specifies the units of measurement to be used. For example Lux.
    
    """
    arg_str = StringUtil._convert_args_to_string("set.attribute.units", type, 
                                                 units)
    py2ecotect.conversation.Exec(arg_str)



if __name__ == "__main__":
    #set_flag("text", False)
    #print get_flag(1)
    #print get_flags()
    #set_name(0, "")
    #print get_name(0)
    #set_scale(100, 1000)
    #print get_scale()
    #set_type(0, 42)
    #set_units(1, "LUX" )
    #print get_units(1)
    
    print "Tests completed"
    
    
    
    
    
    
    
    
    
    