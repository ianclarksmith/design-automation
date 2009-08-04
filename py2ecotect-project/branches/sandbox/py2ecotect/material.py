import py2ecotect as p2e

class Material(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def edit(self, material):
        """
        
        Displays the Materials Editor with the specified material selected. Note 
        that the script only continues after the user closes the dialog. 

        Parameter(s)
        This command takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the required material.
        
        """
        arg_str = p2e._util._convert_args_to_string("material.edit", material)
        p2e.conversation.Exec(arg_str)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_absorption(self, material):
        """
        
        Retrieves the Solar Absorption value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required material. 
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        The solar absorption value used for the specified material. 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.absorption", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_absorption(self, material, value):
        """
        
        Sets the solar absorption value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The solar absorption value to use for the specified material. It can be 
        a decimal value between 0 and 1.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.absorption", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_admittance(self, material):
        """
        
        Retrieves the Admittance value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the 
        required material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        The thermal admittance value used for the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.admittance", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_admittance(self, material, value):
        """
        
        Sets the admittance value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The admittance value to use for the specified material. It is given in 
        W/m^2K. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.admittance", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_colour(self, material):
        """
        
        Retrieves the internal and external colour for the specified material. 
        Two hexidecimal values are returned, corresponding to the internal and 
        external colours, in that order. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        internal 
        The colour used for the internal face of the specified material. 
        
        external 
        The colour used for the external face of the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.colour", 
                                                     material)
        val = p2e.conversation.Request(arg_str)        
        return p2e._util._convert_str_to_list(val, str, str)

    def set_colour(self, material, internal, external):
        """
        
        Sets the internal and external colour for the specified material. Colour 
        values must be given in full hexidecimal, for example 0xFF8800. Note 
        that the 0x prefix must be included. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        internal 
        The colour to use for the internal face of the specified material. 
        
        external 
        The colour to use for the external face of the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.colour", 
                                                     material, internal, external)
        p2e.conversation.Exec(arg_str)

    def get_cost_per_unit(self, material):
        """
        
        Retrieves the Cost Per Unit value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        The cost per unit value used for the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.costperunit", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_cost_per_unit(self, material, value):
        """
        
        Sets the Cost Per Unit value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The cost per unit value to use for the specified material. It is a two 
        decimal value, such as 5.50, and is displayed using the currency symbol 
        as specified in the User Preferences dialog box.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.costperunit", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_cost_type(self, material):
        """
        
        Retrieves the way costs are calculated for the specified material. 
        There are three possible values that can be returned, as outlined in the 
        following table. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        costType 
        An integer value showing how costs are calculated for the specified 
        material. There are three possible values as outlined in the following 
        Cost Type table. 
        
        Relevant Data Table(s)
        
        Material Cost Types 
        Token Value Description 
        perm^2 0 Per square metre area. 
        permeter 1 Per metre length. 
        peritem 2 Per individual item. 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.costtype", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

    def set_cost_type(self, material, costType):
        """
        
        Sets the way how costs are calculated for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to set. 
        
        costType 
        An integer value showing how costs should be calculated for the 
        specified material. There are three possible values that can be used, 
        as outlined in the following Cost Type table. 
        
        Relevant Data Table(s)
        
        Material Cost Types Token Value Description 
        perm^2 0 Per square metre area. 
        permeter 1 Per metre length. 
        peritem 2 Per individual item. 


        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.costtypr", 
                                                     material, costType)
        p2e.conversation.Exec(arg_str)

    def get_data(self, material, index):
        """
        
        Retrieves values from the data array of the specified material. Each 
        material contains an array of data values used for different purposes, 
        depending on the element type. For example, for SPEAKER and LIGHT o
        bjects, the array defines the output profile. While for WALLS, FLOORS 
        and CEILINGS it defines the sound absorption coefficient at different 
        frequencies.

        The number of variables required to retrieve the data value array are 
        outlined in the following Material Data Types table. 
        
        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        index 
        Specifies which index value of the array to retrieve, as outlined in the 
        following Material Data table. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        The data value to assign to the specified index, given as a decimal value between 0 and 1. 
        
        Relevant Data Table(s)
        Material Data Types 
        Data Array Type Array values 
        Absorption Co-efficients 0-8 
        Output Profiles 0-18 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.data", 
                                                     material, index)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_data(self, material, index, value):
        """
        
        Sets values for the data array of the specified material.

        Each material contains an array of data values used for different 
        purposes, depending on the element type. For example, for SPEAKER and 
        LIGHT objects, the array defines the output profile. While for WALLS, 
        FLOORS and CEILINGS it defines the sound absorption coefficient at 
        different frequencies. 
        
        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        index 
        Specifies which index value of the array to set, as outlined in the 
        following Material Data Types table. 
        
        value 
        The data value to assign to the specified index. Generally, it is a 
        decimal value between 0 and 1. 
        
        Relevant Data Table(s)
        Material Data Types 
        Data Array Type Array values 
        Absorption Co-efficients 0-8 
        Output Profiles 0-18 

        """
        arg_str = p2e._util._convert_args_to_string("set.material.data", 
                                                     material, index, value)
        p2e.conversation.Exec(arg_str)
    
    def get_decrement(self, material):
        """
        
        Retrieves the thermal decrement value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.decrement", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_decrement(self, material, value):
        """
        
        Sets the thermal decrement value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The thermal decrement value to use for the specified material. It can be 
        a decimal value between 0 and 1. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.decrement", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)
    
    @apply
    def myattr():
        def fset(self, materail):
            """
            
            Set this property to make the specified material the default for all 
            new objects of the same element type. 
    
            Parameter(s)
            This property takes the following parameters.
            
            material 
            An integer value that specifies the zero-based index of the material to set as default. 
    
            """
            arg_str = p2e._util._convert_args_to_string("set.material.default", 
                                                         material)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())

    def get_description(self, material):
        """
        
        Retrieves the description for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        description 
        A text string value containing notes or a description of the material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.description", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, str)

    def set_description(self, material, description):
        """
        
        Sets the description for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        description 
        A text string value up to 256 characters in length, containing notes or 
        a description of the material.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.description", 
                                                     material, description)
        p2e.conversation.Exec(arg_str)

    def get_element(self, material):
        """
        
        Returns the element type of the specified material as a string. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        element 
        A text string corresponding to the token column in the following Element 
        Types table. 
        
        Relevant Data Table(s)
        
        Element Types 
        Token Value 
        void 0 
        roof 1 
        floor 2 
        ceiling 3 
        wall 4 
        partition 5 
        window 6 
        panel 7 
        door 8 
        point 9 
        speaker 10 
        light 11 
        appliance 12 
        line 13 
        solarcollector 14 
        camera 15 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.element", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, str)

    def get_embodied_energy(self, material):
        """
        
        Retrieves the Initial Embodied Energy value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.embodiedenergy", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_embodied_energy(self, material, value):
        """
        
        Sets the Initial Embodied Energy value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Initial Embodied Energy value to use for the specified material. It 
        is measured in Watt Hours (Wh).
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.embodiedenergy", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_energy_maintenance(self, material):
        """
        
        Retrieves the Annual Maintenance Energy value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.energymaintenance", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_energy_maintenance(self, material, value):
        """
        
        Sets the Annual Maintenance Energy value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Annual Maintenance Energy value to use for the specified material. 
        It is measured in Watt Hours (Wh). 

        """
        arg_str = p2e._util._convert_args_to_string("set.material.energymaintenance", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_ext_emissivity(self, material):
        """
        
        Retrieves the External Emissivity value for the specified material. The 
        value returned is a decimal ratio between 0 and 1. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.extemissivity", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_ext_emissivity(self, material, value):
        """
        
        Sets the External Emissivity value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The External Emissivity value to use for the specified material. It is a 
        decimal ratio between 0 and 1. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.extemissivity", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_ext_roughness(self, material):
        """
        
        Retrieves the External Roughness value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.extroughness", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_ext_roughness(self, material, value):
        """
        
        Sets the External Roughness value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The External Roughness value to use for the specified material. It is a 
        decimal ratio between 0 and 1.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.extroughness", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_ext_specularity(self, material):
        """
        
        Retrieves the External Specularity value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
    
        """
        arg_str = p2e._util._convert_args_to_string("get.material.extspecularity", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_ext_specularity(self, material, value):
        """
        
        Sets the External Specularity value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The External Specularity value to use for the specified material. It is 
        a decimal ratio between 0 and 1. 

        """
        arg_str = p2e._util._convert_args_to_string("set.material.extspecularity", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_greenhouse_gas(self, material):
        """
        
        Retrieves the Greenhouse Gas Emission value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.greenhousegas", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_greenhouse_gas(self, material, value):
        """
        
        Sets the Greenhouse Gas Emission value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to set. 
        value 
        The Greenhouse Gas Emission value to use for the specified material. It can be any numeric value, per unit measure. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.greenhousegas", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)
    
    @staticmethod
    def get_index(name):
        """
        
        This property returns the zero-based index of the material with a name 
        matching the name parameter. If no matching material is found, an index 
        of -1 is returned. Note: All material properties require as their first 
        parameter the zero-based index of the material to be modified or 
        interrogated. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        The name of the material to retrieve the index for. It can be a string 
        value of any length. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the matching material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.index", name)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

    def get_int_emissivity(self, material):
        """
        
        Retrieves the Internal Emissivity value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.intemissivity", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_int_emissivity(self, material, value):
        """
        
        Sets the Internal Emissivity value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Internal Emissivity value to use for the specified material. It is a 
        decimal ratio between 0 and 1. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.intemissivity", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_int_roughness(self, material):
        """
        
        Retrieves the Internal Roughness value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.introughness", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_int_roughness(self, material, value):
        """
        
        Sets the Internal Roughness value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Internal Roughness value to use for the specified material. It is a 
        decimal ratio between 0 and 1. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.introughness", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_int_specularity(self, material):
        """
        
        Retrieves the Internal Specularity value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.intspecularity", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_int_specularity(self, material, value):
        """
        
        Sets the Internal Specularity value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Internal Specularity value to use for the specified material. It is 
        a decimal ratio between 0 and 1.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.intspecularity", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_lag(self, material):
        """
        
        Retrieves the Thermal Lag value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.lag", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_lag(self, material, value):
        """
        
        Sets the Thermal Lag value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Thermal Lag value to use for the specified material. It can be any 
        numeric value, measured in hours.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.lag", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_layer_conductivity(self, material, layer):
        """
        
        Retrieves the Thermal Conductivity value of the specified layer in the 
        material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        conductivity 
        The conductivity value used for the specified layer, measured in W/m.K.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.layer.conductivity", 
                                                     material, layer)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_layer_conductivity(self, material, layer, conductivity):
        """
        
        Sets the Thermal Conductivity value of the layer in the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        conductivity 
        Sets the conductivity value to use for the specified layer, measured in 
        W/m.K. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.layer.conductivity", 
                                                     material, layer, conductivity)
        p2e.conversation.Exec(arg_str)

    def get_layer_density(self, material, layer):
        """
        
        Retrieves the Density value of the specified layer in the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        density 
        The density value to use for the specified layer, given in kg/m3. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.layer.density", 
                                                     material, layer)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_layer_density(self, material, layer, density):
        """
        
        Sets the Density value of the specified layer in the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        density 
        Sets the density value to use for the specified layer, measured in kg/m3.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.layer.density", 
                                                     material, layer, density)
        p2e.conversation.Exec(arg_str)

    def get_layer_hatch(self, material, layer):
        """
        
        Retrieves the Hatch Pattern value of the specified layer in the material. 
        An integer value is returned, corresponding with the various hatch patterns 
        available. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        hatch 
        An integer value that sets the hatch type to use for the specified layer.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.layer.hatch", 
                                                     material, layer)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

    def set_layer_hatch(self, material, layer, hatch):
        """
        
        Sets the Hatch value of the specified layer in the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        hatch 
        An integer value that sets the hatch type to use for the specified layer.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.layer.hatch", 
                                                     material, layer, hatch)
        p2e.conversation.Exec(arg_str)

    def get_layer_name(self, material, layer):
        """
        
        Retrieves the Layer Name value of the specified row for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        name 
        A text string value containing the name of the specified layer.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.layer.name", 
                                                     material, layer)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, str)

    def set_layer_name(self, material, layer, name):
        """
        
        Sets the Layer Name value of the specified row for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        name 
        A string value that specifies the name of the specified layer.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.layer.name", 
                                                     material, layer, name)
        p2e.conversation.Exec(arg_str)

    def get_layer_specific_heat(self, material, layer):
        """
        
        Retrieves the Specific Heat value of the specified layer the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        specific_heat 
        The specific heat value used for the specified layer, measured in J/kg.K.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.layer.specific_heat", 
                                                     material, layer)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_layer_specific_heat(self, material, layer, specific_heat):
        """
        
        Sets the Specific Heat value of the specified layer in the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        specific_heat 
        Sets the specific heat value to use for the specified layer, measured in 
        J/kg.K.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.layer.specific_heat", 
                                                     material, layer, specific_heat)
        p2e.conversation.Exec(arg_str)

    def get_layer_type(self, material, layer):
        """
        
        Retrieves the Type value of the specified layer in the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        type 
        An integer value giving type used for the specified layer.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.layer.type", 
                                                     material, layer)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

    def set_layer_type(self, material, layer, type):
        """
        
        Sets the Type value of the specified layer in the material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        type 
        An integer value that sets the type to use for the specified layer. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.layer.type", 
                                                     material, layer, type)
        p2e.conversation.Exec(arg_str)

    def get_layer_width(self, material, layer):
        """
        
        Retrieves the Width value of the specified layer in the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        width 
        The width of the specified layer in the material, given in mm. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.layer.width", 
                                                     material, layer)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_layer_width(self, material, layer, width):
        """
        
        Sets the Width value of the specified row for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        layer 
        The zero-based index for the layer row number for the value to retrieve, 
        as shown under the Layer tab for the specified material. 
        
        width 
        The width value to use for the specified layer in the material, measured 
        in mm.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.layer.width", 
                                                     material, layer, width)
        p2e.conversation.Exec(arg_str)

    def get_lca(self, material):
        """
        
        Retrieves the LCAid Reference value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.lca", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)
        
    def set_lca(self, material, value):
        """
        
        Sets the LCAid Reference value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The LCAid Reference value to use for the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.lca", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_life_span(self, material):
        """
        
        Retrieves the Expected Life value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.lifespan", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_life_span(self, material, value):
        """
        
        Sets the lifespanid Reference value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Expected Life value to use for the specified material, measured in 
        years.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.lifespan", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_maintenance_cost(self, material):
        """
        
        Retrieves the Annual Maintenance Costs value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.get_maintenancecost", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_maintenance_cost(self, material, value):
        """
        
        Sets the Annual Maintenance Costs value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Annual Maintenance Costs value to use for the specified material, 
        measured in selected currency.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.maintenancecost", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_name(self, material):
        """
        
        Retrieves the Material Name value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        name 
        A text string value containing the current name of the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.name", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, str)

    def set_name(self, material, value):
        """
        
        Sets the name of the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The string value containing the new name of the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.name", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_ref1(self, material):
        """
        
        Retrieves the External Reference 1 value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.ref1", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_ref1(self, material, value):
        """
        
        Sets the External Reference 1 value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The External Reference 1 value to use for the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.ref1", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_ref2(self, material):
        """
        
        Retrieves the External Reference 2 value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.ref2", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_ref2(self, material, value):
        """
        
        Sets the External Reference 2 value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The External Reference 2 value to use for the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.ref2", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_reflectance(self, material):
        """
        
        Retrieves the internal and external reflectance of the specified material. 
        Reflectances are given as decimal values ranging from 0.0 to 1.0. 
        Retrieving this value returns two decimal reflectance values corresponding 
        to the internal and external parameters, in that order. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        internal 
        The internal reflectance value. Reflectances are given as decimal values 
        ranging from 0.0 to 1.0. 
        
        external 
        The external reflectance value. Reflectances are given as decimal values 
        ranging from 0.0 to 1.0. 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.reflectance", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float)

    def set_reflectance(self, material, internal, external):
        """
        
        Sets the internal and external reflectance of the specified material. 
        The reflectance of a material is based on its color value, thus setting 
        this value will modify the colour by brightening or darkening it. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        internal 
        The internal reflectance value. Reflectances are given as decimal values 
        ranging from 0.0 to 1.0. Values outside this range will be ignored and 
        the corresponding colour not updated. 
        
        external 
        The external reflectance value. Reflectances are given as decimal values 
        ranging from 0.0 to 1.0. Values outside this range will be ignored and 
        the corresponding colour not updated.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.reflectance", 
                                                     material, internal, external)
        p2e.conversation.Exec(arg_str)

    def get_thickness(self, material):
        """
        
        Retrieves the Thickness value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.thickness", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_thickness(self, material, value):
        """
        
        Sets the Thickness value for the specified material. Note: The material 
        thickness is usually calculated as the sum of the individual layer 
        thicknesses as configured under the Layers tab. Setting the Thickness 
        using this command overrides this calculated value, but does not change 
        the thickness values for the individual layers. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Thickness value to use for the specified material, measured in 
        millimetres. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.thickness", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_transparency(self, material):
        """
        
        Retrieves the Transparency value for the specified material. The value 
        returned is a decimal value between 0.0 and 1.0. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.transparency", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_transparency(self, material, value):
        """
        
        Sets the Transparency value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The Transparency value to use for the specified material. This can be a 
        decimal value between 0.0 and 1.0. 

        """
        arg_str = p2e._util._convert_args_to_string("set.material.transparency", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_type(self, material):
        """
        
        Retrieves the element type for the specified material. These correspond 
        directly to object element types, as outlined in the following table. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the material to 
        retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        type 
        An integer value corresponding to the following Element Types table. 
        
        Relevant Data Table(s)
        Element Types 
        Token Value 
        void 0 
        roof 1 
        floor 2 
        ceiling 3 
        wall 4 
        partition 5 
        window 6 
        panel 7 
        door 8 
        point 9 
        speaker 10 
        light 11 
        appliance 12 
        line 13 
        solarcollector 14 
        camera 15 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.type", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

    def set_type(self, material, type):
        """
        
        Sets the element type for the specified material. These correspond 
        directly to object element types. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the material to 
        set. 
        
        type 
        This parameter can be given either as a token or value, corresponding to 
        the following Element Types table. 
        
        Relevant Data Table(s)
        Element Types 
        Token Value 
        void 0 
        roof 1 
        floor 2 
        ceiling 3 
        wall 4 
        partition 5 
        window 6 
        panel 7 
        door 8 
        point 9 
        speaker 10 
        light 11 
        appliance 12 
        line 13 
        solarcollector 14 
        camera 15 

        """
        arg_str = p2e._util._convert_args_to_string("set.material.type", 
                                                     material, type)
        p2e.conversation.Exec(arg_str)

    def get_used(self, material):
        """
        
        Returns the number of objects in the current model that use the 
        specified material. This includes objects on hidden and locked zones but 
        NOT on zones that are currently off. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        use. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        count 
        An integer count of the objects in the current model that are assigned 
        this material. 

        """
        arg_str = p2e._util._convert_args_to_string("get.materialused.used", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)

    def get_uvalue(self, material):
        """
        
        Retrieves the U-Value value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified 
        material. 

        """
        arg_str = p2e._util._convert_args_to_string("get.material.uvalue", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_uvalue(self, material, value):
        """
        
        Sets the U-Value value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to 
        set. 
        
        value 
        The U-Value value to use for the specified material, measured in W/m^2.K.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.uvalue", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)

    def get_weight(self, material):
        """
        
        Retrieves the Weight value for the specified material. The value 
        returned is measured in kilograms. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the required 
        material. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the retrieved date from the specified material. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.material.weight", 
                                                     material)
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)

    def set_weight(self, material, value):
        """
        
        Sets the Weight value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to set. 
        value 
        The Weight value to use for the specified material, measured in kilograms.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.material.weight", 
                                                     material, value)
        p2e.conversation.Exec(arg_str)
