import py2ecotect
from py2ecotect import StringUtil

class Masks(object):
    
    def clear(self):
        """
        
        Deletes the shading masks list and frees allocated memory. If a future 
        calculation requires shading masks, ECOTECT will attempt to re-load them 
        from the cache file on disk. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("masks.clear")

    def copy(self, _from, to):
        """
        
        Copies all day information from one shading mask to another. 

        Parameter(s)
        This command takes the following parameters.
        
        _from 
        The zero-based index of the shading mask to copy from. 
        
        to 
        The zero-based index of the shading mask to copy to.
        
        """
        arg_str = StringUtil._convert_args_to_string("masks.copy", _from, to )
        py2ecotect.conversation.Exec(arg_str)

    def interpolate(self, index, t1, t2, fraction):
        """
        
        Interpolates between the values in two masks and stores them in a new mask. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The zero-based index of the shading mask where the interpolation will be 
        stored. 
        t1 
        The zero-based index of the shading mask from which the interpolation 
        will begin. 
        t2 
        The zero-based index of the shading mask at which the interpolation 
        will end. 
        fraction 
        The fractional mask bias for the interpolation, typically between 0 (t1) 
        and 1 (t2).
        
        """
        arg_str = StringUtil._convert_args_to_string("masks.interpolate", index, t1, 
                                                     t2, fraction )
        py2ecotect.conversation.Exec(arg_str)

    def load(self):
        """
        
        Loads the shading mask list. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("masks.load")

    def save(self):
        """
        
        Saves the current shading mask list. 

        Parameter(s)
        There are no parameters for this command.

        """
        py2ecotect.conversation.Exec("masks.save")

    def update(self, index):
        """
        
        Updates the specified shading mask's information. 

        Parameter(s)
        This command takes the following parameters.
        
        index 
        The zero-based index of the shading mask. 
        
        """
        arg_str = StringUtil._convert_args_to_string("masks.update", index)
        py2ecotect.conversation.Exec(arg_str)

    def add_mask(self, object = 0):
        """
        
        Adds a new shading mask to the masks list and returns the zero-based 
        index of the mask just added. 

        Parameter(s)
        This property takes the following parameters.
        
        [object] 
        This optional parameter sets the index to which the new shading mask 
        will be assigned to. 
        
        Return Value(s)
        Getting this property returns the following value(s).
        
        maskIndex 
        The zero-based index of the new shading mask.
        
        """
        arg_str = StringUtil._convert_args_to_string("add.mask", object)
        val = py2ecotect.conversation.Request("add.mask")
        return StringUtil._convert_str_to_type(val, int)

    def get_count(self):
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



if __name__ == "__main__":
    x = Masks()
    
    #x.clear()
    #x.copy(1, 5)
    # x.interpolate(10, 2, 5, 0.5)
    #x.load()
    #x.save()
    #x.update(1)
    #print x.add_mask(99)
    
    
    print "Tests completed"
