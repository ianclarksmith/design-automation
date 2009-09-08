import py2ecotect as p2e
from exceptions import Exception

#==============================================================================
# _ObjectRootDupl
#==============================================================================
class _ObjectRootDupl(object):
    #-------------------------------------------------------------------------
    def copy(self):
        """
        
        Creates a duplicate copy of the specified object. 

        Parameter(s)
        None
 
        """
        self.copy_move_by_vec((0,0,0))
    #-------------------------------------------------------------------------
    def copy_move(self, start_point=None, end_point=None):
        """
        
        Creates a duplicate copy of the specified object and from one location to another, or in-place.. 

        Parameter(s)
        This command takes the following parameters.
        
        start_point
        The 3-D starting, or base, point of the copy operation.  If omitted, the object is copied in-place. 
        
        end_point
        The 3-D end, or target, point of the copy operation.
 
        """
        if start_point and end_point:
            vector = (end_point[0] - start_point[0], end_point[1] - start_point[1], end_point[2] - start_point[2])
        else:
            vector = (0,0,0)
        self.copy_move_by_vec(vector)
    #-------------------------------------------------------------------------
    def copy_move_by_vec(self, vector):
        """
        
        Creates a duplicate copy of the specified object a distance of x, y and 
        z in each of the major axes. 

        Parameter(s)
        This command takes the following parameters.
        
        vector
        A list of three values that specifies a vector to move the duplicate 
        object in each of the major axes. 
        
        """
        vector = p2e._base._util.scale_1000(vector)
        
        arg_str = p2e._base._util._convert_args_to_string("object.duplicate", 
                                                      self._eco_id, 
                                                      vector[0], 
                                                      vector[1], 
                                                      vector[2])
        p2e._app.Exec(arg_str)
        
        #get the id of the new object
        eco_id = p2e.doc.model.number_of_objects() - 1
        
        #create the object
        return _ObjectRoot(eco_id, None)
    
#==============================================================================
# _ObjectRootTrfm
#==============================================================================
class _ObjectRootTrfm(object):
    #-------------------------------------------------------------------------
    def move(self, start_point, end_point):
        """
        
        This command moves the specified object. 

        Parameter(s)
        This command takes the following parameters.

        start_point
        The 3-D starting, or base, point of the move operation.
        
        end_point
        The 3-D end, or target, point of the copy operation.
        
        """
        vector = (end_point[0] - start_point[0], end_point[1] - start_point[1], end_point[2] - start_point[2])
        self.move_by_vec(vector)

    def move_by_vec(self, vector):
        """
        
        This command moves the specified object. 

        Parameter(s)
        This command takes the following parameters.

        vector
        A list of three values that specifies a vector to move the specified 
        object in each of the major axes.
        
        """
        vector = p2e._base._util.scale_1000(vector)
        
        arg_str = p2e._base._util._convert_args_to_string("object.move",
                                                          self._eco_id, 
                                                          vector[0], 
                                                          vector[1], 
                                                          vector[2])
        p2e._app.Exec(arg_str)
        
    def move_by_centre(self, centre_point):
        """
        
        Sets the centre point for the specified object - the object is moved so 
        that its center is aligned to the point specified. 

        Parameter(s)
        This property takes the following parameters.
        
        centre_point
        A list of three values that represents the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.center", 
                                                          self._eco_id, 
                                                          centre_point[0], 
                                                          centre_point[1], 
                                                          centre_point[2])
        p2e._app.Exec(arg_str)        
    #-------------------------------------------------------------------------
    def nudge(self, dir):
        """
        
        Nudges the specified object in the given axis direction, by the current 
        grid snap distance setting. 

        Parameter(s)
        This command takes the following parameters.
        
        dir 
        A number representing the three major axes as given in the Nudge Direction 
        table. If the value is negative, the direction is in the negative axial 
        direction. 
        
        Relevant Data Table(s)
        
        Nudge Directions 
        Value Description 
        1, -1 In the X axis. 
        2, -2 In the Y axis. 
        3, -3 In the Z axis. 
    
        """
        arg_str = p2e._base._util._convert_args_to_string("object.nudge", self._eco_id, dir)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def rotate(self, azi, alt):
        """
        
        Rotates the specified object about the Transformation Origin (see set.
        model.origin for more information). Normally, polar rotation is done 
        about the y-axis (altitude) first and then the z-axis (aziumuth). 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The azimuth angle of rotation in decimal degrees. 
        
        alt 
        The altitude angle of rotation in decimal degrees.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.rotate", self._eco_id, azi, alt)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def rotate_axis(self, rotation_value):
        """
        
        Rotates the specified object about the Transformation Origin (see set.
        model.origin for more information) along the specified axes. 

        Parameter(s)
        This command takes the following parameters.
        
        rotation_value 
        A list of three values that represent the amount of rotation in decimal 
        degrees for each required axis, in a positive anti-clockwise direction. 
        Use a value of 0 if no rotation is required for a particular axis. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.rotateaxis", 
                                                      self._eco_id, 
                                                      rotation_value[0], 
                                                      rotation_value[1], 
                                                      rotation_value[2])
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def rotate_reverse(self, azi, alt):
        """
        
        Similar to object.rotate, this command rotates the specified object 
        about the Transformation Origin, except in reserve order. This allows a 
        normal polar rotation to be un-done correctly. 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The azimuth angle of rotation in decimal degrees. 
        
        alt 
        The altitude angle of rotation in decimal degrees.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.rotatereverse", 
                                                      self._eco_id, azi, alt)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def scale(self, scale_factor):
        """
        
        This command scales the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        scale_factor
        A list of three scale factors to apply in each of the major axes. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.scale", 
                                                          self._eco_id, 
                                                          scale_factor[0], 
                                                          scale_factor[1], 
                                                          scale_factor[2])
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def spin(self, spin):
        """
        
        Rotates the specified object about its geometric centre, around the axis 
        of its surface normal. 

        Parameter(s)
        This command takes the following parameters.
        
        spin 
        The spin angle given in decimal degrees.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.spin", self._eco_id, spin)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def xform(self, trans, function_values):
        """
        
        Applies a generic transformation to the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        trans 
        The generic tranformation to apply, according to the Tranformation Types 
        table below. 
        
        function_values
        A list of three values that specifies the function of the x y z 
        parameters are determined by the specified trans parameter, as shown in 
        the table above. 
        
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
        #TODO: scale the values by 1000 - but not in all cases
        
        arg_str = p2e._base._util._convert_args_to_string("object.xform", 
                                                          self._eco_id, 
                                                          trans, 
                                                          function_values[0], 
                                                          function_values[1], 
                                                          function_values[2])
        p2e._app.Exec(arg_str)
#==============================================================================
# _ObjectRootModf
#==============================================================================
class _ObjectRootModf(object):
    #-------------------------------------------------------------------------    
    def delete(self):
        """
        
        This command removes the specified object from the model. Note that this 
        will reduce the number of objects in the model so, if you are cycling 
        through all model objects in a loop, make sure you decrement the overall 
        object count accordingly. Alternatively, you could start from the last 
        object and delete backwards through the list. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        
        #get all the nodes in this object
        nodes = self._object.nodes.nodes()
        
        #execute ecotect instruction
        arg_str = p2e._base._util._convert_args_to_string("object.delete", self._eco_id)
        p2e._app.Exec(arg_str)
        
        #update the nodes list
        for i in nodes:
            p2e.doc._nodes.remove(i)
        
        #update model list
        p2e.doc._objects.remove(self._object)    
    #-------------------------------------------------------------------------
    def orient_normal(self, azi, alt):
        """
        
        Orients the surface normals of the specified object to the given azimuth 
        and altitude angles. 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The horizontal angle of orientation, given in degrees. 
        
        alt 
        The vertical angle of orientation, given in degrees. 
  
        """
        arg_str = p2e._base._util._convert_args_to_string("object.orient", self._eco_id, 
                                                     azi, alt)
        p2e._app.Exec(arg_str)        
    #-------------------------------------------------------------------------
    def orient_normal_by_axis(self, axis):
        """
        
        Orients surface normals of the specified object in the 
        given model direction. 

        Parameter(s)
        This command takes the following parameters. 
        
        axis 
        An integer with a value corresponding to the Object Normal Directions 
        table below. 
        
        Relevant Data Table(s)
        
        Object Normal Directions 
        Value Description 
        0 Towards current sun position. 
        1 Towards positive X axis. 
        2 Towards positive Y axis. 
        3 Towards positive Z axis. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.normal", self._eco_id, 
                                                     axis)
        p2e._app.Exec(arg_str)   
    #-------------------------------------------------------------------------
    def reverse_normal(self):
        #Check to see which objects are selected
        selection = p2e.doc.selection
        m = p2e.doc.model
        first_index = selection.next
        index = -1;
        selected_objects = []
        if (first_index == -1): 
            #Only one object is selected. So selection.next() returns -1
            selected_objects.append(p2e.doc._objects[m.Model().current_object])
        else:
            selected_objects.append(p2e.doc._objects[first_index])
            while(True):
                index = selection.next
                if (first_index == index): break
                selected_objects.append(p2e.doc._objects[index])
                
        #Select this object and reverse normal
        self.select()
        selection.reverse()
        
        #Re-select the previous objects
        p2e.doc.select.Select().index(selected_objects)  
#==============================================================================
# 
#==============================================================================
class _ObjectRootState(object):
    #-------------------------------------------------------------------------
    def select(self):
        """
        
        Selects this object. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.select", self._eco_id)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def update(self):
        """
        
        Use this command to check and refresh inter-object relationships for the 
        specified object. Complex model with many inter-relationships can take a 
        little time to regenerate so ECOTECT doesn't do this automatically after 
        each script-based manipulation. You can also use model.update to do this 
        for all objects in the model at once. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.update", self._eco_id)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------  
    def set_current(self):
        """
        
        Several actions within ECOTECT act on the current object (sun-path 
        diagrams, etc). Set this property of an object to ensure that it is the 
        current object before invoking a command. 

        Parameter(s)
        There are no parameters for this property.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.current", self._eco_id)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def is_selected(self):
        """
        
        Retrieves the selection state of the specified object. A value of 1 
        means the object is part of the current selection set, whilst a value of 
        0 means that it is not. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        selected 
        This is a boolean value where 1 represents that the object is selected 
        and 0 that it is not. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.selected", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
    
    def set_selected(self, state = True):
        """
        
        Sets the selection state of the specified object.
        
        Parameter(s)
        This property takes the following parameters.
        
        [state] 
        This optional parameter determines whether to set the object as selected 
        or not. This is a boolean value where 1 or true represents the 
        affirmative and 0 or false the negative. If not given, this parameter 
        defaults to true. Setting an object as selected also sets that object 
        as the current object.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.selected", 
                                                     self._eco_id, state)
        p2e._app.Exec(arg_str)
        
        #Note: Once you finish selecting the individual objects you want, you 
        #should then call the doc.selection.update function. 
        p2e.doc.selection.update()
    #-------------------------------------------------------------------------
    def zone(self):  
        """
        
        Retrieves the zone of the specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        link 
        The zone the specified object is assigned to.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.zone", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e.doc._zones[p2e._base._util._convert_str_to_type(val, int)]
        
    def set_zone(self, zone):
        """
        
        Sets the zone.

        Parameter(s)
        This property takes the following parameters.
        
        zone 
        An instance of the zone class.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.zone", self._eco_id, zone.eco_id())
        p2e._app.Exec(arg_str)
       
