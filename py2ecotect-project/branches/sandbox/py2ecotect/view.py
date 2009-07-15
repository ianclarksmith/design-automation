import py2ecotect
from py2ecotect import string_util

class View(object):
    
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
        There are no parameters for this command.

        """
        if len(format) != 0:
            format = "." + format
        py2ecotect.conversation.Exec("view.copy" + format)

    def draw_arrow2d(self, x, y, size = 0):
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
        arg_str = string_util._convert_args_to_string("view.draw.arrow2d", x, y, 
                                                      size)
        py2ecotect.conversation.Exec(arg_str)

    def draw_arrowto(self, x, y, z, size = 0):
        """
        
        Draws a 3D arrow object from the origin point to the specified 3D world 
        position in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 
        
        [size] 
        This optional parameter sets the size of the object in the current 
        modelling units.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.arrowto", x, y, 
                                                      z, size)
        py2ecotect.conversation.Exec(arg_str)

    def draw_cross(self, x, y, z):
        """
        
        Draws a 2D cross object at the specified 3D world position in the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 

        """
        arg_str = string_util._convert_args_to_string("view.draw.cross", x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def draw_line2d(self, x, y):
        """
        
        Draws a 2D line object from the origin point to the specified 2D screen 
        location in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y 
        Represents a position on the screen in the X and Y axis as an offset 
        from the top-left corner in pixels of the display canvas or control 
        being used.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.line2d", x, y)
        py2ecotect.conversation.Exec(arg_str)

    def draw_lineto(self, x, y, z):
        """
        
        Draws a 3D line object from the origin point to the specified 3D world 
        position in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.lineto", x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def draw_move2d(self, x, y):
        """
        
        Moves the 2D origin point to the specified 2D screen location in the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y 
        Represents a position on the screen in the X and Y axis as an offset 
        from the top-left corner in pixels of the display canvas or control 
        being used.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.move2d", x, y)
        py2ecotect.conversation.Exec(arg_str)

    def draw_moveto(self, x, y, z):
        """
        
        Moves the 3D origin point to the specified 3D world position within the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.moveto", x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def draw_pixel(self, x, y, z):
        """
        
        Draws a pixel at the specified 3D world position within the curent view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.pixel", x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def draw_point(self, x, y ,z):
        """
        
        Draws a point at the specified 3D world position within the current 
        view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.point", x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def draw_sphere(self, x, y, z, radius):
        """
        
        Draws a 3D sphere object at the specified 3D world position in the current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 dimensional model space. 
        radius 
        The radius of the sphere in the current modelling units.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.sphere", x, y, 
                                                      z, sphere)
        py2ecotect.conversation.Exec(arg_str)

    def draw_text(self, x, y, z, text):
        """
        
        Displays a string of text at the specified 3D world position inside the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 
        
        text 
        The text string to be displayed.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.text", x, y, 
                                                      z, text)
        py2ecotect.conversation.Exec(arg_str)

    def draw_text2d(selfx, y, string):
        """
        
        Displays a string of text at the specified 3D world position inside the 
        current view. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y 
        Represents a position on the screen in the X and Y axis as an offset 
        from the top-left corner in pixels of the display canvas or control 
        being used. 
        
        string 
        The text string to be displayed.
        
        """
        arg_str = string_util._convert_args_to_string("view.draw.text2d", x, y, 
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

    def mouse_event(self, action, x, y):
        """
        
        Simulates mouse events within the main model canvas. For more 
        information, see the app.mouseevent command. 

        Parameter(s)
        This command takes the following parameters.
        
        action 
        A token corresponding to the table below. 
        
        x 
        The position at which to trigger the mouse event on the X-Axis in pixels. 
        
        y 
        The position at which to trigger the mouse event on the Y-Axis in pixels. 
        
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
                                                      action, x, y)
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
        arg_str = string_util._convert_args_to_string("view.copy" + format, 
                                                      filename)
        py2ecotect.conversation.Exec(arg_str)






if __name__ == "__main__":
    x = View()
    
    #x.copy()
    #x.draw_arrow2d(100, 250)
    #x.draw_arrowto(50, 100, 100)
    #x.draw_cross(2300.0, 5400.0, 2400.0)
    x.save("C:\Test\mymodel.bmp")
    
    

    print "Tests completed"