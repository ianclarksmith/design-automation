import py2ecotect as p2e

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
        p2e.conversation.Exec("rays.animate")
    
    def free(self):
        """
        
        Clears any existing rays or particles from the model and frees associated 
        application memory. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("rays.free")
    
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
        arg_str = p2e._util._convert_args_to_string("rays.generate", method)
        p2e.conversation.Exec(arg_str)
        
    def rewind(self):
        """
        
        Rewinds the ray animation frame counter back to the beginning. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("rays.rewind")
    
    def save(self, filename):
        """
        
        Saves the currently displayed rays or particles to an ECOTECT Ray (.ray) 
        file. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to where the ECOTECT Ray (.ray) file will be stored. 
        
        """
        arg_str = p2e._util._convert_args_to_string("rays.save", filename)
        p2e.conversation.Exec(arg_str)
    
    def step(self, steps):
        """
        
        Steps the ray animation frame counter forward by the number of steps 
        specified. 

        Parameter(s)
        This command takes the following parameters.
        
        steps 
        An integer representing the number of steps to move the counter forward.
        
        """
        arg_str = p2e._util._convert_args_to_string("rays.step", step)
        p2e.conversation.Exec(arg_str)
    
    def update(self):
        """
        
        Recalculates ray point values. Use this command when a material is 
        changed or values need updating. 

        Parameter(s)
        There are no parameters for this command.
 
        """
        p2e.conversation.Exec("rays.update")
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    @apply
    def altitude():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.altitude")
            return p2e._util._convert_str_to_type(val, float)
    
        def fset(self, angle):
            """
            
            Sets the controlling altitude angle when using the spherical or 
            cylindrical methods in the rays.spray command. 
    
            Parameter(s)
            This property takes the following parameters.
            
            angle 
            Specifies the angle to use, in decimal degrees.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.altitude", angle)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def angle():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.angle")
            return p2e._util._convert_str_to_type(val, float)
        
        def fset(self, angle):
            """
            
            Sets the angular increment between rays when using the spherical or 
            cylindrical methods in the rays.spray command. 
    
            Parameter(s)
            This property takes the following parameters.
            
            angle 
            Specifies the angle to use, in decimal degrees
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.angle", angle)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def avg_absorption():
        def fget(self, band):
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
            arg_str = p2e._util._convert_args_to_string("get.rays.avgabsorption", 
                                                          band)
            val = p2e.conversation.Request(arg_str)
            return p2e._util._convert_str_to_type(val, float)
        
        return property(**locals())
    
    @apply
    def azimuth():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.azimuth")
            return p2e._util._convert_str_to_type(val, float)
            
        def fset(self, angle):
            """
            
            Sets the controlling azimuth angle when using the spherical or 
            cylindrical methods in the rays.spray command. 
    
            Parameter(s)
            This property takes the following parameters.
            
            angle 
            The angle in degrees to use. 
    
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.azimuth", angle)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
        
    @apply
    def count():
        def fget(self):
            """
            
            Retrieves the number of rays in the ray list. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The number of rays in the ray list. 
    
            """
            val = p2e.conversation.Request("get.rays.count")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())
    
    @apply
    def distance():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.distance")
            return p2e._util._convert_str_to_type(val, float)
    
        def fset(self, dist):
            """
            
            Sets the distance on which the animation is based. It's possible to use 
            this to control the timing of an animation. 
    
            Parameter(s)
            This property takes the following parameters.
            
            dist 
            A decimal value specifying the required distance, in the current modelling units.
                    
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.distance", dist)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def edt10():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.edt10")
            return p2e._util._convert_str_to_type(val, float)
        
        return property(**locals())

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
        arg_str = p2e._util._convert_args_to_string("get.rays.flag", flag)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

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
        arg_str = p2e._util._convert_args_to_string("set.rays.flag", flag, 
                                                      state)
        p2e.conversation.Exec(arg_str)
    
    @apply
    def increment():
        def fget(self):
            """
            
            Retrieves the animation frame increment in milliseconds. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            inc 
            The current increment in milliseconds.
            
            """
            val = p2e.conversation.Request("get.rays.increment")
            return p2e._util._convert_str_to_type(val, float)
    
        def fset(self, inc):
            """
            
            Sets the animation frame increment in milliseconds. 
    
            Parameter(s)
            This property takes the following parameters.
            
            inc 
            The increment to set in milliseconds. 
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.increment", inc)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def max_distance():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.maxdistance")
            return p2e._util._convert_str_to_type(val, float)
        
        return property(**locals())
    
    @apply
    def mean_free_path_length():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.meanfreepathlength")
            return p2e._util._convert_str_to_type(val, float)
        
        return property(**locals())
    
    @apply
    def nodes():
        def fget(self):
            """
            
            Retrieves the number of ray nodes in the ray list. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The number of ray nodes in the ray list.
            
            """
            val = p2e.conversation.Request("get.rays.nodes")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())
    
    @apply
    def precision():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.precision")
            return p2e._util._convert_str_to_type(val, float)
    
        def fset(self, precision):
            """
            
            Sets the currently set distance between points when rays are generated 
            towards tagged acoustic reflectors using the reflectors method in the 
            rays.spray command. 
    
            Parameter(s)
            This property takes the following parameters.
            
            precision 
            A decimal value representing the distance.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.precision", 
                                                          precision)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def random():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.random")
            return p2e._util._convert_str_to_type(val, int)
            
        def fset(self, rays):
            """
            
            Sets the currently set number of random rays to be generated when the 
            random method is used in the rays.spray command. 
    
            Parameter(s)
            This property takes the following parameters.
            
            rays 
            An integer value respresenting the number of rays to generate. 
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.random", 
                                                          rays)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def reflections():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.reflections")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self):
            """
            
            Sets the currently set maximum number of refections to test during any 
            subsequent ray spraying calculation. 
    
            Parameter(s)
            This property takes the following parameters.
            
            bounces 
            The maximum number of reflections.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.reflections", 
                                                          bounces)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def rt60():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.rt60")
            return p2e._util._convert_str_to_type(val, float)
        
        return property(**locals())

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
        val = p2e.conversation.Request("get.rays.scale")
        return p2e._util._convert_str_to_list(val, float, float, float)
        
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
        arg_str = p2e._util._convert_args_to_string("set.rays.scale", min, 
                                                      max, inc)
        p2e.conversation.Exec(arg_str)
    
    @apply
    def source():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.source")
            return p2e._util._convert_str_to_type(val, int)
            
        def fset(self, index):
            """
            
            Sets the the SPEAKER object to be used as the sound source. 
    
            Parameter(s)
            This property takes the following parameters.
            
            index 
            The zero-based index number of the SPEAKER object to be used. If this 
            is not specified, the first visible SPEAKER object found will be used. 
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.source", index)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def units():
        def fget(self):
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
            val = p2e.conversation.Request("get.rays.units")
            return p2e._util._convert_str_to_type(val, str)
    
        def fset(self, units):
            """
            
            Sets the units used for each ray. This is also displayed at the top of 
            the legend. 
    
            Parameter(s)
            This property takes the following parameters.
            
            units 
            An text string representing the units to use. 
            
            """
            arg_str = p2e._util._convert_args_to_string("set.rays.units", units)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())

    
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

