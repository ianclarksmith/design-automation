import py2ecotect
from py2ecotect import string_util

class Weather(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def load(self, filename = ""):
        """
        
        Loads a weather data file into the current model. By default, this 
        script method only loads the actual hourly weather data, leaving the 
        latitude, longitude, time-zone and other location data untouched. If 
        you include '.all' after the load command (cmd("weather.load.all", 
        "C:\\Temp\\Location.wea")), both the hourly weather data and location 
        data is loaded. 

        Parameter(s)
        This command takes the following parameters.
        
        [filename] 
        This optional parameter indicates the full path to the file that is to 
        be loaded. If not given, then the last loaded weather file will be used. 
        
        """
        arg_str = string_util._convert_args_to_string("weather.load", filename)
        py2ecotect.conversation.Exec(arg_str)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_beam_solar(self, day, hour):
        """
        
        Retrieves the beam solar radiation (W) for the specified day and hour in 
        the current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A value in Watts representing the beam solar radiation.
        
        """
        arg_str = string_util._convert_args_to_string("get.weather.beamsolar", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_beam_solar(self, day, hour, value):
        """
        
        Sets the beam solar radiation (W) for the specified day and hour in the 
        current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        A value in Watts representing the beam solar radiation. 

        
        """
        arg_str = string_util._convert_args_to_string("set.weather.beamsolar", 
                                                     day, hour, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_cloudiness(self, day, hour):
        """
        
        Retrieves the cloudiness (%) for the specified day and hour in the 
        current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A percentage value representing the cloudiness.
        
        """
        arg_str = string_util._convert_args_to_string("get.weather.cloudiness", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_cloudiness(self, day, hour, value):
        """
        
        Sets the cloudiness (%) for the specified day and hour in the current 
        weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        A percentage value representing the cloudiness.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.cloudiness", 
                                                     day, hour, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_country(self):
        """
        
        Retrieves the name of the state/country in the currently loaded weather 
        data set. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A text string representing the state/country in the current weather 
        data set.
        
        """
        val = py2ecotect.conversation.Request("get.weather.country")
        return string_util._convert_str_to_type(val, str)
        
    def set_country(self, name):
        """
        
        Sets the name of the state/country in the currently loaded weather data 
        set. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        A text string representing the state/country given to the current 
        weather data set.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.country", 
                                                     name)
        py2ecotect.conversation.Exec(arg_str)

    def get_diffuse_solar(self, day, hour):
        """
        
        Retrieves the diffuse solar radiation (W) for the specified day and 
        hour in the current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A value in Watts representing the diffuse solar radiation. 
        
        """
        arg_str = string_util._convert_args_to_string("get.weather.diffusesolar", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_diffuse_solar(self, day, hour, value):
       """
       
       Sets the diffuse solar radiation (W) for the specified day and hour in 
       the current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        A value in Watts representing the diffuse solar radiation.
       
       """
       arg_str = string_util._convert_args_to_string("set.weather.diffusesolar", 
                                                     day, hour, value)
       py2ecotect.conversation.Exec(arg_str)     

    def get_direction(self, day, hour):
        """
        
        Retrieves the wind direction (0-16) for the specified day and hour in 
        the current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The direction of the wind as an integer between 0 and 16, where 0 
        represents North.
        
        """
        arg_str = string_util._convert_args_to_string("get.weather.direction", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)
    
    def set_direction(self, day, hour, value):
        """
        
        Sets the wind direction (0-16) for the specified day and hour in the 
        current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        The direction of the wind as an integer between 0 and 16, where 0 
        represents North.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.direction", 
                                                     day, hour, value)
        py2ecotect.conversation.Exec(arg_str)     

    def get_file(self):
        """
        
        Retrieves the the full pathname of the currently loaded weather data file. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        filename 
        A text string containing the full path to the current weather data file.
        
        """
        val = py2ecotect.conversation.Request("get.weather.file")
        return string_util._convert_str_to_type(val, str)

    def get_name(self):
        """
        
        Retrieves the name of the location in the currently loaded weather data 
        set. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A text string representing the name of the current weather data set.
        
        """
        val = py2ecotect.conversation.Request("get.weather.name")
        return string_util._convert_str_to_type(val, str)
        
    def set_name(self, name):
        """
        
        Sets the name of the location in the currently loaded weather data set. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        A string representing the location given to the current weather data set.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.name", name)
        py2ecotect.conversation.Exec(arg_str)     
        
    def get_rainfall(self, day, hour):
        """
        
        Retrieves the rainfall (mm) for the specified day and hour in the 
        current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day.
        
        """
        arg_str = string_util._convert_args_to_string("get.weather.rainfall", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_rainfall(self, day, hour, value):
        """
        
        Sets the rainfall (mm) for the specified day and hour in the current 
        weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        A value specifying the amount of rainfall in millimeters.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.rainfall", 
                                                     day, hour, value)
        py2ecotect.conversation.Exec(arg_str)     

    def get_rel_humidity(self, day, hour):
        """
        
        Retrieves the relative humidity (%) for the specified day and hour in 
        the current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A value specifying the relative humidity as a percentage.
        
        """
        arg_str = string_util._convert_args_to_string("get.weather.relhumidity", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)
        
    def set_rel_humidity(self, day, hour, value):
        """
        
        Sets the relative humidity (%) for the specified day and hour in the 
        current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        A value specifying the relative humidity as a percentage.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.relhumidity", 
                                                     day, hour, value)
        py2ecotect.conversation.Exec(arg_str)     

    def get_speed(self, day, hour):
        """
        
        Retrieves the wind speed (km/hr) for the specified day and hour in the 
        current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A value specifying the wind speed speed in kilometers per hour 

        """
        arg_str = string_util._convert_args_to_string("get.weather.speed", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_speed(self, day, hour, value):
        """
        
        Sets the wind speed (k,/hr) for the specified day and hour in the 
        current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        A value specifying the wind speed speed in kilometers per hour.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.speed", 
                                                     day, hour, value)
        py2ecotect.conversation.Exec(arg_str)     

    def get_temperature(self, day, hour):
        """
        
        Retrieves the temperature (Dry Bulb, deg celsius) for the specified day 
        and hour in the current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A value specifying the temperature to set in degrees celsius.
        
        """
        arg_str = string_util._convert_args_to_string("get.weather.temperature", 
                                                     day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_temperature(self, day, hour, value):
        """
        
        Sets the temperature (Dry Bulb, degree celsius) for the specified day 
        and hour in the current weather data. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        value 
        A value specifying the temperature to set in degrees celsius.
        
        """
        arg_str = string_util._convert_args_to_string("set.weather.temperature", 
                                                     day, hour, value)
        py2ecotect.conversation.Exec(arg_str)     

    country = property(fget = get_country, fset = set_country, 
                        doc = "The name of the state/country in the currently"
                        " loaded weather data set")
    
    file = property(fget = get_file, doc = "The full pathname of the currently"
                    " loaded weather data file")
    
    name = property(fget = get_name, doc = "The name of the location in the"
                    " currently loaded weather data set")






if __name__ == "__main__":
    x = Weather()
    
    #x.load("C:\Program Files\Autodesk\Ecotect 2009\Weather\Germany-Munich.wea")
    #print x.get_beam_solar(300, 17)
    #x.set_beam_solar(300, 17, 500)
    #print x.get_cloudiness(300, 17)
    #x.set_cloudiness(300, 17, 75)
    #print x.get_country()
    #x.set_country("Singapore")
    #print x.get_diffuse_solar(300, 17)
    #x.set_diffuse_solar(300, 17, 88)
    #print x.get_direction(300, 17)
    #x.set_direction(300, 17, 4)
    #print x.get_file()
    #print x.get_name()
    #x.set_name("TEST")
    #print x.get_rainfall(300, 17)
    #x.set_rainfall(300, 17, 100)
    #print x.get_speed(300, 17)
    #x.set_speed(300, 17, 45.7)
    #print x.get_temperature(300, 17)
    #x.set_temperature(300, 17, 45.9)

    

    print "Tests completed"
