import py2autocad
from util import to_array
from line import Line

class ModelSpace(object):
    
    def __init__(self):
        pass
    
    def AddLine(self, start_point, end_point):
        #Add a LINE in ModelSpace
        id = py2autocad.ms.AddLine(to_array(start_point), to_array(end_point))
        return Line(id)