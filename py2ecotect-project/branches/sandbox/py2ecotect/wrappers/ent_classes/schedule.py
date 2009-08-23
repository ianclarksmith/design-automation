import py2ecotect as p2e

class Schedule(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def add(self, name):
        """
        
        This command creates a new operational schedule within the current 
        model, and returns the zero-based index of the created schedule. 

        Parameter(s)
        This command takes the following parameters.
        
        name 
        A text string specifying the name of the new schedule.
        
        """
        arg_str = p2e._util._convert_args_to_string("schedule.add", name)
        p2e._app.Exec(arg_str)
    
    def delete(self, schedule):
        """
        
        Deletes the specified schedule. 

        Parameter(s)
        This command takes the following parameters.
        
        schedule 
        The zero-based index of the schedule or its name. The index can be 
        determined by using the get.schedule.index command or by viewing the 
        Schedule Editor dialog with sorting turned off.
        
        """
        arg_str = p2e._util._convert_args_to_string("schedule.delete", schedule)
        p2e._app.Exec(arg_str)
    
    def load(self, filename):
        """
        
        Loads the specified schedule library file .slf. Note that loading a 
        schedule library will replace all existing schedules in the model with 
        those in the library file. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to the library file to load.
        
        """
        arg_str = p2e._util._convert_args_to_string("schedule.load", filename)
        p2e._app.Exec(arg_str)
    
    def profile_read(self, schedule, profile, filename):
        """
        
        Reads the specified daily profile contained within a schedule from the 
        selected text-based 24 hour profile file (*.pfl). 

        Parameter(s)
        This command takes the following parameters.
        
        schedule 
        The zero-based index of the schedule to read from. 
        
        profile 
        The index of the daily profile to read, being from 0-11. 
        
        filename 
        The full path to the profile file to read from. 
        
        """
        arg_str = p2e._util._convert_args_to_string("schedule.profile.read", 
                                                      schedule, profile, filename)
        p2e._app.Exec(arg_str)
    
    def profile_write(self, schedule, profile, filename):
        """
        
        Writes a daily profile to the schedule in the selected text-based 24 
        hour profile file (*.pfl). 

        Parameter(s)
        This command takes the following parameters.
        
        schedule 
        The zero-based index of the schedule to write to. 
        
        profile 
        The index of the daily profile (0-11) to write to. 
        
        filename 
        The full path to where the profile file will be written. 

        """
        arg_str = p2e._util._convert_args_to_string("schedule.profile.write", 
                                                      schedule, profile, filename)
        p2e._app.Exec(arg_str)
    
    def read(self, schedule, filename):
        """
        
        Reads from a schedule defined inside a text-based hourly schedule data 
        file (*.sch). 

        Parameter(s)
        This command takes the following parameters.
        
        schedule 
        The zero-based index of the schedule to read from. 
        filename 
        The full path to the schedule data file to read from. 
        
        """
        arg_str = p2e._util._convert_args_to_string("schedule.read", 
                                                      schedule, filename)
        p2e._app.Exec(arg_str)
    
    def save(self, filename):
        """
        
        Saves a schedule library file (.slf) to the specified location. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to where the schedule library file will be written. 
        
        """
        arg_str = p2e._util._convert_args_to_string("schedule.save", 
                                                      filename)
        p2e._app.Exec(arg_str)
    
    def write(self, schedule, filename):
        """
        
        Saves a schedule to a text-based hourly schedule data file (*.sch). 

        Parameter(s)
        This command takes the following parameters.
        
        schedule 
        The zero-based index to write to. 
        filename 
        The full path to where the schedule data file will be written. 

        """
        arg_str = p2e._util._convert_args_to_string("schedule.write", 
                                                      schedule, filename)
        p2e._app.Exec(arg_str)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_activation(self, schedule, profile, hour):
        """
        
        Retrieves the activation value of the specified profile within the 
        given schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        profile 
        The zero-based index (0-11) of the profile. 
        
        hour 
        An integer between 0 and 23, where 0 is midnight on the previous day 
        and 23 is 11:00pm on the given day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        activation 
        A decimal value between 0 and 1. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.schedule.activation", 
                                                     schedule, profile, hour)
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)
    
    def set_activation(self, schedule, profile, hour, value):
        """
        
        Sets the activation value of the specified profile within the given 
        schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        profile 
        The zero-based index (0-11) of the profile. 
        
        hour 
        An integer between 0 and 23, where 0 is midnight on the previous day 
        and 23 is 11:00pm on the given day. 
        
        value 
        A decimal value between 0 and 1. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.schedule.activation", 
                                                     schedule, profile, hour, 
                                                     value)
        p2e._app.Exec(arg_str)
    
    def get_day(self, schedule, day):
        """
        
        Retrieves the profile used for the specified day of the year. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        day 
        The julian date given as an integer between 1 and 365. 
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based daily profile index.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.schedule.day", 
                                                     schedule, day)
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)
    
    def set_day(self, schedule, day, profile):
        """
        
        Sets the profile used for the specified day of the year. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        day 
        The julian date given as an integer between 1 and 365. 
        
        profile 
        The zero-based index of the profile, being a value between 0 and 11.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.schedule.day", 
                                                     schedule, day, profile)
        p2e._app.Exec(arg_str)
    
    def get_index(self, name):
        """
        
        Returns the zero-based index of the schedule specified by its name. If 
        no matching name is found, an index of -1 is returned. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        A string containing the name to match. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the matching schedule.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.schedule.index", name)
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)
    
    def get_magnitude(self, schedule):
        """
        
        Retrieves the magnitude value assigned to the specified schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        magnitude 
        The schedule magnitude value. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.schedule.magnitude", 
                                                      schedule)
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)
    
    def set_magnitude(self, schedule, value):
        """
        
        Sets the magnitude value assigned to the specified schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        value 
        Magnitudes are not currently used within ECOTECT, but will be when 
        exporting schedules to other external applications. The magnitude 
        values will be user-defined and depend on the specific application of 
        the schedule in each application.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.schedule.magnitude", 
                                                     schedule, value)
        p2e._app.Exec(arg_str)

    def get_name(self, schedule):
        """
        
        Retrieves the specified schedule's name. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        name 
        A string of up to 128 characters in length.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.schedule.name", 
                                                      schedule)
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_type(val, str)

    def set_name(self, schedule, name):
        """
        
        Sets the name of the specified schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        name 
        A string of up to 128 characters in length.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.schedule.name", 
                                                     schedule, name)
        p2e._app.Exec(arg_str)

    def get_profile_index(self, schedule, name):
        """
        
        Retrieves the index of a daily profile within the specified schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        name 
        A string representing the name of the profile. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based daily profile index. 

        """
        arg_str = p2e._util._convert_args_to_string("get.schedule.profile.index", 
                                                      schedule, name)
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)
        
    def get_profile_name(self,schedule, index):
        """
        
        Retrieves the name of a daily profile within the specified schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        index 
        An integer between 0 and 11 representing the zero-based index of the 
        profile to use. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        name 
        A string representing the name of the profile.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.schedule.profile.name", 
                                                      schedule, index)
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_type(val, int)
        
    def set_profile_name(self,schedule, index, name):
        """
        
        Sets the name of a daily profile within the specified schedule. 

        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        The zero-based index of the schedule. 
        
        index 
        An integer between 0 and 11 representing the zero-based index of the 
        profile to use. 
        
        name 
        A text string containing the new profile name.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.schedule.profile.name", 
                                                     schedule, index, name)
        p2e._app.Exec(arg_str)

