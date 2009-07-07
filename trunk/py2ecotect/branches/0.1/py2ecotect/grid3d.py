import py2ecotect
from py2ecotect import StringUtil

class Grid3D(object):
    def delete(self):
        """
        
        This method deletes current 3D data and frees all associated memory. It 
        does not affect the current 2D analysis grid object. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("grid3d.reset")

    def getframe(self, index):
        """
        
        Use this method to get frames within the 3D data grid. When used in this 
        way, the third dimension of the 3D grid becomes an animation buffer for 
        the 2D grid. The 2D grid remains in the same relative position as frames 
        are copied from the frame buffer. This can be useful if you need to 
        directly compare results from a range of calculations carried out under 
        different conditions. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        Specifies which frame number to retrieve. The maximum number of frames 
        in the buffer is equal to the size of the 3D grid in the current axis. 
        Obvously, if you fill up the 3D frame buffer and then change the current 
        axis of the 2D grid, you will get invalid 2D results.
        
        """
        arg_str = StringUtil._convert_args_to_string("grid3d.getframe", index)
        py2ecotect.conversation.Exec(arg_str)

    def initialise(self):
        """
        
        Use this command to allocate memory for the 3D analysis space. The size 
        of the 3D grid and the number of cells is given as part of the 2D 
        analysis grid object. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("grid3d.initialise")

    def reset(self):
        """
        
        Use this method to reset all 3D grid values back to 0.0. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("grid3d.reset")

    def setframe(self):
        """
        
        Use this method to set frames within the 3D data grid. When used in 
        this way, the third dimension of the 3D grid becomes an animation buffer 
        for the 2D grid. The 2D grid remains in the same relative position as 
        frames are copied to the frame buffer. This can be useful if you need to 
        directly compare results from a range of calculations carried out under 
        different conditions. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        Specifies which frame number to set. The maximum number of frames in 
        the buffer is equal to the size of the 3D grid in the current axis. 
        Obvously, if you fill up the 3D frame buffer and then change the current 
        axis of the 2D grid, you will end up with invalid 2D results.
        
        """
        arg_str = StringUtil._convert_args_to_string("grid3d.setframe", index)
        py2ecotect.conversation.Exec(arg_str)

    def get_blockage(self, i, j, k, state):
        """
        
        Sets the CFD blockage flag of the specified grid cell. When in CFD mode, 
        the state value of each 3D grid cell stores information about boundary 
        conditions within the model, instead of the values outlined in the 
        get.grid3d.state property. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j, k 
        The 3D index of a cell within the analysis grid. Each must be an 
        integer between 0 and the current grid size - 1 in the relevant grid 
        axis. 
        
        state 
        An integer value for the configuration of the blockage flag, as outlined 
        in the following Grid Blockage Options table. 
        
        Relevant Data Table(s)
        
        Grid Blockage Options 
        Value Description 
        1 Cell blocked (set automatically during calculation). 
        2 Surface passes though cell (set during calculation). 
        4 Pressure boundary at cell (set during calculation). 
        8 Heat gains in cell (set during calculation). 
        16 Air outflow in cell (set during calculation). 
        32 Air intflow in cell (set during calculation). 
        64 Contaminant gains in cell (set during calculation). 
        128 Cell contains a WINDOW object (set during calculation). 
        256 Cell contains a VOID (set during calculation). 
        512 USED INTERNALLY FOR TEMPORARY FLAG 
        1024 Cell should be blocked no matter what is in it. 
        
        """
        arg_str = StringUtil._convert_args_to_string("set.grid3d.blockage", i, j, 
                                                     k, state)
        py2ecotect.conversation.Exec(arg_str)

    def get_cell(self, i, j, k, index = 0):
        """
        
        Retrieves the value stored in the specified 3D grid cell. Getting this 
        property returns two values. The first is the actual value of the cell 
        in the current units, while the second is the state of the 3D cell, 
        whether it is hidden or has been interactively selected by the user. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j, k 
        The 3D index of a cell within the analysis grid. Each must be an integer 
        between 0 and the current grid size - 1 in the relevant grid axis. 
        
        [index] 
        Each 3D grid cell has up to 3 different slots for storing values. The 
        optional [index] parameter specifies which particular slot this value 
        should be retrieved and can be 0, 1 or 2. If not specified, the 
        currently selected index is used. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        The value stored within the specified grid cell. 
        
        state 
        the state of the specified grid cell. The possible values returned are 
        shown in the following Grid Cell State Codes table. 
        
        Relevant Data Table(s)
        Grid Cell State Codes 
        Value Description 
        1 Visible and selected. 
        0 Visible but not selected. 
        -99 Disabled. 
        -100 Hidden. 
        -100 Hidden and selected. 

        """
        arg_str = StringUtil._convert_args_to_string("get.grid3d.cell", i, j, 
                                                     k, index)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_list(val, float, int)

    def set_cell(self, i, j, k, value, index = 0):
        """
        
        Sets the value stored in the specified 3D grid cell. 

        Parameter(s)
        This property takes the following parameters.
        
        i, j, k 
        The 3D index of a cell within the analysis grid. Each must be an integer 
        between 0 and the current grid size - 1 in the relevant grid axis. 
        value 
        The value to be stored within the specified grid cell. 
        [index] 
        Each 3D grid cell has up to 3 different slots for storing values. The 
        optional [index] parameter specifies which particular slot this value 
        should be stored in and can be 0, 1 or 2. If not specified, the 
        currently displayed index is used. 

        """
        arg_str = StringUtil._convert_args_to_string("set.grid3d.cell", i, j, 
                                                     k, value, index)
        py2ecotect.conversation.Exec(arg_str)

    def get_index(self, x, y, z):
        """
        
        Returns the i, j, k index of the specified 3D world coordinate given by 
        the x, y, z parameters. This function is necessary because the spacing 
        between cells in each axis can be set to any value by the user. In 
        addition to the i, j, k values returned is a boolean (0 or 1) value 
        specifying if the point is actually within the bounded grid volume. 
        Thus, before using the i, j, k indexes, first check they are valid, as 
        shown in the example code. 

        Parameter(s)
        This property takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        i, j, k 
        The 3D index of a cell within the analysis grid. Each is an integer 
        between 0 and the current grid size - 1 in the relevant grid axis. 
        
        valid 
        A boolean (0 or 1) value specifying if the node is actually within the bounded grid volume. 
        
        """
        arg_str = StringUtil._convert_args_to_string("get.grid3d.index", x, y, z)
        val = py2ecotect.conversation.Request(arg_str)
        print val
        #return StringUtil._convert_str_to_list(val, float, int)






if __name__ == "__main__":
    x = Grid3D()
    
    #x.delete()
    #x.getframe(4)
    #x.reset()
    #x.get_blockage(5, 3, 4, 64)
    print x.get_cell(15, 25, 4)
    #x.set_cell(15, 25, 4, 0.32)
    x.get_index(5500.0, 2500.0, 1800.0)
    
    
    
    
    print "Tests completed"