import py2autocad
from util import _to_array
from acad_line import AcadLine

#THIS CLASS IS NOT COMPLETE
class AcadModelSpace(object):
    
    def __init__(self, id):
        self._id = id
    
    def add_line(self, start_point, end_point):
        #Add a LINE in ModelSpace
        id = self._id.AddLine(_to_array(start_point), _to_array(end_point))
        return AcadLine(id)
