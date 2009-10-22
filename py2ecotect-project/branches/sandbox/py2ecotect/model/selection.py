import py2ecotect as p2e

#===========================================================================
# Commands
#===========================================================================
#------------------------------------------------------------------------------ 
def update():
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
    p2e._app.Exec("selection.update")
#------------------------------------------------------------------------------ 
def recalc_equations():
    """
    
    Recalculates the plane equations and surface areas of currently selected 
    object(s). 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("selection.equation")
#------------------------------------------------------------------------------ 
def delete():
    """
    
    Deletes the currently selected object(s) from the model. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("selection.delete")

#------------------------------------------------------------------------------ 
def duplicate(offset_distance):
    """
    
    Creates a duplicate copy of currently selected object(s). 

    Parameter(s)
    This command takes the following parameters.
    
    offset_distance 
    A list of three values that represent the offset distance in each of the 
    X, Y and Z axis, given in model coordinates, where the duplicate will 
    be placed. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("selection.duplicate", 
                                                  offset_distance[0],
                                                  offset_distance[1],
                                                  offset_distance[2])
    p2e._app.Exec(arg_str)    
#------------------------------------------------------------------------------ 
def group():
    """
    
    Establishes a group for the currently selected object(s). 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("selection.group")

def ungroup():
    """
    
    Removes the group status for the currently selected object(s). 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("selection.ungroup")
#------------------------------------------------------------------------------ 
def link():
    """
    
    Creates inter-object relationship links between the currently selected 
    objects. Such as establishing OBJECT_INSIDE and OBJECT_PLANAR links for 
    WINDOWS objects inside WALL objects. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("selection.link")

def unlink():
    """
    
    Removes any inter-object relationships from all currently selected objects. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("selection.unlink")
#------------------------------------------------------------------------------ 
def length():
    """
    
    Retrieves the total length (m) of the current selection set, if linear. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified data.
    
    """
    val = p2e._app.Request("get.selection.length")
    return p2e._base._util._convert_str_to_type(val, float)

def area():
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
    val = p2e._app.Request("get.selection.area")
    return p2e._base._util._convert_str_to_type(val, float)

def exposed_area():
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
    val = p2e._app.Request("get.selection.exposure")
    return p2e._base._util._convert_str_to_type(val, float)

def underground_area():
    """
    
    Retrieves the surface area exposed to ground conditions (m2), if planar. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified data.
    
    """
    #Return value is different. It returns 2 values. So a list 
    #of 2 values is returned
    val = p2e._app.Request("get.selection.underground")
    return p2e._base._util._convert_str_to_list(val, float, float)

def panel_area():
    """
    
    Retrieves the surface overlapping a WINDOW / DOOR in adjacent zone (m^2). 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified data.
    
    """
    val = p2e._app.Request("get.selection.panelarea")
    return p2e._base._util._convert_str_to_type(val, float)
#------------------------------------------------------------------------------ 
def count():
    """
    
    Returns the number of objects in the current selection set. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    count 
    The number of objects in current selection set. 

    """
    val = p2e._app.Request("get.selection.count")
    return p2e._base._util._convert_str_to_type(val, int)

def next_object():
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
    val = p2e._app.Request("get.selection.next")
    return p2e._base._util._convert_str_to_type(val, int)

def prev_object():
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
    val = p2e._app.Request("get.selection.prev")
    return p2e._base._util._convert_str_to_type(val, int)
#------------------------------------------------------------------------------ 
#=============================================================================
# Properties
#=============================================================================

def material():
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
    val = p2e._app.Request("get.selection.material")
    return p2e._base._util._convert_str_to_type(val, int)

def set_material(index, both):
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
    arg_str = p2e._base._util._convert_args_to_string("set.selection.material", index, both)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def alternate_material():
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
    val = p2e._app.Request("get.selection.alternate")
    return p2e._base._util._convert_str_to_type(val, int)
    

def set_alternate_material(index):
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
    arg_str = p2e._base._util._convert_args_to_string("set.selection.alternate", index)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def attr_1():
    """
    
    Retrieves the value for the attr1 slot of the current selection set. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified data. 
    
    """
    val = p2e._app.Request("get.selection.attr1")
    return p2e._base._util._convert_str_to_type(val, float)

def set_attr_1(value):
    """
    
    Sets the value for the attr1 slot of the current selection set. 

    Parameter(s)
    This property takes the following parameters.
    
    value 
    The decimal value to be stored.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.selection.attr1", value)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def attr_2():
    """
    
    Retrieves the value for the attr2 slot of the current selection set. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified data. 
    
    """
    val = p2e._app.Request("get.selection.attr2")
    return p2e._base._util._convert_str_to_type(val, float)

def set_attr_2(value):
    """
    
    Sets the value for the attr2 slot of the current selection set. 

    Parameter(s)
    This property takes the following parameters.
    
    value 
    The decimal value to be stored.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.selection.attr2", value)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def attr_3():
    """
    
    Retrieves the value for the attr3 slot of the current selection set. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified data. 
    
    """
    val = p2e._app.Request("get.selection.attr3")
    return p2e._base._util._convert_str_to_type(val, float)


def set_attr_3(value):
    """
    
    Sets the value for the attr3 slot of the current selection set. 

    Parameter(s)
    This property takes the following parameters.
    
    value 
    The decimal value to be stored.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.selection.attr3", 
                                                 value)
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 
def curve_resolution():
    """
    
    Retrieves the curve resolution for virtual polylines. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    value 
    A decimal value containing the specified data.
    
    """
    val = p2e._app.Request("get.selection.resolution")
    return p2e._base._util._convert_str_to_type(val, float)

