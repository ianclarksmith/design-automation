from comtypes.client import GetActiveObject, CreateObject
from acad_document import AcadDocument


#THIS CLASS IS NOT COMPLETE
class AcadApplication(object):
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self):
        #TODO: this needs to be improved - e.g. what if AutoCAD is not open
        self._id = GetActiveObject("AutoCAD.Application")
    #===========================================================================
    # Methods
    #===========================================================================
    def update(self):
        """Updates the object to the drawing screen"""
        #Add a LINE in ModelSpace
        id = self._id.Update()
    #===========================================================================
    # Properties
    #=========================================================================== 
    def _get_active_document(self):
        return AcadDocument(self._id.ActiveDocument)
    active_document = property(
                fget=_get_active_document, 
                doc="The active document (drawing file)")     
    #---------------------------------------------------------------------------
