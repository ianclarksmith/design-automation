import py2ecotect
from py2ecotect import string_util

class Object(object):
    
    def __init__(self, elemType, objType, selected = True, link = 0):
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
        
        zoneIndex 
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
        arg_str = string_util._convert_args_to_string("add.object", elemType, 
                                                     objType, selected, link)
        val = py2ecotect.conversation.Request(arg_str)
        self._id = string_util._convert_str_to_type(val, int)
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def delete(self):
        """
        
        This command removes the specified object from the model. Note that this 
        will reduce the number of objects in the model so, if you are cycling 
        through all model objects in a loop, make sure you decrement the overall 
        object count accordingly. Alternatively, you could start from the last 
        object and delete backwards through the list. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to be deleted.
        
        """
        arg_str = string_util._convert_args_to_string("object.delete", self._id)
        py2ecotect.conversation.Exec(arg_str)
        
    def delnode(self, node):
        """
        
        The delnode command removes the specified node from the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to delete the node from. 
        
        node 
        The zero-based node index belonging to the object. 
        
        """
        arg_str = string_util._convert_args_to_string("object.delnode", self._id, 
                                                     node)
        py2ecotect.conversation.Exec(arg_str)

    def done(self):
        """
        
        Call this method to complete a new object after you have used the add.
        object and add.node commands to generate it. This command tells ECOTECT 
        to check the object's validity, calculate its plane equation and surface 
        area (if required) and exit the interactive add node mode. 

        Parameter(s)
        There are no parameters for this command.
  
        """
        py2ecotect.conversation.Exec("object.done")

    def duplicate(self, x, y, z):
        """
        
        Creates a duplicate copy of the specified object a distance of x, y and 
        z in each of the major axes. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to duplicate. 
        
        x, y, z 
        Specifies a distance move the duplicate object in each of the major axes. 
        
        """
        arg_str = string_util._convert_args_to_string("object.duplicate", 
                                                      self._id, x, y, z)
        py2ecotect.conversation.Exec(arg_str)
        
    def extrude(self, x, y, z):
        """
        
        Extrudes the specified object a distance of x, y and z in the major axis. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to extrude. 
        
        x, y, z 
        Specifies a distance to extrude the specified object in each of the 
        major axes.
        
        """
        arg_str = string_util._convert_args_to_string("object.extrude", self._id, 
                                                     x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def link(self, parent):
        """
        
        This command link two objects together to create a parent-child 
        relationship between the two objects. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to link as the child object. 
        
        parent 
        Specifies the zero-based index of the object the child object is linked 
        with.
        
        """
        arg_str = string_util._convert_args_to_string("object.link", self._id, 
                                                     parent)
        py2ecotect.conversation.Exec(arg_str)

    def move(self, x, y, z):
        """
        
        This command moves the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to move. 
        x, y, z 
        Specifies a distance to move the specified object in each of the major axes.
        
        """
        arg_str = string_util._convert_args_to_string("object.move", self._id, 
                                                     x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def normal(self, type):
        """
        
        This command orients the surface normals of the specified object in the 
        given model direction. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to affect. 
        
        type 
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
        arg_str = string_util._convert_args_to_string("object.normal", self._id, 
                                                     type)
        py2ecotect.conversation.Exec(arg_str)

    def nudge(self, dir):
        """
        
        Nudges the specified object in the given axis direction, by the current 
        grid snap distance setting. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to nudge. 
        
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
        arg_str = string_util._convert_args_to_string("object.nudge", 
                                                      self._id, dir)
        py2ecotect.conversation.Exec(arg_str)

    def orient(self, azi, alt):
        """
        
        Orients the surface normals of the specified object to the given azimuth 
        and altitude angles. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to select. 
        
        azi 
        The horizontal angle of orientation, given in degrees. 
        
        alt 
        The vertical angle of orientation, given in degrees. 
  
        """
        arg_str = string_util._convert_args_to_string("object.orient", self._id, 
                                                     azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def revolve(self, axis, angle, segs):
        """
        
        Revolves the specified object around the Transformation Origin to create 
        a 3D volume. See the object.rotate command for more information on 
        specifying the Transformation Origin. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to revolve. 
        
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
        arg_str = string_util._convert_args_to_string("object.revolve", self._id, 
                                                     axis, angle, segs)
        py2ecotect.conversation.Exec(arg_str)

    def rotate(self, azi, alt):
        """
        
        Rotates the specified object about the Transformation Origin (see set.
        model.origin for more information). Normally, polar rotation is done 
        about the y-axis (altitude) first and then the z-axis (aziumuth). 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to rotate. 
        
        azi 
        The azimuth angle of rotation in decimal degrees. 
        
        alt 
        The altitude angle of rotation in decimal degrees.
        
        """
        arg_str = string_util._convert_args_to_string("object.rotate", self._id, 
                                                     azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def rotateaxis(self, rx, ry, rz):
        """
        
        Rotates the specified object about the Transformation Origin (see set.
        model.origin for more information) along the specified axes. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to rotate. 
        
        rx, ry, rz 
        The amount of rotation in decimal degrees for each required axis, in a 
        positive anti-clockwise direction. Use a value of 0 if no rotation is 
        required for a particular axis. 
        
        """
        arg_str = string_util._convert_args_to_string("object.rotateaxis", 
                                                      self._id, rx, ry, rz)
        py2ecotect.conversation.Exec(arg_str)
        
    def rotatereverse(self, azi, alt):
        """
        
        Similar to object.rotate, this command rotates the specified object 
        about the Transformation Origin, except in reserve order. This allows a 
        normal polar rotation to be un-done correctly. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to rotate. 
        
        azi 
        The azimuth angle of rotation in decimal degrees. 
        
        alt 
        The altitude angle of rotation in decimal degrees.
        
        """
        arg_str = string_util._convert_args_to_string("object.rotatereverse", 
                                                      self._id, azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def scale(self, dx, dy, dz):
        """
        
        This command scales the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to scale. 
        
        dx, dy, dz 
        The scale factor to apply in each of the major axes. 
        
        """
        arg_str = string_util._convert_args_to_string("object.scale", self._id, 
                                                     dx, dy, dz)
        py2ecotect.conversation.Exec(arg_str)

    def select(self):
        """
        
        Selects the specified object or, if multiple object indexes are given, 
        then all the specified objects. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The the zero-based index of the object to select. Repeat as necessary. 
        
        """
        arg_str = string_util._convert_args_to_string("object.select", self._id)
        py2ecotect.conversation.Exec(arg_str)
        
    def spin(self, spin):
        """
        
        Rotates the specified object about its geometric centre, around the axis 
        of its surface normal. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to spin. 
        
        spin 
        The spin angle given in decimal degrees.
        
        """
        rg_str = string_util._convert_args_to_string("object.spin", self._id, spin)
        py2ecotect.conversation.Exec(arg_str)

    def update(self):
        """
        
        Use this command to check and refresh inter-object relationships for the 
        specified object. Complex model with many inter-relationships can take a 
        little time to regenerate so ECOTECT doesn't do this automatically after 
        each script-based manipulation. You can also use model.update to do this 
        for all objects in the model at once. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The the zero-based index of the object to select.
        
        """
        arg_str = string_util._convert_args_to_string("object.update", self._id)
        py2ecotect.conversation.Exec(arg_str)

    def xform(self, trans, x, y, z):
        """
        
        Applies a generic transformation to the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to transform. 
        
        trans 
        The generic tranformation to apply, according to the Tranformation Types 
        table below. 
        
        x, y, z 
        The function of the x y z parameters are determined by the specified 
        trans parameter, as shown in the table above. 
        
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
        arg_str = string_util._convert_args_to_string("object.xform", self._id, 
                                                     trans, x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def get_id(self):
        """
        
        Id of the object
        
        """
        return self._id
    
    def get_activation(self, day, hour):
        """
        
        Returns the fractional activation value of the specified object for the 
        given day and hour. This will be a value between 0 - 1, where 0 is off 
        and 1 is on. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.activation", 
                                                     self._id, day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_alternate(self):
        """
        
        Retrieves the index of the alternate material to the specified object. 
        It is also possible to access all material properties this way. Thus, 
        you could use something like get("object.alternate.absorption", 23) to 
        retrieve data from the alternate material assigned to this object. See 
        the material object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        Return Value(s)
        Getting this property returns the following value(s).
        
        altIndex 
        The zero-based index of the assigned alternate material. 

        """
        arg_str = string_util._convert_args_to_string("get.object.alternate", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def set_alternate(sel, material):
        """
        
        Sets the index of the alternate material of the specified object. It is 
        also possible to set any material properties this way. For example, you 
        could use something like set("object.alternate.absorption", 23, 0.57) to 
        set data for the alternate material assigned to this object. See the 
        material object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        material 
        This parameter can be given as either a material name or as a number, 
        being the zero-based index of the material to be assigned from within 
        the material list. You can obtain this index manually from the material 
        name using the get.material.index property.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.alternate", 
                                                     self._id, material)
        py2ecotect.conversation.Exec(arg_str)

    def get_angle(self, type):
        """
        
        Returns the angle, in degrees, of the surface normal of a planar object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.angle", 
                                                     self._id, type)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_area(self):
        """
        
        Retrieves the surface area for the specified object, measured in square 
        metres. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.area", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)
        
    def get_attr1(self):
        """
        
        Retrieves the calculated value stored as Attribute Number 1 for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.attr1", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_attr1(self, value):
        """
        
        Sets the calculated value stored as Attribute Number 1 for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        value 
        The value to assign.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.attr1", 
                                                     self._id, value)
        py2ecotect.conversation.Exec(arg_str)
 
 
    def get_attr2(self):
        """
        
        Retrieves the calculated value stored as Attribute Number 2 for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.attr2", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_attr2(self, value):
        """
        
        Sets the calculated value stored as Attribute Number 2 for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        value 
        The value to assign.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.attr2", 
                                                     self._id, value)
        py2ecotect.conversation.Exec(arg_str)       

    def get_attr3(self):
        """
        
        Retrieves the calculated value stored as Attribute Number 3 for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.attr3", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_attr3(self, value):
        """
        
        Sets the calculated value stored as Attribute Number 3 for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        value 
        The value to assign.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.attr3", 
                                                     self._id, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_center(self):
        """
        
        Returns three decimal values corresponding to the X, Y and Z components 
        of geometric centre for the specified object. The values of the object 
        centre are given in absolute world coordinates. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the centre 
        point in 3 dimensional model space. 

        """
        arg_str = string_util._convert_args_to_string("get.object.center", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def set_center(self, x, y, z):
        """
        
        Sets the centre point for the specified object - the object is moved so 
        that its center is aligned to the point specified. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.center", 
                                                     self._id, x, y, z)
        py2ecotect.conversation.Exec(arg_str)

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
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.child.extents", 
                                                     self._id, absolute)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float, float)

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
        
        object 
        The zero-based index of the child object to set. 
        
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
        arg_str = string_util._convert_args_to_string("set.object.child.extents", 
                                                     self._id, u, v, wu, hv)
        py2ecotect.conversation.Exec(arg_str)

    def get_coplanar(self, x, y, z):
        """
        
        Determines if a point is co-planar with the specified object. Onviously 
        this only works with objects that are closed planar surfaces. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        colanar 
        A boolean value where 1 means that the point is coplanar and 0 means that it isn't. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.coplanar", 
                                                     self._id, x, y, z)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def set_current(self):
        """
        
        Several actions within ECOTECT act on the current object (sun-path 
        diagrams, etc). Set this property of an object to ensure that it is the 
        current object before invoking a command. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.current", 
                                                     self._id)
        py2ecotect.conversation.Exec(arg_str)

    def get_distanceto(self, x, y, z):
        """
        
        Returns a single floating point value, being the distance between the 
        specified object and the specified 3D point. If this is a POINT object, 
        the distance is the point-to-point distance. If the object is planar, it 
        is the distance of the specified point in line with the plane of the 
        object, even if this point is outside the object's boundaries. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dist 
        The distance fro the point to the object.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.distanceto", 
                                                     self._id, x, y, z)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_equation(self):
        """
        
        Getting this property returns the values used to calculate the plane 
        equation for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        A, B, C, D 
        Four decimal values corresponding to A, B, C and D from the plane 
        equation:
        Ax + By + Cz = D 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.equation", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float, float)
 
    def set_equation(self):
        """
        
        When this property is set, ECOTECT recalculates the plane equation 
        Ax + By + Cz = D for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to calculate.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.equation", 
                                                     self._id)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_exposure(self):
        """
        
        This command retrieves the surface area of an object that is exposed to 
        outside conditions. This command only works for planar objects. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.exposure", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_extents(self):
        """
        
        Retrieves the overall size for the specified object, measured in 
        millimetres. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dx, dy, dz 
        The overall dimensions of the object in each of the X, Y and Z axis. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.extents", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def get_extents_2dpt(self, u, v):
        """
        
        This command retrieves coordinates for the nominated point on the face 
        of the specified object. Note that this command only works for planar 
        objects. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        u, v 
        Proportional values that nominate the point to measure in relation to 
        the extents of the specified object. For example, to nominate the centre 
        of the object, the u and v values should be 0.5, whilst the minimum and 
        maximum extents would be of 0.0 and 1.0 respectively.
        
        This property always assumes you are looking towards the outside face of 
        the object, where the minimum value is always the bottom-left. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.extents.2dpt", 
                                                     self._id, u, v)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def get_extents_max(self):
        """
        
        Retrieves the 3D coordinates for the maximum extent of the selected 
        object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the maximum 
        point in 3 dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.extents.max", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def get_extents_min(self):
        """
        
        Retrieves the coordinates for the minimum extent of the selected object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the minimum 
        point in 3 dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.extents.min", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def get_firstnode(self):
        """
        
        Returns the zero-based absolute index of its first node. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        nodeIndex 
        The zero-based index of the object's first node.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.firstnode", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def get_flag(self, flag):
        """
        
        In ECOTECT, objects have a range of boolean flags associated with them 
        that are used at various times. This command retrieves the nominated 
        flag settings for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.flag", 
                                                     self._id, flag)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

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
        
        object 
        The zero-based index of the object to set. 
        
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
        arg_str = string_util._convert_args_to_string("set.object.flag", 
                                                     self._id, flag, state)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_incidence(self, x, y, z):
        """
        
        Returns the angle in degrees between the surface normal of the specified 
        object and the nominated 3D point. This is effectively the incidence 
        angle of a ray fired towards the geometric centre of the object from the 
        nominated point. If the object is not planar, the angle value returned 
        will be in relation to the positive x axis. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        x, y, z 
        The coordinates of the point to check in relation to the object. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        angle 
        The incidence angle in degrees. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.incidence", 
                                                     self._id, x, y, z)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)
        
    def get_inside(self, x, y, z, checkChildren = True):
        """
        
        Determines if the specified point is within the boundary of the 
        specified object, either 0 for false or 1 for true. This command 
        obviously only works for closed planar objects.

        Note: It is assumed that the specified point is very close to being 
        co-planar with the object. If it lies any signficiant distance away from 
        the surface, invalid results are likely. 
        
        Parameter(s)
        This property takes the following parameters.
        
        object 
        The ero-based index of the object to retrieve. 
        
        x, y, z 
        The coordinates of the point to check in relation to the object. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.inside", 
                                                     self._id, x, y, z, 
                                                     checkChildren)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def get_intersect(self, x1, y1, z1, x2, y2, z2):
        """
        
        Returns the coordinates of the intersection point between a line joining 
        the two nominated points with the plane of the specified object. This 
        command only works with planar objects.

        The intersection point can occur anywhere along the line, both between 
        the points and either side. 
        
        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        x1, y1, z1 
        The 3D start point of the intersecting line. 
        
        x2, y2, z2 
        The 3D end point of the intersecting line. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the 
        intersection point in 3 dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.intersect", 
                                                     self._id, x1, y1, z1, x2, y2, 
                                                     z2)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def get_lastnode(self):
        """
        
        Returns the zero-based absolute index of its last node. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        Return Value(s)
        Getting this property returns the following value(s).
        
        nodeIndex 
        The zero-based index of the object's last node. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.lastnode", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def get_length(self):
        """
        
        Retrieves the length value for the specified object, measured in 
        millimetres. This command only works on linear objects. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.length", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_link(self):
        """
        
        Getting this property returns the absolute index of the object to which 
        the specified object is linked. If the object is not linked to any other 
        object, it returns a value of -1. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        link 
        The zero-based index of the linked object.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.link", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def get_mask(self):
        """
        
        Retrieves the index of the object's shading mask. The shading mask 
        assigned to each object determines when and by how much the object is 
        overshadowed at any particular time. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        mask 
        An integer value between -1 and the value given by get.masks.count - 1, 
        being the zero-based index of the shading mask in the current list.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.mask", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def set_mask(self, index):
        """
        
        Sets the index of the object's shading mask. The shading mask assigned 
        to each object determines when and by how much the object is 
        overshadowed at any particular time. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        index 
        An integer value between -1 and the value given by get.masks.count - 1, 
        being the zero-based index of the shading mask in the current list. 

        """
        arg_str = string_util._convert_args_to_string("set.object.mask", 
                                                     self._id, index)
        py2ecotect.conversation.Exec(arg_str)

    def get_material(self):
        """
        
        Retrieves the index of the object's primary material. It is also 
        possible to access all material properties this way. Thus, you could use 
        something like get("object.material.absorption", 23) to retrieve data 
        from the primary material assigned to this object. See the material 
        object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        matIndex 
        The zero-based index of the assigned primary material. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.material", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def set_material(self, material):
        """
        
        Sets the index of the object's primary material. It is also possible to 
        set any material properties this way. For example, you could use 
        something like set("object.material.absorption", 23, 0.57) to set data 
        for the primary material assigned to this object. See the material 
        object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        material 
        Either a material name or an integer, being the zero-based index of the 
        material to be assigned from within the material list. You can obtain 
        this index manually from the material name using the get.material.index 
        command.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.material", 
                                                     self._id, material)
        py2ecotect.conversation.Exec(arg_str)

    def get_node_position(self, node):
        """
        
        Retrieves the position of the node in absolute world coordinates for 
        each of the major axes. Three coordinate values are returned. In fact, 
        it is possible to access all node properties this way - see the node 
        object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        node 
        The relative index of the node in the specified object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the node in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.node.position", 
                                                     self._id, node)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def set_node_position(self, node, x, y, z):
        """
        
        Sets the position of the node in absolute world coordinates for each of 
        the major axes. In fact, it is possible to set all node properties this 
        way - see the node object for more details. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        node 
        The relative index of the node in the specified object to set. 
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the node in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.node.position", 
                                                     self._id, node, x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def get_nodes(self):
        """
        
        Returns the number of nodes in the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        Return Value(s)
        Getting this property returns the following value(s).
        
        count 
        The number of nodes in this object. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.node", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def get_normal(self):
        """
        
        Retrieves the values corresponding to the x, y and z axis components for 
        the normal of the specified object. Note that all surface normals in 
        ECOTECT are normalised such that they are of unit length 
        (ie: length = 1.0). 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dx, dy, dz 
        A vector value representing the offset distance in each of the X, Y and 
        Z axis, given in model coordinates, of the object's normal.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.normal", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def get_panelarea(self):
        """
        
        Retrieves the surface area value overlapping with a WINDOW or DOOR 
        object in an adjacent zone, measured in square metres. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.panelarea", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)


    def get_pt_even(self):
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
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.pt.even", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float, int)

    def get_pt_initialise(self, fraction):
        """
        
        Many analysis functions require a range of sample points distributed 
        over an object's surface or along its length. This property allows you 
        to initiate this process for the specified object. The returned value is 
        a single integer value either 0 (false) or 1 (true) depending on whether 
        points were found, which will allow the process to continue. See 
        get.object.pt.rand and get.object.pt.even for more information. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.pt.initialise", 
                                                     self._id, fraction)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def get_pt_random(self):
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
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.pt.random", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float, int)

    def get_reflect(self, x, y, z):
        """
        
        Reflects the nominated 3D point around the plane of the specified object 
        and returns three floating point values representing the x, y and z 
        components of the new point. This command only works for planar objects. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        x, y, z 
        The absolute position in the X, Y and Z axis of the reflected point in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.reflect", 
                                                     self._id, x, y, z)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def get_resolution(self):
        """
        
        Retrieves the current curve resolution to use for virtual polylines, for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.resolution", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def set_resolution(self, value):
        """
        
        Sets the curve resolution to use for virtual polylines, for the 
        specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        value 
        The value to use for the virtual polyline curve resolution.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.node.position", 
                                                     self._id, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_sameside(self, x1, y1, z1, x2, y2, z2):
        """
        
        Returns a single integer value, either 0 (false) or 1 (true), depending 
        on whether the two nominated points are on the same side of the 
        specified object's plane equation. This command only works for planar 
        objects. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        x1 y1 z1 
        The first 3D point to use for the comparison. 
        
        x2 y2 z2 
        The second 3D point to use for the comparison. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        same 
        A boolean value where 1 means that the points are on the same side and 0 
        means that they aren't.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.sameside", 
                                                     self._id, x1, y1, z1, x2, y2, 
                                                     z2)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def get_schedule(self):
        """
        
        Retrieves the index value for the specified object's activation 
        schedule. The activation schedule determines when and how much an object 
        is turned on or off.

        It is also possible to access all schedule properties this way. Thus, 
        you could use something like get("object.schedule.name", 23) to retrieve 
        data from the schedule assigned to this object. See the schedule object 
        for more details. 
        
        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        schIndex 
        The zero-based index of the schedule assigned to this object. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.schedule", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
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
        
        object 
        The zero-based index of the object to set. 
        
        schedule 
        Either a schedule name or as the zero-based index of the schedule to be 
        assigned from within the model's schedule list. This index value can be 
        obtained manually from the schedule name, using the get.schedule.index 
        command.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.schedule", 
                                                     self._id, schedule)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_selected(self):
        """
        
        Retrieves the selection state of the specified object. A value of 1 
        means the object is part of the current selection set, whilst a value of 
        0 means that it is not. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        selected 
        This is a boolean value where 1 represents that the object is selected 
        and 0 that it is not. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.selected", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def set_selected(self, state = True):
        """
        
        Sets the selection state of the specified object.

        Note: Once you finish selecting the individual objects you want, you 
        should then call the selection.update command. 
        
        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        [state] 
        This optional parameter determines whether to set the object as selected 
        or not. This is a boolean value where 1 or true represents the 
        affirmative and 0 or false the negative. If not given, this parameter 
        defaults to true. Setting an object as selected also sets that object 
        as the current object.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.selected", 
                                                     self._id, state)
        py2ecotect.conversation.Exec(arg_str)

    def get_sunangles(self):
        """
        
        Returns the objects vertical shadow angle (VSA, always assuming it as a 
        vertical surface) and horizontal shadow angle (HSA), given in decimal 
        degrees.

        Note: As these values are always given in relation to the azimuth of the 
        object, the object's tilt angle can be set in relation to this common 
        base. 
        
        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        VSA 
        The Vertical Shadow Angle of the object at the current date and time. 
        
        HSA 
        The Horizontal Shadow Angle of the object at the current date and time. 
        
        """
        arg_str = string_util._convert_args_to_string("get.object.sunangles", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float)

    def get_tag(self, tag):
        """
        
        Retrieves information about tags that have been assigned to the 
        specified object. Tags are simply indicators to ECOTECT that the object 
        performs additional functions or is specifically marked for certain 
        calculations. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.tag", 
                                                     self._id, tag)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def set_tag(self, tag, state = True):
        """
        
        Sets tags for the specified object. Tags are simply indicators to 
        ECOTECT that the object performs additional functions or is specifically 
        marked for certain calculations. To test multiple tags at once, simply 
        add their values together. The optional [true|false] parameter 
        determines whether set or reset the tag(s), defaulting to true. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
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
        arg_str = string_util._convert_args_to_string("set.object.tag", 
                                                     self._id, tag, state)
        py2ecotect.conversation.Exec(arg_str)

    def get_type(self):
        """
        
        Returns the element type of the specified object, according to the 
        values in the Element Types table. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
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
        arg_str = string_util._convert_args_to_string("get.object.type", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def set_type(self, type):
        """
        
        Sets the specified object as the given element type. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        type 
        Either a token or value corresponding to the Element Types table.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.type", 
                                                     self._id, type)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_underground(self):
        """
        
        Gets the surface area that is underground. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        value 
        A decimal value containing the requested object data.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.underground", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

    def get_vector(self):
        """
        
        Retrieves the extrusion vector of the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        dx, dy, dz 
        A vector value representing the offset distance in each of the X, Y and 
        Z axis, given in model coordinates, of the object's extrusion vector.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.vector", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def set_vector(self, dx, dy, dz):
        """
        
        Sets the extrusion vector of the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        dx, dy, dz 
        A vector value representing the offset distance in each of the X, Y and 
        Z axis, given in model coordinates. 
        
        """
        arg_str = string_util._convert_args_to_string("set.object.vector", 
                                                     self._id, dx, dy, dz)
        py2ecotect.conversation.Exec(arg_str)
        
    def get_zone(self):
        """
        
        Retrieves the zone index of the specified object. The value returned 
        corresponds with the numerical order of the zone in the Zone Management 
        Panel. For example, if the specified object is part of the second zone 
        in the Zone Management panel, the value returned will be 2. The Outside 
        zone is always 0. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to retrieve. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        link 
        The zero-based index of the zone the specified object is assigned to.
        
        """
        arg_str = string_util._convert_args_to_string("get.object.zone", 
                                                     self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def set_zone(self, index):
        """
        
        Sets the specified object as a zone of the given index. The value set 
        should correspond with the numerical order of the required zone in the 
        Zone Management Panel. For example, if the specified object is to be 
        part of the second zone in the Zone Management panel, the set value 
        should be 2. The Outside zone is always 0. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        
        index 
        The zero-based index of the zone the specified object will be assigned 
        to.
        
        """
        arg_str = string_util._convert_args_to_string("set.object.zone", 
                                                     self._id, index)
        py2ecotect.conversation.Exec(arg_str)
        
    id = property(fget = get_id, doc = "Id of the object")
    
    activation = property(fget = get_activation, doc = "The fractional"
                          " activation value of the specified object for the"
                          " given day and hour. This will be a value between"
                          " 0 - 1, where 0 is off and 1 is on")
    
    alternate = property(fget = get_alternate, fset = set_alternate, 
                        doc = "The index of the alternate material to the"
                        " specified object")
    
    angle = property(fget = get_angle, doc = "The angle, in degrees, of the"
                     " surface normal of a planar object")
    
    area = property(fget = get_area, doc = "The surface area for the specified"
                    " object, measured in square metres")
    
    attr1 = property(fget = get_attr1, fset = set_attr1, 
                        doc = "The calculated value stored as Attribute Number"
                        " 1 for the specified object")
    
    attr2 = property(fget = get_attr2, fset = set_attr2, 
                        doc = "The calculated value stored as Attribute Number"
                        " 2 for the specified object")
    
    attr3 = property(fget = get_attr3, fset = set_attr3, 
                        doc = "The calculated value stored as Attribute Number"
                        " 3 for the specified object")
    
    center = property(fget = get_center, fset = set_center, 
                        doc = "The values of the object centre are given in"
                        " absolute world coordinates")
    
    child_extents= property(fget = get_child_extents, fset = set_child_extents, 
                        doc = "The size and location of a child object within"
                        " a parent object")
    
    coplanar = property(fget = get_coplanar, doc = "Determines if a point is"
                        " co-planar with the specified object. Onviously this"
                        " only works with objects that are closed planar"
                        " surfaces")
    
    current = property(fset = set_current, doc = "Several actions within"
                       " ECOTECT act on the current object (sun-path diagrams,"
                       " etc). Set this property of an object to ensure that it"
                       " is the current object before invoking a command")
    
    distanceto = property(fget = get_distanceto, doc = "Returns a single"
                          " floating point value, being the distance between"
                          " the specified object and the specified 3D point. If"
                          " this is a POINT object, the distance is the"
                          " point-to-point distance. If the object is planar,"
                          " it is the distance of the specified point in line"
                          " with the plane of the object, even if this point is"
                          " outside the object's boundaries")
    
    equation = property(fget = get_equation, fset = set_equation, 
                        doc = "Values used to calculate the plane equation for"
                        " the specified object")

    exposure = property(fget = get_exposure, doc = "The surface area"
                        " of an object that is exposed to outside conditions."
                        " Only works for planar objects.")
    
    extents = property(fget = get_extents, doc = "The overall size for the"
                       " specified object, measured in millimetres")
    
    extents_2dpt= property(fget = get_extents_2dpt, doc = "Coordinates for the"
                           " nominated point on the face of the specified"
                           " object. Note that this command only works for"
                           " planar objects")
    
    extents_max= property(fget = get_extents_max, doc = "The 3D coordinates for"
                          " the maximum extent of the selected object")
    
    extents_min= property(fget = get_extents_min, doc = "The coordinates for"
                          " the minimum extent of the selected object")
    
    firstnode = property(fget = get_firstnode, doc = "The zero-based absolute"
                         " index of its first node")
    
    flag = property(fget = get_flag, fset = set_flag, 
                        doc = "In ECOTECT, objects have a range of boolean"
                        " flags associated with them that are used at various"
                        " times")
    
    incidence = property(fget = get_incidence, doc = "The angle in degrees"
                         " between the surface normal of the specified object"
                         " and the nominated 3D point. This is effectively the"
                         " incidence angle of a ray fired towards the geometric"
                         " centre of the object from the nominated point. If"
                         " the object is not planar, the angle value returned"
                         " will be in relation to the positive x axis")
    
    inside = property(fget = get_inside, doc = "Determines if the specified"
                      " point is within the boundary of the specified object,"
                      " either 0 for false or 1 for true")
    
    intersect = property(fget = get_intersect, doc = "The coordinates of the"
                         " intersection point between a line joining the two"
                         " nominated points with the plane of the specified"
                         " object. This command only works with planar objects")
    
    lastnode = property(fget = get_lastnode, doc = "The zero-based absolute"
                        " index of its last node")
    
    length = property(fget = get_length, doc = "The length value for the"
                      " specified object, measured in millimetres. This command"
                      " only works on linear objects")
    
    link = property(fget = get_link, doc = "The absolute index of the object to"
                    " which the specified object is linked.")
    
    mask = property(fget = get_mask, fset = set_mask, 
                        doc = "The index of the object's shading mask. The"
                        " shading mask assigned to each object determines when"
                        " and by how much the object is overshadowed at any"
                        " particular time")
    
    material = property(fget = get_material, fset = set_material, 
                        doc = "The index of the object's primary material")
    
    node_position = property(fget = get_node_position, fset = set_node_position, 
                        doc = "The position of the node in absolute world"
                        " coordinates for each of the major axes")
    
    nodes = property(fget = get_nodes, doc = "The number of nodes in the"
                     " specified object")
    
    normal = property(fget = get_normal, doc = "The values corresponding to the"
                      " x, y and z axis components for the normal of the"
                      " specified object")
    
    panelarea = property(fget = get_panelarea, doc = "The surface area value"
                         " overlapping with a WINDOW or DOOR object in an"
                         " adjacent zone, measured in square metres")
    
    pt_even = property(fget = get_pt_even, doc = "Information about how sample"
                       " points are evenly distributed across an object")
    
    pt_initialise= property(fget = get_pt_initialise, doc = "This property"
                            " allows you to initiate this process for the"
                            " specified object")
    
    pt_random= property(fget = get_pt_random, doc = "Information about how"
                        " sample points are randomly distributed across an"
                        " object")
    
    reflect = property(fget = get_reflect, doc = "Reflects the nominated 3D"
                       " point around the plane of the specified object")
    
    resolution = property(fget = get_resolution, fset = set_resolution, 
                        doc = "The current curve resolution to use for virtual"
                        " polylines, for the specified object")
    
    sameside = property(fget = get_sameside, doc = "A single integer value,"
                        " either 0 (false) or 1 (true), depending on whether"
                        " the two nominated points are on the same side of the"
                        " specified object's plane equation")
    
    schedule = property(fget = get_schedule, fset = set_schedule, 
                        doc = "The index value for the specified object's"
                        " activation schedule. The activation schedule"
                        " determines when and how much an object is turned on"
                        " or off")
    
    selected = property(fget = get_selected, fset = set_selected, 
                        doc = "The selection state of the specified object. A"
                        " value of 1 means the object is part of the current"
                        " selection set, whilst a value of 0 means that it is"
                        " not")
    
    sunangles = property(fget = get_sunangles, doc = "The objects vertical"
                         " shadow angle (VSA, always assuming it as a vertical"
                         " surface) and horizontal shadow angle (HSA), given in"
                         " decimal degrees")
    
    tag = property(fget = get_tag, fset = set_tag, 
                        doc = "Tags are simply indicators to ECOTECT that the"
                        " object performs additional functions or is"
                        " specifically marked for certain calculations")
    
    type = property(fget = get_type, fset = set_type, 
                        doc = "The element type of the specified object")
    
    underground = property(fget = get_underground, doc = "The surface area that"
                           " is underground")
    
    vector = property(fget = get_vector, fset = set_vector, 
                        doc = "The extrusion vector of the specified object")
    
    zone = property(fget = get_zone, fset = set_zone, 
                        doc = "The zone index of the specified object")


if __name__ == "__main__":
    x = Object(15, 2444, True, 4)
    
    #print x.id
    
    #x.delete(294)
    #x.delnode(367, 1808)
    #print x.add_object(6, 2444, True, 4)
    #print x.get_activation(18, 244, 22)
    #print x.get_alternate(18)
    #x.set_alternate(18, 70)
    #print x.get_angle(18, 4)
    #print x.get_attr1(18)
    #x.set_attr1(18, 2.5)
    #print x.get_center(18)
    #print x.get_child_extents(18)
    #print x.get_coplanar(18, 1000, 2034.5, 763.54)
    #print x.get_equation(18)
    #print x.get_extents_max(18)
    #print x.get_extents_min(18)
    #print x.get_firstnode(18)
    #print x.get_flag(18, 8)
    #x.set_flag(18, 8, False)
    #print x.get_pt_even(18)
    #print x.get_type(1176)
    #x.set_type(1176, 2)
    #print x.get_zone(950)
    #x.set_zone(950, 5)

    print "Tests completed"