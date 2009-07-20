import py2ecotect
from py2ecotect import string_util

class Node(object):
    
    def __init__(self, object, index, x, y, z, nodeType = 0, link = 0):
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
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of a point in 3 
        dimensional model space. 
        
        [nodeType] 
        Sets the type of node, according to the following Node Types table. 
        
        [link] 
        The zero-based index of the object or node to which the specified node 
        is to be linked. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        zoneIndex 
        The zero-based index of the node just added. A value of -1 indicates 
        that the operation failed. 
        
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
        #arg_str = string_util._convert_args_to_string("add.node", object, index, 
        #                                             x, y, z, nodeType, link)
        #val = py2ecotect.conversation.Request(arg_str)
        #self._id = string_util._convert_str_to_type(val, int)
        self._id = 1293
 
    #===========================================================================
    # Commands
    #===========================================================================
   
    def move(self, x, y, z):
        """
        
        Moves the specified node in the last selected object. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        These parameters specify the move distance and direction in each of the 
        major X, Y and Z axis.
        
        """
        arg_str = string_util._convert_args_to_string("node.move", self._id, 
                                                      x, y, z)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = string_util._convert_args_to_string("node.nudge", self._id, dir)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = string_util._convert_args_to_string("node.rotate", self._id, 
                                                      azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def rotate_axis(self, x, y, z):
        """
        
        Rotates the specified node in the last created object about the 
        Transformation Origin (see set.model.origin for more information) along 
        the specified axes. 

        Parameter(s)
        This command takes the following parameters.
        
        x, y, z 
        These parameters specify the amount of rotation in decimal degrees for 
        each required axis, in a positive anti-clockwise direction. Use a value 
        of 0 if no rotation is required for a particular axis.
        
        """
        arg_str = string_util._convert_args_to_string("node.rotateaxis", self._id,
                                                       x, y, z)
        py2ecotect.conversation.Exec(arg_str)

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
        arg_str = string_util._convert_args_to_string("node.rotatereverse", 
                                                      self._id, azi, alt)
        py2ecotect.conversation.Exec(arg_str)

    def scale(self, dx, dy, dz):
        """
        
        Scale the specified node in the last selected object. 

        Parameter(s)
        This command takes the following parameters.
        
        dx, dy, dz 
        These parameters specifies the scale factor to apply in each of the 
        major X, Y and Z axis.
        
        """
        arg_str = string_util._convert_args_to_string("node.scale", self._id, dx, 
                                                     dy, dz)
        py2ecotect.conversation.Exec(arg_str)
        
    def xform(self, trans, x, y, z):
        """
        
        Applies a generic transformation to the specified node in the last 
        selected object. 

        Parameter(s)
        This command takes the following parameters.
        
        trans 
        The generic tranformation to apply, according to the Transform Types 
        table below. 
        
        x, y, z 
        The function of these parameters are determined by the specified trans 
        parameter, as shown in the table below. 
        
        Relevant Data Table(s)
        T
        ransformation Types 
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
        arg_str = string_util._convert_args_to_string("node.xform", 
                                                      self._id, trans, x, y, z)
        py2ecotect.conversation.Exec(arg_str)
    
    #===========================================================================
    # Properties
    #===========================================================================

    def get_id(self):
        """
        
        Id of the node object
        
        """
        return self._id
    
    def get_flag(self, flag):
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
        arg_str = string_util._convert_args_to_string("get.node.flag", self._id, 
                                                      flag)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
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
        arg_str = string_util._convert_args_to_string("set.node.flag", self._id,
                                                       flag, state) 
        py2ecotect.conversation.Exec(arg_str)

    def get_flags(self):
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
        arg_str = string_util._convert_args_to_string("get.node.flags", self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)
        
    def get_link(self):
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
        arg_str = string_util._convert_args_to_string("get.node.link", self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

    def set_link(self, link):
        """
        
        Sets individual flags that control the display of attribute values. 

        Parameter(s)
        This property takes the following parameters.
        
        link 
        The zero-based index of the object or node to which the specified node 
        is to be linked.
        
        """
        arg_str = string_util._convert_args_to_string("set.node.link", self._id, 
                                                      link)
        py2ecotect.conversation.Exec(arg_str)

    def get_modifier(self):
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
        arg_str = string_util._convert_args_to_string("get.node.modifier", 
                                                      self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, float)

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
        arg_str = string_util._convert_args_to_string("set.node.modifier", 
                                                      self._id, mod)
        py2ecotect.conversation.Exec(arg_str)

    def get_position(self):
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
        arg_str = string_util._convert_args_to_string("get.node.position", self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_list(val, float, float, float)

    def set_position(self, x, y, z):
        """
        
        Sets the position of the node in absolute world coordinates in each of 
        the major axes. 

        Parameter(s)
        This property takes the following parameters.
        
        x, y, z 
        Represents the absolute position in the X, Y and Z axis of the node in 3 
        dimensional model space.
        
        """
        arg_str = string_util._convert_args_to_string("set.node.position", 
                                                      self._id, x, y, z)
        py2ecotect.conversation.Exec(arg_str)

    def get_selected(self):
        """
        
        Retrieves the selection state of the specified node. 

        Parameter(s)
        There are no parameters for this property.
         
        Return Value(s)
        Getting this property returns the following value(s).
        
        state 
        If this value is 1, then the node is selected. If 0 the node is not selected. 

        """
        arg_str = string_util._convert_args_to_string("get.node.selected", 
                                                      self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

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
        arg_str = string_util._convert_args_to_string("set.node.selected", 
                                                      self._id, state)
        py2ecotect.conversation.Exec(arg_str)

    def get_type(self):
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
        arg_str = string_util._convert_args_to_string("get.node.type", self._id)
        val = py2ecotect.conversation.Request(arg_str)
        return string_util._convert_str_to_type(val, int)

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
            arg_str = string_util._convert_args_to_string("set.node.type", 
                                                          self._id, type, link)
            py2ecotect.conversation.Exec(arg_str)


    id = property(fget = get_id, doc = "Id of the Node object")
    
    flags = property(fget = get_flags, doc = "A value representing the total of"
                     " all the node's flags")
    
    link = property(fget = get_link, fset = set_link, 
                        doc = "The node or object this node is linked to")
    
    modifier = property(fget = get_modifier, fset = set_modifier, 
                        doc = "The node modifier value")
    
    selected = property(fget = get_selected, fset = set_selected, 
                        doc = "The selection state of the specified node")

if __name__ == "__main__":
    #x = Node(255, 3, 1000, 2000, 0)
    
    #print x.id
    #x.move(101, 0, 0, 1500)
    #print x.add_node(102, 3, 1000, 2000, 0,)
    #print x.get_flag(1636, "text")
    #x.set_flag(1636, "text", "False")
    #print x.get_flags(1636)
    #print x.get_link(1636)
    #x.set_link(1636, 25)
    #print x.get_modifier(1636)
    #x.set_modifier(1636, 2400)
    #print x.get_position(9055)
    #x.set_position(1636, 1200, 2321, 600.0)
    #print x.get_selected(1636)
    #x.set_selected(1636)
    #print x.get_type(9055)
    #x.set_type(9055, 8)
    
    
    print "Tests completed"
