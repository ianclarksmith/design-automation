import py2ecotect
from py2ecotect import StringUtil

class Grid(object):
    def export(self, filename):
        """
        
        Use this command to export 2D analysis grid data as a comma separated 
        value (*.CSV) file. The file will be saved into the current model 
        directory by default. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        This parameter specifies the file where the data will be saved, and may 
        include a full pathname. However, be aware of the issues with backslashes in 
        filename parameters described here.
        
        """
        arg_str = StringUtil._convert_args_to_string("grid.export", filename)
        py2py2ecotect.conversation.Exec(arg_str)
    
    def fit_selection(self, fit_form = True):
        """
        
        Fits the analysis grid to the extents of currently selected objects. 
        This is the same as selecting the Fit to Selected Objects button in the 
        Analysis Grid panel. Calling this method updates the grid.max, grid.min 
        and grid.average properties. 

        Parameter(s)
        This command takes the following parameters.
        
        [fit_form] 
        This optional parameter determines whether the grid fits to the form as 
        well as the extents of the selected objects. This is a boolean value 
        where 1 or true represents the affirmative and 0 or false the negative. 
      
        """
        arg_str = StringUtil._convert_args_to_string("grid.fit.selection", fit_form)
        py2ecotect.conversation.Exec(arg_str)

    def fit_values(self):
        """
        
        Calculates the optimum scale required to fit the full range of currently 
        visible grid values. Calling this method updates the grid.scale property. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("grid.fit.values")

    def import_data(self, filename, operation = ""):
        """
        
        This command imports data from an external coma separated value (*.CSV) 
        file into the 2D analysis grid.

        When importing grid data you can perform a range of operations to 
        transform the grid information, where XXX can be one of the values shown 
        in the following table. 
        
        Parameter(s)
        This command takes the following parameters.
        
        filename 
        This parameter specifies the file where the data will be imported from, 
        and may include a full pathname. However, be aware of the issues with 
        backslashes in filename parameters described here. 
        
        Relevant Data Table(s)
        Grid Import Operations 
        Command Suffix Description 
         If no value is appended, current grid data is overwritten. 
        subtract Subtract imported data from existing data. 
        add Add imported data to existing data. 
        divide Divide existing data by imported data. 
        percentage Show existing data as a percentage of imported data. 

        """
        arg_str = StringUtil._convert_args_to_string("grid.import." + operation, 
                                                     filename)
        py2ecotect.conversation.Exec(arg_str)

    def load(self, filename):
        """
        
        This command loads any analysis grid stored as a (*.GRD) binary data 
        file. The loaded file contains both 2D and 3D grid data (if it exists) 
        as well as all other grid settings. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        This parameter specifies the file where the data will be imported from 
        and may include a full pathname. However, be aware of the issues with 
        backslashes in filename parameters described here.
        
        """
        arg_str = StringUtil._convert_args_to_string("grid.import", filename)
        py2ecotect.conversation.Exec(arg_str)

    def reset(self):
        """
        
        Use this command to reset all grid values back to zero. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("grid.reset")

    def save(self, filename):
        """
        
        This command saves the analysis grid as a (*.GRD) binary data file. The 
        saved file contains both 2D and 3D grid data (if it exists) as well as 
        all other grid settings. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        This parameter specifies the file where the data will be imported from, 
        and may include a full pathname. However, be aware of the issues with 
        backslashes in filename parameters described here. 
        
        """
        arg_str = StringUtil._convert_args_to_string("grid.save", filename)
        py2ecotect.conversation.Exec(arg_str)

    def show(self, show = True):
        """
        
        Displays the current analysis grid in the model. 

        Parameter(s)
        This command takes the following parameters.
        
        show 
        When given, this optional parameter determines whether to show or hide 
        the analysis grid in the main model view. This is a boolean value where 
        1 or true represents the affirmative and 0 or false the negative. If not 
        specified, this defaults to true. 
        
        """
        arg_str = StringUtil._convert_args_to_string("grid.show", show)
        py2ecotect.conversation.Exec(arg_str)

    def get_average(self):
        """
        
        Getting this property returns three values - the average value of all 
        enabled grid nodes, the number of enabled grid nodes, and the fraction 
        of enabled nodes above the clipping threshold (the minimum scale value). 
        This last value is only calculated when the Clip to Minimum option is 
        selected.

        Grids are generally rectilinear in shape. However, more complex shapes 
        can be accommodated using a large grid with some disabled nodes - this 
        is how the Fit Grid to Selected Objects button works. Note that the 
        above values are based on the number of enabled nodes in the grid, 
        irrespective of whether they are visible or not due to a clipping 
        threshold. 
        
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        avgValue 
        The average value of all enabled nodes within the currently displayed 
        grid. 
        
        nodeCount 
        The number of enabled nodes within the currently displayed grid. 
        
        fractAbove 
        The fraction of enabled nodes whose current data value is above the 
        minimum scale when the Clip to Minimum option is selected for the 
        currently displayed grid. 
        
        """
        val = py2ecotect.conversation.Request("get.grid.average")
        return StringUtil._convert_str_to_list(val, float, int, float)

    def get_axis(self):
        """
        
        Retrieves the grid axis, being the axis within which the 2D slice has 
        been drawn. The value returned is a single integer value corresponding 
        with the following table. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        axis 
        An integer value representing the current grid axis with a value from 
        the following Grid Axis table. 
        
        Relevant Data Table(s)
        
        Grid Axis Value Axis 
        0 XY Axis 
        1 YZ Axis 
        2 XZ Axis 

        """
        val = py2ecotect.conversation.Request("get.grid.axis")
        return StringUtil._convert_str_to_type(val, int)

    def set_axis(self, axis):
        """
        
        Sets the grid axis, being the axis within which the 2D slice has been 
        drawn. 

        Parameter(s)
        This property takes the following parameters.
        
        axis 
        A single integer value corresponding with the following Grid Axis table. 
        
        Relevant Data Table(s)
        
        Grid Axis Value Axis 
        0 XY Axis 
        1 YZ Axis 
        2 XZ Axis 

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.axis", axis)
        py2ecotect.conversation.Exec(arg_str)

    def get_cell(self, i, j, index = 0):
        """
        
        Retrieves the value stored in the specified grid cell. Two values are 
        returned - the first is the actual value of the cell in the current 
        units, whilst the second is the state of the cell. The possible state 
        values that can be returned are given in the following table. Each grid 
        cell can store up to 5 different data values. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the required cell within the 
        grid. Each must be an integer between 0 and the current grid size - 1 in 
        the relevant grid axis. 
        
        [index] 
        This optional parameter specifies the index of the specified data value 
        to be retieved and can be an integer between 0 and 4. If this parameter 
        is not specified, the currently selected data index is used. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        The current data value at the specified grid cell.

        """
        arg_str = StringUtil._convert_args_to_string("get.grid.cell", i, j, index)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_list(val, float, int)

    def set_cell(self, i, j, value, index = 0):
        """
        
        Sets the value to be stored in the specified grid cell. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant grid axis. 
        
        value 
        This parameter is the decimal value to be stored within the cell. 
        
        [index] 
        Each grid cell can store up to 5 different data values. This optional 
        parameter specifies which particular slot the specified value should be 
        stored in, and can be an integer between 0 and 4. If this parameter is 
        not specified, the currently displayed index is used by default.

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.cell", i, j, 
                                                     value, index)
        py2ecotect.conversation.Exec(arg_str)

    def get_data(self):
        """
        
        Each grid cell of the analysis grid can store up to 5 different values, 
        as displayed within the selection list in the DATA & SCALE section of 
        the Analysis Grid Panel. This property gets the currently displayed data 
        index. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The index of the grid cell data currently displayed. This is given as an 
        integer value in the range 0 to 4. 

        """
        val = py2ecotect.conversation.Request("get.grid.data")
        return StringUtil._convert_str_to_type(val, int)

    def set_data(self, index):
        """
        
        Each grid cell of the analysis grid can store up to 5 different values. 
        This property sets the grid cell index to be displayed. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        The index of the grid cell data to be displayed, given as an integer 
        value in the range 0 to 4.

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.data", index)
        py2ecotect.conversation.Exec(arg_str)

    def get_description(self, index):
        """
        
        Each cell of the analysis grid can store up to 5 different values, each 
        in an individual slot. This command returns the description for the 
        specified slot. If no slot is specified, the description returned is for 
        the currently selected index. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        This optional parameter specifies the particular slot to return the 
        description for, and can be an integer in the range 0 to 4. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        description 
        A text string containing the description of the nominated slot.
        
        """
        arg_str = StringUtil._convert_args_to_string("get.grid.description", 
                                                     index)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, str)

    def set_description(self, index, description):
        """
        
        Each cell of the analysis grid can store up to 5 different values, each 
        in an individual slot. This command sets the description for the 
        specified slot. If no slot is specified, the description is set for the 
        currently displayed index. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        This optional parameter specifies the particular slot to set the 
        description for, and can be an integer in the range 0 to 4. 
        
        description 
        The description to be used for the nominated slot.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.description", 
                                                     index, description)
        py2ecotect.conversation.Exec(arg_str)

    def get_flag(self, flag):
        """
        
        The analysis grid uses a series of boolean flags to control how it is 
        displayed in both the View and OpenGL canvasses. This property returns 
        the current state for the flag value/s specified. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer that specifies which flag state to return, according to the 
        following Grid Flags table
        
        To return the values for multiple flags at once, add their respective 
        values together. For example, using an integer value of 18 will return 
        the state for both the values and contours flags. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        [state] 
        The state of the specified flag(s). This is a boolean value where 1 or 
        true represents the affirmative and 0 or false the negative. 
        
        Relevant Data Table(s)
        
        Grid Flag Codes 
        Token Value Description 
        axis 1 Display grid axis with units. 
        values 2 Display text values at each grid node. 
        extents 4 Display a bounding box showing the full 3D grid space. 
         8 UNUSED. 
        contours 16 Display contours if variable data is available. 
        selected 32 Display text values at selected grid nodes only. 
        peaks 64 Display text values at peaks and troughs between values. 
        colours 128 Display colour-shaded grid squares. 
         256 UNUSED. 
        elastic 512 Use elastic method when dragging axial nodes. 
         1024 UNUSED. 
        clip 2048 Clip the displayed grid to those nodes above the minimum range. 
        average 4096 Display the average of all visible values at bottom of canvas. 
        lines 8192 Display grid lines. 
        3d 16384 Display grid values as a 3D peturbed surface. 
        daylight 32768 Indicates that grid displays valid daylight analysis results. 
 
        """
        arg_str = StringUtil._convert_args_to_string("get.grid.flag", 
                                                     flag)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, bool)

    def set_flag(self, flag, state = True):
        """
        
        The analysis grid uses a series of boolean flags to control how it is 
        displayed in both the View and OpenGL canvasses. This property sets the 
        current state for the flag value/s specified. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer that specifies which flag state to set, according to the 
        following Grid Flags table.
        
        To set the values for multiple flags at once, add their respective 
        values together. For example, using an integer value of 18 will set the 
        state for both the values and contours flags. 
        
        [state] 
        This optional parameter determines if the specified flag(s) are set or 
        not. This is a boolean value where 1 or true represents the affirmative 
        and 0 or false the negative. If this paramater is not specified, the 
        default state is set to true. 
        
        Relevant Data Table(s)
        
        Grid Flag Codes Token Value Description 
        axis 1 Display grid axis with units. 
        values 2 Display text values at each grid node. 
        extents 4 Display a bounding box showing the full 3D grid space. 
         8 UNUSED. 
        contours 16 Display contours if variable data is available. 
        selected 32 Display text values at selected grid nodes only. 
        peaks 64 Display text values at peaks and troughs between values. 
        colours 128 Display colour-shaded grid squares. 
         256 UNUSED. 
        elastic 512 Use elastic method when dragging axial nodes. 
         1024 UNUSED. 
        clip 2048 Clip the displayed grid to those nodes above the minimum range. 
        average 4096 Display the average of all visible values at bottom of canvas. 
        lines 8192 Display grid lines. 
        3d 16384 Display grid values as a 3D peturbed surface. 
        daylight 32768 Indicates that grid displays valid daylight analysis results. 

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.flag", 
                                                     flag, state)
        py2ecotect.conversation.Exec(arg_str)

    def set_fraction(self, fraction):
        """
        
        This property is a shortcut for setting the grid base offset when 
        animating through 3D data. Instead of giving an absolute base offset 
        using the set.grid.offset property, you can instead set the fraction of 
        the 2D grid section between the minimum and maximum extents in the 3D 
        grid. 

        Parameter(s)
        This property takes the following parameters.
        
        fraction 
        A decimal number between 0 and 1. This property can also be used to 
        cycle through indexed grid animation frames using the grid3d.setframe 
        command. 

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.fraction", 
                                                     fraction)
        py2ecotect.conversation.Exec(arg_str)

    def get_max(self):
        """
        
        Retreives the values for the maximum extent of the grid for the x y and 
        z axes. The axial values are given in absolute world co-ordinates. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        The absolute position in the X, Y and Z axis of the maximun extents of 
        the analysis grid in 3 dimensional model space.

        """
        val = py2ecotect.conversation.Request("get.grid.max")
        return StringUtil._convert_str_to_list(val, float, float, float)

    def set_max(self, x, y, z):
        """
        
        Sets the maximum values of the grid extents for the x, y and z axes. The 
        axial values are specified in absolute world co-ordinates. 

        Parameter(s)
        This property takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the maximun 
        extents of the analysis grid in 3 dimensional model space. 
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.max", x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def get_min(self):
        """
        
        Retreives the values for the minimum extent of the grid for the x y and 
        z axes. The axial values are given in absolute world co-ordinates. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        The absolute position in the X, Y and Z axis of the minimun extents of 
        the analysis grid in 3 dimensional model space.
        
        """
        val = py2ecotect.conversation.Request("get.grid.min")
        return StringUtil._convert_str_to_list(val, float, float, float)

    def set_min(self, x, y, z):
        """
        
        Sets the minimum values of the grid extents in theX, Y and Z axes. 

        Parameter(s)
        This property takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the minimun 
        extents of the analysis grid in 3 dimensional model space.

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.min", x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def get_offset(self):
        """
        
        Retrieves the grid base value, the offset distance of the 2D grid 
        section from the base of the 3D grid. See the grid.axis command for more 
        information. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        offset 
        The offset distance of the 2D grid section from the base of the 3D grid, 
        for the currently selected axis.
        
        """
        val = py2ecotect.conversation.Request("get.grid.offset")
        return StringUtil._convert_str_to_type(val, float)

    def set_offset(self, offset):
        """
        
        Sets the grid base value. If full 3D grid values have been calculated, 
        you can use this value to animate the grid by cycling between the 
        minimum and maximum range in the current axis. 

        Parameter(s)
        This property takes the following parameters.
        
        base 
        The offset distance of the 2D grid section from the base of the 3D grid, 
        for the currently selected axis. See the grid.axis 

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.offset", offset)
        py2ecotect.conversation.Exec(arg_str)

    def get_position(self, i, j):
        """
        
        Retrieves the position of a grid point. Three values are returned, being 
        the x y and z coordinates of the specified cell. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant grid axis. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the grid cell 
        node in 3 dimensional model space.
        
        """
        arg_str = StringUtil._convert_args_to_string("get.grid.position", i, j)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_list(val, float, float, float)

    def set_position(self, i, j, pos):
        """
        
        Sets the position of a grid point. Note that setting this value is only 
        possible when the grid has been form fit to selected objects using the 
        grid.fit.selection command, or by selecting the Fit to Selected Objects > 
        3D Form button in the Analysis Grid panel. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant axis. 
        
        pos 
        Thisparameter is the absolute world coordinate of the cell in the 
        current grid axis. Thus if the axis is currently set to XY (0), then a 
        value of 1500 would equate to a height of 1.5m in the z axis. 
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.position", i, j,
                                                     pos)
        py2ecotect.conversation.Exec(arg_str)

    def get_range(self):
        """
        
        Getting this property returns the minimum and maximum base offsets in 
        the current axis. The base offset property of the grid will therefore be 
        within these two values. This is basically a shortcut to the grid.min 
        and grid.max where only values for the currently selected grid axis are 
        returned. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        min 
        The minimum value in the current grid axis. 
        
        max 
        The maximum value in the current grid axis. 
                
        """
        val = py2ecotect.conversation.Request("get.grid.range")
        return StringUtil._convert_str_to_list(val, float, float)

    def get_scale(self):
        """
        
        Returns the scale values used to colour the grid and define the number 
        of contours displayed. Three values are returned, being the minimum 
        scale, the maximum scale, and the increments used to draw the contours. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        min 
        The minimum scale value. 
        
        max 
        The maximum scale value. 
        
        inc 
        The increment size used to draw contours. 
        
        """
        val = py2ecotect.conversation.Request("get.grid.scale")
        return StringUtil._convert_str_to_list(val, float, float, float)

    def set_scale(self,min, max, inc):
        """
        
        Sets the scale range values used to colour the grid and define the 
        number of contours displayed. 

        Parameter(s)
        This property takes the following parameters.
        
        min 
        The minimum scale value. 
        
        max 
        The maximum scale value. 
        
        inc 
        The increment size used to draw contours.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.scale", min, max,
                                                     inc)
        py2ecotect.conversation.Exec(arg_str)

    def get_size(self):
        """
        
        Retrieves the number of cells within the current analysis grid, for each 
        of its axes. Three integer values are returned, being the x, y and z 
        grid cell values. If the z value returns as 0, this means that the 
        current analysis grid is not configured as a 3D analysis grid. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        ix, jy, kz 
        The number of grid cells in each of the X, Y and Z axis directions. 

        """
        val = py2ecotect.conversation.Request("get.grid.size")
        return StringUtil._convert_str_to_list(val, int, int, int)

    def set_size(self, ix, jy, kz):
        """
        
        Sets the number of cells to use with the current analysis grid, for each 
        of its axes. 

        Parameter(s)
        This property takes the following parameters.
        
        ix, jy, kz 
        These parameters define the number of grid cells to create in each of 
        the X, Y and Z axis directions of the analysis grid. If kz is not 
        specified, the analysis grid becomes a 2D analysis grid.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.size", ix, jy, kz)
        py2ecotect.conversation.Exec(arg_str)

    def get_state(self, i, j):
        """
        
        Retrieves the state of the specified grid cell. The possible values 
        returned correspond with the following table. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant grid axis. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        An integer value representing the state of the specified cell, according 
        to the following Grid Cell State table 
        
        Relevant Data Table(s)
        
        Grid Cell State Codes Value Description 
        1 Visible and selected. 
        0 Visible but not selected. 
        -99 Disabled. 
        -100 Hidden. 
        -100 Hidden and selected. 

        """
        arg_str = StringUtil._convert_args_to_string("get.grid.state", i, j)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)

    def set_state(self, i, j, state):
        """
        
        Sets the state of the specified grid cell. The possible values returned 
        correspond with the following table. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant grid axis. 
        
        state 
        This parameter is an integer value that controls how the specified cell 
        is to be acted upon and displayed, according to the following Grid Cell 
        State table 
        
        Relevant Data Table(s)
        
        Grid Cell State Codes Value Description 
        1 Visible and selected. 
        0 Visible but not selected. 
        -99 Disabled. 
        -100 Hidden. 
        -100 Hidden and selected. 

        """
        arg_str = StringUtil._convert_args_to_string("set.grid.state", i, j, 
                                                     state)
        py2ecotect.conversation.Exec(arg_str)

    def get_title(self):
        """
        
        Retrieves the title of the current analysis grid. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        title 
        A text string up to 64 characters in length. 
        
        """
        val = py2ecotect.conversation.Request("get.grid.title")
        return StringUtil._convert_str_to_type(val, str)

    def set_title(self, title):
        """
        
        Sets the title of the current analysis grid. 

        Parameter(s)
        This property takes the following parameters.
        
        title 
        A text string up to 64 characters in length containing the new title.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.title", title)
        py2ecotect.conversation.Exec(arg_str)

    def get_units(self, index = 0):
        """
        
        Retrieves the units of measurement used for the values stored in the 
        analysis grid, such as Lux or W/m^2. 

        Parameter(s)
        This property takes the following parameters.
        
        [index] 
        Each grid cell can store up to 5 different values and units of 
        measurement. This optional parameter specifies which slot to retrieve 
        the units for and can be an integer in the range 0 to 4. If not 
        specified, the currently selected index is used by default. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        units 
        A text string containing the units name of the nominated slot.
        
        """
        arg_str = StringUtil._convert_args_to_string("get.grid.units", index)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, str)

    def set_units(self, units, index = 0):
        """
        
        Sets the units of measurement used for the values stored in the analysis 
        grid. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        Each grid cell can store up to 5 different values and units of 
        measurement. The optional [index] parameter specifies which slot to 
        change the units for, and can be an integer in the range 0 to 4. If the 
        [index] parameter is not specified, the currently displayed index is 
        used by default. 
        units 
        Specifies what units of measurement to use, and can be a short string 
        such as Lux or W/m^2. 
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.units", index, 
                                                     units)
        py2ecotect.conversation.Exec(arg_str)

    def get_vector(self, i, j):
        """
        
        Retrieves the vector value stored in the specified grid cell. Three 
        values are returned, being the x y and z components of the vector value. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant grid axis. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dx, dy, dz 
        A vector value representing the offset distance in each of the X, Y and 
        Z axis, given in model coordinates. 
        
        """
        arg_str = StringUtil._convert_args_to_string("get.grid.vector", i, j)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_list(val, float, float, float)

    def set_vector(self, i, j, dx, dy, dz):
        """
        
        Sets the vector value stored in the specified grid cell. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant grid axis. 
        dx, dy, dz 
        A vector value representing the offset distance in each of the X, Y and 
        Z axis, given in model coordinates.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid.vector", i, j, 
                                                     dx, dy, dz)
        py2ecotect.conversation.Exec(arg_str)

    def get_zone(self, i, j, axis = 0, draw = False):
        """
        
        Attempts to determine the zone within which the grid cell resides. This 
        is achieved by drawing a test ray in the direction specified by the 
        given axis. The first object hit by this ray gives the zone within which 
        this specified grid cell is located. If an axis value of 0 is used, only 
        FLOOR objects within each zone are checked - this is a very quick 
        calculation and is usualy the most appropriate axis. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j 
        The horizontal and vertical position of the cell within the grid where 
        the value is to be stored. Each must be an integer between 0 and the 
        current grid size - 1 in the relevant grid axis. 
        
        [axis] 
        Specifies the axis about which to trace the test ray, according to the 
        following Grid Axis table. If not specified, the XY axis is used and 
        only FLOOR objects checked. 
        
        [draw] 
        This optional parameter determines if the test ray should be drawn in 
        the 3D EDITOR page or not. This is a boolean value where 1 or true 
        represents the affirmative and 0 or false the negative. If not specified, 
        the default setting is not to draw each test ray. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        zone 
        The zero-based index of the zone within which the specified grid cell is most likely located. 
        
        Relevant Data Table(s)
        
        Grid Axis 
        Value Axis 
        0 XY Axis 
        1 YZ Axis 
        2 XZ Axis 

        """
        arg_str = StringUtil._convert_args_to_string("get.grid.zone", i, j, 
                                                     axis, draw)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)











if __name__ == "__main__":
    x = Grid()
    
    #x.export("C:\\Test\\grid.csv")
    #x.fit_selection(True)
    #x.fit_values()
    #x.import_data("C:\\Test\\grid.csv")
    #x.reset()
    #x.save("C:\\Test\\grid.grd")
    x.show()
    #print x.get_average()
    #print x.get_axis()
    #x.set_axis(1)
    #print x.get_cell(5, 5, 3)
    #x.set_cell(5, 5, 3.1415, 3)
    #print x.get_data()
    #x.set_data(3)
    #print x.get_description(1)
    #x.set_description(1, "TEST")
    #print x.get_flag(1)
    #x.set_flag(1)
    #x.set_fraction(0.75)
    #print x.get_max()
    #x.set_max(5000, 7500, 3000)
    #print x.get_min()
    #x.set_min(5000, 7500, 3000)
    #print x.get_offset()
    #x.set_offset(700)
    #print x.get_position(5, 10)
    #x.set_position(12, 24, 1500.0)
    #print x.get_range()
    #print x.get_scale()
    #x.set_scale(3000, 10000, 500)
    #print x.get_size()
    #x.set_size(25, 40, 16)
    #print x.get_state(5, 10)
    #x.set_state(5, 10, -99)
    #print x.get_title()
    #x.set_title("TEST")
    #print x.get_units(3)
    #x.set_units("W/m2", 3)
    #print x.get_vector(5, 10)
    #x.set_vector(5, 10, 0, 245, 100)
    #print x.get_zone(5, 3, True)
    
    print "Tests completed"
    
    
    
    
    
    