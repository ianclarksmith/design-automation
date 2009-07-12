from comtypes.client import GetActiveObject, CreateObject
from acad_model_space import AcadModelSpace

#Get running instance of the AutoCAD application


#THIS CLASS IS NOT COMPLETE
class AcadDatabase(object):
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self, id):
        self._id = id
    #===========================================================================
    # Methods
    #===========================================================================
    #===========================================================================
    # Properties
    #=========================================================================== 
    def _get_model_space(self):
        return AcadModelSpace(self._id.ModelSpace)
    model_space = property(
                fget=_get_model_space, 
                doc="The ModelSpace collection for the document")     
    #---------------------------------------------------------------------------

