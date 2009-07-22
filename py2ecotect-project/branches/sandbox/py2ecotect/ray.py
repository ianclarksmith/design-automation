import py2ecotect
from py2ecotect import string_util

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
        arg_str = string_util._convert_args_to_string("ray.draw", depth)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = string_util._convert_args_to_string("ray.shoot", type, azi, 
                                                      alt)
        py2ecotect.conversation.Exec(arg_str)

    def trace(self, type, dx, dy, dz):
        """
        
        Sends out and traces a ray which travels directly away from the 
        specified position. 

        Parameter(s)
        This command takes the following parameters.
        
        type 
        An integer value controlling the type of the ray corresponding to the 
        following Types of Ray table. 
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates. 
        
        Relevant Data Table(s)
        
        Types of Ray 
        Token Value Description 
        xray 0 Rays pass through all objects intersected, recording each point. 
        sound 1 Rays are reflected specularly by solid objects in the model. 
        light 2 Rays reflect off opaque objects but pass through transparent 
        objects. 

        """
        arg_str = string_util._convert_args_to_string("ray.trace", type, dx, dy, 
                                                      dz)
        py2ecotect.conversation.Exec(arg_str)

    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_depth(self):
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
        val = py2ecotect.conversation.Request("get.ray.depth")
        return string_util._convert_str_to_type(val, int)

    def set_depth(self, depth):
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
        arg_str = string_util._convert_args_to_string("set.ray.depth", depth)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_max_depth(self):
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
        val = py2ecotect.conversation.Request("get.ray.maxdepth")
        return string_util._convert_str_to_type(val, int)
    
    def set_max_depth(self, depth):
        """
        
        Sets the maximum number of reflections to which rays will be traced. 

        Parameter(s)
        This property takes the following parameters.
        
        depth 
        An integer value specifying the maximum number of reflections.
        
        """
        arg_str = string_util._convert_args_to_string("set.ray.maxdepth", depth)
        py2ecotect.conversation.Exec(arg_str)
    
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
        #TODO: check return value
        arg_str = string_util._convert_args_to_string("get.ray.object", depth)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def set_object(self, depth, object):
        """
        
        Sets the object index at the specified reflection depth. 

        Parameter(s)
        This property takes the following parameters.
        
        depth 
        An integer value representing the depth. 
        
        object 
        The zero-based index of the object.
        
        """
        arg_str = string_util._convert_args_to_string("set.ray.object", depth, 
                                                      object)
        py2ecotect.conversation.Exec(arg_str)
        
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
        arg_str = string_util._convert_args_to_string("get.ray.position", depth)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float, int)
    
    def set_position(self, depth, x, y, z, object = ""):
        """
        
        Sets the 3D position of the ray point at the given reflection depth. 

        Parameter(s)
        This property takes the following parameters.
        
        depth 
        An integer value representing the depth. 
        
        x, y, z 
        The absolute position in the X, Y and Z axis of the ray point in 3 
        dimensional model space. 
        
        [object] 
        This optional parameter specifies the zero-based index of the object 
        intersected. 
                
        """
        arg_str = string_util._convert_args_to_string("set.ray.position", depth, 
                                                      x, y, z, object)
        py2ecotect.conversation.Exec(arg_str)

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
        val = py2ecotect.conversation.Request("get.ray.source")
        return string_util._convert_str_to_list(val, float, float, float)
        
    def set_source(self, x, y, z):
        """
        
        Sets the position of the ray source. 

        Parameter(s)
        This property takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the source 
        point in 3 dimensional model space. 

        """
        arg_str = string_util._convert_args_to_string("set.ray.source", x, y, z,)
        py2ecotect.conversation.Exec(arg_str)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    depth = property(fget = get_depth, fset = set_depth, 
                        doc = "The number of reflections contained in the"
                        " currently generated ray")
    
    max_depth= property(fget = get_max_depth, fset = set_max_depth, 
                        doc = "The maximum number of reflections to which rays"
                        " will be traced")

if __name__ == "__main__":
    x = Ray()
    
    #print x.get_object(3)
    #print x.get_position(3)
    #x.set_position(3, 50, 80, 10, 1)
    #print x.get_source()
    #print x.depth
    #x.depth = 9
    

    print "Tests completed"