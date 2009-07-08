import py2ecotect
from py2ecotect import StringUtil

class Material(object):
    def edit(self, material):
        """
        
        Displays the Materials Editor with the specified material selected. Note 
        that the script only continues after the user closes the dialog. 

        Parameter(s)
        This command takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the required material.
        
        """
        arg_str = StringUtil._convert_args_to_string("material.edit", material)
        py2ecotect.conversation.Exec(arg_str)
    
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
        arg_str = StringUtil._convert_args_to_string("get.material.absorption", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

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
        arg_str = StringUtil._convert_args_to_string("set.material.absorption", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.admittance", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

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
        arg_str = StringUtil._convert_args_to_string("set.material.admittance", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.colour", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)        
        return StringUtil._convert_str_to_list(val, str, str)

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
        arg_str = StringUtil._convert_args_to_string("set.material.colour", 
                                                     material, internal, external)
        py2ecotect.conversation.Exec(arg_str)

    def get_costperunit(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.costperunit", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_costperunit(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.costperunit", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_costtype(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.costtype", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)

    def set_costtype(self, material, costType):
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
        arg_str = StringUtil._convert_args_to_string("set.material.costtypr", 
                                                     material, costType)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.data", 
                                                     material, index)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

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
        arg_str = StringUtil._convert_args_to_string("set.material.data", 
                                                     material, index, value)
        py2ecotect.conversation.Exec(arg_str)
    
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
        arg_str = StringUtil._convert_args_to_string("get.material.decrement", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

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
        arg_str = StringUtil._convert_args_to_string("set.material.decrement", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def set_default(self, materail):
        """
        
        Set this property to make the specified material the default for all 
        new objects of the same element type. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        An integer value that specifies the zero-based index of the material to set as default. 

        """
        arg_str = StringUtil._convert_args_to_string("set.material.default", 
                                                     material)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.description", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, str)

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
        arg_str = StringUtil._convert_args_to_string("set.material.description", 
                                                     material, description)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.element", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, str)

    def get_embodiedenergy(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.embodiedenergy", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_embodiedenergy(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.embodiedenergy", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_energymaintenance(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.energymaintenance", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_energymaintenance(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.energymaintenance", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_extemissivity(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.extemissivity", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_extemissivity(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.extemissivity", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_extroughness(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.extroughness", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_extroughness(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.extroughness", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_extspecularity(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.extspecularity", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_extspecularity(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.extspecularity", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_greenhousegas(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.greenhousegas", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_greenhousegas(self, material, value):
        """
        
        Sets the Greenhouse Gas Emission value for the specified material. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        an integer value that specifies the zero-based index of the material to set. 
        value 
        The Greenhouse Gas Emission value to use for the specified material. It can be any numeric value, per unit measure. 
        
        """
        arg_str = StringUtil._convert_args_to_string("set.material.greenhousegas", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_index(self, name):
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
        arg_str = StringUtil._convert_args_to_string("get.material.index", name)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)

    def get_intemissivity(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.intemissivity", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_intemissivity(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.intemissivity", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_introughness(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.introughness", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_introughness(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.introughness", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_intspecularity(self, material):
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
        arg_str = StringUtil._convert_args_to_string("get.material.intspecularity", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_intspecularity(self, material, value):
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
        arg_str = StringUtil._convert_args_to_string("set.material.intspecularity", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.lag", 
                                                     material)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

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
        arg_str = StringUtil._convert_args_to_string("set.material.lag", 
                                                     material, value)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.layer.conductivity", 
                                                     material, layer)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

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
        arg_str = StringUtil._convert_args_to_string("set.material.conductivity", 
                                                     material, layer, conductivity)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.density", 
                                                     material, layer)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

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
        arg_str = StringUtil._convert_args_to_string("set.material.density", 
                                                     material, layer, density)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.hatch", 
                                                     material, layer)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)

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
        arg_str = StringUtil._convert_args_to_string("set.material.hatch", 
                                                     material, layer, hatch)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = StringUtil._convert_args_to_string("get.material.name", 
                                                     material, layer)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, str)

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
        arg_str = StringUtil._convert_args_to_string("set.material.name", 
                                                     material, layer, name)
        py2ecotect.conversation.Exec(arg_str)















































































if __name__ == "__main__":
    x = Material()
    
    #x.edit(54)
    #print x.get_absorption(54)
    #x.set_absorption(54, 0.98)
    #print x.get_admittance(34)
    #x.set_admittance(34, 10.000)
    #print x.get_colour(34)
    #x.set_colour(34, "0xFF8800", "0xFF8800")
    #print x.get_costperunit(34)
    #x.set_costperunit(34, 5.50)
    #print x.get_costtype(34)
    #print x.get_layer_conductivity(34, 2)
    
    
    
    print "Tests completed"