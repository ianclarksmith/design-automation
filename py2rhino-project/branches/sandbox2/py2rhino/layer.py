# Auto-generated wrapper for Rhino4 RhinoScript functions

import exceptions
import pythoncom
import py2rhino
from py2rhino._util import *
from py2rhino._rhinoscript import IRhinoScript

class Layer(IRhinoScript):

    # Class constructor
    def __init__(self):
        if py2rhino._rso is None:
            raise exceptions.Exception
        # initialisation code coped from win32com.client.DispatchBaseClass
        oobj = py2rhino._rso
        oobj = oobj._oleobj_.QueryInterface(self.CLSID, pythoncom.IID_IDispatch)
        self.__dict__["_oleobj_"] = oobj

    def add_layer(self, layer=None, color=None, visible=None, locked=None, parent=None):
        """        
        Adds a new layer to the document.
    
        Parameters
        ==========

        layer, String, Optional        
        The name of the new layer.  If omitted, Rhino automatically generates the layer name.
            
        color, Integer, Optional        
        A Red-Green-Blue color value.  If omitted, the color Black is assigned.
            
        visible, Boolean, Optional        
        The layer's visibility. The default is visible (True).
            
        locked, Boolean, Optional        
        The layer's locked state. The default is not locked (False).
            
        parent, String, Optional        
        The name of the new layer's parent layer. If omitted, the new layer will have not parent layer.
            
        Returns
        =======

        string
        The name of the new layer if successful.

        null
        If not successful, or on error.

        """

        params = [layer, color, visible, locked, parent]
        required = [False, False, False, False, False]
        magic = [(VT_BSTR, 1), (VT_I4, 1), (VT_BOOL, 1), (VT_BOOL, 1), (VT_BSTR, 1)]
        flattened = [layer, color, visible, locked, parent]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(3, 1, (VT_VARIANT, 0), magic, u"AddLayer", None, *flattened)

    def current_layer(self, layer=None):
        """        
        Returns or changes the current layer.
    
        Parameters
        ==========

        layer, String, Optional        
        The name of an existing layer to make current.
            
        Returns
        =======

        string
        If a layer name is not specified, the name of the current layer if successful.

        string
        If a layer name is specified, the name of the previous current layer if successful.

        null
        If not successful, or on error.

        """

        params = [layer]
        required = [False]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(5, 1, (VT_VARIANT, 0), magic, u"CurrentLayer", None, *flattened)

    def delete_layer(self, layer):
        """        
        Removes an existing layer from the document.  The layer to be removed cannot be the current layer.  Unlike the PurgeLayer method,  the layer must be empty, or contain no objects, before it can be removed. Any layers that are children of the specified layer will also be removed if they are also empty.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an empty layer.
            
        Returns
        =======

        boolean
        True or false indicating success or failure.

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(4, 1, (VT_VARIANT, 0), magic, u"DeleteLayer", None, *flattened)

    def expand_layer(self, layer, expand):
        """        
        Expands a layer. Expanded layers can be viewed in Rhino's Layer dialog.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer to expand.
            
        expand, Boolean, Required        
        True to expand, False to collapse.
            
        Returns
        =======

        boolean
        True or False indicating success or failure.

        null
        On error.

        """

        params = [layer, expand]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [layer, expand]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(690, 1, (VT_VARIANT, 0), magic, u"ExpandLayer", None, *flattened)

    def is_layer(self, layer):
        """        
        Verifies the existence of a layer in the document.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(6, 1, (VT_VARIANT, 0), magic, u"IsLayer", None, *flattened)

    def is_layer_changeable(self, layer):
        """        
        Verifies that the objects on a layer can be changed (normal).
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(18, 1, (VT_VARIANT, 0), magic, u"IsLayerChangeable", None, *flattened)

    def is_layer_child_of(self, layer, test):
        """        
        Verifies that a layer is a child of another layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer to test against.
            
        test, String, Required        
        The name of the layer to test
            
        Returns
        =======

        boolean
        True if strTest is a child of strLayer. False otherwise.

        null
        On error.

        """

        params = [layer, test]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [layer, test]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(692, 1, (VT_VARIANT, 0), magic, u"IsLayerChildOf", None, *flattened)

    def is_layer_current(self, layer):
        """        
        Verifies that a layer is the current layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(313, 1, (VT_VARIANT, 0), magic, u"IsLayerCurrent", None, *flattened)

    def is_layer_empty(self, layer):
        """        
        Verifies that an existing layer is empty, or contains no objects.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(7, 1, (VT_VARIANT, 0), magic, u"IsLayerEmpty", None, *flattened)

    def is_layer_expanded(self, layer):
        """        
        Verifies that a layer is expanded. Expanded layers can be viewed in Rhino's Layer dialog.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer to test.
            
        Returns
        =======

        boolean
        True if expanded, False if collapsed.

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(689, 1, (VT_VARIANT, 0), magic, u"IsLayerExpanded", None, *flattened)

    def is_layer_locked(self, layer):
        """        
        Verifies that an existing layer is locked.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(8, 1, (VT_VARIANT, 0), magic, u"IsLayerLocked", None, *flattened)

    def is_layer_on(self, layer):
        """        
        Verifies that an existing layer is on.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(9, 1, (VT_VARIANT, 0), magic, u"IsLayerOn", None, *flattened)

    def is_layer_parent_of(self, layer, test):
        """        
        Verifies that a layer is a parent of another layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer to test against.
            
        test, String, Required        
        The name of the layer to test
            
        Returns
        =======

        boolean
        True if strTest is a parent of strLayer. False otherwise.

        null
        On error.

        """

        params = [layer, test]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [layer, test]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(693, 1, (VT_VARIANT, 0), magic, u"IsLayerParentOf", None, *flattened)

    def is_layer_reference(self, layer):
        """        
        Verifies that an existing layer is from a reference file.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(10, 1, (VT_VARIANT, 0), magic, u"IsLayerReference", None, *flattened)

    def is_layer_selectable(self, layer):
        """        
        Verifies that an existing layer is selectable (normal and reference).
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(19, 1, (VT_VARIANT, 0), magic, u"IsLayerSelectable", None, *flattened)

    def is_layer_visible(self, layer):
        """        
        Verifies that an existing layer is visible (normal, locked,  and reference).
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(20, 1, (VT_VARIANT, 0), magic, u"IsLayerVisible", None, *flattened)

    def layer_child_count(self, layer):
        """        
        Returns the number of immediate child layers of a layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer.
            
        Returns
        =======

        number
        The number of immediate child layers if successful

        null
        On error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(694, 1, (VT_VARIANT, 0), magic, u"LayerChildCount", None, *flattened)

    def layer_children(self, layer):
        """        
        Returns the immediate child layers of a layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer.
            
        Returns
        =======

        array
        An array of strings identifying the layer's children if successful

        null
        If the layer has no children, or on error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(691, 1, (VT_VARIANT, 0), magic, u"LayerChildren", None, *flattened)

    def layer_color(self, layer, color=None):
        """        
        Returns or changes the color of a layer.  Layer colors are represented as RGB colors.  An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be displayed.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        color, Integer, Optional        
        The new color value.  If omitted, the current layer color is returned.
            
        Returns
        =======

        number
        If a color value  is not specified,  the current color value if successful.

        number
        If a color value is specified, the previous color value if successful.

        null
        If not successful, or on error.

        """

        params = [layer, color]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I4, 1)]
        flattened = [layer, color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(11, 1, (VT_VARIANT, 0), magic, u"LayerColor", None, *flattened)

    def layer_count(self):
        """        
        Returns the number of layers in the document.
    
        No parameters

        Returns
        =======

        number
        The number of layers in the document.

        """

        params = []
        required = []
        magic = []
        flattened = []

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(12, 1, (VT_VARIANT, 0), magic, u"LayerCount", None, *flattened)

    def layer_linetype(self, layer, linetype=None):
        """        
        Returns or changes the linetype of a layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        linetype, String, Optional        
        The name of the new linetype.
            
        Returns
        =======

        string
        If a linetype is not specified,  the name of the current linetype if successful.

        string
        If a linetype is specified, the name of the previous linetype if successful.

        null
        If not successful, or on error.

        """

        params = [layer, linetype]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [layer, linetype]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(602, 1, (VT_VARIANT, 0), magic, u"LayerLinetype", None, *flattened)

    def layer_locked(self, layer, visible=None):
        """        
        Returns or changes the locked mode of a layer. This method should be use instead of LayerMode.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        visible, Boolean, Optional        
        The new layer locked mode.  True = Locked, False = Unlocked.
            
        Returns
        =======

        boolean
        If a layer mode is not specified,  the current layer locked mode if successful.

        boolean
        If a layer mode is specified, the previous layer locked mode if successful.

        null
        If not successful, or on error.

        """

        params = [layer, visible]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [layer, visible]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(601, 1, (VT_VARIANT, 0), magic, u"LayerLocked", None, *flattened)

    def layer_material_index(self, layer):
        """        
        Returns the material index of a layer.  A material index of -1 indicates that no material has been assigned to the layer.  Thus, the layer will use Rhino's default layer material.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        number
        A zero-based material index if successful.

        null
        If not successful, or on error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(13, 1, (VT_VARIANT, 0), magic, u"LayerMaterialIndex", None, *flattened)

    def layer_mode(self, layer, mode=None):
        """        
        OBSOLETE, use either LayerLocked or LayerVisible instead.
		Returns or changes the mode of a layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        mode, Integer, Optional        
        The new layer mode.  The layer modes are as follows:
		Value
		Description
		0
		Normal.  The layer is visible, and objects on the layer can be selected and changed. (Visible and Unlocked)
		1
		Hidden.  The layer is not visible, and objects on the layer cannot be selected or changed. (Hidden and Unlocked)
		2
            
        Returns
        =======

        number
        If a layer mode is not specified,  the current layer mode  if successful.

        number
        If a layer mode is specified, the previous layer mode if successful.

        null
        If not successful, or on error.

        """

        params = [layer, mode]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I2, 1)]
        flattened = [layer, mode]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(14, 1, (VT_VARIANT, 0), magic, u"LayerMode", None, *flattened)

    def layer_names(self, sort=None):
        """        
        Returns the names of all layers in the document.
    
        Parameters
        ==========

        sort, Boolean, Optional        
        Return a sorted list of layer names. The default is not to return a sorted list (False).
            
        Returns
        =======

        array
        An array of layer names if successful.

        null
        If not successful, or on error.

        """

        params = [sort]
        required = [False]
        magic = [(VT_BOOL, 1),]
        flattened = [sort]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(15, 1, (VT_VARIANT, 0), magic, u"LayerNames", None, *flattened)

    def layer_order(self, layer):
        """        
        Returns the current display order index of a layer as displayed in Rhino's Layer dialog box.  A display order index of -1 indicates that the current Layer dialog filter does not allow the layer to appear in the layer list.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        Returns
        =======

        number
        A zero-based display order index if successful.

        null
        If not successful, or on error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(17, 1, (VT_VARIANT, 0), magic, u"LayerOrder", None, *flattened)

    def layer_print_color(self, layer, color=None):
        """        
        Returns or changes the print color of a layer. Layer print colors are represented as RGB colors. An RGB color specifies the relative intensity of red, green, and blue to cause a specific color to be printed.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        color, Integer, Optional        
        The new print color value.  If omitted, the current layer print color is returned.
            
        Returns
        =======

        number
        If a layer print color is not specified,  the current layer print color if successful.

        number
        If a layer print color is specified, the previous layer print color if successful.

        null
        If not successful, or on error.

        """

        params = [layer, color]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_I4, 1)]
        flattened = [layer, color]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(603, 1, (VT_VARIANT, 0), magic, u"LayerPrintColor", None, *flattened)

    def layer_print_width(self, layer, width=None):
        """        
        Returns or changes the print width of a layer. Print width is specified in millimeters. A print width of 0.0 denotes the "default" print width.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        width, Double, Optional        
        The new layer print width in millimeters.
            
        Returns
        =======

        number
        If a layer print width is not specified,  the current layer print width if successful.

        number
        If a layer print width is specified, the previous layer print width if successful.

        null
        If not successful, or on error.

        """

        params = [layer, width]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_R8, 1)]
        flattened = [layer, width]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(604, 1, (VT_VARIANT, 0), magic, u"LayerPrintWidth", None, *flattened)

    def layer_visible(self, layer, visible=None):
        """        
        Returns or changes the visibility property of a layer. This method should be use instead of LayerMode.
    
        Parameters
        ==========

        layer, String, Required        
        The name of an existing layer.
            
        visible, Boolean, Optional        
        The new layer visibility.  True = Visible, False = Hidden.
            
        Returns
        =======

        boolean
        If a layer mode is not specified,  the current layer visibility if successful.

        boolean
        If a layer mode is specified, the previous layer visibility if successful.

        null
        If not successful, or on error.

        """

        params = [layer, visible]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BOOL, 1)]
        flattened = [layer, visible]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(600, 1, (VT_VARIANT, 0), magic, u"LayerVisible", None, *flattened)

    def parent_layer(self, layer, parent=None):
        """        
        Returns or modifies the parent layer of a layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer.
            
        parent, String, Optional        
        The name of the new parent layer. To remove the parent layer, thus making a root-level layer, specify either Null or an empty string, or "".
            
        Returns
        =======

        string
        If strParent is not specified, the name of the current parent layer if successful.

        string
        If strParent is specified, the name of the previous parent layer if successful.

        null
        If the layer does not have a parent, or on error.

        """

        params = [layer, parent]
        required = [True, False]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [layer, parent]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(688, 1, (VT_VARIANT, 0), magic, u"ParentLayer", None, *flattened)

    def purge_layer(self, layer):
        """        
        Removes an existing layer from the document.  Unlike the DeleteLayer method, PurgeLayer will remove the layer even if contains geometry objects.  The layer to be removed cannot be the current layer.
    
        Parameters
        ==========

        layer, String, Required        
        The name of the layer to purge.
            
        Returns
        =======

        string
        The name of the purged layer if successful.

        null
        If not successful, or on error.

        """

        params = [layer]
        required = [True]
        magic = [(VT_BSTR, 1),]
        flattened = [layer]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(291, 1, (VT_VARIANT, 0), magic, u"PurgeLayer", None, *flattened)

    def rename_layer(self, old_name, new_name):
        """        
        Renames an existing layer.
    
        Parameters
        ==========

        old_name, String, Required        
        The name of an existing layer.
            
        new_name, String, Required        
        The new layer name.
            
        Returns
        =======

        string
        The new layer name if successful.

        null
        If not successful, or on error.

        """

        params = [old_name, new_name]
        required = [True, True]
        magic = [(VT_BSTR, 1), (VT_BSTR, 1)]
        flattened = [old_name, new_name]

        magic, flattened = select_params(params, required, magic, flattened)

        return self._ApplyTypes_(16, 1, (VT_VARIANT, 0), magic, u"RenameLayer", None, *flattened)

