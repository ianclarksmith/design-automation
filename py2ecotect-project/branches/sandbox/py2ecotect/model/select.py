import py2ecotect as p2e

def all():
    """
    
    Selects all visible objects. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("select.all")

def alternate(index):
    """
    
    Selects all visible objects with the specified material as alternate 
    material. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    The zero-based index of the material obtained using the 
    get.material.index property.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("select.alternate", 
                                                  index)
    p2e._app.Exec(arg_str)

def child():
    """
    
    Selects all children of the currently selected objects. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("select.child")

def element(index):
    """
    
    Selects all visible objects of the specified element type. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    The element type as given in the add.object command(in ecotect). 
    For python reference, look at _create_object() in _Object class . 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("select.element", 
                                                  index)
    p2e._app.Exec(arg_str)

def objects(objects):
    """
    
    Selects multiple objects. 

    Parameter(s)
    This command takes the following parameters.
    
    objects 
    A list of objects to select.
    
    """
    eco_ids = ""
    for i in objects:
        eco_ids += str(i._eco_id) + ", "
        
    arg_str = p2e._base._util._convert_args_to_string("select.index", eco_ids)
    p2e._app.Exec(arg_str)
    
def invert():
    """
    
    Inverts the selection set. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("select.invert")

def none():
    """
    
    Clears the selection set. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("select.none")
    
def normals(index):
    """
    
    Selects all visible objects pointing in the specified direction. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    An integer value corresponding to the Select by Axis table below. 
    
    Relevant Data Table(s)
    
    Select by Axis 
    Value Axis 
    0 Up (+Z Axis) 
    1 Down (-Z Axis) 
    2 Left (-X Axis) 
    3 Right (+X Axis) 
    4 Back (+Y Axis) 
    5 Front (-Y Axis) 

    """
    arg_str = p2e._base._util._convert_args_to_string("select.normals", 
                                                  index)
    p2e._app.Exec(arg_str)
    
def object(object):
    """
    
    Selects the specified object, if it is visible. 

    Parameter(s)
    This command takes the following parameters.
    
    object 
    The object to be selected. 

    """
    arg_str = p2e._base._util._convert_args_to_string("select.object", 
                                                  object._eco_id)
    p2e._app.Exec(arg_str)

def parent():
    """
    
    Selects the parent(s) of all currently selected objects. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("select.parent")

def previous():
    """
    
    Selects all the visible objects selected at a previous time. 

    Parameter(s)
    There are no parameters for this command.
    
    """
    p2e._app.Exec("select.previous")

def primary(index):
    """
    
    Selects all the visible objects with the specified material as the 
    primary material. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    The ordinal number of the material obtained using the 
    get.material.index property.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("select.primary", 
                                                  index)
    p2e._app.Exec(arg_str)

def schedule(index):
    """
    
    Selects all the visible objects assigned to the specified schedule. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    The ordinal number of the schedule obtained using the 
    get.schedule.index property.
    
    """
    arg_str = p2e._base._util._convert_args_to_string("select.schedule", 
                                                  index)
    p2e._app.Exec(arg_str)
    
def tag(index):
    """
    
    Selects all the visible objects with the specified tags. 

    Parameter(s)
    This command takes the following parameters.
    
    index 
    The parameter specifies the tags to use, according to the values in the 
    following Object Tags table. To specify multiple tags, add the required 
    tag values together. 
    
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
    arg_str = p2e._base._util._convert_args_to_string("select.tag", 
                                                  index)
    p2e._app.Exec(arg_str)
    
def zone(zone):
    """
    
    Selects all visible objects located on the specified zone. 

    Parameter(s)
    This command takes the following parameters.
    
    zone 
    The zone to use. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("select.zone", 
                                                  zone._eco_id)
    p2e._app.Exec(arg_str)

