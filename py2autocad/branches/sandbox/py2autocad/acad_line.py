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
    # Methods
    #===========================================================================
    def offset(self, distance):
        """Creates a new line by offsetting the current line by a specified distance"""
        #return AcadLine(self._id.Offset(distance))
        raise exceptions.NotImplementedError()
    #===========================================================================
    # Properties
    #===========================================================================
    def _get_start_point(self):
        return self._id.StartPoint
    def _set_start_point(self, start_point):
        self._id.StartPoint = to_array(start_point)
    start_point = property(
                fget=_get_start_point, 
                fset=_set_start_point, 
                doc="The X, Y, Z coordinate of the start point of the line or use the Pick Point button to set X, Y, Z values simultaneously")    
    #---------------------------------------------------------------------------
    def _get_end_point(self):
        return self._id.EndPoint
    def _set_end_point(self, end_point):
        self._id.EndPoint = to_array(end_point)  
    end_point = property(
                fget=_get_end_point, 
                fset=_set_end_point, 
                doc="The X, Y, Z coordinate of the end point of the line or use the Pick Point button to set X, Y, Z values simultaneously")    
    #---------------------------------------------------------------------------
    def _get_normal(self):
        return self._id.Normal
    def _set_normal(self, normal):
        self._id.Normal = to_array(normal)
    normal = property(
                fget=_get_normal, 
                fset=_set_normal, 
                doc="The three-dimensional normal unit vector for the entity")    
    #---------------------------------------------------------------------------
    def _get_thickness(self):
        return self._id.Thickness
    def _set_thickness(self, thickness):
        self._id.Thickness = thickness
    thickness = property(
                fget=_get_thickness, 
                fset=_set_thickness, 
                doc="The thickness of the line")    
    #---------------------------------------------------------------------------
    def _get_delta(self):
        return self._id.Delta
    delta = property(
                fget=_get_delta, 
                doc="The delta of the line")       
    #---------------------------------------------------------------------------
    def _get_length(self):
        return self._id.Length
    length = property(
                fget=_get_length, 
                doc="The length of the line")    
    #---------------------------------------------------------------------------
    def _get_angle(self):
        return self._id.Angle
    angle = property(
                fget=_get_angle, 
                doc="The angle of the line")     
    #---------------------------------------------------------------------------
