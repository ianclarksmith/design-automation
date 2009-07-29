import py2ecotect as p2e

class Project_Data(object):
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    def get_data(self, nodeName):
        """
        
        Retrieves the stored data at the given node. 

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
        A text string containing the node data. 

        """
        arg_str = p2e.string_util._convert_args_to_string("get.project.data", 
                                                     nodeName)
        val = p2e.conversation.Request(arg_str)
        return p2e.string_util._convert_str_to_type(val, str)

    def set_data(self, nodeName, notes):
        """
        
        Sets the stored data for the given node. If the data node does not 
        exist, it will be created first. 

        Parameter(s)
        This property takes the following parameters.
        
        nodeName
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
        arg_str = p2e.string_util._convert_args_to_string("set.project.data", 
                                                     nodeName, notes)
        p2e.conversation.Exec(arg_str)

    def add_data(self, nodeName, notes):
        """
        
        Appends new stored to the given data node. If the node already exists, 
        any data you provide will be appended to it's stored data. If it does 
        not exist, it will be created first. 

        Parameter(s)
        This property takes the following parameters.
        
        nodeName 
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
        arg_str = p2e.string_util._convert_args_to_string("add.project.data", 
                                                      nodeName, notes)
        p2e.conversation.Request(arg_str)

    def get_format(self, nodeName):
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
        arg_str = p2e.string_util._convert_args_to_string("get.project.data.format", 
                                                     nodeName)
        val = p2e.conversation.Request(arg_str)
        return p2e.string_util._convert_str_to_type(val, int)
    
    def set_format(self, nodeName, format):
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
        arg_str = p2e.string_util._convert_args_to_string("set.project.data.format", 
                                                     nodeName, format)
        p2e.conversation.Exec(arg_str)

    def get_notes(self, nodeName):
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
        arg_str = p2e.string_util._convert_args_to_string("get.project.data.notes", 
                                                     nodeName)
        val = p2e.conversation.Request(arg_str)
        return p2e.string_util._convert_str_to_type(val, str)
        
    def set_notes(self, nodeName, notes):
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
        arg_str = p2e.string_util._convert_args_to_string("set.project.data.notes", 
                                                     nodeName, notes)
        p2e.conversation.Exec(arg_str)

    def add_notes(self, nodeName, notes):
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
        arg_str = p2e.string_util._convert_args_to_string("add.project.data.notes", 
                                                      nodeName, notes)
        p2e.conversation.Request(arg_str)
    
    def get_param(self, nodeName, parameter):
        """
        
        Retrieves the format of the given data node. 

        Parameter(s)
        This property takes the following parameters.
        
        nodeName 
        A text string containing the full dot(.)-separated path to the embedded 
        data node. For example 'EXPORT.RADIANCE.MYDATA'. Paths to data nodes 
        cannot contain spaces of any kind. If you want to separate words, use 
        the underscore (_) character. 
        
        parameter 
        A text string containing the parameter name or 'key' value. This is the 
        name of the item that appears in the left-hand columns of the list. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        format 
        A text string containing the parameter name or 'key' value. This is the 
        name of the item that appears in the left-hand columns of the list. 
        
        Relevant Data Table(s)
        
        Embedded Data Format 
        Value Description 
        -1 Data node is hidden text. 
        0 No format has been defined, assume raw text. 
        1 Data contains raw text. 
        2 Data contains a parameter set (key=value). 
        3 Data contains runnable script code. 

        """
        arg_str = p2e.string_util._convert_args_to_string("get.project.data.param", 
                                                     nodeName, parameter)
        val = p2e.conversation.Request(arg_str)
        return p2e.string_util._convert_str_to_type(val, str)

    def set_param(self, nodeName, key_value):
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
        
        key=value 
        A text string containing both the key name and the value to be set, 
        separated by an '=' sign. Thus, if you wanted to assign the value 'This 
        is a test' to a parameter named 'title', simply use 'title=This is a 
        test' in this parameter. 
        
        Relevant Data Table(s)
        
        Embedded Data Format 
        Value Description 
        -1 Data node is hidden text. 
        0 No format has been defined, assume raw text. 
        1 Data contains raw text. 
        2 Data contains a parameter set (key=value). 
        3 Data contains runnable script code. 

        """
        arg_str = p2e.string_util._convert_args_to_string("set.project.data.param", 
                                                     nodeName, key_value)
        p2e.conversation.Exec(arg_str)


if __name__ == "__main__":
    x = Project_Data()
    
    #print x.get_data("EXPORT.RADIANCE.MYDATA")
    #x.set_data("EXPORT.RADIANCE.MYDATA", "TEST")
    #x.set_data(["EXPORT.RADIANCE.MYDATA", "asd"])
    #x.add_data("EXPORT.RADIANCE.MYDATA", "xcvx")
    #print x.get_format("EXPORT.RADIANCE.MYDATA")
    #x.format = ["EXPORT.RADIANCE.MYDATA",1]
    #x.set_format("EXPORT.RADIANCE.MYDATA", 2)
    #print x.get_param("EXPORT.RADIANCE.MYDATA", "title")
    #x.set_param("EXPORT.RADIANCE.MYDATA", "title=This is a test")
    
    print "Tests completed"