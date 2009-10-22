import py2ecotect as p2e
  
#==============================================================================
# _ZoneRootObjs
#==============================================================================
class _ZoneRootObjs(object):
    #------------------------------------------------------------------------------ 
    def objects(self):
        """
        
        Returns the zone's object(s). 

        Parameter(s)
        This property has no parameters.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        objects 
        A list of objects belonging to this zone.
        
        """
        object_id = self.next_object(-1, -1, -1, -1)
        prev_id = object_id
        objects = []
        while (object_id != -1):
            objects.append(p2e.model._objects[object_id])
            object_id = self.next_object(prev_id, -1, -1, -1)
            prev_id = object_id
        return objects
    #------------------------------------------------------------------------------ 
    def next_object(self, startat, type, flag, tag):
        """
        
        Use this property to obtain the zero-based index of the next object 
        matching the type, flag and tag values specified, but belonging to the 
        specificed zone. 

        Parameter(s)
        This property takes the following parameters.
        
        startat 
        The index value to start searching from. To search from the start, use 
        a value of -1. 
        
        type 
        The element type, as outlined in the Element Types table below. To 
        ignore this parameter, enter a negative value, such as -1. 
        
        flag 
        The boolean flags from the Object Flags table. To combine multiple flag 
        values, add their numeric values together. To ignore this parameter, 
        enter a negative value, such as -1. 
        
        tag 
        The boolean tag parameter from the Object Tags table. To combine 
        multiple tag values, add their numeric values together. To ignore this 
        parameter, enter a negative value, such as -1. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the next matching object. If no object is found, 
        a value of -1 is returned. 
        
        Relevant Data Table(s)
        
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
        arg_str = p2e._base._util._convert_args_to_string("get.zone.nextobject", 
                                                     self._eco_id, 
                                                     startat, type, flag, tag)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)         
#==============================================================================
# _ZoneRootModf
#==============================================================================
class _ZoneRootModf(object):
    #---------------------------------------------------------------------------
    def delete(self):
        """
        
        Use this method to delete the specified zone and all the objects it 
        contains. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        #execute ecotect instruction
        arg_str = p2e._base._util._convert_args_to_string("zone.delete", self._eco_id)
        p2e._app.Exec(arg_str)
        
        #Delete objects of this zone
        objects = self._zone.objs.objects
        for i in objects():
            i.delete()
            
        #Update model lists
        p2e.model._zones.remove(self._zone)
#==============================================================================
# _ZoneRootTrfm
#==============================================================================
class _ZoneRootTrfm(object):
    def move_by_vec(self, vector):
        """
        
        Moves all objects in the specified zone a distance of dx , dy and dz in 
        the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        vector 
        A list of three values representing the offset distance in each of the 
        X, Y and Z axis, given in model coordinates.
        
        """
        vector = p2e._base._util.scale_1000(vector)
        
        arg_str = p2e._base._util._convert_args_to_string("zone.move", self._eco_id, 
                                                      vector[0], 
                                                      vector[1], 
                                                      vector[2])
        p2e._app.Exec(arg_str)

    def nudge(self, dir):
        """
        
        Nudges the all objects in the specified zone in the given axis. 

        Parameter(s)
        This command takes the following parameters.
        
        dir 
        An integer value corresponding to the Nudge Direction table below. 
        
        Relevant Data Table(s)
        
        Nudge Directions 
        Value Description 
        1, -1 In the X axis. 
        2, -2 In the Y axis. 
        3, -3 In the Z axis. 

        """
        arg_str = p2e._base._util._convert_args_to_string("zone.nudge", self._eco_id, dir)
        p2e._app.Exec(arg_str)

    def rotate(self, azi, alt):
        """
        
        Rotates all objects in the specified zone about the Transformation 
        Origin (see set.model.origin). Rotation is done about the Y axis first 
        (altitude) and then the Z axis (aziumuth). 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The azimuth value in degrees. 
        
        alt 
        The altitude value in degrees. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("zone.rotate", self._eco_id, 
                                                      azi, alt)
        p2e._app.Exec(arg_str)

    def rotate_axis(self, rotation_degree):
        """
        
        Rotates all objects in the specified zone about the Transformation 
        Origin (see set.model.origin). Rotation is done by the given angles in 
        each axis. 

        Parameter(s)
        This command takes the following parameters.
        
        rotation_degree 
        A list of three values representing the degrees of rotation in each of 
        the X, Y, Z Axis.
        """
        arg_str = p2e._base._util._convert_args_to_string("zone.rotateaxis", 
                                                      self._eco_id, 
                                                      rotation_degree[0], 
                                                      rotation_degree[1], 
                                                      rotation_degree[2])
        p2e._app.Exec(arg_str)

    def rotate_reverse(self, azi, alt):
        """
        
        Rotates all objects in the specified zone about the Transformation 
        Origin (see set.model.origin). Rotation is done about the Z axis first 
        (altitude) and then the Y axis (aziumuth). 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The azimuth value in degrees. 
        
        alt 
        The altitude value in degrees.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("zone.rotatereverse", 
                                                      self._eco_id, azi, alt)
        p2e._app.Exec(arg_str)

    def scale(self, scale_factors):
        """
        
        Scales all objects in the specified zone by a factor of sx, sy and sz in 
        the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        scale_factors 
        A list of three values representing the scaling factor in each of the 
        X, Y and Z axis.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("zone.scale", self._eco_id, 
                                                     scale_factors[0], 
                                                     scale_factors[1], 
                                                     scale_factors[2])
        p2e._app.Exec(arg_str)

    def xform(self, transformation, function_values):
        """
        
        Apply a generic transform to all objects in the specified zone. 

        Parameter(s)
        This command takes the following parameters.
        
        transformation 
        The transformation to use, given as a token corresponding to the 
        Transformation Types table. 
        
        function_values 
        A list of three values specified by the table below. 
        
        Relevant Data Table(s)
        
        Transformation Types 
        Token Description 
        axis Axial rotation, where x , y and z are axial angles in degrees. 
        reverse Reverse polar rotation, where x and y are azi and alt in degrees. 
        rotate Polar rotation, where x and y are azi and alt in degrees. 
        move Translate objects by x , y and z values in the major axis. 
        scale Scale objects by x , y and z in the major axis. 
        mirror Mirror objects around About Point and vector formed by x , y and z.  
        normal Extrude objects a distance of x along its surface normal. 
        extrude Extrude objects by x , y and z in the major axis. 
        revolve Revolve objects around axis x , y degrees and in z segments. 
        nudge Nudge objects a distance of x , y and z in the major axis. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("zone.xform", self._eco_id, 
                                                      transformation, 
                                                      function_values[0], 
                                                      function_values[1], 
                                                      function_values[2])
        p2e._app.Exec(arg_str)
    
