import py2ecotect as p2e


#===========================================================================
# Functions
#===========================================================================
#------------------------------------------------------------------------------ 
def num_nodes():
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
    val = p2e._app.Request("get.model.nodes")
    return p2e._base._util._convert_str_to_type(val, int)

def num_objects():
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
    val = p2e._app.Request("get.model.objects")
    return p2e._base._util._convert_str_to_type(val, int)

def num_zones():
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
    val = p2e._app.Request("get.model.zones")
    return p2e._base._util._convert_str_to_type(val, int)     

def num_materials():
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
    val = p2e._app.Request("get.model.materials")
    return p2e._base._util._convert_str_to_type(val, int)  
#------------------------------------------------------------------------------ 
def nodes():
    """
    
    Returns a list of all the nodes in the model
    """
    return p2e.model._nodes
def objects():
    """
    
    Returns a list of all the nodes in the model
    """
    return p2e.model._objects
def zones():
    """
    
    Returns a list of all the nodes in the model
    """
    return p2e.model._zones
#------------------------------------------------------------------------------ 
def object_by_id(id):
    """
    
    Returns the object with the specified id within the 
    currently loaded ECOTECT model. 
    Warning: Ecotect id's can change when other objects are deleted. The id is 
    just the index in a list.

    Parameter(s)
    This property takes the following parameters.
    
    index 
    The index of the object.
    
    Return Value(s)
    
    object 
    The object. 
    
    """    
    return p2e.model._objects[id] 
#------------------------------------------------------------------------------ 
def current_node():
    """
    
    Returns the last selected node within the 
    currently loaded ECOTECT model. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    node 
    The zero-based index of the current node. 
    
    """
    val = p2e._app.Request("get.model.currentnode")
    val = p2e._base._util._convert_str_to_type(val, int)
    return p2e.model._nodes[val]

def current_object():
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
    val = p2e._app.Request("get.model.currentobject")
    val = p2e._base._util._convert_str_to_type(val, int)
    return p2e.model._objects[val]

def current_zone():
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
    val = p2e._app.Request("get.model.currentzone")
    val = p2e._base._util._convert_str_to_type(val, int)
    return p2e.model._zones[val]
#------------------------------------------------------------------------------ 
def last_node_index():
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
    val = p2e._app.Request("get.model.lastnode")
    return p2e._base._util._convert_str_to_type(val, int)

#------------------------------------------------------------------------------ 
def prev_node(object, node):
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
    args = p2e._base._util._convert_args_to_string("get.model.prevnode", 
                                             object._eco_id, node._eco_id)
    val = p2e._app.Request(args)
    return p2e._base._util._convert_str_to_type(val, int)        

def prev_object(startat, type, flag, tag, zone):
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
        args = p2e._base._util._convert_args_to_string("get.model.prevobject", 
                                                 startat, type, flag, tag, 
                                                 zone)
    else:
        args = p2e._base._util._convert_args_to_string("get.model.prevobject", 
                                                 startat, type, flag, tag, 
                                                 zone._eco_id)
    val = p2e._app.Request(args)
    return p2e._base._util._convert_str_to_type(val, int)       
#------------------------------------------------------------------------------ 
def next_node(object, node):
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
    args = p2e._base._util._convert_args_to_string("get.model.nextnode", 
                                             object._eco_id, node._eco_id)
    val = p2e._app.Request(args)
    return p2e._base._util._convert_str_to_type(val, int)       

def next_object(startat, type, flag, tag, zone):
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
        args = p2e._base._util._convert_args_to_string("get.model.nextobject", 
                                                 startat, type, flag, tag, 
                                                 zone)
    else:
        args = p2e._base._util._convert_args_to_string("get.model.nextobject", 
                                                 startat, type, flag, tag, 
                                                 zone._eco_id)
    val = p2e._app.Request(args)
    return p2e._base._util._convert_str_to_type(val, int)          
