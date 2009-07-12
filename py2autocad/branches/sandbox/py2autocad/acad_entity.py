from acad_object import _AcadObject
import exceptions
from util import _to_array

class _AcadEntity(_AcadObject):
    """Abstract base class for an AutoCAD Entity"""
    #===========================================================================
    # Constructor
    #===========================================================================
    def __init__(self):
        exceptions.Exception("This class cannot be instantiated")  
    #===========================================================================
    # Methods
    #===========================================================================
    def array_polar(self, number_of_objects, angle_to_fill, center_point):
        """Creates an array of selected objects in a polar pattern."""
        raise exceptions.NotImplementedError()
    def array_rectangular(self, number_of_rows, number_of_columns, number_of_levels, dist_between_rows, dist_between_cols, dist_between_levels):
        """Creates an array of selected objects in a rectangular pattern."""
        raise exceptions.NotImplementedError()
    def highlight(self, highlight_flag):
        """Highlights the entity object."""
        self._id.Highlight(highlight_flag)
    def copy(self):
        """Copies the entity object."""
        return self.__class__(self._id.Copy())
    def move(self, from_point, to_point):
        """Moves the entity object from source to destination."""
        self._id.Move(_to_array(from_point), _to_array(to_point)) 
    def rotate(self, base_point, rotation_angle):
        """Rotates the entity object about a point."""
        self._id.Rotate(_to_array(base_point), rotation_angle) 
    def rotate_3d(self, point_1, point_2, rotation_angle):
        """Rotates the entity object about a 3D line."""
        self._id.Rotate3D(_to_array(point_1), _to_array(point_2), rotation_angle) 
    def mirror(self, point_1, point_2):
        """Mirrors selected objects about a line."""
        return self.__class__(self._id.Mirror(_to_array(point_1), _to_array(point_2))) 
    def mirror_3d(self, point_1, point_2, point_3):
        """Mirrors selected objects about a plane defined by three points."""
        return self.__class__(self._id.Mirror3D(_to_array(point_1), _to_array(point_2), _to_array(point_3)))
    def scale_entity(self, base_point, scale_factor):
        """Scale the entity object with respect to the base point and the scale factor."""
        self._id.ScaleEntity(_to_array(base_point), scale_factor)  
    def transform_by(self, transformation_matrix):
        """Performs the specified transformation on the entity object."""
        #TODO:test how this matrix works
        self._id.TransformBy(transformation_matrix)  
    def update(self):
        """Updates the graphics of the entity object."""
        self._id.Update()  
    def get_bounding_box(self):
        """Returns the min and max point of the bounding box of the entity object."""
        return self._id.getBoundingBox()
    def intersect_with(self, intersect_object, option):
        """Intersects with the input entity object."""
        raise exceptions.NotImplementedError()
    #===========================================================================
    # Properties
    #===========================================================================
    def _get_true_color(self):
        #TODO: wrap the return value as a AcadAcCmColor object
        return self._id.Color
    def _set_true_color(self, color):
        self._id.Color = color     
    true_color = property(
                fget=_get_true_color, 
                fset=_set_true_color, 
                doc="The true color of the object")    
    #---------------------------------------------------------------------------
    def _get_layer(self):
        return self._id.Layer
    def _set_layer(self, layer):
        self._id.Layer = layer     
    layer = property(
                fget=_get_layer, 
                fset=_set_layer, 
                doc="The current layer of the object")       
    #---------------------------------------------------------------------------
    def _get_linetype(self):
        return self._id.Linetype
    def _set_linetype(self, linetype):
        self._id.Linetype = linetype
    linetype = property(
                fget=_get_linetype, 
                fset=_set_linetype, 
                doc="The current linetype of the object")    
    #---------------------------------------------------------------------------
    def _get_linetype_scale(self):
        return self._id.LinetypeScale
    def _set_linetype_scale(self, linetype_scale):
        self._id.LinetypeScale = linetype_scale
    linetype_scale = property(
                fget=_get_linetype_scale, 
                fset=_set_linetype_scale, 
                doc="The linetype scale factor of the object")      
    #---------------------------------------------------------------------------
    def _get_visible(self):
        return self._id.Visible
    def _set_visible(self, visible):
        self._id.Visible = visible 
    visible = property(
                fget=_get_visible, 
                fset=_set_visible, 
                doc="The visibility of an object or the application")     
    #---------------------------------------------------------------------------
    def _get_plot_style_name(self):
        return self._id.PlotStyleName
    def _set_plot_style_name(self, plot_style_name):
        self._id.PlotStyleName = plot_style_name
    plot_style_name = property(
                fget=_get_plot_style_name, 
                fset=_set_plot_style_name, 
                doc="The plotstyle name for the object")    
    #---------------------------------------------------------------------------
    def _get_lineweight(self):
        return self._id.Lineweight
    def _set_lineweight(self, lineweight):
        self._id.Lineweight = lineweight
    lineweight = property(
                fget=_get_lineweight, 
                fset=_set_lineweight, 
                doc="The lineweight for the object")     
    #---------------------------------------------------------------------------
    def _get_hyperlinks(self):
        return self._id.Hyperlinks
    hyperlinks = property(
                fget=_get_hyperlinks, 
                doc="Assigns a hyperlink to an object and displays the hyperlink name or description (if one is specified)") 
    #---------------------------------------------------------------------------
    def _get_material(self):
        return self._id.Material
    def _set_material(self, material):
        self._id.Material = material
    material = property(
                fget=_get_material, 
                fset=_set_material, 
                doc="The material of the object")            
    #---------------------------------------------------------------------------
    def _get_entity_name(self):
        return self._id.EntityName   
    entity_name = property(
                fget=_get_entity_name, 
                doc="The class name of the object")   
    #---------------------------------------------------------------------------
    def _get_entity_type(self):
        return self._id.EntityType   
    entity_type = property(
                fget=_get_entity_type, 
                doc="The entity type of the object as an integer")       
    #---------------------------------------------------------------------------
    #TODO: check why this color property is set as hidden
    def _get_color(self):
        return self._id.color
    def _set_color(self, color):
        self._id.color = color
    color = property(
                fget=_get_color, 
                fset=_set_color, 
                doc="The color of the object objects")
    #---------------------------------------------------------------------------  
    
    