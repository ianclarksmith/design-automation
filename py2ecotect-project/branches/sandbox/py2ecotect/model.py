import py2ecotect as p2e

_zones = []
_objects = []
_nodes = []

def _populate():
    val = p2e.conversation.Request("get.model.zones")
    num_zones = p2e._util._convert_str_to_type(val, int)    
    for eco_id in range(num_zones):
            p2e.Zone(eco_id)

class Model(object):         

    #===========================================================================
    # Commands
    #===========================================================================
        
    def dump(self, filename):
        """
        
        Use the dump command to save a snapshot copy of the current model to the 
        specified filename and location, without changing the stored filename or 
        marking the model as having been recently saved. This command can be 
        useful when performing a large number of parametric calculations and 
        wish to generate several interim results files without all the 
        information usually associated with a model.saveas command. As a 
        comparison, the model.saveas command saves the model with the new 
        filename, copies its adjacency and shading table files, then updates the 
        stored model filename and the main window caption. 
    
        Parameter(s)
    
        filename 
        Specifies the filename to use for the dump; however, be aware of the 
        issues with backslashes in filename parameters. It is generally good 
        practice to specify a directory location in addition to the filename, or 
        the export file will be saved to current model directory by default. 
        
        Here is an example:
        
        >>> dump("C:\\Test\\mytest.eco")
        
        """
        arg_str = p2e._util._convert_args_to_string("model.dump", filename)
        p2e.conversation.Exec(arg_str)
    
    def export_file(self, filename, fileformat):
        """
        
        Use this command to export the current model data to the a file. A 
        suffix component can be used to specify the file format, as given in the 
        following table. By default, the file(s) will be saved to the disk. 
        However, for some of the formats marked with [run.], if you insert the 
        prefix run. in front of the file type token, ECOTECT will automatically 
        invoke the last action for the export and actually run the associated 
        application to process the exported file. For example, the examples 
        given below show exports to Radiance. With the model.export.run.rad 
        command, Radiance will be involked to actually generate the images 
        defined within the exported Radiance file. 
           
        Parameter(s)
    
        filename 
        Specifies the filename to use for the export. However, be aware of the 
        issues with backslashes in filename parameters. It is generally good 
        practice to specify a directory location in addition to the filename, 
        or the export file will be saved to current model directory by default.
        
        Extension Read Write Format 
        mod yes yes ASCII Model File 
        rad yes yes RADIANCE Scene File 
        oct no yes RADIANCE Octree 
        pov no yes POV-Ray Scene File 
        wrl yes yes VRML 2.0 FIle 
        dxf yes yes AutoCAD DXF File 
        htb no yes HTB2 Model File 
        nat no yes NatHERS Model File 
        esp no yes ESP-r Model File 
        ray yes yes Binary Acoustic Rays File 
        grd yes yes Binary Analysis Grid File 
        cfd no yes NIST FDS CFD Model File 
        air no yes WinAir 4 CFD Model File 
        wmf no yes Windows Metafile Image File 
        bmp yes yes Windows Bitmap Image File 
        jpg yes yes JPEG Image File 
        gif yes yes GIF Image File 
        scr yes no ECOTECT Script File 
        csv yes yes Comma Separated Value (CSV) File 
        asc yes yes ASCII Text File 
        dat yes yes RADIANCE Point Data File 
        chm no no Microsoft Compiled Help File 
        msk yes yes Shanding Mask File 
        idf yes yes EnergyPlus Input File 
        eio yes no EnergyPlus Summary File 
        eso yes no EnergyPlus Binary Output 
        txt yes yes ASCII Text File 
        
        Here is an example:
        
        >>> export_file("D:\\Temp\\mytest.dxf", ".dxf")
        
        """
        #TODO: add error checking
        arg_str = p2e._util._convert_args_to_string("model.export" + fileformat, filename)
        p2e.conversation.Exec(arg_str)
    
    def import_file(self, filename):
        """
        
        Use this command to import data in into the current model. A suffix 
        component can be used to specify the the file format from the following 
        table.
        
        The Ecotect version of this command is:
        model.import
    
        Parameter(s)
    
        filename 
        Specifies the filename to use for the import. However, be aware of the 
        issues with backslashes in filename parameters. It is generally good 
        practice to specify a directory location in addition to the filename, or 
        the import file will be saved to current model directory by default.
        
        Extension Read Write Format 
        mod yes yes ASCII Model File 
        rad yes yes RADIANCE Scene File 
        oct no yes RADIANCE Octree 
        pov no yes POV-Ray Scene File 
        wrl yes yes VRML 2.0 FIle 
        dxf yes yes AutoCAD DXF File 
        htb no yes HTB2 Model File 
        nat no yes NatHERS Model File 
        esp no yes ESP-r Model File 
        ray yes yes Binary Acoustic Rays File 
        grd yes yes Binary Analysis Grid File 
        cfd no yes NIST FDS CFD Model File 
        air no yes WinAir 4 CFD Model File 
        wmf no yes Windows Metafile Image File 
        bmp yes yes Windows Bitmap Image File 
        jpg yes yes JPEG Image File 
        gif yes yes GIF Image File 
        scr yes no ECOTECT Script File 
        csv yes yes Comma Separated Value (CSV) File 
        asc yes yes ASCII Text File 
        dat yes yes RADIANCE Point Data File 
        chm no no Microsoft Compiled Help File 
        msk yes yes Shanding Mask File 
        idf yes yes EnergyPlus Input File 
        eio yes no EnergyPlus Summary File 
        eso yes no EnergyPlus Binary Output 
        txt yes yes ASCII Text File 
        
        """
        arg_str = p2e._util._convert_args_to_string("model.import", filename)
        p2e.conversation.Exec(arg_str)
    
    def load(self, filename):
        """
        
        Loads the specified file as the current model. 
    
        Parameter(s)
    
        filename 
        Specifies the name of the ECOTECT file to load. In most cases you will 
        need to specify the full pathname of the file to be loaded, as the 
        directory in which the model file resides will become the current
        directory in which the application will work. An example may be:
    
        filename =  C:\Temp\Test.eco
        
        """
        arg_str = p2e.p2e._util._convert_args_to_string("model.load", filename)
        p2e.conversation.Exec(arg_str)
        
        #Clear model lists
        self.zones = []
        self.objects = []
        self.nodes = []
        
        #Update the lists
        self._populate_zones() 
        self._populate_objects()
        self._populate_nodes()
    
    def load_new(self):
        """   
        
        Clears the current model from memory and resets the material library. 
        Note: when used as part of a script, this command will not prompt you to 
        save any changes you have made to the current model. Once called, all 
        changes will be lost. 
    
        Parameter(s)
        There are no parameters for this command.
        
        Command in ECOTECT:
        model.new
        
        """
        #p2e.conversation.Exec("model.new")
        
        #Clear model lists
        #self.zones = []
        #self.objects = []
        #self.nodes = []
         
    
    def revert(self):
        """
        
        Use this command to revert to the last saved version of the current 
        model file. This can be useful where you have been running a long script 
        unattended that has made many changes to the model and do not want them 
        saved. Simply add a model.revert command at the end of the script and it 
        will reload the original. 
    
        Parameter(s)
        There are no parameters for this command.
        
        """
        p2e.conversation.Exec("model.revert")
    
    def save(self):
        """
        
        This command simply saves the current model to disk. If the model does 
        not already have a filename, the command will fail. 
    
        Parameter(s)
        There are no parameters for this command.
        
        """
        p2e.conversation.Exec("model.save")
    
    def save_as(self, filename):
        """
        
        When invoked, the model.saveas command saves the model with the new 
        filename, copies its adjacency and shading table files, then updates the 
        stored model filename and the main window caption. As a comparison, the 
        model.dump command only saves a snapshot copy of the current model to 
        the specified file, without changing the stored filename or marking the 
        model as having been recently saved. 
    
        Parameter(s)
        This command takes the following parameters.
        
        """
        arg_str = p2e._util._convert_args_to_string("model.saveas", filename)        
        p2e.conversation.Exec(arg_str)
        
    def update(self):
        """
        
        Use the update command to check and refresh inter-object relationships 
        within the model. Complex model with many inter-relationships can take 
        a little time to regenerate so ECOTECT doesn't do this automatically 
        after each script-based manipulation. You can also use object.update to 
        do this specific objects in the model. 
        
        Parameter(s)
        There are no parameters for this command.
        
        """
        p2e.conversation.Exec("model.update")
        
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_altitude(self, absolute_position_start, absolute_position_end):
        """
        
        Retrieves geometric information from the current ECOTECT model, 
        specifically the vertical angular distance of a line starting at 
        (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
        returned is given in degrees. 
    
        Parameter(s)
        This property takes the following parameters.
    
        absolute_position_start 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a starting point in 3 dimensional model space.
         
        absolute_position_end 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of an end point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
    
        alt 
        The altitude angle in degrees. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.model.altitude", 
                                                          absolute_position_start[0],
                                                          absolute_position_start[1], 
                                                          absolute_position_start[2],
                                                          absolute_position_end[0],
                                                          absolute_position_end[1],
                                                          absolute_position_end[2])
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)        
        
    def get_azimuth(self, absolute_position_start, absolute_position_end):
        """
        
        Retrieves geometric information from the current ECOTECT model, 
        specifically the horizontal angular distance of a line starting at 
        (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
        returned is given in degrees. 
    
        Parameter(s)
        This property takes the following parameters.
        
        absolute_position_start 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a starting point in 3 dimensional model space.
         
        absolute_position_end 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of an end point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        azi 
        The azimuth angle in degrees.
        
        """
        arg_str = p2e._util._convert_args_to_string("get.model.azimuth",
                                                          absolute_position_start[0],
                                                          absolute_position_start[1], 
                                                          absolute_position_start[2],
                                                          absolute_position_end[0],
                                                          absolute_position_end[1],
                                                          absolute_position_end[2])
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_type(val, float)           
    
    @apply
    def current_node():
        def fget(self):
            """
            
            Returns the zero-based index of the last selected node within the 
            currently loaded ECOTECT model. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            node 
            The zero-based index of the current node. 
            
            """
            val = p2e.conversation.Request("get.model.currentnode")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())  
    
    @apply
    def current_object():
        def fget(self):
            """
            
            Returns the zero-based index of the last selected object within the 
            currently loaded ECOTECT model. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            object 
            The zero-based index of the current object in the model.
             
            """
            val = p2e.conversation.Request("get.model.currentobject")
            return p2e._util._convert_str_to_type(val, int)   
        
        return property(**locals())  
    
    @apply
    def current_zone():
        def fget(self):
            """
            
            Returns the zero-based index of the current zone in the currently 
            loaded ECOTECT model. Thus, the Outside zone is always 0. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            model.currentzone 
            The zero-based index of the current zone. 
            
            """
            val = p2e.conversation.Request("get.model.currentzone")
            return p2e._util._convert_str_to_type(val, int)   
        
        return property(**locals())  
    
    def get_date(self):
        """
        
        Retrieves the current date as a formatted string ready for printing 
        or output to a file. 
    
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        day 
        An integer value between 1 and 31. 
        
        month 
        An integer value between 0 and 11. 
        
        """
        val = p2e.conversation.Request("get.model.date")
        return p2e._util._convert_str_to_list(val, int)  
    
    def set_date(self, day, month, time = None):
        """
        
        Sets the date in the ECOTECT model. 
        
        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 31. 
        
        month 
        An integer value between 0 and 11. 
        
        [time] 
        An optional decimal value between 0.0 and 23.99. 
        
        """
        if time:
            arg_str = p2e._util._convert_args_to_string("set.model.date", day, month, time)
        else:
            arg_str = p2e._util._convert_args_to_string("set.model.date", day, month)
        p2e.conversation.Exec(arg_str)
    
    @apply
    def date_string():    
        def fget(self):
            """
            
            Retrieves a formated string containing the current model date. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            dateStr 
            A formated date string. 
            
            """
            val = p2e.conversation.Request("get.model.datestring")
            return p2e._util._convert_str_to_type(val, str)
        
        return property(**locals())
    
    @apply
    def daylight_savings():            
        def fget(self):
            """
            
            Retrieves the status of the daylight savings flag. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            state 
            The daylight savings setting given as a boolean value where 1 
            represents the affirmative and 0 the negative. When true, the 
            current time is offset by one hour. 
            
            """
            val = p2e.conversation.Request("get.model.daylightsavings")
            return p2e._util._convert_str_to_type(val, bool)          
        
        def fset(self, state):
            """
            
            Sets the status of the daylight savings flag. 
    
            Parameter(s)
            This property takes the following parameters.
            
            [state] 
            Sets the daylight savings flag. This is a boolean value where 1 or true 
            represents the affirmative and 0 or false the negative. When set to 
            true, the current time is offset by one hour.
            
            """
            args = p2e._util._convert_args_to_string("set.model.daylightsavings", 
                                                       state)
            p2e.conversation.Exec(args)
            
        return property(**locals())
        
        
    def get_day_of_the_year(self):
        """
        
        Retrieves the current date and displays it in the julian date 
        format, where a single integer value between 1 and 365 represents a 
        day of the year. 
    
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        day 
        An integer value between 1 and 365 that represents a day of the 
        year. 
        
        """
        val = p2e.conversation.Request("get.model.dayoftheyear")
        return p2e._util._convert_str_to_type(val, int)  
    
    def set_day_of_the_year(self, day, time = None):
        """
        
        Sets the current date using the julian date format. 
    
        Parameter(s)
        This property takes the following parameters.
        
        day 
        An integer value between 1 and 365 that represents a day of the year. 
        
        [time] 
        This optional parameter is a decimal hour between 0.0 and 23.99.
         
        """
        if time:
            arg_str = p2e._util._convert_args_to_string("set.model.dayoftheyear", 
                                                          day, time)
        else:
            arg_str = p2e._util._convert_args_to_string("set.model.dayoftheyear", 
                                                          day)
        p2e.conversation.Exec(arg_str)
    
    @apply
    def directory():
        def fget(self):
            """
            
            Returns the drive and directory in which the currently loaded 
            ECOTECT model is located. This is essentially the full pathname, but 
            without the filename component. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            path 
            A text string containing the current directory path. 
        
            """
            val = p2e.conversation.Request("get.model.directory")
            return p2e._util._convert_str_to_type(val, str)
        
        def fset(self, path):
            """
            
            Sets the drive and directory to use with the currently loaded 
            ECOTECT model. 
        
            Parameter(s)
            This property takes the following parameters.
            
            path 
            A string value that defines the directory to use. Include both the 
            drive letter and full directory path. However, be aware of the 
            issues with backslashes in filename parameters as described in the 
            ECOTECT help file.
            
            """
            args = p2e._util._convert_args_to_string("set.model.directory", path)
            arg_str = p2e._util._convert_args_to_string(args)
            p2e.conversation.Exec(arg_str)
        
        return property(**locals())
    
    @apply
    def display():
        def fget(self):
            """
            
            Retrieves the current information display. When retrieving this 
            value, a single integer value is returned corresponding to items in 
            the Model Display table. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            display 
            What information is displayed in the model. This is given as an 
            integer value from the Model Display table below. 
                        
            Token Value Description 
            model 0 Default model only. 
            shadows 1 Shadows and reflections 
            normals 2 Surface normals. 
            sketch 3 Sketched view. 
            winddata 5 Wind distribution data. 
            sprayedrays 7 Sprayed acoustic rays. 
            values 8 Object attribute values. 
            zonetemps 9 Zone temperatures 
            rays 10 Acoustic rays and particles. 
            
            """
            val = p2e.conversation.Request("get.model.display")
            return p2e._util._convert_str_to_type(val, int)        
        
        def fset(self, display):
            """
            
            This property sets the current information display. 
        
            Parameter(s)
            This property takes the following parameters.
            
            display 
            Sets what information to display in the model. This can be specified 
            as either a token or value parameter, as outlined in the Model 
            Display table below. 
            
            Token Value Description 
            model 0 Default model only. 
            shadows 1 Shadows and reflections 
            normals 2 Surface normals. 
            sketch 3 Sketched view. 
            winddata 5 Wind distribution data. 
            sprayedrays 7 Sprayed acoustic rays. 
            values 8 Object attribute values. 
            zonetemps 9 Zone temperatures 
            rays 10 Acoustic rays and particles. 
            
            """
            args = p2e._util._convert_args_to_string("set.model.display", display)
            p2e.conversation.Exec(args)
        
        return property(**locals())
    
    def get_distance(self, absolute_position_start, absolute_position_end):
        """
        
        Retrieves geometric information from the current ECOTECT model, 
        specifically the distance between two points, starting at 
        (x1, y1, z1) and ending at (x2, y2, z2). The value returned is given 
        in the current units. 
        
        Parameter(s)
        This property takes the following parameters.
        
        absolute_position_start 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a starting point in 3 dimensional model space.
         
        absolute_position_end 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of an end point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dist 
        The distance value in the current model units.    
        
        """
        args = p2e._util._convert_args_to_string("get.model.distance", 
                                                       absolute_position_start[0],
                                                       absolute_position_start[1], 
                                                       absolute_position_start[2],
                                                       absolute_position_end[0],
                                                       absolute_position_end[1],
                                                       absolute_position_end[2])
        val = p2e.conversation.Request(args)
        return p2e._util._convert_str_to_type(val, float)          
    
    @apply
    def filename():
        def fget(self):
            """
            
            Returns the filename of the currently loaded ECOTECT model. This is 
            the filename only, with no drive or directory components. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            filename 
            A text string containing the filename. 
            
            """
            val = p2e.conversation.Request("get.model.filename")
            return p2e._util._convert_str_to_type(val, str)
        
        return property(**locals())
    
    @apply
    def last_node():
        def fget(self):
            """
            
            Returns the zero-based index of the last added/inserted node within 
            the currently loaded ECOTECT model. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            node 
            The zero-based index of the last created or inserted node. If no 
            such node exists, a value of -1 is returned. 
            
            """
            val = p2e.conversation.Request("get.model.lastnode")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())
    
    @apply
    def number_of_materials():
        def fget(self):
            """
            
            Returns the number of materials stored in the currently loaded 
            ECOTECT model. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The total number of materials defined within the current model's 
            element library. 
            
            """
            val = p2e.conversation.Request("get.model.materials")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())      
    
    @apply
    def month():
        def fget(self):
            """
            
            Returns the current month. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            month 
            The current model month given as an integer index between 0 and 11.
             
            """
            val = p2e.conversation.Request("get.model.month")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())
    
    def get_next_node(self, object, node):
        """
        
        Returns the zero-based absolute index of the next node in the specified 
        object, in relation to the current node. 
        
        Parameter(s)
        This property takes the following parameters.
        
        object 
        The object to use. 
        
        index 
        The node within the current object to use. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        node 
        The zero-based index of the next node. If no matching node is found, a 
        value of -1 is returned. 
        
        """
        args = p2e._util._convert_args_to_string("get.model.nextnode", 
                                                 object.eco_id, node.eco_id)
        val = p2e.conversation.Request(args)
        return p2e._util._convert_str_to_type(val, int)       
    
    def get_next_object(self, startat, type, flag, tag, zone):
        """
        
        Use this property to obtain the zero-based index of the next object 
        matching the type, flag and tag values specified. 
        
        Parameter(s)
        This property takes the following parameters.
        
        startat 
        The index value to start searching from. To search from the start, use a 
        value of -1. 
        
        type 
        The element type, as outlined in the Element Types table below. To 
        ignore this parameter, enter it as a negative value, such as -1. 
        
        flag 
        The integer flags from the Object Flags table. To combine multiple flag 
        values, add their numeric values together. To ignore this parameter, 
        enter it as a negative value, such as -1. 
        
        tag 
        The integer tag parameter from the Object Tags table. To combine 
        multiple tag values, add their numeric values together. To ignore this 
        parameter, enter it as a negative value, such as -1. 
        
        zone 
        The zone to which the object must belong. To ignore this parameter, 
        enter it as a negative value, such as -1. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        object 
        The zero-based index of the next object found. If no matching object is 
        found, a value of -1 is returned. 
        
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
        
        Object Flag Codes 
        Value Description 
        1 Object is a single-node point. 
        2 Object is a direction vector. 
        4 Object is a flat surface with an equation. 
        8 Objects is a closed loop. 
        16 Object defines a virtual polyline. 
        32 Object is formed from the extrusion of its parent. 
        64 Object has been extruded. 
        128 Object is linked to another as coplanar. 
        256 Object is linked to another as inside its extents. 
        512 Object is a complex/concave polygon. 
        1024 Object is the parent of another. 
        2048 Object is the child of another. 
        4096 Object defines a model zone. 
        8192 *User has specified particular nodes to generate equation. 
        16384 Object's surface normal is reversed. 
        32768 Object is partially transparent. 
        
        Object Tag Codes 
        Value Description 
        1 *User clicked near one of its lines. 
        2 *Part of the previous selection set. 
        16 Object has valid assigned attribute data. 
        32 Shadows are cast onto this object. 
        256 Object produces solar reflections. 
        512 Object is tagged as an acoustic reflector. 
        4096 Not used. 
        32768 *Generic calculation marker. 
    
        """
        #When -1 is entered for the zone parameter
        if zone < 0:
            args = p2e._util._convert_args_to_string("get.model.nextobject", 
                                                     startat, type, flag, tag, 
                                                     zone)
        else:
            args = p2e._util._convert_args_to_string("get.model.nextobject", 
                                                     startat, type, flag, tag, 
                                                     zone.eco_id)
        val = p2e.conversation.Request(args)
        return p2e._util._convert_str_to_type(val, int)          
    
    @apply
    def number_of_nodes():
        def fget(self):
            """
            
            Returns the number of individual object nodes within the currently 
            loaded ECOTECT model. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The total number of nodes within the current model. 
            
            """
            val = p2e.conversation.Request("get.model.nodes")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())          
    
    @apply
    def number_of_objects():
        def fget(self):
            """
            
            Returns the number of objects in the currently loaded ECOTECT model. 
            
            Parameter(s)
            This property takes the following parameters.
            
            count 
            The total number of objects in the current model. 
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The total number of objects in the current model.
             
            """
            val = p2e.conversation.Request("get.model.objects")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())
    
    def get_orientation(self, absolute_position_start, absolute_position_end):
        """
        
        Retrieves geometric information from the current ECOTECT model, 
        specifically the relative horizontal angle from North of a line starting 
        at (x1, y1, z1) and travelling towards var>(x2, y2, z2). The value 
        returned is given in a positive clockwise direction. 
        
        Parameter(s)
        This property takes the following parameters.
        
        absolute_position_start 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of a starting point in 3 dimensional model space.
         
        absolute_position_end 
        A list of three values that represent the absolute position in the 
        X, Y and Z axis of an end point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        ori 
        The orinetation angle in degrees. 
        
        """
        args = p2e._util._convert_args_to_string("get.model.orientation",
                                                           absolute_position_start[0],
                                                           absolute_position_start[1], 
                                                           absolute_position_start[2],
                                                           absolute_position_end[0],
                                                           absolute_position_end[1],
                                                           absolute_position_end[2])
        val = p2e.conversation.Request(args)
        return p2e._util._convert_str_to_type(val, float)        
    
    @apply
    def origin():
        def fget(self):
            """
            
            Retrieves the location of the Transformation Origin. This is a dynamic 
            point about which objects are rotated, scaled or mirrored. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            x, y, z 
            Represents the absolute position in the X, Y and Z axis of a point in 3 
            dimensional model space.
             
            """
            val = p2e.conversation.Request("get.model.origin")
            return p2e.p2e._util._convert_str_to_list(val, float)
        
        def fset(self, absolute_position):
            """
            
            Sets the location of the Transformation Origin. This is a dynamic point 
            about which objects are rotated, scaled or mirrored. 
            
            Parameter(s)
            This property takes the following parameters.
            
            absolute_position 
            A list of three values that represent the absolute position in the 
            X, Y and Z axis of a point in 3 dimensional model space. 
        
            """
            args = p2e._util._convert_args_to_string("set.model.origin", 
                                                               absolute_position[0],
                                                               absolute_position[1],
                                                               absolute_position[2])
            p2e.conversation.Exec(args)
        return property(**locals())     
    
    @apply
    def path_name():
        def fget(self):
            """
            
            Returns the full pathname of the currently loaded ECOTECT model. This 
            includes the full drive, directory and filename specification. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            pathname 
            A text string containing the full pathname.
            
            """
            return p2e.conversation.Request("get.model.pathname")
        
        return property(**locals())
    
    def get_prev_node(self, object, node):
        """
        
        Returns the zero-based absolute index of the previous node in the 
        specified object, in relation to the current node. 
    
        Parameter(s)
        This property takes the following parameters.
        
        object 
        The object to use. 
        
        index 
        The current node in the current object to use. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        node 
        The zero-based index of the previous node. If no matching node is found, 
        a value of -1 is returned. 
        
        """
        args = p2e._util._convert_args_to_string("get.model.prevnode", 
                                                 object.eco_id, node.eco_id)
        val = p2e.conversation.Request(args)
        return p2e._util._convert_str_to_type(val, int)        
    
    def get_prev_object(self, startat, type, flag, tag, zone):
        """
        
        Use this property to obtain the zero-based index of the preceding object 
        matching the type, flag and tag values specified. 
    
        Parameter(s)
        This property takes the following parameters.
        
        startat 
        The index value to start searching from. To search from the start, use 
        a value of -1. 
        
        type 
        This refers to the element type, as outlined in the Element Types table. 
        To ignore this parameter, enter it as a negative value such as -1. 
        
        flag 
        This parameter refers to the items in the Object Flags table. To combine 
        multiple flag values, simply add their numeric values together. To 
        ignore this parameter, enter it as a negative value such as -1. 
        
        tag 
        This parameter refers to the items in the Object Tags table. To combine 
        multiple tag values, simply add their numeric values together. To ignore 
        this parameter, enter it as a negative value such as -1. 
        
        zone 
        The zone to which the object must belong. To ignore this parameter, 
        enter it as a negative value such as -1. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        object 
        The zero-based index of the next object found. If no matching object is 
        found, a value of -1 is returned. 
        
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
    
        Object Flag Codes 
        Value Description 
        1 Object is a single-node point. 
        2 Object is a direction vector. 
        4 Object is a flat surface with an equation. 
        8 Objects is a closed loop. 
        16 Object defines a virtual polyline. 
        32 Object is formed from the extrusion of its parent. 
        64 Object has been extruded. 
        128 Object is linked to another as coplanar. 
        256 Object is linked to another as inside its extents. 
        512 Object is a complex/concave polygon. 
        1024 Object is the parent of another. 
        2048 Object is the child of another. 
        4096 Object defines a model zone. 
        8192 *User has specified particular nodes to generate equation. 
        16384 Object's surface normal is reversed. 
        32768 Object is partially transparent. 
    
        Object Tag Codes 
        Value Description 
        1 *User clicked near one of its lines. 
        2 *Part of the previous selection set. 
        16 Object has valid assigned attribute data. 
        32 Shadows are cast onto this object. 
        256 Object produces solar reflections. 
        512 Object is tagged as an acoustic reflector. 
        4096 Not used. 
        32768 *Generic calculation marker. 
        
        """
        #When -1 is entered for the zone parameter
        if zone < 0:
            args = p2e._util._convert_args_to_string("get.model.prevobject", 
                                                     startat, type, flag, tag, 
                                                     zone)
        else:
            args = p2e._util._convert_args_to_string("get.model.prevobject", 
                                                     startat, type, flag, tag, 
                                                     zone.eco_id)
        val = p2e.conversation.Request(args)
        return p2e._util._convert_str_to_type(val, int)         
    
    @apply
    def snap():
        def fget(self):
            """
            
            Retrieves the current information display
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            display 
            What information is displayed in the model. This is given as an integer 
            value from the Model Display table below. 
            
            Relevant Data Table(s)
            
            Model Display Options 
            Token Value Description 
            model 0 Default model only. 
            shadows 1 Shadows and reflections 
            normals 2 Surface normals. 
            sketch 3 Sketched view. 
            winddata 5 Wind distribution data. 
            sprayedrays 7 Sprayed acoustic rays. 
            values 8 Object attribute values. 
            zonetemps 9 Zone temperatures 
            rays 10 Acoustic rays and particles 
    
            """
            val = p2e.conversation.Request("get.model.snap")
            return p2e._util._convert_str_to_type(val, bool)         
        
        def fset(self, snap):
            """
            
            This property sets the current information display. 
    
            Parameter(s)
            This property takes the following parameters.
            
            display 
            Sets what information to display in the model. This can be specified as
             either a token or value parameter, as outlined in the Model Display
              table below. 
            
            Relevant Data Table(s)
            
            Model Display Options
             Token Value Description 
            model 0 Default model only. 
            shadows 1 Shadows and reflections 
            normals 2 Surface normals. 
            sketch 3 Sketched view. 
            winddata 5 Wind distribution data. 
            sprayedrays 7 Sprayed acoustic rays. 
            values 8 Object attribute values. 
            zonetemps 9 Zone temperatures 
            rays 10 Acoustic rays and particles. 
    
            """
            args = p2e._util._convert_args_to_string("set.model.snap", snap)
            p2e.conversation.Exec(args)
        
        return property(**locals())
    
    @apply
    def sun_angles():    
        def fget(self):
            """
            
            Returns two values, being the azimuth and altitude of the Sun for the 
            current date and time, given in decimal degrees. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            azi 
            The current solar azimuth given in degrees. 
            
            alt 
            The current solar altitude given in degrees. 
            
            """
            val = p2e.conversation.Request("get.model.sunangles")
            return p2e._util._convert_str_to_list(val, float)
        
        return property(**locals())          
        
    def get_sun_position(self, dist = 0, xyz = (0,0,0)):
        """
        
        Returns a position value that can be used to represent the Sun location 
        relative to the model. This is useful is you wish to locate a Sun 
        position relative to the centre of a WINDOW in order to spray a ray or 
        do a visibility test, for example. 
        
        Parameter(s)
        This property takes the following parameters.
        
        [dist] 
        The optional distance the Sun will be placed from the centre of the 
        model. 
        
        [x, y, z] 
        A list of three values. If these optional parameters are given, the Sun 
        position will be generated at a location dist away from this position, 
        using the current Sun angles in the model. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the Sun in 3 
        dimensional model space. 
        
        """
        arg_str = p2e._util._convert_args_to_string("get.model.sunposition", 
                                                              dist, xyz[0], 
                                                              xyz[1], xyz[2])
        val = p2e.conversation.Request(arg_str)
        return p2e._util._convert_str_to_list(val, float) 
    
    @apply
    def sunrise():
        def fget(self):
            """
            
            Returns the sunrise time as a 24 hour decimal value. Thus, 6:30am would 
            be returned as 6.5. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            sunrise 
            The time of sunrise given as a decimal hour. 
            
            """
            val = p2e.conversation.Request("get.model.sunrise")
            return p2e._util._convert_str_to_type(val, float)
        
        return property(**locals())   
    
    @apply
    def sun_set():
        def fget(self):
            """
            
            Returns the sunset time as a 24 hour decimal value. Thus, 6:30pm would 
            be returned as 18.5. 
        
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            sunset 
            The time of sunset given as a decimal hour. 
            
            """
            val = p2e.conversation.Request("get.model.sunset")
            return p2e._util._convert_str_to_type(val, float)
        
        return property(**locals())        
    
    @apply
    def time():
        def fget(self):
            """
            
            Retrieves the current time of day. The time value returned is a decimal 
            value between 0.0 and 23.99. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            time 
            A decimal value between 0.0 and 23.99. 
            
            """
            val = p2e.conversation.Request("get.model.time")
            return p2e._util._convert_str_to_type(val, float)          
        
        def fset(self, time):
            """
            
            Sets the current time of day. 
            
            Parameter(s)
            This property takes the following parameters.
            
            time 
            The time given in decimal hours, between 0.0 and 23.99. 
            
            """
            args = p2e._util._convert_args_to_string("set.model.time", time)
            p2e.conversation.Exec(args)
        
        return property(**locals())
    
    @apply
    def time_string():
        def fget(self):
            """
            
            Retrieves a formated string containing the current model time. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            timeStr 
            A formated time string. 
            
            """
            val = p2e.conversation.Request("get.model.timestring")
            return p2e._util._convert_str_to_type(val, str)
    
        return property(**locals())
    
    @apply
    def cap_extrusions():
        def fget(self):
            """
            
            Retrieves the capextrusions flag. When capextrusions is set to true or 
            1, extruding an object automatically generates a top or 'lid' to cap off 
            the volume. When set to false or 0, no lid is generated. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            state 
            A boolean value where 1 represents the affirmative and 0 the negative.
             
            """
            val = p2e.conversation.Request("get.model.xform.capextrusions")
            return p2e._util._convert_str_to_type(val, bool)          
        
        def fset(self, state = True):
            """
            
            Sets the capextrusions flag. 
            
            Parameter(s)
            This property takes the following parameters.
            
            [state] 
            When set to true, extruding an object automatically generates a top or 
            'lid' to cap off the volume. When set to false, no lid is generated. 
            
            """
            args = p2e._util._convert_args_to_string("set.model.xform.capextrusions", state)
            p2e.conversation.Exec(args)
        
        return property(**locals())
    
    @apply
    def vectors():
        def fget(self):
            """
            
            Retrieves the xform.vectors flag. With transform vectors set to true or 
            1, rotating an object with offset-linked children will also rotate the 
            offset vector. When set to false or 0, the offset vector remains the 
            same even though each object rotates individually. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            state 
            A boolean value where 1 represents the affirmative and 0 the negative.
             
            """
            val = p2e.conversation.Request("get.model.xform.vectors")
            return p2e._util._convert_str_to_type(val, bool)
        
        def fset(self, state = True):
            """
            
            Returns the number of zones in the currently loaded ECOTECT model as a 
            single integer. 
            
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The total number of zones in the current model. 
            
            """
            args = p2e._util._convert_args_to_string("set.model.xform.vectors", state)
            p2e.conversation.Exec(args)
        
        return property(**locals())
    
    @apply
    def zones():
        def fget(self):
            """
            
            Returns the number of zones in the currently loaded ECOTECT model as a 
            single integer. 
    
            Parameter(s)
            There are no parameters for this property.
            
            Return Value(s)
            Getting this property returns the following value(s).
            
            count 
            The total number of zones in the current model.
            
            """
            val = p2e.conversation.Request("get.model.zones")
            return p2e._util._convert_str_to_type(val, int)
        
        return property(**locals())
    
#===============================================================================
# Main function used for testing
#===============================================================================
def test_doc_test():
    """
    >>> test_doc_test()
    Hi
    """
    print "Hi"
        
if __name__ == "__main__":
    x = Model()
    #import doctest
    #doctest.testmod()
    #dump("C:\Test\mytest1.eco")
    #print get_altitude(11, 10, 15, 9, 16, 13)
    #print x.get_zones()
    
    print "Tests completed"     
    