import pythoncom
from py2rhino import _base

#The following functions were not included here:
#CurrentLayer - with no arg
#IsLayer - should be implemented in object_types
#LayerCount - should be implemented in object_types
#LayerNames - should be implemented in object_types



class _LayerModf(object):
    
    
    def delete(self):
        """ Removes an empty layer.
        
        The layer to be removed cannot be the current layer.  Unlike the purge_layer method,  the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: DeleteLayer

        
        """
        return _base._rsf.delete_layer(self._layer._name)
    
    def purge(self):
        """ Removes an existing layer.

        Removes an existing layer from the document.  Unlike the delete_layer method, purge_layer will remove the layer even if contains geometry objects.  The layer to be removed cannot be the current layer.  
        
        Parameters
        ==========
        None

        Returns
        =======
        String - The name of the purged layer if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: PurgeLayer

        
        """
        return _base._rsf.purge_layer(self._layer._name)
    
    
    
class _LayerProp(object):
    #LayerChildCount
    #LayerChildren
    
    def make_current(self):
        """ Changes the current layer.

        
        Returns or changes the current layer.
        
        Parameters
        ==========
        None

        Returns
        =======
        String - If a layer name is not specified, the name of the current layer if successful.
        String - If a layer name is specified, the name of the previous current layer if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurrentLayer

        
        """
        return _base._rsf.current_layer(self._layer._name)
    
    def name(self, name):
        """ Returns the name of the layer.
        
        Returns the name of the layer.
        
        Parameters
        ==========
        None

        Returns
        =======
        string - The layer name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        None

        
        """
        return self._layer._name 
    
    def rename(self, name):
        """ Renames a layer.
        
        Renames the layer. The new name must be unique.
        
        Parameters
        ==========
        name (string, Required) - The new name of the layer.

        Returns
        =======
        string - The new layer name if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: RenameLayer

        
        """
        name = _base._rsf.rename_layer(self._layer._name, name)
        if name:
            self._layer._name = name
            return name
        else:
            return None  
    
    def child_count(self):
        """ Returns the number of immediate child layers of a layer.
        
        Returns the number of immediate child layers of a layer.
        
        Parameters
        ==========
        None

        Returns
        =======
        int - The number of immediate child layers if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerChildCount

        
        """
        return _base._rsf.layer_child_count(self._layer._name)
    
    def children(self):
        """ Returns the immediate child layers of a layer.
        
        Returns the immediate child layers of a layer.
        
        Parameters
        ==========
        None

        Returns
        =======
        List - An array of strings identifying the layer's children if successful
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerChildren

        
        """
        return _base._rsf.layer_children(self._layer._name)
        
