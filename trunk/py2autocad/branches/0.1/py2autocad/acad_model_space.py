import py2autocad
from util import to_array
from line import Line

class AcadModelSpace(object):
    
    def __init__(self, id):
        self._id = id
    
    def AddLine(self, start_point, end_point):
        #Add a LINE in ModelSpace
        id = self._id.AddLine(to_array(start_point), to_array(end_point))
        return Line(id)