import py2ecotect
from py2ecotect import string_util

class View(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def axonometric(self, azi = 0.0):
        """
        
        Sets to a 3D axonometric view. 

        Parameter(s)
        This command takes the following parameters.
        
        [azi] 
        This optional parameter can be used to specify the azimuth angle in 
        degrees from which the model is viewed.
        
        """
        arg_str = string_util._convert_args_to_string("view.axonometric", azi)
        py2ecotect.conversation.Exec(arg_str)

    def copy(self, format = ""):
        """
        
        Copies the current model view to the clipboard in the Windows Bitmap 
        (.bmp) format. If the .wmf suffix is used, a the Windows Metafile 
        (.wfm) format is created instead. 

        Parameter(s)
        This command takes the following parameters.
        
        [format]
        Can be bmp or wmf. Default is blank.

        """
        if len(format) != 0:
            format = "." + format
        py2ecotect.conversation.Exec("view.copy" + format)

    def draw_arrow2d(self, offset, size = ""):
        """
        
        Draws a 2D arrow object from the origin point to the specified 2D screen 
        location in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        offset 
        A list of two values that represent the position on the screen in the 
        X and Y axis as an offset from the top-left corner in pixels of the 
        display canvas or control being used. 
        
        [size] 
        This optional parameter sets the size of the object in pixels.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.arrow2d", 
                                                      offset[0],
                                                      offset[1], 
                                                      size)
        py2ecotect.conversation.Exec(arg_str)

    def draw_arrowto(self, absolute_position, size = ""):
        """
        
        Draws a 3D arrow object from the origin point to the specified 3D world 
        position in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        [size] 
        This optional parameter sets the size of the object in the current 
        modelling units.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.arrowto", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2], size)
        py2ecotect.conversation.Exec(arg_str)

    def draw_cross(self, absolute_position):
        """
        
        Draws a 2D cross object at the specified 3D world position in the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space.  

        """
        arg_str = string_util._convert_args_to_string("view.draw.cross", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        py2ecotect.conversation.Exec(arg_str)

    def draw_line2d(self, offset):
        """
        
        Draws a 2D line object from the origin point to the specified 2D screen 
        location in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        offset 
        A list of two values that represent the position on the screen in the 
        X and Y axis as an offset from the top-left corner in pixels of the 
        display canvas or control being used.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.line2d", 
                                                      offset[0],
                                                      offset[1])
        py2ecotect.conversation.Exec(arg_str)

    def draw_lineto(self, absolute_position):
        """
        
        Draws a 3D line object from the origin point to the specified 3D world 
        position in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.lineto", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        py2ecotect.conversation.Exec(arg_str)

    def draw_move2d(self, offset):
        """
        
        Moves the 2D origin point to the specified 2D screen location in the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        offset 
        A list of two values that represent the position on the screen in the 
        X and Y axis as an offset from the top-left corner in pixels of the 
        display canvas or control being used.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.move2d", 
                                                      offset[0],
                                                      offset[1])
        py2ecotect.conversation.Exec(arg_str)

    def draw_moveto(self, absolute_position):
        """
        
        Moves the 3D origin point to the specified 3D world position within the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.moveto", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        py2ecotect.conversation.Exec(arg_str)

    def draw_pixel(self, absolute_position):
        """
        
        Draws a pixel at the specified 3D world position within the curent view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.pixel", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        py2ecotect.conversation.Exec(arg_str)

    def draw_point(self, absolute_position):
        """
        
        Draws a point at the specified 3D world position within the current 
        view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.point", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        py2ecotect.conversation.Exec(arg_str)

    def draw_sphere(self, absolute_position, radius):
        """
        
        Draws a 3D sphere object at the specified 3D world position in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space.
                
        radius 
        The radius of the sphere in the current modelling units.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.sphere", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2], 
                                                      radius)
        py2ecotect.conversation.Exec(arg_str)

    def draw_text(self, absolute_position, text):
        """
        
        Displays a string of text at the specified 3D world position inside the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        absolute_position
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        text 
        The text string to be displayed.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.text", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2], text)
        py2ecotect.conversation.Exec(arg_str)

    def draw_text2d(self, offset, string):
        """
        
        Displays a string of text at the specified 3D world position inside the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        offset 
        A list of two values that represent the position on the screen in the 
        X and Y axis as an offset from the top-left corner in pixels of the 
        display canvas or control being used. 
        
        string 
        The text string to be displayed.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.text2d", 
                                                      offset[0],
                                                      offset[1], 
                                                      string)
        py2ecotect.conversation.Exec(arg_str)

    def fit(self):
        """
        
        Zooms the current model view to fit entirely within the display canvas. 
        This does not change the current ground display grid. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("view.fit")
    
    def fit_grid(self):
        """
        
        Resizes the ground display grid to encompass all currently visible 
        elements within the model and fits the resulting model view within the 
        display canvas. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("view.fitgrid")

    def front(self):
        """
        
        Sets the current view type to Front. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("view.front")

    def maximise(self):
        """
        
        Maximises the main ECOTECT application window. 

        Parameter(s)
        This command takes the following parameters.
        
        [state] 
        This optional parameter determines whether the application is maximised 
        (true), or restored to its previous state (false). Defaulting to true 
        if now specified.
        
        """
        py2ecotect.conversation.Exec("view.maximise")

    def minimise(self):
        """
        
        Minimises the main ECOTECT application window. 

        Parameter(s)
        This command takes the following parameters.
        
        [state] 
        This optional parameter determines whether the application is minimised (true), or restored to its previous state (false). Defaulting to true if now specified.
        
        """
        py2ecotect.conversation.Exec("view.minimise")

    def mouse_event(self, action, position):
        """
        
        Simulates mouse events within the main model canvas. For more 
        information, see the app.mouseevent command. 

        Parameter(s)
        This command takes the following parameters.
        
        action 
        A token corresponding to the table below. 
        
        position
        A list of two values that represent the position at which to trigger 
        the mouse event on the XY-Axis in pixels.
        
        Relevant Data Table(s)
        
        Available Mouse Actions 
        Token Description 
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
        arg_str = string_util._convert_args_to_string("view.mouseevent", 
                                                      action, 
                                                      position[0], position[1])
        py2ecotect.conversation.Exec(arg_str)

    def move_in(self, shift = False):
        """
        
        Moves the perspective eye position 10 34653648nward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the move 
        instead. 
        
        """
        arg_str = string_util._convert_args_to_string("view.movein", shift)
        py2ecotect.conversation.Exec(arg_str)
        
    def move_out(self, shift = False):
        """
        
        Moves the perspective eye position 10204142720utward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the move 
        instead.
        
        """
        arg_str = string_util._convert_args_to_string("view.moveout", shift)
        py2ecotect.conversation.Exec(arg_str)

    def pan_down(self, shift = False):
        """
        
        Pans the current 2D and 3D view by 10 deg downward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the pan 
        instead.
        
        """
        arg_str = string_util._convert_args_to_string("view.pandown", shift)
        py2ecotect.conversation.Exec(arg_str)

    def pan_left(self, shift = False):
        """
        
        Pans the current 2D and 3D view by 10 deg to the left. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the pan 
        instead. 
        
        """
        arg_str = string_util._convert_args_to_string("view.panleft", shift)
        py2ecotect.conversation.Exec(arg_str)
        
    def pan_right(self, shift = False):
        """
        
        Pans the current 2D and 3D view by 10 deg to the right. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the pan 
        instead. 
        
        """
        arg_str = string_util._convert_args_to_string("view.panright", shift)
        py2ecotect.conversation.Exec(arg_str)

    def pan_up(self, shift = False):
        """
        
        Pans the current 2D and 3D view by 10 deg upward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the pan 
        instead. 
  
        """
        arg_str = string_util._convert_args_to_string("view.panup", shift)
        py2ecotect.conversation.Exec(arg_str)

    def perspective(self):
        """
        
        Sets the current view type to Perspective. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("view.perspective")

    def plan(self):
        """
        
        Sets the current view type to Plan. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("view.plan")

    def redraw(self):
        """
        
        Redraws the current model view, updating it with any previously made changes. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("view.redraw")

    def reset(self):
        """
        
        Resets the view to fit canvas. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("view.reset")

    def restore(self, index):
        """
        
        Restore a previously stored model view. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        An integer value between 1 and 5 specifying the index of the stored view. 
        
        """ 
        arg_str = string_util._convert_args_to_string("view.restore", index)
        py2ecotect.conversation.Exec(arg_str)

    def rotate_down(self, shift = False):
        """
        
        Rotates the current 3D view by 10 deg downward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the 
        rotation instead.
        
        """
        arg_str = string_util._convert_args_to_string("view.rotatedown", shift)
        py2ecotect.conversation.Exec(arg_str)

    def rotate_left(self, shift = False):
        """
        
        Rotates the current 3D view by 10 deg to the left. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the 
        rotation instead. 
        
        """
        arg_str = string_util._convert_args_to_string("view.rotateleft", shift)
        py2ecotect.conversation.Exec(arg_str)
        
    def rotate_right(self, shift = False):
        """
        
        Rotates the current 3D view by 10 deg to the right. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the 
        rotation instead.
        
        """
        arg_str = string_util._convert_args_to_string("view.rotateright", shift)
        py2ecotect.conversation.Exec(arg_str)
        
    def rotate_up(self, shift = False):
        """
        
        Rotates the current 3D view by 10 deg upward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the rotation instead.
        
        """
        arg_str = string_util._convert_args_to_string("view.rotateup", shift)
        py2ecotect.conversation.Exec(arg_str)

    def save(self, filename, format = ""):
        """
        
        Saves the current model view to the specified location. If no command 
        suffix is given, the default Windows Bitmap (.bmp) format is used, 
        otherwise the suffix is used to select between JPEG (.jpg) and Windows 
        Metafile (.wmf) formats. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path of the location where the file will be stored.
        
        format
        Optional parameter thats specifies file format. By default file will be 
        saved in .bmp
        
        """
        if len(format) != 0:
            format = "." + format
        arg_str = string_util._convert_args_to_string("view.save" + format, 
                                                      filename)
        py2ecotect.conversation.Exec(arg_str)

    def side(self):
        """
        
        Sets the current view type to Side. 

        Parameter(s)
        There are no parameters for this command.
        
        LUA Script Example(s)

        """
        py2ecotect.conversation.Exec("view.side")
        
    def store(self, index):
        """
        
        Stores the current model view to the specified index. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        An integer between 1 and 5 indication the index number to which the 
        view will be assigned. 

        """
        arg_str = string_util._convert_args_to_string("view.store", index)
        py2ecotect.conversation.Exec(arg_str)

    def zoom(self, factor):
        """
        
        Zoom the current model view by the specified factor. 

        Parameter(s)
        This command takes the following parameters.
        
        factor 
        A decimal value given as a multiplier.
        
        """
        arg_str = string_util._convert_args_to_string("view.store", factor)
        py2ecotect.conversation.Exec(arg_str)

    def zoom_in(self, shift = False):
        """
        
        Zooms the current 2D and 3D view by 10 deg inward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the zoom 
        instead. 
        
        """
        arg_str = string_util._convert_args_to_string("view.zoomin", shift)
        py2ecotect.conversation.Exec(arg_str)

    def zoom_out(self, shift = False):
        """
        
        Zooms the current 2D and 3D view by 10 deg outward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1% will be used for the zoom 
        instead. 
                
        """
        arg_str = string_util._convert_args_to_string("view.zoomout", shift)
        py2ecotect.conversation.Exec(arg_str)
        
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_align(self):
        """
        
        Retrieves the the alignment of output text by the view.draw.text. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        alignment 
        The alignment parameter is an integer value representing binary bits, as 
        shown in the Text Align table below. Horizontal and vertical alignments 
        are combined by adding the corresponding values. 
        
        Relevant Data Table(s)
        Text Alignment Codes 
        Value Description 
        0 LEFT and TOP 
        2 RIGHT 
        6 CENTER 
        8 BOTTOM 
        24 BASELINE 
        
        """
        val = py2ecotect.conversation.Request("get.view.align")
        return string_util._convert_str_to_type(val, int)

    def set_align(self, alignment):
        """
        
        This command allows you to set the alignment of any subsequent output 
        text by the view.draw.text. 

        Parameter(s)
        This property takes the following parameters.
        
        alignment 
        The alignment parameter is an integer value representing binary bits, 
        as shown in the Text Align table below. To combine horizontal and 
        vertical alignments, add the corresponding values together. 
        
        Relevant Data Table(s)
        
        Text Alignment Codes 
        Value Description 
        0 LEFT and TOP 
        2 RIGHT 
        6 CENTER 
        8 BOTTOM 
        24 BASELINE 

        """
        arg_str = string_util._convert_args_to_string("set.view.align", 
                                                      alignment)
        py2ecotect.conversation.Exec(arg_str)

    def get_font(self):
        """
        
        Retrieves the current font settings for subsequent output text in the 
        current model view (see the view.draw commands above). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        size 
        This is an integer value describing the size of the font in points. 
        
        name 
        The full name of the font type being used.
        
        """
        val = py2ecotect.conversation.Request("get.view.font")
        return string_util._convert_str_to_list(val, int, str)

    def set_font(self, size, name):
        """
        
        Sets the font settings for subsequent output text in the current model 
        view (see the view.draw commands above). 

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
        arg_str = string_util._convert_args_to_string("set.view.font", 
                                                      size, name)
        py2ecotect.conversation.Exec(arg_str)

    def get_grid_max(self):
        """
        
        Retrieves the maximum end position of the current display grid. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a maximum 
        point in 3 dimensional model space. 
        
        """
        val = py2ecotect.conversation.Request("get.view.grid.max")
        return string_util._convert_str_to_list(val, float, float, float)

    def set_grid_max(self, absolute_position):
        """
        
        This method/property is yet to be documented. 

        Parameter(s)
        This property takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a maximum point in 3 dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("set.view.grid.max", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        py2ecotect.conversation.Exec(arg_str)

    def get_grid_min(self):
        """
        
        Retrieves the minimum starting position of the current display grid. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a minimum 
        point in 3 dimensional model space. 

        """
        val = py2ecotect.conversation.Request("get.view.grid.min")
        return string_util._convert_str_to_list(val, float, float, float)

    def set_grid_min(self, absolute_position):
        """
        
        Sets the minimum starting position of the current display grid. 

        Parameter(s)
        This property takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a minimum point in 3 dimensional model space. 
        
        """
        arg_str = string_util._convert_args_to_string("set.view.grid.min", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        py2ecotect.conversation.Exec(arg_str)

    def get_pen(self):
        """
        
        Retrieves the current pen color and size. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        color 
        The color as a RGB hexidecimal number, given in the form 0xFF8800. 
        
        width 
        The thickness of the pen line in pixels. 
        
        """
        val = py2ecotect.conversation.Request("get.view.pen")
        return string_util._convert_str_to_list(val, str, float)

    def set_pen(self, color, width = 0, alpha = 0.0):
        """
        
        Sets the current pen color, size and opacity. 

        Parameter(s)
        This property takes the following parameters.
        
        color 
        The color as a RGB hexidecimal number, given as a string in the form of 
        "0xFF8800" or "FF8800". 
        
        [width] 
        This optional parameter specifies the thickness of the pen line in 
        pixels. 
        
        [alpha] 
        This optional parameter is a decimal value between 0 (transparent) and 
        1(opaque). 
        
        """
        arg_str = string_util._convert_args_to_string("set.view.pen", color, 
                                                      width, alpha)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_point(self, absolute_position):
        """
        
        Returns the 2D screen position of the specified 3D point within the 
        current view. 

        Parameter(s)
        This property takes the following parameters.
        
        absolute_position 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y 
        Represents a position on the screen in the X and Y axis as an offset 
        from the top-left corner in pixels. 
        
        """
        arg_str = string_util._convert_args_to_string("get.view.point", 
                                                      absolute_position[0],
                                                      absolute_position[1],
                                                      absolute_position[2])
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float)

    def get_size(self):
        """
        
        Retrieves the current view dimensions in pixels. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        width 
        The width of the view canvas. 
        
        height 
        The height of the view canvas.
        
        """
        val = py2ecotect.conversation.Request("get.view.size")
        return string_util._convert_str_to_list(val, float, float)
        
    def set_size(self, width, height):
        """
        
        Sets the current view dimensions in pixels. 

        Parameter(s)
        This property takes the following parameters.
        
        width 
        The new width of the view canvas. 
        
        height 
        The new height of the view canvas.
        
        """
        arg_str = string_util._convert_args_to_string("set.view.size", width, 
                                                      height)
        py2ecotect.conversation.Exec(arg_str)

    def get_visible(self):
        """
        
        Returns whether or not the 3D EDITOR view is currently displayed or not. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        visible 
        This is a boolean value where 1 means true and 0 means false.
        
        """
        val = py2ecotect.conversation.Request("get.view.visible")
        return string_util._convert_str_to_type(val, int)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    align = property(fget = get_align, fset = set_align, 
                        doc = "The alignment of output text by the view.draw."
                        "text")



        

if __name__ == "__main__":
    x = View()
    
    #x.copy()
    x.draw_arrow2d(100, 250)
    #x.draw_arrowto(50, 100, 100)
    #x.draw_cross(2300.0, 5400.0, 2400.0)
    #x.draw_text(2300, 5400, 2400, "TEST")
    #x.save("C:\\Test\\myview.wmf", "wmf")
    #print x.get_align()
    #x.set_align(6)
    #print x.get_font()
    #x.set_font(12, "Arial")
    #print x.get_grid_max()
    #print x.get_pen()
    #x.set_pen("FF8800", 10, 0.9)
    #print x.get_point(100, 50, 100)
    #print x.align
    #x.align = 24
    
    

    print "Tests completed"