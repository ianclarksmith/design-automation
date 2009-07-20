import py2ecotect
from py2ecotect import string_util

class Project(object):
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_altitude(self):
        """
        
        Retrieves the current altitude of the site, relative to sea level. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        alt 
        The altitude as height above sea level.
        
        """
        val = py2ecotect.conversation.Request("get.project.altitude")
        return string_util._convert_str_to_type(val, float)

    def set_altitude(self, alt):
        """
        
        Sets the altitude of the site, above sea level. 

        Parameter(s)
        This property takes the following parameters.
        
        alt 
        The altitude as height above sea level.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.altitude", 
                                                     alt)
        py2ecotect.conversation.Exec(arg_str)

    def get_client(self):
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
        val = py2ecotect.conversation.Request("get.project.client")
        return string_util._convert_str_to_type(val, str)

    def set_client(self, client):
        """
        
        Sets the text value used to identify the user who worked on the model 
        or the client for whom the model was created. 

        Parameter(s)
        This property takes the following parameters.
        
        client 
        A text string containing the new client name.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.client", 
                                                     client)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_description(self):
        """
        
        Retrieves the job description of the project. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A text string containing the result. 
        
        """
        val = py2ecotect.conversation.Request("get.project.description")
        return string_util._convert_str_to_type(val, str)
        
    def set_description(self, description):
        """
        
        Sets the job description of the project. 

        Parameter(s)
        This property takes the following parameters.
        
        description 
        A text string containing the new description.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.description", 
                                                     description)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_latitude(self):
        """
        
        Retrieves the latitude of the current model. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        lat 
        The latitude in decimal degrees.
        
        """
        val = py2ecotect.conversation.Request("get.project.latitude")
        return string_util._convert_str_to_type(val, float)
 
    def set_latitude(self, lat):
        """
        
        Sets the latitude of the current model. 

        Parameter(s)
        This property takes the following parameters.
        
        lat 
        The latitude in decimal degrees.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.latitude", 
                                                     lat)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_location(self):
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
        val = py2ecotect.conversation.Request("get.project.location")
        return string_util._convert_str_to_list(val, float, float, float)

    def set_location(self, latitude, longitude, timezone, update = True):
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
        arg_str = string_util._convert_args_to_string("set.project.location", 
                                                     latitude, longitude, 
                                                     timezone, update)
        py2ecotect.conversation.Exec(arg_str)

    def get_loc_name(self):
        """
        
        Retrieves the name of the current model location. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        name 
        A text string representing the name of the location.
        
        """
        val = py2ecotect.conversation.Request("get.project.locname")
        return string_util._convert_str_to_type(val, str)

    def set_loc_name(self, name):
        """
        
        Sets the name of the current model location. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        A text string representing the new name of the location.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.locname", 
                                                     name)
        py2ecotect.conversation.Exec(arg_str)

    def get_longitude(self):
        """
        
        Retrieves the longitude of the current model. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        lng 
        The longitude in decimal degrees.
        
        """
        val = py2ecotect.conversation.Request("get.project.longitude")
        return string_util._convert_str_to_type(val, float)
          
    def set_longitude(self, lng):
        """
        
        Sets the longitude of the current model. 

        Parameter(s)
        This property takes the following parameters.
        
        lng 
        The longitude in decimal degrees.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.longitude", 
                                                     lng)
        py2ecotect.conversation.Exec(arg_str)

    def get_north(self):
        """
        
        Retrieves the North angle offset. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        angle 
        The angle in degrees between true north and the positive Y axis.
        
        """
        val = py2ecotect.conversation.Request("get.project.north")
        return string_util._convert_str_to_type(val, float)

    def set_north(self, north):
        """
        
        Sets the North angle offset. 

        Parameter(s)
        This property takes the following parameters.
        
        north 
        The angle in degrees between true north and the positive Y axis.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.north", 
                                                     north)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_reference(self):
        """
        
        Retrieves the job reference number for the project. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A text string containing the result.
        
        """
        val = py2ecotect.conversation.Request("get.project.reference")
        return string_util._convert_str_to_type(val, str)

    def set_reference(self, description):
        """
        
        Sets the job reference number of the project. 

        Parameter(s)
        This property takes the following parameters.
        
        description 
        A text string containing the new reference number. 
        
        """
        arg_str = string_util._convert_args_to_string("set.project.reference", 
                                                     description)
        py2ecotect.conversation.Exec(arg_str)

    def get_terrain(self):
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
        val = py2ecotect.conversation.Request("get.project.terrain")
        return string_util._convert_str_to_type(val, int)

    def set_terrain(self, terrain):
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
        arg_str = string_util._convert_args_to_string("set.project.terrain", 
                                                     terrain)
        py2ecotect.conversation.Exec(arg_str)

    def get_timezone(self):
        """
        
        Retrieves the timezone for the model location. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        tz 
        The time zone as an offset from GMT in decimal hours. 
        
        """
        val = py2ecotect.conversation.Request("get.project.timezone")
        return string_util._convert_str_to_type(val, float)
        
    def set_timezone(self, tz):
        """
        
        Sets the timezone of the model's location. 

        Parameter(s)
        This property takes the following parameters.
        
        tz 
        A GMT offset value in +/- decimal hours.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.timezone", 
                                                      tz)
        py2ecotect.conversation.Exec(arg_str)

    def get_title(self):
        """
        
        Retrieves the title for the project. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A text string containing the result. 
        
        """
        val = py2ecotect.conversation.Request("get.project.title")
        return string_util._convert_str_to_type(val, str)

    def set_title(self, description):
        """
        
        Sets the title of the project. 

        Parameter(s)
        This property takes the following parameters.
        
        description 
        A text string containing the new title.
        
        """
        arg_str = string_util._convert_args_to_string("set.project.title", 
                                                     description)
        py2ecotect.conversation.Exec(arg_str)

    def get_type(self):
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
        val = py2ecotect.conversation.Request("get.project.type")
        return string_util._convert_str_to_type(val, int)

    def set_type(self, type):
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
        arg_str = string_util._convert_args_to_string("set.project.type", type)
        py2ecotect.conversation.Exec(arg_str)

    altitude = property(fget = get_altitude, fset = set_altitude, 
                        doc = "The current altitude of the site, relative to"
                        " sea level")
    
    client = property(fget = get_client, fset = set_client, 
                        doc = "The text value used to identify the user who"
                        " worked on the model or the client for whom the model"
                        " was created")
    
    description = property(fget = get_description, fset = set_description, 
                        doc = "The job description of the project")
    
    latitude = property(fget = get_latitude, fset = set_latitude, 
                        doc = "The latitude of the current model")
    
    loc_name = property(fget = get_loc_name, fset = set_loc_name, 
                        doc = "The name of the current model location")
    
    longitude = property(fget = get_longitude, fset = set_longitude, 
                        doc = "The longitude of the current model")
    
    north = property(fget = get_north, fset = set_north, 
                        doc = "The North angle offset")
    
    reference = property(fget = get_reference, fset = set_reference, 
                        doc = "The job reference number for the project")
    
    terrain = property(fget = get_terrain, fset = set_terrain, 
                        doc = "The type of terrain the project site is located on")
    
    timezone = property(fget = get_timezone, fset = set_timezone, 
                        doc = "The timezone for the model location")
    
    title = property(fget = get_title, fset = set_title, 
                        doc = "The title for the project")
    
    type = property(fget = get_type, fset = set_type, 
                        doc = "The building type")


if __name__ == "__main__":
    x = Project()
    #x.type = 3
    #print x.type
    
    print "Tests completed"