import py2ecotect
from py2ecotect import string_util

class Selection(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def delete(self):
        """
        
        Deletes the currently selected object(s) from the model. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.delete")
    
    def duplicate(self, dx, dy, dz):
        """
        
        Creates a duplicate copy of currently selected object(s). 

        Parameter(s)
        This command takes the following parameters.
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates, where the duplicate will be placed. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.duplicate", dx, 
                                                      dy, dz)
        py2ecotect.conversation.Exec(arg_str)
        
    def equation(self):
        """
        
        Recalculates the plane equations and surface areas of currently selected 
        object(s). 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.equation")
    
    def extrude(self, dx, dy, dz):
        """
        
        Extrudes currently selected object(s). 

        Parameter(s)
        This command takes the following parameters.
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.extrude", dx, 
                                                      dy, dz)
        py2ecotect.conversation.Exec(arg_str)
    
    def group(self):
        """
        
        Establishes a group for the currently selected object(s). 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.group")
    
    def link(self):
        """
        
        Creates inter-object relationship links between the currently selected 
        objects. Such as establishing OBJECT_INSIDE and OBJECT_PLANAR links for 
        WINDOWS objects inside WALL objects. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.link")
    
    def move(self, dx, dy, dz):
        """
        
        Moves the currently selected object(s). 

        Parameter(s)
        This command takes the following parameters.
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.move", dx, dy, 
                                                      dz)
        py2ecotect.conversation.Exec(arg_str)
    
    def normal(self, type):
        """
        
        Orients the surface normals of all currently selected objects in the specified direction. 

        Parameter(s)
        This command takes the following parameters.
        
        type 
        An integer value corresponding to the following Object Normals table. 
        Relevant Data Table(s)
        Object Normal Directions Value Description 
        0 Towards current sun position. 
        1 Towards positive X axis. 
        2 Towards positive Y axis. 
        3 Towards positive Z axis. 

        """
        arg_str = string_util._convert_args_to_string("selection.normal", type)
        py2ecotect.conversation.Exec(arg_str)
    
    def nudge(self, dir):
        """
        
        Nudges the currently selected objects along the given axis direction. 

        Parameter(s)
        This command takes the following parameters.
        
        dir 
        An integer value corresponding to the Nudge Direction table below. 
        Relevant Data Table(s)
        Nudge Directions Value Description 
        1, -1 In the X axis. 
        2, -2 In the Y axis. 
        3, -3 In the Z axis. 

        """
        arg_str = string_util._convert_args_to_string("selection.nudge", dir)
        py2ecotect.conversation.Exec(arg_str)
    
    def orient(self, azi, alt):
        """
        
        Orients the surface normals of all currently selected objects to the 
        given azimuth and altitude angles. 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The azimuth angle in degrees. 
        
        alt 
        The altitude angle in degrees. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.nudge", 
                                                      azi, alt)
        py2ecotect.conversation.Exec(arg_str)
        
    def reverse(self):
        """
        
        Reverses the surface normals of the currently selected object(s). 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("selection.reverse")
        
    def revolve(self, axis, angle, segs):
        """
        
        Revolves objects around axis , angle degrees, in segs segments. 

        Parameter(s)
        This command takes the following parameters.
        
        axis 
        An integer corresponding to the Axis table below. 
        angle 
        The angle of rotation in degrees. 
        segs 
        The number of segments to rotate by. 
        Relevant Data Table(s)
        Axis Types Value Description 
        0 Around the Z axis. 
        1 Around the X axis. 
        2 Around the Y axis. 

        """
        arg_str = string_util._convert_args_to_string("selection.revolve", 
                                                      axis, angle, segs)
        py2ecotect.conversation.Exec(arg_str)
    
    def rotate(self, azi, alt):
        """
        
        Rotates the currently selected object(s) about the Transformation 
        Origin (see set.model.origin for more information). This is done about 
        the Y axis first (altitude) and then the Z axis (aziumuth). You can 
        also use the app.cmd command to set the Transformation Origin about 
        which the rotation will occur. 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The aziumuth angle in degrees. 
        
        alt 
        The altitude angle in degrees. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.rotate", 
                                                      azi, alt)
        py2ecotect.conversation.Exec(arg_str)
    
    def rotateaxis(self, x, y, z):
        """
        
        Rotates the selected object(s) by the given angles in each axis. 

        Parameter(s)
        This command takes the following parameters.
        
        x 
        The angle to rotate around the X-Axis, in decimal degrees. 
        
        y 
        The angle to rotate around the Y-Axis, in decimal degrees. 
        
        z 
        The angle to rotate around the Z-Axis, in decimal degrees.
        
        """
        arg_str = string_util._convert_args_to_string("selection.rotateaxis", x, 
                                                      y, z)
        py2ecotect.conversation.Exec(arg_str)
    
    def rotatereverse(self, azi, alt):
        """
        
        Rotates the currently selected object(s) about the Transformation 
        Origin (see set.model.origin for more information), but in reverse 
        order. This is necessary to properly undo a normal polar rotation. 

        Parameter(s)
        This command takes the following parameters.
        
        azi 
        The aziumuth angle in degrees. 
        
        alt 
        The altitude angle in degrees. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.rotatereverse", 
                                                      azi, alt)
        py2ecotect.conversation.Exec(arg_str)
    
    def scale(self, dx, dy, dz):
        """
        
        Scales currently selected objects by a factor of dx, dy and dz in the 
        major axes. See the selection.rotate command for information on 
        specifying the Transformation Origin. 

        Parameter(s)
        This command takes the following parameters.
        
        dx 
        The scaling factor along the X-Axis. 
        
        dy 
        The scaling factor along the Y-Axis. 
        
        dz 
        The scaling factor along the Z-Axis. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.scale", dx, dy, 
                                                      dz)
        py2ecotect.conversation.Exec(arg_str)
    
    def spin(self, angle):
        """
        
        Rotates each selected object about its geometric centre, being the axis 
        of its surface normal. 

        Parameter(s)
        This command takes the following parameters.
        
        angle 
        The angle of rotation in degrees. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.spin", angle)
        py2ecotect.conversation.Exec(arg_str)
    
    def ungroup(self):
        """
        
        Removes the group status for the currently selected object(s). 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("selection.ungroup")
    
    def unlink(self):
        """
        
        Removes any inter-object relationships from all currently selected objects. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("selection.unlink")
    
    def update(self):
        """
        
        Updates the Selection Information panel. There are several ways to 
        select objects using script commands in ECOTECT. For example, the 
        selection commands are used to grab many objects in one call, so it is 
        logical for ECOTECT to automatically update the Selection Information 
        panel whenever one of these commands is used. However, when the 
        set.object.selected command is used to select/deselect individual 
        objects, this may be applied to several hundred objects in a large 
        model, which would mean that updating the Selection Information panel 
        at the end of each action would result in an unneccesary reduction in 
        the speed of the script. Thus, the Selection Information panel is not 
        updated when the selection status of individual objects is changed, so 
        you should use the selection.update command when you have completed 
        your selection. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.update")
    
    def xform(self, trans, x, y, z):
        """
        
        Apply a generic transform to the selected object(s) in the model. 

        Parameter(s)
        This command takes the following parameters.
        
        trans 
        The transformation to use, given as a token corresponding to the 
        following Transformation Types table. 
        
        x, y, z 
        Coordinate values specified by the table below. 
        
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
        arg_str = string_util._convert_args_to_string("selection.xform", trans, 
                                                      x, y, z)
        py2ecotect.conversation.Exec(arg_str)
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_alternate(self):
        """
        
        Retrieves the alternate material index of all currently selected 
        objects. A negative result indicates that the alternate material varies 
        within the selection. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the alternate material assigned
        
        """
        val = py2ecotect.conversation.Request("get.selection.alternate")
        return string_util._convert_str_to_type(val, int)
        
    def set_alternate(self, index):
        """
        
        Sets the alternate material index of all currently selected objects. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        A zero-based index of the material to be assigned, as obtained from the 
        get.material.index property. This parameter can also be given as a 
        string containing the material name, in which case it must not contain 
        any white-space characters and is case sensitive.
        
        """
        arg_str = string_util._convert_args_to_string("set.selection.alternate", 
                                                     index)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_area(self):
        """
        
        Retrieves the surface area (in m^2) of the current selection set, if 
        planar. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data. 

        """
        val = py2ecotect.conversation.Request("get.selection.area")
        return string_util._convert_str_to_type(val, float)
    
    def get_attr1(self):
        """
        
        Retrieves the value for the attr1 slot of the current selection set. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data. 
        
        """
        val = py2ecotect.conversation.Request("get.selection.attr1")
        return string_util._convert_str_to_type(val, float)
    
    def set_attr1(self, value):
        """
        
        Sets the value for the attr1 slot of the current selection set. 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        The decimal value to be stored.
        
        """
        arg_str = string_util._convert_args_to_string("set.selection.attr1", 
                                                     value)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_attr2(self):
        """
        
        Retrieves the value for the attr2 slot of the current selection set. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data. 
        
        """
        val = py2ecotect.conversation.Request("get.selection.attr2")
        return string_util._convert_str_to_type(val, float)
    
    def set_attr2(self, value):
        """
        
        Sets the value for the attr2 slot of the current selection set. 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        The decimal value to be stored.
        
        """
        arg_str = string_util._convert_args_to_string("set.selection.attr2", 
                                                     value)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_attr3(self):
        """
        
        Retrieves the value for the attr3 slot of the current selection set. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data. 
        
        """
        val = py2ecotect.conversation.Request("get.selection.attr3")
        return string_util._convert_str_to_type(val, float)
    
    def set_attr3(self, value):
        """
        
        Sets the value for the attr3 slot of the current selection set. 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        The decimal value to be stored.
        
        """
        arg_str = string_util._convert_args_to_string("set.selection.attr3", 
                                                     value)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_count(self):
        """
        
        Returns the number of objects in the current selection set. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        count 
        The number of objects in current selection set. 

        """
        val = py2ecotect.conversation.Request("get.selection.count")
        return string_util._convert_str_to_type(val, int)
        
    def get_exposure(self):
        """
        
        Retrieves the surface area exposed to outside conditions (in m^2) of 
        the current selection set, if planar. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data. 
        
        """
        val = py2ecotect.conversation.Request("get.selection.exposure")
        return string_util._convert_str_to_type(val, float)
    
    def get_length(self):
        """
        
        Retrieves the total length (m) of the current selection set, if linear. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data.
        
        """
        val = py2ecotect.conversation.Request("get.selection.length")
        return string_util._convert_str_to_type(val, float)
    
    def get_material(self):
        """
        
        Retrieves the primary material index of all currently selected objects. 
        A negative result indicates that the material varies within the 
        selection. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the primary material assigned.
        
        """
        val = py2ecotect.conversation.Request("get.selection.material")
        return string_util._convert_str_to_type(val, int)
    
    def set_material(self, index, both):
        """
        
        Sets the primary material index of all currently selected objects. 

        Parameter(s)
        This property takes the following parameters.
        
        index 
        A zero-based index of the material to be assigned, as obtained from the 
        get.material.index property. This parameter can also be given as a 
        string containing the material name, in which case it must not contain 
        any white-space characters and is case sensitive. 
        
        both 
        Determines whether the specified material is assigned to the alternate 
        material setting of selected objects as well. This is a boolean value 
        where 1 or true represents the affirmative and 0 or false the negative.
        
        """
        arg_str = string_util._convert_args_to_string("set.selection.material", 
                                                     index, both)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_next(self):
        """
        
        Returns the index of the next object in the current selection set. A 
        negative value indicates the end of the list. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the next selected object. 

        """
        val = py2ecotect.conversation.Request("get.selection.next")
        return string_util._convert_str_to_type(val, int)
        
    def get_panel_area(self):
        """
        
        Retrieves the surface overlapping a WINDOW / DOOR in adjacent zone (m^2). 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data.
        
        """
        val = py2ecotect.conversation.Request("get.selection.panelarea")
        return string_util._convert_str_to_type(val, float)
    
    def get_prev(self):
        """
        
        Returns the index of the previous object in the current selection set. 
        A negative value indicates the end of the list. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        index 
        The zero-based index of the next previous object. 

        """
        val = py2ecotect.conversation.Request("get.selection.prev")
        return string_util._convert_str_to_type(val, int)
    
    def get_resolution(self):
        """
        
        Retrieves the curve resolution for virtual polylines. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data.
        
        """
        val = py2ecotect.conversation.Request("get.selection.resolution")
        return string_util._convert_str_to_type(val, float)
    
    def set_resolution(self, value):
        """
        
        Sets the curve resolution for virtual polylines. 

        Parameter(s)
        This property takes the following parameters.
        
        value 
        An integer specifying the curve resolution.
        
        """
        arg_str = string_util._convert_args_to_string("set.selection.resolution", 
                                                     value)
        py2ecotect.conversation.Exec(arg_str)
    
    def get_type(self):
        """
        
        Retrieves the element type of all selected objects. A negative result 
        indicates that the type varies within the selection. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        type 
        An integer value corresponding to the following Element Types table.
        
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
        val = py2ecotect.conversation.Request("get.selection.type")
        return string_util._convert_str_to_type(val, int)
    
    def set_type(self, type, state = True):
        """
        
        Sets the element type of all selected objects. 

        Parameter(s)
        This property takes the following parameters.
        
        type 
        An integer value corresponding to the following Element Types table. 
        
        [state] 
        An optional boolean parameter specifying if the default material of the 
        new element type is assigned to the material as well. This parameter 
        defaults to true. 
        
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
        arg_str = string_util._convert_args_to_string("set.selection.type", 
                                                     type, state)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_underground(self):
        """
        
        Retrieves the surface area exposed to ground conditions (m2), if planar. 

        Parameter(s)
        There are no parameters for this property.
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the specified data.
        
        """
        val = py2ecotect.conversation.Request("get.selection.underground")
        #TODO: Result is different
        return string_util._convert_str_to_type(val, float)
    
    alternate = property(fget = get_alternate, fset = set_alternate, 
                        doc = "The alternate material index of all currently"
                        " selected objects")
    
    area = property(fget = get_area, doc = "The surface area (in m^2) of the"
                    " current selection set, if planar")
    
    attr1 = property(fget = get_attr1, fset = set_attr1, 
                        doc = "The value for the attr1 slot of the current"
                        " selection set.")
    
    attr2 = property(fget = get_attr2, fset = set_attr2, 
                        doc = "The value for the attr2 slot of the current"
                        " selection set")
    
    attr3 = property(fget = get_attr3, fset = set_attr3, 
                        doc = "The value for the attr3 slot of the current"
                        " selection set. ")
    
    count = property(fget = get_count, doc = "The number of objects in the"
                     " current selection set")
    
    exposure = property(fget = get_exposure, doc = "The surface area exposed to"
                        " outside conditions (in m^2) of the current selection"
                        " set, if planar")
    
    length = property(fget = get_length, doc = "The total length (m) of the"
                      " current selection set, if linear")
    
    next = property(fget = get_next, doc = "The index of the next object in the"
                    " current selection set")
    
    panel_area = property(fget = get_panel_area, doc = "The surface overlapping a"
                         " WINDOW / DOOR in adjacent zone (m^2)")
    
    prev = property(fget = get_prev, doc = "The index of the previous object in"
                    " the current selection set")
    
    resolution = property(fget = get_resolution, doc = "The curve resolution"
                          " for virtual polylines")
    
    underground = property(fget = get_underground, doc = "The surface area"
                           " exposed to ground conditions (m^2), if planar")
    
    
    
if __name__ == "__main__":
    x = Selection()
    #x.delete()
    
    #print x.get_alternate()
    #print x.get_count()
    #print x.get_length()
    #print x.get_material()
    #x.set_material(39, 0)
    print x.underground

    

    print "Tests completed"