#==============================================================================
# 
#==============================================================================
class _ObjectRootMtrl(object):
    #-------------------------------------------------------------------------
    def get_alternate_material(self):
        """
        
        Retrieves the index of the alternate material to the specified object. 
        It is also possible to access all material properties this way. Thus, 
        you could use something like get("object.alternate.absorption", 23) to 
        retrieve data from the alternate material assigned to this object. See 
        the material object for more details. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        altIndex 
        The zero-based index of the assigned alternate material. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.alternate", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
        
    def set_alternate_material(self, material):
        """
        
        Sets the index of the alternate material of the specified object. It is 
        also possible to set any material properties this way. For example, you 
        could use something like set("object.alternate.absorption", 23, 0.57) to 
        set data for the alternate material assigned to this object. See the 
        material object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        This parameter can be given as either a material name or as a number, 
        being the zero-based index of the material to be assigned from within 
        the material list. You can obtain this index manually from the material 
        name using the get.material.index property.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.alternate", self._eco_id, material)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def get_material(self):
        """
        
        Retrieves the index of the object's primary material. It is also 
        possible to access all material properties this way. Thus, you could use 
        something like get("object.material.absorption", 23) to retrieve data 
        from the primary material assigned to this object. See the material 
        object for more details. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        matIndex 
        The zero-based index of the assigned primary material. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.material", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_material(self, material):
        """
        
        Sets the index of the object's primary material. It is also possible to 
        set any material properties this way. For example, you could use 
        something like set("object.material.absorption", 23, 0.57) to set data 
        for the primary material assigned to this object. See the material 
        object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        material 
        Either a material name or an integer, being the zero-based index of the 
        material to be assigned from within the material list. You can obtain 
        this index manually from the material name using the get.material.index 
        command.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.material", self._eco_id, material)
        p2e._app.Exec(arg_str)
