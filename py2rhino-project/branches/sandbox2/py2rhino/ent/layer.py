import pythoncom
from py2rhino import _base

#The following functions were not included here:
#CurrentLayer - with no arg
#IsLayer
#LayerCount
#LayerNames



class _LayerModf(object):
    
    
    def delete(self):
        """ Removes an empty layer.
        
        The layer to be removed cannot be the current layer.  Unlike the PurgeLayer method,  the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.
        
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

        Removes an existing layer from the document.  Unlike the DeleteLayer method, PurgeLayer will remove the layer even if contains geometry objects.  The layer to be removed cannot be the current layer.  
        
        Parameters
        ==========
        None

        Returns
        =======
        boolean - True or false indicating success or failure.
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
        boolean - True or false indicating success or failure.
        None - On error.

        Rhinoscript
        ===========
        This function calls the Rhinoscript function: CurrentLayer

        
        """
        name = _base._rsf.current_layer(self._layer._name)
        if name:
            return True
        else:
            return None
    
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
        This function calls the Rhinoscript function: RenameGroup

        
        """
        name = _base._rsf.rename_layer(self._layer._name)
        if name:
            self._layer._name = name
            return name
        else:
            return None  
    
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
    
    pass
    
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
        name = _base._rsf.current_layer(self._layer._name)
        if name:
            return True
        else:
            return None
    
class Layer(object):
    #--------------------------------------------------------------------------
    # nested classes to hold methods
    class modf(_LayerModf):
        def __init__(self, _group):
            self._group = _group
    class test(_LayerTest):
        def __init__(self, _group):
            self._group = _group            
    class dspl(_LayerDspl):
        def __init__(self, _group):
            self._group = _group
    class prop(_LayerProp):
        def __init__(self, _group):
            self._group = _group
            
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


    

    

    

    

    
