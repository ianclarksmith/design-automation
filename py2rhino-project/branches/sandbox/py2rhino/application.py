from comtypes.client import GetActiveObject, CreateObject
import time

#THIS CLASS IS NOT COMPLETE
class Application(object):
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self):
        #TODO: this needs to be improved - e.g. what if Rhino is not open
        self._id = CreateObject("Rhino4.Interface")
        print "app id = ", self._id
        time.sleep(1)
        
    #===========================================================================
    # Methods
    #===========================================================================
    def visible(self, visible=True):
        self._id.Visible = visible
        
    def get_script_object(self):
        return self._id.GetScriptObject
    
       
    #===========================================================================
    # Properties
    #=========================================================================== 
    
    #---------------------------------------------------------------------------
