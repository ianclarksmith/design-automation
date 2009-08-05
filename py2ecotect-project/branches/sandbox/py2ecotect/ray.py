import py2ecotect as p2e

class Ray(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def draw(self, depth = ""):
        """
        
        Draws the path of the current ray as an arrow within the model. 

        Parameter(s)
        This command takes the following parameters.
        
        [depth] 
        This optional parameter specifies the number of reflections to draw. If 
        not given, the entire ray is drawn.
        
        """
        arg_str = p2e._util._convert_args_to_string("ray.draw", depth)
        p2e.conversation.Exec(arg_str)

    def shoot(self, type, azi, alt):
        """
        
        Sends out and traces a ray that travels relative to the x-axis in the 
        given azimuth and altitude angles. 

        Parameter(s)
        This command takes the following parameters.
        
        type 
        An integer value controlling the type of the ray corresponding to the 
        following Types of Ray table. 
        
        azi 
        The azimuth angle in degrees. 
        
        alt 
        The altitude angle in degrees. 
        
        Relevant Data Table(s)
        
        Types of Ray 
        Token Value Description 
        xray 0 Rays pass through all objects intersected, recording each point. 
        sound 1 Rays are reflected specularly by solid objects in the model. 
        light 2 Rays reflect off opaque objects but pass through transparent objects. 
        
        """
        arg_str = p2e._util._convert_args_to_string("ray.shoot", type, azi, 
                                                      alt)
        p2e.conversation.Exec(arg_str)

    def trace(self, type, offset_distance):
        """
        
        Sends out and traces a ray which travels directly away from the 
        specified position. 

        Parameter(s)
        This command takes the following parameters.
        
        type 
        An integer value controlling the type of the ray corresponding to the 
        following Types of Ray table. 
        
        offset_distance 
        A list of three values that represent the offset distance in each of 
        the X, Y and Z axis, given in model coordinates. 
        
        Relevant Data Table(s)
        
        Types of Ray 
        Token Value Description 
        xray 0 Rays pass through all objects intersected, recording each point. 
        sound 1 Rays are reflected specularly by solid objects in the model. 
        light 2 Rays reflect off opaque objects but pass through transparent 
        objects. 

        """
        arg_str = p2e._util._convert_args_to_string("ray.trace", type, 
                                                      offset_distance[0],
                                                      offset_distance[1],
                                                      offset_distance[2])
        p2e.conversation.Exec(arg_str)

    #===========================================================================
    # Properties
    #===========================================================================
    
    @apply
    def depth():
        def fget(self):
            """
            
            Retrieves the number of reflections contained in the currently 
            generated ray. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            depth 
            An integer value giving the number of reflections.
            
            """
            val = p2e.conversation.Request("get.ray.depth")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, depth):
            """
            
            Creates a ray which can then be set with calls to the set.ray.position 
            command. 
    
            Parameter(s)
            This property takes the following parameters.
            
            depth 
            An integer value specifying the number of reflections. This parameter 
            must be less than or equal to get.ray.maxdepth and all intersection 
            points will initially default to the world origin.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.ray.depth", depth)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def max_depth():
        def fget(self):
            """
            
            Retrieves the maximum number of reflections to which rays will be 
            traced. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            max 
            An integer value giving the maximum number of reflections.
            
            """
            val = p2e.conversation.Request("get.ray.maxdepth")
            return p2e._util._convert_str_to_type(val, int)
        
        def fset(self, depth):
            """
            
            Sets the maximum number of reflections to which rays will be traced. 
    
            Parameter(s)
            This property takes the following parameters.
            
            depth 
            An integer value specifying the maximum number of reflections.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.ray.maxdepth", depth)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    def get_object(self, depth):
        """
        
        Retrieves the object index at the specified reflection depth. 

        Parameter(s)
        This property takes the following parameters.
        
        depth 
        An integer value representing the depth. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        object 
        The zero-based index of the object.
        
        """
        #Return value is different. It returns 4 values. So a list 
        #of 4 values is returned
        arg_str = p2e._util._convert_args_to_string("get.ray.object", depth)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float, float, float)
        
    def set_object(self, depth, object):
        """
        
        Sets the object at the specified reflection depth. 

        Parameter(s)
        This property takes the following parameters.
        
        depth 
        An integer value representing the depth. 
        
        object 
        The object to set.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.ray.object", depth, 
                                                      object.eco_id)
        p2e.conversation.Exec(arg_str)
        
    def get_position(self, depth):
        """
        
        Retrieves the 3D position of the ray point at the given reflection depth. 

        Parameter(s)
        This property takes the following parameters.
        
        depth 
        An integer value representing the depth. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        The absolute position in the X, Y and Z axis of the ray point in 3 
        dimensional model space. 
        
        object 
        The zero-based index of the object intersected.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.ray.position", depth)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float, float, int)
    
    def set_position(self, depth, absolute_position, object = ""):
        """
        
        Sets the 3D position of the ray point at the given reflection depth. 

        Parameter(s)
        This property takes the following parameters.
        
        depth 
        An integer value representing the depth. 
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of the ray point in 3 dimensional model space. 
        
        [object] 
        This optional parameter specifies the zero-based index of the object 
        intersected. 
                
        """
        if object == "":
            arg_str = p2e._util._convert_args_to_string("set.ray.position", 
                                                        depth, 
                                                        absolute_position[0],
                                                        absolute_position[1], 
                                                        absolute_position[2], 
                                                        object)
        else:
            arg_str = p2e._util._convert_args_to_string("set.ray.position", 
                                                        depth, 
                                                        absolute_position[0],
                                                        absolute_position[1], 
                                                        absolute_position[2], 
                                                        object.eco_id)
        p2e.conversation.Exec(arg_str)

    def get_source(self):
        """
        
        Retrieves the position of the ray source. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        The absolute position in the X, Y and Z axis of the source point in 3 
        dimensional model space. 
                
        """
        val = p2e.conversation.Request("get.ray.source")
        return p2e._util._convert_str_to_list(val, float, float, float)
        
    def set_source(self, absolute_position):
        """
        
        Sets the position of the ray source. 

        Parameter(s)
        This property takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of the ray point in 3 dimensional model space. 

        """
        arg_str = p2e._util._convert_args_to_string("set.ray.source", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        p2e.conversation.Exec(arg_str)
    
