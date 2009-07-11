from acad_entity import _AcadEntity
import exceptions
from util import to_array

class AcadLine(_AcadEntity):
    """AutoCAD Line"""
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self, id):
        self._id = id
    #===========================================================================
    # Methods: Class IAcadLine
    #===========================================================================
    def offset(self, distance):
        """Creates a new line by offsetting the current line by a specified distance"""
        return Line(self._id.Offset(distance))
    #===========================================================================
    #    Properties:  IAcadLine
    #===========================================================================
    def _get_start_point(self):
        return self._id.GetStartPoint()
    def _set_start_point(self, start_point):
        self._id.SetStartPoint(to_array(start_point))
    start_point = property(
                fget=_get_start_point, 
                fset=_set_start_point, 
                doc="The X, Y, Z coordinate of the start point of the line or use the Pick Point button to set X, Y, Z values simultaneously")    
    #---------------------------------------------------------------------------
    def _get_end_point(self):
        return self._id.GetEndPoint()
    def _set_end_point(self, end_point):
        self._id.SetEndPoint(to_array(end_point))  
    end_point = property(
                fget=_get_end_point, 
                fset=_set_end_point, 
                doc="The X, Y, Z coordinate of the end point of the line or use the Pick Point button to set X, Y, Z values simultaneously")    
    #---------------------------------------------------------------------------
    def _get_normal(self):
        return self._id.GetNormal()
    def _set_normal(self, normal):
        self._id.SetNormal(to_array(normal))     
    normal = property(
                fget=_get_normal, 
                fset=_set_normal, 
                doc="The three-dimensional normal unit vector for the entity")    
    #---------------------------------------------------------------------------
    def _get_thickness(self):
        return self._id.GetThickness()
    def _set_thickness(self, thickness):
        self._id.SetThickness(to_array(thickness))  
    thickness = property(
                fget=_get_thickness, 
                fset=_set_thickness, 
                doc="The thickness of the line")    
    #---------------------------------------------------------------------------
    def _get_delta(self):
        return self._id.GetDelta()  
    delta = property(
                fget=_get_delta, 
                doc="The delta of the line")       
    #---------------------------------------------------------------------------
    def _get_length(self):
        return self._id.GetLength()
    length = property(
                fget=_get_length, 
                doc="The length of the line")    
    #---------------------------------------------------------------------------
    def _get_angle(self):
        return self._id.GetAngle()
    angle = property(
                fget=_get_angle, 
                doc="The angle of the line")     
    #---------------------------------------------------------------------------


    








    