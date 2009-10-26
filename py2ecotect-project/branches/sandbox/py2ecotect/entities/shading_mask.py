import py2ecotect as p2e

#==============================================================================
# _ShadingMaskObjs
#==============================================================================
class _ShadingMaskObjs(object):
    
    def object(self):
        """
        
        Retrieves the object to which the specified mask belongs. 

        Parameter(s)
        This property takes no parameters.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        object 
        The zero-based index of the object.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.masks.object", 
                                                          self._mask._eco_id)
        val = p2e._app.Request(arg_str)
        index = p2e._base._util._convert_str_to_type(val, int)
        return p2e.model._objects[index]

    def set_object(self, object):
        """
        
        Sets the object to which the specified mask will belong. You can use 
        this property to change shading masks at any time during a calculation. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The object. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.masks.object", 
                                                          self._mask._eco_id, 
                                                          object._eco_id)
        p2e._app.Exec(arg_str)
        

        
#==============================================================================
# _ShadingMaskDupl
#==============================================================================
class _ShadingMaskDupl(object):
    
    def copy_data(self, to_mask):
        """
        
        Copies all day information from one shading mask to another. 

        Parameter(s)
        This command takes the following parameters.
        
        to_mask 
        The shading mask to copy to.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("masks.copy", 
                                                          self._mask._eco_id, 
                                                          to_mask._mask._eco_id)
        p2e._app.Exec(arg_str)

    def interpolate_data(self, mask_1, mask_2, fraction):
        """
        
        Interpolates between the values in two masks and stores them in a new mask. 

        Parameter(s)
        This command takes the following parameters.
        
        mask_1 
        The shading mask from which the interpolation 
        will begin. 
        
        mask_2 
        The shading mask at which the interpolation 
        will end. 
        
        fraction 
        The fractional mask bias for the interpolation, typically between 0 (mask_1) 
        and 1 (mask_2).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("masks.interpolate", 
                                                          self._mask._eco_id, 
                                                          mask_1._mask._eco_id,
                                                          mask_2._mask._eco_id, 
                                                          fraction )
        p2e._app.Exec(arg_str)   

