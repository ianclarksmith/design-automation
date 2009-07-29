import py2ecotect
from py2ecotect import string_util

class Rays(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def animate(self):
        """
        
        Begins the ray animation from the current position of the animation 
        frame counter. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("rays.animate")
    
    def free(self):
        """
        
        Clears any existing rays or particles from the model and frees associated 
        application memory. 

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
        
        Saves the currently displayed rays or particles to an ECOTECT Ray (.ray) 
        file. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to where the ECOTECT Ray (.ray) file will be stored. 
        
        """
        arg_str = string_util._convert_args_to_string("rays.save", filename)
        py2ecotect.conversation.Exec(arg_str)
    
    def step(self, steps):
        """
        
        Steps the ray animation frame counter forward by the number of steps 
        specified. 

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
        
        Retrieves the controlling azimuth angle when using the spherical or 
        cylindrical methods in the rays.spray command. 

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

    def get_flag(self, flag):
        """
        
        Retrieves the current state of the specified flag. These properties 
        control how ECOTECT displays ray objects in both the view and opengl 
        canvases. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value or token corresponding to the following Rays Flag 
        Codes table. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        A boolean value with the current state of the flag. This is a boolean 
        value where 1 is set and 0 means unset. 
        
        Relevant Data Table(s)
        
        Rays Flag Codes 
        Token Value Description 
        rotate 1 Display rays while rotating model. 
        testonly 2 Test only acoustic reflectors when generating rays. 
        show 4 Display rays or particles within the model. 
        numeric 8 Display sound levels as text for each ray. 
        relative 16 Colour rays by relative sound level. 
        depth 128 Colour rays by reflection depth. 
        hide 256 Hide rays below specified sound level. 
        fat 512 Show particles using fat pixels. 
        arrows 1024 Show rays as arrows. 
        wheel 2048 Control ray animation using mouse wheel. 

        """
        arg_str = string_util._convert_args_to_string("get.rays.flag", flag)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def set_flag(self, flag, state = True):
        """
        
        Sets the options for how ECOTECT displays ray objects in both the view 
        and opengl canvases. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value or token corresponding to the following Rays Flag Codes table. 
        
        [state] 
        This optional parameter specifies whether to set the specified flag or 
        not. This is a boolean value where 1 or true represents the affirmative 
        and 0 or false the negative. If not given, this parameter defaults to 
        true if not specified. 
        
        Relevant Data Table(s)
        
        Rays Falg Codes 
        Token Value Description 
        rotate 1 Display rays while rotating model. 
        testonly 2 Test only acoustic reflectors when generating rays. 
        show 4 Display rays or particles within the model. 
        numeric 8 Display sound levels as text for each ray. 
        relative 16 Colour rays by relative sound level. 
        depth 128 Colour rays by reflection depth. 
        hide 256 Hide rays below specified sound level. 
        fat 512 Show particles using fat pixels. 
        arrows 1024 Show rays as arrows. 
        wheel 2048 Control ray animation using mouse wheel. 
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.flag", flag, 
                                                      state)
        py2ecotect.conversation.Exec(arg_str)

    def get_increment(self):
        """
        
        Retrieves the animation frame increment in milliseconds. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        inc 
        The current increment in milliseconds.
        
        """
        val = py2ecotect.conversation.Request("get.rays.increment")
        return string_util._convert_str_to_type(val, float)

    def set_increment(self, inc):
        """
        
        Sets the animation frame increment in milliseconds. 

        Parameter(s)
        This property takes the following parameters.
        
        inc 
        The increment to set in milliseconds. 
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.increment", inc)
        py2ecotect.conversation.Exec(arg_str)

    def get_max_distance(self):
        """
        
        Retrieves the maximum distance travelled by the longest ray. This is 
        useful to know when changing the rays.distance property. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        distance 
        The maximum distance travelled. 

        """
        val = py2ecotect.conversation.Request("get.rays.maxdistance")
        return string_util._convert_str_to_type(val, float)

    def get_mean_free_path_length(self):
        """
        
        Retrieves the average travel distance between striking surfaces, 
        averaged over all traced rays. Note that this value is only set during 
        a calculation - see calc.acousticresponse for more information. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        length 
        A decimal value containing the mean free path length. 

        """
        val = py2ecotect.conversation.Request("get.rays.meanfreepathlength")
        return string_util._convert_str_to_type(val, float)

    def get_nodes(self):
        """
        
        Retrieves the number of ray nodes in the ray list. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        count 
        The number of ray nodes in the ray list.
        
        """
        val = py2ecotect.conversation.Request("get.rays.nodes")
        return string_util._convert_str_to_type(val, int)

    def get_precision(self):
        """
        
        Retrieves the distance between points when rays are generated towards 
        tagged acoustic reflectors using the reflectors method in the 
        rays.spray command. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        precision 
        A decimal value containing the distance. 
        
        """
        val = py2ecotect.conversation.Request("get.rays.precision")
        return string_util._convert_str_to_type(val, float)

    def set_precision(self, precision):
        """
        
        Sets the currently set distance between points when rays are generated 
        towards tagged acoustic reflectors using the reflectors method in the 
        rays.spray command. 

        Parameter(s)
        This property takes the following parameters.
        
        precision 
        A decimal value representing the distance.
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.precision", 
                                                      precision)
        py2ecotect.conversation.Exec(arg_str)

    def get_random(self):
        """
        
        Retrieves the currently set number of random rays to be generated when 
        the random method is used in the rays.spray command. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        rays 
        An integer value respresenting the number of rays generated. 

        """
        val = py2ecotect.conversation.Request("get.rays.random")
        return string_util._convert_str_to_type(val, int)
        
    def set_random(self, rays):
        """
        
        Sets the currently set number of random rays to be generated when the 
        random method is used in the rays.spray command. 

        Parameter(s)
        This property takes the following parameters.
        
        rays 
        An integer value respresenting the number of rays to generate. 
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.random", 
                                                      rays)
        py2ecotect.conversation.Exec(arg_str)

    def get_reflections(self):
        """
        
        Retrieves the currently set maximum number of refections to test during 
        any subsequent ray spraying calculation. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        bounces 
        The maximum number of reflections.
        
        """
        val = py2ecotect.conversation.Request("get.rays.reflections")
        return string_util._convert_str_to_type(val, int)

    def set_reflections(self):
        """
        
        Sets the currently set maximum number of refections to test during any 
        subsequent ray spraying calculation. 

        Parameter(s)
        This property takes the following parameters.
        
        bounces 
        The maximum number of reflections.
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.reflections", 
                                                      bounces)
        py2ecotect.conversation.Exec(arg_str)

    def get_rt60(self):
        """
        
        Retrieves the value of the currently set Reverberation Time o ver 60dB 
        taken from the line-of-best fit of all currently stored acoustic rays. 
        Note that this value is only set during a calculation - see 
        calc.acousticresponse for more information. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        rt60 
        A decimal value containing the reverberation time in seconds. 
        
        """
        val = py2ecotect.conversation.Request("get.rays.rt60")
        return string_util._convert_str_to_type(val, float)

    def get_scale(self):
        """
        
        Retrieves the current set values of min and max. These refer to the 
        values used to colour each ray or point and is displayed in the legend. 
        The range is from min to max, where a point with a value less than or 
        equal to min will be displayed with the lowest colour, interpolated up 
        through to max where the highest colour is used. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        min 
        The minimum value in the rays legend scale. 
        
        max 
        The maximum value in the rays legend scale. 
        
        inc 
        A decimal value containing the scale increment 
        
        """
        val = py2ecotect.conversation.Request("get.rays.scale")
        return string_util._convert_str_to_list(val, float, float, float)
        
    def set_scale(self, min, max, inc):
        """
        
        Sets the values of min and max. These refer to the values used to 
        colour each ray or point and is displayed in the legend. The range is 
        from min to max, where a point with a value less than or equal to min 
        will be displayed with the lowest colour, interpolated up through to 
        max where the highest colour is used. 

        Parameter(s)
        This property takes the following parameters.
        
        min 
        A decimal value representing the minimum value to use. 
        
        max 
        A decimal value representing the maximum value to use. 
        
        inc 
        A decimal value representing the scale increment. 
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.scale", min, 
                                                      max, inc)
        py2ecotect.conversation.Exec(arg_str)

    def get_source(self):
        """
        
        Retrieves the zero-based index number of the SPEAKER object currently 
        being used as the sound source. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index number of the SPEAKER object to be used.
        
        """
        val = py2ecotect.conversation.Request("get.rays.source")
        return string_util._convert_str_to_type(val, int)
        
    def set_source(self, index):
        """
        
        Sets the the SPEAKER object to be used as the sound source. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index number of the SPEAKER object to be used. If this 
        is not specified, the first visible SPEAKER object found will be used. 
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.source", index)
        py2ecotect.conversation.Exec(arg_str)

    def get_units(self):
        """
        
        Retrieves the units currently being used for each ray. This value is 
        also displayed at the top of the legend. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        units 
        An text string representing the units to use. 
        
        """
        val = py2ecotect.conversation.Request("get.rays.units")
        return string_util._convert_str_to_type(val, str)

    def set_units(self, units):
        """
        
        Sets the units used for each ray. This is also displayed at the top of 
        the legend. 

        Parameter(s)
        This property takes the following parameters.
        
        units 
        An text string representing the units to use. 
        
        """
        arg_str = string_util._convert_args_to_string("set.rays.units", units)
        py2ecotect.conversation.Exec(arg_str)

    #===========================================================================
    # Properties
    #===========================================================================
    
    altitude = property(fget = get_altitude, fset = set_altitude, 
                        doc = "The controlling altitude angle when using the"
                        " spherical or cylindrical methods in the"
                        " rays.spray command")
    
    angle = property(fget = get_angle, fset = set_angle, 
                        doc = "The angular increment between rays when using"
                        " the spherical or cylindrical methods in the"
                        " rays.spray command")
    
    avg_absorption= property(fget = get_avg_absorption, doc = "The average"
                             " absorption co-efficient of all incident rays at"
                             " the given frequency band")
    
    azimuth = property(fget = get_azimuth, fset = set_azimuth, 
                        doc = "The controlling azimuth angle when using the"
                        " spherical or cylindrical methods in the"
                        " rays.spray command")
    
    count = property(fget = get_count, doc = "The number of rays in the ray list")
    
    distance = property(fget = get_distance, fset = set_distance, 
                        doc = "The distance on which the animation is based."
                        " It is possible to use this to find the travel"
                        " distance of the longest ray")
    
    edt10 = property(fget = get_edt10, doc = "The Reverberation Time over 60dB"
                     " taken from the line-of-best fit of all currently stored"
                     " acoustic rays")
    
    increment = property(fget = get_increment, fset = set_increment, 
                        doc = "The animation frame increment in milliseconds")
    
    max_distance = property(fget = get_max_distance, doc = "The maximum"
                            " distance travelled by the longest ray")
    
    mean_free_path_length = property(fget = get_mean_free_path_length, 
                        doc = "The average travel distance between striking"
                        " surfaces, averaged over all traced rays")
    
    nodes = property(fget = get_nodes, doc = "The number of ray nodes in the"
                     " ray list")
    
    precision = property(fget = get_precision, fset = set_precision, 
                        doc = "The distance between points when rays are"
                        " generated towards tagged acoustic reflectors using"
                        " the reflectors method in the rays.spray command")
    
    random = property(fget = get_random, fset = set_random, 
                        doc = "The currently set number of random rays to be"
                        " generated when the random method is used in the"
                        " rays.spray command")
    
    reflections = property(fget = get_reflections, fset = set_reflections, 
                        doc = "The currently set maximum number of refections"
                        " to test during any subsequent ray spraying calculation")
    
    rt60 = property(fget = get_rt60, doc = "The value of the currently set"
                    " Reverberation Time o ver 60dB taken from the line-of-best"
                    " fit of all currently stored acoustic rays")
    
    source = property(fget = get_source, fset = set_source, 
                        doc = "The zero-based index number of the SPEAKER"
                        " object currently being used as the sound source")
    
    units  = property(fget = get_units, fset = set_units, 
                        doc = "The units used for each ray. This is also"
                        " displayed at the top of the legend")








     


if __name__ == "__main__":
    x = Rays()
    
    #print x.get_altitude()
    #x.set_altitude(54)
    #print x.get_max_distance()
    #print x.get_reflections()
    #print x.get_scale()
    #print x.units
    #x.units = "TEST"
    

    print "Tests completed"

