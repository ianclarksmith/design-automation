import py2ecotect
from py2ecotect import string_util

class Selection(object):
    
    #===========================================================================
    # Commands
    #===========================================================================
    
    def delete(self):
        """
        
        Deletes the currently selected object(s) from the model. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.delete")
    
    def duplicate(self, dx, dy, dz):
        """
        
        Creates a duplicate copy of currently selected object(s). 

        Parameter(s)
        This command takes the following parameters.
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates, where the duplicate will be placed. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.duplicate", dx, 
                                                      dy, dz)
        py2ecotect.conversation.Exec(arg_str)
        
    def equation(self):
        """
        
        Recalculates the plane equations and surface areas of currently selected 
        object(s). 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.equation")
    
    def extrude(self, dx, dy, dz):
        """
        
        Extrudes currently selected object(s). 

        Parameter(s)
        This command takes the following parameters.
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.extrude", dx, 
                                                      dy, dz)
        py2ecotect.conversation.Exec(arg_str)
    
    def group(self):
        """
        
        Establishes a group for the currently selected object(s). 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.group")
    
    def link(self):
        """
        
        Creates inter-object relationship links between the currently selected 
        objects. Such as establishing OBJECT_INSIDE and OBJECT_PLANAR links for 
        WINDOWS objects inside WALL objects. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("selection.link")
    
    def move(self, dx, dy, dz):
        """
        
        Moves the currently selected object(s). 

        Parameter(s)
        This command takes the following parameters.
        
        dx, dy, dz 
        A value representing the offset distance in each of the X, Y and Z axis, 
        given in model coordinates. 
        
        """
        arg_str = string_util._convert_args_to_string("selection.move", dx, dy, 
                                                      dz)
        py2ecotect.conversation.Exec(arg_str)
    
    
    
    
    
    
    
    
    
    
    
    
    #===========================================================================
    # Properties
    #===========================================================================
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    x = Selection()
    x.delete()

    

    print "Tests completed"