#==============================================================================
# _ZoneRootFunc
#==============================================================================
class _ZoneRootFunc(object):

    def extrude_by_vec(self, vector):
        """
        
        Extrudes the FLOOR object(s) in the specified zone a distance of 
        (dx, dy, dz) in the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        vector 
        A list of three values representing the offset distance in each of the 
        X, Y and Z axis, given in model coordinates. 
        
        """
        vector = p2e._base._util.scale_1000(vector)
        
        arg_str = p2e._base._util._convert_args_to_string("zone.extrude", self._eco_id, 
                                                      vector[0], 
                                                      vector[1], 
                                                      vector[2])
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def index(self, name):
        """
        
        This property returns the zero-based index of the zone with a name 
        matching the name parameter. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        A string value representing the name of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the matching zone. If no matching zone is found, 
        an index of -1 is returned. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.index", 
                                                     name)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

#==============================================================================
# _ZoneRootGrps
#==============================================================================
class _ZoneRootGrps(object):
    #------------------------------------------------------------------------------ 
    def group_hidden(self, group):
        """
        
        Retrieves the hidden state of the specified zone group. Hidden zones 
        still take part in all analytical calculations, but are not visible in 
        the current model view. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.group.hidden", 
                                                     group)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
         
    def set_group_hidden(self, group, hidden):
        """
        
        Sets the hidden state of all zones in the specified zone group. Hidden 
        zones still take part in all analytical calculations, but are not 
        visible in the current model view. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        hidden 
        A boolean value where 1 or true represents the affirmative and 0 or 
        false the negative.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.group.hidden", 
                                                     group, hidden)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def group_index(self, name):
        """
        
        Retrieves the index (0-15) the specified zone group name. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        The name of the zone group to find the index of. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The zero-based index of the matching zone group (0-15). if no match is 
        found, the value -1 is returned.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.group.index", 
                                                     name)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
    #------------------------------------------------------------------------------ 
    def group_locked(self, group):
        """
        
        Retrieves the locked state of the specified zone group. Locked zones are 
        still displayed and take part in calculations, but the user cannot 
        interactively select or manipulate them. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.group.locked", 
                                                     group)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
        
    def set_group_locked(self, group, locked):
        """
        
        Sets the locked state of all zones in the specified zone group. Locked 
        zones are still displayed and take part in calculations, but the user 
        cannot interactively select or manipulate them. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        locked 
        A boolean value where 1 or true represents the affirmative and 0 or 
        false the negative.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.group.locked", 
                                                     group, locked)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def group_name(self, group, nospaces = False):
        """
        
        Retrieves the name of the specified zone group. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        [nospaces] 
        An optional boolean true/false parameter specifying that the returned 
        name should have all spaces replaced by the underscore ('_') character. 
        The default values for this parameters is false. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A test string containing the name of the specfied group.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.group.name", 
                                                     group, nospaces)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, str)

    def set_group_name(self, group, name):
        """
        
        Sets the name of the specified zone group. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        name 
        The name of the specfied group.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.group.name", 
                                                     group, name)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def  group_off(self, group):
        """
        
        Retrieves the off state of the specified zone group. Off zones are 
        effectively removed from the mode and are not displayed or involved in 
        any calculations. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.group.off", 
                                                     group)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_group_off(self, group, off):
        """
        
        Sets the off state of all zones in the specified zone group. Off zones 
        are effectively removed from the mode and are not displayed or involved 
        in any calculations. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        off 
        A boolean value where 1 or true represents the affirmative and 0 or 
        false the negative. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.group.off", 
                                                     group, off)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def is_group_thermal(self, group):
        """
        
        Retrieves the thermal state of the specified zone group. Thermal zones 
        are treated as fully enclosed spaces or rooms for which volume, 
        temperature and acoustic data is calculated. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.group.thermal", 
                                                     group)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_is_group_thermal(self, group, thermal):
        """
        
        Sets the thermal state of all zones in the specified zone group. 
        Thermal zones are treated as fully enclosed spaces or rooms for which 
        volume, temperature and acoustic data is calculated. 

        Parameter(s)
        This property takes the following parameters.
        
        group 
        The zero-based index of the required zone group (0-15). 
        
        thermal 
        A boolean value where 1 or true represents the affirmative and 0 or 
        false the negative. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.group.thermal", 
                                                     group, thermal)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 

    def is_in_group(self, group):
        """
        
        Determines if the specified zone belongs to the given zone group. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index of the zone to be tested. 
        
        group 
        The zero-based index of the zone group (0-15) to test against. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        belongs 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.ingroup", 
                                                     self._eco_id, group)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)        
#==============================================================================
# _ZoneRootState
#==============================================================================
class _ZoneRootState(object):
    #------------------------------------------------------------------------------ 
    def colour(self):
        """
        
        Retrieves the colour of the specified zone. 

        Parameter(s)
        There are no parameters for this command.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dcolor 
        The displayed colour of the zone as a full hexidecimal value. 
        
        scolor 
        The colour of shadow the zone projects as a full hexidecimal value. 
        
        rcolor 
        The colour of reflection the zone project as a full hexidecimal value.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.colour", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, str, str, str)
    
    def set_colour(self, display, shadow = "0x000000", reflection = "000000"):
        """
        
        Sets the colour or colours of the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        display 
        The colour of the zone as a full hexidecimal value (eg: 0xFF8800). 
        
        [shadow] 
        This optional parameter specifies the colour of the shadow generated by 
        the zone, given as a full hexideciman value (eg: 0xFF8800). 
        
        [reflection] 
        This optional parameter specifies the colour of the reflection generated 
        by the zone, given as a full hexideciman value (eg: 0xFF8800). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.colour", 
                                                     self._eco_id, display, shadow, 
                                                     reflection)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def random_colour(self):
        """
        
        Sets the display colour of the specified zone to a random colour based 
        on the current background. 

        Parameter(s)
        There are no parameters for this property.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.randomcolour", self._eco_id)
        p2e._app.Exec(arg_str)        
    #------------------------------------------------------------------------------ 
    def is_current(self):
        """
        
        Determine if the specified zone is the current zone. To get the actual 
        index of the current zone, use the model.currentzone property. 

        Parameter(s)
        There are no parameters for this command.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.current", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
        
    def set_current(self):
        """
        
        Sets the specified zone to be the current zone. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.current", self._eco_id)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def select_objects(self, state = True):
        """
        
        Selects or deselects all objects in the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        [state] 
        This optional parameter specifies whether to select (true) or deselect 
        (false) objects on the zone. It defaults to true. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.selected", self._eco_id, state)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)   
    #------------------------------------------------------------------------------ 
    def is_off(self):
        """
        
        Retrieves the current off state of the specified zone. Off zones are 
        effectively removed from the mode and are not displayed or involved in 
        any calculations. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.off", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_off(self, state = True):
        """
        
        Sets or resets the specified zone's off state. Off zones are effectively 
        removed from the mode and are not displayed or involved in any 
        calculations. 

        Parameter(s)
        This property takes the following parameters.
        
        [state] 
        This optional parameter will set (true) or reset (false) the specified 
        state. Defaulting to true if not given. 

        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.off", self._eco_id, state)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def is_locked(self):
        """
        
        Retrieves the current locked state of the specified zone. Locked zones 
        are still displayed and take part in calculations, but the user cannot 
        interactively select or manipulate them. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.locked", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int) 
    
    def set_locked(self, state = True):
        """
        
        Sets or resets the specified zone's locked state. Locked zones are still 
        displayed and take part in calculations, but the user cannot 
        interactively select or manipulate them. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        [state] 
        This optional parameter will set (true) or reset (false) the specified 
        state. Defaulting to true if not given.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.locked", 
                                                     self._eco_id, state)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def is_thermal(self):
        """
        
        Retrieves the current thermal state of the specified zone. Thermal zones 
        are treated as fully enclosed spaces or rooms for which volume, 
        temperature and acoustic data is calculated. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.thermal", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
    
    def set_thermal(self, state = True):
        """
        
        Sets or resets the specified zone's thermal state. Thermal zones are 
        treated as fully enclosed spaces or rooms for which volume, temperature 
        and acoustic data is calculated. 

        Parameter(s)
        This property takes the following parameters.
        
        [state] 
        This optional parameter will set (true) or reset (false) the specified 
        state. Defaulting to true if not given.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.thermal", self._eco_id, state)
        p2e._app.Exec(arg_str)        
   #------------------------------------------------------------------------------         
    def isolate(self):
        """
        
        Hides all other zones and isolates the specified zone within the current 
        view. Effectively the same as interactively pressing the F4 key. 

        Parameter(s)
        This command takes the following parameters.

        """
        arg_str = p2e._base._util._convert_args_to_string("zone.isolate", self._eco_id)
        p2e._app.Exec(arg_str)        
#==============================================================================
# _ZoneRootProp
#==============================================================================
class _ZoneRootProp(object):
    
    #------------------------------------------------------------------------------ 
    def activity(self):
        """
        
        Retrieves the occupant activity rate in the specified zone. 

        Parameter(s)
        There are no parameters for this command.
        
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The activity rate index based on the following Zone Activity Rates table. 
        
        Relevant Data Table(s)
        
        Zone Activity Rates 
        Token Value Description 
        sedentary 0 Sitting at a desk (70W) 
        walking 1 Moving about (80W) 
        exercising 2 Significant activity (100W) 
        strenuous 3 Significant exertion (150W) 
        sleeping 5 Sleeping (40 W, 0.7 Met) 
        resting 6 Resting (45 W, 0.8 Met) 
        reading 7 Reading (55 W, 1.0 Met) 
        typing 8 Typing (65 W, 1.1 Met) 
        clerical 9 Clerical (70 W, 1.2 Met) 
        cooking 10 Cooking, lite (95 W, 1.6 Met) 
        cleaning 12 Cleaning, lite (115 W, 2.0 Met) 
        slow walking 13 Slow Walking (115 W, 2.0 Met) 
        dancing 14 Dancing, lite (140 W, 2.4 Met) 
        lite execise 16 Light Exercise (175 W, 3.0 Met) 
        fast walking 17 Fast Walking (200 W, 3.4 Met) 
        hvyexercise 19 Exercise, hvy (235 W, 4.0 Met) 
        work 20 Heavy Work (235 W, 4.0 Met) 
        sport 22 Team Sport (440 W, 7.6 Met) 
  
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.activity", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
    
    def set_activity(self, type):
        """
        
        Sets the average occupant activity rate in the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        An integer value corresponding to the following Zone Activity Rates 
        table. 
        
        Relevant Data Table(s)
        
        Zone Activity Rates 
        Token Value Description 
        sedentary 0 Sitting at a desk (70W) 
        walking 1 Moving about (80W) 
        exercising 2 Significant activity (100W) 
        strenuous 3 Significant exertion (150W) 
        sleeping 5 Sleeping (40 W, 0.7 Met) 
        resting 6 Resting (45 W, 0.8 Met) 
        reading 7 Reading (55 W, 1.0 Met) 
        typing 8 Typing (65 W, 1.1 Met) 
        clerical 9 Clerical (70 W, 1.2 Met) 
        cooking 10 Cooking, lite (95 W, 1.6 Met) 
        cleaning 12 Cleaning, lite (115 W, 2.0 Met) 
        slow walking 13 Slow Walking (115 W, 2.0 Met) 
        dancing 14 Dancing, lite (140 W, 2.4 Met) 
        lite execise 16 Light Exercise (175 W, 3.0 Met) 
        fast walking 17 Fast Walking (200 W, 3.4 Met) 
        hvyexercise 19 Exercise, hvy (235 W, 4.0 Met) 
        work 20 Heavy Work (235 W, 4.0 Met) 
        sport 22 Team Sport (440 W, 7.6 Met) 

        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.activity", 
                                                     self._eco_id, type)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 

    def admittance(self):
        """
        
        Retrieves the specified zone's current value for the total zone 
        admittance (W/m^2K). 

        Parameter(s)
        There are no parameters for this command.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.admittance", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    def set_admittance(self, value):
        """
        
        Sets the specified zone's value for the total zone admittance (W/m^2K). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total zone admittance (W/m^2K). 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.admittance", 
                                                     self._eco_id, value)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def air_speed(self):
        """
        
        Retrieves the specified zone's current value for the designed internal 
        air-speed (m/s). 

        Parameter(s)
        There are no parameters for this command.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.airspeed", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_air_speed(self, value):
        """
        
        Sets the specified zone's value for the designed internal air-speed (m/s). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the designed internal air-speed as (m/s).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.airspeed", 
                                                     self._eco_id, value)
        p2e._app.Exec(arg_str)  
    #------------------------------------------------------------------------------ 
    def appliance_energy(self):
        """
        
        Retrieves the specified zone's current value for the total energy gain 
        from APPLIANCE objects. 

        Parameter(s)
        There are no parameters for this command.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.applianceenergy", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    def set_appliance_energy(self, value):
        """
        
        Sets the specified zone's current value for the total energy gain from 
        APPLIANCE objects. 
        
        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total energy gain from APPLIANCE objects.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.applianceenergy", 
                                                      self._eco_id, value)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def clothing(self):
        """
        
        Retrieves the specified zone's current value for the design clothing 
        value of occupants (clo). 

        Parameter(s)
        There are no parameters for this command.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.clothing", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    def set_clothing(self, value):
        """
        
        Sets the specified zone's current value for the design clothing value of 
        occupants (clo). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the design clothing value of occupants (clo). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.clothing", 
                                                     self._eco_id, value)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def hvac_efficiency(self):
        """
        
        Retrieves the specified zone's current value for the HVAC system 
        efficiency (%). 

        Parameter(s)
        There are no parameters for this property. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.efficiency", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    def set_hvac_efficiency(self, value):
        """
        
        Sets the specified zone's current value for the HVAC system 
        efficiency (%). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the HVAC system efficiency (%). 

        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.efficiency", self._eco_id, value)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def window_equator_area(self):
        """
        
        Retrieves the specified zone's current value for the total exposed 
        WINDOW area facing the equator (m^). 

        Parameter(s)
        There are no parameters for this property.

        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.equatorarea", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    def set_window_equator_area(self, value):
        """
        
        Sets the specified zone's current value for the total exposed WINDOW 
        area facing the equator (m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total exposed WINDOW area facing the equator 
        (m^2). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.equatorarea", self._eco_id, value)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def exposed_area(self):
        """
        
        Retrieves the specified zone's current value for the total surface area 
        exposed to outside conditions (m^2). 

        Parameter(s)
        There are no parameters for this property.
    
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.exposedarea", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_exposed_area(self, value):
        """
        
        Sets the specified zone's current value for the total surface area 
        exposed to outside conditions (m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total surface area exposed to outside 
        conditions (m^2).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.exposedarea", self._eco_id, value)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def flag(self, flag):
        """
        
        In ECOTECT, zone have a range of boolean flags associated with them that 
        are used at various times. This property retrieves the nominated flag 
        settings for the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value representing a binary bit as shown in the Zone Flag 
        Codes table below. To test multiple flags at once, simply add their 
        values together. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true if the flag is set and 0 or 
        false if the flag is not set. 
        
        Relevant Data Table(s)
        
        Zone Flag Codes 
        No. Flag Name 
        1 VOLUME_OK 
        2 THERMAL_OK 
        4 MATERIALS_OK 
        8 DELETED 
        16 OFF 
        32 LOCKED 
        64 THERMAL 
        128 HIDDEN 
        256 SELECTED 
        512 CROSSVENT 
        1024 SINGLE_SIDED 
        2048 UNDO_FLAG 
        4096 COMFORT 
        8192 TEMPERATURES 
        16384 HEAT_LOADS 
        32768 SHADOWCOLOR 
        65536 MALFORMED 
        131072 NO_EXPORT 
        1048576 LIST_REFRESH 
        8388608 NO_SHADOWS 
        16777216 NO_OUTLINE 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.flag", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_flag(self, flag, state = True):
        """
        
        In ECOTECT, zone have a range of boolean flags associated with them that 
        are used at various times. This property sets the nominated flag 
        settings for the specified zone.

        Important Note: Flags are fundamental to how the model works. Be very 
        careful before setting any of them manually, and always operate on files 
        for which you have up-to-date backups. Incorrect usage of flags can 
        corrupt your model beyond repair (ECOTECT probably shouldn't allow these 
        values to be set via a script, however someone will have a valid reason 
        at some stage, and if the user cannot be trusted, who can be trusted?). 
        
        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value representing a binary bit, as shown in the Zone Flag 
        Codes table. To set multiple flags at once, simply add their values 
        together. 
        
        state 
        A boolean value representing the desired state of the flag, where 1 or 
        true sets the flag and 0 or false clears it. This parameter defaults to 
        true if not specified. 
        
        Relevant Data Table(s)
        
         Zone Flag Codes 
         No. Flag Name 
        1 VOLUME_OK 
        2 THERMAL_OK 
        4 MATERIALS_OK 
        8 DELETED 
        16 OFF 
        32 LOCKED 
        64 THERMAL 
        128 HIDDEN 
        256 SELECTED 
        512 CROSSVENT 
        1024 SINGLE_SIDED 
        2048 UNDO_FLAG 
        4096 COMFORT 
        8192 TEMPERATURES 
        16384 HEAT_LOADS 
        32768 SHADOWCOLOR 
        65536 MALFORMED 
        131072 NO_EXPORT 
        1048576 LIST_REFRESH 
        8388608 NO_SHADOWS 
        16777216 NO_OUTLINE 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.flag", self._eco_id, flag, state)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------    
    def floor_area(self):
        """
        
        Retrieves the specified zone's current value for the total zone floor 
        area (m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.floorarea", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
        
    def set_floor_area(self, value):
        """
        
        Sets the specified zone's current value for the total zone floor area 
        (m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        value representing the total zone floor area (m^2). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.floorarea", self._eco_id, value)
        p2e._app.Exec(arg_str)

    #------------------------------------------------------------------------------ 
    def upper_comfort_band(self):
        """
        
        Retrieves the specified zone's current value for the upper comfort band 
        (deg celsius). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.upperband", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_upper_comfort_band(self, value):
        """
        
        Sets the specified zone's current value for the upper comfort band 
        (deg celcius). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the upper comfort band (deg celsius). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.upperband", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def u_value(self):
        """
        
        Retrieves the specified zone's current value for the total U-Value of 
        exposed surface area (Heat loss rate W/m K). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.uvalue", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_u_value(self, value):
        """
        
        Sets the specified zone's current value for the total U-Value of exposed 
        surface area (Heat loss rate W/m K). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total U-Value of exposed surface area (Heat 
        loss rate W/m K). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.uvalue", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def ventilation_rate(self):
        """
        
        Retrieves the specified zone's current value for the wind-driven 
        ventilation rate (ac/h). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.ventilationrate", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_ventilation_rate(self, value):
        """
        
        Sets the specified zone's current value for the wind-driven ventilation 
        rate (ac/h). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the wind-driven ventilation rate (ac/h).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.ventilationrate", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def volume(self):
        """
        
        Retrieves the specified zone's current value for the internal zone 
        volume (m^3). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.volume", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
        
    def set_volume(self, value):
        """
        
        Sets the specified zone's current value for the internal zone volume 
        (m^3). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the internal zone volume (m^3).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.volume", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def window_area(self):
        """
        
        Retrieves the specified zone's current value for the total exposed 
        WINDOW area (m^2). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.windowarea", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
 
    def set_window_area(self, value):
        """
        
        Sets the specified zone's current value for the total exposed WINDOW 
        area (m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total exposed WINDOW area (m^2). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.windowarea", self._eco_id, value)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def comfort(self, day, hour):
        """
        
        Retrieves the number of hours the specified zone spent at the given 
        temperature. This value is only valid after a Temperature Distribution 
        calculation has been performed. 

        Parameter(s)
        There are no parameters for this command.
        
        day 
        An integer value between 1 and 365 representing the day of the year. 
        
        hour 
        An integer value between 0 and 23 representing the hour of the day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        pmv 
        The Predicted Mean Vote value between -3 and +3. 
        
        ppd 
        The Percentage People Dissatisfied between 5% (losest) and 100% 
        (everyone).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.comfort", 
                                                     self._eco_id, day, hour)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float)
    #------------------------------------------------------------------------------ 
    def cooling_load(self, month):
        """
        
        Retrieves the total monthly cooling load for the zone during the given 
        month. 

        Parameter(s)
        This property takes the following parameters.
       
        month 
        A value between 0 and 11 representing the month to retrieve the value 
        from. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The cooling load value for the given month. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.cooling", self._eco_id, month)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    #------------------------------------------------------------------------------ 
    def temperature_distribution(self, temperature):
        """
        
        Retrieves the number of hours the specified zone spent at the given 
        temperature. This value is only valid after a Temperature Distribution 
        calculation has been performed. 

        Parameter(s)
        This property takes the following parameters.
        
        temperature 
        The temperature in degrees celsius. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The hour count spent at the given temperature.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.distribution", 
                                                     self._eco_id, temperature)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    #------------------------------------------------------------------------------ 
    def heating_load(self, month):
        """
        
        Retrieves the total monthly heating load for the zone during the given 
        month. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        month 
        A value between 0 and 11 representing the month to retrieve the value 
        from. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The heating load in Wh for the given month.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.heating", 
                                                     self._eco_id, month)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    #------------------------------------------------------------------------------ 
    def hidden(self):
        """
        
        Retrieves the current hidden state of the specified zone. Hidden zones 
        still take part in all analytical calculations, but are not visible in 
        the current model view. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        A boolean value where 1 represents true and 0 represents false. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.hidden", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
            
    def set_hidden(self, state = True):
        """
        
        Sets or resets the specified zone's hidden state. Hidden zones still 
        take part in all analytical calculations, but are not visible in the 
        current model view. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        [state] 
        This optional parameter will set (true) or reset (false) the specified 
        state. Defaulting to true if not given.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.hidden", self._eco_id, state)
        p2e._app.Exec(arg_str)
        

    #------------------------------------------------------------------------------ 
    def infiltration_rate(self):
        """
        
        Retrieves the specified zone's current value for the air infiltration 
        rate (ac/h). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.infiltrationrate", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    def set_infiltration_rate(self, value):
        """
        
        Sets the specified zone's current value for the air infiltration rate 
        (ac/h). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the air infiltration rate (ac/h). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.infiltrationrate", 
                                                     self._eco_id, value)
        p2e._app.Exec(arg_str)
    
    #------------------------------------------------------------------------------ 
    def internal_gains(self):
        """
        
        Retrieves the specified zone's current value for the total internally 
        generated heat gains (W). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.internalgains", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
        
    def set_internal_gains(self, value):
        """
        
        Sets the specified zone's current value for the total internally 
        generated heat gains (W). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the total internally generated heat gains (W). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.internalgains", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------   
    def interzonal_gains(self):
        """
        
        Retrieves the specified zone's current value for the total gains flowing 
        to/from other adjacent zones (W). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.interzonalgains", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    
    #------------------------------------------------------------------------------ 
    def latent_gains(self):
        """
        
        Retrieves the specified zone's current value for the latent internal 
        heat gains (W/m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.latentgains", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float) 
    
    def set_latent_gains(self, value):
        """
        
        Sets the specified zone's current value for the latent internal heat 
        gains (W/m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the latent internal heat gains (W/m^2).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.latentgains", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def lighting_energy(self):
        """
        
        Retrieves the specified zone's current value for the total energy gain 
        from LIGHT objects. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.lightingenergy", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float) 
    
    def set_lighting_energy(self, value):
        """
        
        Sets the specified zone's current value for the total energy gain from 
        LIGHT objects. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the total energy gain from LIGHT objects.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.latentgains", self._eco_id, value)
        p2e._app.Exec(arg_str)
        

        
    #------------------------------------------------------------------------------ 
    def lower_comfort_band(self):
        """
        
        Retrieves the specified zone's current value for the lower comfort 
        band ( deg Celsius). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.lowerband", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float) 
    
    def set_lower_comfort_band(self, value):
        """
        
        Sets the specified zone's current value for the lower comfort band 
        (deg Celsius). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the lower comfort band (deg Celsius). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.lowerband", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def lux(self):
        """
        
        Retrieves the specified zone's current value for the design internal 
        lighting level (lux). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.lux", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float) 

    def set_lux(self, value):
        """
        
        Sets the specified zone's current value for the design internal lighting 
        level (lux). 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the design internal lighting level (lux). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.lux", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def method_reverb(self):
        """
        
        Retrieves the specified zone's current value for the reverberation 
        calculation method. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.methodreverb", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float) 

    def set_method_reverb(self, value):
        """
        
        Sets the specified zone's current value for the reverberation 
        calculation method. 

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        The zero-based index value of the zone. 
        
        value 
        A value representing the reverberation calculation method.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.methodreverb", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def name(self):
        """
        
        Returns the zone's name. 

        Parameter(s)
        This property has no parameters.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        name 
        A text string containing the zone's name.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.name", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, str) 

    def set_name(self, name):
        """
        
        Sets the specified zone's name. 

        Parameter(s)
        This property takes the following parameters. 
        
        name 
        A string of up to 40 characters representing the zone name. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.name", self._eco_id, name)
        p2e._app.Exec(arg_str)
        

    #------------------------------------------------------------------------------ 
    def occupancy(self):
        """
        
        Retrieves the number of people within the specified zone. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        people 
        A value representing the number of people in the zone. 
        
        full 
        The current percentage of maximum zone occupancy. 
        
        seatingtype 
        The seating type corresponding to the Zone Seating Codes table below. 
        
        Relevant Data Table(s)
        
        Zone Seating Codes 
        Value Description 
        0 None 
        1 Upholstered seating 
        2 Cloth covered seating 
        3 Hard-backed seating 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.occupancy", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, int, float, int)

    def set_occupancy(self, people, percentagefull = 0.0, seatingtype = 0):
        """
        
        Sets the number of people within the specified zone. 

        Parameter(s)
        This property takes the following parameters.

        people 
        A value representing the number of people. 
        
        [percentagefull] 
        This optional parameter specifies the percentage of the zone that is 
        occupied. 
        
        [seatingtype] 
        This optional parameter specifies the seating type and corresponds to 
        the Zone Seating Codes table below. 
        
        Relevant Data Table(s)
        
        Zone Seating Codes 
        Value Description 
        0 None 
        1 Upholstered seating 
        2 Cloth covered seating 
        3 Hard-backed seating 

        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.occupancy", 
                                                     self._eco_id, people, 
                                                     percentagefull, seatingtype)
        p2e._app.Exec(arg_str)

    #------------------------------------------------------------------------------ 
    def hvac_operation(self):
        """
        
        Retrieves the current hourly on/off times for the occupancy or HVAC 
        system in the specified zone. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        wkdayon 
        A value between 0 and 23 representing the on hour on a weekday. 
        
        wkdayoff 
        A value between 0 and 23 representing the off hour on a weekday. 
        
        wkendon 
        A value between 0 and 23 representing the on hour on a weekend. 
        
        wkendoff 
        A value between 0 and 23 representing the on hour off a weekend.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.operation", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, int, int, int, int)

    def set_hvac_operation(self, wkday_on, wkday_off, wkend_on, wkend_off):
        """
        
        Sets the current hourly on/off times for the occupancy or HVAC system in 
        the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        wkday_on 
        A value between 0 and 23 representing the on hour on a weekday. 
        
        wkday_off 
        A value between 0 and 23 representing the off hour on a weekday. 
        
        wkend_on 
        A value between 0 and 23 representing the on hour on a weekend. 
        
        wkend_off 
        A value between 0 and 23 representing the on hour off a weekend.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.operation", self._eco_id, 
                                                     wkday_on, wkday_off, 
                                                     wkend_on, wkend_off)
        p2e._app.Exec(arg_str)
    #------------------------------------------------------------------------------ 
    def peak_cooling(self):
        """
        
        Retrieves the specified zone's current value for the peak cooling load 
        (W). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.peakcooling", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_peak_cooling(self, value):
        """
        
        Sets the specified zone's current value for the peak cooling load (W). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the peak cooling load (W). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.peakcooling", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def peak_heating(self):
        """
        
        Retrieves the specified zone's current value for the peak heating 
        load (W). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.peakheating", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_peak_heating(self, value):
        """
        
        Sets the specified zone's current value for the peak heating load (W). 

        Parameter(s)
        This property takes the following parameters.

        value 
        A value representing the peak heating load (W). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.peakheating", self._eco_id, value)
        p2e._app.Exec(arg_str)
        

        
    #------------------------------------------------------------------------------ 
    def temperature_range(self):
        """
        
        Retrieves the minimum, maximum and average temperature of the zone for 
        the last calculated day. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        max 
        The maximum temperature for the day, given in degrees Celcius. 
        
        min 
        The minimum temperature for the day, given in degrees Celcius. 
        
        avg 
        The average temperature over that day, given in degrees Celcius.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.range", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float)
        
    #------------------------------------------------------------------------------ 
    def rel_humidity(self):
        """
        
        Retrieves the specified zone's current value for the design internal 
        relative humidity (%). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.relhumidity", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_rel_humidity(self, value):
        """
        
        Sets the specified zone's current value for the design internal relative 
        humidity (%). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the design internal relative humidity (%). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.relhumidity", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def response_factor(self):
        """
        
        Retrieves the specified zone's current value for the total zone response 
        factor. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.responsefactor", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_response_factor(self, value):
        """
        
        Sets the specified zone's current value for the total zone response 
        factor. 

        Parameter(s)
        There are no parameters for this property.
        
        value 
        A value representing the total zone response factor.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.responsefactor", self._eco_id, value)
        p2e._app.Exec(arg_str)

    #------------------------------------------------------------------------------ 
    def reverb_time(self, octave):
        """
        
        Retrieves the reverberation time for the given zone at the specified 
        octave. This value is only valid after a Statistical Reverberation Time 
        calculation has been performed. 

        Parameter(s)
        This property takes the following parameters.
        
        octave 
        An integer value ranging from 0 to 8, where 0 is 63Hz, 1 is 125Hz, 2 is 
        250Hz right up to 8 which means 16kHz - as shown in the Centre 
        Frequencies table below. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The zone's reverberation time in decimal seconds. 
        
        Relevant Data Table(s)
        
        Octave Frequencies 
        Value Frequency 
        0 63 Hz 
        1 125 Hz 
        2 250 Hz 
        3 500 Hz 
        4 1000 Hz 
        5 2000 Hz 
        6 4000 Hz 
        7 8000 Hz 
        8 16000 Hz 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.reverbtime", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    #------------------------------------------------------------------------------ 
    def schedules(self):
        """
        
        Retrieves the control schedule indexes for zone occupancy, ventilation 
        and internal gain. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        occIndex 
        The zero-based index of the zone's occupancy schedule. 
        
        ventIndex 
        The zero-based index of the zone's infiltration/ventilation schedule. 
        
        gainsIndex 
        The zero-based index of the zone's internal gains schedule.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.schedules", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, int, int, int)

    def set_schedules(self, occIndex, ventIndex, gainsIndex):
        """
        
        Sets the control schedule indexes for zone occupancy, ventilation and 
        internal gain. Each value is a zero based index into the schedule list. 
        You can obtain these indexes from the schedule name using the 
        get.schedule.index command. 

        Parameter(s)
        This property takes the following parameters. 
        
        occIndex 
        A value corresponding to the zero-based index of a schedule.This index 
        is obtainable through the use of the get.schedule.index command. 
        
        ventIndex 
        A value corresponding to the zero-based index of a schedule. This index 
        is obtainable through the use of the get.schedule.index command. 
        
        gainsIndex 
        A value corresponding to the zero-based index of a schedule. This index 
        is obtainable through the use of the get.schedule.index command.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.sensiblegains", 
                                                     self._eco_id, occIndex, 
                                                     ventIndex, gainsIndex)
        p2e._app.Exec(arg_str)

        
    #------------------------------------------------------------------------------ 
    def sensible_gains(self):
        """
        
        Retrieves the specified zone's current value for the sensible internal 
        heat gains (W/m^2). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.sensiblegains", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_sensible_gains(self, value):
        """
        
        Sets the specified zone's current value for the sensible internal heat 
        gains (W/m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the sensible internal heat gains (W/m^2).
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.sensiblegains", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def solar_gains(self):
        """
        
        Retrieves the specified zone's current value for the total direct solar 
        gains through WINDOWS and transparent appertures. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.solargains", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
        
    def set_solar_gains(self, value):
        """
        
        Sets the specified zone's current value for the total direct solar gains 
        through WINDOWS and transparent appertures. 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total direct solar gains through WINDOWS and 
        transparent appertures.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.solargains", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def surface_area(self):
        """
        
        Retrieves the specified zone's current value for the total zone internal 
        surface area (m^2). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the reqested zone data. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.surfacearea", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_surface_area(self, value):
        """
        
        Sets the specified zone's current value for the total zone internal 
        surface area (m^2). 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        A value representing the total zone internal surface area (m^2). 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.surfacearea", self._eco_id, value)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def hvac_system(self):
        """
        
        Retrieves the HVAC system type for the specified zone. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        An integer value corresponding to the following Zone HVAC System Codes 
        table. 
        
        Relevant Data Table(s)
        
        Zone HVAC System Codes 
        Token Value Description 
        none 0 No HVAC or ventilation system. 
        natvent 1 Natural ventilation only. 
        mixedmode 2 Mixed mode HVAC operation. 
        airconditioning 3 Full-time HVAC operation. 
        heating 4 Heating system only. 
        cooling 5 Cooling system only. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.system", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
    
    def set_hvac_system(self, type):
        """
        
        Sets the HVAC system type for the specified zone. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        An integer value or token corresponding to the following Zone HVAC 
        System Codes table. 
        
        Relevant Data Table(s)
        
        Zone HVAC System Codes 
        Token Value Description 
        none 0 No HVAC or ventilation system. 
        natvent 1 Natural ventilation only. 
        mixedmode 2 Mixed mode HVAC operation. 
        airconditioning 3 Full-time HVAC operation. 
        heating 4 Heating system only. 
        cooling 5 Cooling system only. 

        """
        arg_str = p2e._base._util._convert_args_to_string("set.zone.system", self._eco_id, type)
        p2e._app.Exec(arg_str)
        
    #------------------------------------------------------------------------------ 
    def temperature(self, hour):
        """
        
        Retrieves the temperature of the zone at the specified hour. 

        Parameter(s)
        This property takes the following parameters.
        
        hour 
        An integer value between 0 and 23 specifying the hour. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        result 
        The temperature value at the given time in degrees celcius.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.zone.temperature", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
        
    #------------------------------------------------------------------------------ 
    

#==============================================================================
# Zone
#==============================================================================
class Zone(object):
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    class objs(_ZoneRootObjs):
        def __init__(self, _zone):
            self._zone = _zone
            self._eco_id = _zone._eco_id
    class modf(_ZoneRootModf):
        def __init__(self, _zone):
            self._zone = _zone
            self._eco_id = _zone._eco_id  
    class trfm(_ZoneRootTrfm):
        def __init__(self, _zone):
            self._zone = _zone
            self._eco_id = _zone._eco_id           
    class func(_ZoneRootFunc):
        def __init__(self, _zone):
            self._zone = _zone
            self._eco_id = _zone._eco_id  
    class grps(_ZoneRootGrps):
        def __init__(self, _zone):
            self._zone = _zone
            self._eco_id = _zone._eco_id   
    class state(_ZoneRootState):
        def __init__(self, _zone):
            self._zone = _zone
            self._eco_id = _zone._eco_id   
    class prop(_ZoneRootProp):
        def __init__(self, _zone):
            self._zone = _zone
            self._eco_id = _zone._eco_id         

    #--------------------------------------------------------------------------
    #constructor 
    def __init__(self, zone_eco_id):
        
        #update model zones list
        p2e.model._zones.append(self)
        assert self._eco_id == zone_eco_id
        
        #create instances of the nested classes
        self.objs = Zone.objs(self)
        self.modf = Zone.modf(self)
        self.trfm = Zone.trfm(self)
        self.func = Zone.func(self)                        
        self.grps = Zone.grps(self)
        self.state = Zone.state(self)
        self.prop = Zone.prop(self)    
            
        #update model objects list
        self.state.set_current()
        object_id = self.objs.next_object(-1, -1, -1, -1)
        prev_id = object_id
        while (object_id != -1):
            p2e.obj._ObjectRoot(object_id, None)
            object_id = self.objs.next_object(prev_id, -1, -1, -1)
            prev_id = object_id
            
    @staticmethod
    def create(name):
        """
        
        Use this command to create new zones in the model. It returns the 
        zero-based index of the zone just added which you can then use to edit 
        properties. 

        Parameter(s)
        This property takes the following parameters.
        
        name 
        A text string containing the name of the zone to create. If this name 
        already exists, it will be incremented by adding '(X)' to the end, where 
        X is the first unique name. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        zoneIndex 
        The zone object just added. A value of -1 indicates 
        that the operation failed. 
        
        """

        #execute ecotect instruction        
        arg_str = p2e._base._util._convert_args_to_string("add.zone", name)
        val = p2e._app.Request(arg_str)
        eco_id = p2e._base._util._convert_str_to_type(val, int)
        
        #return the zone
        return Zone(eco_id)

    #===========================================================================
    # Properties
    #===========================================================================
    #id property  
    @apply
    def _eco_id():
        def fget(self):
            """
            
            Id of the zone object
        
            """
            return p2e.model._zones.index(self)

        return property(**locals())    

    