class _LayerTest(object):
    
    #IsLayerChangeable
    #IsLayerChildOf
    #IsLayerCurrent
    #IsLayerEmpty
    #IsLayerExpanded
    #IsLayerOn
    #IsLayerParentOf
    #IsLayerReference
    #IsLayerSelectable
    #IsLayerVisible
    #IsLayerLocked
    
    def is_changeable(self):
        """ Verifies that the objects on a layer can be changed (normal).
        
        Verifies that the objects on a layer can be changed (normal).
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if successful. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerChangeable

        
        """
        return _base._rsf.is_layer_changeable(self._layer._name)
    
    def is_child_of(self,test):
        """ Returns the layer is a child of another layer.
        
        Returns the layer is a child of another layer.
        
        Parameters
        ==========
        test (string, Required) - The name of the layer to test

        Returns
        =======
        boolean - True if strTest is a child of strLayer. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerChildOf

        
        """
        return _base._rsf.is_layer_child_of(self._layer._name,test)
            
    def is_current(self):
        """ 
        
        Verifies that a layer is the current layer.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if successful. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerCurrent

        
        """
        return _base._rsf.is_layer_current(self._layer._name)
            
    def is_empty(self):
        """ 
        
        Verifies that an existing layer is empty, or contains no objects.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if successful. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerEmpty

        
        """
        return _base._rsf.is_layer_empty(self._layer._name)
            
    def is_expanded(self):
        """ 
        
        Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's Layer dialog.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if expanded, False if collapsed.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerExpanded

        
        """
        return _base._rsf.is_layer_expanded(self._layer._name)
            
    def is_on(self):
        """ 
        
        Verifies that an existing layer is on.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if there is an existing layer is on, False if collapsed.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerOn

        
        """
        return _base._rsf.is_layer_on(self._layer._name)
            
    def is_parent_of(self,test):
        """ 
        
        Verifies that a layer is a parent of another layer.
        
        Parameters
        ==========
        test (string, Required) - The name of the layer to test.

        Returns
        =======
        boolean - True if test is a parent of strLayer. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerParentOf

        
        """
        return _base._rsf.is_layer_parent_of(self._layer._name,test)
            
    def is_reference(self):
        """ 
        
        Verifies that an existing layer is from a reference file.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if an existing layer is from a reference file. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerReference

        
        """
        return _base._rsf.is_layer_reference(self._layer._name)
            
    def is_selectable(self):
        """ 
        
        Verifies that an existing layer is selectable (normal and reference).
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if an existing layer is selectable. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerSelectable

        
        """
        return _base._rsf.is_layer_selectable(self._layer._name)    
            
    def is_visible(self):
        """ 
        
        Verifies that an existing layer is visible (normal, locked,  and reference).
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if an existing layer is visible. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerVisible

        
        """
        return _base._rsf.is_layer_visible(self._layer._name)    
            
    def is_locked(self):
        """ 
        
        Verifies that an existing layer is locked.
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True if an existing layer is locked. False otherwise.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: IsLayerLocked

        
        """
        return _base._rsf.is_layer_locked(self._layer._name)    
    
class _LayerDspl(object):
    
    #LayerColor
    #LayerLinetype
    #LayerMaterialIndex
    #LayerMode
    #LayerOrder
    #LayerPrintColor
    #LayerPrintWidth
    #LayerVisible
    #LayerLocked
    
    
    def expand(self, expand):
        """
        
        Expands a layer. Expanded layers can be viewed in Rhino's Layer dialog.
        
        Parameters
        ==========
        expand (boolean, Required) - True to expand, False to collapse.
 
        Returns
        =======
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: ExpandLayer

        
        """
        return _base._rsf.expand_layer(self._layer._name, expand)

    def color(self,color=pythoncom.Empty):
        """
        
        Returns or changes the color of a layer.  Layer colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed. 

        Parameters
        ==========
        color (int, Optional) -  The new color value.  If omitted, the current layer color is returned.
 
        Returns
        =======
        int - If a color value  is not specified,  the current color value if successful.
        int - If a color value is specified, the previous color value if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerColor
        
        """
        
        return _base._rsf.layer_color(self._layer._name, color)
    
    def line_type(self,line_type=pythoncom.Empty):
        """
        
        Returns or changes the linetype of a layer.
        
        Parameters
        ==========
        line_type (string, Optional) -  The name of the new linetype.
 
        Returns
        =======
        String - If a linetype is not specified,  the name of the current linetype if successful.
        String - If a linetype is specified, the name of the previous linetype if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerLinetype
        
        """
        
        return _base._rsf.layer_linetype(self._layer._name, line_type)
    
    def material_index(self):
        """
        Parameters
        ==========
        None
 
        Returns
        =======
        int - A zero-based material index if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerMaterialIndex
        
        """
        
        return _base._rsf.layer_material_index(self._layer._name)
        
    def mode(self,mode=pythoncom.Empty):
        """
        Parameters
        ==========
        mode (int, Optional) -  The new layer mode.  The layer modes are listed in the table for mode.
    
        Table: mode
        Value, Description
        0, Normal - The layer is visible, and objects on the layer can be selected and changed. (Visible and Unlocked)
        1, Hidden - The layer is not visible, and objects on the layer cannot be selected or changed. (Hidden and Unlocked)
        2, Locked - The layer is visible, but objects on the layer cannot be selected or changed. (Visible and Locked)
 
        Returns
        =======
        int - If a layer mode is not specified,  the current layer mode  if successful.
        int - If a layer mode is specified, the previous layer mode if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerMode
        
        """
        
        return _base._rsf.layer_mode(self._layer._name,mode)
            
    def order(self):
        """
        Parameters
        ==========
        None
        
        Returns
        =======
        int - A zero-based display order index if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerOrder
        
        """
        
        return _base._rsf.layer_order(self._layer._name)
            
    def print_color(self, color=pythoncom.Empty):
        """
        
        Returns or changes the print color of a layer. Layer print colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be printed. 
        
        Parameters
        ==========
        color (int, Optional) The new print color value.  If omitted, the current layer print color is returned.
        
        Returns
        =======
        int - If a layer print color is not specified,  the current layer print color if successful.
        int - If a layer print color is specified, the previous layer print color if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerPrintColor
        
        """
        
        return _base._rsf.layer_print_color(self._layer._name,color)
            
    def print_width(self, width=pythoncom.Empty):
        """
        
        Returns or changes the print width of a layer. Print width is specified in millimeters. A print width of 0.0 denotes the "default" print width.
        
        Parameters
        ==========
        width (int, Optional) - The new layer print width in millimeters.
        
        Returns
        =======
        float - If a layer print width is not specified,  the current layer print width if successful.
        float - If a layer print width is specified, the previous layer print width if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerPrintWidth
        
        """
        
        return _base._rsf.layer_print_width(self._layer._name,width)
            
    def visible(self, visible=pythoncom.Empty):
        """
        
        Returns or changes the visibility property of a layer.
        
        Parameters
        ==========
        visible (boolean, Optional) - The new layer visibility.  True = Visible, False = Hidden.
        
        Returns
        =======
        Boolean - If a layer mode is not specified,  the current layer visibility if successful.
        Boolean - If a layer mode is specified, the previous layer visibility if successful.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerVisible
        
        """
        
        return _base._rsf.layer_visible(self._layer._name,visible)
            
    def locked(self, visible=pythoncom.Empty):
        """
        
        Returns or changes the locked mode of a layer
        
        Parameters
        ==========
        visible (boolean, Optional) - The new layer locked mode.  True = Locked, False = Unlocked.
        
        Returns
        =======
        Boolean - If a layer mode is not specified,  the current layer locked mode if successful.
        Boolean - If a layer mode is specified, the previous layer locked mode if successful.W
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: LayerLocked
        
        """
        
        return _base._rsf.layer_locked(self._layer._name,visible)
    
