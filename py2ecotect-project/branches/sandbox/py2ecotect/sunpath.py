import py2ecotect as p2e

class Sunpath(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def copy(self):
        """
        
        Copies the sunpath view to the clipboard in the default, Windows Bitmap 
        (.bmp), format. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("sunpath.copy")
        
    def copy_bmp(self):
        """
        
        Copies the sunpath view to the clipboard in the Windows Bitmap (.bmp) format. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("sunpath.copy.bmp")
        
    def copy_wmf(self):
        """
        
        Copies the sunpath view to the clipboard in the Windows Metafile (.wmf) format. 

        Parameter(s)
        There are no parameters for this command.
   
        """
        p2e.conversation.Exec("sunpath.copy.wmf")

    def mouse_event(self):
        """
        
        Simulate mouse events within the sunpath canvas. For more information, 
        see the app.mouseevent command. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("sunpath.mouseevent")
        
    def pan_down(self, shift = False):
        """
        
        Pans the current rendered view by 10 deg upward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1 deg will be used for the pan 
        instead.
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.pandown", shift)
        p2e.conversation.Exec(arg_str)
        
    def pan_left(self, shift = False):
        """
        
        Pans the current rendered view by 10 deg to the left. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1 deg will be used for the pan 
        instead.
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.panleft", shift)
        p2e.conversation.Exec(arg_str)

    def pan_right(self, shift = False):
        """
        
        Pans the current rendered view by 10 deg to the right. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1 deg will be used for the pan 
        instead.
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.panright", shift)
        p2e.conversation.Exec(arg_str)
        
    def pan_up(self, shift = False):
        """
        
        Pans the current rendered view by 10 deg upward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1 deg will be used for the 
        pan instead.
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.panup", shift)
        p2e.conversation.Exec(arg_str)

    def redraw(self):
        """
        
        Redraws the current sunpath view, updating it with any previously made changes. 

        Parameter(s)
        There are no parameters for this command.

        """
        p2e.conversation.Exec("sunpath.redraw")

    def save(self, filename):
        """
        
        Saves the current sunpath view to the specified location in the default, 
        Windows Bitmap (.bmp), format. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to the location where the file will be stored.
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.save", filename)
        p2e.conversation.Exec(arg_str)

    def save_bmp(self, filename):
        """
        
        Saves the current sunpath view to the specified location in the Windows 
        Bitmap (.bmp) format. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to the location where the file will be stored.
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.save.bmp", 
                                                      filename)
        p2e.conversation.Exec(arg_str)

    def save_htb2(self, filename):
        """
        
        Saves the current sunpath shading percentage data to the specified 
        location as a HTB2 shading mask. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to the location where the file will be stored.
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.save.htb2", 
                                                      filename)
        p2e.conversation.Exec(arg_str)
        
    def save_shading(self, filename):
        """
        
        Saves the current sunpath shading percentage data to the specified 
        location as a text file. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to the location where the file will be stored. 

        """
        arg_str = p2e._util._convert_args_to_string("sunpath.save.shading", 
                                                      filename)
        p2e.conversation.Exec(arg_str)

    def save_wmf(self, filename):
        """
        
        Saves the current sunpath view to the specified location in the Windows 
        Metafile (.wmf) format. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The full path to the location where the file will be stored. 
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.save.wmf", 
                                                      filename)
        p2e.conversation.Exec(arg_str)

    def show(self):
        """
        
        Displays the sun-path window and brings it to the front if it is behind 
        any other windows. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        p2e.conversation.Exec("sunpath.show")
        
    def zoomin(self, shift = False):
        """
        
        Zooms the currently rendered view by 10 deg inward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1 deg will be used for the 
        zoom instead. 
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.zoomin", 
                                                      shift)
        p2e.conversation.Exec(arg_str)
        
    def zoomout(self, shift = False):
        """
        
        Zooms the currently rendered view by 10 deg outward. 

        Parameter(s)
        This command takes the following parameters.
        
        [shift] 
        If this optional parameter is set to true, 1 deg will be used for the 
        zoom instead. 
        
        """
        arg_str = p2e._util._convert_args_to_string("sunpath.zoomout", 
                                                      shift)
        p2e.conversation.Exec(arg_str)

    #===========================================================================
    # Properties
    #===========================================================================
    
    @apply
    def display():
        def fget(self):
            """
            
            Retrieves the current display and data overlay settings. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            display 
            An integer taken from the following Sunpath Display Types table. 
            
            overlay 
            An integer taken from the following Sunpath Data Overlay Types table.
            
            """
            val = p2e.conversation.Request("get.sunpath.display")
            return p2e._util._convert_str_to_list(val, int, int)
        
        return property(**locals())
    
    @apply
    def focus():
        def fget(self):
            """
            
            Retrieves the position of the current SunPath focus point. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            x, y, z 
            Represents the absolute position in the X, Y and Z axis of the focus 
            point in 3 dimensional model space.
            
            """
            val = p2e.conversation.Request("get.sunpath.focus")
            return p2e._util._convert_str_to_list(val, float, float, float)
        
        return property(**locals())

    def get_point(self, point):
        """
        
        Translates a point within the Sun-Path diagram into an absolute screen 
        position. 

        Parameter(s)
        This property takes the following parameters.
        
        point 
        A list of two values that represent the X and Y axis position of the 
        point in the Sun-Path diagram. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y 
        The X and Y axis position of the point in absolute screen coordinates.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.sunpath.point", 
                                                      point[0],
                                                      point[1])
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float, float)
        
    def get_pos(self):
        """
        
        Retrieves the current position of the Sunpath dialog box in your local 
        screen coordinates. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        left 
        The offset of the dialog box from the left of the screen in pixels 
        
        top 
        The offset of the dialog box from the top of the screen in pixels 

        """
        val = p2e.conversation.Request("get.sunpath.pos")
        return p2e._util._convert_str_to_list(val, int, int)
    
    def set_pos(self, left, top):
        """
        
        Sets the current position of the Sunpath dialog box in your local 
        screen coordinates. 

        Parameter(s)
        This property takes the following parameters.
        
        left 
        The offset of the dialog box from the left of the screen in pixels 
        
        top 
        The offset of the dialog box from the top of the screen in pixels
        
        """
        arg_str = p2e._util._convert_args_to_string("set.sunpath.pos", left, 
                                                      top)
        p2e.conversation.Exec(arg_str)

    def get_size(self):
        """
        
        Retrieve the size of the Sunpath dialog box. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        width 
        The width in pixels. 
        
        height 
        The height in pixels.
        
        """
        val = p2e.conversation.Request("get.sunpath.size")
        return p2e._util._convert_str_to_list(val, int, int)

    def set_size(self, width, height):
        """
        
        Resizes the Sunpath dialog box to the specified size. 

        Parameter(s)
        This property takes the following parameters.
        
        width 
        The new width in pixels. 
        
        height 
        The new height in pixels. 
        
        """
        arg_str = p2e._util._convert_args_to_string("set.sunpath.size", width, 
                                                      height)
        p2e.conversation.Exec(arg_str)
    
    @apply
    def visible():    
        def fget(self):
            """
            
            Displays or hides the SunPath Diagram dialog box. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            shown 
            This is a boolean value where 1 or true means show the dialog and 0 or 
            false means hide it. 
    
            """
            val = p2e.conversation.Request("get.sunpath.visible")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())
    

if __name__ == "__main__":
    x = Sunpath()
    
    #print x.get_display()
    #print x.get_focus()
    #print x.get_pos()
    #print x.get_size()
    #print x.visible
    

    print "Tests completed"
 