import py2ecotect
from py2ecotect import string_util

class Results(object):
    
    #===========================================================================
    # Properties
    #===========================================================================

    def get_array(self, i, j):
        """
        
        The various solar and thermal analysis calculations store their results 
        either directly within the zones they are working on, or in a large 2D 
        data array. This method allows access to this array. The exact format 
        of data within the array depends upon the type of calculation last 
        performed. 

        Parameter(s)
        This property takes the following parameters.
        
        i 
        As defined below. 
        
        j 
        As defined below. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified array value. 
        
        Relevant Data Table(s)
        
        Thermal Analysis
        
        Hourly Temperatures
        Internal temperature values are stored in each zone. Use the following 
        command to access them:
        
        get.zone.temperature zone hour
        
        Hourly Gains 
        The seven different gains are stored in the first seven elements of the 
        array. Thus the i value refers to the table below whereas the j value 
        is the hour index of the day (0 to 23). 
        
        Data Type Value 
        HVAC Load 0 
        Conduction Gain 1 
        Sol-Air Gains 2 
        Direct Solar Gains 3 
        Ventilation Gains 4 
        Internal Gains 5 
        Inter-Zonal Gains 6 
        
        Heat / Cool Load
        Monthly heating and cooling loads are stored directly in the heating 
        and cooling load arrays for each zone. The 'Outside' zone (index = 0) 
        stores the total loads of all zones visible at the time of the last 
        calculation. Use the following commands to access them:
        
        get.zone.heating zone month
        get.zone.cooling zone month  
        
        Temperature Distribution (0 - 48)
        This too is stored within the heating and cooling load arrays for each 
        zone. As there are only 12 indexes in each load array (1 for each 
        month), each index represents a 2-degree range with the heating array 
        representing 0-24 deg Cel and the cooling array 24-48deg Cel.
        
        Solar Exposure
        Single Day
        The data from a single day's solar radiation analysis on a surface is 
        not stored in the results array. Use the get.results.solar command 
        described below.
        
        Average Daily & Total Monthly
        These values are stored in the array by MONTHS and HOURS. The i value 
        refers to the month (0-11) whereas the j value is the hour index of the 
        day (0 to 23). The array only stores the current radiation data value. 
        Thus, if the Radiation Data: Item is set to Absorbed, then only the 
        absorbed value is stored and displayed. 
        
        An annual value is also stored for i=12, but not displayed. For Total 
        Monthly calculations, these are the annual totals for each hour. For 
        Average Daily calculations these are the annual average daily value 
        for eah hour.
        
        Full Hourly
        This calculation stores all 8760 hourly values in the array by DAY and 
        HOUR. The i value refers to the day of the year (0-364) whereas the j 
        value is the hour index of the day (0 to 23). 
        
        Resource Use
        The resource use values are stored in the array by day and type. The i 
        value refers to the day of the year (0-364) whereas the j value is 0 
        for the resource used or 1 for the resource collected.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.array", i, j)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_conduction(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for the total gains conducted through the building fabric. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.conduction", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_daily(self, zone):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        either the Hourly Temperature Profile or Hourly Heat Gains/Losses calculation), 
        this command will directly access the calculated results for the total sum of 
        all gains for the entire day. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.daily", 
                                                      zone)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_fabric(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for conduction through fabric, opaque and glazing objects. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.fabric", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_glazing_fabric(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for the conduction gains through only glazing fabric. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        hour 
        The hour to retrieve, being from 0 to 23. 
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.glazingfabric", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_indirect(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for the indirect solar and air temperature effect. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.indirect", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_internal(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for internal gains from people and APPLIANCES. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.internal", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_opaque_fabric(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for the conduction gains through only opaque fabric. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.opaquefabric", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_solar(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for the direct solar radiation through glazing. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to retrieve. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.solar", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_gains_total(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for the total sum of all gains for the given hour. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value.
        
        """ 
        arg_str = string_util._convert_args_to_string("get.results.gains.total", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)   

    def get_gains_ventilation(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for infiltration and ventilation. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.ventilation", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)   

    def get_gains_zonal(self, zone, hour):
        """
        
        Once an hourly thermal analysis has been performed for a single day 
        (either the Hourly Temperature Profile or Hourly Heat Gains/Losses 
        calculation), this command will directly access the calculated results 
        for inter-zonal gains. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to use. 
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified gains value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.gains.zonal", 
                                                      zone, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)   

    def get_solar_absorbed(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        amount of radiation absorbed by the surface (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.absorbed", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)   
        
    def get_solar_angle(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        angle of incidence (degrees). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.angle", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)   
        
    def get_solar_area(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        area of collector surface (m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.area", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)   

    def get_solar_available(self, hour):
        """
        
        Returns the available radiation value after a calc.solar.day calculation 
        for the amount of available solar radiation from the weather file, 
        given in (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.available", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)   

    def get_solar_diffuse(self, hour):
        """
        
        Returns solar radiation value after a calc.solar.day calculation for 
        the amount of diffuse radiation incident on surface (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.diffuse", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_solar_direct(self, hour):
        """
        
        Returns solar radiation value after a calc.solar.day calculation for 
        the amount of direct radiation incident on surface (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.direct", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_solar_global(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        total global horizontal radiation from Sun (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value. 
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.global", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_solar_incident(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        amount of radiation incident on the surface (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.incident", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_solar_reflected(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        amount of reflected incident radiation (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.reflected", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_solar_shading(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        percentage of surface shading (%). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.shading", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_solar_transmitted(self, hour):
        """
        
        Returns the radiation value after a calc.solar.day calculation for the 
        amount of radiation transmitted through the surface (W). 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        The hour to retrieve, being from 0 to 23. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified solar value.
        
        """
        arg_str = string_util._convert_args_to_string("get.results.solar.transmitted", 
                                                      hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)




if __name__ == "__main__":
    x = Results()
    
    #print x.get_array(3, 7)
    #print x.get_gains_glazing_fabric(12, 3)
    

    print "Tests completed"