class Layer(object):
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    class modf(_LayerModf):
        def __init__(self, _layer):
            self._layer = _layer
    class test(_LayerTest):
        def __init__(self, _layer):
            self._layer = _layer            
    class dspl(_LayerDspl):
        def __init__(self, _layer):
            self._layer = _layer
    class prop(_LayerProp):
        def __init__(self, _layer):
            self._layer = _layer
            
    #--------------------------------------------------------------------------
    # Class constructor
    def __init__(self, name):
        if name==None:
            raise Exception("Use the create... methods to create instances of this class.")
        self._name = name
        
        #create instances of the nested classes
        self.modf = Layer.modf(self)
        self.test = Layer.test(self)
        self.dspl = Layer.dspl(self)
        self.prop = Layer.prop(self)   
        
    #--------------------------------------------------------------------------
    @staticmethod
    def create(name=pythoncom.Empty, color=pythoncom.Empty, visible=pythoncom.Empty, locked=pythoncom.Empty, parent=pythoncom.Empty):
        """ Adds a new layer.

        Factory method:
        Adds a new layer to the document. Each layer must have a unique name.

        Parameters
        ==========
        name (String, Optional) - The name of the new layer.  If omitted, Rhino automatically generates the layer name.
        color (list of integer, Optional)  - A Red-Green-Blue color value.  If omitted, the color Black is assigned.
        visible (boolean, Optional)  -  The layer's visibility. The default is visible (True).
        locked (boolean, Optional)  - The layer's locked state. The default is not locked (False).
        parent (layer, Optional)  - The name of the new layer's parent layer. If omitted, the new layer will have not parent layer.
 
        Returns
        =======
        String - The name of the new layer if successful.
        None - If not successful, or on error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: AddLayer

        
        """
        if parent != pythoncom.Empty:
            parent = parent._name
        name = _base._rsf.add_layer(name, color, visible, locked, parent)
        if name:
            return Layer(name)
        else:
            return None
        

    

    

    

    

    
