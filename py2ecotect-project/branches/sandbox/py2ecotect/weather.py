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
    







if __name__ == "__main__":
    x = Weather()
    
    #x.load("C:\Program Files\Autodesk\Ecotect 2009\Weather\Germany-Munich.wea")

    

    print "Tests completed"