def set_curve_resolution(value):
    """
    
    Sets the curve resolution for virtual polylines. 

    Parameter(s)
    This property takes the following parameters.
    
    value 
    An integer specifying the curve resolution.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("set.selection.resolution", 
                                                 value)
    p2e._app.Exec(arg_str)

#------------------------------------------------------------------------------ 
def type():
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
    val = p2e._app.Request("get.selection.type")
    return p2e._base._util._convert_str_to_type(val, int)

def set_type(type, state = True):
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
    arg_str = p2e._base._util._convert_args_to_string("set.selection.type", 
                                                 type, state)
    p2e._app.Exec(arg_str)
#=============================================================================
# Properties
#=============================================================================    
#------------------------------------------------------------------------------ 
def orient_normal_by_axis(axis):
    """
    
    Orients the surface normals of all currently selected objects in the specified direction. 

    Parameter(s)
    This command takes the following parameters.
    
    axis 
    An integer value corresponding to the following Object Normals table. 
    Relevant Data Table(s)
    Object Normal Directions Value Description 
    0 Towards current sun position. 
    1 Towards positive X axis. 
    2 Towards positive Y axis. 
    3 Towards positive Z axis. 

    """
    arg_str = p2e._base._util._convert_args_to_string("selection.normal", axis)
    p2e._app.Exec(arg_str)
    
def orient_normal(azi, alt):
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
    arg_str = p2e._base._util._convert_args_to_string("selection.nudge", 
                                                  azi, alt)
    p2e._app.Exec(arg_str)
    

def reverse_normal():
    """
    
    Reverses the surface normals of the currently selected object(s). 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("selection.reverse")
#------------------------------------------------------------------------------ 
def extrude_by_vec(vector):
    """
    
    Extrudes currently selected object(s). 

    Parameter(s)
    This command takes the following parameters.
    
    vector 
    A list of three values that represent the offset distance in each of the 
    X, Y and Z axis, given in model coordinates, where the duplicate will 
    be placed. 
    
    """
    vector = p2e._base._util.scale_1000(vector)    
    
    arg_str = p2e._base._util._convert_args_to_string("selection.extrude", 
                                                  vector[0],
                                                  vector[1],
                                                  vector[2])
    p2e._app.Exec(arg_str)

def move_by_vec(vector):
    """
    
    Moves the currently selected object(s). 

    Parameter(s)
    This command takes the following parameters.
    
    vector 
    A list of three values that represent the offset distance in each of the 
    X, Y and Z axis, given in model coordinates, where the duplicate will 
    be placed. 
    
    """
    vector = p2e._base._util.scale_1000(vector)
            
    arg_str = p2e._base._util._convert_args_to_string("selection.move", 
                                                  vector[0],
                                                  vector[1],
                                                  vector[2])
    p2e._app.Exec(arg_str)

def nudge(direction):
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
    arg_str = p2e._base._util._convert_args_to_string("selection.nudge", direction)
    p2e._app.Exec(arg_str)

def revolve(axis, angle, segs):
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
    arg_str = p2e._base._util._convert_args_to_string("selection.revolve", 
                                                  axis, angle, segs)
    p2e._app.Exec(arg_str)


def rotate(azi, alt):
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
    arg_str = p2e._base._util._convert_args_to_string("selection.rotate", 
                                                  azi, alt)
    p2e._app.Exec(arg_str)


def rotate_axis(rotateion_angles):
    """
    
    Rotates the selected object(s) by the given angles in each axis. 

    Parameter(s)
    This command takes the following parameters.
    
    rotateion_angles
    A list of three values that represent the angle to rotate around the 
    X-Axis, Y-Axis, and Z-Axis, in decimal degrees.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("selection.rotateaxis", 
                                                  rotateion_angles[0],
                                                  rotateion_angles[1],
                                                  rotateion_angles[2])
    p2e._app.Exec(arg_str)


def rotate_reverse(azi, alt):
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
    arg_str = p2e._base._util._convert_args_to_string("selection.rotatereverse", 
                                                  azi, alt)
    p2e._app.Exec(arg_str)


def scale(scale_factors):
    """
    
    Scales currently selected objects by a factor of dx, dy and dz in the 
    major axes. See the selection.rotate command for information on 
    specifying the Transformation Origin. 

    Parameter(s)
    This command takes the following parameters.
    
    scale_factors
    A list of three values that represent the scaling factor along the 
    X, Y, Z Axis
    
    """
    arg_str = p2e._base._util._convert_args_to_string("selection.scale", 
                                                  scale_factors[0],
                                                  scale_factors[1],
                                                  scale_factors[2])
    p2e._app.Exec(arg_str)


def spin(angle):
    """
    
    Rotates each selected object about its geometric centre, being the axis 
    of its surface normal. 

    Parameter(s)
    This command takes the following parameters.
    
    angle 
    The angle of rotation in degrees. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("selection.spin", angle)
    p2e._app.Exec(arg_str)

def xform(transformation, function_values):
    """
    
    Apply a generic transform to the selected object(s) in the model. 

    Parameter(s)
    This command takes the following parameters.
    
    transformation 
    The transformation to use, given as a token corresponding to the 
    following Transformation Types table. 
    
    function_values 
    A list of three values that represent the coordinate values specified 
    by the table below. 
    
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
    arg_str = p2e._base._util._convert_args_to_string("selection.xform", transformation, 
                                                  function_values[0], 
                                                  function_values[1], 
                                                  function_values[2])
    p2e._app.Exec(arg_str)
#------------------------------------------------------------------------------ 




