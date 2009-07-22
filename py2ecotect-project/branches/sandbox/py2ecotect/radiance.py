import py2ecotect
from py2ecotect import string_util

class Radiance(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def load(self, filename = ""):
        """
        
        Loads the radiance point data file into ECOTECT. 

        Parameter(s)
        This command takes the following parameters.
        
        [filename] 
        This optional filename parameter must point to a file containing point 
        or object data calculated using the Generate Point Data Option in the 
        Radiance Export dialog. It must also directly correspond to either the 
        current analysis grid or the attributes of objects in the model. If the 
        filename parameter is not given, ECOTECT uses the last output file used 
        by its Radiance calculation functions.
        
        """
        arg_str = string_util._convert_args_to_string("radiance.load", filename)
        py2ecotect.conversation.Exec(arg_str)

    def load_grid(self, filename = ""):
        """
        
        Loads the radiance point data file into ECOTECT, as grid data. 

        Parameter(s)
        This command takes the following parameters.
        
        [filename] 
        This optional filename parameter must point to a file containing point 
        or object data calculated using the Generate Point Data Option in the 
        Radiance Export dialog. It must also directly correspond to either the 
        current analysis grid or the attributes of objects in the model. If the 
        filename parameter is not given, ECOTECT uses the last output file used 
        by its Radiance calculation functions. 

        """
        arg_str = string_util._convert_args_to_string("radiance.load.grid", 
                                                      filename)
        py2ecotect.conversation.Exec(arg_str)

    def load_object(self, filename = ""):
        """
        
        Loads the radiance point data file into ECOTECT, as object data. 

        Parameter(s)
        This command takes the following parameters.
        
        [filename] 
        This optional filename parameter must point to a file containing point 
        or object data calculated using the Generate Point Data Option in the 
        Radiance Export dialog. It must also directly correspond to either the 
        current analysis grid or the attributes of objects in the model. If the 
        filename parameter is not given, ECOTECT uses the last output file used 
        by its Radiance calculation functions.
        
        """
        arg_str = string_util._convert_args_to_string("radiance.load.object", 
                                                      filename)
        py2ecotect.conversation.Exec(arg_str)

    def render(self, filename):
        """
        
        Begins the radiance rendering process. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full directory path of where the rendering output will be stored. 

        """
        arg_str = string_util._convert_args_to_string("radiance.render", 
                                                      filename)
        py2ecotect.conversation.Exec(arg_str)

    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_action(self):
        """
        
        Retrieves the current set radiance render action setting. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        An integer value corresponding to the following Radiance Actions table. 
        
        Relevant Data Table(s)
        Radiance Actions 
        Value Description 
        0 Save Only 
        1 Run RadTool 
        2 Interactive Render 
        3 Final Render (Default) 
        
        """
        val = py2ecotect.conversation.Request("get.radiance.action")
        return string_util._convert_str_to_type(val, int)

    def set_action(self, action = 3):
        """
        
        Sets the radiance render action setting. 

        Parameter(s)
        This property takes the following parameters.
        
        [action] 
        This optional parameter is an integer value corresponding to the 
        following Radiance Actions table. If this is not specified, the action 
        will default to a full and final render (3). 
        
        Relevant Data Table(s)
        
        Radiance Actions 
        Value Description 
        0 Save Only 
        1 Run RadTool 
        2 Interactive Render 
        3 Final Render (Default) 

        """
        arg_str = string_util._convert_args_to_string("set.radiance.action", 
                                                     action)
        py2ecotect.conversation.Exec(arg_str)

    def get_detail(self):
        """
        
        Retrieves the current level of geometric complexity within the model. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        detail 
        An integer value corresponding to the following Radiance Settings table. 
        
        Relevant Data Table(s)
        
        Radiance Settings 
        Token Value Description 
        low 0 Low 
        medium 1 Medium 
        high 2 High 

        """
        val = py2ecotect.conversation.Request("get.radiance.detail")
        return string_util._convert_str_to_type(val, int)

    def set_detail(self, detail):
        """
        
        Sets the current level of geometric complexity within the model. 

        Parameter(s)
        This property takes the following parameters.
        
        detail 
        A value corresponding to the following Radiance Settings table. 
        This parameter can be set as a token or a value. 
        
        Relevant Data Table(s)
        Radiance Settings 
        Token Value Description 
        low 0 Low 
        medium 1 Medium 
        high 2 High 

        """
        arg_str = string_util._convert_args_to_string("set.radiance.detail", 
                                                     detail)
        py2ecotect.conversation.Exec(arg_str)

    def get_flag(self, flag):
        """
        
        Retrieves the current setting for the specified flag. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value specifying the flag, information of which to retrieve, 
        according to the following Radiance Flag Codes table. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        Whether or not the specified flag is set. This is a boolean value where 
        1 means it is set and 0 means it isn't. 
        
        Relevant Data Table(s)
        
        Radiance Flag Codes 
        Value Description 
        1 Save as seperate zone files 
        2 Use current model view 
        4 Check for Material.rad files 
        8 Generate RIF file 
        16 Include material definitions 
        32 Include camera views 
        64 Use DOS 8.3 filenames 
        128 Use ECOTECT sun angles 
        256 Check for #Zone.rad files 
        512 Render an Illuminance image 
        1024 Use ECOTECT design sky value  
        2048 Render a Daylight Factor image 
        4096 Generate Point Data for analysis  
        32768 Do not display images when complete  

        """
        arg_str = string_util._convert_args_to_string("get.radiance.flag", 
                                                     flag)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def set_flag(self, flag, state = True):
        """
        
        Sets or resets the specified radiance option flag(s). 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value specifying the flag to modify according to the 
        following Radiance Flag Codes table. To modify multiple flags at once, 
        simply add their values together. 
        
        [state] 
        This optional parameter specifies whether or not to set the specified 
        flag. This is a boolean value where 1 or true represents the 
        affirmative and 0 or false the negative. If not specified, this 
        defaults to true. 
        
        Relevant Data Table(s)
        
        Radiance Flag Codes V
        alue Description 
        1 Save as seperate zone files 
        2 Use current model view 
        4 Check for Material.rad files 
        8 Generate RIF file 
        16 Include material definitions 
        32 Include camera views 
        64 Use DOS 8.3 filenames 
        128 Use ECOTECT sun angles 
        256 Check for #Zone.rad files 
        512 Render an Illuminance image 
        1024 Use ECOTECT design sky value  
        2048 Render a Daylight Factor image 
        4096 Generate Point Data for analysis  
        32768 Do not display images when complete  

        """
        arg_str = string_util._convert_args_to_string("set.radiance.flag", 
                                                     flag, state)
        py2ecotect.conversation.Exec(arg_str)

    def get_image_type(self):
        """
        
        Retrieves the currently set image type. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        image 
        An integer value corresponding to the Radiance Image Types table below. 
        
        Relevant Data Table(s)
        
        Radiance Image Types 
        Value Description 
        0 Luminance (cd/m^2) 
        1 Illuminance (Lux) 
        2 Daylight Factor (%) 
        3 Sky Component (%) 
        
        """
        val = py2ecotect.conversation.Request("get.radiance.imagetype")
        return string_util._convert_str_to_type(val, int)
        
    def set_image_type(self, type):
        """
        
        Sets the image type that is to be generated. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        An integer value corresponding to the Radiance Image Types table below. 
        
        Relevant Data Table(s)
        
        Radiance Image Types
         Value Description 
        0 Luminance (cd/m^2) 
        1 Illuminance (Lux) 
        2 Daylight Factor (%) 
        3 Sky Component (%) 

        """
        arg_str = string_util._convert_args_to_string("set.radiance.imagetype", 
                                                     type)
        py2ecotect.conversation.Exec(arg_str)

    def get_lights(self):
        """
        
        Retrieves the current setting for how LIGHT objects are exported in 
        Radiance scene files. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        lights 
        An integer value corresponding to the Radiance Light Export table below. 
        
        Relevant Data Table(s)
        
        Radiance Light Export 
        Value Description 
        0 Turn LIGHTS Off 
        1 Generate Automatically 
        2 Generate as Spheres 
        3 Generate as Markers 

        """
        val = py2ecotect.conversation.Request("get.radiance.lights")
        return string_util._convert_str_to_type(val, int)

    def set_light_data(self, lights):
        """
        
        Sets the option for how LIGHT objects are exported in Radiance scene 
        files. 

        Parameter(s)
        This property takes the following parameters.
        
        lights 
        An integer value corresponding to the Radiance Light Export table below. 
        
        Relevant Data Table(s)
        Radiance Light Export Value Description 
        0 Turn LIGHTS Off 
        1 Generate Automatically 
        2 Generate as Spheres 
        3 Generate as Markers 

        """
        arg_str = string_util._convert_args_to_string("set.radiance.lightdata", 
                                                     lights)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_point_data(self):
        """
        
        Retrieves the current setting for what, if any, point data is exported 
        for analysis in Radiance. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        type 
        An integer value corresponding to values in the following Radiance 
        Point Data table. 
        
        Relevant Data Table(s)
        
        Radiance Point Data 
        Value Description 
        -1 No point data generated  
        0 Current 2D analysis grid 
        1 Current 3D analysis grid 
        2 Objects tagged as shaded  
        3 Currently selected objects  

        """
        val = py2ecotect.conversation.Request("get.radiance.pointdata")
        return string_util._convert_str_to_type(val, int)

    def set_point_data(self, type):
        """
        
        Sets the current setting for what, if any, point data is exported for 
        analysis in Radiance. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        An integer value corresponding to the Radiance Point Data table below. 
        Setting this property also sets or resets the 4096 flag in the 
        set.radiance.flag property. 
        
        Relevant Data Table(s)
        
        Radiance Point Data 
        
        Value Description 
        -1 No point data generated  
        0 Current 2D analysis grid 
        1 Current 3D analysis grid 
        2 Objects tagged as shaded  
        3 Currently selected objects  

        """
        arg_str = string_util._convert_args_to_string("set.radiance.pointdata", 
                                                     type)
        py2ecotect.conversation.Exec(arg_str)

    def get_quality(self):
        """
        
        Retrieves the current setting for the amount of anti-aliasing in the 
        final render. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        quality 
        An integer value corresponding to the following Radiance Settings table. 
        
        Relevant Data Table(s)
        
        Radiance Settings 
        Token Value Description 
        low 0 Low 
        medium 1 Medium 
        high 2 High 
        
        """
        val = py2ecotect.conversation.Request("get.radiance.quality")
        return string_util._convert_str_to_type(val, int)

    def set_quality(self, quality):
        """
        
        Sets the amount of anti-aliasing in the final render. 

        Parameter(s)
        This property takes the following parameters.
        
        quality 
        A value corresponding to the following Radiance Settings table. This 
        parameter can be set as a token or a value.
                
        """
        
        arg_str = string_util._convert_args_to_string("set.radiance.quality", 
                                                     quality)
        py2ecotect.conversation.Exec(arg_str)

    def get_reflections(self):
        """
        
        Retrieves the current setting for the number of surface reflections 
        that are traced from each sampling point ray. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        bounces 
        The number of bounces given as an integer value between 0 and 12.
        
        """
        val = py2ecotect.conversation.Request("get.radiance.reflections")
        return string_util._convert_str_to_type(val, int)
        
    def set_reflections(self, bounces):
        """
        
        Sets the number of surface reflections that are traced from each 
        sampling point ray. 

        Parameter(s)
        This property takes the following parameters.
        
        bounces 
        An integer value between 0 and 12 specifying the number of bounces for 
        each ray.
        
        """
        arg_str = string_util._convert_args_to_string("set.radiance.reflections", 
                                                     bounces)
        py2ecotect.conversation.Exec(arg_str)

    def get_resolution(self):
        """
        
        Retrieves the current setting specifying the resolution of the resulting image. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        xres 
        The resulting image width in pixels. 
        
        yres 
        The resulting image height in pixels. 

        """
        val = py2ecotect.conversation.Request("get.radiance.resolution")
        return string_util._convert_str_to_list(val, int, int)

    def set_resolution(self,  xres, yres):
        """
        
        Sets the resolution for the resulting image. Results may vary depending 
        on the CAMERA view aspect ratio. Basically, one dimension will always 
        be accurate but the other will be modified to maintain the CAMERA 
        aspect ratio. 

        Parameter(s)
        This property takes the following parameters.
        
        xres 
        The resulting image width in pixels. 
        
        yres 
        The resulting image height in pixels.
        
        """
        arg_str = string_util._convert_args_to_string("set.radiance.resolution", 
                                                     xres, yres)
        py2ecotect.conversation.Exec(arg_str)

    def get_scale(self):
        """
        
        Retrieves the current setting of the scaling value from world 
        coordinates to Radiance coordinantes. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        scale 
        A decimal value containing the scaling value.
        
        """
        val = py2ecotect.conversation.Request("get.radiance.scale")
        return string_util._convert_str_to_type(val, float)
        
    def set_scale(self, scale):
        """
        
        Sets the scaling value from world to Radiance coordinantes. The default 
        value converts millimetres in the model to metres in Radiance and is 
        0.001. 

        Parameter(s)
        This property takes the following parameters.
        
        scale 
        A decimal value specifying the new scaling value. 
        
        """
        arg_str = string_util._convert_args_to_string("set.radiance.scale", 
                                                     scale)
        py2ecotect.conversation.Exec(arg_str)    

    def get_sky(self):
        """
        
        Retrieves the current setting of how the sky is exported in the sky.rad 
        file. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        skytype 
        An integer value corresponding to values in the following Radiance Sky 
        Types table. 
        
        Relevant Data Table(s)
        
        Radiance Sky Types  
        Value Description 
        0 [No Sky] 
        1 Sunny with sun 
        2 Sunny without sun 
        3 Intermediate with sun 
        4 Intermediate no sun 
        5 Overcast sky 
        6 Uniform sky 
        
        """
        val = py2ecotect.conversation.Request("get.radiance.sky")
        return string_util._convert_str_to_type(val, int)

    def set_sky(self, skytype):
        """
        
        Sets how the sky is exported in the sky.rad file. 

        Parameter(s)
        This property takes the following parameters.
        
        skytype 
        An integer value corresponding with the values in the following Radiance 
        Sky Types table. 
        
        Relevant Data Table(s)
        
        Radiance Sky Types  
        Value Description 
        0 [No Sky] 
        1 Sunny with sun 
        2 Sunny without sun 
        3 Intermediate with sun 
        4 Intermediate no sun 
        5 Overcast sky 
        6 Uniform sky 

        """
        arg_str = string_util._convert_args_to_string("set.radiance.sky", 
                                                     skytype)
        py2ecotect.conversation.Exec(arg_str)    
    
    def get_variability(self):
        """
        
        Retrieves the setting of the likely difference in light levels between 
        adjacent points on a surface. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        variability 
        An integer value corresponding to the following Radiance Settings table. 
        
        Relevant Data Table(s)
        Radiance Settings 
        Token Value Description 
        low 0 Low 
        medium 1 Medium 
        high 2 High 
        
        """
        val = py2ecotect.conversation.Request("get.radiance.variability")
        return string_util._convert_str_to_type(val, int)

    def set_variability(self, variability):
        """
        
        Sets the likely difference in light levels between adjacent points on a 
        surface. 

        Parameter(s)
        This property takes the following parameters.
        
        variability 
        A value corresponding to the following Radiance Settings table. This 
        parameter can be set as a token or a value. 
        
        Relevant Data Table(s)
        
        Radiance Settings 
        Token Value Description 
        low 0 Low 
        medium 1 Medium 
        high 2 High 

        """
        arg_str = string_util._convert_args_to_string("set.radiance.variability", 
                                                     variability)
        py2ecotect.conversation.Exec(arg_str)    

    def get_view_type(self):
        """
        
        Retrieves the currently set internal/external view type. If external, 
        RADIANCE adds an ambient component to the scene to simulate outside 
        conditions so you should be careful to ensure this setting is correct. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        type 
        An integer value corresponding to the Radiance View Types table below. 
        
        Relevant Data Table(s)
        Radiance View Types  
        Value Description 
        0 Interior View 
        1 Exterior view 

        """
        val = py2ecotect.conversation.Request("get.radiance.viewtype")
        return string_util._convert_str_to_type(val, int)

    def set_view_type(self, type):
        """
        
        Sets the internal/external view type that is to be generated. If 
        external, RADIANCE adds an ambient component to the scene to simulate 
        outside conditions so you should be careful to ensure this setting is 
        correct. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        An integer value corresponding to the Radiance View Types table below. 
        
        Relevant Data Table(s)
        Radiance View Types  
        Value Description 
        0 Interior View 
        1 Exterior view 

        """
        arg_str = string_util._convert_args_to_string("set.radiance.viewtype", 
                                                     type)
        py2ecotect.conversation.Exec(arg_str)    

    #===========================================================================
    # Properties
    #===========================================================================

    action = property(fget = get_action, fset = set_action, 
                        doc = "The current set radiance render action setting")
    
    detail = property(fget = get_detail, fset = set_detail, 
                        doc = "The current level of geometric complexity within"
                        " the model")
    
    image_type= property(fget = get_image_type, fset = set_image_type, 
                        doc = "The currently set image type")
    
    lights = property(fget = get_lights, fset = set_light_data, 
                        doc = "The current setting for how LIGHT objects are"
                        " exported in Radiance scene files")
    
    point_data = property(fget = get_point_data, fset = set_point_data, 
                        doc = "The current setting for what, if any, point data"
                        " is exported for analysis in Radiance")
    
    quality = property(fget = get_quality, fset = set_quality, 
                        doc = "The current setting for the amount of"
                        " anti-aliasing in the final render")
    
    reflections = property(fget = get_reflections, fset = set_reflections, 
                        doc = "The current setting for the number of surface"
                        " reflections that are traced from each sampling point"
                        " ray")
    
    scale = property(fget = get_scale, fset = set_scale, 
                        doc = "The current setting of the scaling value from"
                        " world coordinates to Radiance coordinantes")
    
    sky = property(fget = get_sky, fset = set_sky, 
                        doc = "The current setting of how the sky is exported"
                        " in the sky.rad file")
    
    variability = property(fget = get_variability, fset = set_variability, 
                        doc = "The setting of the likely difference in light"
                        " levels between adjacent points on a surface")
    
    view_type= property(fget = get_view_type, fset = set_view_type, 
                        doc = "The currently set internal/external view type")
    


if __name__ == "__main__":
    x = Radiance()
    
    #x.load("C:\\Program Files\\Autodesk\\Ecotect 2009\\Weather\\UK-LondonE")
    #print x.get_action()
    #x.set_action(2)
    #print x.get_flag(1024)
    #x.set_flag(1024)
    #print x.get_lights()
    #x.set_lights(2)
    #print x.get_resolution()
    #print x.view_type
    #x.view_type = 1


    print "Tests completed"