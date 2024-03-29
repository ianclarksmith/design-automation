import py2ecotect as p2e

class Graph(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def copy(self, format = "bmp"):
        """
    
        Copies the current graph to the clipboard. Using a command suffix of wmf 
        or bmp, it is possible to specify the graphic format used. If not 
        specified, the default format is a bitmap. 
    
        Parameter(s)
        There are no parameters for this command.
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.copy", format)
        p2e._app.Exec(arg_str)
    
    def dock(self, docked = True):
        """
        
        Use this command to dock or undock the Graphical Results graph from its 
        position in the Analysis page of the main application window. When 
        undocked, the graph appears in a seperate dialog box. 
    
        Parameter(s)
        This command takes the following parameters.
        
        [docked] 
        Determines whether the Graphical Results graph is in the docked position 
        or not, given as a boolean value where 1 or true represents the 
        affirmative and 0 or false the negative. 
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.dock", docked)
        p2e._app.Exec(arg_str)
    
    def draw(self):
        """
        
        This set of commands allows you to draw simple objects within the 
        analysis graph. This can be useful for adding simple annotations to a 
        graph just prior to saving the image for use in a report.
    
        The 2D functions with x, y parameters are based on actual screen pixels 
        relative to the top left corner of the graph. The get.graph.size 
        scripting property can be used to retrieve the width and height of the 
        current graph. The 3D functions with x, y, z parameters are based on the 
        3D graph dimensions derived from the actual units in the X and Y axis. 
        Even though most graphs are shown only in 2D, it is a fully 3D 
        enviroment simply viewed in plan - thus you can specify a 3D position, 
        but this is only used in specific 3D 
        graphs.
        
        It is possible to swap between the 2D and 3D move/line/arrow functions 
        at any time. For example, this allows you to place explanatory text at 
        an absolute position on the 2D screen and then have an arrow properly 
        point at some part of the 3D graph, independent of the current 3D graph 
        projection. 
        
        Parameter(s)
        There are no parameters for this command.
    
        """
        p2e._app.Exec("graph.draw")
    
    def draw_arrow2d(self, offset, size = 0):
        """
        
        Draws a 2D arrow object from the origin point to the specified 2D screen 
        location in the current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        x, y 
        Represents a position on the screen in the X and Y axis as an offset 
        from the top-left corner in pixels of the display canvas or control 
        being used. 
        
        [size] 
        This optional parameter sets the size of the object in pixels. 
            
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.arrow2d", 
                                                      x, y, size)
        p2e._app.Exec(arg_str)
    
    def draw_arrowto(self, absolute_position, size = 0):
        """
        
        Draws a 3D arrow object from the origin point to the specified 3D world 
        position in the current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales. 
        
        [size] 
        This optional parameter sets the size of the object in the current 
        modelling units.
            
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.arrowto", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2], size)
        p2e._app.Exec(arg_str)
    
    def draw_cross(self, absolute_position):
        """
        
        Draws a 2D cross object at the specified location within the current 
        graph. 
    
        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        A list of three values that represents the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales. 
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.cross", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2])
        p2e._app.Exec(arg_str)
    
    def draw_line2d(self, offset):
        """
        
        Draws a 2D line object from the origin point to the specified 2D screen 
        location in the current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        offset 
        A list of two values that represent a position on the screen in the 
        X and Y axis as an offset from the top-left corner in pixels of the 
        display canvas or control being used. 
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.line2d", 
                                                      offset[0],
                                                      offset[1])
        p2e._app.Exec(arg_str)
    
    def draw_lineto(self, absolute_position):
        """
        
        Draws a 3D line object from the origin point to the specified 3D world 
        position in the current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales.
        
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.lineto", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2])
        p2e._app.Exec(arg_str)
    
    def draw_move2d(self, offset):
        """
        
        Moves the 2D origin point to the specified 2D screen location in the 
        current 
        view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        offset 
        A list of two values that represent a position on the screen in the 
        X and Y axis as an offset from the top-left corner in pixels of the 
        display canvas or control being used. 
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.move2d", 
                                                      offset[0], offset[1])
        p2e._app.Exec(arg_str)
        
    def draw_moveto(self, absolute_position):    
        """
        
        Moves the 3D origin point to the specified 3D world position within the 
        current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales. 
        
        """
        
        arg_str = p2e._util._convert_args_to_string("graph.draw.moveto", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2])
        p2e._app.Exec(arg_str)
    
    def draw_pixel(self, absolute_position):
        """
        
        Draws a pixel at the specified 3D location inside the curent graph. 
    
        Parameter(s)
        This command takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.pixel", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2])
        p2e._app.Exec(arg_str)
    
    def draw_point(self, absolute_position):
        """
        
        Draws a point at the specified 3D world position within the current 
        view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales.
          
        """    
        arg_str = p2e._util._convert_args_to_string("graph.draw.point", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2])
        p2e._app.Exec(arg_str)
    
    def draw_sphere(self, absolute_position, radius):
        """
        
        Draws a 3D sphere object at the specified 3D world position in the 
        current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales. 
        
        radius 
        The radius of the sphere in the current modelling units.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.sphere", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2], 
                                                      radius)
        p2e._app.Exec(arg_str)
    
    def draw_text(self, absolute_position, text):
        """
        
        Displays a string of text at the specified 3D world position inside the 
        current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point within the current graph given in the units 
        of its axial scales. 
        
        text 
        The text string to be displayed. The HTML-like formatting tags that can 
        be used within this text are shown in the Formatted Text Tags table 
        below. 
        
        Relevant Data Table(s)
        
        Formatted Text Tags 
        Simple Tag Description 
        <strike></strike> Strike-through text. 
        <u></u> Underline 
        <i></i> Italic 
        <b></b> Bold 
        <sup></sup> Superscripted 
        <sub></sub> Subscripted 
        <up></up> Incease font size by 1pt (may be nested). 
        <r></r> Red text 
        <y></y> Yellow text 
        <g></g> Green text 
        <w></w> White text 
        <#XXXXXX><#> Changes colour to specified RGB hexidecimal notation, where 
        FFFFFF is white, 000000 is black and 0000FF is blue etc. 
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.text", 
                                                      absolute_position[0],
                                                      absolute_position[1], 
                                                      absolute_position[2], text)
        p2e._app.Exec(arg_str)
    
    def draw_text2d(self, offset, string):
        """
        
        Displays a string of text at the specified 3D world position inside the 
        current view. 
    
        Parameter(s)
        This command takes the following parameters.
        
        offset 
        A list of two values that represent a position on the screen in the 
        X and Y axis as an offset from the top-left corner in pixels of the 
        display canvas or control being used. 
        
        string 
        The text string to be displayed. The HTML-like formatting tags that can 
        be used within this text are shown in the Formatted Text Tags table 
        below. 
        
        Relevant Data Table(s)
        
        Formatted Text Tags 
        Simple Tag Description 
        <strike></strike> Strike-through text. 
        <u></u> Underline 
        <i></i> Italic 
        <b></b> Bold 
        <sup></sup> Superscripted 
        <sub></sub> Subscripted 
        <up></up> Incease font size by 1pt (may be nested). 
        <r></r> Red text 
        <y></y> Yellow text 
        <g></g> Green text 
        <w></w> White text 
        <#XXXXXX><#> Changes colour to specified RGB hexidecimal notation, where 
        FFFFFF is white, 000000 is black and 0000FF is blue etc. 
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.draw.text2d", 
                                                      offset[0], 
                                                      offset[1], 
                                                      string)
        p2e._app.Exec(arg_str)
    
    def mouse_event(self, action, location):
        """
        
        Parameter(s)
        This command takes the following parameters.
        
        action 
        This parameter specifies the type of action/operation to use with the 
        mouse at the given screen location. See the following table for details. 
        
        location
        A list of two values that represent the horizontal X location of the 
        desired mouse operation in pixel coordinates relative to the left 
        corner of the application window and the vertical Y location of the 
        desired mouse operation in pixel coordinates relative to the top corner 
        of the application window. 
        
        Relevant Data Table(s)
        
        Available Mouse Actions Token Description 
        move move mouse to new position 
        lclick Left mouse button clicked 
        ldown Left mouse button pressed 
        lup Left mouse button released 
        rclick Right mouse button clicked 
        rdown Right mouse button pressed 
        rup Right mouse button released 
        mclick Middle mouse button clicked 
        mdown Middle mouse button pressed 
        mup Middle mouse button released 
        wdown Mouse wheel pressed 
        wup Mouse wheel released 
        ldblclick Left mouse button double-clicked 
        rdblclick Right mouse button double-clicked 
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.mouseevent", 
                                                      action, location[0], 
                                                      location[1])
        p2e._app.Exec(arg_str)
    
    def pan_down(self, shift = True):
        """
        
        Pans the current results graph in the down direction by an increment of 
        10 deg. 
    
        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to 1 or true, then an increment of 
        1 deg is used instead, as if the Shift key were pressed.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.pandown", shift)
        p2e._app.Exec(arg_str)
    
    def pan_left(self, shift = True):
        """
        
        Pans the current results graph in the left direction by an increment of 
        10 deg. 
    
        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to 1 or true, then an increment of 
        1 deg is used instead, as if the Shift key were pressed.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.panleft", shift)
        p2e._app.Exec(arg_str)
    
    def pan_right(self, shift = True):
        """
        
        Pans the current results graph in the right direction by an increment of 
        10 deg. 
    
        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to 1 or true, then an increment of 
        1 deg is used instead, as if the Shift key were pressed.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.panright", shift)
        p2e._app.Exec(arg_str)
    
    def pan_up(self, shift = True):
        """
        
        Pans the current results graph in the up direction by an increment of 
        10 deg. 
    
        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to 1 or true, then an increment of 
        1 deg is used instead, as if the Shift key were pressed.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.panup", shift)
        p2e._app.Exec(arg_str)
    
    def redraw(self):
        """
        
        Redraws the current results graph. This is useful if you have made 
        several 
        changes and wish to update the canvas before continuing. 
    
        Parameter(s)
        There are no parameters for this command.
        
        """
        p2e._app.Exec("graph.redraw")
    
    def save(self, filename):
        """
        
        Saves the current graph using the specified filename to the current 
        model directory. The default format for this command is a bitmap (.BMP) 
        file.
    
        If you wish to save the file into a directory other than the current 
        model directory, you must include the full pathname, as shown in the 
        following example. However, be aware of the issues with backslashes in 
        filename parameters as described here. 
        
        Parameter(s)
        This command takes the following parameters.
        
        filename 
        A text string specifying the filename to use for the saved file. 
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.save", filename)
        p2e._app.Exec(arg_str)
    
    def save_bmp(self, filename):
        """
        
        Saves the current graph using the specified filename to the current 
        model directory, as a bitmap (.BMP) file.

        If you wish to save the file into a directory other than the current 
        model directory, you must include the full pathname, as shown in the 
        following example. However, be aware of the issues with backslashes in 
        filename parameters as described here. 
        
        Parameter(s)
        This command takes the following parameters.
        
        filename 
        A text string specifying the filename to use for the saved file.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.save.bmp", filename)
        p2e._app.Exec(arg_str)

        
    def save_results(self, filename):
        """
        
        Saves the current graph using the specified filename to the current 
        model directory, as an ASCII comma separated values (.CSV) file. This 
        allows graph data to be used in other applications, such as a Microsoft 
        Excel.
    
        If you wish to save the file into a directory other than the current 
        model directory, you must include the full pathname, as shown in the 
        following example. However, be aware of the issues with backslashes in 
        filename parameters as described here. 
        
        Parameter(s)
        This command takes the following parameters.
        
        filename 
        A text string specifying the filename to use for the saved file. 
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.save.results", 
                                                      filename)
        p2e._app.Exec(arg_str)
    
    def save_wmf(self, filename):
        """
        
        Saves the current graph using the specified filename to the current 
        model directory, in the windows metafile (.WMF) format.
    
        If you wish to save the file into a directory other than the current 
        model directory, you must include the full pathname, as shown in the 
        following example. However, be aware of the issues with backslashes in 
        filename parameters as described here. 
        
        Parameter(s)
        This command takes the following parameters.
        
        filename 
        A text string specifying the filename to use for the saved file.
        
        """
        arg_str = p2e._util._convert_args_to_string("graph.save.wmf", filename)
        p2e._app.Exec(arg_str)
    
    def show(self):
        """
        
        Displays the results graph dialog and brings it to the front if it is 
        behind any other windows. 
    
        Parameter(s)
        There are no parameters for this command.
    
        """
        p2e._app.Exec("graph.show")
    
    def zoom_in(self, shift = True):
        """
        
        Zooms in on the current graph by an increment of 10 deg. 
    
        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to 1 or true, then an increment of 1 
        deg is used instead, as if the Shift key were pressed.
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.zoomin", shift)
        p2e._app.Exec(arg_str)
    
    def zoom_out(self, shift = True):
        """
        
        Zooms out from the current graph by an increment of 10 deg. 
    
        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, then an increment of 1deg is 
        used instead, as if the Shift key were pressed.
    
        """
        arg_str = p2e._util._convert_args_to_string("graph.zoomout", shift)
        p2e._app.Exec(arg_str)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_font(self):
        """
        
        Retrieves the font currently being used to output text in the current 
        analysis graph, returning two values. 
    
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        size 
        This is an integer value describing the size of the font in points. 
        
        name 
        The full name of the font type being used.
    
        """
        val = p2e._app.Request("get.graph.font")
        return p2e._util._convert_str_to_list(val, int, str)
    
    def set_font(self, size, name):
        """
        
        Sets the font to be used for subsequent output text in the current 
        analysis graph. See the graph.draw group of commands for more 
        information. 
    
        Parameter(s)
        This property takes the following parameters.
        
        size 
        The font size to be used. This is usually given as a negative number to 
        tell Windows to use the height of the font. A positive number is used to 
        set the default font cell size. 
        name 
        The string identifier of the font to use, for example Arial, Verdana or 
        Courier New. The font name specified should be enclosed in "", as shown 
        in the following example.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.graph.font", size, 
                                                      name)
        p2e._app.Exec(arg_str)
    
    def get_pen(self):
        """
        
        Retrieves the current pen colour and size used within the graph 
    
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        colour 
        The colour of the pen given as formatted RGB hexidecimal number, in the 
        form 0xFF8800 or FF8800. 
        
        width 
        The thickness of the pen line in pixels. 
    
        """
        val = p2e._app.Request("get.graph.pen")
        return p2e._util._convert_str_to_list(val, str, int)
    
    def set_pen(self, colour, width):
        """
        
        Sets the current pen colour and size. 
    
        Parameter(s)
        This property takes the following parameters.
        
        colour 
        A RGB hexidecimal number, given as a string in the form 0xFF8800 or 
        FF8800. 
        
        width 
        The thickness of the pen line in pixels.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.graph.pen", colour, 
                                                      width)
        p2e._app.Exec(arg_str)
    
    def get_point(self, absolute_position):
        """
        
        Returns the 2D screen position of the specified 3D point within the 
        current graph. The 2D position is given as an x, y pixel value relative 
        to the top-left corner of the screen. These values can then be used to 
        position the mouse or a help hint, for example. 
    
        Parameter(s)
        This property takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y 
        The 2D screen position given as X and Y axis offsets from the top-left 
        corner of the graph canvas, in pixels.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.graph.point", 
                                                      absolute_position[0], 
                                                      absolute_position[1], 
                                                      absolute_position[2])
        val = p2e._app.Request(arg_str)
        return p2e._util._convert_str_to_list(val, int, int)
    
    def get_pos(self):
        """
        
        Retrieves the current position of the Graphical Results dialog. The 
        values returned are in relation to the local screen coordinates and the 
        top left hand corner of the dialog, measured in pixels. To use this 
        command, the Graphical Results dialog must be undocked from the Analysis 
        page in the main application window. For more information, see the 
        graph.dock command. 
    
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        left 
        The distance from the left of the screen to the left of the graph, in 
        pixels. 
        
        top 
        The distance from the top of the screen to the top of the graph, in 
        pixels.
        
        """
        val = p2e._app.Request("get.graph.pos")
        return p2e._util._convert_str_to_list(val, int, int)
    
    def set_pos(self, left, top):
        """
        
        Sets the current position of the Graphical Results dialog when it is 
        undocked. The values specified are in relation to the local screen 
        coordinates and the top left hand corner of the dialog, measured in 
        pixels. To use this command, the Graphical Results dialog must be 
        undocked from the Analysis page in the main application window. For more 
        information, see the graph.dock command. 
    
        Parameter(s)
        This property takes the following parameters.
        
        left 
        Specifies the distance from the left of the screen to the left of the 
        graph in pixels. 
        
        top 
        Specifies the distance from the top of the screen to the top of the 
        graph in pixels.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.graph.pos", left, top)
        p2e._app.Exec(arg_str)
    
    def get_size(self):
        """
        
        Returns the size of the Graphical Results dialog, being its width and 
        height in pixels. The values returned refer to the actual size of the 
        graph itself, and do not include the surrounding controls and borders. 
    
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        width 
        The width of the graph in pixels. 
        
        height 
        The height of the graph in pixels.
        
        """
        val = p2e._app.Request("get.graph.size")
        return p2e._util._convert_str_to_list(val, int, int)
    
    def set_size(self, width, height):
        """
        
        Sets the size of the Graphical Results dialog, being its width and 
        height in pixels. The size refers to the actual graph itself, and does 
        not include the surrounding controls and borders. 
    
        Parameter(s)
        This property takes the following parameters.
        
        width 
        Specifies the width of the graph in pixels. 
        
        height 
        Specifies the height of the graph in pixels.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.graph.size", width, 
                                                      height)
        p2e._app.Exec(arg_str)
    
    @apply
    def tab():
        def fget(self):
            """
            
            Retrieves the currently selected tab within the Analysis Page in the 
            main application window. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            index 
            A number from 0 to 5 indicating the index of the currently selected tab 
            of the 6 immediately below the Analysis graph, as shown in the following 
            Analysis Tabs table. 
            
            Relevant Data Table(s)
            
            Analysis Tabs 
            Value Tab 
            0 Thermal Analysis 
            1 Solar Exposure 
            2 Material Costs 
            3 Resource Consumption 
            4 Reverberation Times 
            5 Acoustic Response 
        
            """
            val = p2e._app.Request("get.graph.tab")
            return p2e._util._convert_str_to_type(val, int)
        
        def fset(self, index):
            """
            
            Sets the currently displayed analysis tab. 
        
            Parameter(s)
            This property takes the following parameters.
            
            index 
            A number from 0 to 5, corresponding to the 6 tabs immediately below the 
            Analysis graph, as shown in the following Analysis Tabs table. 
            
            Relevant Data Table(s)
            
            Analysis Tabs Value Tab 
            0 Thermal Analysis 
            1 Solar Exposure 
            2 Material Costs 
            3 Resource Consumption 
            4 Reverberation Times 
            5 Acoustic Response 
        
            """
            arg_str = p2e._util._convert_args_to_string("set.graph.tab", index)
            p2e._app.Exec(arg_str)
        
        return property(**locals())

