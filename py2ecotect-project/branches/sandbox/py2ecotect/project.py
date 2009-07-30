import py2ecotect as p2e

class Project(object):
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    @apply
    def altitude():
        def fget(self):
            """
            
            Retrieves the current altitude of the site, relative to sea level. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            alt 
            The altitude as height above sea level.
            
            """
            val = p2e.conversation.Request("get.project.altitude")
            return p2e._util._convert_str_to_type(val, float)
    
        def fset(self, alt):
            """
            
            Sets the altitude of the site, above sea level. 
    
            Parameter(s)
            This property takes the following parameters.
            
            alt 
            The altitude as height above sea level.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.altitude", 
                                                         alt)
            p2e.conversation.Exec(arg_str)
            
        return property(**locals())
    
    @apply
    def client():
        def fget(self):
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
            val = p2e.conversation.Request("get.project.client")
            return p2e._util._convert_str_to_type(val, str)
    
        def fset(self, client):
            """
            
            Sets the text value used to identify the user who worked on the model 
            or the client for whom the model was created. 
    
            Parameter(s)
            This property takes the following parameters.
            
            client 
            A text string containing the new client name.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.client", 
                                                         client)
            p2e.conversation.Exec(arg_str)
            
        return property(**locals())
    
    @apply
    def description():
        def fget(self):
            """
            
            Retrieves the job description of the project. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            result 
            A text string containing the result. 
            
            """
            val = p2e.conversation.Request("get.project.description")
            return p2e._util._convert_str_to_type(val, str)
            
        def fset(self, description):
            """
            
            Sets the job description of the project. 
    
            Parameter(s)
            This property takes the following parameters.
            
            description 
            A text string containing the new description.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.description", 
                                                         description)
            p2e.conversation.Exec(arg_str)
            
        return property(**locals())
    
    @apply
    def latitude():    
        def fget(self):
            """
            
            Retrieves the latitude of the current model. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            lat 
            The latitude in decimal degrees.
            
            """
            val = p2e.conversation.Request("get.project.latitude")
            return p2e._util._convert_str_to_type(val, float)
     
        def fset(self, lat):
            """
            
            Sets the latitude of the current model. 
    
            Parameter(s)
            This property takes the following parameters.
            
            lat 
            The latitude in decimal degrees.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.latitude", 
                                                         lat)
            p2e.conversation.Exec(arg_str)
            
        return property(**locals())
        
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
        val = p2e.conversation.Request("get.project.location")
        return p2e._util._convert_str_to_list(val, float, float, float)

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
        arg_str = p2e._util._convert_args_to_string("set.project.location", 
                                                     latitude, longitude, 
                                                     timezone, update)
        p2e.conversation.Exec(arg_str)
    
    @apply
    def loc_name():
        def fget(self):
            """
            
            Retrieves the name of the current model location. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            name 
            A text string representing the name of the location.
            
            """
            val = p2e.conversation.Request("get.project.locname")
            return p2e._util._convert_str_to_type(val, str)
    
        def fset(self, name):
            """
            
            Sets the name of the current model location. 
    
            Parameter(s)
            This property takes the following parameters.
            
            name 
            A text string representing the new name of the location.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.locname", 
                                                         name)
            p2e.conversation.Exec(arg_str)
            
        return property(**locals())
    
    @apply
    def longitude():
        def fget(self):
            """
            
            Retrieves the longitude of the current model. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            lng 
            The longitude in decimal degrees.
            
            """
            val = p2e.conversation.Request("get.project.longitude")
            return p2e._util._convert_str_to_type(val, float)
              
        def fset(self, lng):
            """
            
            Sets the longitude of the current model. 
    
            Parameter(s)
            This property takes the following parameters.
            
            lng 
            The longitude in decimal degrees.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.longitude", 
                                                         lng)
            p2e.conversation.Exec(arg_str)
            
        return property(**locals())
    
    @apply
    def north():
        def fget(self):
            """
            
            Retrieves the North angle offset. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            angle 
            The angle in degrees between true north and the positive Y axis.
            
            """
            val = p2e.conversation.Request("get.project.north")
            return p2e._util._convert_str_to_type(val, float)
    
        def fset(self, north):
            """
            
            Sets the North angle offset. 
    
            Parameter(s)
            This property takes the following parameters.
            
            north 
            The angle in degrees between true north and the positive Y axis.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.north", 
                                                         north)
            p2e.conversation.Exec(arg_str)
            
        return property(**locals())
    
    @apply
    def reference(): 
        def fget(self):
            """
            
            Retrieves the job reference number for the project. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            result 
            A text string containing the result.
            
            """
            val = p2e.conversation.Request("get.project.reference")
            return p2e._util._convert_str_to_type(val, str)
    
        def fset(self, description):
            """
            
            Sets the job reference number of the project. 
    
            Parameter(s)
            This property takes the following parameters.
            
            description 
            A text string containing the new reference number. 
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.reference", 
                                                         description)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def terrain():
        def fget(self):
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
            val = p2e.conversation.Request("get.project.terrain")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, terrain):
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
            arg_str = p2e._util._convert_args_to_string("set.project.terrain", 
                                                         terrain)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def timezone():
        def fget(self):
            """
            
            Retrieves the timezone for the model location. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            tz 
            The time zone as an offset from GMT in decimal hours. 
            
            """
            val = p2e.conversation.Request("get.project.timezone")
            return p2e._util._convert_str_to_type(val, float)
            
        def fset(self, tz):
            """
            
            Sets the timezone of the model's location. 
    
            Parameter(s)
            This property takes the following parameters.
            
            tz 
            A GMT offset value in +/- decimal hours.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.timezone", 
                                                          tz)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def title():
        def fget(self):
            """
            
            Retrieves the title for the project. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            result 
            A text string containing the result. 
            
            """
            val = p2e.conversation.Request("get.project.title")
            return p2e._util._convert_str_to_type(val, str)
    
        def fset(self, description):
            """
            
            Sets the title of the project. 
    
            Parameter(s)
            This property takes the following parameters.
            
            description 
            A text string containing the new title.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.project.title", 
                                                         description)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def type():
        def fget(self):
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
            val = p2e.conversation.Request("get.project.type")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, type):
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
            arg_str = p2e._util._convert_args_to_string("set.project.type", type)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())


if __name__ == "__main__":
    x = Project()
    #x.type = 3
    #print x.title
    #x.title = "HELLO"
    
    print "Tests completed"