from comtypes.client import GetActiveObject, CreateObject
from acad_database import AcadDatabase

#Get running instance of the AutoCAD application


#THIS CLASS IS NOT COMPLETE
class AcadDocument(AcadDatabase):
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self, id):
        self._id = id
    #===========================================================================
    # Methods
    #===========================================================================
    def regen(self, which_viewports):
        """Regenerates the entire drawing and recomputes the screen coordinates and view resolution for all objects"""
        id = self._id.Regen(which_viewports)
    #===========================================================================
    # Properties
    #=========================================================================== 
 
    #---------------------------------------------------------------------------

