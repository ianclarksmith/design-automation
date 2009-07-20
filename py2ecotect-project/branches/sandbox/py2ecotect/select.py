import py2ecotect
from py2ecotect import string_util

class Select(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def all(self):
        """
        
        Selects all visible objects. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("select.all")

    def alternate(self, index):
        """
        
        Selects all visible objects with the specified material as alternate 
        material. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The zero-based index of the material obtained using the 
        get.material.index property.
        
        """
        arg_str = string_util._convert_args_to_string("select.alternate", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)

    def child(self):
        """
        
        Selects all children of the currently selected objects. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("select.child")

    def element(self, index):
        """
        
        Selects all visible objects of the specified element type. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The element type as given in the add.object command. 
        
        """
        arg_str = string_util._convert_args_to_string("select.element", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)

    def index(self, index):
        """
        
        Selects multiple objects. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        Specifies the index of the objects to select. Repeat as required.
        
        """
        arg_str = string_util._convert_args_to_string("select.index", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)
        
    def invert(self):
        """
        
        Inverts the selection set. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("select.invert")

    def none(self):
        """
        
        Clears the selection set. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("select.none")
        
    def normals(self, index):
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
        arg_str = string_util._convert_args_to_string("select.normals", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)
        
    def object(self, index):
        """
        
        Selects the specified object, if it is visible. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The ordinal number of the object to be selected obtained either 
        programatically (from the add.object command) or by looking at the top 
        of the Selection Information panel. 

        """
        arg_str = string_util._convert_args_to_string("select.object", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)

    def parent(self):
        """
        
        Selects the parent(s) of all currently selected objects. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("select.parent")

    def previous(self):
        """
        
        Selects all the visible objects selected at a previous time. 

        Parameter(s)
        There are no parameters for this command.
        
        """
        py2ecotect.conversation.Exec("select.previous")

    def primary(self, index):
        """
        
        Selects all the visible objects with the specified material as the 
        primary material. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The ordinal number of the material obtained using the 
        get.material.index property.
        
        """
        arg_str = string_util._convert_args_to_string("select.primary", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)

    def schedule(self, index):
        """
        
        Selects all the visible objects assigned to the specified schedule. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The ordinal number of the schedule obtained using the 
        get.schedule.index property.
        
        """
        arg_str = string_util._convert_args_to_string("select.schedule", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)
        
    def tag(self, index):
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
        arg_str = string_util._convert_args_to_string("select.tag", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)
        
    def zone(self, index):
        """
        
        Selects all visible objects located on the specified zone. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The zero-based index value of the zone to use. 
        
        """
        arg_str = string_util._convert_args_to_string("select.zone", 
                                                      index)
        py2ecotect.conversation.Exec(arg_str)














if __name__ == "__main__":
    x = Select()
    
    x.all()
    

    print "Tests completed"