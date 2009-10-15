import py2ecotect as p2e


#===========================================================================
# Functions
#===========================================================================

def clear():
    """
    
    Deletes the shading masks list and frees allocated memory. If a future 
    calculation requires shading masks, ECOTECT will attempt to re-load them 
    from the cache file on disk. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("masks.clear")

def load():
    """
    
    Loads the shading mask list. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("masks.load")

def save():
    """
    
    Saves the current shading mask list. 

    Parameter(s)
    There are no parameters for this command.

    """
    p2e._app.Exec("masks.save")

def num_masks():

    """
    
    Returns the number of shading masks in the current list. If no masks 
    have been loaded, a value of 0 will be returned. 

    Parameter(s)
    There are no parameters for this property.
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    count 
    The number of shading masks in the list.
    
    """
    val = p2e._app.Request("get.masks.count")
    return p2e._base._util._convert_str_to_type(val, int)
        


