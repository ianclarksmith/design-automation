import py2ecotect as p2e

def data(node_name):
    """
    
    Retrieves the stored data at the given node. 

    Parameter(s)
    This property takes the following parameters.
    
    node_name 
    A text string containing the full dot(.)-separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    notes 
    A text string containing the node data. 

    """
    arg_str = p2e._base._util._convert_args_to_string("get.project.data", 
                                                 node_name)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, str)

def set_data(node_name, notes):
    """
    
    Sets the stored data for the given node. If the data node does not 
    exist, it will be created first. 

    Parameter(s)
    This property takes the following parameters.
    
    node_name
    A text string containing the full dot(.)-separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    notes
    A text string containing the data to be set. 
    
    Relevant Data Table(s)
    
    Embedded Data Format 
    Value Description 
    -1 Data node is hidden text. 
    0 No format has been defined, assume raw text. 
    1 Data contains raw text. 
    2 Data contains a parameter set (key=value). 
    3 Data contains runnable script code. 
 
    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.data", 
                                                 node_name, notes)
    p2e._app.Exec(arg_str)

def add_data(node_name, notes):
    """
    
    Appends new stored to the given data node. If the node already exists, 
    any data you provide will be appended to it's stored data. If it does 
    not exist, it will be created first. 

    Parameter(s)
    This property takes the following parameters.
    
    node_name 
    A text string containing the full dot(.)-separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    notes 
    A text string containing the new data to append. 
    
    Relevant Data Table(s)
    
    Embedded Data Format 
    Value Description 
    -1 Data node is hidden text. 
    0 No format has been defined, assume raw text. 
    1 Data contains raw text. 
    2 Data contains a parameter set (key=value). 
    3 Data contains runnable script code. 

    """
    arg_str = p2e._base._util._convert_args_to_string("add.project.data", 
                                                  node_name, notes)
    p2e._app.Request(arg_str)

def data_format(nodeName):
    """
    
    Retrieves the format of the given data node. 

    Parameter(s)
    This property takes the following parameters.
    
    nodeName 
    A text string containing the full dot(.) separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    format 
    An integer value containing the data format as defined in the following 
    table. 
    
    Relevant Data Table(s)
    
    Embedded Data Format 
    Value Description 
    -1 Data node is hidden text. 
    0 No format has been defined, assume raw text. 
    1 Data contains raw text. 
    2 Data contains a parameter set (key=value). 
    3 Data contains runnable script code. 

    """
    arg_str = p2e._base._util._convert_args_to_string("get.project.data.format", 
                                                 nodeName)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, int)

def set_data_format(nodeName, format):
    """
    
    Sets the format of the given data node. If the data node does not exist, 
    it will be created first. 

    Parameter(s)
    This property takes the following parameters.
    
    nodeName 
    A text string containing the full dot(.)-separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    format 
    An integer value containing the data format as defined in the following 
    table. 
    
    Relevant Data Table(s)
    
    Embedded Data Format 
    Value Description 
    -1 Data node is hidden text. 
    0 No format has been defined, assume raw text. 
    1 Data contains raw text. 
    2 Data contains a parameter set (key=value). 
    3 Data contains runnable script code. 

    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.data.format", 
                                                 nodeName, format)
    p2e._app.Exec(arg_str)

def data_notes(nodeName):
    """
    
    Retrieves the notes text associated with the given data node. 

    Parameter(s)
    This property takes the following parameters.
    
    nodeName 
    A text string containing the full dot(.)-separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    Return Value(s)
    Getting this property returns the following value(s).
    
    notes 
    A text string containing the associated notes. 
    
    """
    arg_str = p2e._base._util._convert_args_to_string("get.project.data.notes", 
                                                 nodeName)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, str)
    
def set_data_notes(nodeName, notes):
    """
    
    Sets the notes text associated with the given data node. If the data 
    node does not exist, it will be created first. 

    Parameter(s)
    This property takes the following parameters.
    
    nodeName 
    A text string containing the full dot(.)-separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    notes 
    A text string containing the new notes test to set. 
    
    Relevant Data Table(s)
    
    Embedded Data Format 
    Value Description 
    -1 Data node is hidden text. 
    0 No format has been defined, assume raw text. 
    1 Data contains raw text. 
    2 Data contains a parameter set (key=value). 
    3 Data contains runnable script code. 

    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.data.notes", 
                                                 nodeName, notes)
    p2e._app.Exec(arg_str)

def add_data_notes(nodeName, notes):
    """
    
    Appends new note text to the associated data node. If the node already 
    exists, any text you provide will be appended to it's existing notes. If 
    the data node does not exist, it will be created first. 

    Parameter(s)
    This property takes the following parameters.
    
    nodeName 
    A text string containing the full dot(.)-separated path to the embedded 
    data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
    cannot contain spaces of any kind. If you want to separate words, use 
    the underscore (_) character. 
    
    notes 
    A text string containing the new note text to append. 
    
    Relevant Data Table(s)
    Embedded Data Format 
    Value Description 
    -1 Data node is hidden text. 
    0 No format has been defined, assume raw text. 
    1 Data contains raw text. 
    2 Data contains a parameter set (key=value). 
    3 Data contains runnable script code. 

    """
    arg_str = p2e._base._util._convert_args_to_string("add.project.data.notes", 
                                                  nodeName, notes)
    p2e._app.Request(arg_str)

def data_param(nodeName, parameter):
    """
    
    ... 

    """
    arg_str = p2e._base._util._convert_args_to_string("get.project.data.param", 
                                                 nodeName, parameter)
    val = p2e._app.Request(arg_str)
    return p2e._base._util._convert_str_to_type(val, str)

def set_data_param(nodeName, key_value):
    """
    
    ...

    """
    arg_str = p2e._base._util._convert_args_to_string("set.project.data.param", 
                                                 nodeName, key_value)
    p2e._app.Exec(arg_str)


