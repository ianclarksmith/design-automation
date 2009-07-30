import py2ecotect as p2e

class Masks(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def clear(self):
        """
        
        Deletes the shading masks list and frees allocated memory. If a future 
        calculation requires shading masks, ECOTECT will attempt to re-load them 
        from the cache file on disk. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("masks.clear")

    def copy(self, _from, to):
        """
        
        Copies all day information from one shading mask to another. 

        Parameter(s)
        This command takes the following parameters.
        
        _from 
        The zero-based index of the shading mask to copy from. 
        
        to 
        The zero-based index of the shading mask to copy to.
        
        """
        arg_str = p2e._util._convert_args_to_string("masks.copy", _from, to )
        p2e.conversation.Exec(arg_str)

    def interpolate(self, index, t1, t2, fraction):
        """
        
        Interpolates between the values in two masks and stores them in a new mask. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The zero-based index of the shading mask where the interpolation will be 
        stored. 
        
        t1 
        The zero-based index of the shading mask from which the interpolation 
        will begin. 
        
        t2 
        The zero-based index of the shading mask at which the interpolation 
        will end. 
        
        fraction 
        The fractional mask bias for the interpolation, typically between 0 (t1) 
        and 1 (t2).
        
        """
        arg_str = p2e._util._convert_args_to_string("masks.interpolate", 
                                                      index, t1, t2, fraction )
        p2e.conversation.Exec(arg_str)

    def load(self):
        """
        
        Loads the shading mask list. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("masks.load")

    def save(self):
        """
        
        Saves the current shading mask list. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("masks.save")

    def update(self, index):
        """
        
        Updates the specified shading mask's information. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        """
        arg_str = p2e._util._convert_args_to_string("masks.update", index)
        p2e.conversation.Exec(arg_str)

    def add_mask(self, object = 0):
        """
        
        Adds a new shading mask to the masks list and returns the zero-based 
        index of the mask just added. 

        Parameter(s)
        This property takes the following parameters.
        
        [object] 
        This optional parameter sets the index to which the new shading mask 
        will be assigned to. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        maskIndex 
        The zero-based index of the new shading mask.
        
        """
        arg_str = p2e._util._convert_args_to_string("add.mask", object)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    @apply
    def count():
        def fget(self):
            """
            
            Returns the number of shading masks in the current list. If no masks 
            have been loaded, a value of 0 will be returned. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The number of shading masks in the list.
            
            """
            val = p2e.conversation.Request("get.masks.count")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())

    def get_data(self, index, i, j):
        """
        
        Retrieves the shading value for the specified azimuth and altitude 
        indexes in the sky. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        i 
        A value between 0 and 71 representing the azimuth angle corresponding 
        to a sky segment. 
        
        j 
        A value between 0 and 17 representing the altitude angle corresponding 
        to a sky segment. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        shading 
        A decimal value between 0 (unshaded) and 1 (fully shaded) representing 
        the effective shading of the object whose shadng mask is specified. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.masks.data", index, i, 
                                                     j)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_data(self, index, i, j, value):
        """
        
        Sets the shading value for the specified at the given azimuth and 
        altitude indexes over the sky. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        i 
        A value between 0 and 71 representing the azimuth angle as an index 
        corresponding to a sky segment. 
        
        j 
        A value between 0 and 17 representing the altitude angle as an index 
        corresponding to a sky segment. 
        
        value 
        A decimal value between 0 (unshaded) and 1 (fully shaded) representing 
        the effective shading of the object whose shading mask is specified.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.masks.data", index, i, 
                                                     j, value)
        p2e.conversation.Exec(arg_str)

    def get_object(self, index):
        """
        
        Retrieves the zero-based index of the object to which the specified mask 
        belongs. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        object 
        The zero-based index of the object.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.masks.object", index)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

    def set_object(self, index, object):
        """
        
        Sets the object to which the specified mask will belong. You can use 
        this property to change shading masks at any time during a calculation. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        object 
        The zero-based index of the object. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.masks.object", index, 
                                                      object)
        p2e.conversation.Exec(arg_str)

    def get_percentage(self, index):
        """
        
        Returns the percentage-in-shade of the object/mask at the current model 
        date and time as a single decimal percentage value. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        shading 
        A decimal value between 0 (unshaded) and 100 (fully shaded) representing 
        the effective percentage shading of the object whose shading mask is 
        specified. 
        
        cosAngle 
        A decimal fraction representing the effect of direct incidence. This is 
        equal to the cosine of the 3D incidence angle between the centre-point 
        of the sky segment and the surface normal of the object represented by 
        the mask.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.masks.percentage", index)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float)

    def get_percentage_angle(self, index, azi, alt):
        """
        
        Returns the percentage-in-shade of the specified mask as a single 
        decimal percentage value from a source located at the given angles. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        azi 
        The azimuth (-180 deg to 180 deg) angle representing, together with the 
        altitude angle, a point in the sky from which to retrieve the value. To 
        retrieve the sun position at any time, use the model.sunangles property. 
        
        alt 
        The altitude (0 deg to 90 deg) angle representing, together with the azimuth 
        angle, a point in the sky from which to retrieve the value. To retrieve 
        the sun position at any time, use the model.sunangles property. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        shading 
        A decimal value between 0 (unshaded) and 100 (fully shaded) representing 
        the effective percentage shading of the object whose shading mask is 
        specified. 
        
        cosAngle 
        A decimal fraction representing the effect of direct incidence. This is 
        equal to the cosine of the 3D incidence angle between the centre-point 
        of the sky segment and the surface normal of the object represented by 
        the mask.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.masks.percentage.angle", 
                                                     index, azi, alt)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float)

    def get_percentage_datetime(self, index, day, time):
        """
        
        Returns the percentage-in-shade of the selected object's mask as a 
        single decimal percentage value at the given date and time. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        day 
        The Julian date of the year (1-365) for the percentage value to return. 
        
        time 
        The time of the day to use in decimal hours (0.0-23.99). 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        shading 
        A decimal value between 0 (unshaded) and 100 (fully shaded) representing 
        the effective percentage shading of the object whose shading mask is 
        specified. 
        
        cosAngle 
        A decimal fraction representing the effect of direct incidence. This is 
        equal to the cosine of the 3D incidence angle between the centre-point 
        of the sky segment and the surface normal of the object represented by 
        the mask.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.masks.percentage.datetime", 
                                                     index, day, time)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float)

    def get_percentage_index(self, index, x, y):
        """
        
        Returns the percentage-in-shade of the specified object's mask as a 
        single decimal percentage value. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        x 
        The X index of the shading table, where X is the azimuth angle increment 
        set in the set.shading.angles property. 
        
        y 
        The Y index of the shading table, where Y is the altitude angle increment 
        set in the set.shading.angles property. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        shading 
        A decimal value between 0 (unshaded) and 100 (fully shaded) representing 
        the effective percentage shading of the object whose shading mask is 
        specified. 
        
        cosAngle 
        A decimal fraction representing the effect of direct incidence. This is 
        equal to the cosine of the 3D incidence angle between the centre-point 
        of the sky segment and the surface normal of the object represented by 
        the mask.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.masks.percentage.index", 
                                                     index, x, y)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float)

    def get_shading(self, index, azi, alt):
        """
        
        Returns the shading value, a decimal value between 0 (unshaded) and 1 
        (fully shaded), representing the effective percentage of the exposed 
        surface area of the object that is in shade for the specified sky angles. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        azi 
        The azimuth angle, in degrees, representing the compass direction, with 
        North being 0 deg. 
        
        alt 
        The altitude angle with 0 deg representing horizontal direction and 90 deg
        being vertical. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value, between 0 (unshaded) and 1 (fully shaded).
        
        """
        arg_str = p2e._util._convert_args_to_string("get.masks.shading", index, 
                                                     azi, alt)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_shading(self, index, azi, alt, value):
        """
        
        Sets the shading value, representing the effective percentage of the 
        object/mask that is in shade using the specified sky angles. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        azi 
        The azimuth angle, in degrees, representing the compass direction with 
        North being 0 deg. 
        
        alt 
        The altitude angle with 0 deg representing horizontal direction and 90 deg 
        being vertical. 
        
        value 
        A decimal value, between 0 (unshaded) and 1 (fully shaded). 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.masks.shading", index, 
                                                     azi, alt, value)
        p2e.conversation.Exec(arg_str)

if __name__ == "__main__":
    x = Masks()
    
    #x.clear()
    #x.copy(1, 5)
    # x.interpolate(10, 2, 5, 0.5)
    #x.load()
    #x.save()
    #x.update(1)
    #print x.add_mask(3)
    #print x.get_count()
    #print x.get_data(4, 9, 8)
    #x.set_data(4, 9, 8, 0.225)
    #print x.get_object(2)
    #print x.get_percentage(1)
    #print x.get_percentage_angle(1, 45, 90)
    #print x.get_percentage_datetime(4, 300, 15)
    #print x.get_percentage_index(1, 5, 5)
    #print x.get_shading(4, 0, 45)
    #x.set_shading(1, 0, 45, 0.5)
    #print x.count
    
    
    print "Tests completed"
