import py2ecotect
from py2ecotect import string_util

class Rays(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def animate(self):
        """
        
        Begins the ray animation from the current position of the animation frame counter. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("rays.animate")
    
    def free(self):
        """
        
        Clears any existing rays or particles from the model and frees associated application memory. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("rays.free")
    
    def generate(self, method):
        """
        
        Sprays rays from the currently defined source point. 

        Parameter(s)
        This command takes the following parameters.
        
        method 
        The method used to spray as specified in the following Ray Spray Methods 
        table. 
        
        Relevant Data Table(s)
        
        Ray Spray Methods 
        Token Value Description 
        reflectors 0 Spray rays only at objects tagged as an acoustic reflector. 
        random 1 Spray rays in random directions. 
        spherical 2 Spray evenly distributed rays spherically. 
        cylindrical 3 Spray a circle of rays in one plane. 

        """
        arg_str = string_util._convert_args_to_string("rays.generate", method)
        py2ecotect.conversation.Exec(arg_str)
        
    def rewind(self):
        """
        
        Rewinds the ray animation frame counter back to the beginning. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("rays.rewind")
    
    def save(self, filename):
        """
        
        Saves the currently displayed rays or particles to an ECOTECT Ray (.ray) file. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to where the ECOTECT Ray (.ray) file will be stored. 
        
        """
        arg_str = string_util._convert_args_to_string("rays.save", filename)
        py2ecotect.conversation.Exec(arg_str)
    
    def step(self, steps):
        """
        
        Steps the ray animation frame counter forward by the number of steps specified. 

        Parameter(s)
        This command takes the following parameters.
        
        steps 
        An integer representing the number of steps to move the counter forward.
        
        """
        arg_str = string_util._convert_args_to_string("rays.step", step)
        py2ecotect.conversation.Exec(arg_str)
    
    def update(self):
        """
        
        Recalculates ray point values. Use this command when a material is 
        changed or values need updating. 

        Parameter(s)
        There are no parameters for this command.
 
        """
        py2ecotect.conversation.Exec("rays.update")
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_altitude(self):
        """
        
        Retrieves the controlling altitude angle when using the spherical or 
        cylindrical methods in the rays.spray command. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        alt 
        The altitude in degrees. 
        
        """
        val = py2ecotect.conversation.Request("get.rays.altitude")
        return string_util._convert_str_to_type(val, float)

    def set_altitude(self, angle):
        """
        
        Sets the controlling altitude angle when using the spherical or 
        cylindrical methods in the rays.spray command. 

        Parameter(s)
        This property takes the following parameters.
        
        angle 
        Specifies the angle to use, in decimal degrees.
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.altitude", angle)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_angle(self):
        """
        
        Retrieves the angular increment between rays when using the spherical or 
        cylindrical methods in the rays.spray command. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        angle 
        The angular increment in degrees.
        
        """
        val = py2ecotect.conversation.Request("get.rays.angle")
        return string_util._convert_str_to_type(val, float)
    
    def set_angle(self, angle):
        """
        
        Sets the angular increment between rays when using the spherical or 
        cylindrical methods in the rays.spray command. 

        Parameter(s)
        This property takes the following parameters.
        
        angle 
        Specifies the angle to use, in decimal degrees
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.angle", angle)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_avg_absorption(self, band):
        """
        
        Retrieves the average absorption co-efficient of all incident rays at 
        the given frequency band. 

        Parameter(s)
        This property takes the following parameters.
        
        band 
        An index of the frequency corresponding to the following Centre 
        Frequencies table. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        avgabs 
        A decimal value containing the average absorption co-efficient. 
        
        Relevant Data Table(s)
        
        Octave Frequencies 
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
        arg_str = string_util._convert_args_to_string("get.rays.avgabsorption", 
                                                      band)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_azimuth(self):
        """
        
        Retrieves the controlling azimuth angle when using the spherical or cylindrical methods in the rays.spray command. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        azi 
        The azimuth in degrees. 
        
        """
        val = py2ecotect.conversation.Request("get.rays.azimuth")
        return string_util._convert_str_to_type(val, float)
        
    def set_azimuth(self, angle):
        """
        
        Sets the controlling azimuth angle when using the spherical or 
        cylindrical methods in the rays.spray command. 

        Parameter(s)
        This property takes the following parameters.
        
        angle 
        The angle in degrees to use. 

        """
        arg_str = string_util._convert_args_to_string("set.rays.azimuth", angle)
        py2ecotect.conversation.Exec(arg_str)

    def get_count(self):
        """
        
        Retrieves the number of rays in the ray list. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        count 
        The number of rays in the ray list. 

        """
        val = py2ecotect.conversation.Request("get.rays.count")
        return string_util._convert_str_to_type(val, int)

    def get_distance(self):
        """
        
        Retrieves the distance on which the animation is based. It is possible 
        to use this to find the travel distance of the longest ray. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dist 
        A decimal value containing the distance. 

        """
        val = py2ecotect.conversation.Request("get.rays.distance")
        return string_util._convert_str_to_type(val, float)

    def set_distance(self, dist):
        """
        
        Sets the distance on which the animation is based. It's possible to use 
        this to control the timing of an animation. 

        Parameter(s)
        This property takes the following parameters.
        
        dist 
        A decimal value specifying the required distance, in the current modelling units.
                
        """
        arg_str = string_util._convert_args_to_string("set.rays.distance", dist)
        py2ecotect.conversation.Exec(arg_str)

    def get_edt10(self):
        """
        
        Retrieves the Reverberation Time over 60dB taken from the line-of-best 
        fit of all currently stored acoustic rays. Note that this value is only 
        set during a calculation - see calc.acousticresponse for more 
        information. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        edt10 
        A decimal value containing the early decay time in seconds.
        
        """
        val = py2ecotect.conversation.Request("get.rays.edt10")
        return string_util._convert_str_to_type(val, float)

















        


if __name__ == "__main__":
    x = Rays()
    
    #print x.get_altitude()
    #x.set_altitude(54)
    

    print "Tests completed"