#==============================================================================
# _ShadingMaskProp
#==============================================================================
class _ShadingMaskProp(object):
    def update(self):
        """
        
        Updates the specified shading mask's information. 

        Parameter(s)
        This command takes no parameters.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("masks.update", 
                                                          self._mask._eco_id)
        p2e._app.Exec(arg_str)  
    def shading_by_segment(self, azi_segment, alt_segment):
        """
        
        Retrieves the shading value for the specified azimuth and altitude 
        indexes in the sky. 

        Parameter(s)
        This property takes the following parameters.
        
        azi_segment 
        A value between 0 and 71 representing the azimuth angle corresponding 
        to a sky segment. 
        
        alt_segment 
        A value between 0 and 17 representing the altitude angle corresponding 
        to a sky segment. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        shading 
        A decimal value between 0 (unshaded) and 1 (fully shaded) representing 
        the effective shading of the object whose shadng mask is specified. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.masks.data", 
                                                          self._mask._eco_id, 
                                                          azi_segment,
                                                          alt_segment) 
                                                     
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_shading_by_segment(self, azi_segment, alt_segment, value):
        """
        
        Sets the shading value for the specified at the given azimuth and 
        altitude indexes over the sky. 

        Parameter(s)
        This property takes the following parameters.
        
        azi_segment 
        A value between 0 and 71 representing the azimuth angle as an index 
        corresponding to a sky segment. 
        
        alt_segment 
        A value between 0 and 17 representing the altitude angle as an index 
        corresponding to a sky segment. 
        
        value 
        A decimal value between 0 (unshaded) and 1 (fully shaded) representing 
        the effective shading of the object whose shading mask is specified.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.masks.data", 
                                                          self._mask._eco_id, 
                                                          azi_segment,
                                                          alt_segment, 
                                                          value) 
                                                     
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def shading_by_azi_alt(self, azi, alt):
        """
        
        Returns the shading value, a decimal value between 0 (unshaded) and 1 
        (fully shaded), representing the effective percentage of the exposed 
        surface area of the object that is in shade for the specified sky angles. 

        Parameter(s)
        This property takes the following parameters.
        
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
        arg_str = p2e._base._util._convert_args_to_string("get.masks.shading", 
                                                          self._mask._eco_id, 
                                                          azi, alt)
                                                     
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_shading_by_azi_alt(self, azi, alt, value):
        """
        
        Sets the shading value, representing the effective percentage of the 
        object/mask that is in shade using the specified sky angles. 

        Parameter(s)
        This property takes the following parameters.
        
        azi 
        The azimuth angle, in degrees, representing the compass direction with 
        North being 0 deg. 
        
        alt 
        The altitude angle with 0 deg representing horizontal direction and 90 deg 
        being vertical. 
        
        value 
        A decimal value, between 0 (unshaded) and 1 (fully shaded). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.masks.shading", 
                                                          self._mask._eco_id, 
                                                          azi, alt, value)
                                                     
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def result_percentage_by_current_day_time(self):
        """
        
        Returns the percentage-in-shade of the object/mask at the current model 
        date and time as a single decimal percentage value. 

        Parameter(s)
        This property takes no parameters.
        
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
        arg_str = p2e._base._util._convert_args_to_string("get.masks.percentage", 
                                                          self._mask._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float)
    
    def result_percentage_by_table_index(self, x, y):
        """
        
        Returns the percentage-in-shade of the specified object's mask as a 
        single decimal percentage value. 

        Parameter(s)
        This property takes the following parameters.
        
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
        arg_str = p2e._base._util._convert_args_to_string("get.masks.percentage.index", 
                                                     self._mask._eco_id, x, y)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float)
    
    def result_percentage_by_azi_alt(self, azi, alt):
        """
        
        Returns the percentage-in-shade of the specified mask as a single 
        decimal percentage value from a source located at the given angles. 

        Parameter(s)
        This property takes the following parameters.
        
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
        arg_str = p2e._base._util._convert_args_to_string("get.masks.percentage.angle", 
                                                     self._mask._eco_id, azi, alt)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float)

    def result_percentage_by_day_time(self, day, time):
        """
        
        Returns the percentage-in-shade of the selected object's mask as a 
        single decimal percentage value at the given date and time. 

        Parameter(s)
        This property takes the following parameters.
        
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
        arg_str = p2e._base._util._convert_args_to_string("get.masks.percentage.datetime", 
                                                     self._mask._eco_id, day, time)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float)




#================================================================================
# ShadingMask
#================================================================================
class ShadingMask(object):    
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    class objs(_ShadingMaskObjs):
        def __init__(self, _mask):
            self._mask = _mask
    class dupl(_ShadingMaskDupl):
        def __init__(self, _mask):
            self._mask = _mask
    class prop(_ShadingMaskProp):
        def __init__(self, _mask):
            self._mask = _mask       

    #--------------------------------------------------------------------------
    #constructor 
    def __init__(self, zone_eco_id):
        
        #update model list
        p2e.model._masks.append(self)
        assert self._eco_id == zone_eco_id
        
        #create instances of the nested classes
        self.objs = ShadingMask.objs(self)
        self.dupl = ShadingMask.dupl(self)
        self.prop = ShadingMask.prop(self)
            
    @staticmethod
    def create(object = 0):
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
        arg_str = p2e._base._util._convert_args_to_string("add.mask", object)
        val = p2e._app.Request(arg_str)
        eco_id = p2e._base._util._convert_str_to_type(val, int)
        
        #return the zone
        return ShadingMask(eco_id)
        
    #===========================================================================
    # Properties
    #===========================================================================
    #id property  
    @apply
    def _eco_id():
        def fget(self):
            """
            
            Id of the mask
        
            """
            return p2e.model._masks.index(self)

        return property(**locals())



