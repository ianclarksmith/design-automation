import py2ecotect
from py2ecotect import StringUtil

class Object(object):
    def delete(self, object):
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
        arg_str = StringUtil._convert_args_to_string("object.delete", object)
        py2ecotect.conversation.Exec(arg_str)
        
    def delnode(self, object, node):
        """
        
        The delnode command removes the specified node from the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to delete the node from. 
        
        node 
        The zero-based node index belonging to the object. 
        
        """
        arg_str = StringUtil._convert_args_to_string("object.delnode", object, 
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

    def duplicate(self, object, x, y, z):
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
        arg_str = StringUtil._convert_args_to_string("object.duplicate", object, 
                                                     x, y, z)
        py2ecotect.conversation.Exec(arg_str)
        
    def extrude(self, object, x, y, z):
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
        arg_str = StringUtil._convert_args_to_string("object.extrude", object, 
                                                     x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def link(self, object, parent):
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
        arg_str = StringUtil._convert_args_to_string("object.link", object, 
                                                     parent)
        py2ecotect.conversation.Exec(arg_str)

    def move(self, object, x, y, z):
        """
        
        This command moves the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to move. 
        x, y, z 
        Specifies a distance to move the specified object in each of the major axes.
        
        """
        arg_str = StringUtil._convert_args_to_string("object.move", object, 
                                                     x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def normal(self, object, type):
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
        arg_str = StringUtil._convert_args_to_string("object.normal", object, 
                                                     type)
        py2ecotect.conversation.Exec(arg_str)

    def nudge(self, object, dir):
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
        arg_str = StringUtil._convert_args_to_string("object.nudge", object, dir)
        py2ecotect.conversation.Exec(arg_str)

    def orient(self, object, azi, alt):
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
        arg_str = StringUtil._convert_args_to_string("object.orient", object, 
                                                     azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def revolve(self, object, axis, angle, segs):
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
        arg_str = StringUtil._convert_args_to_string("object.revolve", object, 
                                                     axis, angle, segs)
        py2ecotect.conversation.Exec(arg_str)

    def rotate(self, object, azi, alt):
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
        arg_str = StringUtil._convert_args_to_string("object.rotate", object, 
                                                     azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def rotateaxis(self, object, rx, ry, rz):
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
        arg_str = StringUtil._convert_args_to_string("object.rotateaxis", object, 
                                                     rx, ry, rz)
        py2ecotect.conversation.Exec(arg_str)
        
    def rotatereverse(self, object, azi, alt):
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
        arg_str = StringUtil._convert_args_to_string("object.rotatereverse", object, 
                                                     azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def scale(self, object, dx, dy, dz):
        """
        
        This command scales the specified object. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The zero-based index of the object to scale. 
        
        dx, dy, dz 
        The scale factor to apply in each of the major axes. 
        
        """
        arg_str = StringUtil._convert_args_to_string("object.scale", object, 
                                                     dx, dy, dz)
        py2ecotect.conversation.Exec(arg_str)

    def select(self, object):
        """
        
        Selects the specified object or, if multiple object indexes are given, 
        then all the specified objects. 

        Parameter(s)
        This command takes the following parameters.
        
        object 
        The the zero-based index of the object to select. Repeat as necessary. 
        
        """
        arg_str = StringUtil._convert_args_to_string("object.select", object)
        py2ecotect.conversation.Exec(arg_str)
        
    def spin(self, object, spin):
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
        rg_str = StringUtil._convert_args_to_string("object.spin", object, spin)
        py2ecotect.conversation.Exec(arg_str)

    def update(self, object):
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
        arg_str = StringUtil._convert_args_to_string("object.update", object)
        py2ecotect.conversation.Exec(arg_str)

    def xform(self, object, trans, x, y, z):
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
        arg_str = StringUtil._convert_args_to_string("object.xform", object, 
                                                     trans, x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def add_object(self, object, elemType, objType, selected = True, link = 0):
        arg_str = StringUtil._convert_args_to_string("add.object", elemType, 
                                                     objType, selected, link)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)

    def get_activation(self, object, day, hour):
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
        arg_str = StringUtil._convert_args_to_string("get.object.activation", 
                                                     object, day, hour)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def get_alternate(self, object):
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
        arg_str = StringUtil._convert_args_to_string("get.object.alternate", 
                                                     object)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, int)
        
    def set_alternate(self, object, material):
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
        arg_str = StringUtil._convert_args_to_string("set.object.alternate", 
                                                     object, material)
        py2ecotect.conversation.Exec(arg_str)

    def get_angle(self, object, type):
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
        arg_str = StringUtil._convert_args_to_string("get.object.angle", 
                                                     object, type)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def get_area(self, object):
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
        arg_str = StringUtil._convert_args_to_string("get.object.area", 
                                                     object)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)
        
    def get_attr1(self, object):
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
        arg_str = StringUtil._convert_args_to_string("get.object.attr1", 
                                                     object)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_attr1(self, object, value):
        """
        
        Sets the calculated value stored as Attribute Number 1 for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        value 
        The value to assign.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.object.attr1", 
                                                     object, value)
        py2ecotect.conversation.Exec(arg_str)
 
 
    def get_attr2(self, object):
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
        arg_str = StringUtil._convert_args_to_string("get.object.attr2", 
                                                     object)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_attr2(self, object, value):
        """
        
        Sets the calculated value stored as Attribute Number 2 for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        value 
        The value to assign.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.object.attr2", 
                                                     object, value)
        py2ecotect.conversation.Exec(arg_str)       

    def get_attr3(self, object):
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
        arg_str = StringUtil._convert_args_to_string("get.object.attr3", 
                                                     object)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_type(val, float)

    def set_attr3(self, object, value):
        """
        
        Sets the calculated value stored as Attribute Number 3 for the specified object. 

        Parameter(s)
        This property takes the following parameters.
        
        object 
        The zero-based index of the object to set. 
        value 
        The value to assign.
        
        """
        arg_str = StringUtil._convert_args_to_string("set.object.attr3", 
                                                     object, value)
        py2ecotect.conversation.Exec(arg_str)

    def get_center(self, object):
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
        arg_str = StringUtil._convert_args_to_string("get.object.center", 
                                                     object)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_list(val, float, float, float)

    def set_center(self, object, x, y, z):
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
        arg_str = StringUtil._convert_args_to_string("set.object.center", 
                                                     object, x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def get_child_extents(self, object, absolute = True):
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
        arg_str = StringUtil._convert_args_to_string("get.object.child.extents", 
                                                     object, absolute)
        val = py2ecotect.conversation.Request(arg_str)
        return StringUtil._convert_str_to_list(val, float, float, float, float)

    def set_child_extents(self, object, u, v, wu, hv):
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
        arg_str = StringUtil._convert_args_to_string("set.object.child.extents", 
                                                     object, u, v, wu, hv)
        py2ecotect.conversation.Exec(arg_str)







if __name__ == "__main__":
    x = Object()
    
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    print "Tests completed"