#==============================================================================
# 
#==============================================================================
class _ObjectRootEval(object):    
    #-------------------------------------------------------------------------
    def extents(self):
        """
        
        Retrieves the overall size for the specified object, measured in 
        meters. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dx, dy, dz 
        The overall dimensions of the object in each of the X, Y and Z axis. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.extents", self._eco_id)
        val = p2e._app.Request(arg_str)
        size = p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_inverse_1000(size)
    #-------------------------------------------------------------------------
    def evaluate(self, parameters):
        """
        
        This command retrieves coordinates for the nominated point on the face 
        of the specified object. Note that this command only works for planar 
        objects. 

        Parameter(s)
        This property takes the following parameters.
        
        parameters 
        A list of two proportional values that nominate the point to measure in 
        relation to the extents of the specified object. For example, to 
        nominate the centre of the object, the u and v values should be 0.5, 
        whilst the minimum and maximum extents would be of 0.0 and 1.0 
        respectively.
        
        This property always assumes you are looking towards the outside face of 
        the object, where the minimum value is always the bottom-left. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.extents.2dpt", 
                                                     self._eco_id, 
                                                     parameters[0],
                                                     parameters[1])
        val = p2e._app.Request(arg_str)
        point = p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_1000(point)    
    #-------------------------------------------------------------------------
    def evaluate_max(self):
        """
        
        Retrieves the 3D coordinates for the maximum extent of the selected 
        object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the maximum 
        point in 3 dimensional model space.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.extents.max", self._eco_id)
        val = p2e._app.Request(arg_str)
        point = p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_1000(point)
    #-------------------------------------------------------------------------
    def evaluate_min(self):
        """
        
        Retrieves the coordinates for the minimum extent of the selected object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the minimum 
        point in 3 dimensional model space.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.extents.min", self._eco_id)
        val = p2e._app.Request(arg_str)
        point = p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_1000(point)        
    #-------------------------------------------------------------------------
    def area(self):
        """
        
        Retrieves the surface area for the specified object, measured in square 
        metres. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.area", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def panel_area(self):
        """
        
        Retrieves the surface area value overlapping with a WINDOW or DOOR 
        object in an adjacent zone, measured in square metres. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.panelarea", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def exposed_area(self):
        """
        
        This command retrieves the surface area of an object that is exposed to 
        outside conditions. This command only works for planar objects. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.exposure", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
        
    def underground_area(self):  
        """
        
        Gets the surface area that is underground. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.underground", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

        
    #-------------------------------------------------------------------------
    def length(self):
        """
        
        Retrieves the length value for the specified object, measured in 
        millimetres. This command only works on linear objects. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.length", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    
    def centre(self): 
        """
        
        Returns three decimal values corresponding to the X, Y and Z components 
        of geometric centre for the specified object. The values of the object 
        centre are given in absolute world coordinates. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the centre 
        point in 3 dimensional model space. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.center", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float)  
    #-------------------------------------------------------------------------
    def normal(self):
        """
        
        Retrieves the values corresponding to the x, y and z axis components for 
        the normal of the specified object. Note that all surface normals in 
        ECOTECT are normalised such that they are of unit length 
        (ie: length = 1.0). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dx, dy, dz 
        A vector value representing the offset distance in each of the X, Y and 
        Z axis, given in model coordinates, of the object's normal.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.normal", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float)        

    def normal_angle(self, type):
        """
        
        Returns the angle, in degrees, of the surface normal of a planar object. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        What the surface normal angle is measured in relation to, and may be 
        given as a token or value corresponding to the Object Angles table. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        angle 
        The resulting angle in degrees. 
        
        Relevant Data Table(s)
        
        Object Angles 
        Token Value Description 
        azimuth 0 Angle of surface in horizontal plane to positive Y axis. 
        altitude 1 Angle of surface in vertical plane with the ground. 
        sunangle 2 3D angle between surface normal and current sun position. 
        north 3 Angle of surface in horizontal plane to current North Point. 
        eye 4 3D angle between surface normal and current eye position. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.angle", 
                                                     self._eco_id, type)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)      

    def sun_angles(self):
        """
        
        Returns the objects vertical shadow angle (VSA, always assuming it as a 
        vertical surface) and horizontal shadow angle (HSA), given in decimal 
        degrees.

        Note: As these values are always given in relation to the azimuth of the 
        object, the object's tilt angle can be set in relation to this common 
        base. 
        
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        VSA 
        The Vertical Shadow Angle of the object at the current date and time. 
        
        HSA 
        The Horizontal Shadow Angle of the object at the current date and time. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.sunangles", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float)    
#==============================================================================
# _ObjectRootProp
#==============================================================================
class _ObjectRootProp(object):
    #-------------------------------------------------------------------------
    def get_activation(self, day, hour):
        """
        
        Returns the fractional activation value of the specified object for the 
        given day and hour. This will be a value between 0 - 1, where 0 is off 
        and 1 is on. 

        Parameter(s)
        This property takes the following parameters.
        
        day 
        The julian date, given as an integer between 1 and 365. 
        
        hour 
        The hour of the day and must be an integer between 0 and 23, where 0 is 
        midnight on the previous day and 23 is 11:00pm on the given day. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        activation 
        The fractional activation value of the specified object for the given 
        day and hour. This will be a value between 0 - 1, where 0 is off and 1 
        is on.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.activation", 
                                                     self._eco_id, day, hour)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)        
    #-------------------------------------------------------------------------
    def equation(self):
        """
        
        Getting this property returns the values used to calculate the plane 
        equation for the specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        A, B, C, D 
        Four decimal values corresponding to A, B, C and D from the plane 
        equation:
        Ax + By + Cz = D 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.equation", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float, float)

    def recalc_equation(self):
        """
        
        When this property is set, ECOTECT recalculates the plane equation 
        Ax + By + Cz = D for the specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.equation", self._eco_id)
        p2e._app.Exec(arg_str)
    
    #-------------------------------------------------------------------------
    def attr_1(self):
        """
        
        Retrieves the calculated value stored as Attribute Number 1 for the 
        specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.attr1", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_attr_1(self, value):
        """
        
        Sets the calculated value stored as Attribute Number 1 for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.
         
        value 
        The value to assign.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.attr1", self._eco_id, value)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def attr_2(self):
        """
        
        Retrieves the calculated value stored as Attribute Number 2 for the 
        specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.attr2", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_attr_2(self, value):
        """
        
        Sets the calculated value stored as Attribute Number 2 for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        The value to assign.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.attr2", self._eco_id, value)
        p2e._app.Exec(arg_str)      
    #-------------------------------------------------------------------------
    def attr_3(self):
        """
        
        Retrieves the calculated value stored as Attribute Number 3 for the 
        specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.attr3", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_attr_3(self, value):
        """
        
        Sets the calculated value stored as Attribute Number 3 for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.

        value 
        The value to assign.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.attr3", self._eco_id, value)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def element_type(self):
        """
        
        Returns the element type of the specified object, according to the 
        values in the Element Types table. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        type 
        An integer value corresponding to the Element Types table. 
        
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
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.type", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
    
    def set_element_type(self, type):
        """
        
        Sets the specified object as the given element type. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        Either a token or value corresponding to the Element Types table.
        
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
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.type", self._eco_id, type)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def flag(self, flag):
        """
        
        In ECOTECT, objects have a range of boolean flags associated with them 
        that are used at various times. This command retrieves the nominated 
        flag settings for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value representing a binary bit, as shown in the Object Flags 
        table below. To test multiple flags at once, simply add their values 
        together. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        A value representing whether the particular flag is set or not. This is 
        a boolean value where 1 represents the affirmative and 0 the negative. 
        
        Relevant Data Table(s)
        
        Object Flag Codes 
        Value Description Notes 
        1 OBJECT_POINT Object is a single-node point. 
        2 OBJECT_VECTOR Object is a direction vector. 
        4 OBJECT_PLANAR  Object is a flat surface with an equation. 
        8 OBJECT_CLOSED Objects is a closed loop. 
        16 OBJECT_POLYLINE Object defines a virtual polyline. 
        32 OBJECT_EXTRUSION Object is formed from the extrusion of its parent. 
        64 OBJECT_EXTRUDED Object has been extruded. 
        128 OBJECT_COPLANAR Object is linked to another as coplanar. 
        256 OBJECT_INSIDE Object is linked to another as inside it's extents. 
        512 OBJECT_CONCAVE Object is a complex/concave polygon. 
        1024 OBJECT_PARENT Object is the parent of another. 
        2048 OBJECT_CHILD Object is the child of another. 
        4096 OBJECT_ZONE Object defines a model zone. 
        8192 OBJECT_PLANE_EQN* User has specified particular nodes to generate 
        equation. 
        16384 OBJECT_REVERSE Object's surface normal is reversed. 
        32768 OBJECT_SEE_THRU Object is partially transparent. 
        
        *Indicates temporary and volatile markers for internal use only.
     
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.flag", 
                                                     self._eco_id, flag)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_flag(self, flag, state = True):
        """
        
        In ECOTECT, objects have a range of boolean flags associated with them 
        that are used at various times. This command sets the nominated flag 
        settings for the specified object.

        Important Note: Flags are fundamental to how the model works. Be very 
        careful before setting any of them manually, and always operate on files 
        for which you have up-to-date backups. Incorrect usage of flags can 
        corrupt your model beyond repair (ECOTECT probably shouldn't allow these 
        values to be set via a script, however someone will have a valid reason 
        at some stage, and if the user cannot be trusted, who can be trusted?). 
        
        Parameter(s)
        This property takes the following parameters.
        
        flag 
        An integer value representing a binary bit, as shown in the Object Flags 
        table. To set multiple flags at once, add their values together. 
        
        [state] 
        An optional parameter that determines whether to set or reset the 
        flag(s). This is a boolean value where 1 or true represents the 
        affirmative and 0 or false the negative. 
        
        Relevant Data Table(s)
        
        Object Flag Codes 
        Value Description Notes 
        1 OBJECT_POINT Object is a single-node point. 
        2 OBJECT_VECTOR Object is a direction vector. 
        4 OBJECT_PLANAR  Object is a flat surface with an equation. 
        8 OBJECT_CLOSED Objects is a closed loop. 
        16 OBJECT_POLYLINE Object defines a virtual polyline. 
        32 OBJECT_EXTRUSION Object is formed from the extrusion of its parent. 
        64 OBJECT_EXTRUDED Object has been extruded. 
        128 OBJECT_COPLANAR Object is linked to another as coplanar. 
        256 OBJECT_INSIDE Object is linked to another as inside it's extents. 
        512 OBJECT_CONCAVE Object is a complex/concave polygon. 
        1024 OBJECT_PARENT Object is the parent of another. 
        2048 OBJECT_CHILD Object is the child of another. 
        4096 OBJECT_ZONE Object defines a model zone. 
        8192 OBJECT_PLANE_EQN* User has specified particular nodes to generate equation. 
        16384 OBJECT_REVERSE Object's surface normal is reversed. 
        32768 OBJECT_SEE_THRU Object is partially transparent. 

        *Indicates temporary and volatile markers for internal use only.

        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.flag", 
                                                     self._eco_id, flag, state)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def mask(self):
        """
        
        Retrieves the index of the object's shading mask. The shading mask 
        assigned to each object determines when and by how much the object is 
        overshadowed at any particular time. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        mask 
        An integer value between -1 and the value given by get.masks.count - 1, 
        being the zero-based index of the shading mask in the current list.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.mask", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_mask(self, index):
        """
        
        Sets the index of the object's shading mask. The shading mask assigned 
        to each object determines when and by how much the object is 
        overshadowed at any particular time. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        An integer value between -1 and the value given by get.masks.count - 1, 
        being the zero-based index of the shading mask in the current list. 

        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.mask", self._eco_id, index)
        p2e._app.Exec(arg_str)

    #-------------------------------------------------------------------------
    def curve_resolution(self):
        """
        
        Retrieves the current curve resolution to use for virtual polylines, for 
        the specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.resolution", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_curve_resolution(self, value):
        """
        
        Sets the curve resolution to use for virtual polylines, for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        The value to use for the virtual polyline curve resolution.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.node.position", self._eco_id, value)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def schedule(self):
        """
        
        Retrieves the index value for the specified object's activation 
        schedule. The activation schedule determines when and how much an object 
        is turned on or off.

        It is also possible to access all schedule properties this way. Thus, 
        you could use something like get("object.schedule.name", 23) to retrieve 
        data from the schedule assigned to this object. See the schedule object 
        for more details. 
        
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        schIndex 
        The zero-based index of the schedule assigned to this object. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.schedule", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
        
    def set_schedule(self, schedule):
        """
        
        Sets the index value to use for the specified object's activation 
        schedule. The activation schedule determines when and how much an object 
        is turned on or off.

        It is also possible to access all schedule properties this way. Thus, 
        you could use something like set("object.schedule.name", 23, "NightWork") 
        to set data from the schedule assigned to this object. See the schedule 
        object for more details. 
        
        Parameter(s)
        This property takes the following parameters.
        
        schedule 
        Either a schedule name or as the zero-based index of the schedule to be 
        assigned from within the model's schedule list. This index value can be 
        obtained manually from the schedule name, using the get.schedule.index 
        command.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.schedule", self._eco_id, schedule)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def tag(self, tag):
        """
        
        Retrieves information about tags that have been assigned to the 
        specified object. Tags are simply indicators to ECOTECT that the object 
        performs additional functions or is specifically marked for certain 
        calculations. 

        Parameter(s)
        This property takes the following parameters.
        
        tag 
        An integer value representing a binary bit, as shown in the Object Tags 
        table. The value returned for the nominated tag will be a boolean 
        integer value - 0 for off, or 1 for on. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        A value representing whether the particular tag is set or not. This is a 
        boolean value where 1 represents the affirmative and 0 the negative. 
        
        Relevant Data Table(s)
        
        Object Tag Codes Value Description Notes 
        1 TAGGED_PICKED* User clicked near one of it's lines. 
        2 TAGGED_PREVIOUS* Part of the previous selection set. 
        16 TAGGED_SHOWVALUE Object has valid assigned attribute values. 
        32 TAGGED_SHADED Shadows are cast onto this object. 
        64 TAGGED_ERROR Object has violated an inter-object relationship. 
        128 TAGGED_UPDATE Object has changed and needs an update. 
        256 TAGGED_MIRROR Object produces solar reflections. 
        512 TAGGED_ACOUSTIC Object is tagged as an acoustic reflector. 
        4096 TAGGED_3PTS_CONCAVE First 3 nodes are concave. 
        16384 TAGGED_INCOMPLETE Object being created - nodes still being added. 
        32768 TAGGED_MARKER* Generic calculation marker. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.tag", 
                                                     self._eco_id, tag)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_tag(self, tag, state = True):
        """
        
        Sets tags for the specified object. Tags are simply indicators to 
        ECOTECT that the object performs additional functions or is specifically 
        marked for certain calculations. To test multiple tags at once, simply 
        add their values together. The optional [true|false] parameter 
        determines whether set or reset the tag(s), defaulting to true. 

        Parameter(s)
        This property takes the following parameters.
        
        tag 
        An integer value representing a binary bit, as shown in the Object Tags 
        table. To test multiple tags at once, simply add their values together. 
        
        [state] 
        An optional parameter determining whether to set or reset the tag(s). 
        This is a boolean value where 1 or true represents the affirmative and 0 
        or false the negative. If not given, it defaults to true. 
        
        Relevant Data Table(s)
        
        Object Tag Codes 
        Value Description Notes 
        1 TAGGED_PICKED* User clicked near one of it's lines. 
        2 TAGGED_PREVIOUS* Part of the previous selection set. 
        16 TAGGED_SHOWVALUE Object has valid assigned attribute values. 
        32 TAGGED_SHADED Shadows are cast onto this object. 
        64 TAGGED_ERROR Object has violated an inter-object relationship. 
        128 TAGGED_UPDATE Object has changed and needs an update. 
        256 TAGGED_MIRROR Object produces solar reflections. 
        512 TAGGED_ACOUSTIC Object is tagged as an acoustic reflector. 
        4096 TAGGED_3PTS_CONCAVE First 3 nodes are concave. 
        16384 TAGGED_INCOMPLETE Object being created - nodes still being added. 
        32768 TAGGED_MARKER* Generic calculation marker. 


        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.tag", 
                                                     self._eco_id, tag, state)
        p2e._app.Exec(arg_str)
    #-------------------------------------------------------------------------
    def vector(self):
        """
        
        Retrieves the extrusion vector of the specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dx, dy, dz 
        A vector value representing the offset distance in each of the X, Y and 
        Z axis, given in model coordinates, of the object's extrusion vector.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.vector", self._eco_id)
        val = p2e._app.Request(arg_str)
        vector = p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_inverse_1000(vector) 
            
    def set_vector(self, vector):
        """
        
        Sets the extrusion vector of the specified object. 

        Parameter(s)
        This property takes the following parameters. 
        
        vector
        A list of three vector values representing the offset distance in each 
        of the X, Y and Z axis, given in model coordinates. 
        
        """
        vector = p2e._base._util.scale_1000(vector) 
        
        arg_str = p2e._base._util._convert_args_to_string("set.object.vector", 
                                                     self._eco_id, 
                                                     vector[0], 
                                                     vector[1], 
                                                     vector[2])
        p2e._app.Exec(arg_str)
#==============================================================================
# 
#==============================================================================
class _ObjectRootFunc(object):
    #-------------------------------------------------------------------------
    def distance_to_pnt(self, point):
        """
        
        Returns a single floating point value, being the distance between the 
        specified object and the specified 3D point. If this is a POINT object, 
        the distance is the point-to-point distance. If the object is planar, it 
        is the distance of the specified point in line with the plane of the 
        object, even if this point is outside the object's boundaries. 

        Parameter(s)
        This property takes the following parameters.
        
        point
        A list of three values that represents the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dist 
        The distance from the point to the object.
        
        """
        point = p2e._base._util.scale_1000(point)
        
        arg_str = p2e._base._util._convert_args_to_string("get.object.distanceto", 
                                                     self._eco_id, 
                                                     point[0], 
                                                     point[1], 
                                                     point[2])
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def angle_to_pnt(self, point):
        """
        
        Returns the angle in degrees between the surface normal of the specified 
        object and the nominated 3D point. This is effectively the incidence 
        angle of a ray fired towards the geometric centre of the object from the 
        nominated point. If the object is not planar, the angle value returned 
        will be in relation to the positive x axis. 

        Parameter(s)
        This property takes the following parameters.
        
        point
        A list of three values that are the x, y, z coordinates of the point to 
        check in relation to the object. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        angle 
        The incidence angle in degrees. 
        
        """
        point = p2e._base._util.scale_1000(point)
        
        arg_str = p2e._base._util._convert_args_to_string("get.object.incidence", 
                                                     self._eco_id, 
                                                     point[0], 
                                                     point[1], 
                                                     point[2])
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)
    #-------------------------------------------------------------------------
    def intersect(self, start_point, end_point):
        """
        
        Returns the coordinates of the intersection point between a line joining 
        the two nominated points with the plane of the specified object. This 
        command only works with planar objects.

        The intersection point can occur anywhere along the line, both between 
        the points and either side. 
        
        Parameter(s)
        This property takes the following parameters.
        
        start_point
        A list of 3 values of x1, y1, z1 that are the 3D start point of the 
        intersecting line. 
        
        end_point
        A list of 3 values of x2, y2, z2 that are the 3D end point of the 
        intersecting line. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the 
        intersection point in 3 dimensional model space.
        
        """
        start_point = p2e._base._util.scale_1000(start_point)
        end_point = p2e._base._util.scale_1000(end_point)
        
        arg_str = p2e._base._util._convert_args_to_string("get.object.intersect", 
                                                     self._eco_id, 
                                                     start_point[0], 
                                                     start_point[1], 
                                                     start_point[2],
                                                     end_point[0],
                                                     end_point[1], 
                                                     end_point[2])
        val = p2e._app.Request(arg_str)
        point = p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_inverse_1000(point)
    #-------------------------------------------------------------------------
    def reflect_pnt(self, point):
        """
        
        Reflects the nominated 3D point around the plane of the specified object 
        and returns three floating point values representing the x, y and z 
        components of the new point. This command only works for planar objects. 

        Parameter(s)
        This property takes the following parameters.
        
        absolute_position 
        A list of 3 values that represents the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        absolute_position 
        A lost of three values that represent the absolute position in the 
        X, Y and Z axis of the reflected point in 3 dimensional model space.
        
        """
        point = p2e._base._util.scale_1000(point)
        
        arg_str = p2e._base._util._convert_args_to_string("get.object.reflect", 
                                                     self._eco_id, 
                                                     point[0], 
                                                     point[1],
                                                     point[2])
        val = p2e._app.Request(arg_str)
        point = p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_inverse_1000(point)
    #-------------------------------------------------------------------------
    def is_pnt_inside(self, point, checkChildren = True):
        """
        
        Determines if the specified point is within the boundary of the 
        specified object, either 0 for false or 1 for true. This command 
        obviously only works for closed planar objects.

        Note: It is assumed that the specified point is very close to being 
        co-planar with the object. If it lies any signficiant distance away from 
        the surface, invalid results are likely. 
        
        Parameter(s)
        This property takes the following parameters.
        
        point 
        A list of three values that are the coordinates of the point to check 
        in relation to the object. 
        
        [checkChildren] 
        If the specified object contains child objects (such as WINDOWS, DOORS, 
        VOIDS and PANELS), by default the nominated point is checked against 
        these as well. If the point is inside a child object, the result will be 
        false. However, you can set the optional checkChildren parameter to false 
        to avoid this check. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        inside 
        A boolean value where 1 means that the point is inside and 0 means that 
        it isn't. 
        
        """
        point = p2e._base._util.scale_1000(point)
        
        arg_str = p2e._base._util._convert_args_to_string("get.object.inside", 
                                                     self._eco_id, 
                                                     point[0], 
                                                     point[1],
                                                     point[2], 
                                                     checkChildren)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)    

    def is_pnt_coplanar(self, point):
        """
        
        Determines if a point is co-planar with the specified object. Obviously 
        this only works with objects that are closed planar surfaces. 

        Parameter(s)
        This property takes the following parameters.
        
        absolute_position
        A list of three values that represents the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        colanar 
        A boolean value where 1 means that the point is coplanar and 0 means 
        that it isn't. 
        
        """
        point = p2e._base._util.scale_1000(point)
        
        arg_str = p2e._base._util._convert_args_to_string("get.object.coplanar", 
                                                     self._eco_id, 
                                                     point[0], 
                                                     point[1], 
                                                     point[2])
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)    

    def are_pnts_same_side(self, point_1, point_2):
        """
        
        Returns a single integer value, either 0 (false) or 1 (true), depending 
        on whether the two nominated points are on the same side of the 
        specified object's plane equation. This command only works for planar 
        objects. 

        Parameter(s)
        This property takes the following parameters.
        
        point_1
        A list of three values that are the x1 y1 z1 of the first 3D point to 
        use for the comparison. 
        
        point_2
        A list of three values that are the x2 y2 z2 of the second 3D point to 
        use for the comparison. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        same 
        A boolean value where 1 means that the points are on the same side and 0 
        means that they aren't.
        
        """
        point_1 = p2e._base._util.scale_1000(point_1)
        point_2 = p2e._base._util.scale_1000(point_2)
        
        arg_str = p2e._base._util._convert_args_to_string("get.object.sameside", 
                                                     self._eco_id, 
                                                     point_1[0], 
                                                     point_1[1], 
                                                     point_1[2],
                                                     point_2[0], 
                                                     point_2[1], 
                                                     point_2[2])
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    #-------------------------------------------------------------------------
    def extrude(self, vector):
        """
        
        Extrudes the specified object a distance of x, y and z in the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        vector
        A list of three values that specifies a distance to extrude the specified 
        object in each of the major axes.
        
        """
        vector = p2e._base._util.scale_1000(vector)
        
        before_extrude_len = p2e.doc.model.get_num_objects()
        
        arg_str = p2e._base._util._convert_args_to_string("object.extrude", 
                                                          self._eco_id, 
                                                          vector[0]*1000, 
                                                          vector[1]*1000, 
                                                          vector[2]*1000)
        p2e._app.Exec(arg_str)
        
        after_extrude_len = p2e.doc.model.get_num_objects()
        
        for eco_id in range(before_extrude_len, after_extrude_len):
            _ObjectRoot(eco_id, None)
        
    def revolve(self, axis, angle, segs):
        """
        
        Revolves the specified object around the Transformation Origin to create 
        a 3D volume. See the object.rotate command for more information on 
        specifying the Transformation Origin. 

        Parameter(s)
        This command takes the following parameters.
        
        axis 
        The axis for the revolve, and is an integer selected from the Axis table. 
        
        angle 
        The revolve angle, given in degrees from 0 to 360. 
        
        segs 
        The number of angular segments to use for the revolve. The greater the 
        number of segments, the 'smoother' the reolved object. However, this 
        will also increase the geometric complexity of the revolved object. 
        
        Relevant Data Table(s)
        
        Axis Types 
        Value Description 
        0 Around the Z axis. 
        1 Around the X axis. 
        2 Around the Y axis. 
        
        """
        before_extrude_len = p2e.doc.model.get_num_objects()
        
        arg_str = p2e._base._util._convert_args_to_string("object.revolve", self._eco_id, 
                                                     axis, angle, segs)
        p2e._app.Exec(arg_str)
        
        after_extrude_len = p2e.doc.model.get_num_objects()
        
        for eco_id in range(before_extrude_len, after_extrude_len):
            _ObjectRoot(eco_id, None)
    #-------------------------------------------------------------------------
    def initialise_srf_pnts(self, fraction):
        """
        
        Many analysis functions require a range of sample points distributed 
        over an object's surface or along its length. This property allows you 
        to initiate this process for the specified object. The returned value is 
        a single integer value either 0 (false) or 1 (true) depending on whether 
        points were found, which will allow the process to continue. See 
        get.object.pt.rand and get.object.pt.even for more information. 

        Parameter(s)
        This property takes the following parameters.
        
        fraction 
        A multiplier to control the density of points over the object's surface. 
        By default this is configured as a 25x25 grid with a value of 1. Thus, a 
        factor value of 4 would result in a 100x100 grid, while a factor value 
        of 0.2 would result in a 5x5 grid. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        valid 
        A boolean value where 1 represents success and 0 means that the object 
        is unsuitable for this. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.pt.initialise", self._eco_id, fraction)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def are_srf_pnts_even(self):
        """
        
        Retrieves information about how sample points are evenly distributed 
        across an object. Note that this command can only be used after a 
        previous call to get.object.pt.initialise, as this specifies the object 
        to be used and the density of subsequent points.

        Four values are returned - the first three are floating point values 
        representing the x, y and z components of a subsequent point within the 
        object. The fourth value is an integer, corresponding with the Object 
        Point Results table.
        
        This last value must be checked for a value of 0 to denote that the 
        process is complete. 
        
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point on 
        the object surface or length. 
        
        valid 
        A result indicator where 1 represents a valid point, -1 a point that is 
        outside the object and should be ignored, and 0 means the process if 
        complete and all parts of the object checked. 
        
        Relevant Data Table(s)
        Object Point Results 
        Value Description 
        1 A valid point within the object was found. 
        -1 An invalid point outside the object was found. 
        0 Finished - no further points to be found. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.pt.even", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float, int)    

    def are_srf_pnts_random(self):
        """
        
        Retrieves information about how sample points are randomly distributed 
        across an object. Note that this command can only be used after a 
        previous call to get.object.pt.initialise, as this specifies the object 
        to be used and the density of subsequent points.

        Four values are returned - the first three are floating point values 
        representing the x, y and z components of a subsequent point within the 
        object. The fourth value is an integer, corresponding with the following 
        table.
        
        This last value must be checked for a value of 0 to denote that the 
        process is complete. 
        
        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point on 
        the object surface or length. 
        
        valid 
        A result indicator where 1 represents a valid point, -1 a point that is 
        outside the object and should be ignored, and 0 means the process if 
        complete and all parts of the object checked. 
        
        Relevant Data Table(s)
        
        Object Point Results 
        Value Description 
        1 A valid point within the object was found. 
        -1 An invalid point outside the object was found. 
        0 Finished - no further points to be found. 
 
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.pt.random", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float, int)            
#==============================================================================
# 
#==============================================================================
class _ObjectRootNodes(object):
    #-------------------------------------------------------------------------
    def done(self):
        """
        
        Call this method to complete a new object after you have used the add.
        object and add.node commands to generate it. This command tells ECOTECT 
        to check the object's validity, calculate its plane equation and surface 
        area (if required) and exit the interactive add node mode. 

        Parameter(s)
        There are no parameters for this command.
  
        """
        p2e._app.Exec("object.done")    
    #-------------------------------------------------------------------------
    def add_node(self, point):
        #execute ecotect instruction
        node_eco_id = p2e.obj.Node._gen_node(self, self.number_of_nodes -1, point)
        if node_eco_id != -1:
            p2e.obj.Node(self, node_eco_id)
        self.done()
    #-------------------------------------------------------------------------
    def delete_node(self, node, node_index = 0):
        """
        
        The delnode command removes the specified node from the specified object. 

        Parameter(s)
        This command takes the following parameters.

        node 
        The node belonging to the object. 
        
        [node_index]
        The index of the node belonging to the object. It is not the id of the 
        node. Default value is 0.
        
        """
        #execute ecotect instruction
        arg_str = p2e._base._util._convert_args_to_string("object.delnode", self._eco_id, 
                                                     node_index)
        p2e._app.Exec(arg_str)
        
        #Update model lists
        p2e.doc._nodes.remove(node)
    #-------------------------------------------------------------------------
    def first_node(self):
        """
        
        Returns the zero-based absolute index of its first node. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        nodeIndex 
        The zero-based index of the object's first node.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.firstnode", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
        
    #-------------------------------------------------------------------------
    def last_node(self):
        """
        
        Returns the zero-based absolute index of its last node. 

        Parameter(s)
        There are no parameters for this property.
         
        Return Value(s)
        Getting this property returns the following value(s).
        
        nodeIndex 
        The zero-based index of the object's last node. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.lastnode", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)  
    #-------------------------------------------------------------------------
    def nodes(self):
        """
        
        Returns the nodes of this object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        nodes 
        A list of nodes in this object. 
        
        """
        nodes = []
        for node_num in range(self.first_node(), self.last_node()):
            nodes.append(p2e.doc._nodes[node_num])
        return nodes
        
    #-------------------------------------------------------------------------
    def number_of_nodes(self):

        """
        
        Returns the number of nodes in the specified object. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        count 
        The number of nodes in this object. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.node", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
    #-------------------------------------------------------------------------
    
    '''def node_position(self, node):
        """
        
        Retrieves the position of the node in absolute world coordinates for 
        each of the major axes. Three coordinate values are returned. In fact, 
        it is possible to access all node properties this way - see the node 
        object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        node 
        The node in the specified object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the node in 3 
        dimensional model space.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.node.position", 
                                                     self._eco_id, node.eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float)
    #-------------------------------------------------------------------------
    def set_node_position(self, node, absolute_position):
        """
        
        Sets the position of the node in absolute world coordinates for each of 
        the major axes. In fact, it is possible to set all node properties this 
        way - see the node object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        node 
        The node in the specified object to set. 
        
        absolute_position 
        A list of three values that represents the absolute position in the 
        X, Y and Z axis of the node in 3 dimensional model space.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.node.position", 
                                                     self._eco_id, node.eco_id, 
                                                     absolute_position[0],
                                                     absolute_position[1],
                                                     absolute_position[2])
        p2e._app.Exec(arg_str)'''
#==============================================================================
# 
#==============================================================================
class _ObjectRootChild(object):
    #-------------------------------------------------------------------------
    def create_link(self, child):
        """
        
        This command link two objects together to create a parent-child 
        relationship between the two objects. 

        Parameter(s)
        This command takes the following parameters.
        
        child 
        Specifies the object the parent object is linked with.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("object.link", 
                                                          self._eco_id, 
                                                          child._eco_id)
        p2e._app.Exec(arg_str)    
    #-------------------------------------------------------------------------
    def link(self):
        """
        
        Returns the absolute index of the object to which 
        the specified object is linked. If the object is not linked to any other 
        object, it returns a value of -1. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        link 
        The zero-based index of the linked object.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.link", 
                                                     self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)    
    #-------------------------------------------------------------------------
    def get_child_extents(self, absolute = True):
        """
        
        Returns the size and location of a child object within a parent object. 
        For example, if you have a WINDOW object located with an WALL, the first 
        two returned values are the location of the bottom left corner of the 
        WINDOW, and the next two values are the size of the window given as a 
        relative proportion to the size of WALL. Note that this command always 
        assumes you are looking at the outside face of the object, where the 
        minimum extent is always the bottom-left. 

        Parameter(s)
        This property takes the following parameters.
        
        [absolute] 
        This optional parameter, if set to true, will return the size of the 
        child object as absolute values, rather than as a relative proportion 
        to the parent object. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        u 
        The horizontal location of the bottom left hand corner of the child object. 
        
        v 
        The vertical location of the bottom left hand corner of the child object. 
        
        wu 
        The relative width of the child object. 
        
        hv 
        The relative height of the child object. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.object.child.extents", 
                                                     self._eco_id, absolute)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_list(val, float, float, float, float)
    #-------------------------------------------------------------------------
    def set_child_extents(self, u, v, wu, hv):
        """
        
        Sets the size and location of a child object within a parent object. For 
        example, if you have a WINDOW object located with an WALL, the first two 
        returned values are the location of the bottom left corner of the WINDOW, 
        and the next two values are the size of the window given as a relative 
        proportion to the size of WALL.

        Note that this command is intended for use with child objects, which 
        must reside within the bounds of their parent object. Any parameter 
        values greater than 1.0 are assumed to be absolute coordinates, as 
        opposed to a fraction of the parent size. For the same reason, negative 
        parameter values are ignored, with the corresponding dimension remaining 
        unchanged. 
        
        Parameter(s)
        This property takes the following parameters.
        
        u 
        The horizontal location of the bottom left hand corner of the child 
        object. Note that this command always assumes you are looking towards 
        the outside face of the object, where the minimum extents is always the 
        bottom-left. 
        
        v 
        The vertical location of the bottom left hand corner of the child object. 
        Note that this command always assumes you are looking towards the outside 
        face of the object, where the minimum extents is always the bottom-left. 
        
        wu 
        The width of the child object, as a relative proportion to the size of 
        the parent object. For example, a value of 0.5 would make the width of 
        the child object half the size of the parent object. 
        
        hv 
        The height of the child object, as a relative proportion to the size of 
        the parent object. For example, a value of 0.75 would make the height of 
        the child object 3/4 the size of the parent object.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.object.child.extents", 
                                                     self._eco_id, u, v, wu, hv)
        p2e._app.Exec(arg_str)

#==============================================================================
# _ObjectRoot
#==============================================================================
class _ObjectRoot(object):
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    class child(_ObjectRootChild):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class func(_ObjectRootFunc):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class modf(_ObjectRootModf):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class mtrl(_ObjectRootMtrl):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class nodes(_ObjectRootNodes):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class eval(_ObjectRootEval):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id     
    class prop(_ObjectRootProp):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class state(_ObjectRootState):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class trfm(_ObjectRootTrfm):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    class dupl(_ObjectRootDupl):
        def __init__(self, _object):
            self._object = _object
            self._eco_id = _object._eco_id
    #--------------------------------------------------------------------------
    #constructor
    def __init__(self, object_eco_id, points):
        
        if object_eco_id == -1 or object_eco_id == None:
            raise Exception
        
        #update model lists
        p2e.doc._objects.append(self)  
        
        #create instances of the nested classes
        self.child = _ObjectRoot.child(self)
        self.func = _ObjectRoot.func(self)
        self.modf = _ObjectRoot.modf(self)
        self.mtrl = _ObjectRoot.mtrl(self)
        self.nodes = _ObjectRoot.nodes(self)
        self.eval = _ObjectRoot.eval(self)        
        self.prop = _ObjectRoot.prop(self)
        self.state = _ObjectRoot.state(self)
        self.trfm = _ObjectRoot.trfm(self)
        self.dupl = _ObjectRoot.dupl(self)        
        
        if points == None:
            #add exisiting nodes
            for node_num in range(self.nodes.first_node(), self.nodes.last_node()):
                p2e.obj.Node(self, node_num) 
                
        else:
            #add new nodes
            for node_num in range(len(points)):
                #execute ecotect instruction
                node_eco_id = p2e.obj.Node._gen_node(self, node_num, points[node_num])
                if node_eco_id != -1:
                    p2e.obj.Node(self, node_eco_id)
                else:
                    pass
                    #raise Exception
            self.nodes.done() 

    #--------------------------------------------------------------------------
    #factory method   
    @classmethod
    def _gen_object(cls, elemType, objType, selected = True, link = 0):  
        """
        
        Use this command to create new objects in the model. It returns the 
        zero-based index of the object just added which you can then use to 
        add nodes. 

        Parameter(s)
        This property takes the following parameters.
        
        elemType 
        The element type of the new object and may be given as either a token 
        or value as shown in the Element Types table below. 
        
        objType 
        The type of object to be created and may be given as either a token or 
        value corresponding with the following Object Types table. 
        
        [selected] 
        This optional parameter determines whether the newly created object is 
        set as selected. This is a boolean value where 1 or true represents the 
        affirmative and 0 or false the negative. If not specified, this 
        parameter defaults to true. 
        
        [link] 
        If the objtype is set to child, this optional parameter specifies what 
        type of object the child is linked with. The [link] value can be 
        selected from the same table for the elemType parameter. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        objectIndex 
        The zero-based index of the object just added. A value of -1 indicates 
        that the operation failed. 
        
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
        
        
        Object Type Codes 
        Token  Value  
        point 1 
        vector 2 
        plane 12 
        wall 32 
        zone 4140 
        source 3 
        child 2444 

        """
        
        #execute ecotect instruction
        arg_str = p2e._base._util._convert_args_to_string("add.object", elemType, 
                                                     objType, selected, link)
        val = p2e._app.Request(arg_str)
        eco_id = p2e._base._util._convert_str_to_type(val, int)

        return eco_id
    
    #--------------------------------------------------------------------------
    #id property  
    @apply
    def _eco_id():
        def fget(self):
            """
            
            Id of the object
        
            """
            return p2e.doc._objects.index(self)

        return property(**locals())    
#==============================================================================
# 
#==============================================================================

class Point(_ObjectRoot):

    
    @staticmethod
    def create(points):
        """
        
        Use this function to create new point objects in the model. It returns 
        the point object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the point.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The point object just added. None is returned if the operation 
        failed. 
        
        """        
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Point._gen_object("point", "point")
        if id == -1: return None
        return Point(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Line(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new line objects in the model. It returns 
        the line object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the line.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The line object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Line._gen_object("line", "plane")
        if id == -1: return None
        return Line(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Roof(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new roof objects in the model. It returns 
        the roof object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the roof.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The roof object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
            
        eco_id = Roof._gen_object("roof", "plane")
        if id == -1: return None
        return Roof(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Floor(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new fllor objects in the model. It returns 
        the floor object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the floor.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The floor object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Floor._gen_object("floor", "plane")
        if id == -1: return None
        return Floor(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Ceiling(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new ceiling objects in the model. It returns 
        the ceiling object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the ceiling.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The ceiling object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Ceiling._gen_object("ceiling", "plane")
        if id == -1: return None
        return Ceiling(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Wall(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new wall objects in the model. It returns the 
        wall object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the wall.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The wall object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Wall._gen_object("wall", "plane")
        if id == -1: return None
        return Wall(eco_id, points)

#==============================================================================
# 
#==============================================================================

class Partition(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new partition objects in the model. It 
        returns the partition object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the partition.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The partition object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Partition._gen_object("partition", "plane")
        if id == -1: return None
        return Partition(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Void(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new void objects in the model. It returns 
        the void object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the void.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The void object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Void._gen_object("void", "plane")
        if id == -1: return None
        return Void(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Window(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new window objects in the model. It returns 
        the window object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the window.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The window object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Window._gen_object("window", "plane")
        if id == -1: return None
        return Window(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Panel(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new panel objects in the model. It returns 
        the panel object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the panel.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The panel object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Panel._gen_object("panel", "plane")
        if id == -1: return None
        return Panel(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Door(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new door objects in the model. It returns 
        the door object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the door.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The door object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Door._gen_object("door", "plane")
        if id == -1: return None
        return Door(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Speaker(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new speaker objects in the model. It returns 
        the speaker object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the speaker.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The speaker object just added. None is returned if the operation 
        failed. 
        
        """        
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Speaker._gen_object("speaker", "source")
        if id == -1: return None
        return Speaker(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Light(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new light objects in the model. It returns 
        the light object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the light.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The light object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Light._gen_object("light", "source")
        if id == -1: return None
        return Light(eco_id, points)
#==============================================================================
# 
#==============================================================================

class Appliance(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new appliance objects in the model. It 
        returns the appliance object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the appliance.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The appliance object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Appliance._gen_object("appliance", "vector")
        if id == -1: return None
        return Appliance(eco_id, points)
#==============================================================================
# 
#==============================================================================

class SolarCollector(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new solarcollector objects in the model. 
        It returns the solarcollector object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the solarcollector.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The solarcollector object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = SolarCollector._gen_object("solarcollector", "vector")
        if id == -1: return None
        return SolarCollector(eco_id, points)
#==============================================================================
# Camers
#==============================================================================

class Camera(_ObjectRoot):

    @staticmethod
    def create(points):
        """
        
        Use this function to create new camera objects in the model. It returns 
        the camera object just added. 

        Parameter(s)
        This function takes the following parameters.
        
        points 
        The ordered list of points that define the camera.
        
        Return Value(s)
        This function returns the following value(s).
        
        object 
        The camera object just added. None is returned if the operation 
        failed. 
        
        """
        points = p2e._base._util.scale_1000(points)
        
        eco_id = Camera._gen_object("camera", "vector")
        if id == -1: return None
        return Camera(eco_id, points)


#==============================================================================
# _NodeRootTrfm
#==============================================================================
class _NodeRootTrfm(object):
    def move_by_vec(self, vector):
        """
        
        Moves the specified node in the last selected object. 

        Parameter(s)
        This command takes the following parameters.
        
        vector
        A list of three values that specify the move distance and direction in 
        each of the major X, Y and Z axis.
        
        """
        vector = p2e._base._util.scale_1000(vector)
        
        arg_str = p2e._base._util._convert_args_to_string("node.move", self._eco_id, 
                                                      vector[0], 
                                                      vector[1], 
                                                      vector[2])
        p2e._app.Exec(arg_str)

    def nudge(self, dir):
        """
        
        Nudges the specified node in the last selected object, by the current grid snap distance. 

        Parameter(s)
        This command takes the following parameters.
        
        dir 
        The nudge direction, according to the table below. 
        
        Relevant Data Table(s)
        
        Nudge Directions 
        Value Description 
        1, -1 In the X axis. 
        2, -2 In the Y axis. 
        3, -3 In the Z axis. 

        """
        arg_str = p2e._base._util._convert_args_to_string("node.nudge", self._eco_id, dir)
        p2e._app.Exec(arg_str)

    def rotate(self, azi, alt):
        """
        
        Rotates the specified node in the last created object about the 
        Transformation Origin (see set.model.origin for more information). 
        Normally, polar rotation is done about the y-axis (altitude) first and 
        then the z-axis (aziumuth). 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The azimuth angle of rotation, in decimal degrees. 
        
        alt 
        The altitude angle of rotation, in decimal degrees. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("node.rotate", self._eco_id, 
                                                      azi, alt)
        p2e._app.Exec(arg_str)

    def rotate_axis(self, rotation_value):
        """
        
        Rotates the specified node in the last created object about the 
        Transformation Origin (see set.model.origin for more information) along 
        the specified axes. 

        Parameter(s)
        This command takes the following parameters.
        
        rotation_value
        A list of three values that specify the amount of rotation in decimal 
        degrees for each required axis, in a positive anti-clockwise direction. 
        Use a value of 0 if no rotation is required for a particular axis.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("node.rotateaxis", 
                                                      self._eco_id,
                                                      rotation_value[0], 
                                                      rotation_value[1], 
                                                      rotation_value[2])
        p2e._app.Exec(arg_str)

    def rotate_reverse(self, azi, alt):
        """
        
        Similar to node.rotate, this command rotates the specified node in the 
        last created object about the Transformation Origin, except in reserve 
        order. This allows a normal polar rotation to be un-done correctly. 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The azimuth angle of rotation, in decimal degrees. 
        
        alt 
        The altitude angle of rotation, in decimal degrees. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("node.rotatereverse", 
                                                      self._eco_id, azi, alt)
        p2e._app.Exec(arg_str)

    def scale(self, scale_factors):
        """
        
        Scale the specified node in the last selected object. 

        Parameter(s)
        This command takes the following parameters.
        
        scale_factors 
        A list of three values that specifies the scale factor to apply in each 
        of the major X, Y and Z axis.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("node.scale", self._eco_id,
                                                      scale_factors[0], 
                                                      scale_factors[1], 
                                                      scale_factors[2])
        p2e._app.Exec(arg_str)
        
    def xform(self, transformation, function_values):
        """
        
        Applies a generic transformation to the specified node in the last 
        selected object. 

        Parameter(s)
        This command takes the following parameters.
        
        trans 
        The generic tranformation to apply, according to the Transform Types 
        table below. 
        
        function_values 
        A list of three values that specify the function determined by the 
        specified trans parameter, as shown in the table below. 
        
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
        #TODO: scale by 1000
        
        arg_str = p2e._base._util._convert_args_to_string("node.xform", 
                                                      self._eco_id, transformation,
                                                      function_values[0],
                                                      function_values[1],
                                                      function_values[2])
        p2e._app.Exec(arg_str)
#==============================================================================
# _NodeRootProp
#==============================================================================
class _NodeRootProp(object):
    def link(self):
        """
        
        Gets the node or object this node is linked to. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        link 
        The zero-based index of the object or node to which the specified node 
        is linked.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.node.link", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_link(self, link):
        """
        
        Sets the node or object this node is linked to.

        Parameter(s)
        This property takes the following parameters.
        
        link 
        The object or node to which the specified node is to be linked.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.node.link", self._eco_id, link._eco_id)
        p2e._app.Exec(arg_str)
        

    def flag(self, flag):
        """
        
        Gets the state of individual node flags. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        Refer to the table below. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        The boolean state of the selected bitwise flag. If set, the value is 1, 
        if not it is 0. The table below gives the bitwise values of each 
        available node flag. 
        
        Relevant Data Table(s)
        
        Available Attribute Flags 
        Token Value Description 
        text 1 Display object attribute as a text value 
        vectors 2 Display object attribute as a vector. 
        colours 4 Display object attribute as a fill colous. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.node.flag", self._eco_id, 
                                                      flag)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
        
    def set_flag(self, flag, state = True):
        """
        
        Sets individual flags that control the display of attribute values. 

        Parameter(s)
        This property takes the following parameters.
        
        flag 
        This parameter specifies the bitwise flag to be set or cleared. 
        
        [state] 
        This parameter determines whether the flag is to be set or cleared. This 
        is a boolean value where 1 or true represents the affirmative and 0 or 
        false the negative. If not included, it defaults to true. 
        
        Relevant Data Table(s)
        
        Available Attribute Flags 
        Token Value Description 
        text 1 Display object attribute as a text value 
        vectors 2 Display object attribute as a vector. 
        colours 4 Display object attribute as a fill colous. 

        """
        arg_str = p2e._base._util._convert_args_to_string("set.node.flag", self._eco_id,
                                                       flag, state) 
        p2e._app.Exec(arg_str)
    

    def flags(self):
        """
        
        Retrieves a value representing the total of all the node's flags. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        flags 
        The bitwise total of all the flags currently set. The table below gives 
        the bitwise values of each available node flag. 
        
        Relevant Data Table(s)
        table_NodeFlags.txt
      
        """
        arg_str = p2e._base._util._convert_args_to_string("get.node.flags", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)
        

    def type(self):
        """
        
        Retrieves the node type for the specified node in the last created 
        object, according to the following Node Types table. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        type 
        The type of node, according to the following Node Types table. 
        
        Relevant Data Table(s)
        
        Node Types 
        Token Value Description 
        editable 0 An editable unlinked node (default) 
        constrained 1 Constrained to parent extrusion vector. 
        linked 2 Linked to another node by current offset. 
        locked 3 Locked in place. 
        bound 4 Bound to the position of linked node. 
        fillet 5 Control node for a virtual fillet. 
        arc 6 Control node for a virtual arc. 
        bezier 7 Control node for a virtual 3pt bezier spline. 
        spline 8 Control node for a virtual spline curve. 
  
        """
        arg_str = p2e._base._util._convert_args_to_string("get.node.type", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_type(self, type, link = -1):
        """
        
        Sets the node type for the specified node in the last created object. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        Sets the type of node, according to the following Node Types table. 
        
        [link] 
        This optional parameter may be given if the set node type is such that 
        it establishes a link between this node and another object. 
        
        Relevant Data Table(s)
        
        Node Types 
        Token Value Description 
        editable 0 An editable unlinked node (default) 
        constrained 1 Constrained to parent extrusion vector. 
        linked 2 Linked to another node by current offset. 
        locked 3 Locked in place. 
        bound 4 Bound to the position of linked node. 
        fillet 5 Control node for a virtual fillet. 
        arc 6 Control node for a virtual arc. 
        bezier 7 Control node for a virtual 3pt bezier spline. 
        spline 8 Control node for a virtual spline curve. 

        """
        if type == 2 and  link != -1:
            return
        else:
            arg_str = p2e._base._util._convert_args_to_string("set.node.type", 
                                                          self._eco_id, type, link)
            p2e._app.Exec(arg_str)
   
    def modifier(self):
        """
        Gets the node modifier value. This is decimal value whose use depends on 
        the inter-node relationships to which this node is a party. Typically it 
        stores the relative offset along the extrusion vector when it is part of 
        an object created from the extrusion of a parent. For non-linked object, 
        you are free to use it for anything you wish. 

        Parameter(s)
        There are no parameters for this property.
         
        Return Value(s)
        Getting this property returns the following value(s).
        
        mod 
        The decimal value of the node modifier.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.node.modifier", 
                                                      self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, float)

    def set_modifier(self, mod):
        """
        
        Sets the node modifier value. This is decimal value whose use depends on 
        the inter-node relationships to which this node is a party. Typically it 
        stores the relative offset along the extrusion vector when it is part of 
        an object created from the extrusion of a parent. For non-linked object, 
        you are free to use it for anything you wish. 

        Parameter(s)
        There are no parameters for this property.
        
        mod 
        The new decimal value of the node modifier.
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.node.modifier", 
                                                      self._eco_id, mod)
        p2e._app.Exec(arg_str)
        

    

    def position(self):
        """
        
        Retrieves the position of the node in absolute world coordinates in each 
        of the major axes. Three coordinate values are returned. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the node in 3 
        dimensional model space. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("get.node.position", self._eco_id)
        val = p2e._app.Request(arg_str)
        
        absolute_position =  p2e._base._util._convert_str_to_list(val, float, float, float)
        return p2e._base._util.scale_inverse_1000(absolute_position)

    def set_position(self, point):
        """
        
        Sets the position of the node in absolute world coordinates in each of 
        the major axes. 

        Parameter(s)
        This property takes the following parameters.
        
        point 
        A list of three values that represents the absolute position in the 
        X, Y and Z axis of the node in 3 dimensional model space.
        
        """
        point = p2e._base._util.scale_1000(point)
        
        arg_str = p2e._base._util._convert_args_to_string("set.node.position", 
                                                      self._eco_id, 
                                                      point[0], 
                                                      point[1], 
                                                      point[2])
        p2e._app.Exec(arg_str)
            

    
#==============================================================================
# _NodeRootState
#==============================================================================
class _NodeRootState(object):
    def selected(self):
        """
        
        Retrieves the selection state of the specified node. 

        Parameter(s)
        There are no parameters for this property.
         
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        If this value is 1, then the node is selected. If 0 the node is not selected. 

        """
        arg_str = p2e._base._util._convert_args_to_string("get.node.selected", self._eco_id)
        val = p2e._app.Request(arg_str)
        return p2e._base._util._convert_str_to_type(val, int)

    def set_selected(self, state = 1):
        """
        
        Sets the selection state of the specified node. 

        Parameter(s)
        This property takes the following parameters.
        
        [state] 
        Determines whether to select or deselect the specified node. This can be 
        given as either the words true or false or also as boolean integers 1 or 
        0. If not given, this parameter defaults to true. 
        
        """
        arg_str = p2e._base._util._convert_args_to_string("set.node.selected", self._eco_id, state)
        p2e._app.Exec(arg_str)
        
#==============================================================================
# _NodeRootModf
#==============================================================================
class _NodeRootModf(object):
    def delete(self, node_index = 0):
        
        """
        
        The delete function removes the specified node from its object. 

        Parameter(s)
        This command takes the following parameters.
        
        [node_index]
        The index of the node belonging to the object. It is not the id of the 
        node. Default value is 0.
        
        """
        #execute ecotect instruction
        arg_str = p2e._base._util._convert_args_to_string("object.delnode", 
                                            self._object._eco_id, node_index)
        p2e._app.Exec(arg_str)
        
        #Update node lists
        p2e.doc._nodes.remove(self)
        
        #set object to none
        self._object.done()
        self._object = None
#==============================================================================
# Node
#==============================================================================
class Node(object):
    _object = None
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    class trfm(_NodeRootTrfm):
        def __init__(self, _eco_id):self._eco_id = _eco_id    
    class prop(_NodeRootProp):
        def __init__(self, _eco_id):self._eco_id = _eco_id    
    class state(_NodeRootState):
        def __init__(self, _eco_id):self._eco_id = _eco_id           
    class modf(_NodeRootModf):
        def __init__(self, _eco_id):self._eco_id = _eco_id    
                  
    #--------------------------------------------------------------------------
    #constructor 
    def __init__(self, obj, node_eco_id):
        
        #create instances of the nested classes
        self.trfm = Node.trfm(node_eco_id)
        self.prop = Node.prop(node_eco_id)
        self.state = Node.state(node_eco_id)        
        self.modf = Node.modf(node_eco_id)        
        
        #create the node
        self._object = obj
        
        #update model nodes lists
        p2e.doc._nodes.append(self)
        assert self._eco_id == node_eco_id
    #--------------------------------------------------------------------------
    #factory method   
    @classmethod
    def _gen_node(cls, object, index, point, nodeType = 0, link = 0):
        """
        
        Use this command to create new nodes in the model. It returns the 
        zero-based index of the node just added which you can then use to edit 
        properties. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The integer index of the object to add the new node to. 
        
        index 
        The integer index of the node at which to add, given in the range 0 to 
        the number of nodes already in the object. If an index less than the 
        number of nodes in the object is given, the node is inserted at the 
        given index and all nodes at a greater index are incremented up by one. 
        
        points
        A list of three values that represents the absolute position in the 
        X, Y and Z axis of a point in 3 dimensional model space. 
        
        [nodeType] 
        Sets the type of node, according to the following Node Types table. 
        
        [link] 
        The zero-based index of the object or node to which the specified node 
        is to be linked. 
        
        Relevant Data Table(s)
        
        Node Types 
        Token Value Description 
        editable 0 An editable unlinked node (default) 
        constrained 1 Constrained to parent extrusion vector. 
        linked 2 Linked to another node by current offset. 
        locked 3 Locked in place. 
        bound 4 Bound to the position of linked node. 
        fillet 5 Control node for a virtual fillet. 
        arc 6 Control node for a virtual arc. 
        bezier 7 Control node for a virtual 3pt bezier spline. 
        spline 8 Control node for a virtual spline curve. 
        
        """

        #execute ecotect instruction
        arg_str = p2e._base._util._convert_args_to_string("add.node", object._eco_id, index, 
                                                     point[0], 
                                                     point[1], 
                                                     point[2], 
                                                     nodeType, link)
        val = p2e._app.Request(arg_str)
        eco_id = p2e._base._util._convert_str_to_type(val, int)
        
        return eco_id
    #--------------------------------------------------------------------------
    #id property       
    @apply
    def _eco_id():
        def fget(self):
            """
            
            Id of the node object
            
            """
            return p2e.doc._nodes.index(self)
        
        return property(**locals())
#==============================================================================
# The End
#==============================================================================