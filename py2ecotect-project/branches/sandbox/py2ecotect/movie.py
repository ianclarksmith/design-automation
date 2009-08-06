import py2ecotect as p2e

class Movie(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def add_frame(self):
        """
        
        Call this command to add a new frame to the movie. You can call this 
        command anytime whilst you are recording, regardless of the current 
        capture settings. Calls to this command when not recording are ignored. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        p2e._app.Exec("movie.addframe")

    def finish(self):
        """
        
        This command MUST be called in order to finish recording the current 
        movie. If you do not, recording will continue until you manually click 
        the Finish button in the Create Animation dialog. 

        Parameter(s)
        There are no parameters for this command.
 
        """
        p2e._app.Exec("movie.finish")

    def play(self, filename):
        """
        
        Call this command to play a movie in Windows Media Player, or to view 
        an image. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The path and filename of the movie to play, and updates the value of 
        the filename edit field. If this parameter is not given, the current 
        filename in the Create Animation dialog is used.
        
        Be aware of the issues with backslashes in filename parameters as described here. 

        """
        arg_str = p2e._util._convert_args_to_string("movie.play", filename)
        p2e._app.Exec(arg_str)

    def record(self, filename):
        """
        
        Use this command to begin recording a movie. 

        Parameter(s)
        This command takes the following parameters.
        
        filename 
        The path and filename to use for saving the recorded movie. If this 
        parameter is not given, the current filename in the Create Animation 
        dialog is used. Note: There are many parameters of the movie that 
        cannot be changed whilst actually recording. Thus, these parameters are 
        only read and applied when this command is called.
        
        Be aware of the issues with backslashes in filename parameters as described here.

        """
        arg_str = p2e._util._convert_args_to_string("movie.record", filename)
        p2e._app.Exec(arg_str)

    def show(self, state = True):
        """
        
        Use this command to show or hide the movie dialog box. This command is 
        useful if you need to hide it so as not to obstruct part of the main 
        window during an animation. 

        Parameter(s)
        This command takes the following parameters.
        
        [state] 
        Set this parameter to true to display the movie dialog box and false to 
        hide it.
        
        """
        arg_str = p2e._util._convert_args_to_string("movie.show", state)
        p2e._app.Exec(arg_str)
        
    #===========================================================================
    # Properties
    #===========================================================================
    
    @apply
    def aero_3d():
        def fget(self):
            """
            
            Determines whether the Windows Vista Aero theme is using 3D desktop 
            composition. Desktop composition within the Aero theme uses the 3D 
            graphics buffer to generate blurred transparency and 3D overlay effects. 
            With Aero enabled, ECOTECT must completely re-render the OpenGL image 
            each time a new screenshot or animation frame is required. Use this 
            property to determine if Aero is currently running in Vista. If you do 
            not use Aero or Vista, the result will always be false. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            state 
            This is a boolean value where 1 or true represents the affirmative and 
            0 or false is negative.
            
            """
            val = p2e._app.Request("get.movie.aero3d")
            return p2e._util._convert_str_to_type(val, int)

        def fset(self, state):
            """
            
            Enable or disable 3D desktop composition in the Windows Vista Aero 
            theme. Desktop composition within the Aero theme uses the 3D graphics 
            buffer to generate blurred transparency and 3D overlay effects. With 
            Aero enabled, ECOTECT must completely re-render the OpenGL image each 
            time a new screenshot or animation frame is required. Temporarily 
            disabling Aero will not affect your computer in any way other than 
            stopping it displaying transparent window frames and 3D application 
            images. If you do not use Aero or Vista, setting this property will 
            have no effect. 
    
            Parameter(s)
            This property takes the following parameters.
            
            state 
            This is a boolean value where 1 or true represents the affirmative and 
            0 or false is negative.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.movie.aero3d", 
                                                         state)
            p2e._app.Exec(arg_str)
            
        return property(**locals())
    
    @apply
    def capture():    
        def fget(self):
            """
            
            Retrieves the current capture settings by which frames are added to the 
            animation, as shown in the table below. Note that you can change methods 
            any time during the recording of an animation. For example, you could 
            choose to manually add the first few frames, then switch to each redraw 
            while you run a shadow or ray animation, and then switch to the timer 
            option as you move around the results. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            type 
            An integer value from the Movie Capture Options table below, 
            representing capture settings used during recording. 
            
            Relevant Data Table(s)
            
            Movie Capture Options 
            Token Value Description 
            manual 0 Manually 
            redraw 1 On Each Redraw  
            timer 2 On Timer  
    
            """
            val = p2e._app.Request("get.movie.capture")
            return p2e._util._convert_str_to_type(val, int)

        def fset(self, type):
            """
            
            Sets the current capture settings by which frames are added to the 
            animation recording. 
    
            Parameter(s)
            This property takes the following parameters.
            
            type 
            The capture settings to use during recording, as outlined in the Movie 
            Capture Options table below. 
            
            Relevant Data Table(s)
            
            Movie Capture Options 
            Token Value Description 
            manual 0 Manually 
            redraw 1 On Each Redraw  
            timer 2 On Timer  
    
            """
            arg_str = p2e._util._convert_args_to_string("set.movie.capture", 
                                                         type)
            p2e._app.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def filename():     
        def fget(self):
            """
            
            Retrieves the current pathname of the file to which the movie will be 
            recorded. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            filename 
            A text string containing the filename and directory where animations are 
            currently recorded.
            
            """
            val = p2e._app.Request("get.movie.filename")
            return p2e._util._convert_str_to_type(val, str)
    
        def fset(self, filename):
            """
            
            Retrieves the current pathname of the file to which the movie will be 
            recorded. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            filename 
            A text string containing the filename and directory where animations are 
            currently recorded.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.movie.filename", 
                                                         filename)
            p2e._app.Exec(arg_str)
        
        return property(**locals())

    @apply
    def frame_rate():     
        def fget(self):
            """
            
            Retrieves the current movie playback speed, measured in frames per 
            second. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            fps 
            The number of frames per second. 
    
            """
            val = p2e._app.Request("get.movie.framerate")
            return p2e._util._convert_str_to_type(val, str)
        
        def fset(self, parameter):
            """
            
            Sets the number of frames that are recorded per second for the current 
            animation. 
    
            Parameter(s)
            This property takes the following parameters.
            
            parameter 
            Specifies the number of frames per second to use. Note that the greater 
            the number of frames per second, the larger the file size will be for 
            the recorded animation.
            
            """
            arg_str = p2e._util._convert_args_to_string("set.movie.framerate", 
                                                         parameter)
            p2e._app.Exec(arg_str)
        
        return property(**locals())    
    
    def get_size(self):
        """
        
        Retrieves the size of the screen currently being used to record the 
        animation. When retrieving this property, an additional resize parameter 
        is returned before the width and height. This parameter is 1 when the 
        Specific Size: option is selected, and 0 when the Same as Source option 
        is selected, under the Create New Animation dialog box. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        resize 
        A boolean value that indicates whether the movie resizes to fit the 
        current window size. It is 1 when the Specific Size: option is selected, 
        and 0 when the Same as Source option is selected, under the Create New 
        Animation dialog box. 
        
        width 
        The width used for the animation recording, given in pixels. 
        
        height 
        The height used for the animation recording, given in pixels.
        
        """
        val = p2e._app.Request("get.movie.size")
        return p2e._util._convert_str_to_list(val, int, float, float)

    def set_size(self, width, height):
        """
        
        Sets the size of the ECOTECT application window to use for the animation 
        recording. If the movie.source property is set to Main Window, the width 
        and height parameters refer to the overall dimensions of the main 
        application window. Otherwise, the main window is adjusted so that only 
        the drawing canvas is set to the specified size.

        Note that the ECOTECT application window does not adjust until the 
        movie.record command is called. If you wish to resize the application 
        window without creating an animation recording, this can be achieved 
        using the set.view.size, set.opengl.size, set.graph.size or 
        set.app.window commands. 
        
        Parameter(s)
        This property takes the following parameters.
        
        width 
        Sets the width to use for the animation recording, measured in pixels. 
        height 
        Sets the height to use for the animation recording, measured in pixels.
        
        """
        arg_str = p2e._util._convert_args_to_string("set.movie.size", 
                                                     width, height)
        p2e._app.Exec(arg_str)  
    
    @apply
    def source():   
        def fget(self):
            """
            
            Controls what appears inside the animation or each frame of the 
            recording. The possible values returned are shown in the Movie Source 
            Options table below. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            src 
            The source used for the animation or frame recording, as outlined in 
            the Movie Source Options table below. 
            
            Relevant Data Table(s)
            
            Movie Source Options 
            Token Value Description 
            canvas 0 Canvas Only 
            window 1 Main Window  
            
            """
            val = p2e._app.Request("get.movie.source")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, src):
            """
            
            The movie.source property controls what appears inside the animation or 
            each frame of the recording. 
    
            Parameter(s)
            This property takes the following parameters.
            
            src 
            Specifies the source to use for the animation or frame recording, as 
            outlined in the Movie Source Options table below.
            
            When set to Canvas Only, only the drawing areas in the 3D Editor, 
            Visualise and Analysis pages are captured.
            
            When set to Main Window, the entire ECOTECT application window is 
            recorded in the animation, including the title bar, toolbars, panels 
            and pages - this also includes the Sun-Path Diagram dialog box. If you 
            are using the timer capture recording option, this also includes dialog 
            boxes, as long as they are entirely within the boundaries of the main 
            application window.
            
            While it is possible to switch between the 3D Editor and the Visualise 
            pages during a recording, due to some limitations it is not possible to 
            swap between the Analysis page and the 3D Editor or Visualise pages. 
            This will cause an exception error in msvidc32.dll (this is not serious, 
            you should be able to continue the movie but without those frames). 
            
            Relevant Data Table(s)
            
            Movie Source Options 
            Token Value Description 
            canvas 0 Canvas Only 
            window 1 Main Window  
       
            """
            arg_str = p2e._util._convert_args_to_string("set.movie.source", src)
            p2e._app.Exec(arg_str)
        
        return property(**locals())    
    
    @apply
    def type(): 
        def fget(self):
            """
            
            Returns the file format used to output the animation recording, as 
            shown in the Movie Types table below.
    
            When set to 0 (avi), the result is a single movie file. When set to 1 
            (bmp) or 2 (jpg), the result is a series of image files for each frame 
            of the animation. The filename specified in the movie.record command is 
            used as the base for each frame, with the frame number appended to it. 
            The filename displayed in the Create New Animation dialog box will also 
            be updated as the frame number increments. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            type 
            The file format used for the animation recording output, as outlined in 
            the following Movie Types table. 
            
            Relevant Data Table(s)
            
            Available Movie Types 
            Token Value Description 
            avi 0 AVI Movie  
            bmp 1 Bitmap Files  
            jpg 2 JPEG Files 
    
            """
            val = p2e._app.Request("get.movie.source")
            return p2e._util._convert_str_to_type(val, int)
    
        def fset(self, type):
            """
            
            Sets the file format used to output the animation recording. 
    
            Parameter(s)
            This property takes the following parameters.
            
            type 
            Specifies the file format to use for the animation recording output, as 
            outlined in the following table:
            
            When set to avi, the result is a single movie file. When set to bmp or 
            jpg, the result is a series of image files for each frame of the 
            animation. The filename specified in the movie.record command is used as 
            the base for each frame, with the frame number appended to it. The 
            filename displayed in the Create New Animation dialog box will also be 
            updated as the frame number increments. 
            
            Relevant Data Table(s)
            
            Available Movie Types 
            Token Value Description 
            avi 0 AVI Movie  
            bmp 1 Bitmap Files  
            jpg 2 JPEG Files 
    
            """
            arg_str = p2e._util._convert_args_to_string("set.movie.type", type)
            p2e._app.Exec(arg_str)
            
        return property(**locals())    
